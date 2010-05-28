begin_unit
string|'"""\nTable of Contents Extension for Python-Markdown\n* * *\n\n(c) 2008 [Jack Miller](http://codezen.org)\n\nDependencies:\n* [Markdown 2.0+](http://www.freewisdom.org/projects/python-markdown/)\n\n"""'
newline|'\n'
name|'import'
name|'markdown'
newline|'\n'
name|'from'
name|'markdown'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
DECL|class|TocTreeprocessor
name|'class'
name|'TocTreeprocessor'
op|'('
name|'markdown'
op|'.'
name|'treeprocessors'
op|'.'
name|'Treeprocessor'
op|')'
op|':'
newline|'\n'
comment|'# Iterator wrapper to get parent and child all at once'
nl|'\n'
DECL|member|iterparent
indent|'    '
name|'def'
name|'iterparent'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'parent'
name|'in'
name|'root'
op|'.'
name|'getiterator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'child'
name|'in'
name|'parent'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'parent'
op|','
name|'child'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
dedent|''
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|','
name|'doc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'div'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"div"'
op|')'
newline|'\n'
name|'div'
op|'.'
name|'attrib'
op|'['
string|'"class"'
op|']'
op|'='
string|'"toc"'
newline|'\n'
name|'last_li'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# Add title to the div'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'config'
op|'['
string|'"title"'
op|']'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'header'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'div'
op|','
string|'"span"'
op|')'
newline|'\n'
name|'header'
op|'.'
name|'attrib'
op|'['
string|'"class"'
op|']'
op|'='
string|'"toctitle"'
newline|'\n'
name|'header'
op|'.'
name|'text'
op|'='
name|'self'
op|'.'
name|'config'
op|'['
string|'"title"'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'level'
op|'='
number|'0'
newline|'\n'
name|'list_stack'
op|'='
op|'['
name|'div'
op|']'
newline|'\n'
name|'header_rgx'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"[Hh][123456]"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get a list of id attributes'
nl|'\n'
name|'used_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'c'
name|'in'
name|'doc'
op|'.'
name|'getiterator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|'"id"'
name|'in'
name|'c'
op|'.'
name|'attrib'
op|':'
newline|'\n'
indent|'                '
name|'used_ids'
op|'.'
name|'append'
op|'('
name|'c'
op|'.'
name|'attrib'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'for'
op|'('
name|'p'
op|','
name|'c'
op|')'
name|'in'
name|'self'
op|'.'
name|'iterparent'
op|'('
name|'doc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'c'
op|'.'
name|'text'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# To keep the output from screwing up the'
nl|'\n'
comment|'# validation by putting a <div> inside of a <p>'
nl|'\n'
comment|'# we actually replace the <p> in its entirety.'
nl|'\n'
comment|'# We do not allow the marker inside a header as that'
nl|'\n'
comment|'# would causes an enless loop of placing a new TOC '
nl|'\n'
comment|'# inside previously generated TOC.'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'c'
op|'.'
name|'text'
op|'.'
name|'find'
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|'"marker"'
op|']'
op|'['
number|'0'
op|']'
op|')'
op|'>'
op|'-'
number|'1'
name|'and'
name|'not'
name|'header_rgx'
op|'.'
name|'match'
op|'('
name|'c'
op|'.'
name|'tag'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'p'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'p'
op|'['
name|'i'
op|']'
op|'=='
name|'c'
op|':'
newline|'\n'
indent|'                        '
name|'p'
op|'['
name|'i'
op|']'
op|'='
name|'div'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'header_rgx'
op|'.'
name|'match'
op|'('
name|'c'
op|'.'
name|'tag'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'tag_level'
op|'='
name|'int'
op|'('
name|'c'
op|'.'
name|'tag'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Regardless of how many levels we jumped'
nl|'\n'
comment|'# only one list should be created, since'
nl|'\n'
comment|'# empty lists containing lists are illegal.'
nl|'\n'
nl|'\n'
name|'if'
name|'tag_level'
op|'<'
name|'level'
op|':'
newline|'\n'
indent|'                    '
name|'list_stack'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'level'
op|'='
name|'tag_level'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'tag_level'
op|'>'
name|'level'
op|':'
newline|'\n'
indent|'                    '
name|'newlist'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"ul"'
op|')'
newline|'\n'
name|'if'
name|'last_li'
op|':'
newline|'\n'
indent|'                        '
name|'last_li'
op|'.'
name|'append'
op|'('
name|'newlist'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'list_stack'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'append'
op|'('
name|'newlist'
op|')'
newline|'\n'
dedent|''
name|'list_stack'
op|'.'
name|'append'
op|'('
name|'newlist'
op|')'
newline|'\n'
name|'level'
op|'='
name|'tag_level'
newline|'\n'
nl|'\n'
comment|'# Do not override pre-existing ids '
nl|'\n'
dedent|''
name|'if'
name|'not'
string|'"id"'
name|'in'
name|'c'
op|'.'
name|'attrib'
op|':'
newline|'\n'
indent|'                    '
name|'id'
op|'='
name|'self'
op|'.'
name|'config'
op|'['
string|'"slugify"'
op|']'
op|'['
number|'0'
op|']'
op|'('
name|'c'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'in'
name|'used_ids'
op|':'
newline|'\n'
indent|'                        '
name|'ctr'
op|'='
number|'1'
newline|'\n'
name|'while'
string|'"%s_%d"'
op|'%'
op|'('
name|'id'
op|','
name|'ctr'
op|')'
name|'in'
name|'used_ids'
op|':'
newline|'\n'
indent|'                            '
name|'ctr'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'id'
op|'='
string|'"%s_%d"'
op|'%'
op|'('
name|'id'
op|','
name|'ctr'
op|')'
newline|'\n'
dedent|''
name|'used_ids'
op|'.'
name|'append'
op|'('
name|'id'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'attrib'
op|'['
string|'"id"'
op|']'
op|'='
name|'id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'id'
op|'='
name|'c'
op|'.'
name|'attrib'
op|'['
string|'"id"'
op|']'
newline|'\n'
nl|'\n'
comment|'# List item link, to be inserted into the toc div'
nl|'\n'
dedent|''
name|'last_li'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|'"li"'
op|')'
newline|'\n'
name|'link'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'last_li'
op|','
string|'"a"'
op|')'
newline|'\n'
name|'link'
op|'.'
name|'text'
op|'='
name|'c'
op|'.'
name|'text'
newline|'\n'
name|'link'
op|'.'
name|'attrib'
op|'['
string|'"href"'
op|']'
op|'='
string|"'#'"
op|'+'
name|'id'
newline|'\n'
nl|'\n'
name|'if'
name|'int'
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|'"anchorlink"'
op|']'
op|'['
number|'0'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'anchor'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'c'
op|','
string|'"a"'
op|')'
newline|'\n'
name|'anchor'
op|'.'
name|'text'
op|'='
name|'c'
op|'.'
name|'text'
newline|'\n'
name|'anchor'
op|'.'
name|'attrib'
op|'['
string|'"href"'
op|']'
op|'='
string|'"#"'
op|'+'
name|'id'
newline|'\n'
name|'anchor'
op|'.'
name|'attrib'
op|'['
string|'"class"'
op|']'
op|'='
string|'"toclink"'
newline|'\n'
name|'c'
op|'.'
name|'text'
op|'='
string|'""'
newline|'\n'
nl|'\n'
dedent|''
name|'list_stack'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'append'
op|'('
name|'last_li'
op|')'
newline|'\n'
nl|'\n'
DECL|class|TocExtension
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'TocExtension'
op|'('
name|'markdown'
op|'.'
name|'Extension'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'configs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'config'
op|'='
op|'{'
string|'"marker"'
op|':'
op|'['
string|'"[TOC]"'
op|','
nl|'\n'
string|'"Text to find and replace with Table of Contents -"'
nl|'\n'
string|'"Defaults to \\"[TOC]\\""'
op|']'
op|','
nl|'\n'
string|'"slugify"'
op|':'
op|'['
name|'self'
op|'.'
name|'slugify'
op|','
nl|'\n'
string|'"Function to generate anchors based on header text-"'
nl|'\n'
string|'"Defaults to a built in slugify function."'
op|']'
op|','
nl|'\n'
string|'"title"'
op|':'
op|'['
name|'None'
op|','
nl|'\n'
string|'"Title to insert into TOC <div> - "'
nl|'\n'
string|'"Defaults to None"'
op|']'
op|','
nl|'\n'
string|'"anchorlink"'
op|':'
op|'['
number|'0'
op|','
nl|'\n'
string|'"1 if header should be a self link"'
nl|'\n'
string|'"Defaults to 0"'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'configs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setConfig'
op|'('
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|"# This is exactly the same as Django's slugify"
nl|'\n'
DECL|member|slugify
dedent|''
dedent|''
name|'def'
name|'slugify'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Slugify a string, to make it URL friendly. """'
newline|'\n'
name|'import'
name|'unicodedata'
newline|'\n'
name|'value'
op|'='
name|'unicodedata'
op|'.'
name|'normalize'
op|'('
string|"'NFKD'"
op|','
name|'value'
op|')'
op|'.'
name|'encode'
op|'('
string|"'ascii'"
op|','
string|"'ignore'"
op|')'
newline|'\n'
name|'value'
op|'='
name|'unicode'
op|'('
name|'re'
op|'.'
name|'sub'
op|'('
string|"'[^\\w\\s-]'"
op|','
string|"''"
op|','
name|'value'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'re'
op|'.'
name|'sub'
op|'('
string|"'[-\\s]+'"
op|','
string|"'-'"
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|extendMarkdown
dedent|''
name|'def'
name|'extendMarkdown'
op|'('
name|'self'
op|','
name|'md'
op|','
name|'md_globals'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tocext'
op|'='
name|'TocTreeprocessor'
op|'('
name|'md'
op|')'
newline|'\n'
name|'tocext'
op|'.'
name|'config'
op|'='
name|'self'
op|'.'
name|'config'
newline|'\n'
name|'md'
op|'.'
name|'treeprocessors'
op|'.'
name|'add'
op|'('
string|'"toc"'
op|','
name|'tocext'
op|','
string|'"_begin"'
op|')'
newline|'\n'
nl|'\n'
DECL|function|makeExtension
dedent|''
dedent|''
name|'def'
name|'makeExtension'
op|'('
name|'configs'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'TocExtension'
op|'('
name|'configs'
op|'='
name|'configs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
