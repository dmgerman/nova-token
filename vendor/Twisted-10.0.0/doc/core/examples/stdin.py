begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nAn example of reading a line at a time from standard input\nwithout blocking the reactor.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'stdio'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'basic'
newline|'\n'
nl|'\n'
DECL|class|Echo
name|'class'
name|'Echo'
op|'('
name|'basic'
op|'.'
name|'LineReceiver'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'os'
name|'import'
name|'linesep'
name|'as'
name|'delimiter'
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
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|"'>>> '"
op|')'
newline|'\n'
nl|'\n'
DECL|member|lineReceived
dedent|''
name|'def'
name|'lineReceived'
op|'('
name|'self'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sendLine'
op|'('
string|"'Echo: '"
op|'+'
name|'line'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
string|"'>>> '"
op|')'
newline|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'stdio'
op|'.'
name|'StandardIO'
op|'('
name|'Echo'
op|'('
op|')'
op|')'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
