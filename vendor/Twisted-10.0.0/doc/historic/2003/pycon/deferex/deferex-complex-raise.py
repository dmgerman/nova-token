begin_unit
DECL|class|MyExc
name|'class'
name|'MyExc'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"A sample exception."'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
DECL|variable|x
indent|'    '
name|'x'
op|'='
number|'1'
op|'+'
number|'3'
newline|'\n'
name|'raise'
name|'MyExc'
op|'('
string|'"I can\'t go on!"'
op|')'
newline|'\n'
DECL|variable|x
name|'x'
op|'='
name|'x'
op|'+'
number|'1'
newline|'\n'
name|'print'
name|'x'
newline|'\n'
dedent|''
name|'except'
name|'MyExc'
op|','
name|'me'
op|':'
newline|'\n'
indent|'    '
name|'print'
string|"'error ('"
op|','
name|'me'
op|','
string|"').  x was:'"
op|','
name|'x'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'    '
name|'print'
string|"'fatal error! abort!'"
newline|'\n'
dedent|''
endmarker|''
end_unit
