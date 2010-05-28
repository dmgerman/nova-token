begin_unit
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.internet._pollingfile}.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'runtime'
name|'import'
name|'platform'
newline|'\n'
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
name|'if'
name|'platform'
op|'.'
name|'isWindows'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'_pollingfile'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|_pollingfile
indent|'    '
name|'_pollingfile'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestPollableWritePipe
dedent|''
name|'class'
name|'TestPollableWritePipe'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{_pollingfile._PollableWritePipe}.\n    """'
newline|'\n'
nl|'\n'
DECL|member|test_checkWorkUnicode
name|'def'
name|'test_checkWorkUnicode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When one tries to pass unicode to L{_pollingfile._PollableWritePipe}, a\n        C{TypeError} is raised instead of passing the data to C{WriteFile}\n        call which is going to mangle it.\n        """'
newline|'\n'
name|'p'
op|'='
name|'_pollingfile'
op|'.'
name|'_PollableWritePipe'
op|'('
number|'1'
op|','
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'write'
op|'('
string|'"test"'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'checkWork'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'p'
op|'.'
name|'write'
op|'('
string|'u"test"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TypeError'
op|','
name|'p'
op|'.'
name|'checkWork'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'_pollingfile'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'    '
name|'TestPollableWritePipe'
op|'.'
name|'skip'
op|'='
string|'"_pollingfile is only avalable under Windows."'
newline|'\n'
dedent|''
endmarker|''
end_unit
