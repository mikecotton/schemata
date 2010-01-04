from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260999273.858242
_template_filename='/Users/mike/schemata/schemata/templates/data_entry.mako'
_template_uri='data_entry.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<form action="/data_entry" method="POST" id="data_entry_form">\n<p>\n\n</p>\n<p>\n</p>\n<table>\n<tr><td>table name: ')
        # SOURCE LINE 10
        __M_writer(escape(c.table_name))
        __M_writer(u' </td></tr>\n<tr><td>table version: ')
        # SOURCE LINE 11
        __M_writer(escape(c.table_version))
        __M_writer(u'</td></tr>\n<tr><td>table index: <input id="table_index" name="table_index" value="')
        # SOURCE LINE 12
        __M_writer(escape(c.table_index))
        __M_writer(u'"></td></td>\n\n</table>\n\n<table border="1">\n  <tr>\n<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n\n')
        # SOURCE LINE 20
        for column in c.category_data['columns']:
            # SOURCE LINE 21
            __M_writer(u'<th> ')
            __M_writer(escape(column['name']))
            __M_writer(u' </th>\n')
        # SOURCE LINE 23
        __M_writer(u'</tr>\n')
        # SOURCE LINE 24
        for row in c.category_data['rows']:
            # SOURCE LINE 25
            __M_writer(u'<tr>\n<td>')
            # SOURCE LINE 26
            __M_writer(escape(row['name']))
            __M_writer(u'</td>\n')
            # SOURCE LINE 27
            for column in c.category_data['columns']:
                # SOURCE LINE 28
                __M_writer(u'<td><input name="')
                __M_writer(escape(row['name'] + '^' + column['name'] + '^' + row['index'] + '^' + column['index']))
                __M_writer(u'" \n')
                # SOURCE LINE 29
                for field in c.table_data.get('data', []):
                    # SOURCE LINE 30
                    if field['row_index'] == row['index'] and field['column_index'] == column['index']:
                        # SOURCE LINE 31
                        __M_writer(u'value="')
                        __M_writer(escape(field['value']))
                        __M_writer(u'\n')
                # SOURCE LINE 34
                __M_writer(u'"></td>\n')
            # SOURCE LINE 36
            __M_writer(u'</tr>\n')
        # SOURCE LINE 38
        __M_writer(u'</table>\n<input type="hidden" name="table_name" value="')
        # SOURCE LINE 39
        __M_writer(escape(c.table_name))
        __M_writer(u'">\n<input type="hidden" name="table_version" value="')
        # SOURCE LINE 40
        __M_writer(escape(c.table_version))
        __M_writer(u'">\n')
        # SOURCE LINE 41
        if c.edit:
            # SOURCE LINE 42
            __M_writer(u'<input name="edited" value="true" type="hidden">\n')
        # SOURCE LINE 44
        if c.new:
            # SOURCE LINE 45
            __M_writer(u'<input name="new" value="true" type="hidden">\n')
        # SOURCE LINE 47
        __M_writer(u'<br/>\n<input type="button" value="submit" onclick="new function(){ \n       if (document.getElementById(\'table_index\').value == \'\') {\n       \t  alert(\'Table Index cannot be left blank.\')\n       }\n       else {\n      \t  document.getElementById(\'data_entry_form\').submit()\n       };\n}">\n<br/><br/><br/><br/><br/><br/>\n\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


