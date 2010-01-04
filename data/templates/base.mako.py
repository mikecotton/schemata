from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1260918715.7113559
_template_filename='/Users/mike/schemata/schemata/templates/base.mako'
_template_uri='base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        getattr = context.get('getattr', UNDEFINED)
        c = context.get('c', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n\n<head>\n    <meta http-equiv="content-type" content="text/html; charset=UTF-8">\n    <META HTTP-EQUIV="Pragma" CONTENT="no-cache">\n    <META HTTP-EQUIV="Expires" CONTENT="-1">\n\n<script type="text/javascript" src="http://127.0.0.1:5001/js/prototype.js"></script>\n<script type="text/javascript" src="http://127.0.0.1:5001/js/scriptaculous.js"></script>\n\n<!-- <script type="text/javascript">\nfunction addRowToTable()\n{\n  var tbl = document.getElementById(\'tblSample\');\n  var lastRow = tbl.rows.length;\n  // if there\'s no header row in the table, then iteration = lastRow + 1\n  var iteration = lastRow;\n  var row = tbl.insertRow(lastRow);\n\n  // left cell\n  var cellLeft = row.insertCell(0);\n  var textNode = document.createTextNode(iteration);\n  cellLeft.appendChild(textNode);\n\n  // right cell\n  var cellRight = row.insertCell(1);\n  var el = document.createElement(\'input\');\n  el.type = \'text\';\n  el.name = \'txtRow\' + iteration;\n  el.id = \'txtRow\' + iteration;\n  el.size = 40;\n\n  el.onkeypress = keyPressTest;\n  cellRight.appendChild(el);\n\n  // select cell\n  var cellRightSel = row.insertCell(2);\n  var sel = document.createElement(\'select\');\n  sel.name = \'selRow\' + iteration;\n  sel.options[0] = new Option(\'column\', \'column\');\n  sel.options[1] = new Option(\'compound column\', \'comp_column\');\n  sel.options[2] = new Option(\'sub-column\', \'sub_column\');\n  sel.options[3] = new Option(\'row\', \'row\');\n  sel.options[4] = new Option(\'compound row\', \'comp_row\');\n  sel.options[5] = new Option(\'sub-row\', \'sub_row\');\n  cellRightSel.appendChild(sel);\n}\nfunction keyPressTest(e, obj)\n{\n  var validateChkb = document.getElementById(\'chkValidateOnKeyPress\');\n  if (validateChkb.checked) {\n    var displayObj = document.getElementById(\'spanOutput\');\n    var key;\n    if(window.event) {\n      key = window.event.keyCode;\n    }\n    else if(e.which) {\n      key = e.which;\n    }\n    var objId;\n    if (obj != null) {\n      objId = obj.id;\n    } else {\n      objId = this.id;\n    }\n    displayObj.innerHTML = objId + \' : \' + String.fromCharCode(key);\n  }\n}\nfunction removeRowFromTable()\n{\n  var tbl = document.getElementById(\'tblSample\');\n  var lastRow = tbl.rows.length;\n  if (lastRow > 2) tbl.deleteRow(lastRow - 1);\n}\nfunction openInNewWindow(frm)\n{\n  // open a blank window\n  var aWindow = window.open(\'\', \'TableAddRowNewWindow\',\n   \'scrollbars=yes,menubar=yes,resizable=yes,toolbar=no,width=400,height=400\');\n\n  // set the target to the blank window\n  frm.target = \'TableAddRowNewWindow\';\n\n  // submit\n  frm.submit();\n}\n\nfunction validateRow(frm)\n{\n  var chkb = document.getElementById(\'chkValidate\');\n  if (chkb.checked) {\n    var tbl = document.getElementById(\'tblSample\');\n    var lastRow = tbl.rows.length - 1;\n    var i;\n    for (i=1; i<=lastRow; i++) {\n        var aRow = document.getElementById(\'txtRow\' + i);\n        if (aRow.value.length <= 0) {\n                                 alert(\'Row \' + i + \' is empty\');\n                                 return;\n                                    }\n                                }\n                    }\n                    openInNewWindow(frm);\n}\n\n</script> -->\n</head>\n<body>\n\n')
        # SOURCE LINE 112
        if getattr(c, 'error'):
            # SOURCE LINE 113
            __M_writer(u'        <center class="error-message">')
            __M_writer(filters.html_escape(escape(c.error )))
            __M_writer(u'<br/><br/></center>\n')
        # SOURCE LINE 115
        __M_writer(u'\n        ')
        # SOURCE LINE 116
        __M_writer(escape(self.body()))
        __M_writer(u'\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


