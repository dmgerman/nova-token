begin_unit
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'util'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'spread'
name|'import'
name|'pb'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
name|'import'
name|'portal'
op|','
name|'checkers'
op|','
name|'credentials'
newline|'\n'
nl|'\n'
DECL|class|Avatar
name|'class'
name|'Avatar'
op|'('
name|'pb'
op|'.'
name|'Avatar'
op|')'
op|':'
newline|'\n'
DECL|member|perspective_exception
indent|'    '
name|'def'
name|'perspective_exception'
op|'('
name|'self'
op|','
name|'x'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'x'
op|'/'
number|'0'
newline|'\n'
nl|'\n'
DECL|class|Realm
dedent|''
dedent|''
name|'class'
name|'Realm'
op|':'
newline|'\n'
DECL|member|requestAvatar
indent|'    '
name|'def'
name|'requestAvatar'
op|'('
name|'self'
op|','
name|'interface'
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
name|'pb'
op|'.'
name|'IPerspective'
name|'in'
name|'interfaces'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'pb'
op|'.'
name|'IPerspective'
op|','
name|'Avatar'
op|'('
op|')'
op|','
name|'lambda'
op|':'
name|'None'
newline|'\n'
nl|'\n'
DECL|function|cbLogin
dedent|''
dedent|''
dedent|''
name|'def'
name|'cbLogin'
op|'('
name|'avatar'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'avatar'
op|'.'
name|'callRemote'
op|'('
string|'"exception"'
op|','
number|'10'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'str'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'util'
op|'.'
name|'println'
op|')'
newline|'\n'
nl|'\n'
DECL|function|ebLogin
dedent|''
name|'def'
name|'ebLogin'
op|'('
name|'failure'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
name|'failure'
newline|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'c'
op|'='
name|'checkers'
op|'.'
name|'InMemoryUsernamePasswordDatabaseDontUse'
op|'('
name|'user'
op|'='
string|'"pass"'
op|')'
newline|'\n'
name|'p'
op|'='
name|'portal'
op|'.'
name|'Portal'
op|'('
name|'Realm'
op|'('
op|')'
op|','
op|'['
name|'c'
op|']'
op|')'
newline|'\n'
name|'server'
op|'='
name|'pb'
op|'.'
name|'PBServerFactory'
op|'('
name|'p'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'unsafeTracebacks'
op|'='
name|'True'
newline|'\n'
name|'client'
op|'='
name|'pb'
op|'.'
name|'PBClientFactory'
op|'('
op|')'
newline|'\n'
name|'login'
op|'='
name|'client'
op|'.'
name|'login'
op|'('
name|'credentials'
op|'.'
name|'UsernamePassword'
op|'('
string|'"user"'
op|','
string|'"pass"'
op|')'
op|')'
newline|'\n'
name|'login'
op|'.'
name|'addCallback'
op|'('
name|'cbLogin'
op|')'
op|'.'
name|'addErrback'
op|'('
name|'ebLogin'
op|')'
op|'.'
name|'addBoth'
op|'('
name|'lambda'
op|':'
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'p'
op|'='
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'0'
op|','
name|'server'
op|')'
newline|'\n'
name|'c'
op|'='
name|'reactor'
op|'.'
name|'connectTCP'
op|'('
string|"'127.0.0.1'"
op|','
name|'p'
op|'.'
name|'getHost'
op|'('
op|')'
op|'.'
name|'port'
op|','
name|'client'
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
