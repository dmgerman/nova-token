begin_unit
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
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
name|'python'
name|'import'
name|'log'
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
name|'web'
name|'import'
name|'server'
op|','
name|'resource'
op|','
name|'guard'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'portal'
name|'import'
name|'IRealm'
op|','
name|'Portal'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'checkers'
name|'import'
name|'InMemoryUsernamePasswordDatabaseDontUse'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GuardedResource
name|'class'
name|'GuardedResource'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A resource which is protected by guard and requires authentication in order\n    to access.\n    """'
newline|'\n'
DECL|member|getChild
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|render
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Authorized!"'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleRealm
dedent|''
dedent|''
name|'class'
name|'SimpleRealm'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A realm which gives out L{GuardedResource} instances for authenticated\n    users.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IRealm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|requestAvatar
name|'def'
name|'requestAvatar'
op|'('
name|'self'
op|','
name|'avatarId'
op|','
name|'mind'
op|','
op|'*'
name|'interfaces'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'resource'
op|'.'
name|'IResource'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'resource'
op|'.'
name|'IResource'
op|','
name|'GuardedResource'
op|'('
op|')'
op|','
name|'lambda'
op|':'
name|'None'
newline|'\n'
dedent|''
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'log'
op|'.'
name|'startLogging'
op|'('
name|'sys'
op|'.'
name|'stdout'
op|')'
newline|'\n'
name|'checkers'
op|'='
op|'['
name|'InMemoryUsernamePasswordDatabaseDontUse'
op|'('
name|'joe'
op|'='
string|"'blow'"
op|')'
op|']'
newline|'\n'
name|'wrapper'
op|'='
name|'guard'
op|'.'
name|'HTTPAuthSessionWrapper'
op|'('
nl|'\n'
name|'Portal'
op|'('
name|'SimpleRealm'
op|'('
op|')'
op|','
name|'checkers'
op|')'
op|','
nl|'\n'
op|'['
name|'guard'
op|'.'
name|'DigestCredentialFactory'
op|'('
string|"'md5'"
op|','
string|"'example.com'"
op|')'
op|']'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8889'
op|','
name|'server'
op|'.'
name|'Site'
op|'('
nl|'\n'
name|'resource'
op|'='
name|'wrapper'
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
