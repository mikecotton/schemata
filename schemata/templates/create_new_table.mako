<%inherit file="base.mako"/>
<form target="/new_table">
Table Name: <input name="table_name" value="${c.table_name}"/><br/>
Table Version: <input name="table_version" /><br/>
X-Axis Label: <input name="x_axis_label" value="${c.x_axis_label}"/><br/>
Y-Axis Label: <input name="y_axis_label" value="${c.y_axis_label}"/><br/>
<ol id="row_column_list">

%for i, item in enumerate(c.existing_items or c.default_table_data):
    <li id="list_element_${i}">	
    	<input id="element_name_${i}" name="element_name_${i}" value="${item['name']}" />
    	<select id="row_or_column_${i}" name="row_or_column_${i}">

%for option in ['column', 'comp_column', 'sub_column', 'row', 'comp_row', 'sub_row']:
<option value="${option}"
%if option == item['type']:
selected="selected"
%endif
>${option}</option>
%endfor

</select>
	<input id="delete_button_${i}" type="button" onClick="new function(){
delete_list_element(document.getElementById('list_element_${i}'))
}" />
    </li>
%endfor
</ol>
<input id="add" type="button" value="add" onClick="add_list_element()">
<input type='submit'>
</form>

<script type="text/javascript">
Sortable.create('row_column_list', tag='li');
</script>

<script type="text/javascript">
function delete_list_element(li_element){
    var rc_list = document.getElementById('row_column_list');
    rc_list.removeChild(li_element);
}
</script>

<script type="text/javascript">
iteration = document.getElementsByTagName('li').length;

</script>

<script type="text/javascript">

function add_list_element(){


var rclist = document.getElementById('row_column_list');

var new_element = document.createElement('li');
    new_element.id = ('new_element_' + iteration);

var new_text_field = document.createElement('input');
    new_text_field.id = ('element_name_' + iteration);
    new_text_field.name = ('element_name_' + iteration);

var new_select = document.getElementById('row_or_column_0').cloneNode(true);
    new_select.id = ('row_or_column_' + iteration);
    new_select.name = ('row_or_column_' + iteration);
    new_select.options[document.getElementById('row_or_column_' + (iteration - 1)).selectedIndex].selected = true;

var new_delete_button = document.createElement('input');
    new_delete_button.type = ('button');
    new_delete_button.id = ('delete_button_' + iteration);
    new_delete_button.onclick = function(){delete_list_element(this.parentNode)
};

new_element.appendChild(new_text_field);
new_element.appendChild(new_select);
new_element.appendChild(new_delete_button);
rclist.appendChild(new_element);

iteration += 1;
Sortable.create('row_column_list', tag='li');
};

</script>
<br/>

<script "text/javascript">
last_selected_option = document.getElementById('row_or_column_' + (iteration - 1)).selectedIndex;
</script>
