begin_unit
nl|'\n'
string|'"""\nBenchmarks for L{twisted.internet.task}.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'timer'
name|'import'
name|'timeit'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
newline|'\n'
nl|'\n'
DECL|function|test_performance
name|'def'
name|'test_performance'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    L{LoopingCall} should not take long to skip a lot of iterations.\n    """'
newline|'\n'
name|'clock'
op|'='
name|'task'
op|'.'
name|'Clock'
op|'('
op|')'
newline|'\n'
name|'call'
op|'='
name|'task'
op|'.'
name|'LoopingCall'
op|'('
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'call'
op|'.'
name|'clock'
op|'='
name|'clock'
newline|'\n'
nl|'\n'
name|'call'
op|'.'
name|'start'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'clock'
op|'.'
name|'advance'
op|'('
number|'1000000'
op|')'
newline|'\n'
nl|'\n'
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
name|'print'
string|'"LoopingCall large advance takes"'
op|','
name|'timeit'
op|'('
name|'test_performance'
op|','
name|'iter'
op|'='
number|'1'
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
