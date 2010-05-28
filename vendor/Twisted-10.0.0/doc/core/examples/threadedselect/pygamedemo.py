begin_unit
name|'from'
name|'__future__'
name|'import'
name|'generators'
newline|'\n'
nl|'\n'
comment|'# import Twisted and install'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'_threadedselect'
newline|'\n'
name|'_threadedselect'
op|'.'
name|'install'
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
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'pygame'
newline|'\n'
name|'from'
name|'pygame'
op|'.'
name|'locals'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'pygame'
op|'.'
name|'fastevent'
name|'as'
name|'eventmodule'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'pygame'
op|'.'
name|'event'
name|'as'
name|'eventmodule'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# You can customize this if you use your'
nl|'\n'
comment|'# own events, but you must OBEY:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   USEREVENT <= TWISTEDEVENT < NUMEVENTS'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|TWISTEDEVENT
dedent|''
name|'TWISTEDEVENT'
op|'='
name|'USEREVENT'
newline|'\n'
nl|'\n'
DECL|function|postTwistedEvent
name|'def'
name|'postTwistedEvent'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
comment|'# if not using pygame.fastevent, this can explode if the queue'
nl|'\n'
comment|"# fills up.. so that's bad.  Use pygame.fastevent, in pygame CVS"
nl|'\n'
comment|'# as of 2005-04-18.'
nl|'\n'
indent|'    '
name|'eventmodule'
op|'.'
name|'post'
op|'('
name|'eventmodule'
op|'.'
name|'Event'
op|'('
name|'TWISTEDEVENT'
op|','
name|'iterateTwisted'
op|'='
name|'func'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|helloWorld
dedent|''
name|'def'
name|'helloWorld'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
string|'"hello, world"'
newline|'\n'
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'1'
op|','
name|'helloWorld'
op|')'
newline|'\n'
dedent|''
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'1'
op|','
name|'helloWorld'
op|')'
newline|'\n'
nl|'\n'
DECL|function|twoSecondsPassed
name|'def'
name|'twoSecondsPassed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'print'
string|'"two seconds passed"'
newline|'\n'
dedent|''
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'2'
op|','
name|'twoSecondsPassed'
op|')'
newline|'\n'
nl|'\n'
DECL|function|eventIterator
name|'def'
name|'eventIterator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'eventmodule'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'='
name|'eventmodule'
op|'.'
name|'poll'
op|'('
op|')'
newline|'\n'
name|'if'
name|'event'
op|'.'
name|'type'
op|'=='
name|'NOEVENT'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'event'
newline|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pygame'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'eventmodule'
op|','
string|"'init'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'eventmodule'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
dedent|''
name|'screen'
op|'='
name|'pygame'
op|'.'
name|'display'
op|'.'
name|'set_mode'
op|'('
op|'('
number|'300'
op|','
number|'300'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# send an event when twisted wants attention'
nl|'\n'
name|'reactor'
op|'.'
name|'interleave'
op|'('
name|'postTwistedEvent'
op|')'
newline|'\n'
comment|"# make shouldQuit a True value when it's safe to quit"
nl|'\n'
comment|'# by appending a value to it.  This ensures that'
nl|'\n'
comment|'# Twisted gets to shut down properly.'
nl|'\n'
name|'shouldQuit'
op|'='
op|'['
op|']'
newline|'\n'
name|'reactor'
op|'.'
name|'addSystemEventTrigger'
op|'('
string|"'after'"
op|','
string|"'shutdown'"
op|','
name|'shouldQuit'
op|'.'
name|'append'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'event'
name|'in'
name|'eventIterator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'event'
op|'.'
name|'type'
op|'=='
name|'TWISTEDEVENT'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'.'
name|'iterateTwisted'
op|'('
op|')'
newline|'\n'
name|'if'
name|'shouldQuit'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'event'
op|'.'
name|'type'
op|'=='
name|'QUIT'
op|':'
newline|'\n'
indent|'            '
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'event'
op|'.'
name|'type'
op|'=='
name|'KEYDOWN'
name|'and'
name|'event'
op|'.'
name|'key'
op|'=='
name|'K_ESCAPE'
op|':'
newline|'\n'
indent|'            '
name|'reactor'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'pygame'
op|'.'
name|'quit'
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
