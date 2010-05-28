begin_unit
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nDocBook output support for Lore.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|','
name|'cgi'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
name|'as'
name|'dom'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'lore'
name|'import'
name|'latex'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DocbookSpitter
name|'class'
name|'DocbookSpitter'
op|'('
name|'latex'
op|'.'
name|'BaseLatexSpitter'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|currentLevel
indent|'    '
name|'currentLevel'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|writeNodeData
name|'def'
name|'writeNodeData'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'writer'
op|'('
name|'node'
op|'.'
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNode_body
dedent|''
name|'def'
name|'visitNode_body'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'visitNodeDefault'
op|'('
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'writer'
op|'('
string|"'</section>'"
op|'*'
name|'self'
op|'.'
name|'currentLevel'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNodeHeader
dedent|''
name|'def'
name|'visitNodeHeader'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'level'
op|'='
name|'int'
op|'('
name|'node'
op|'.'
name|'tagName'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'difference'
op|','
name|'self'
op|'.'
name|'currentLevel'
op|'='
name|'level'
op|'-'
name|'self'
op|'.'
name|'currentLevel'
op|','
name|'level'
newline|'\n'
name|'self'
op|'.'
name|'writer'
op|'('
string|"'<section>'"
op|'*'
name|'difference'
op|'+'
string|"'</section>'"
op|'*'
op|'-'
name|'difference'
op|')'
newline|'\n'
name|'if'
name|'difference'
op|'<='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'writer'
op|'('
string|"'</section>\\n<section>'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'writer'
op|'('
string|"'<title>'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'visitNodeDefault'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNode_a_listing
dedent|''
name|'def'
name|'visitNode_a_listing'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fileName'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'currDir'
op|','
name|'node'
op|'.'
name|'getAttribute'
op|'('
string|"'href'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'writer'
op|'('
string|"'<programlisting>\\n'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'writer'
op|'('
name|'cgi'
op|'.'
name|'escape'
op|'('
name|'open'
op|'('
name|'fileName'
op|')'
op|'.'
name|'read'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'writer'
op|'('
string|"'</programlisting>\\n'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNode_a_href
dedent|''
name|'def'
name|'visitNode_a_href'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'visitNodeDefault'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNode_a_name
dedent|''
name|'def'
name|'visitNode_a_name'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'visitNodeDefault'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|visitNode_li
dedent|''
name|'def'
name|'visitNode_li'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'getattr'
op|'('
name|'child'
op|','
string|"'tagName'"
op|','
name|'None'
op|')'
op|'!='
string|"'p'"
op|':'
newline|'\n'
indent|'                '
name|'new'
op|'='
name|'dom'
op|'.'
name|'Element'
op|'('
string|"'p'"
op|')'
newline|'\n'
name|'new'
op|'.'
name|'childNodes'
op|'='
op|'['
name|'child'
op|']'
newline|'\n'
name|'node'
op|'.'
name|'replaceChild'
op|'('
name|'new'
op|','
name|'child'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'visitNodeDefault'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'visitNode_h2'
op|'='
name|'visitNode_h3'
op|'='
name|'visitNode_h4'
op|'='
name|'visitNodeHeader'
newline|'\n'
name|'end_h2'
op|'='
name|'end_h3'
op|'='
name|'end_h4'
op|'='
string|"'</title><para />'"
newline|'\n'
name|'start_title'
op|','
name|'end_title'
op|'='
string|"'<section><title>'"
op|','
string|"'</title><para />'"
newline|'\n'
name|'start_p'
op|','
name|'end_p'
op|'='
string|"'<para>'"
op|','
string|"'</para>'"
newline|'\n'
name|'start_strong'
op|','
name|'end_strong'
op|'='
name|'start_em'
op|','
name|'end_em'
op|'='
string|"'<emphasis>'"
op|','
string|"'</emphasis>'"
newline|'\n'
name|'start_span_footnote'
op|','
name|'end_span_footnote'
op|'='
string|"'<footnote><para>'"
op|','
string|"'</para></footnote>'"
newline|'\n'
name|'start_q'
op|'='
name|'end_q'
op|'='
string|'\'"\''
newline|'\n'
name|'start_pre'
op|','
name|'end_pre'
op|'='
string|"'<programlisting>'"
op|','
string|"'</programlisting>'"
newline|'\n'
name|'start_div_note'
op|','
name|'end_div_note'
op|'='
string|"'<note>'"
op|','
string|"'</note>'"
newline|'\n'
name|'start_li'
op|','
name|'end_li'
op|'='
string|"'<listitem>'"
op|','
string|"'</listitem>'"
newline|'\n'
name|'start_ul'
op|','
name|'end_ul'
op|'='
string|"'<itemizedlist>'"
op|','
string|"'</itemizedlist>'"
newline|'\n'
name|'start_ol'
op|','
name|'end_ol'
op|'='
string|"'<orderedlist>'"
op|','
string|"'</orderedlist>'"
newline|'\n'
name|'start_dl'
op|','
name|'end_dl'
op|'='
string|"'<variablelist>'"
op|','
string|"'</variablelist>'"
newline|'\n'
name|'start_dt'
op|','
name|'end_dt'
op|'='
string|"'<varlistentry><term>'"
op|','
string|"'</term>'"
newline|'\n'
name|'start_dd'
op|','
name|'end_dd'
op|'='
string|"'<listitem><para>'"
op|','
string|"'</para></listitem></varlistentry>'"
newline|'\n'
dedent|''
endmarker|''
end_unit
