<%inherit file="base.mako"/>

<form method="GET" action="/processtable">
<table>
<tr>
<td colspan="${len(c.column_titles)}">
<center>${c.table_name}</center>
</td>
</tr>

%for case in c.case_titles:
<tr><center><td colspan="${len(c.column_titles) + 1}">${case}</td></center></tr>
<td></td>
%for column in c.column_titles:
<td>${column}</td>
%endfor
</tr>
%for row in c.row_titles:
<tr><td>${row}</td>
%for i in range(len(c.column_titles)):
<td><input name="x:${row}^y:${column}^c:${case}"></td>
%endfor
</tr>
%endfor
<tr><td>&nbsp;</td></tr>
%endfor

<tr><td><input type="submit"></td></tr>
</table>
</form>
