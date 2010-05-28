begin_unit
comment|'# Copyright (c) 2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.lore.latex}.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'import'
name|'Comment'
op|','
name|'Element'
op|','
name|'Text'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'filepath'
name|'import'
name|'FilePath'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
op|'.'
name|'unittest'
name|'import'
name|'TestCase'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'lore'
op|'.'
name|'latex'
name|'import'
name|'LatexSpitter'
op|','
name|'getLatexText'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LatexHelperTests
name|'class'
name|'LatexHelperTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for free functions in L{twisted.lore.latex}.\n    """'
newline|'\n'
DECL|member|test_getLatexText
name|'def'
name|'test_getLatexText'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{getLatexText} calls the writer function with all of the text at or\n        beneath the given node.  Non-ASCII characters are encoded using\n        UTF-8.\n        """'
newline|'\n'
name|'node'
op|'='
name|'Element'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'text'
op|'='
name|'Text'
op|'('
op|')'
newline|'\n'
name|'text'
op|'.'
name|'data'
op|'='
string|'u"foo \\N{SNOWMAN}"'
newline|'\n'
name|'node'
op|'.'
name|'appendChild'
op|'('
name|'text'
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'getLatexText'
op|'('
name|'node'
op|','
name|'result'
op|'.'
name|'append'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
op|'['
string|'u"foo \\N{SNOWMAN}"'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|LatexSpitterTests
dedent|''
dedent|''
name|'class'
name|'LatexSpitterTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for L{LatexSpitter}.\n    """'
newline|'\n'
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
name|'filename'
op|'='
name|'self'
op|'.'
name|'mktemp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'='
name|'LatexSpitter'
op|'('
name|'self'
op|'.'
name|'output'
op|'.'
name|'append'
op|','
name|'filename'
op|'='
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_head
dedent|''
name|'def'
name|'test_head'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{LatexSpitter.visitNode} writes out author information for each\n        I{link} element with a I{rel} attribute set to I{author}.\n        """'
newline|'\n'
name|'head'
op|'='
name|'Element'
op|'('
string|"'head'"
op|')'
newline|'\n'
name|'first'
op|'='
name|'Element'
op|'('
string|"'link'"
op|')'
newline|'\n'
name|'first'
op|'.'
name|'setAttribute'
op|'('
string|"'rel'"
op|','
string|"'author'"
op|')'
newline|'\n'
name|'first'
op|'.'
name|'setAttribute'
op|'('
string|"'title'"
op|','
string|"'alice'"
op|')'
newline|'\n'
name|'second'
op|'='
name|'Element'
op|'('
string|"'link'"
op|')'
newline|'\n'
name|'second'
op|'.'
name|'setAttribute'
op|'('
string|"'rel'"
op|','
string|"'author'"
op|')'
newline|'\n'
name|'second'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
string|"'http://example.com/bob'"
op|')'
newline|'\n'
name|'third'
op|'='
name|'Element'
op|'('
string|"'link'"
op|')'
newline|'\n'
name|'third'
op|'.'
name|'setAttribute'
op|'('
string|"'rel'"
op|','
string|"'author'"
op|')'
newline|'\n'
name|'third'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
string|"'mailto:carol@example.com'"
op|')'
newline|'\n'
name|'head'
op|'.'
name|'appendChild'
op|'('
name|'first'
op|')'
newline|'\n'
name|'head'
op|'.'
name|'appendChild'
op|'('
name|'second'
op|')'
newline|'\n'
name|'head'
op|'.'
name|'appendChild'
op|'('
name|'third'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'head'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|','
nl|'\n'
string|"'\\\\author{alice \\\\and $<$http://example.com/bob$>$ \\\\and $<$carol@example.com$>$}'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_skipComments
dedent|''
name|'def'
name|'test_skipComments'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{LatexSpitter.visitNode} writes nothing to its output stream for\n        comments.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'Comment'
op|'('
string|"'foo'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'foo'"
op|','
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_anchorListing
dedent|''
name|'def'
name|'test_anchorListing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{LatexSpitter.visitNode} emits a verbatim block when it encounters a\n        code listing (represented by an I{a} element with a I{listing} class).\n        """'
newline|'\n'
name|'path'
op|'='
name|'FilePath'
op|'('
name|'self'
op|'.'
name|'mktemp'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'.'
name|'setContent'
op|'('
string|"'foo\\nbar\\n'"
op|')'
newline|'\n'
name|'listing'
op|'='
name|'Element'
op|'('
string|"'a'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'class'"
op|','
string|"'listing'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
name|'path'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'listing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|','
nl|'\n'
string|'"\\\\begin{verbatim}\\n"'
nl|'\n'
string|'"foo\\n"'
nl|'\n'
string|'"bar\\n"'
nl|'\n'
string|'"\\\\end{verbatim}\\\\parbox[b]{\\\\linewidth}{\\\\begin{center} --- "'
nl|'\n'
string|'"\\\\begin{em}temp\\\\end{em}\\\\end{center}}"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_anchorListingSkipLines
dedent|''
name|'def'
name|'test_anchorListingSkipLines'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When passed an I{a} element with a I{listing} class and an I{skipLines}\n        attribute, L{LatexSpitter.visitNode} emits a verbatim block which skips\n        the indicated number of lines from the beginning of the source listing.\n        """'
newline|'\n'
name|'path'
op|'='
name|'FilePath'
op|'('
name|'self'
op|'.'
name|'mktemp'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'.'
name|'setContent'
op|'('
string|"'foo\\nbar\\n'"
op|')'
newline|'\n'
name|'listing'
op|'='
name|'Element'
op|'('
string|"'a'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'class'"
op|','
string|"'listing'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'skipLines'"
op|','
string|"'1'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
name|'path'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'listing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|','
nl|'\n'
string|'"\\\\begin{verbatim}\\n"'
nl|'\n'
string|'"bar\\n"'
nl|'\n'
string|'"\\\\end{verbatim}\\\\parbox[b]{\\\\linewidth}{\\\\begin{center} --- "'
nl|'\n'
string|'"\\\\begin{em}temp\\\\end{em}\\\\end{center}}"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_anchorRef
dedent|''
name|'def'
name|'test_anchorRef'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{LatexSpitter.visitNode} emits a footnote when it encounters an I{a}\n        element with an I{href} attribute with a network scheme.\n        """'
newline|'\n'
name|'listing'
op|'='
name|'Element'
op|'('
string|"'a'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
string|"'http://example.com/foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'listing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|','
nl|'\n'
string|'"\\\\footnote{http://example.com/foo}"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_anchorName
dedent|''
name|'def'
name|'test_anchorName'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        When passed an I{a} element with a I{name} attribute,\n        L{LatexSpitter.visitNode} emits a label.\n        """'
newline|'\n'
name|'listing'
op|'='
name|'Element'
op|'('
string|"'a'"
op|')'
newline|'\n'
name|'listing'
op|'.'
name|'setAttribute'
op|'('
string|"'name'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'spitter'
op|'.'
name|'visitNode'
op|'('
name|'listing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'output'
op|')'
op|','
nl|'\n'
string|'"\\\\label{%sHASHfoo}"'
op|'%'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'self'
op|'.'
name|'filename'
op|')'
op|'.'
name|'replace'
op|'('
string|"'\\\\'"
op|','
string|"'/'"
op|')'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
