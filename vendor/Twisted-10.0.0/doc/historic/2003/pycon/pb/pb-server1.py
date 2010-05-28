begin_unit
comment|'#! /usr/bin/python'
nl|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'spread'
name|'import'
name|'pb'
newline|'\n'
name|'import'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'app'
newline|'\n'
nl|'\n'
DECL|class|ServerObject
name|'class'
name|'ServerObject'
op|'('
name|'pb'
op|'.'
name|'Root'
op|')'
op|':'
newline|'\n'
DECL|member|remote_add
indent|'    '
name|'def'
name|'remote_add'
op|'('
name|'self'
op|','
name|'one'
op|','
name|'two'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'answer'
op|'='
name|'one'
op|'+'
name|'two'
newline|'\n'
name|'print'
string|'"returning result:"'
op|','
name|'answer'
newline|'\n'
name|'return'
name|'answer'
newline|'\n'
DECL|member|remote_subtract
dedent|''
name|'def'
name|'remote_subtract'
op|'('
name|'self'
op|','
name|'one'
op|','
name|'two'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'one'
op|'-'
name|'two'
newline|'\n'
nl|'\n'
DECL|variable|app
dedent|''
dedent|''
name|'app'
op|'='
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'app'
op|'.'
name|'Application'
op|'('
string|'"server1"'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'listenTCP'
op|'('
number|'8800'
op|','
name|'pb'
op|'.'
name|'BrokerFactory'
op|'('
name|'ServerObject'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'run'
op|'('
name|'save'
op|'='
number|'0'
op|')'
newline|'\n'
endmarker|''
end_unit
