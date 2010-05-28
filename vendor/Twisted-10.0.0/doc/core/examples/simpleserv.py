begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
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
string|'"""This is just about the simplest possible protocol"""'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
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
string|'"As soon as any data is received, write it back."'
newline|'\n'
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
string|'"""This runs the protocol on port 8000"""'
newline|'\n'
name|'factory'
op|'='
name|'protocol'
op|'.'
name|'ServerFactory'
op|'('
op|')'
newline|'\n'
name|'factory'
op|'.'
name|'protocol'
op|'='
name|'Echo'
newline|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8000'
op|','
name|'factory'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# this only runs if the module was *not* imported'
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
