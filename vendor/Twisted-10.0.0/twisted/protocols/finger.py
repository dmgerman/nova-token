begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""The Finger User Information Protocol (RFC 1288)"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'basic'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
DECL|class|Finger
name|'class'
name|'Finger'
op|'('
name|'basic'
op|'.'
name|'LineReceiver'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|lineReceived
indent|'    '
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
name|'parts'
op|'='
name|'string'
op|'.'
name|'split'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'parts'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'='
op|'['
string|"''"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'slash_w'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'slash_w'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'user'
op|'='
name|'parts'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
string|"'@'"
name|'in'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'host_place'
op|'='
name|'string'
op|'.'
name|'rfind'
op|'('
name|'user'
op|','
string|"'@'"
op|')'
newline|'\n'
name|'user'
op|'='
name|'user'
op|'['
op|':'
name|'host_place'
op|']'
newline|'\n'
name|'host'
op|'='
name|'user'
op|'['
name|'host_place'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'forwardQuery'
op|'('
name|'slash_w'
op|','
name|'user'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'getUser'
op|'('
name|'slash_w'
op|','
name|'user'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'getDomain'
op|'('
name|'slash_w'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_refuseMessage
dedent|''
dedent|''
name|'def'
name|'_refuseMessage'
op|'('
name|'self'
op|','
name|'message'
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
name|'message'
op|'+'
string|'"\\n"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|forwardQuery
dedent|''
name|'def'
name|'forwardQuery'
op|'('
name|'self'
op|','
name|'slash_w'
op|','
name|'user'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_refuseMessage'
op|'('
string|"'Finger forwarding service denied'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|getDomain
dedent|''
name|'def'
name|'getDomain'
op|'('
name|'self'
op|','
name|'slash_w'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_refuseMessage'
op|'('
string|"'Finger online list denied'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|getUser
dedent|''
name|'def'
name|'getUser'
op|'('
name|'self'
op|','
name|'slash_w'
op|','
name|'user'
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
string|"'Login: '"
op|'+'
name|'user'
op|'+'
string|"'\\n'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_refuseMessage'
op|'('
string|"'No such user'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
