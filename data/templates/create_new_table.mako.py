from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261779122.870086
_template_filename='/Users/mike/schemata/schemata/templates/create_new_table.mako'
_template_uri='create_new_table.mako'
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
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<form target="/new_table">\nTable Name: <input name="table_name" value="')
        # SOURCE LINE 3
        __M_writer(escape(c.table_name))
        __M_writer(u'"/><br/>\nTable Version: <input name="table_version" /><br/>\nX-Axis Label: <input name="x_axis_label" value="')
        # SOURCE LINE 5
        __M_writer(escape(c.x_axis_label))
        __M_writer(u'"/><br/>\nY-Axis Label: <input name="y_axis_label" value="')
        # SOURCE LINE 6
        __M_writer(escape(c.y_axis_label))
        __M_writer(u'"/><br/>\n<ol id="row_column_list">\n\n')
        # SOURCE LINE 9
        for i, item in enumerate(c.existing_items or c.default_table_data):
            # SOURCE LINE 10
            __M_writer(u'    <li id="list_element_')
            __M_writer(escape(i))
            __M_writer(u'">\t\n    \t<input id="element_name_')
            # SOURCE LINE 11
            __M_writer(escape(i))
            __M_writer(u'" name="element_name_')
            __M_writer(escape(i))
            __M_writer(u'" value="')
            __M_writer(escape(item['name']))
            __M_writer(u'" />\n    \t<select id="row_or_column_')
            # SOURCE LINE 12
            __M_writer(escape(i))
            __M_writer(u'" name="row_or_column_')
            __M_writer(escape(i))
            __M_writer(u'">\n\n')
            # SOURCE LINE 14
            for option in ['column', 'comp_column', 'sub_column', 'row', 'comp_row', 'sub_row']:
                # SOURCE LINE 15
                __M_writer(u'<option value="')
                __M_writer(escape(option))
                __M_writer(u'"\n')
                # SOURCE LINE 16
                if option == item['type']:
                    # SOURCE LINE 17
                    __M_writer(u'selected="selected"\n')
                # SOURCE LINE 19
                __M_writer(u'>')
                __M_writer(escape(option))
                __M_writer(u'</option>\n')
            # SOURCE LINE 21
            __M_writer(u'\n</select>\n\t<input id="delete_button_')
            # SOURCE LINE 23
            __M_writer(escape(i))
            __M_writer(u'" type="button" onClick="new function(){\ndelete_list_element(document.getElementById(\'list_element_')
            # SOURCE LINE 24
            __M_writer(escape(i))
            __M_writer(u'\'))\n}" />\n    </li>\n')
        # SOURCE LINE 28
        __M_writer(u'</ol>\n<input id="add" type="button" value="add" onClick="add_list_element()">\n<input type=\'submit\'>\n</form>\n\n<script type="text/javascript">\nSortable.create(\'row_column_list\', tag=\'li\');\n</script>\n\n<script type="text/javascript">\nfunction delete_list_element(li_element){\n    var rc_list = document.getElementById(\'row_column_list\');\n    rc_list.removeChild(li_element);\n}\n</script>\n\n<script type="text/javascript">\niteration = document.getElementsByTagName(\'li\').length;\n\n</script>\n\n<script type="text/javascript">\n\nfunction add_list_element(){\n\n\nvar rclist = document.getElementById(\'row_column_list\');\n\nvar new_element = document.createElement(\'li\');\n    new_element.id = (\'new_element_\' + iteration);\n\nvar new_text_field = document.createElement(\'input\');\n    new_text_field.id = (\'element_name_\' + iteration);\n    new_text_field.name = (\'element_name_\' + iteration);\n\nvar new_select = document.getElementById(\'row_or_column_0\').cloneNode(true);\n    new_select.id = (\'row_or_column_\' + iteration);\n    new_select.name = (\'row_or_column_\' + iteration);\n    new_select.options[document.getElementById(\'row_or_column_\' + (iteration - 1)).selectedIndex].selected = true;\n\nvar new_delete_button = document.createElement(\'input\');\n    new_delete_button.type = (\'button\');\n    new_delete_button.id = (\'delete_button_\' + iteration);\n    new_delete_button.onclick = function(){delete_list_element(this.parentNode)\n};\n\nnew_element.appendChild(new_text_field);\nnew_element.appendChild(new_select);\nnew_element.appendChild(new_delete_button);\nrclist.appendChild(new_element);\n\niteration += 1;\nSortable.create(\'row_column_list\', tag=\'li\');\n};\n\n</script>\n<br/>\n\n<script "text/javascript">\nlast_selected_option = document.getElementById(\'row_or_column_\' + (iteration - 1)).selectedIndex;\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


