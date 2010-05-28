begin_unit
comment|'# -*- test-case-name: twisted.test.test_stringtransport -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2010 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nAssorted functionality which is commonly useful when writing unit tests.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'StringIO'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
op|'.'
name|'verify'
name|'import'
name|'verifyObject'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'interfaces'
name|'import'
name|'ITransport'
op|','
name|'IConsumer'
op|','
name|'IPushProducer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'interfaces'
name|'import'
name|'IReactorTCP'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'basic'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
op|','
name|'error'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccumulatingProtocol
name|'class'
name|'AccumulatingProtocol'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    L{AccumulatingProtocol} is an L{IProtocol} implementation which collects\n    the data delivered to it and can fire a Deferred when it is connected or\n    disconnected.\n\n    @ivar made: A flag indicating whether C{connectionMade} has been called.\n    @ivar data: A string giving all the data passed to C{dataReceived}.\n    @ivar closed: A flag indicated whether C{connectionLost} has been called.\n    @ivar closedReason: The value of the I{reason} parameter passed to\n        C{connectionLost}.\n    @ivar closedDeferred: If set to a L{Deferred}, this will be fired when\n        C{connectionLost} is called.\n    """'
newline|'\n'
name|'made'
op|'='
name|'closed'
op|'='
number|'0'
newline|'\n'
DECL|variable|closedReason
name|'closedReason'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|closedDeferred
name|'closedDeferred'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|data
name|'data'
op|'='
string|'""'
newline|'\n'
nl|'\n'
DECL|variable|factory
name|'factory'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|connectionMade
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
name|'made'
op|'='
number|'1'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'factory'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'protocolConnectionMade'
name|'is'
name|'not'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'protocolConnectionMade'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'protocolConnectionMade'
op|'='
name|'None'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'self'
op|')'
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
name|'self'
op|'.'
name|'data'
op|'+='
name|'data'
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
name|'closed'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'closedReason'
op|'='
name|'reason'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'closedDeferred'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|','
name|'self'
op|'.'
name|'closedDeferred'
op|'='
name|'self'
op|'.'
name|'closedDeferred'
op|','
name|'None'
newline|'\n'
name|'d'
op|'.'
name|'callback'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LineSendingProtocol
dedent|''
dedent|''
dedent|''
name|'class'
name|'LineSendingProtocol'
op|'('
name|'basic'
op|'.'
name|'LineReceiver'
op|')'
op|':'
newline|'\n'
DECL|variable|lostConn
indent|'    '
name|'lostConn'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'lines'
op|','
name|'start'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'lines'
op|'='
name|'lines'
op|'['
op|':'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'response'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'start'
op|'='
name|'start'
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
name|'start'
op|':'
newline|'\n'
indent|'            '
name|'map'
op|'('
name|'self'
op|'.'
name|'sendLine'
op|','
name|'self'
op|'.'
name|'lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lineReceived
dedent|''
dedent|''
name|'def'
name|'lineReceived'
op|'('
name|'self'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'start'
op|':'
newline|'\n'
indent|'            '
name|'map'
op|'('
name|'self'
op|'.'
name|'sendLine'
op|','
name|'self'
op|'.'
name|'lines'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lines'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'response'
op|'.'
name|'append'
op|'('
name|'line'
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
name|'lostConn'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDatagramTransport
dedent|''
dedent|''
name|'class'
name|'FakeDatagramTransport'
op|':'
newline|'\n'
DECL|variable|noAddr
indent|'    '
name|'noAddr'
op|'='
name|'object'
op|'('
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
name|'written'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'packet'
op|','
name|'addr'
op|'='
name|'noAddr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'written'
op|'.'
name|'append'
op|'('
op|'('
name|'packet'
op|','
name|'addr'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StringTransport
dedent|''
dedent|''
name|'class'
name|'StringTransport'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A transport implementation which buffers data in memory and keeps track of\n    its other state without providing any behavior.\n\n    L{StringTransport} has a number of attributes which are not part of any of\n    the interfaces it claims to implement.  These attributes are provided for\n    testing purposes.  Implementation code should not use any of these\n    attributes; they are not provided by other transports.\n\n    @ivar disconnecting: A C{bool} which is C{False} until L{loseConnection} is\n        called, then C{True}.\n\n    @ivar producer: If a producer is currently registered, C{producer} is a\n        reference to it.  Otherwise, C{None}.\n\n    @ivar streaming: If a producer is currently registered, C{streaming} refers\n        to the value of the second parameter passed to C{registerProducer}.\n\n    @ivar hostAddr: C{None} or an object which will be returned as the host\n        address of this transport.  If C{None}, a nasty tuple will be returned\n        instead.\n\n    @ivar peerAddr: C{None} or an object which will be returned as the peer\n        address of this transport.  If C{None}, a nasty tuple will be returned\n        instead.\n\n    @ivar producerState: The state of this L{StringTransport} in its capacity\n        as an L{IPushProducer}.  One of C{\'producing\'}, C{\'paused\'}, or\n        C{\'stopped\'}.\n\n    @ivar io: A L{StringIO} which holds the data which has been written to this\n        transport since the last call to L{clear}.  Use L{value} instead of\n        accessing this directly.\n    """'
newline|'\n'
name|'implements'
op|'('
name|'ITransport'
op|','
name|'IConsumer'
op|','
name|'IPushProducer'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|disconnecting
name|'disconnecting'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|variable|producer
name|'producer'
op|'='
name|'None'
newline|'\n'
DECL|variable|streaming
name|'streaming'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|hostAddr
name|'hostAddr'
op|'='
name|'None'
newline|'\n'
DECL|variable|peerAddr
name|'peerAddr'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|producerState
name|'producerState'
op|'='
string|"'producing'"
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'hostAddress'
op|'='
name|'None'
op|','
name|'peerAddress'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
name|'if'
name|'hostAddress'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hostAddr'
op|'='
name|'hostAddress'
newline|'\n'
dedent|''
name|'if'
name|'peerAddress'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'peerAddr'
op|'='
name|'peerAddress'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'connected'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Discard all data written to this transport so far.\n\n        This is not a transport method.  It is intended for tests.  Do not use\n        it in implementation code.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'io'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|value
dedent|''
name|'def'
name|'value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Retrieve all data which has been buffered by this transport.\n\n        This is not a transport method.  It is intended for tests.  Do not use\n        it in implementation code.\n\n        @return: A C{str} giving all data written to this transport since the\n            last call to L{clear}.\n        @rtype: C{str}\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'io'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# ITransport'
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
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'unicode'
op|')'
op|':'
comment|'# no, really, I mean it'
newline|'\n'
indent|'            '
name|'raise'
name|'TypeError'
op|'('
string|'"Data must not be unicode"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'io'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|writeSequence
dedent|''
name|'def'
name|'writeSequence'
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
name|'io'
op|'.'
name|'write'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
string|'"""\n        Close the connection. Does nothing besides toggle the C{disconnecting}\n        instance variable to C{True}.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'disconnecting'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getPeer
dedent|''
name|'def'
name|'getPeer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'peerAddr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|"'StringIO'"
op|','
name|'repr'
op|'('
name|'self'
op|'.'
name|'io'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'peerAddr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|getHost
dedent|''
name|'def'
name|'getHost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'hostAddr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|"'StringIO'"
op|','
name|'repr'
op|'('
name|'self'
op|'.'
name|'io'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'hostAddr'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# IConsumer'
nl|'\n'
DECL|member|registerProducer
dedent|''
name|'def'
name|'registerProducer'
op|'('
name|'self'
op|','
name|'producer'
op|','
name|'streaming'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'producer'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"Cannot register two producers"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'producer'
op|'='
name|'producer'
newline|'\n'
name|'self'
op|'.'
name|'streaming'
op|'='
name|'streaming'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|unregisterProducer
dedent|''
name|'def'
name|'unregisterProducer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'producer'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
string|'"Cannot unregister a producer unless one is registered"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'producer'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'streaming'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# IPushProducer'
nl|'\n'
DECL|member|_checkState
dedent|''
name|'def'
name|'_checkState'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'disconnecting'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
string|'"Cannot resume producing after loseConnection"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'producerState'
op|'=='
string|"'stopped'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"Cannot resume a stopped producer"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|pauseProducing
dedent|''
dedent|''
name|'def'
name|'pauseProducing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_checkState'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'producerState'
op|'='
string|"'paused'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|stopProducing
dedent|''
name|'def'
name|'stopProducing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'producerState'
op|'='
string|"'stopped'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|resumeProducing
dedent|''
name|'def'
name|'resumeProducing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_checkState'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'producerState'
op|'='
string|"'producing'"
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|StringTransportWithDisconnection
dedent|''
dedent|''
name|'class'
name|'StringTransportWithDisconnection'
op|'('
name|'StringTransport'
op|')'
op|':'
newline|'\n'
DECL|member|loseConnection
indent|'    '
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
name|'connected'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'connected'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'connectionLost'
op|'('
name|'error'
op|'.'
name|'ConnectionDone'
op|'('
string|'"Bye."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|StringIOWithoutClosing
dedent|''
dedent|''
dedent|''
name|'class'
name|'StringIOWithoutClosing'
op|'('
name|'StringIO'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A StringIO that can\'t be closed.\n    """'
newline|'\n'
DECL|member|close
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Do nothing.\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MemoryReactor
dedent|''
dedent|''
name|'class'
name|'MemoryReactor'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A fake reactor to be used in tests.  This reactor doesn\'t actually do\n    much that\'s useful yet.  It accepts TCP connection setup attempts, but\n    they will never succeed.\n\n    @ivar tcpClients: a list that keeps track of connection attempts (ie, calls\n        to C{connectTCP}).\n    @type tcpClients: C{list}\n\n    @ivar tcpServers: a list that keeps track of server listen attempts (ie, calls\n        to C{listenTCP}).\n    @type tcpServers: C{list}\n    """'
newline|'\n'
name|'implements'
op|'('
name|'IReactorTCP'
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
string|'"""\n        Initialize the tracking lists.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'tcpClients'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tcpServers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|listenTCP
dedent|''
name|'def'
name|'listenTCP'
op|'('
name|'self'
op|','
name|'port'
op|','
name|'factory'
op|','
name|'backlog'
op|'='
number|'50'
op|','
name|'interface'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Fake L{reactor.listenTCP}, that does nothing but log the call.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'tcpServers'
op|'.'
name|'append'
op|'('
op|'('
name|'port'
op|','
name|'factory'
op|','
name|'backlog'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|connectTCP
dedent|''
name|'def'
name|'connectTCP'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'factory'
op|','
name|'timeout'
op|'='
number|'30'
op|','
name|'bindAddress'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Fake L{reactor.connectTCP}, that does nothing but log the call.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'tcpClients'
op|'.'
name|'append'
op|'('
op|'('
name|'host'
op|','
name|'port'
op|','
name|'factory'
op|','
name|'timeout'
op|','
name|'bindAddress'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'verifyObject'
op|'('
name|'IReactorTCP'
op|','
name|'MemoryReactor'
op|'('
op|')'
op|')'
newline|'\n'
endmarker|''
end_unit
