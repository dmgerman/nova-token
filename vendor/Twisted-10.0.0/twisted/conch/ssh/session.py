begin_unit
comment|'# -*- test-case-name: twisted.conch.test.test_session -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nThis module contains the implementation of SSHSession, which (by default)\nallows access to a shell and a python interpreter over SSH.\n\nMaintainer: Paul Swartz\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'struct'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
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
name|'conch'
op|'.'
name|'interfaces'
name|'import'
name|'ISession'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'conch'
op|'.'
name|'ssh'
name|'import'
name|'common'
op|','
name|'channel'
newline|'\n'
nl|'\n'
DECL|class|SSHSession
name|'class'
name|'SSHSession'
op|'('
name|'channel'
op|'.'
name|'SSHChannel'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|name
indent|'    '
name|'name'
op|'='
string|"'session'"
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'channel'
op|'.'
name|'SSHChannel'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'buf'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|request_subsystem
dedent|''
name|'def'
name|'request_subsystem'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subsystem'
op|','
name|'ignored'
op|'='
name|'common'
op|'.'
name|'getNS'
op|'('
name|'data'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|'\'asking for subsystem "%s"\''
op|'%'
name|'subsystem'
op|')'
newline|'\n'
name|'client'
op|'='
name|'self'
op|'.'
name|'avatar'
op|'.'
name|'lookupSubsystem'
op|'('
name|'subsystem'
op|','
name|'data'
op|')'
newline|'\n'
name|'if'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'pp'
op|'='
name|'SSHSessionProcessProtocol'
op|'('
name|'self'
op|')'
newline|'\n'
name|'proto'
op|'='
name|'wrapProcessProtocol'
op|'('
name|'pp'
op|')'
newline|'\n'
name|'client'
op|'.'
name|'makeConnection'
op|'('
name|'proto'
op|')'
newline|'\n'
name|'pp'
op|'.'
name|'makeConnection'
op|'('
name|'wrapProtocol'
op|'('
name|'client'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'pp'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'failed to get subsystem'"
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|request_shell
dedent|''
dedent|''
name|'def'
name|'request_shell'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'getting shell'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'='
name|'ISession'
op|'('
name|'self'
op|'.'
name|'avatar'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pp'
op|'='
name|'SSHSessionProcessProtocol'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'openShell'
op|'('
name|'pp'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'deferr'
op|'('
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'pp'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|request_exec
dedent|''
dedent|''
name|'def'
name|'request_exec'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'='
name|'ISession'
op|'('
name|'self'
op|'.'
name|'avatar'
op|')'
newline|'\n'
dedent|''
name|'f'
op|','
name|'data'
op|'='
name|'common'
op|'.'
name|'getNS'
op|'('
name|'data'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|'\'executing command "%s"\''
op|'%'
name|'f'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pp'
op|'='
name|'SSHSessionProcessProtocol'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'execCommand'
op|'('
name|'pp'
op|','
name|'f'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'deferr'
op|'('
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'pp'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|request_pty_req
dedent|''
dedent|''
name|'def'
name|'request_pty_req'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'='
name|'ISession'
op|'('
name|'self'
op|'.'
name|'avatar'
op|')'
newline|'\n'
dedent|''
name|'term'
op|','
name|'windowSize'
op|','
name|'modes'
op|'='
name|'parseRequest_pty_req'
op|'('
name|'data'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'pty request: %s %s'"
op|'%'
op|'('
name|'term'
op|','
name|'windowSize'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'.'
name|'getPty'
op|'('
name|'term'
op|','
name|'windowSize'
op|','
name|'modes'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'err'
op|'('
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|request_window_change
dedent|''
dedent|''
name|'def'
name|'request_window_change'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'='
name|'ISession'
op|'('
name|'self'
op|'.'
name|'avatar'
op|')'
newline|'\n'
dedent|''
name|'winSize'
op|'='
name|'parseRequest_window_change'
op|'('
name|'data'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'.'
name|'windowChanged'
op|'('
name|'winSize'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'error changing window size'"
op|')'
newline|'\n'
name|'log'
op|'.'
name|'err'
op|'('
op|')'
newline|'\n'
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
dedent|''
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|':'
newline|'\n'
comment|'#self.conn.sendClose(self)'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'buf'
op|'+='
name|'data'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'client'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|extReceived
dedent|''
name|'def'
name|'extReceived'
op|'('
name|'self'
op|','
name|'dataType'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'dataType'
op|'=='
name|'connection'
op|'.'
name|'EXTENDED_DATA_STDERR'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'client'
name|'and'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'client'
op|'.'
name|'transport'
op|','
string|"'writeErr'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'client'
op|'.'
name|'transport'
op|'.'
name|'writeErr'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'weird extended data: %s'"
op|'%'
name|'dataType'
op|')'
newline|'\n'
nl|'\n'
DECL|member|eofReceived
dedent|''
dedent|''
name|'def'
name|'eofReceived'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'.'
name|'eofReceived'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'conn'
op|'.'
name|'sendClose'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|closed
dedent|''
dedent|''
name|'def'
name|'closed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'session'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'session'
op|'.'
name|'closed'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'#def closeReceived(self):'
nl|'\n'
comment|"#    self.loseConnection() # don't know what to do with this"
nl|'\n'
nl|'\n'
DECL|member|loseConnection
dedent|''
dedent|''
name|'def'
name|'loseConnection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'.'
name|'transport'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
dedent|''
name|'channel'
op|'.'
name|'SSHChannel'
op|'.'
name|'loseConnection'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|class|_ProtocolWrapper
dedent|''
dedent|''
name|'class'
name|'_ProtocolWrapper'
op|'('
name|'protocol'
op|'.'
name|'ProcessProtocol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This class wraps a L{Protocol} instance in a L{ProcessProtocol} instance.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'proto'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proto'
op|'='
name|'proto'
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
name|'self'
op|'.'
name|'proto'
op|'.'
name|'connectionMade'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|outReceived
name|'def'
name|'outReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
name|'self'
op|'.'
name|'proto'
op|'.'
name|'dataReceived'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|processEnded
name|'def'
name|'processEnded'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
name|'self'
op|'.'
name|'proto'
op|'.'
name|'connectionLost'
op|'('
name|'reason'
op|')'
newline|'\n'
nl|'\n'
DECL|class|_DummyTransport
dedent|''
name|'class'
name|'_DummyTransport'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'proto'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proto'
op|'='
name|'proto'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proto'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proto'
op|'.'
name|'dataReceived'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|writeSequence
dedent|''
name|'def'
name|'writeSequence'
op|'('
name|'self'
op|','
name|'seq'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'write'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'seq'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|loseConnection
dedent|''
name|'def'
name|'loseConnection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'proto'
op|'.'
name|'connectionLost'
op|'('
name|'protocol'
op|'.'
name|'connectionDone'
op|')'
newline|'\n'
nl|'\n'
DECL|function|wrapProcessProtocol
dedent|''
dedent|''
name|'def'
name|'wrapProcessProtocol'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'isinstance'
op|'('
name|'inst'
op|','
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_ProtocolWrapper'
op|'('
name|'inst'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
DECL|function|wrapProtocol
dedent|''
dedent|''
name|'def'
name|'wrapProtocol'
op|'('
name|'proto'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_DummyTransport'
op|'('
name|'proto'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
comment|'# SUPPORTED_SIGNALS is a list of signals that every session channel is supposed'
nl|'\n'
comment|'# to accept.  See RFC 4254'
nl|'\n'
DECL|variable|SUPPORTED_SIGNALS
dedent|''
name|'SUPPORTED_SIGNALS'
op|'='
op|'['
string|'"ABRT"'
op|','
string|'"ALRM"'
op|','
string|'"FPE"'
op|','
string|'"HUP"'
op|','
string|'"ILL"'
op|','
string|'"INT"'
op|','
string|'"KILL"'
op|','
nl|'\n'
string|'"PIPE"'
op|','
string|'"QUIT"'
op|','
string|'"SEGV"'
op|','
string|'"TERM"'
op|','
string|'"USR1"'
op|','
string|'"USR2"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|SSHSessionProcessProtocol
name|'class'
name|'SSHSessionProcessProtocol'
op|'('
name|'protocol'
op|'.'
name|'ProcessProtocol'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# once initialized, a dictionary mapping signal values to strings'
nl|'\n'
comment|'# that follow RFC 4254.'
nl|'\n'
DECL|variable|_signalValuesToNames
indent|'    '
name|'_signalValuesToNames'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
name|'session'
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
name|'if'
name|'self'
op|'.'
name|'session'
op|'.'
name|'buf'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'session'
op|'.'
name|'buf'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'buf'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|outReceived
dedent|''
dedent|''
name|'def'
name|'outReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|errReceived
dedent|''
name|'def'
name|'errReceived'
op|'('
name|'self'
op|','
name|'err'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'writeExtended'
op|'('
name|'connection'
op|'.'
name|'EXTENDED_DATA_STDERR'
op|','
name|'err'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inConnectionLost
dedent|''
name|'def'
name|'inConnectionLost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'conn'
op|'.'
name|'sendEOF'
op|'('
name|'self'
op|'.'
name|'session'
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
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_getSignalName
dedent|''
name|'def'
name|'_getSignalName'
op|'('
name|'self'
op|','
name|'signum'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get a signal name given a signal number.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_signalValuesToNames'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_signalValuesToNames'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|'# make sure that the POSIX ones are the defaults'
nl|'\n'
name|'for'
name|'signame'
name|'in'
name|'SUPPORTED_SIGNALS'
op|':'
newline|'\n'
indent|'                '
name|'signame'
op|'='
string|"'SIG'"
op|'+'
name|'signame'
newline|'\n'
name|'sigvalue'
op|'='
name|'getattr'
op|'('
name|'signal'
op|','
name|'signame'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'sigvalue'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_signalValuesToNames'
op|'['
name|'sigvalue'
op|']'
op|'='
name|'signame'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'signal'
op|'.'
name|'__dict__'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Check for platform specific signals, ignoring Python specific'
nl|'\n'
comment|'# SIG_DFL and SIG_IGN'
nl|'\n'
indent|'                '
name|'if'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'SIG'"
op|')'
name|'and'
name|'not'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'SIG_'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'v'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_signalValuesToNames'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'_signalValuesToNames'
op|'['
name|'v'
op|']'
op|'='
name|'k'
op|'+'
string|"'@'"
op|'+'
name|'sys'
op|'.'
name|'platform'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_signalValuesToNames'
op|'['
name|'signum'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|processEnded
dedent|''
name|'def'
name|'processEnded'
op|'('
name|'self'
op|','
name|'reason'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When we are told the process ended, try to notify the other side about\n        how the process ended using the exit-signal or exit-status requests.\n        Also, close the channel.\n        """'
newline|'\n'
name|'if'
name|'reason'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'err'
op|'='
name|'reason'
op|'.'
name|'value'
newline|'\n'
name|'if'
name|'err'
op|'.'
name|'signal'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'signame'
op|'='
name|'self'
op|'.'
name|'_getSignalName'
op|'('
name|'err'
op|'.'
name|'signal'
op|')'
newline|'\n'
name|'if'
op|'('
name|'getattr'
op|'('
name|'os'
op|','
string|"'WCOREDUMP'"
op|','
name|'None'
op|')'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'os'
op|'.'
name|'WCOREDUMP'
op|'('
name|'err'
op|'.'
name|'status'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'exitSignal: %s (core dumped)'"
op|'%'
op|'('
name|'signame'
op|','
op|')'
op|')'
newline|'\n'
name|'coreDumped'
op|'='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'exitSignal: %s'"
op|'%'
op|'('
name|'signame'
op|','
op|')'
op|')'
newline|'\n'
name|'coreDumped'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'session'
op|'.'
name|'conn'
op|'.'
name|'sendRequest'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'exit-signal'"
op|','
nl|'\n'
name|'common'
op|'.'
name|'NS'
op|'('
name|'signame'
op|'['
number|'3'
op|':'
op|']'
op|')'
op|'+'
name|'chr'
op|'('
name|'coreDumped'
op|')'
op|'+'
nl|'\n'
name|'common'
op|'.'
name|'NS'
op|'('
string|"''"
op|')'
op|'+'
name|'common'
op|'.'
name|'NS'
op|'('
string|"''"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'err'
op|'.'
name|'exitCode'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'exitCode: %r'"
op|'%'
op|'('
name|'err'
op|'.'
name|'exitCode'
op|','
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'conn'
op|'.'
name|'sendRequest'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'exit-status'"
op|','
nl|'\n'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'>L'"
op|','
name|'err'
op|'.'
name|'exitCode'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'session'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# transport stuff (we are also a transport!)'
nl|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|writeSequence
dedent|''
name|'def'
name|'writeSequence'
op|'('
name|'self'
op|','
name|'seq'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'write'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'seq'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|loseConnection
dedent|''
name|'def'
name|'loseConnection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'.'
name|'loseConnection'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|SSHSessionClient
dedent|''
dedent|''
name|'class'
name|'SSHSessionClient'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
indent|'    '
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'transport'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# methods factored out to make live easier on server writers'
nl|'\n'
DECL|function|parseRequest_pty_req
dedent|''
dedent|''
dedent|''
name|'def'
name|'parseRequest_pty_req'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the data from a pty-req request into usable data.\n\n    @returns: a tuple of (terminal type, (rows, cols, xpixel, ypixel), modes)\n    """'
newline|'\n'
name|'term'
op|','
name|'rest'
op|'='
name|'common'
op|'.'
name|'getNS'
op|'('
name|'data'
op|')'
newline|'\n'
name|'cols'
op|','
name|'rows'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'>4L'"
op|','
name|'rest'
op|'['
op|':'
number|'16'
op|']'
op|')'
newline|'\n'
name|'modes'
op|','
name|'ignored'
op|'='
name|'common'
op|'.'
name|'getNS'
op|'('
name|'rest'
op|'['
number|'16'
op|':'
op|']'
op|')'
newline|'\n'
name|'winSize'
op|'='
op|'('
name|'rows'
op|','
name|'cols'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|')'
newline|'\n'
name|'modes'
op|'='
op|'['
op|'('
name|'ord'
op|'('
name|'modes'
op|'['
name|'i'
op|']'
op|')'
op|','
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'>L'"
op|','
name|'modes'
op|'['
name|'i'
op|'+'
number|'1'
op|':'
name|'i'
op|'+'
number|'5'
op|']'
op|')'
op|'['
number|'0'
op|']'
op|')'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'modes'
op|')'
op|'-'
number|'1'
op|','
number|'5'
op|')'
op|']'
newline|'\n'
name|'return'
name|'term'
op|','
name|'winSize'
op|','
name|'modes'
newline|'\n'
nl|'\n'
DECL|function|packRequest_pty_req
dedent|''
name|'def'
name|'packRequest_pty_req'
op|'('
name|'term'
op|','
op|'('
name|'rows'
op|','
name|'cols'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|')'
op|','
name|'modes'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pack a pty-req request so that it is suitable for sending.\n\n    NOTE: modes must be packed before being sent here.\n    """'
newline|'\n'
name|'termPacked'
op|'='
name|'common'
op|'.'
name|'NS'
op|'('
name|'term'
op|')'
newline|'\n'
name|'winSizePacked'
op|'='
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'>4L'"
op|','
name|'cols'
op|','
name|'rows'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|')'
newline|'\n'
name|'modesPacked'
op|'='
name|'common'
op|'.'
name|'NS'
op|'('
name|'modes'
op|')'
comment|'# depend on the client packing modes'
newline|'\n'
name|'return'
name|'termPacked'
op|'+'
name|'winSizePacked'
op|'+'
name|'modesPacked'
newline|'\n'
nl|'\n'
DECL|function|parseRequest_window_change
dedent|''
name|'def'
name|'parseRequest_window_change'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the data from a window-change request into usuable data.\n\n    @returns: a tuple of (rows, cols, xpixel, ypixel)\n    """'
newline|'\n'
name|'cols'
op|','
name|'rows'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'>4L'"
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
name|'rows'
op|','
name|'cols'
op|','
name|'xpixel'
op|','
name|'ypixel'
newline|'\n'
nl|'\n'
DECL|function|packRequest_window_change
dedent|''
name|'def'
name|'packRequest_window_change'
op|'('
op|'('
name|'rows'
op|','
name|'cols'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pack a window-change request so that it is suitable for sending.\n    """'
newline|'\n'
name|'return'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'>4L'"
op|','
name|'cols'
op|','
name|'rows'
op|','
name|'xpixel'
op|','
name|'ypixel'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'import'
name|'connection'
newline|'\n'
endmarker|''
end_unit
