begin_unit
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
op|','
name|'protocol'
newline|'\n'
nl|'\n'
DECL|class|FakeTelnet
name|'class'
name|'FakeTelnet'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
DECL|variable|commandToRun
indent|'    '
name|'commandToRun'
op|'='
op|'['
string|"'/bin/sh'"
op|']'
comment|'# could have args too'
newline|'\n'
DECL|variable|dirToRunIn
name|'dirToRunIn'
op|'='
string|"'/tmp'"
newline|'\n'
DECL|member|connectionMade
name|'def'
name|'connectionMade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'connection made'"
newline|'\n'
name|'self'
op|'.'
name|'propro'
op|'='
name|'ProcessProtocol'
op|'('
name|'self'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'spawnProcess'
op|'('
name|'self'
op|'.'
name|'propro'
op|','
name|'self'
op|'.'
name|'commandToRun'
op|'['
number|'0'
op|']'
op|','
name|'self'
op|'.'
name|'commandToRun'
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'self'
op|'.'
name|'dirToRunIn'
op|','
name|'usePTY'
op|'='
number|'1'
op|')'
newline|'\n'
DECL|member|dataReceived
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'propro'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
DECL|member|conectionLost
dedent|''
name|'def'
name|'conectionLost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'connection lost'"
newline|'\n'
name|'self'
op|'.'
name|'propro'
op|'.'
name|'tranport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|ProcessProtocol
dedent|''
dedent|''
name|'class'
name|'ProcessProtocol'
op|'('
name|'protocol'
op|'.'
name|'ProcessProtocol'
op|')'
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
name|'pr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pr'
op|'='
name|'pr'
newline|'\n'
nl|'\n'
DECL|member|outReceived
dedent|''
name|'def'
name|'outReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pr'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|processEnded
dedent|''
name|'def'
name|'processEnded'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'protocol conection lost'"
newline|'\n'
name|'self'
op|'.'
name|'pr'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|variable|f
dedent|''
dedent|''
name|'f'
op|'='
name|'protocol'
op|'.'
name|'Factory'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'protocol'
op|'='
name|'FakeTelnet'
newline|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'5823'
op|','
name|'f'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
