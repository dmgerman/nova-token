begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
op|','
name|'reactor'
op|','
name|'error'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
op|','
name|'components'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'pair'
name|'import'
name|'ethernet'
op|','
name|'raw'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
DECL|class|MyProtocol
name|'class'
name|'MyProtocol'
op|':'
newline|'\n'
indent|'    '
name|'implements'
op|'('
name|'raw'
op|'.'
name|'IRawPacketProtocol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'expecting'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'expecting'
op|'='
name|'list'
op|'('
name|'expecting'
op|')'
newline|'\n'
nl|'\n'
DECL|member|datagramReceived
dedent|''
name|'def'
name|'datagramReceived'
op|'('
name|'self'
op|','
name|'data'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'assert'
name|'self'
op|'.'
name|'expecting'
op|','
string|"'Got a packet when not expecting anymore.'"
newline|'\n'
name|'expect'
op|'='
name|'self'
op|'.'
name|'expecting'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
name|'assert'
name|'expect'
op|'=='
op|'('
name|'data'
op|','
name|'kw'
op|')'
op|','
string|'"Expected %r, got %r"'
op|'%'
op|'('
nl|'\n'
name|'expect'
op|','
op|'('
name|'data'
op|','
name|'kw'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|class|EthernetTestCase
dedent|''
dedent|''
name|'class'
name|'EthernetTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|testPacketParsing
indent|'    '
name|'def'
name|'testPacketParsing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proto'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'p1'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0800'
op|','
name|'p1'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x00foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'assert'
name|'not'
name|'p1'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p1'
op|'.'
name|'expecting'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|testMultiplePackets
dedent|''
name|'def'
name|'testMultiplePackets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proto'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'p1'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
string|"'quux'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"012345"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"abcdef"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0800'
op|','
name|'p1'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x00foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"012345abcdef\\x08\\x00quux"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'assert'
name|'not'
name|'p1'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p1'
op|'.'
name|'expecting'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|testMultipleSameProtos
dedent|''
name|'def'
name|'testMultipleSameProtos'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proto'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'p1'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'p2'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0800'
op|','
name|'p1'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0800'
op|','
name|'p2'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x00foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'assert'
name|'not'
name|'p1'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p1'
op|'.'
name|'expecting'
newline|'\n'
name|'assert'
name|'not'
name|'p2'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p2'
op|'.'
name|'expecting'
newline|'\n'
nl|'\n'
DECL|member|testWrongProtoNotSeen
dedent|''
name|'def'
name|'testWrongProtoNotSeen'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proto'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'p1'
op|'='
name|'MyProtocol'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0801'
op|','
name|'p1'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x00foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"012345abcdef\\x08\\x00quux"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testDemuxing
dedent|''
name|'def'
name|'testDemuxing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proto'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'p1'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
string|"'quux'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"012345"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"abcdef"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0800'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0800'
op|','
name|'p1'
op|')'
newline|'\n'
nl|'\n'
name|'p2'
op|'='
name|'MyProtocol'
op|'('
op|'['
nl|'\n'
nl|'\n'
op|'('
string|"'quux'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"012345"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"abcdef"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0806'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
string|"'foobar'"
op|','
op|'{'
nl|'\n'
string|"'partial'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'dest'"
op|':'
string|'"123456"'
op|','
nl|'\n'
string|"'source'"
op|':'
string|'"987654"'
op|','
nl|'\n'
string|"'protocol'"
op|':'
number|'0x0806'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'addProto'
op|'('
number|'0x0806'
op|','
name|'p2'
op|')'
newline|'\n'
nl|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x00foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"012345abcdef\\x08\\x06quux"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'1'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"123456987654\\x08\\x06foobar"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'0'
op|')'
newline|'\n'
name|'proto'
op|'.'
name|'datagramReceived'
op|'('
string|'"012345abcdef\\x08\\x00quux"'
op|','
nl|'\n'
name|'partial'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'assert'
name|'not'
name|'p1'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p1'
op|'.'
name|'expecting'
newline|'\n'
name|'assert'
name|'not'
name|'p2'
op|'.'
name|'expecting'
op|','
string|"'Should not expect any more packets, but still want %r'"
op|'%'
name|'p2'
op|'.'
name|'expecting'
newline|'\n'
nl|'\n'
DECL|member|testAddingBadProtos_WrongLevel
dedent|''
name|'def'
name|'testAddingBadProtos_WrongLevel'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding a wrong level protocol raises an exception."""'
newline|'\n'
name|'e'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'e'
op|'.'
name|'addProto'
op|'('
number|'42'
op|','
string|'"silliness"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'components'
op|'.'
name|'CannotAdapt'
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
name|'raise'
name|'AssertionError'
op|','
string|"'addProto must raise an exception for bad protocols'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|testAddingBadProtos_TooSmall
dedent|''
dedent|''
name|'def'
name|'testAddingBadProtos_TooSmall'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding a protocol with a negative number raises an exception."""'
newline|'\n'
name|'e'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'e'
op|'.'
name|'addProto'
op|'('
op|'-'
number|'1'
op|','
name|'MyProtocol'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'args'
op|'=='
op|'('
string|"'Added protocol must be positive or zero'"
op|','
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AssertionError'
op|','
string|"'addProto must raise an exception for bad protocols'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|testAddingBadProtos_TooBig
dedent|''
dedent|''
name|'def'
name|'testAddingBadProtos_TooBig'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding a protocol with a number >=2**16 raises an exception."""'
newline|'\n'
name|'e'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'e'
op|'.'
name|'addProto'
op|'('
number|'2'
op|'**'
number|'16'
op|','
name|'MyProtocol'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'args'
op|'=='
op|'('
string|"'Added protocol must fit in 16 bits'"
op|','
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AssertionError'
op|','
string|"'addProto must raise an exception for bad protocols'"
newline|'\n'
nl|'\n'
DECL|member|testAddingBadProtos_TooBig2
dedent|''
dedent|''
name|'def'
name|'testAddingBadProtos_TooBig2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding a protocol with a number >=2**16 raises an exception."""'
newline|'\n'
name|'e'
op|'='
name|'ethernet'
op|'.'
name|'EthernetProtocol'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'e'
op|'.'
name|'addProto'
op|'('
number|'2'
op|'**'
number|'16'
op|'+'
number|'1'
op|','
name|'MyProtocol'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'args'
op|'=='
op|'('
string|"'Added protocol must fit in 16 bits'"
op|','
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AssertionError'
op|','
string|"'addProto must raise an exception for bad protocols'"
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
