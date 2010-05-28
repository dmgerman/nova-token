begin_unit
comment|'# Copyright (c) 2001-2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.words.xish.xmlstream}.\n"""'
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
name|'trial'
name|'import'
name|'unittest'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'xish'
name|'import'
name|'domish'
op|','
name|'utility'
op|','
name|'xmlstream'
newline|'\n'
nl|'\n'
DECL|class|XmlStreamTest
name|'class'
name|'XmlStreamTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'outlist'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'='
name|'xmlstream'
op|'.'
name|'XmlStream'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'transport'
op|'='
name|'self'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'transport'
op|'.'
name|'write'
op|'='
name|'self'
op|'.'
name|'outlist'
op|'.'
name|'append'
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
string|'"""\n        Stub loseConnection because we are a transport.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'connectionLost'
op|'('
string|'"no reason"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_send
dedent|''
name|'def'
name|'test_send'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sending data should result into it being written to the transport.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'connectionMade'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'send'
op|'('
string|'"<root>"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'outlist'
op|'['
number|'0'
op|']'
op|','
string|'"<root>"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_receiveRoot
dedent|''
name|'def'
name|'test_receiveRoot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Receiving the starttag of the root element results in stream start.\n        """'
newline|'\n'
name|'streamStarted'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|streamStartEvent
name|'def'
name|'streamStartEvent'
op|'('
name|'rootelem'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'streamStarted'
op|'.'
name|'append'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addObserver'
op|'('
name|'xmlstream'
op|'.'
name|'STREAM_START_EVENT'
op|','
nl|'\n'
name|'streamStartEvent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'connectionMade'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'dataReceived'
op|'('
string|'"<root>"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'streamStarted'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_receiveBadXML
dedent|''
name|'def'
name|'test_receiveBadXML'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Receiving malformed XML should result in in error.\n        """'
newline|'\n'
name|'streamError'
op|'='
op|'['
op|']'
newline|'\n'
name|'streamEnd'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|streamErrorEvent
name|'def'
name|'streamErrorEvent'
op|'('
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'streamError'
op|'.'
name|'append'
op|'('
name|'reason'
op|')'
newline|'\n'
nl|'\n'
DECL|function|streamEndEvent
dedent|''
name|'def'
name|'streamEndEvent'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'streamEnd'
op|'.'
name|'append'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addObserver'
op|'('
name|'xmlstream'
op|'.'
name|'STREAM_ERROR_EVENT'
op|','
nl|'\n'
name|'streamErrorEvent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'addObserver'
op|'('
name|'xmlstream'
op|'.'
name|'STREAM_END_EVENT'
op|','
nl|'\n'
name|'streamEndEvent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'connectionMade'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'dataReceived'
op|'('
string|'"<root>"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'streamError'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'streamEnd'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'xmlstream'
op|'.'
name|'dataReceived'
op|'('
string|'"<child><unclosed></child>"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'streamError'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'streamError'
op|'['
number|'0'
op|']'
op|'.'
name|'check'
op|'('
name|'domish'
op|'.'
name|'ParserError'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'streamEnd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|DummyProtocol
dedent|''
dedent|''
name|'class'
name|'DummyProtocol'
op|'('
name|'protocol'
op|'.'
name|'Protocol'
op|','
name|'utility'
op|'.'
name|'EventDispatcher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    I am a protocol with an event dispatcher without further processing.\n\n    This protocol is only used for testing XmlStreamFactoryMixin to make\n    sure the bootstrap observers are added to the protocol instance.\n    """'
newline|'\n'
nl|'\n'
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
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'args'
op|'='
name|'args'
newline|'\n'
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'kwargs'
newline|'\n'
name|'self'
op|'.'
name|'observers'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'utility'
op|'.'
name|'EventDispatcher'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|BootstrapMixinTest
dedent|''
dedent|''
name|'class'
name|'BootstrapMixinTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{xmlstream.BootstrapMixin}.\n\n    @ivar factory: Instance of the factory or mixin under test.\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'factory'
op|'='
name|'xmlstream'
op|'.'
name|'BootstrapMixin'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_installBootstraps
dedent|''
name|'def'
name|'test_installBootstraps'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Dispatching an event should fire registered bootstrap observers.\n        """'
newline|'\n'
name|'called'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|cb
name|'def'
name|'cb'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'called'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dispatcher'
op|'='
name|'DummyProtocol'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'addBootstrap'
op|'('
string|"'//event/myevent'"
op|','
name|'cb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'installBootstraps'
op|'('
name|'dispatcher'
op|')'
newline|'\n'
nl|'\n'
name|'dispatcher'
op|'.'
name|'dispatch'
op|'('
name|'None'
op|','
string|"'//event/myevent'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'called'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_addAndRemoveBootstrap
dedent|''
name|'def'
name|'test_addAndRemoveBootstrap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Test addition and removal of a bootstrap event handler.\n        """'
newline|'\n'
nl|'\n'
name|'called'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|cb
name|'def'
name|'cb'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'called'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'factory'
op|'.'
name|'addBootstrap'
op|'('
string|"'//event/myevent'"
op|','
name|'cb'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'removeBootstrap'
op|'('
string|"'//event/myevent'"
op|','
name|'cb'
op|')'
newline|'\n'
nl|'\n'
name|'dispatcher'
op|'='
name|'DummyProtocol'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'installBootstraps'
op|'('
name|'dispatcher'
op|')'
newline|'\n'
nl|'\n'
name|'dispatcher'
op|'.'
name|'dispatch'
op|'('
name|'None'
op|','
string|"'//event/myevent'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'called'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|GenericXmlStreamFactoryTestsMixin
dedent|''
dedent|''
name|'class'
name|'GenericXmlStreamFactoryTestsMixin'
op|'('
name|'BootstrapMixinTest'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Generic tests for L{XmlStream} factories.\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'factory'
op|'='
name|'xmlstream'
op|'.'
name|'XmlStreamFactory'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_buildProtocolInstallsBootstraps
dedent|''
name|'def'
name|'test_buildProtocolInstallsBootstraps'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        The protocol factory installs bootstrap event handlers on the protocol.\n        """'
newline|'\n'
name|'called'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|cb
name|'def'
name|'cb'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'called'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'factory'
op|'.'
name|'addBootstrap'
op|'('
string|"'//event/myevent'"
op|','
name|'cb'
op|')'
newline|'\n'
nl|'\n'
name|'xs'
op|'='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'buildProtocol'
op|'('
name|'None'
op|')'
newline|'\n'
name|'xs'
op|'.'
name|'dispatch'
op|'('
name|'None'
op|','
string|"'//event/myevent'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'called'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_buildProtocolStoresFactory
dedent|''
name|'def'
name|'test_buildProtocolStoresFactory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        The protocol factory is saved in the protocol.\n        """'
newline|'\n'
name|'xs'
op|'='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'buildProtocol'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIdentical'
op|'('
name|'self'
op|'.'
name|'factory'
op|','
name|'xs'
op|'.'
name|'factory'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|XmlStreamFactoryMixinTest
dedent|''
dedent|''
name|'class'
name|'XmlStreamFactoryMixinTest'
op|'('
name|'GenericXmlStreamFactoryTestsMixin'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{xmlstream.XmlStreamFactoryMixin}.\n    """'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'factory'
op|'='
name|'xmlstream'
op|'.'
name|'XmlStreamFactoryMixin'
op|'('
name|'None'
op|','
name|'test'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'.'
name|'protocol'
op|'='
name|'DummyProtocol'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_buildProtocolFactoryArguments
dedent|''
name|'def'
name|'test_buildProtocolFactoryArguments'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Arguments passed to the factory should be passed to protocol on\n        instantiation.\n        """'
newline|'\n'
name|'xs'
op|'='
name|'self'
op|'.'
name|'factory'
op|'.'
name|'buildProtocol'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'('
name|'None'
op|','
op|')'
op|','
name|'xs'
op|'.'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'{'
string|"'test'"
op|':'
name|'None'
op|'}'
op|','
name|'xs'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
