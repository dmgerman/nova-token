begin_unit
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'utils'
name|'import'
name|'ShellCommand'
op|','
name|'get_ts'
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'import'
name|'boto'
op|'.'
name|'utils'
newline|'\n'
nl|'\n'
DECL|class|ScriptBase
name|'class'
name|'ScriptBase'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'config_file'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Instance'"
op|','
string|"'instance-id'"
op|','
string|"'default'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'self'
op|'.'
name|'ts'
op|'='
name|'get_ts'
op|'('
op|')'
newline|'\n'
name|'if'
name|'config_file'
op|':'
newline|'\n'
indent|'            '
name|'boto'
op|'.'
name|'config'
op|'.'
name|'read'
op|'('
name|'config_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|notify
dedent|''
dedent|''
name|'def'
name|'notify'
op|'('
name|'self'
op|','
name|'subject'
op|','
name|'body'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'boto'
op|'.'
name|'utils'
op|'.'
name|'notify'
op|'('
name|'subject'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|mkdir
dedent|''
name|'def'
name|'mkdir'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'boto'
op|'.'
name|'log'
op|'.'
name|'error'
op|'('
string|"'Error creating directory: %s'"
op|'%'
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|umount
dedent|''
dedent|''
dedent|''
name|'def'
name|'umount'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'ismount'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'run'
op|'('
string|"'umount %s'"
op|'%'
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'command'
op|','
name|'notify'
op|'='
name|'True'
op|','
name|'exit_on_error'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'last_command'
op|'='
name|'ShellCommand'
op|'('
name|'command'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'last_command'
op|'.'
name|'status'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'boto'
op|'.'
name|'log'
op|'.'
name|'error'
op|'('
string|'\'Error running command: "%s". Output: "%s"\''
op|'%'
op|'('
name|'command'
op|','
name|'self'
op|'.'
name|'last_command'
op|'.'
name|'output'
op|')'
op|')'
newline|'\n'
name|'if'
name|'notify'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'notify'
op|'('
string|"'Error encountered'"
op|','
string|"'Error running the following command:\\n\\t%s\\n\\nCommand output:\\n\\t%s'"
op|'%'
op|'('
name|'command'
op|','
name|'self'
op|'.'
name|'last_command'
op|'.'
name|'output'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'exit_on_error'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'last_command'
op|'.'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|main
dedent|''
name|'def'
name|'main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
