begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nAn example of using the rotating log.\n"""'
newline|'\n'
nl|'\n'
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
name|'python'
name|'import'
name|'logfile'
newline|'\n'
nl|'\n'
comment|'# rotate every 100 bytes'
nl|'\n'
DECL|variable|f
name|'f'
op|'='
name|'logfile'
op|'.'
name|'LogFile'
op|'('
string|'"test.log"'
op|','
string|'"/tmp"'
op|','
name|'rotateLength'
op|'='
number|'100'
op|')'
newline|'\n'
nl|'\n'
comment|'# setup logging to use our new logfile'
nl|'\n'
name|'log'
op|'.'
name|'startLogging'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
comment|'# print a few message'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'log'
op|'.'
name|'msg'
op|'('
string|'"this is a test of the logfile: %s"'
op|'%'
name|'i'
op|')'
newline|'\n'
nl|'\n'
comment|'# rotate the logfile manually'
nl|'\n'
dedent|''
name|'f'
op|'.'
name|'rotate'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|'"goodbye"'
op|')'
newline|'\n'
endmarker|''
end_unit
