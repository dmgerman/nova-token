begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nSerial port support for Windows.\n\nRequires PySerial and win32all, and needs to be used with win32event\nreactor.\n"""'
newline|'\n'
nl|'\n'
comment|'# system imports'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
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
name|'import'
name|'win32file'
op|','
name|'win32event'
newline|'\n'
nl|'\n'
comment|'# twisted imports'
nl|'\n'
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
name|'abstract'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
newline|'\n'
nl|'\n'
comment|'# sibling imports'
nl|'\n'
name|'from'
name|'serialport'
name|'import'
name|'BaseSerialPort'
newline|'\n'
nl|'\n'
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
string|'"""A select()able serial device, acting as a transport."""'
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
nl|'\n'
name|'bytesize'
op|'='
name|'bytesize'
op|','
name|'parity'
op|'='
name|'parity'
op|','
nl|'\n'
name|'stopbits'
op|'='
name|'stopbits'
op|','
name|'timeout'
op|'='
name|'None'
op|','
nl|'\n'
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
name|'reactor'
op|'='
name|'reactor'
newline|'\n'
name|'self'
op|'.'
name|'protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'outQueue'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'closed'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'closedNotifies'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'writeInProgress'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'_overlappedRead'
op|'='
name|'win32file'
op|'.'
name|'OVERLAPPED'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_overlappedRead'
op|'.'
name|'hEvent'
op|'='
name|'win32event'
op|'.'
name|'CreateEvent'
op|'('
name|'None'
op|','
number|'1'
op|','
number|'0'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_overlappedWrite'
op|'='
name|'win32file'
op|'.'
name|'OVERLAPPED'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_overlappedWrite'
op|'.'
name|'hEvent'
op|'='
name|'win32event'
op|'.'
name|'CreateEvent'
op|'('
name|'None'
op|','
number|'0'
op|','
number|'0'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'reactor'
op|'.'
name|'addEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedRead'
op|'.'
name|'hEvent'
op|','
name|'self'
op|','
string|"'serialReadEvent'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reactor'
op|'.'
name|'addEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedWrite'
op|'.'
name|'hEvent'
op|','
name|'self'
op|','
string|"'serialWriteEvent'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'makeConnection'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|','
name|'comstat'
op|'='
name|'win32file'
op|'.'
name|'ClearCommError'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|')'
newline|'\n'
name|'rc'
op|','
name|'self'
op|'.'
name|'read_buf'
op|'='
name|'win32file'
op|'.'
name|'ReadFile'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
nl|'\n'
name|'win32file'
op|'.'
name|'AllocateReadBuffer'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_overlappedRead'
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialReadEvent
dedent|''
name|'def'
name|'serialReadEvent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'#get that character we set up'
nl|'\n'
indent|'        '
name|'n'
op|'='
name|'win32file'
op|'.'
name|'GetOverlappedResult'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
name|'self'
op|'.'
name|'_overlappedRead'
op|','
number|'0'
op|')'
newline|'\n'
name|'if'
name|'n'
op|':'
newline|'\n'
indent|'            '
name|'first'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'read_buf'
op|'['
op|':'
name|'n'
op|']'
op|')'
newline|'\n'
comment|'#now we should get everything that is already in the buffer'
nl|'\n'
name|'flags'
op|','
name|'comstat'
op|'='
name|'win32file'
op|'.'
name|'ClearCommError'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|')'
newline|'\n'
name|'if'
name|'comstat'
op|'.'
name|'cbInQue'
op|':'
newline|'\n'
indent|'                '
name|'win32event'
op|'.'
name|'ResetEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedRead'
op|'.'
name|'hEvent'
op|')'
newline|'\n'
name|'rc'
op|','
name|'buf'
op|'='
name|'win32file'
op|'.'
name|'ReadFile'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
nl|'\n'
name|'win32file'
op|'.'
name|'AllocateReadBuffer'
op|'('
name|'comstat'
op|'.'
name|'cbInQue'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_overlappedRead'
op|')'
newline|'\n'
name|'n'
op|'='
name|'win32file'
op|'.'
name|'GetOverlappedResult'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
name|'self'
op|'.'
name|'_overlappedRead'
op|','
number|'1'
op|')'
newline|'\n'
comment|'#handle all the received data:'
nl|'\n'
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'dataReceived'
op|'('
name|'first'
op|'+'
name|'str'
op|'('
name|'buf'
op|'['
op|':'
name|'n'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'#handle all the received data:'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'protocol'
op|'.'
name|'dataReceived'
op|'('
name|'first'
op|')'
newline|'\n'
nl|'\n'
comment|'#set up next one'
nl|'\n'
dedent|''
dedent|''
name|'win32event'
op|'.'
name|'ResetEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedRead'
op|'.'
name|'hEvent'
op|')'
newline|'\n'
name|'rc'
op|','
name|'self'
op|'.'
name|'read_buf'
op|'='
name|'win32file'
op|'.'
name|'ReadFile'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
nl|'\n'
name|'win32file'
op|'.'
name|'AllocateReadBuffer'
op|'('
number|'1'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_overlappedRead'
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
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'writeInProgress'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'outQueue'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'writeInProgress'
op|'='
number|'1'
newline|'\n'
name|'win32file'
op|'.'
name|'WriteFile'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
name|'data'
op|','
name|'self'
op|'.'
name|'_overlappedWrite'
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialWriteEvent
dedent|''
dedent|''
dedent|''
name|'def'
name|'serialWriteEvent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'dataToWrite'
op|'='
name|'self'
op|'.'
name|'outQueue'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'writeInProgress'
op|'='
number|'0'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'win32file'
op|'.'
name|'WriteFile'
op|'('
name|'self'
op|'.'
name|'_serial'
op|'.'
name|'hComPort'
op|','
name|'dataToWrite'
op|','
name|'self'
op|'.'
name|'_overlappedWrite'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connectionLost
dedent|''
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
name|'reactor'
op|'.'
name|'removeEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedRead'
op|'.'
name|'hEvent'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'reactor'
op|'.'
name|'removeEvent'
op|'('
name|'self'
op|'.'
name|'_overlappedWrite'
op|'.'
name|'hEvent'
op|')'
newline|'\n'
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
