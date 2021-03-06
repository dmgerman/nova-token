begin_unit
comment|'# -*- coding: utf-8 -*-'
nl|'\n'
comment|'# This is a hack of the builtin todo extension, to make the todo_list'
nl|'\n'
comment|'# more user friendly.'
nl|'\n'
nl|'\n'
name|'from'
name|'sphinx'
op|'.'
name|'ext'
op|'.'
name|'todo'
name|'import'
op|'*'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_
name|'def'
name|'_'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'s'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|process_todo_nodes
dedent|''
name|'def'
name|'process_todo_nodes'
op|'('
name|'app'
op|','
name|'doctree'
op|','
name|'fromdocname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'app'
op|'.'
name|'config'
op|'['
string|"'todo_include_todos'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'node'
name|'in'
name|'doctree'
op|'.'
name|'traverse'
op|'('
name|'todo_node'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'.'
name|'parent'
op|'.'
name|'remove'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
comment|'# Replace all todolist nodes with a list of the collected todos.'
nl|'\n'
comment|'# Augment each todo with a backlink to the original location.'
nl|'\n'
dedent|''
dedent|''
name|'env'
op|'='
name|'app'
op|'.'
name|'builder'
op|'.'
name|'env'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'env'
op|','
string|"'todo_all_todos'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'env'
op|'.'
name|'todo_all_todos'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# remove the item that was added in the constructor, since I'm tired of"
nl|'\n'
comment|'# reading through docutils for the proper way to construct an empty list'
nl|'\n'
dedent|''
name|'lists'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lists'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'bullet_list'
op|'('
string|'""'
op|','
name|'nodes'
op|'.'
name|'Text'
op|'('
string|"''"
op|','
string|"''"
op|')'
op|')'
op|')'
newline|'\n'
name|'lists'
op|'['
name|'i'
op|']'
op|'.'
name|'remove'
op|'('
name|'lists'
op|'['
name|'i'
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'lists'
op|'['
name|'i'
op|']'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'todo_list'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'node'
name|'in'
name|'doctree'
op|'.'
name|'traverse'
op|'('
name|'todolist'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'app'
op|'.'
name|'config'
op|'['
string|"'todo_include_todos'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'.'
name|'replace_self'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'todo_info'
name|'in'
name|'env'
op|'.'
name|'todo_all_todos'
op|':'
newline|'\n'
indent|'            '
name|'para'
op|'='
name|'nodes'
op|'.'
name|'paragraph'
op|'('
op|')'
newline|'\n'
comment|'# Create a reference'
nl|'\n'
name|'newnode'
op|'='
name|'nodes'
op|'.'
name|'reference'
op|'('
string|"''"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'filename'
op|'='
name|'env'
op|'.'
name|'doc2path'
op|'('
name|'todo_info'
op|'['
string|"'docname'"
op|']'
op|','
name|'base'
op|'='
name|'None'
op|')'
newline|'\n'
name|'link'
op|'='
op|'('
name|'_'
op|'('
string|"'%(filename)s, line %(line_info)d'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|','
string|"'line_info'"
op|':'
name|'todo_info'
op|'['
string|"'lineno'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'innernode'
op|'='
name|'nodes'
op|'.'
name|'emphasis'
op|'('
name|'link'
op|','
name|'link'
op|')'
newline|'\n'
name|'newnode'
op|'['
string|"'refdocname'"
op|']'
op|'='
name|'todo_info'
op|'['
string|"'docname'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'newnode'
op|'['
string|"'refuri'"
op|']'
op|'='
name|'app'
op|'.'
name|'builder'
op|'.'
name|'get_relative_uri'
op|'('
nl|'\n'
name|'fromdocname'
op|','
name|'todo_info'
op|'['
string|"'docname'"
op|']'
op|')'
newline|'\n'
name|'newnode'
op|'['
string|"'refuri'"
op|']'
op|'+='
string|"'#'"
op|'+'
name|'todo_info'
op|'['
string|"'target'"
op|']'
op|'['
string|"'refid'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'NoUri'
op|':'
newline|'\n'
comment|'# ignore if no URI can be determined, e.g. for LaTeX output'
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'newnode'
op|'.'
name|'append'
op|'('
name|'innernode'
op|')'
newline|'\n'
name|'para'
op|'+='
name|'newnode'
newline|'\n'
name|'para'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'todo_link'"
op|')'
newline|'\n'
nl|'\n'
name|'todo_entry'
op|'='
name|'todo_info'
op|'['
string|"'todo'"
op|']'
newline|'\n'
nl|'\n'
name|'env'
op|'.'
name|'resolve_references'
op|'('
name|'todo_entry'
op|','
name|'todo_info'
op|'['
string|"'docname'"
op|']'
op|','
nl|'\n'
name|'app'
op|'.'
name|'builder'
op|')'
newline|'\n'
nl|'\n'
name|'item'
op|'='
name|'nodes'
op|'.'
name|'list_item'
op|'('
string|"''"
op|','
name|'para'
op|')'
newline|'\n'
name|'todo_entry'
op|'['
number|'1'
op|']'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'details'"
op|')'
newline|'\n'
nl|'\n'
name|'comment'
op|'='
name|'todo_entry'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
name|'m'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
string|'r"^P(\\d)"'
op|','
name|'comment'
op|'.'
name|'astext'
op|'('
op|')'
op|')'
newline|'\n'
name|'priority'
op|'='
number|'5'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'                '
name|'priority'
op|'='
name|'int'
op|'('
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'if'
name|'priority'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'priority'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'priority'
op|'>'
number|'5'
op|':'
newline|'\n'
indent|'                    '
name|'priority'
op|'='
number|'5'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'item'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'todo_p'"
op|'+'
name|'str'
op|'('
name|'priority'
op|')'
op|')'
newline|'\n'
name|'todo_entry'
op|'['
string|"'classes'"
op|']'
op|'.'
name|'append'
op|'('
string|"'todo_p'"
op|'+'
name|'str'
op|'('
name|'priority'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'item'
op|'.'
name|'append'
op|'('
name|'comment'
op|')'
newline|'\n'
nl|'\n'
name|'lists'
op|'['
name|'priority'
op|'-'
number|'1'
op|']'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'item'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'node'
op|'.'
name|'replace_self'
op|'('
name|'lists'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'app'
op|'.'
name|'add_config_value'
op|'('
string|"'todo_include_todos'"
op|','
name|'False'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'.'
name|'add_node'
op|'('
name|'todolist'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_node'
op|'('
name|'todo_node'
op|','
nl|'\n'
name|'html'
op|'='
op|'('
name|'visit_todo_node'
op|','
name|'depart_todo_node'
op|')'
op|','
nl|'\n'
name|'latex'
op|'='
op|'('
name|'visit_todo_node'
op|','
name|'depart_todo_node'
op|')'
op|','
nl|'\n'
name|'text'
op|'='
op|'('
name|'visit_todo_node'
op|','
name|'depart_todo_node'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'todo'"
op|','
name|'Todo'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'todolist'"
op|','
name|'TodoList'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'connect'
op|'('
string|"'doctree-read'"
op|','
name|'process_todos'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'connect'
op|'('
string|"'doctree-resolved'"
op|','
name|'process_todo_nodes'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'connect'
op|'('
string|"'env-purge-doc'"
op|','
name|'purge_todos'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
