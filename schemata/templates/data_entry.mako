<%inherit file="base.mako"/>

<form action="/data_entry" method="POST" id="data_entry_form">
<p>

</p>
<p>
</p>
<table>
<tr><td>table name: ${c.table_name} </td></tr>
<tr><td>table version: ${c.table_version}</td></tr>
<tr><td>table index: <input id="table_index" name="table_index" value="${c.table_index}"></td></td>

</table>

<table border="1">
  <tr>
<th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>

%for column in c.category_data['columns']:
<th> ${column['name']} </th>
%endfor
</tr>
%for row in c.category_data['rows']:
<tr>
<td>${row['name']}</td>
%for column in c.category_data['columns']:
<td><input name="${row['name'] + '^' + column['name'] + '^' + row['index'] + '^' + column['index']}" 
%for field in c.table_data.get('data', []):
%if field['row_index'] == row['index'] and field['column_index'] == column['index']:
value="${field['value']}
%endif
%endfor
"></td>
%endfor
</tr>
%endfor
</table>
<input type="hidden" name="table_name" value="${c.table_name}">
<input type="hidden" name="table_version" value="${c.table_version}">
%if c.edit:
<input name="edited" value="true" type="hidden">
%endif
%if c.new:
<input name="new" value="true" type="hidden">
%endif
<br/>
<input type="button" value="submit" onclick="new function(){ 
       if (document.getElementById('table_index').value == '') {
       	  alert('Table Index cannot be left blank.')
       }
       else {
      	  document.getElementById('data_entry_form').submit()
       };
}">
<br/><br/><br/><br/><br/><br/>

</form>

