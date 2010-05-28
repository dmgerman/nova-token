begin_unit
comment|'# markdown/html4.py'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Add html4 serialization to older versions of Elementree'
nl|'\n'
comment|'# Taken from ElementTree 1.3 preview with slight modifications'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 1999-2007 by Fredrik Lundh.  All rights reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# fredrik@pythonware.com'
nl|'\n'
comment|'# http://www.pythonware.com'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# --------------------------------------------------------------------'
nl|'\n'
comment|'# The ElementTree toolkit is'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 1999-2007 by Fredrik Lundh'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# By obtaining, using, and/or copying this software and/or its'
nl|'\n'
comment|'# associated documentation, you agree that you have read, understood,'
nl|'\n'
comment|'# and will comply with the following terms and conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission to use, copy, modify, and distribute this software and'
nl|'\n'
comment|'# its associated documentation for any purpose and without fee is'
nl|'\n'
comment|'# hereby granted, provided that the above copyright notice appears in'
nl|'\n'
comment|'# all copies, and that both that copyright notice and this permission'
nl|'\n'
comment|'# notice appear in supporting documentation, and that the name of'
nl|'\n'
comment|'# Secret Labs AB or the author not be used in advertising or publicity'
nl|'\n'
comment|'# pertaining to distribution of the software without specific, written'
nl|'\n'
comment|'# prior permission.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD'
nl|'\n'
comment|'# TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-'
nl|'\n'
comment|'# ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR'
nl|'\n'
comment|'# BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY'
nl|'\n'
comment|'# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS'
nl|'\n'
comment|'# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE'
nl|'\n'
comment|'# OF THIS SOFTWARE.'
nl|'\n'
comment|'# --------------------------------------------------------------------'
nl|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'markdown'
newline|'\n'
DECL|variable|ElementTree
name|'ElementTree'
op|'='
name|'markdown'
op|'.'
name|'etree'
op|'.'
name|'ElementTree'
newline|'\n'
DECL|variable|QName
name|'QName'
op|'='
name|'markdown'
op|'.'
name|'etree'
op|'.'
name|'QName'
newline|'\n'
DECL|variable|Comment
name|'Comment'
op|'='
name|'markdown'
op|'.'
name|'etree'
op|'.'
name|'Comment'
newline|'\n'
DECL|variable|PI
name|'PI'
op|'='
name|'markdown'
op|'.'
name|'etree'
op|'.'
name|'PI'
newline|'\n'
DECL|variable|ProcessingInstruction
name|'ProcessingInstruction'
op|'='
name|'markdown'
op|'.'
name|'etree'
op|'.'
name|'ProcessingInstruction'
newline|'\n'
nl|'\n'
DECL|variable|HTML_EMPTY
name|'HTML_EMPTY'
op|'='
op|'('
string|'"area"'
op|','
string|'"base"'
op|','
string|'"basefont"'
op|','
string|'"br"'
op|','
string|'"col"'
op|','
string|'"frame"'
op|','
string|'"hr"'
op|','
nl|'\n'
string|'"img"'
op|','
string|'"input"'
op|','
string|'"isindex"'
op|','
string|'"link"'
op|','
string|'"meta"'
string|'"param"'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
DECL|variable|HTML_EMPTY
indent|'    '
name|'HTML_EMPTY'
op|'='
name|'set'
op|'('
name|'HTML_EMPTY'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NameError'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|variable|_namespace_map
dedent|''
name|'_namespace_map'
op|'='
op|'{'
nl|'\n'
comment|'# "well-known" namespace prefixes'
nl|'\n'
string|'"http://www.w3.org/XML/1998/namespace"'
op|':'
string|'"xml"'
op|','
nl|'\n'
string|'"http://www.w3.org/1999/xhtml"'
op|':'
string|'"html"'
op|','
nl|'\n'
string|'"http://www.w3.org/1999/02/22-rdf-syntax-ns#"'
op|':'
string|'"rdf"'
op|','
nl|'\n'
string|'"http://schemas.xmlsoap.org/wsdl/"'
op|':'
string|'"wsdl"'
op|','
nl|'\n'
comment|'# xml schema'
nl|'\n'
string|'"http://www.w3.org/2001/XMLSchema"'
op|':'
string|'"xs"'
op|','
nl|'\n'
string|'"http://www.w3.org/2001/XMLSchema-instance"'
op|':'
string|'"xsi"'
op|','
nl|'\n'
comment|'# dublic core'
nl|'\n'
string|'"http://purl.org/dc/elements/1.1/"'
op|':'
string|'"dc"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_raise_serialization_error
name|'def'
name|'_raise_serialization_error'
op|'('
name|'text'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'TypeError'
op|'('
nl|'\n'
string|'"cannot serialize %r (type %s)"'
op|'%'
op|'('
name|'text'
op|','
name|'type'
op|'('
name|'text'
op|')'
op|'.'
name|'__name__'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_encode
dedent|''
name|'def'
name|'_encode'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'text'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|','
string|'"xmlcharrefreplace"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_raise_serialization_error'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_escape_cdata
dedent|''
dedent|''
name|'def'
name|'_escape_cdata'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|':'
newline|'\n'
comment|'# escape character data'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
comment|"# it's worth avoiding do-nothing calls for strings that are"
nl|'\n'
comment|"# shorter than 500 character, or so.  assume that's, by far,"
nl|'\n'
comment|'# the most common case in most applications.'
nl|'\n'
indent|'        '
name|'if'
string|'"&"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"&"'
op|','
string|'"&amp;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"<"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"<"'
op|','
string|'"&lt;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'">"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'">"'
op|','
string|'"&gt;"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'text'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|','
string|'"xmlcharrefreplace"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_raise_serialization_error'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_escape_attrib
dedent|''
dedent|''
name|'def'
name|'_escape_attrib'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|':'
newline|'\n'
comment|'# escape attribute value'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|'"&"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"&"'
op|','
string|'"&amp;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"<"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"<"'
op|','
string|'"&lt;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'">"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'">"'
op|','
string|'"&gt;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"\\""'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"\\""'
op|','
string|'"&quot;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"\\n"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"\\n"'
op|','
string|'"&#10;"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'text'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|','
string|'"xmlcharrefreplace"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_raise_serialization_error'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_escape_attrib_html
dedent|''
dedent|''
name|'def'
name|'_escape_attrib_html'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|':'
newline|'\n'
comment|'# escape attribute value'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|'"&"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"&"'
op|','
string|'"&amp;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'">"'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'">"'
op|','
string|'"&gt;"'
op|')'
newline|'\n'
dedent|''
name|'if'
string|'"\\""'
name|'in'
name|'text'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'text'
op|'.'
name|'replace'
op|'('
string|'"\\""'
op|','
string|'"&quot;"'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'text'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|','
string|'"xmlcharrefreplace"'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_raise_serialization_error'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_serialize_html
dedent|''
dedent|''
name|'def'
name|'_serialize_html'
op|'('
name|'write'
op|','
name|'elem'
op|','
name|'encoding'
op|','
name|'qnames'
op|','
name|'namespaces'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tag'
op|'='
name|'elem'
op|'.'
name|'tag'
newline|'\n'
name|'text'
op|'='
name|'elem'
op|'.'
name|'text'
newline|'\n'
name|'if'
name|'tag'
name|'is'
name|'Comment'
op|':'
newline|'\n'
indent|'        '
name|'write'
op|'('
string|'"<!--%s-->"'
op|'%'
name|'_escape_cdata'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'tag'
name|'is'
name|'ProcessingInstruction'
op|':'
newline|'\n'
indent|'        '
name|'write'
op|'('
string|'"<?%s?>"'
op|'%'
name|'_escape_cdata'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'tag'
op|'='
name|'qnames'
op|'['
name|'tag'
op|']'
newline|'\n'
name|'if'
name|'tag'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'text'
op|':'
newline|'\n'
indent|'                '
name|'write'
op|'('
name|'_escape_cdata'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'e'
name|'in'
name|'elem'
op|':'
newline|'\n'
indent|'                '
name|'_serialize_html'
op|'('
name|'write'
op|','
name|'e'
op|','
name|'encoding'
op|','
name|'qnames'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'write'
op|'('
string|'"<"'
op|'+'
name|'tag'
op|')'
newline|'\n'
name|'items'
op|'='
name|'elem'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'if'
name|'items'
name|'or'
name|'namespaces'
op|':'
newline|'\n'
indent|'                '
name|'items'
op|'.'
name|'sort'
op|'('
op|')'
comment|'# lexical order'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'isinstance'
op|'('
name|'k'
op|','
name|'QName'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'k'
op|'='
name|'k'
op|'.'
name|'text'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'v'
op|','
name|'QName'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'v'
op|'='
name|'qnames'
op|'['
name|'v'
op|'.'
name|'text'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'v'
op|'='
name|'_escape_attrib_html'
op|'('
name|'v'
op|','
name|'encoding'
op|')'
newline|'\n'
comment|'# FIXME: handle boolean attributes'
nl|'\n'
dedent|''
name|'write'
op|'('
string|'" %s=\\"%s\\""'
op|'%'
op|'('
name|'qnames'
op|'['
name|'k'
op|']'
op|','
name|'v'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'namespaces'
op|':'
newline|'\n'
indent|'                    '
name|'items'
op|'='
name|'namespaces'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'items'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
name|'x'
op|'['
number|'1'
op|']'
op|')'
comment|'# sort on prefix'
newline|'\n'
name|'for'
name|'v'
op|','
name|'k'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'k'
op|':'
newline|'\n'
indent|'                            '
name|'k'
op|'='
string|'":"'
op|'+'
name|'k'
newline|'\n'
dedent|''
name|'write'
op|'('
string|'" xmlns%s=\\"%s\\""'
op|'%'
op|'('
nl|'\n'
name|'k'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|')'
op|','
nl|'\n'
name|'_escape_attrib'
op|'('
name|'v'
op|','
name|'encoding'
op|')'
nl|'\n'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'write'
op|'('
string|'">"'
op|')'
newline|'\n'
name|'tag'
op|'='
name|'tag'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
name|'text'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'tag'
op|'=='
string|'"script"'
name|'or'
name|'tag'
op|'=='
string|'"style"'
op|':'
newline|'\n'
indent|'                    '
name|'write'
op|'('
name|'_encode'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'write'
op|'('
name|'_escape_cdata'
op|'('
name|'text'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'e'
name|'in'
name|'elem'
op|':'
newline|'\n'
indent|'                '
name|'_serialize_html'
op|'('
name|'write'
op|','
name|'e'
op|','
name|'encoding'
op|','
name|'qnames'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'tag'
name|'not'
name|'in'
name|'HTML_EMPTY'
op|':'
newline|'\n'
indent|'                '
name|'write'
op|'('
string|'"</"'
op|'+'
name|'tag'
op|'+'
string|'">"'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'elem'
op|'.'
name|'tail'
op|':'
newline|'\n'
indent|'        '
name|'write'
op|'('
name|'_escape_cdata'
op|'('
name|'elem'
op|'.'
name|'tail'
op|','
name|'encoding'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|write_html
dedent|''
dedent|''
name|'def'
name|'write_html'
op|'('
name|'root'
op|','
name|'f'
op|','
nl|'\n'
comment|'# keyword arguments'
nl|'\n'
name|'encoding'
op|'='
string|'"us-ascii"'
op|','
nl|'\n'
name|'default_namespace'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'root'
name|'is'
name|'not'
name|'None'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'f'
op|','
string|'"write"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'open'
op|'('
name|'f'
op|','
string|'"wb"'
op|')'
newline|'\n'
dedent|''
name|'write'
op|'='
name|'f'
op|'.'
name|'write'
newline|'\n'
name|'if'
name|'not'
name|'encoding'
op|':'
newline|'\n'
indent|'        '
name|'encoding'
op|'='
string|'"us-ascii"'
newline|'\n'
dedent|''
name|'qnames'
op|','
name|'namespaces'
op|'='
name|'_namespaces'
op|'('
nl|'\n'
name|'root'
op|','
name|'encoding'
op|','
name|'default_namespace'
nl|'\n'
op|')'
newline|'\n'
name|'_serialize_html'
op|'('
nl|'\n'
name|'write'
op|','
name|'root'
op|','
name|'encoding'
op|','
name|'qnames'
op|','
name|'namespaces'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
comment|'# --------------------------------------------------------------------'
nl|'\n'
comment|'# serialization support'
nl|'\n'
nl|'\n'
DECL|function|_namespaces
dedent|''
name|'def'
name|'_namespaces'
op|'('
name|'elem'
op|','
name|'encoding'
op|','
name|'default_namespace'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# identify namespaces used in this tree'
nl|'\n'
nl|'\n'
comment|'# maps qnames to *encoded* prefix:local names'
nl|'\n'
indent|'    '
name|'qnames'
op|'='
op|'{'
name|'None'
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
comment|'# maps uri:s to prefixes'
nl|'\n'
name|'namespaces'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'default_namespace'
op|':'
newline|'\n'
indent|'        '
name|'namespaces'
op|'['
name|'default_namespace'
op|']'
op|'='
string|'""'
newline|'\n'
nl|'\n'
DECL|function|encode
dedent|''
name|'def'
name|'encode'
op|'('
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'text'
op|'.'
name|'encode'
op|'('
name|'encoding'
op|')'
newline|'\n'
nl|'\n'
DECL|function|add_qname
dedent|''
name|'def'
name|'add_qname'
op|'('
name|'qname'
op|')'
op|':'
newline|'\n'
comment|'# calculate serialized qname representation'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'qname'
op|'['
op|':'
number|'1'
op|']'
op|'=='
string|'"{"'
op|':'
newline|'\n'
indent|'                '
name|'uri'
op|','
name|'tag'
op|'='
name|'qname'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|'"}"'
op|','
number|'1'
op|')'
newline|'\n'
name|'prefix'
op|'='
name|'namespaces'
op|'.'
name|'get'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'if'
name|'prefix'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'prefix'
op|'='
name|'_namespace_map'
op|'.'
name|'get'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'if'
name|'prefix'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                        '
name|'prefix'
op|'='
string|'"ns%d"'
op|'%'
name|'len'
op|'('
name|'namespaces'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'prefix'
op|'!='
string|'"xml"'
op|':'
newline|'\n'
indent|'                        '
name|'namespaces'
op|'['
name|'uri'
op|']'
op|'='
name|'prefix'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'prefix'
op|':'
newline|'\n'
indent|'                    '
name|'qnames'
op|'['
name|'qname'
op|']'
op|'='
name|'encode'
op|'('
string|'"%s:%s"'
op|'%'
op|'('
name|'prefix'
op|','
name|'tag'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'qnames'
op|'['
name|'qname'
op|']'
op|'='
name|'encode'
op|'('
name|'tag'
op|')'
comment|'# default element'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'default_namespace'
op|':'
newline|'\n'
comment|'# FIXME: can this be handled in XML 1.0?'
nl|'\n'
indent|'                    '
name|'raise'
name|'ValueError'
op|'('
nl|'\n'
string|'"cannot use non-qualified names with "'
nl|'\n'
string|'"default_namespace option"'
nl|'\n'
op|')'
newline|'\n'
dedent|''
name|'qnames'
op|'['
name|'qname'
op|']'
op|'='
name|'encode'
op|'('
name|'qname'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'_raise_serialization_error'
op|'('
name|'qname'
op|')'
newline|'\n'
nl|'\n'
comment|'# populate qname and namespaces table'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'iterate'
op|'='
name|'elem'
op|'.'
name|'iter'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'        '
name|'iterate'
op|'='
name|'elem'
op|'.'
name|'getiterator'
comment|'# cET compatibility'
newline|'\n'
dedent|''
name|'for'
name|'elem'
name|'in'
name|'iterate'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag'
op|'='
name|'elem'
op|'.'
name|'tag'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'tag'
op|','
name|'QName'
op|')'
name|'and'
name|'tag'
op|'.'
name|'text'
name|'not'
name|'in'
name|'qnames'
op|':'
newline|'\n'
indent|'            '
name|'add_qname'
op|'('
name|'tag'
op|'.'
name|'text'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'tag'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tag'
name|'not'
name|'in'
name|'qnames'
op|':'
newline|'\n'
indent|'                '
name|'add_qname'
op|'('
name|'tag'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'tag'
name|'is'
name|'not'
name|'None'
name|'and'
name|'tag'
name|'is'
name|'not'
name|'Comment'
name|'and'
name|'tag'
name|'is'
name|'not'
name|'PI'
op|':'
newline|'\n'
indent|'            '
name|'_raise_serialization_error'
op|'('
name|'tag'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'elem'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'key'
op|','
name|'QName'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
name|'key'
op|'.'
name|'text'
newline|'\n'
dedent|''
name|'if'
name|'key'
name|'not'
name|'in'
name|'qnames'
op|':'
newline|'\n'
indent|'                '
name|'add_qname'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'QName'
op|')'
name|'and'
name|'value'
op|'.'
name|'text'
name|'not'
name|'in'
name|'qnames'
op|':'
newline|'\n'
indent|'                '
name|'add_qname'
op|'('
name|'value'
op|'.'
name|'text'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'text'
op|'='
name|'elem'
op|'.'
name|'text'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'text'
op|','
name|'QName'
op|')'
name|'and'
name|'text'
op|'.'
name|'text'
name|'not'
name|'in'
name|'qnames'
op|':'
newline|'\n'
indent|'            '
name|'add_qname'
op|'('
name|'text'
op|'.'
name|'text'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'qnames'
op|','
name|'namespaces'
newline|'\n'
nl|'\n'
DECL|function|to_html_string
dedent|''
name|'def'
name|'to_html_string'
op|'('
name|'element'
op|','
name|'encoding'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
DECL|class|dummy
indent|'    '
name|'class'
name|'dummy'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'file'
op|'='
name|'dummy'
op|'('
op|')'
newline|'\n'
name|'file'
op|'.'
name|'write'
op|'='
name|'data'
op|'.'
name|'append'
newline|'\n'
name|'write_html'
op|'('
name|'ElementTree'
op|'('
name|'element'
op|')'
op|'.'
name|'getroot'
op|'('
op|')'
op|','
name|'file'
op|','
name|'encoding'
op|')'
newline|'\n'
name|'return'
string|'""'
op|'.'
name|'join'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
