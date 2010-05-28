begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|getNumber
name|'def'
name|'getNumber'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|function|getReference
dedent|''
name|'def'
name|'getReference'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|class|Book
dedent|''
name|'class'
name|'Book'
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
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'chapters'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'indexFilename'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'global'
name|'Chapter'
newline|'\n'
name|'Chapter'
op|'='
name|'self'
op|'.'
name|'Chapter'
newline|'\n'
name|'global'
name|'getNumber'
newline|'\n'
name|'getNumber'
op|'='
name|'self'
op|'.'
name|'getNumber'
newline|'\n'
name|'global'
name|'getReference'
newline|'\n'
name|'getReference'
op|'='
name|'self'
op|'.'
name|'getNumber'
newline|'\n'
name|'global'
name|'Index'
newline|'\n'
name|'Index'
op|'='
name|'self'
op|'.'
name|'Index'
newline|'\n'
nl|'\n'
name|'if'
name|'filename'
op|':'
newline|'\n'
indent|'            '
name|'execfile'
op|'('
name|'filename'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getFiles
dedent|''
dedent|''
name|'def'
name|'getFiles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'c'
op|'['
number|'0'
op|']'
name|'for'
name|'c'
name|'in'
name|'self'
op|'.'
name|'chapters'
op|']'
newline|'\n'
nl|'\n'
DECL|member|getNumber
dedent|''
name|'def'
name|'getNumber'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'c'
name|'in'
name|'self'
op|'.'
name|'chapters'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'c'
op|'['
number|'0'
op|']'
op|'=='
name|'filename'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'c'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|getIndexFilename
dedent|''
name|'def'
name|'getIndexFilename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'indexFilename'
newline|'\n'
nl|'\n'
DECL|member|Chapter
dedent|''
name|'def'
name|'Chapter'
op|'('
name|'self'
op|','
name|'filename'
op|','
name|'number'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'chapters'
op|'.'
name|'append'
op|'('
op|'('
name|'filename'
op|','
name|'number'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|Index
dedent|''
name|'def'
name|'Index'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'indexFilename'
op|'='
name|'filename'
newline|'\n'
nl|'\n'
comment|'#_book = Book(None)'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
