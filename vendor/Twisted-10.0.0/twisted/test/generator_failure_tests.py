begin_unit
comment|'# Copyright (c) 2001-2007 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nPython 2.5 test cases for failures thrown into generators.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
op|'.'
name|'unittest'
name|'import'
name|'TestCase'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'failure'
name|'import'
name|'Failure'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'test'
op|'.'
name|'test_failure'
name|'import'
name|'getDivisionFailure'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TwoPointFiveFailureTests
name|'class'
name|'TwoPointFiveFailureTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_inlineCallbacksTracebacks
indent|'    '
name|'def'
name|'test_inlineCallbacksTracebacks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        inlineCallbacks that re-raise tracebacks into their deferred\n        should not lose their tracebacsk.\n        """'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'raiseException'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'.'
name|'errback'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'failures'
op|'='
op|'['
op|']'
newline|'\n'
DECL|function|collect_error
name|'def'
name|'collect_error'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'failures'
op|'.'
name|'append'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|function|ic
dedent|''
name|'def'
name|'ic'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'d'
newline|'\n'
dedent|''
name|'ic'
op|'='
name|'defer'
op|'.'
name|'inlineCallbacks'
op|'('
name|'ic'
op|')'
newline|'\n'
name|'ic'
op|'('
name|'d'
op|')'
op|'.'
name|'addErrback'
op|'('
name|'collect_error'
op|')'
newline|'\n'
nl|'\n'
name|'newFailure'
op|','
op|'='
name|'failures'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'traceback'
op|'.'
name|'extract_tb'
op|'('
name|'newFailure'
op|'.'
name|'getTracebackObject'
op|'('
op|')'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'['
op|'-'
number|'1'
op|']'
op|','
nl|'\n'
string|'"1/0"'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_throwIntoGenerator
dedent|''
name|'def'
name|'_throwIntoGenerator'
op|'('
name|'self'
op|','
name|'f'
op|','
name|'g'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'throwExceptionIntoGenerator'
op|'('
name|'g'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"throwExceptionIntoGenerator should have raised "'
nl|'\n'
string|'"StopIteration"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_throwExceptionIntoGenerator
dedent|''
dedent|''
name|'def'
name|'test_throwExceptionIntoGenerator'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        It should be possible to throw the exception that a Failure\n        represents into a generator.\n        """'
newline|'\n'
name|'stuff'
op|'='
op|'['
op|']'
newline|'\n'
DECL|function|generator
name|'def'
name|'generator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'yield'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'stuff'
op|'.'
name|'append'
op|'('
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Yield should have yielded exception."'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'g'
op|'='
name|'generator'
op|'('
op|')'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_throwIntoGenerator'
op|'('
name|'f'
op|','
name|'g'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'stuff'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|','
name|'ZeroDivisionError'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'stuff'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|','
name|'ZeroDivisionError'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'traceback'
op|'.'
name|'extract_tb'
op|'('
name|'stuff'
op|'['
number|'0'
op|']'
op|'['
number|'2'
op|']'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'['
op|'-'
number|'1'
op|']'
op|','
string|'"1/0"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_findFailureInGenerator
dedent|''
name|'def'
name|'test_findFailureInGenerator'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Within an exception handler, it should be possible to find the\n        original Failure that caused the current exception (if it was\n        caused by throwExceptionIntoGenerator).\n        """'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'cleanFailure'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'foundFailures'
op|'='
op|'['
op|']'
newline|'\n'
DECL|function|generator
name|'def'
name|'generator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'yield'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'foundFailures'
op|'.'
name|'append'
op|'('
name|'Failure'
op|'.'
name|'_findFailure'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"No exception sent to generator"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'g'
op|'='
name|'generator'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_throwIntoGenerator'
op|'('
name|'f'
op|','
name|'g'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'foundFailures'
op|','
op|'['
name|'f'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_failureConstructionFindsOriginalFailure
dedent|''
name|'def'
name|'test_failureConstructionFindsOriginalFailure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When a Failure is constructed in the context of an exception\n        handler that is handling an exception raised by\n        throwExceptionIntoGenerator, the new Failure should be chained to that\n        original Failure.\n        """'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'cleanFailure'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'newFailures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|generator
name|'def'
name|'generator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'yield'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'newFailures'
op|'.'
name|'append'
op|'('
name|'Failure'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"No exception sent to generator"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'g'
op|'='
name|'generator'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_throwIntoGenerator'
op|'('
name|'f'
op|','
name|'g'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'newFailures'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'newFailures'
op|'['
number|'0'
op|']'
op|'.'
name|'getTraceback'
op|'('
op|')'
op|','
name|'f'
op|'.'
name|'getTraceback'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ambiguousFailureInGenerator
dedent|''
name|'def'
name|'test_ambiguousFailureInGenerator'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When a generator reraises a different exception,\n        L{Failure._findFailure} inside the generator should find the reraised\n        exception rather than original one.\n        """'
newline|'\n'
DECL|function|generator
name|'def'
name|'generator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'yield'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                    '
op|'['
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'Failure'
op|'('
op|')'
op|'.'
name|'value'
op|','
name|'IndexError'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'g'
op|'='
name|'generator'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_throwIntoGenerator'
op|'('
name|'f'
op|','
name|'g'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ambiguousFailureFromGenerator
dedent|''
name|'def'
name|'test_ambiguousFailureFromGenerator'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When a generator reraises a different exception,\n        L{Failure._findFailure} above the generator should find the reraised\n        exception rather than original one.\n        """'
newline|'\n'
DECL|function|generator
name|'def'
name|'generator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'yield'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
op|'['
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'g'
op|'='
name|'generator'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'f'
op|'='
name|'getDivisionFailure'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_throwIntoGenerator'
op|'('
name|'f'
op|','
name|'g'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'Failure'
op|'('
op|')'
op|'.'
name|'value'
op|','
name|'IndexError'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
