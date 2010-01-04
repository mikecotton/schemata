<%inherit file="base.mako"/>


<h1>Tables</h1>
<a href="/new_table">Create New Table</a>
%for table in c.all_tables:
<h2>${table}</h2>
%for version in c.table_ranges[table].keys():
version: ${version}<br/>
%for index in c.table_ranges[table][version]:
${index} <a href="/data_entry?table_name=${table}&table_version=${version}&table_index=${index}&edit=true">edit</a>, <a href="/display_data?table_name=${table}&table_version=${version}&table_index=${index}">show</a>
<br/>
<br/>
%endfor
<a href="/data_entry?table_name=${table}&table_version=${version}&new=true">Add new instance of ${table}</a><br/>
<a href="/new_table?table_name=${table}&table_version=${version}">Create a new table based on ${table}</a>
<br/>
%endfor
%endfor
