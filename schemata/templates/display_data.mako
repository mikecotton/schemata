<%inherit file="base.mako"/>
<table>
<tr><td>table name: ${c.table_name} </td></tr>
<tr><td>table version: ${c.table_version}</td></tr>
<tr><td>table index: ${c.table_index}</td></td>

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
%for field in c.table_data.get('data', []):
%if field['row_index'] == row['index'] and field['column_index'] == column['index']:
<td>${field['value']}</td>
%endif
%endfor
%endfor
</tr>
%endfor
</table>
<a href="/data_entry?table_name=${c.table_name}&table_version=${c.table_version}&table_index=${c.table_index}&edit=true">edit</a>