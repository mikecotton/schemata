from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260989256.8553231
_template_filename='/Users/mike/schemata/schemata/templates/make_new_table.mako'
_template_uri='make_new_table.mako'
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
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<form action="newtable" method="get">\n<p>\n\n</p>\n<p>\n\n')
        # SOURCE LINE 9
        if c.data_model:
            # SOURCE LINE 10
            __M_writer(u'<input type="hidden" name="edited" value="True">\n')
        # SOURCE LINE 12
        __M_writer(u'\n</p>\n<table>\n<tr><td>table name<input name="table_name" value="')
        # SOURCE LINE 15
        __M_writer(escape(c.table_name))
        __M_writer(u'"></td></tr>\n<tr><td>table version<input name="table_version"></td></tr>\n<tr><td>x-axis lable<input name="x_axis_label" value="')
        # SOURCE LINE 17
        __M_writer(escape(c.data_model.get('x_axis_label', '')))
        __M_writer(u'"></td></tr>\n<tr><td>y-axis label<input name="y_axis_label" value="')
        # SOURCE LINE 18
        __M_writer(escape(c.data_model.get('y_axis_label', '')))
        __M_writer(u'"></td></tr>\n</table>\n\n<table border="1" id="tblSample">\n  <tr>\n    <th colspan="3">Sample table</th>\n  </tr>\n  <tr>\n')
        # SOURCE LINE 26
        for i, row in enumerate(c.existing_items):
            # SOURCE LINE 27
            __M_writer(u'<td>')
            __M_writer(escape(i+1))
            __M_writer(u'</td>\n<td><input type="text" name="txtRow')
            # SOURCE LINE 28
            __M_writer(escape(i))
            __M_writer(u'" value="')
            __M_writer(escape(row['name']))
            __M_writer(u'" size="40">\n</td> \n<td><select name="selRow')
            # SOURCE LINE 30
            __M_writer(escape(i))
            __M_writer(u'">\n\n')
            # SOURCE LINE 32
            for option in ['column', 'comp_column', 'sub_column', 'row', 'comp_row', 'sub_row']:
                # SOURCE LINE 33
                __M_writer(u'<option value="')
                __M_writer(escape(option))
                __M_writer(u'"\n')
                # SOURCE LINE 34
                if option == row['type']:
                    # SOURCE LINE 35
                    __M_writer(u'selected="selected"\n')
                # SOURCE LINE 37
                __M_writer(u'>')
                __M_writer(escape(option))
                __M_writer(u'</option>\n')
            # SOURCE LINE 39
            __M_writer(u'</select></td>\n</tr>\n')
        # SOURCE LINE 42
        __M_writer(u'</tr>\n<tr>\n    <td>')
        # SOURCE LINE 44
        __M_writer(escape(len(c.existing_items)+1))
        __M_writer(u'</td>\n    <td><input type="text" name="txtRow1"\n     id="txtRow1" size="40" onkeypress="keyPressTest(event, this);" /></td>\n    <td>\n    <select name="selRow1">\n    <option value="column">column</option>\n    <option value="comp_column">compound column</option>\n    <option value="sub_column">sub column</option>\n    <option value="row">row</option>\n    <option value="comp_row">compound row</option>\n    <option value="sub_row">sub row</option>\n    </select>\n    </td>\n  </tr>\n</table>\n\n\n<input type="button" value="Add" onclick="addRowToTable();" />\n<input type="button" value="Remove" onclick="removeRowFromTable();" />\n<input type="button" value="Submit" onclick="validateRow(this.form);" />\n<input type="checkbox" id="chkValidate" /> Validate Submit\n\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


