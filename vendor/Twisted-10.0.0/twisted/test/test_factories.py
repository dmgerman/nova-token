begin_unit
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTest code for basic Factory classes.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'pickle'
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
name|'internet'
name|'import'
name|'reactor'
op|','
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'task'
name|'import'
name|'Clock'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'protocol'
name|'import'
name|'Factory'
op|','
name|'ReconnectingClientFactory'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
op|'.'
name|'basic'
name|'import'
name|'Int16StringReceiver'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|In
name|'class'
name|'In'
op|'('
name|'Int16StringReceiver'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'msgs'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|connectionMade
dedent|''
name|'def'
name|'connectionMade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'factory'
op|'.'
name|'connections'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|stringReceived
dedent|''
name|'def'
name|'stringReceived'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'n'
op|','
name|'msg'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msgs'
op|'['
name|'n'
op|']'
op|'='
name|'msg'
newline|'\n'
name|'self'
op|'.'
name|'sendString'
op|'('
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'n'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connectionLost
dedent|''
name|'def'
name|'connectionLost'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'factory'
op|'.'
name|'allMessages'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'msgs'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'self'
op|'.'
name|'factory'
op|'.'
name|'allMessages'
op|')'
op|'>='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'goal'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'factory'
op|'.'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|Out
dedent|''
dedent|''
dedent|''
name|'class'
name|'Out'
op|'('
name|'Int16StringReceiver'
op|')'
op|':'
newline|'\n'
DECL|variable|msgs
indent|'    '
name|'msgs'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'x'
op|','
string|"'X'"
op|'*'
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'msgs'
op|'='
name|'Out'
op|'.'
name|'msgs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|connectionMade
dedent|''
name|'def'
name|'connectionMade'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'self'
op|'.'
name|'msgs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sendString'
op|'('
name|'pickle'
op|'.'
name|'dumps'
op|'('
op|'('
name|'i'
op|','
name|'self'
op|'.'
name|'msgs'
op|'['
name|'i'
op|']'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stringReceived
dedent|''
dedent|''
name|'def'
name|'stringReceived'
op|'('
name|'self'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'n'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'msgs'
op|'['
name|'n'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'msgs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'howManyTimes'
op|'-='
number|'1'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'howManyTimes'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'factory'
op|'.'
name|'stopTrying'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeConnector
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeConnector'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A fake connector class, to be used to mock connections failed or lost.\n    """'
newline|'\n'
nl|'\n'
DECL|member|stopConnecting
name|'def'
name|'stopConnecting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|connect
dedent|''
name|'def'
name|'connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|ReconnectingFactoryTestCase
dedent|''
dedent|''
name|'class'
name|'ReconnectingFactoryTestCase'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{ReconnectingClientFactory}.\n    """'
newline|'\n'
nl|'\n'
DECL|member|testStopTrying
name|'def'
name|'testStopTrying'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'Factory'
op|'('
op|')'
newline|'\n'
name|'f'
op|'.'
name|'protocol'
op|'='
name|'In'
newline|'\n'
name|'f'
op|'.'
name|'connections'
op|'='
number|'0'
newline|'\n'
name|'f'
op|'.'
name|'allMessages'
op|'='
op|'['
op|']'
newline|'\n'
name|'f'
op|'.'
name|'goal'
op|'='
number|'2'
newline|'\n'
name|'f'
op|'.'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'c'
op|'='
name|'ReconnectingClientFactory'
op|'('
op|')'
newline|'\n'
name|'c'
op|'.'
name|'initialDelay'
op|'='
name|'c'
op|'.'
name|'delay'
op|'='
number|'0.2'
newline|'\n'
name|'c'
op|'.'
name|'protocol'
op|'='
name|'Out'
newline|'\n'
name|'c'
op|'.'
name|'howManyTimes'
op|'='
number|'2'
newline|'\n'
nl|'\n'
name|'port'
op|'='
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'0'
op|','
name|'f'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'port'
op|'.'
name|'stopListening'
op|')'
newline|'\n'
name|'PORT'
op|'='
name|'port'
op|'.'
name|'getHost'
op|'('
op|')'
op|'.'
name|'port'
newline|'\n'
name|'reactor'
op|'.'
name|'connectTCP'
op|'('
string|"'127.0.0.1'"
op|','
name|'PORT'
op|','
name|'c'
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'.'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_testStopTrying_1'
op|','
name|'f'
op|','
name|'c'
op|')'
newline|'\n'
name|'return'
name|'f'
op|'.'
name|'d'
newline|'\n'
dedent|''
name|'testStopTrying'
op|'.'
name|'timeout'
op|'='
number|'10'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_testStopTrying_1
name|'def'
name|'_testStopTrying_1'
op|'('
name|'self'
op|','
name|'res'
op|','
name|'f'
op|','
name|'c'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'f'
op|'.'
name|'allMessages'
op|')'
op|','
number|'2'
op|','
nl|'\n'
string|'"not enough messages -- %s"'
op|'%'
name|'f'
op|'.'
name|'allMessages'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'f'
op|'.'
name|'connections'
op|','
number|'2'
op|','
nl|'\n'
string|'"Number of successful connections incorrect %d"'
op|'%'
nl|'\n'
name|'f'
op|'.'
name|'connections'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'f'
op|'.'
name|'allMessages'
op|','
op|'['
name|'Out'
op|'.'
name|'msgs'
op|']'
op|'*'
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failIf'
op|'('
name|'c'
op|'.'
name|'continueTrying'
op|','
string|'"stopTrying never called or ineffective"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_serializeUnused
dedent|''
name|'def'
name|'test_serializeUnused'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        A L{ReconnectingClientFactory} which hasn\'t been used for anything\n        can be pickled and unpickled and end up with the same state.\n        """'
newline|'\n'
name|'original'
op|'='
name|'ReconnectingClientFactory'
op|'('
op|')'
newline|'\n'
name|'reconstituted'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'original'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'original'
op|'.'
name|'__dict__'
op|','
name|'reconstituted'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_serializeWithClock
dedent|''
name|'def'
name|'test_serializeWithClock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        The clock attribute of L{ReconnectingClientFactory} is not serialized,\n        and the restored value sets it to the default value, the reactor.\n        """'
newline|'\n'
name|'clock'
op|'='
name|'Clock'
op|'('
op|')'
newline|'\n'
name|'original'
op|'='
name|'ReconnectingClientFactory'
op|'('
op|')'
newline|'\n'
name|'original'
op|'.'
name|'clock'
op|'='
name|'clock'
newline|'\n'
name|'reconstituted'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'original'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIdentical'
op|'('
name|'reconstituted'
op|'.'
name|'clock'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_deserializationResetsParameters
dedent|''
name|'def'
name|'test_deserializationResetsParameters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        A L{ReconnectingClientFactory} which is unpickled does not have an\n        L{IConnector} and has its reconnecting timing parameters reset to their\n        initial values.\n        """'
newline|'\n'
name|'factory'
op|'='
name|'ReconnectingClientFactory'
op|'('
op|')'
newline|'\n'
name|'factory'
op|'.'
name|'clientConnectionFailed'
op|'('
name|'FakeConnector'
op|'('
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'factory'
op|'.'
name|'stopTrying'
op|')'
newline|'\n'
nl|'\n'
name|'serialized'
op|'='
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'factory'
op|')'
newline|'\n'
name|'unserialized'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'serialized'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unserialized'
op|'.'
name|'connector'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unserialized'
op|'.'
name|'_callID'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unserialized'
op|'.'
name|'retries'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unserialized'
op|'.'
name|'delay'
op|','
name|'factory'
op|'.'
name|'initialDelay'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unserialized'
op|'.'
name|'continueTrying'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_parametrizedClock
dedent|''
name|'def'
name|'test_parametrizedClock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        The clock used by L{ReconnectingClientFactory} can be parametrized, so\n        that one can cleanly test reconnections.\n        """'
newline|'\n'
name|'clock'
op|'='
name|'Clock'
op|'('
op|')'
newline|'\n'
name|'factory'
op|'='
name|'ReconnectingClientFactory'
op|'('
op|')'
newline|'\n'
name|'factory'
op|'.'
name|'clock'
op|'='
name|'clock'
newline|'\n'
nl|'\n'
name|'factory'
op|'.'
name|'clientConnectionLost'
op|'('
name|'FakeConnector'
op|'('
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'clock'
op|'.'
name|'calls'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
