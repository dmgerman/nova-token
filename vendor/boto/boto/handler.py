begin_unit
comment|'# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, '
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
name|'import'
name|'xml'
op|'.'
name|'sax'
newline|'\n'
nl|'\n'
DECL|class|XmlHandler
name|'class'
name|'XmlHandler'
op|'('
name|'xml'
op|'.'
name|'sax'
op|'.'
name|'ContentHandler'
op|')'
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
name|'root_node'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'nodes'
op|'='
op|'['
op|'('
string|"'root'"
op|','
name|'root_node'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'current_text'
op|'='
string|"''"
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'current_text'
op|'='
string|"''"
newline|'\n'
name|'new_node'
op|'='
name|'self'
op|'.'
name|'nodes'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'.'
name|'startElement'
op|'('
name|'name'
op|','
name|'attrs'
op|','
name|'self'
op|'.'
name|'connection'
op|')'
newline|'\n'
name|'if'
name|'new_node'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nodes'
op|'.'
name|'append'
op|'('
op|'('
name|'name'
op|','
name|'new_node'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nodes'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|'.'
name|'endElement'
op|'('
name|'name'
op|','
name|'self'
op|'.'
name|'current_text'
op|','
name|'self'
op|'.'
name|'connection'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'nodes'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'=='
name|'name'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nodes'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'current_text'
op|'='
string|"''"
newline|'\n'
nl|'\n'
DECL|member|characters
dedent|''
name|'def'
name|'characters'
op|'('
name|'self'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'current_text'
op|'+='
name|'content'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
