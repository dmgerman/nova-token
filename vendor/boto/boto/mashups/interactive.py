begin_unit
comment|'# Copyright (C) 2003-2007  Robey Pointer <robey@lag.net>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This file is part of paramiko.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Paramiko is free software; you can redistribute it and/or modify it under the'
nl|'\n'
comment|'# terms of the GNU Lesser General Public License as published by the Free'
nl|'\n'
comment|'# Software Foundation; either version 2.1 of the License, or (at your option)'
nl|'\n'
comment|'# any later version.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Paramiko is distrubuted in the hope that it will be useful, but WITHOUT ANY'
nl|'\n'
comment|'# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR'
nl|'\n'
comment|'# A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more'
nl|'\n'
comment|'# details.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# You should have received a copy of the GNU Lesser General Public License'
nl|'\n'
comment|'# along with Paramiko; if not, write to the Free Software Foundation, Inc.,'
nl|'\n'
comment|'# 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
comment|'# windows does not have termios...'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'termios'
newline|'\n'
name|'import'
name|'tty'
newline|'\n'
DECL|variable|has_termios
name|'has_termios'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|has_termios
indent|'    '
name|'has_termios'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|interactive_shell
dedent|''
name|'def'
name|'interactive_shell'
op|'('
name|'chan'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'has_termios'
op|':'
newline|'\n'
indent|'        '
name|'posix_shell'
op|'('
name|'chan'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'windows_shell'
op|'('
name|'chan'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|posix_shell
dedent|''
dedent|''
name|'def'
name|'posix_shell'
op|'('
name|'chan'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'select'
newline|'\n'
nl|'\n'
name|'oldtty'
op|'='
name|'termios'
op|'.'
name|'tcgetattr'
op|'('
name|'sys'
op|'.'
name|'stdin'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'tty'
op|'.'
name|'setraw'
op|'('
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
newline|'\n'
name|'tty'
op|'.'
name|'setcbreak'
op|'('
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
newline|'\n'
name|'chan'
op|'.'
name|'settimeout'
op|'('
number|'0.0'
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|','
name|'w'
op|','
name|'e'
op|'='
name|'select'
op|'.'
name|'select'
op|'('
op|'['
name|'chan'
op|','
name|'sys'
op|'.'
name|'stdin'
op|']'
op|','
op|'['
op|']'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'chan'
name|'in'
name|'r'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'x'
op|'='
name|'chan'
op|'.'
name|'recv'
op|'('
number|'1024'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'x'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                        '
name|'print'
string|"'\\r\\n*** EOF\\r\\n'"
op|','
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'x'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'timeout'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'sys'
op|'.'
name|'stdin'
name|'in'
name|'r'
op|':'
newline|'\n'
indent|'                '
name|'x'
op|'='
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'x'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'chan'
op|'.'
name|'send'
op|'('
name|'x'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'termios'
op|'.'
name|'tcsetattr'
op|'('
name|'sys'
op|'.'
name|'stdin'
op|','
name|'termios'
op|'.'
name|'TCSADRAIN'
op|','
name|'oldtty'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# thanks to Mike Looijmans for this code'
nl|'\n'
DECL|function|windows_shell
dedent|''
dedent|''
name|'def'
name|'windows_shell'
op|'('
name|'chan'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'threading'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
string|'"Line-buffered terminal emulation. Press F6 or ^Z to send EOF.\\r\\n\\r\\n"'
op|')'
newline|'\n'
nl|'\n'
DECL|function|writeall
name|'def'
name|'writeall'
op|'('
name|'sock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'sock'
op|'.'
name|'recv'
op|'('
number|'256'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
string|"'\\r\\n*** EOF ***\\r\\n\\r\\n'"
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'writer'
op|'='
name|'threading'
op|'.'
name|'Thread'
op|'('
name|'target'
op|'='
name|'writeall'
op|','
name|'args'
op|'='
op|'('
name|'chan'
op|','
op|')'
op|')'
newline|'\n'
name|'writer'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'='
name|'sys'
op|'.'
name|'stdin'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'d'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'chan'
op|'.'
name|'send'
op|'('
name|'d'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'EOFError'
op|':'
newline|'\n'
comment|'# user hit ^Z or F6'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
