begin_unit
string|'"""Write back all data it receives."""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
DECL|variable|data
name|'data'
op|'='
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
name|'while'
name|'data'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
DECL|variable|data
name|'data'
op|'='
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
string|'"byebye"'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
