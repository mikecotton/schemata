from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260989199.2796121
_template_filename='/Users/mike/schemata/schemata/templates/display_data.mako'
_template_uri='display_data.mako'
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
        __M_writer(u'\n<table>\n<tr><td>table name: ')
        # SOURCE LINE 3
        __M_writer(escape(c.table_name))
        __M_writer(u' </td></tr>\n<tr><td>table version: ')
        # SOURCE LINE 4
        __M_writer(escape(c.table_version))
        __M_writer(u'</td></tr>\n<tr><td>table index: ')
        # SOURCE LINE 5
        __M_writer(escape(c.table_index))
        __M_writer(u'</td></td>\n\n</table>\n\n<table border="1">\n  <tr>\n<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>\n\n')
        # SOURCE LINE 13
        for column in c.category_data['columns']:
            # SOURCE LINE 14
            __M_writer(u'<th> ')
            __M_writer(escape(column['name']))
            __M_writer(u' </th>\n')
        # SOURCE LINE 16
        __M_writer(u'</tr>\n')
        # SOURCE LINE 17
        for row in c.category_data['rows']:
            # SOURCE LINE 18
            __M_writer(u'<tr>\n<td>')
            # SOURCE LINE 19
            __M_writer(escape(row['name']))
            __M_writer(u'</td>\n')
            # SOURCE LINE 20
            for column in c.category_data['columns']:
                # SOURCE LINE 21
                for field in c.table_data.get('data', []):
                    # SOURCE LINE 22
                    if field['row_index'] == row['index'] and field['column_index'] == column['index']:
                        # SOURCE LINE 23
                        __M_writer(u'<td>')
                        __M_writer(escape(field['value']))
                        __M_writer(u'</td>\n')
            # SOURCE LINE 27
            __M_writer(u'</tr>\n')
        # SOURCE LINE 29
        __M_writer(u'</table>\n<a href="/data_entry?table_name=')
        # SOURCE LINE 30
        __M_writer(escape(c.table_name))
        __M_writer(u'&table_version=')
        __M_writer(escape(c.table_version))
        __M_writer(u'&table_index=')
        __M_writer(escape(c.table_index))
        __M_writer(u'&edit=true">edit</a>')
        return ''
    finally:
        context.caller_stack._pop_frame()


