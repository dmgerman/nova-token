begin_unit
comment|'# -*- test-case-name: twisted.web.test.test_httpauth -*-'
nl|'\n'
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nHTTP BASIC authentication.\n\n@see: U{http://tools.ietf.org/html/rfc1945}\n@see: U{http://tools.ietf.org/html/rfc2616}\n@see: U{http://tools.ietf.org/html/rfc2617}\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'binascii'
newline|'\n'
nl|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
name|'import'
name|'credentials'
op|','
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'iweb'
name|'import'
name|'ICredentialFactory'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BasicCredentialFactory
name|'class'
name|'BasicCredentialFactory'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Credential Factory for HTTP Basic Authentication\n\n    @type authenticationRealm: C{str}\n    @ivar authenticationRealm: The HTTP authentication realm which will be issued in\n        challenges.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'ICredentialFactory'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|scheme
name|'scheme'
op|'='
string|"'basic'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'authenticationRealm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'authenticationRealm'
op|'='
name|'authenticationRealm'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getChallenge
dedent|''
name|'def'
name|'getChallenge'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a challenge including the HTTP authentication realm with which\n        this factory was created.\n        """'
newline|'\n'
name|'return'
op|'{'
string|"'realm'"
op|':'
name|'self'
op|'.'
name|'authenticationRealm'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|decode
dedent|''
name|'def'
name|'decode'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Parse the base64-encoded, colon-separated username and password into a\n        L{credentials.UsernamePassword} instance.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'creds'
op|'='
name|'binascii'
op|'.'
name|'a2b_base64'
op|'('
name|'response'
op|'+'
string|"'==='"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'binascii'
op|'.'
name|'Error'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'error'
op|'.'
name|'LoginFailed'
op|'('
string|"'Invalid credentials'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'creds'
op|'='
name|'creds'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'creds'
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'credentials'
op|'.'
name|'UsernamePassword'
op|'('
op|'*'
name|'creds'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'error'
op|'.'
name|'LoginFailed'
op|'('
string|"'Invalid credentials'"
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
