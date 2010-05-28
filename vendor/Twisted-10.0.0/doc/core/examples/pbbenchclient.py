begin_unit
nl|'\n'
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
name|'internet'
name|'import'
name|'defer'
op|','
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'credentials'
name|'import'
name|'UsernamePassword'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
DECL|class|PBBenchClient
name|'class'
name|'PBBenchClient'
op|':'
newline|'\n'
DECL|variable|hostname
indent|'    '
name|'hostname'
op|'='
string|"'localhost'"
newline|'\n'
DECL|variable|portno
name|'portno'
op|'='
name|'pb'
op|'.'
name|'portno'
newline|'\n'
DECL|variable|calledThisSecond
name|'calledThisSecond'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|callLoop
name|'def'
name|'callLoop'
op|'('
name|'self'
op|','
name|'ignored'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d1'
op|'='
name|'self'
op|'.'
name|'persp'
op|'.'
name|'callRemote'
op|'('
string|'"simple"'
op|')'
newline|'\n'
name|'d2'
op|'='
name|'self'
op|'.'
name|'persp'
op|'.'
name|'callRemote'
op|'('
string|'"complexTypes"'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'DeferredList'
op|'('
op|'['
name|'d1'
op|','
name|'d2'
op|']'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'callLoop'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'calledThisSecond'
op|'+='
number|'1'
newline|'\n'
name|'thisSecond'
op|'='
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'thisSecond'
op|'!='
name|'self'
op|'.'
name|'lastSecond'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'thisSecond'
op|'-'
name|'self'
op|'.'
name|'lastSecond'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'print'
string|'"WARNING it took more than one second"'
newline|'\n'
dedent|''
name|'print'
string|"'cps:'"
op|','
name|'self'
op|'.'
name|'calledThisSecond'
newline|'\n'
name|'self'
op|'.'
name|'calledThisSecond'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'lastSecond'
op|'='
name|'thisSecond'
newline|'\n'
nl|'\n'
DECL|member|_cbPerspective
dedent|''
dedent|''
name|'def'
name|'_cbPerspective'
op|'('
name|'self'
op|','
name|'persp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'persp'
op|'='
name|'persp'
newline|'\n'
name|'self'
op|'.'
name|'lastSecond'
op|'='
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'callLoop'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|runTest
dedent|''
name|'def'
name|'runTest'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'factory'
op|'='
name|'pb'
op|'.'
name|'PBClientFactory'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'connectTCP'
op|'('
name|'self'
op|'.'
name|'hostname'
op|','
name|'self'
op|'.'
name|'portno'
op|','
name|'factory'
op|')'
newline|'\n'
name|'factory'
op|'.'
name|'login'
op|'('
name|'UsernamePassword'
op|'('
string|'"benchmark"'
op|','
string|'"benchmark"'
op|')'
op|')'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_cbPerspective'
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
name|'PBBenchClient'
op|'('
op|')'
op|'.'
name|'runTest'
op|'('
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
