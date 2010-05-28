begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'Interface'
op|','
name|'Attribute'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'lore'
name|'import'
name|'process'
op|','
name|'indexer'
op|','
name|'numberer'
op|','
name|'htmlbook'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'usage'
op|','
name|'reflect'
newline|'\n'
name|'from'
name|'twisted'
name|'import'
name|'plugin'
name|'as'
name|'plugin'
newline|'\n'
nl|'\n'
DECL|class|IProcessor
name|'class'
name|'IProcessor'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'Attribute'
op|'('
string|'"The user-facing name of this processor"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|moduleName
name|'moduleName'
op|'='
name|'Attribute'
op|'('
nl|'\n'
string|'"The fully qualified Python name of the object defining "'
nl|'\n'
string|'"this processor.  This object (typically a module) should "'
nl|'\n'
string|'"have a C{factory} attribute with C{generate_<output>} methods."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Options
dedent|''
name|'class'
name|'Options'
op|'('
name|'usage'
op|'.'
name|'Options'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|longdesc
indent|'    '
name|'longdesc'
op|'='
string|'"lore converts documentation formats."'
newline|'\n'
nl|'\n'
DECL|variable|optFlags
name|'optFlags'
op|'='
op|'['
op|'['
string|'"plain"'
op|','
string|"'p'"
op|','
string|'"Report filenames without progress bar"'
op|']'
op|','
nl|'\n'
op|'['
string|'"null"'
op|','
string|"'n'"
op|','
string|'"Do not report filenames"'
op|']'
op|','
nl|'\n'
op|'['
string|'"number"'
op|','
string|"'N'"
op|','
string|'"Add chapter/section numbers to section headings"'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|optParameters
name|'optParameters'
op|'='
op|'['
nl|'\n'
op|'['
string|'"input"'
op|','
string|'"i"'
op|','
string|"'lore'"
op|']'
op|','
nl|'\n'
op|'['
string|'"inputext"'
op|','
string|'"e"'
op|','
string|'".xhtml"'
op|','
string|'"The extension that your Lore input files have"'
op|']'
op|','
nl|'\n'
op|'['
string|'"docsdir"'
op|','
string|'"d"'
op|','
name|'None'
op|']'
op|','
nl|'\n'
op|'['
string|'"linkrel"'
op|','
string|'"l"'
op|','
string|"''"
op|']'
op|','
nl|'\n'
op|'['
string|'"output"'
op|','
string|'"o"'
op|','
string|"'html'"
op|']'
op|','
nl|'\n'
op|'['
string|'"index"'
op|','
string|'"x"'
op|','
name|'None'
op|','
string|'"The base filename you want to give your index file"'
op|']'
op|','
nl|'\n'
op|'['
string|'"book"'
op|','
string|'"b"'
op|','
name|'None'
op|','
string|'"The book file to generate a book from"'
op|']'
op|','
nl|'\n'
op|'['
string|'"prefixurl"'
op|','
name|'None'
op|','
string|'""'
op|','
string|'"The prefix to stick on to relative links; only useful when processing directories"'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
comment|'#zsh_altArgDescr = {"foo":"use this description for foo instead"}'
nl|'\n'
comment|'#zsh_multiUse = ["foo", "bar"]'
nl|'\n'
comment|'#zsh_mutuallyExclusive = [("foo", "bar"), ("bar", "baz")]'
nl|'\n'
comment|'#zsh_actions = {"foo":\'_files -g "*.foo"\', "bar":"(one two three)"}'
nl|'\n'
comment|'#zsh_actionDescr = {"logfile":"log file name", "random":"random seed"}'
nl|'\n'
DECL|variable|zsh_extras
name|'zsh_extras'
op|'='
op|'['
string|'"*:files:_files"'
op|']'
newline|'\n'
nl|'\n'
DECL|function|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usage'
op|'.'
name|'Options'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|opt_config
dedent|''
name|'def'
name|'opt_config'
op|'('
name|'self'
op|','
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'='"
name|'in'
name|'s'
op|':'
newline|'\n'
indent|'            '
name|'k'
op|','
name|'v'
op|'='
name|'s'
op|'.'
name|'split'
op|'('
string|"'='"
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'config'
op|'['
name|'s'
op|']'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|function|parseArgs
dedent|''
dedent|''
name|'def'
name|'parseArgs'
op|'('
name|'self'
op|','
op|'*'
name|'files'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'['
string|"'files'"
op|']'
op|'='
name|'files'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|getProcessor
dedent|''
dedent|''
name|'def'
name|'getProcessor'
op|'('
name|'input'
op|','
name|'output'
op|','
name|'config'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'plugins'
op|'='
name|'plugin'
op|'.'
name|'getPlugins'
op|'('
name|'IProcessor'
op|')'
newline|'\n'
name|'for'
name|'plug'
name|'in'
name|'plugins'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'plug'
op|'.'
name|'name'
op|'=='
name|'input'
op|':'
newline|'\n'
indent|'            '
name|'module'
op|'='
name|'reflect'
op|'.'
name|'namedModule'
op|'('
name|'plug'
op|'.'
name|'moduleName'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# try treating it as a module name'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'module'
op|'='
name|'reflect'
op|'.'
name|'namedModule'
op|'('
name|'input'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|"'%s: no such input: %s'"
op|'%'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|','
name|'input'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'process'
op|'.'
name|'getProcessor'
op|'('
name|'module'
op|','
name|'output'
op|','
name|'config'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'process'
op|'.'
name|'NoProcessorError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"%s: %s"'
op|'%'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|getWalker
dedent|''
dedent|''
name|'def'
name|'getWalker'
op|'('
name|'df'
op|','
name|'opt'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'klass'
op|'='
name|'process'
op|'.'
name|'Walker'
newline|'\n'
name|'if'
name|'opt'
op|'['
string|"'plain'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'klass'
op|'='
name|'process'
op|'.'
name|'PlainReportingWalker'
newline|'\n'
dedent|''
name|'if'
name|'opt'
op|'['
string|"'null'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'klass'
op|'='
name|'process'
op|'.'
name|'NullReportingWalker'
newline|'\n'
dedent|''
name|'return'
name|'klass'
op|'('
name|'df'
op|','
name|'opt'
op|'['
string|"'inputext'"
op|']'
op|','
name|'opt'
op|'['
string|"'linkrel'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|runGivenOptions
dedent|''
name|'def'
name|'runGivenOptions'
op|'('
name|'opt'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Do everything but parse the options; useful for testing.\n    Returns a descriptive string if there\'s an error."""'
newline|'\n'
nl|'\n'
name|'book'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'opt'
op|'['
string|"'book'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'book'
op|'='
name|'htmlbook'
op|'.'
name|'Book'
op|'('
name|'opt'
op|'['
string|"'book'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'df'
op|'='
name|'getProcessor'
op|'('
name|'opt'
op|'['
string|"'input'"
op|']'
op|','
name|'opt'
op|'['
string|"'output'"
op|']'
op|','
name|'opt'
op|'.'
name|'config'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'df'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'getProcessor() failed'"
newline|'\n'
nl|'\n'
dedent|''
name|'walker'
op|'='
name|'getWalker'
op|'('
name|'df'
op|','
name|'opt'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'opt'
op|'['
string|"'files'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'filename'
name|'in'
name|'opt'
op|'['
string|"'files'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'walker'
op|'.'
name|'walked'
op|'.'
name|'append'
op|'('
op|'('
string|"''"
op|','
name|'filename'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'book'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'filename'
name|'in'
name|'book'
op|'.'
name|'getFiles'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'walker'
op|'.'
name|'walked'
op|'.'
name|'append'
op|'('
op|'('
string|"''"
op|','
name|'filename'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'walker'
op|'.'
name|'walkdir'
op|'('
name|'opt'
op|'['
string|"'docsdir'"
op|']'
name|'or'
string|"'.'"
op|','
name|'opt'
op|'['
string|"'prefixurl'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'opt'
op|'['
string|"'index'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'indexFilename'
op|'='
name|'opt'
op|'['
string|"'index'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'book'
op|':'
newline|'\n'
indent|'        '
name|'indexFilename'
op|'='
name|'book'
op|'.'
name|'getIndexFilename'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'indexFilename'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'indexFilename'
op|':'
newline|'\n'
indent|'        '
name|'indexer'
op|'.'
name|'setIndexFilename'
op|'('
string|'"%s.%s"'
op|'%'
op|'('
name|'indexFilename'
op|','
name|'opt'
op|'['
string|"'output'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'indexer'
op|'.'
name|'setIndexFilename'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|'## TODO: get numberSections from book, if any'
nl|'\n'
dedent|''
name|'numberer'
op|'.'
name|'setNumberSections'
op|'('
name|'opt'
op|'['
string|"'number'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'walker'
op|'.'
name|'generate'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'walker'
op|'.'
name|'failures'
op|':'
newline|'\n'
indent|'        '
name|'for'
op|'('
name|'file'
op|','
name|'errors'
op|')'
name|'in'
name|'walker'
op|'.'
name|'failures'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'error'
name|'in'
name|'errors'
op|':'
newline|'\n'
indent|'                '
name|'print'
string|'"%s:%s"'
op|'%'
op|'('
name|'file'
op|','
name|'error'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|"'Walker failures'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|run
dedent|''
dedent|''
name|'def'
name|'run'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'opt'
op|'='
name|'Options'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'opt'
op|'.'
name|'parseOptions'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'usage'
op|'.'
name|'UsageError'
op|','
name|'errortext'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'%s: %s'"
op|'%'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|','
name|'errortext'
op|')'
newline|'\n'
name|'print'
string|"'%s: Try --help for usage details.'"
op|'%'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'runGivenOptions'
op|'('
name|'opt'
op|')'
newline|'\n'
name|'if'
name|'result'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'result'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'run'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
