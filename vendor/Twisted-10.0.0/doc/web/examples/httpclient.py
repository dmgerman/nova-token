begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'from'
name|'pprint'
name|'import'
name|'pprint'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
name|'import'
name|'version'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'defer'
name|'import'
name|'Deferred'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'protocol'
name|'import'
name|'Protocol'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'iweb'
name|'import'
name|'UNKNOWN_LENGTH'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'http_headers'
name|'import'
name|'Headers'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'client'
name|'import'
name|'Agent'
op|','
name|'ResponseDone'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WriteToStdout
name|'class'
name|'WriteToStdout'
op|'('
name|'Protocol'
op|')'
op|':'
newline|'\n'
DECL|member|connectionMade
indent|'    '
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
name|'onConnLost'
op|'='
name|'Deferred'
op|'('
op|')'
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
name|'print'
string|"'Got some:'"
op|','
name|'data'
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
name|'if'
name|'not'
name|'reason'
op|'.'
name|'check'
op|'('
name|'ResponseDone'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'.'
name|'printTraceback'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|"'Response done'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'onConnLost'
op|'.'
name|'callback'
op|'('
name|'None'
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
name|'reactor'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'userAgent'
op|'='
string|"'Twisted/%s (httpclient.py)'"
op|'%'
op|'('
name|'version'
op|'.'
name|'short'
op|'('
op|')'
op|','
op|')'
newline|'\n'
name|'agent'
op|'='
name|'Agent'
op|'('
name|'reactor'
op|')'
newline|'\n'
name|'d'
op|'='
name|'agent'
op|'.'
name|'request'
op|'('
nl|'\n'
string|"'GET'"
op|','
name|'url'
op|','
name|'Headers'
op|'('
op|'{'
string|"'user-agent'"
op|':'
op|'['
name|'userAgent'
op|']'
op|'}'
op|')'
op|')'
newline|'\n'
DECL|function|cbResponse
name|'def'
name|'cbResponse'
op|'('
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pprint'
op|'('
name|'vars'
op|'('
name|'response'
op|')'
op|')'
newline|'\n'
name|'proto'
op|'='
name|'WriteToStdout'
op|'('
op|')'
newline|'\n'
name|'if'
name|'response'
op|'.'
name|'length'
name|'is'
name|'not'
name|'UNKNOWN_LENGTH'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|"'The response body will consist of'"
op|','
name|'response'
op|'.'
name|'length'
op|','
string|"'bytes.'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|"'The response body length is unknown.'"
newline|'\n'
dedent|''
name|'response'
op|'.'
name|'deliverBody'
op|'('
name|'proto'
op|')'
newline|'\n'
name|'return'
name|'proto'
op|'.'
name|'onConnLost'
newline|'\n'
dedent|''
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'cbResponse'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addErrback'
op|'('
name|'log'
op|'.'
name|'err'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addBoth'
op|'('
name|'lambda'
name|'ign'
op|':'
name|'reactor'
op|'.'
name|'callWhenRunning'
op|'('
name|'reactor'
op|'.'
name|'stop'
op|')'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'reactor'
op|','
op|'*'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
