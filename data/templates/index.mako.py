from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1261778665.1680491
_template_filename='/Users/mike/schemata/schemata/templates/index.mako'
_template_uri='index.mako'
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
        __M_writer(u'\n\n\n<h1>Tables</h1>\n<a href="/new_table">Create New Table</a>\n')
        # SOURCE LINE 6
        for table in c.all_tables:
            # SOURCE LINE 7
            __M_writer(u'<h2>')
            __M_writer(escape(table))
            __M_writer(u'</h2>\n')
            # SOURCE LINE 8
            for version in c.table_ranges[table].keys():
                # SOURCE LINE 9
                __M_writer(u'version: ')
                __M_writer(escape(version))
                __M_writer(u'<br/>\n')
                # SOURCE LINE 10
                for index in c.table_ranges[table][version]:
                    # SOURCE LINE 11
                    __M_writer(escape(index))
                    __M_writer(u' <a href="/data_entry?table_name=')
                    __M_writer(escape(table))
                    __M_writer(u'&table_version=')
                    __M_writer(escape(version))
                    __M_writer(u'&table_index=')
                    __M_writer(escape(index))
                    __M_writer(u'&edit=true">edit</a>, <a href="/display_data?table_name=')
                    __M_writer(escape(table))
                    __M_writer(u'&table_version=')
                    __M_writer(escape(version))
                    __M_writer(u'&table_index=')
                    __M_writer(escape(index))
                    __M_writer(u'">show</a>\n<br/>\n<br/>\n')
                # SOURCE LINE 15
                __M_writer(u'<a href="/data_entry?table_name=')
                __M_writer(escape(table))
                __M_writer(u'&table_version=')
                __M_writer(escape(version))
                __M_writer(u'&new=true">Add new instance of ')
                __M_writer(escape(table))
                __M_writer(u'</a><br/>\n<a href="/new_table?table_name=')
                # SOURCE LINE 16
                __M_writer(escape(table))
                __M_writer(u'&table_version=')
                __M_writer(escape(version))
                __M_writer(u'">Create a new table based on ')
                __M_writer(escape(table))
                __M_writer(u'</a>\n<br/>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


