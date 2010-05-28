begin_unit
comment|'# -*- test-case-name: twisted.words.test -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2005 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'""" A temporary placeholder for client-capable strports, until we\nsufficient use cases get identified """'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'strports'
newline|'\n'
nl|'\n'
DECL|function|_parseTCPSSL
name|'def'
name|'_parseTCPSSL'
op|'('
name|'factory'
op|','
name|'domain'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" For the moment, parse TCP or SSL connections the same """'
newline|'\n'
name|'return'
op|'('
name|'domain'
op|','
name|'int'
op|'('
name|'port'
op|')'
op|','
name|'factory'
op|')'
op|','
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_parseUNIX
dedent|''
name|'def'
name|'_parseUNIX'
op|'('
name|'factory'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
name|'address'
op|','
name|'factory'
op|')'
op|','
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_funcs
dedent|''
name|'_funcs'
op|'='
op|'{'
string|'"tcp"'
op|':'
name|'_parseTCPSSL'
op|','
nl|'\n'
string|'"unix"'
op|':'
name|'_parseUNIX'
op|','
nl|'\n'
string|'"ssl"'
op|':'
name|'_parseTCPSSL'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse
name|'def'
name|'parse'
op|'('
name|'description'
op|','
name|'factory'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'args'
op|','
name|'kw'
op|'='
name|'strports'
op|'.'
name|'_parse'
op|'('
name|'description'
op|')'
newline|'\n'
name|'return'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|','
op|')'
op|'+'
name|'_funcs'
op|'['
name|'args'
op|'['
number|'0'
op|']'
op|']'
op|'('
name|'factory'
op|','
op|'*'
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
nl|'\n'
DECL|function|client
dedent|''
name|'def'
name|'client'
op|'('
name|'description'
op|','
name|'factory'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'internet'
newline|'\n'
name|'name'
op|','
name|'args'
op|','
name|'kw'
op|'='
name|'parse'
op|'('
name|'description'
op|','
name|'factory'
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'internet'
op|','
name|'name'
op|'+'
string|"'Client'"
op|')'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
