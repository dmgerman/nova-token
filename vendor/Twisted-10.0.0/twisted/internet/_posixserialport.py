begin_unit
comment|'# Copyright (c) 2001-2007 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nSerial Port Protocol\n"""'
newline|'\n'
nl|'\n'
comment|'# system imports'
nl|'\n'
name|'import'
name|'os'
op|','
name|'errno'
newline|'\n'
nl|'\n'
comment|'# dependent on pyserial ( http://pyserial.sf.net/ )'
nl|'\n'
comment|'# only tested w/ 1.18 (5 Dec 2002)'
nl|'\n'
name|'import'
name|'serial'
newline|'\n'
name|'from'
name|'serial'
name|'import'
name|'PARITY_NONE'
op|','
name|'PARITY_EVEN'
op|','
name|'PARITY_ODD'
newline|'\n'
name|'from'
name|'serial'
name|'import'
name|'STOPBITS_ONE'
op|','
name|'STOPBITS_TWO'
newline|'\n'
name|'from'
name|'serial'
name|'import'
name|'FIVEBITS'
op|','
name|'SIXBITS'
op|','
name|'SEVENBITS'
op|','
name|'EIGHTBITS'
newline|'\n'
nl|'\n'
name|'from'
name|'serialport'
name|'import'
name|'BaseSerialPort'
newline|'\n'
nl|'\n'
comment|'# twisted imports'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'abstract'
op|','
name|'fdesc'
op|','
name|'main'
newline|'\n'
nl|'\n'
DECL|class|SerialPort
name|'class'
name|'SerialPort'
op|'('
name|'BaseSerialPort'
op|','
name|'abstract'
op|'.'
name|'FileDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A select()able serial device, acting as a transport.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|connected
name|'connected'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'protocol'
op|','
name|'deviceNameOrPortNumber'
op|','
name|'reactor'
op|','
nl|'\n'
name|'baudrate'
op|'='
number|'9600'
op|','
name|'bytesize'
op|'='
name|'EIGHTBITS'
op|','
name|'parity'
op|'='
name|'PARITY_NONE'
op|','
nl|'\n'
name|'stopbits'
op|'='
name|'STOPBITS_ONE'
op|','
name|'timeout'
op|'='
number|'0'
op|','
name|'xonxoff'
op|'='
number|'0'
op|','
name|'rtscts'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'abstract'
op|'.'
name|'FileDescriptor'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'reactor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_serial'
op|'='
name|'serial'
op|'.'
name|'Serial'
op|'('
name|'deviceNameOrPortNumber'
op|','
name|'baudrate'
op|'='
name|'baudrate'
op|','
name|'bytesize'
op|'='
name|'bytesize'
op|','
name|'parity'
op|'='
name|'parity'
op|','
name|'stopbits'
op|'='
name|'stopbits'
op|','
name|'timeout'
op|'='
name|'timeout'
op|','
name|'xonxoff'
op|'='
name|'xonxoff'
op|','
name|'rtscts'
op|'='
name|'rtscts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reactor'
op|'='
name|'reactor'
newline|'\n'
name|'self'
op|'.'
name|'flushInput'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flushOutput'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'makeConnection'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'startReading'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|fileno
dedent|''
name|'def'
name|'fileno'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'fd'
newline|'\n'
nl|'\n'
DECL|member|writeSomeData
dedent|''
name|'def'
name|'writeSomeData'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Write some data to the serial device.\n        """'
newline|'\n'
name|'return'
name|'fdesc'
op|'.'
name|'writeToFD'
op|'('
name|'self'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|doRead
dedent|''
name|'def'
name|'doRead'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Some data\'s readable from serial device.\n        """'
newline|'\n'
name|'return'
name|'fdesc'
op|'.'
name|'readFromFD'
op|'('
name|'self'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'dataReceived'
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
name|'abstract'
op|'.'
name|'FileDescriptor'
op|'.'
name|'connectionLost'
op|'('
name|'self'
op|','
name|'reason'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
