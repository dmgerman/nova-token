begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
comment|'# '
nl|'\n'
comment|'# -*- test-case-name: twisted.test.test_journal -*-'
nl|'\n'
nl|'\n'
string|'"""Logging that uses pickles.\n\nTODO: add log that logs to a file.\n"""'
newline|'\n'
nl|'\n'
comment|'# twisted imports'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'persisted'
name|'import'
name|'dirdbm'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
newline|'\n'
nl|'\n'
comment|'# sibling imports'
nl|'\n'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirDBMLog
name|'class'
name|'DirDBMLog'
op|':'
newline|'\n'
indent|'    '
string|'"""Log pickles to DirDBM directory."""'
newline|'\n'
nl|'\n'
name|'implements'
op|'('
name|'base'
op|'.'
name|'ICommandLog'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'logPath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'='
name|'dirdbm'
op|'.'
name|'Shelf'
op|'('
name|'logPath'
op|')'
newline|'\n'
name|'indexs'
op|'='
name|'map'
op|'('
name|'int'
op|','
name|'self'
op|'.'
name|'db'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'indexs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'currentIndex'
op|'='
name|'max'
op|'('
name|'indexs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'currentIndex'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|logCommand
dedent|''
dedent|''
name|'def'
name|'logCommand'
op|'('
name|'self'
op|','
name|'command'
op|','
name|'time'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Log a command."""'
newline|'\n'
name|'self'
op|'.'
name|'currentIndex'
op|'+='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'['
name|'str'
op|'('
name|'self'
op|'.'
name|'currentIndex'
op|')'
op|']'
op|'='
op|'('
name|'time'
op|','
name|'command'
op|')'
newline|'\n'
name|'return'
name|'defer'
op|'.'
name|'succeed'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getCurrentIndex
dedent|''
name|'def'
name|'getCurrentIndex'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return index of last command logged."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'currentIndex'
newline|'\n'
nl|'\n'
DECL|member|getCommandsSince
dedent|''
name|'def'
name|'getCommandsSince'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'index'
op|','
name|'self'
op|'.'
name|'currentIndex'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'db'
op|'['
name|'str'
op|'('
name|'i'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
