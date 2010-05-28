begin_unit
string|'"""A process that reads from stdin and out using Twisted."""'
newline|'\n'
nl|'\n'
comment|'### Twisted Preamble'
nl|'\n'
comment|"# This makes sure that users don't have to set up their environment"
nl|'\n'
comment|'# specially in order to run these programs from bin/.'
nl|'\n'
name|'import'
name|'sys'
op|','
name|'os'
op|','
name|'string'
newline|'\n'
DECL|variable|pos
name|'pos'
op|'='
name|'string'
op|'.'
name|'find'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|','
name|'os'
op|'.'
name|'sep'
op|'+'
string|"'Twisted'"
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|'['
op|':'
name|'pos'
op|'+'
number|'8'
op|']'
op|')'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'curdir'
op|')'
newline|'\n'
comment|'### end of preamble'
nl|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'interfaces'
newline|'\n'
nl|'\n'
name|'log'
op|'.'
name|'startLogging'
op|'('
name|'sys'
op|'.'
name|'stderr'
op|')'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
op|','
name|'reactor'
op|','
name|'stdio'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Echo
name|'class'
name|'Echo'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'implements'
op|'('
name|'interfaces'
op|'.'
name|'IHalfCloseableProtocol'
op|')'
newline|'\n'
nl|'\n'
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
string|'"connection made"'
newline|'\n'
nl|'\n'
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
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|readConnectionLost
dedent|''
name|'def'
name|'readConnectionLost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"readConnectionLost"'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
DECL|member|writeConnectionLost
dedent|''
name|'def'
name|'writeConnectionLost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"writeConnectionLost"'
newline|'\n'
nl|'\n'
DECL|member|connectionLost
dedent|''
name|'def'
name|'connectionLost'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"connectionLost"'
op|','
name|'reason'
newline|'\n'
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'stdio'
op|'.'
name|'StandardIO'
op|'('
name|'Echo'
op|'('
op|')'
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
