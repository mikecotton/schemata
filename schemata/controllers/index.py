import logging
import couchdb
import simplejson

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from schemata.lib.base import BaseController, render

log = logging.getLogger(__name__)

server = couchdb.Server()
app_name = 'schemata'

class IndexController(BaseController):

    def index(self):
        c.all_tables = [i for i in server if 'app_name' in server[i]]
        c.table_ranges = {}
        c.table_indexes = {}
        for table in c.all_tables:
            c.table_ranges[table] = server[table]['data_models']['ranges']
            c.table_indexes[table] = [t for t in server[table] if t != 'data_models' and t != 'app_name']

        return render('index.mako')

    def data_entry(self):
        c.table_name = request.params.get('table_name', None)
        c.table_index = request.params.get('table_index', None)
        c.table_version = request.params.get('table_version', None)
        c.edit = request.params.get('edit', None)
        c.edited = request.params.get('edited', None)
        c.new = request.params.get('new', None)

        db = server[c.table_name]

        if c.table_name and c.table_version:
            #enter new data
            if not c.table_index and c.new =='true':
                c.category_data = db['data_models'][c.table_version] #FIXME - change 'category data' to 'axis data'
                c.table_data = {}
                return render('data_entry.mako')

            #edit existing data
            if c.table_name and c.table_index and c.table_version and c.edit == 'true':
                c.category_data = db['data_models'][c.table_version] #FIXME - change 'category data' to 'axis data'
                c.table_data = db[c.table_index]
                return render('data_entry.mako')

            #display existing data
            if not c.edited and not c.new:
                redirect = 'display_data?table_name=%s&table_version=%s&table_index=%s' % (str(c.table_name), str(c.table_version), str(c.table_index))
                return redirect_to(redirect)

        if c.table_index not in db:
            data_models = db['data_models']
            data_models['ranges'][c.table_version].append(c.table_index)

            db['data_models'] = data_models

        #refactor this to something sane - FIXME
        entered_tuples = [param for param in request.params.iteritems()
                          if param[0] != 'table_name' and
                          param[0] != 'table_index' and
                          param[0] != 'table_version' and
                          param[0] != 'new' and
                          param[0] != 'edited']


        table_data = []

        for entered_tuple in entered_tuples:
            data_dict = {}
            rows_and_columns = entered_tuple[0].split('^')

            data_dict['row_name'] = rows_and_columns[0]
            data_dict['column_name'] = rows_and_columns[1]
            data_dict['row_index'] = rows_and_columns[2]
            data_dict['column_index'] = rows_and_columns[3]
            data_dict['value'] = entered_tuple[1]

            table_data.append(data_dict)

        form_data = db.get(c.table_index, {})
        form_data['table_name'] = c.table_name
        form_data['table_index'] = c.table_index
        form_data['table_version'] = c.table_version
        form_data['data'] = table_data

        db[c.table_index] = form_data

        redirect = 'display_data?table_name=%s&table_version=%s&table_index=%s' % (str(c.table_name), str(c.table_version), str(c.table_index))
        return redirect_to(redirect)

    def display_data(self):
        c.table_name = request.params.get('table_name')
        c.table_version = request.params.get('table_version')
        c.table_index = request.params.get('table_index')

        db = server[c.table_name]
        c.category_data = db['data_models'][c.table_version]

        c.table_data = db[c.table_index]

        return render('display_data.mako')

    def csv(self):
        table_name = request.params.get('table_name')
        table_version = request.params.get('table_version')
        table_index = request.params.get('table_index')

        db = server[table_name]
        category_data = db['data_models'][table_version]
        table_data = db[table_index]

        column_string = ','.join(
            [i['name'] for i in category_data['columns']])

        csv_string = column_string + '\n'

        row_name = table_data['data'][0]['row_name']
        csv_string += row_name

        for cell in table_data['data']:
            if cell['row_name'] != row_name:
                csv_string += ('\n' + cell['row_name'])
                row_name = cell['row_name']
            csv_string += (',' + cell['value'])
        response.headers['Content-Type'] = 'application/vnd.ms-excel'
        csv_string = csv_string.encode('utf-8')
        return(csv_string)

    def new_table(self):
        c.table_name = request.params.get('table_name')
        c.table_version = request.params.get('table_version')
        c.data_model = {}

        #new table
        if c.table_name == None and c.table_version == None:
            default_table_dict = {}
            default_table_dict['index'] = '0'
            default_table_dict['name'] = ''
            default_table_dict['type'] = 'column'
            c.default_table_data = [default_table_dict]
            return render('create_new_table.mako')

        #editing a table
        elif c.table_name and c.table_version and len(request.params) == 2:
            db = server[c.table_name]
            if c.table_version in db['data_models']:
                c.data_model = db['data_models'][c.table_version]
                c.existing_rows = c.data_model.get('rows', [])
                c.x_axis_label = db['data_models'].get('x_axis_label', 'Untitled')
                c.y_axis_label = db['data_models'].get('y_axis_label', 'Untitled')

                c.existing_items = c.existing_rows
                c.existing_items.extend(c.data_model.get('columns', []))
            else:
                session['error'] = 'The table name and table version you requested could not be found.' # -- this wording sucks, FIXME

            return render('create_new_table.mako')

        c.x_axis_label = request.params.get('x_axis_label', 'Untitled')
        c.y_axis_label = request.params.get('y_axis_label', 'Untitled')

        categories = [cat for cat in request.params.iteritems() if 'element_name' in cat[0] or 'row_or_column' in cat[0]]

        category_data = {}
        columns = []
        rows = []
        category_datum = {}

        for i in range(len(categories)):
            if i % 2 == 0:
                index = i
                name = categories[i][1]
                category_type = categories[i+1][1]

                category_datum['name'] = name
                category_datum['type'] = category_type

                if 'row' in category_type:
                    if 'sub' in category_type:
                        for j in range(len(rows) -1, -1, -1):
                            comp_row = ''
                            if 'comp' not in rows[j]['type'] and 'sub' not in rows[j]['type']:
                                session['error'] = 'sub row ' + name + ' does not have a compound row associated with it.  Please correct and resubmit the table design data.'  #FIXME - get a better error message
                                session.save()
                                return redirect_to(edit_table_query_string)

                            if 'comp' in rows[j]['type']:
                                comp_row = rows[j]['name']
                                break

                        category_datum['sub_of'] = comp_row

                    category_datum['index'] = str(len(rows))
                    rows.append(category_datum)

                elif 'column' in category_type:
                    if 'sub' in category_type:
                        for j in range(len(columns) -1, -1, -1):
                            if 'comp' not in columns[j]['type'] and 'sub' not in columns[j]['type']:
                                session['error'] = 'sub column ' + name + ' does not have a compound column associated with it.  Please correct and resubmit the table design data.'  #FIXME - get a better error message
                                session.save()
                                return redirect_to(edit_table_query_string)

                            if 'comp' in columns[j]['type']:
                                comp_row = columns[j]['name']
                                break

                        category_datum['sub_of'] = comp_row

                    category_datum['index'] = str(len(columns))
                    columns.append(category_datum)

                category_datum = {}

        category_data['columns'] = columns
        category_data['rows'] = rows
        category_data['x_axis_label'] = c.x_axis_lable
        category_data['y_axis_label'] = c.y_axis_lable
        category_data['table_name'] = c.table_name
        category_data['table_version'] = c.table_version

        ## this block doesn't work -- FIXME
        if not c.table_name or not c.table_version:
            session['error'] = 'You must provide a unique table name and table version.'
            session.save()
            return redirect_to(edit_table_query_string)

        if c.table_name not in server:
            server.create(c.table_name)

        db = server[c.table_name]

        app_name_dict = db.get('app_name', {})

        if not app_name_dict:
            app_name_dict[app_name] = True
            db['app_name'] = app_name_dict

        data_models = db.get('data_models', {})

        if not data_models:
            data_models['ranges'] = {}

        if c.table_version not in data_models['ranges'].keys():
            data_models['ranges'][c.table_version] = []

        data_models[c.table_version] = category_data

        db['data_models'] = data_models

        data_entry_query_string = '/data_entry?table_name=' + c.table_name + '&table_version=' + c.table_version + '&new=true'

        return redirect_to(str(data_entry_query_string))


