<%inherit file="base.mako"/>

<form action="newtable" method="get">
<p>

</p>
<p>

%if c.data_model:
<input type="hidden" name="edited" value="True">
%endif

</p>
<table>
<tr><td>table name<input name="table_name" value="${c.table_name}"></td></tr>
<tr><td>table version<input name="table_version"></td></tr>
<tr><td>x-axis lable<input name="x_axis_label" value="${c.data_model.get('x_axis_label', '')}"></td></tr>
<tr><td>y-axis label<input name="y_axis_label" value="${c.data_model.get('y_axis_label', '')}"></td></tr>
</table>

<table border="1" id="tblSample">
  <tr>
    <th colspan="3">Sample table</th>
  </tr>
  <tr>
%for i, row in enumerate(c.existing_items):
<td>${i+1}</td>
<td><input type="text" name="txtRow${i}" value="${row['name']}" size="40">
</td> 
<td><select name="selRow${i}">

%for option in ['column', 'comp_column', 'sub_column', 'row', 'comp_row', 'sub_row']:
<option value="${option}"
%if option == row['type']:
selected="selected"
%endif
>${option}</option>
%endfor
</select></td>
</tr>
%endfor
</tr>
<tr>
    <td>${len(c.existing_items)+1}</td>
    <td><input type="text" name="txtRow1"
     id="txtRow1" size="40" onkeypress="keyPressTest(event, this);" /></td>
    <td>
    <select name="selRow1">
    <option value="column">column</option>
    <option value="comp_column">compound column</option>
    <option value="sub_column">sub column</option>
    <option value="row">row</option>
    <option value="comp_row">compound row</option>
    <option value="sub_row">sub row</option>
    </select>
    </td>
  </tr>
</table>


<input type="button" value="Add" onclick="addRowToTable();" />
<input type="button" value="Remove" onclick="removeRowFromTable();" />
<input type="button" value="Submit" onclick="validateRow(this.form);" />
<input type="checkbox" id="chkValidate" /> Validate Submit

</form>

