begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nTest cases for explorer\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'manhole'
name|'import'
name|'explorer'
newline|'\n'
nl|'\n'
name|'import'
name|'types'
op|','
name|'string'
newline|'\n'
nl|'\n'
string|'"""\n# Tests:\n\n Get an ObjectLink.  Browse ObjectLink.identifier.  Is it the same?\n\n Watch Object.  Make sure an ObjectLink is received when:\n   Call a method.\n   Set an attribute.\n\n Have an Object with a setattr class.  Watch it.\n   Do both the navite setattr and the watcher get called?\n\n Sequences with circular references.  Does it blow up?\n"""'
newline|'\n'
nl|'\n'
DECL|class|SomeDohickey
name|'class'
name|'SomeDohickey'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'args'"
op|']'
op|'='
name|'a'
newline|'\n'
nl|'\n'
DECL|member|bip
dedent|''
name|'def'
name|'bip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'args'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestBrowser
dedent|''
dedent|''
name|'class'
name|'TestBrowser'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'pool'
op|'='
name|'explorer'
op|'.'
name|'explorerPool'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'testThing'
op|'='
op|'['
string|'"How many stairs must a man climb down?"'
op|','
nl|'\n'
name|'SomeDohickey'
op|'('
number|'42'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_chain
dedent|''
name|'def'
name|'test_chain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Following a chain of Explorers."'
newline|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'self'
op|'.'
name|'testThing'
op|','
string|"'testThing'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'xplorer'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'self'
op|'.'
name|'testThing'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'xplorer'
op|'.'
name|'identifier'
op|','
string|"'testThing'"
op|')'
newline|'\n'
nl|'\n'
name|'dxplorer'
op|'='
name|'xplorer'
op|'.'
name|'get_elements'
op|'('
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'dxplorer'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'self'
op|'.'
name|'testThing'
op|'['
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Watcher
dedent|''
dedent|''
name|'class'
name|'Watcher'
op|':'
newline|'\n'
DECL|variable|zero
indent|'    '
name|'zero'
op|'='
number|'0'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'links'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|receiveBrowserObject
dedent|''
name|'def'
name|'receiveBrowserObject'
op|'('
name|'self'
op|','
name|'olink'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'links'
op|'.'
name|'append'
op|'('
name|'olink'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setZero
dedent|''
name|'def'
name|'setZero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'zero'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'links'
op|')'
newline|'\n'
nl|'\n'
DECL|member|len
dedent|''
name|'def'
name|'len'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'links'
op|')'
op|'-'
name|'self'
op|'.'
name|'zero'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SetattrDohickey
dedent|''
dedent|''
name|'class'
name|'SetattrDohickey'
op|':'
newline|'\n'
DECL|member|__setattr__
indent|'    '
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'v'
op|'='
name|'list'
op|'('
name|'str'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
name|'v'
op|'.'
name|'reverse'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
name|'k'
op|']'
op|'='
name|'string'
op|'.'
name|'join'
op|'('
name|'v'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|class|MiddleMan
dedent|''
dedent|''
name|'class'
name|'MiddleMan'
op|'('
name|'SomeDohickey'
op|','
name|'SetattrDohickey'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
comment|'# class TestWatch(unittest.TestCase):'
nl|'\n'
DECL|class|FIXME_Watch
dedent|''
name|'class'
name|'FIXME_Watch'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'globalNS'
op|'='
name|'globals'
op|'('
op|')'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'localNS'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'browser'
op|'='
name|'explorer'
op|'.'
name|'ObjectBrowser'
op|'('
name|'self'
op|'.'
name|'globalNS'
op|','
name|'self'
op|'.'
name|'localNS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'watcher'
op|'='
name|'Watcher'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setAttrPlain
dedent|''
name|'def'
name|'test_setAttrPlain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Triggering a watcher response by setting an attribute."'
newline|'\n'
nl|'\n'
name|'testThing'
op|'='
name|'SomeDohickey'
op|'('
string|"'pencil'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'browser'
op|'.'
name|'watchObject'
op|'('
name|'testThing'
op|','
string|"'testThing'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'receiveBrowserObject'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'setZero'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'testThing'
op|'.'
name|'someAttr'
op|'='
string|"'someValue'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'testThing'
op|'.'
name|'someAttr'
op|','
string|"'someValue'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'len'
op|'('
op|')'
op|')'
newline|'\n'
name|'olink'
op|'='
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'links'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'olink'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'testThing'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setAttrChain
dedent|''
name|'def'
name|'test_setAttrChain'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Setting an attribute on a watched object that has __setattr__"'
newline|'\n'
name|'testThing'
op|'='
name|'MiddleMan'
op|'('
string|"'pencil'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'browser'
op|'.'
name|'watchObject'
op|'('
name|'testThing'
op|','
string|"'testThing'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'receiveBrowserObject'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'setZero'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'testThing'
op|'.'
name|'someAttr'
op|'='
string|"'ZORT'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'testThing'
op|'.'
name|'someAttr'
op|','
string|"'TROZ'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'len'
op|'('
op|')'
op|')'
newline|'\n'
name|'olink'
op|'='
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'links'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'olink'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'testThing'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_method
dedent|''
name|'def'
name|'test_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"Triggering a watcher response by invoking a method."'
newline|'\n'
nl|'\n'
name|'for'
name|'testThing'
name|'in'
op|'('
name|'SomeDohickey'
op|'('
string|"'pencil'"
op|')'
op|','
name|'MiddleMan'
op|'('
string|"'pencil'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'browser'
op|'.'
name|'watchObject'
op|'('
name|'testThing'
op|','
string|"'testThing'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'receiveBrowserObject'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'setZero'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rval'
op|'='
name|'testThing'
op|'.'
name|'bip'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'rval'
op|','
op|'('
string|"'pencil'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'len'
op|'('
op|')'
op|')'
newline|'\n'
name|'olink'
op|'='
name|'self'
op|'.'
name|'watcher'
op|'.'
name|'links'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'olink'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'testThing'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|function_noArgs
dedent|''
dedent|''
dedent|''
name|'def'
name|'function_noArgs'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"A function which accepts no arguments at all."'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|function|function_simple
dedent|''
name|'def'
name|'function_simple'
op|'('
name|'a'
op|','
name|'b'
op|','
name|'c'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"A function which accepts several arguments."'
newline|'\n'
name|'return'
name|'a'
op|','
name|'b'
op|','
name|'c'
newline|'\n'
nl|'\n'
DECL|function|function_variable
dedent|''
name|'def'
name|'function_variable'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"A function which accepts a variable number of args and keywords."'
newline|'\n'
name|'return'
name|'a'
op|','
name|'kw'
newline|'\n'
nl|'\n'
DECL|function|function_crazy
dedent|''
name|'def'
name|'function_crazy'
op|'('
op|'('
name|'alpha'
op|','
name|'beta'
op|')'
op|','
name|'c'
op|','
name|'d'
op|'='
name|'range'
op|'('
number|'4'
op|')'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"A function with a mad crazy signature."'
newline|'\n'
name|'return'
name|'alpha'
op|','
name|'beta'
op|','
name|'c'
op|','
name|'d'
op|','
name|'kw'
newline|'\n'
nl|'\n'
DECL|class|TestBrowseFunction
dedent|''
name|'class'
name|'TestBrowseFunction'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'pool'
op|'='
name|'explorer'
op|'.'
name|'explorerPool'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_sanity
dedent|''
name|'def'
name|'test_sanity'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Basic checks for browse_function.\n\n        Was the proper type returned?  Does it have the right name and ID?\n        """'
newline|'\n'
name|'for'
name|'f_name'
name|'in'
op|'('
string|"'function_noArgs'"
op|','
string|"'function_simple'"
op|','
nl|'\n'
string|"'function_variable'"
op|','
string|"'function_crazy'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'eval'
op|'('
name|'f_name'
op|')'
newline|'\n'
nl|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'f'
op|','
name|'f_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'xplorer'
op|'.'
name|'id'
op|','
name|'id'
op|'('
name|'f'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'isinstance'
op|'('
name|'xplorer'
op|','
name|'explorer'
op|'.'
name|'ExplorerFunction'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'xplorer'
op|'.'
name|'name'
op|','
name|'f_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_noArgs
dedent|''
dedent|''
name|'def'
name|'test_signature_noArgs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Testing zero-argument function signature.\n        """'
newline|'\n'
nl|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'function_noArgs'
op|','
string|"'function_noArgs'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'len'
op|'('
name|'xplorer'
op|'.'
name|'signature'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_simple
dedent|''
name|'def'
name|'test_signature_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Testing simple function signature.\n        """'
newline|'\n'
nl|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'function_simple'
op|','
string|"'function_simple'"
op|')'
newline|'\n'
nl|'\n'
name|'expected_signature'
op|'='
op|'('
string|"'a'"
op|','
string|"'b'"
op|','
string|"'c'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'xplorer'
op|'.'
name|'signature'
op|'.'
name|'name'
op|','
name|'expected_signature'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_variable
dedent|''
name|'def'
name|'test_signature_variable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Testing variable-argument function signature.\n        """'
newline|'\n'
nl|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'function_variable'
op|','
nl|'\n'
string|"'function_variable'"
op|')'
newline|'\n'
nl|'\n'
name|'expected_names'
op|'='
op|'('
string|"'a'"
op|','
string|"'kw'"
op|')'
newline|'\n'
name|'signature'
op|'='
name|'xplorer'
op|'.'
name|'signature'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'signature'
op|'.'
name|'name'
op|','
name|'expected_names'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'signature'
op|'.'
name|'is_varlist'
op|'('
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'signature'
op|'.'
name|'is_keyword'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_signature_crazy
dedent|''
name|'def'
name|'test_signature_crazy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Testing function with crazy signature.\n        """'
newline|'\n'
name|'xplorer'
op|'='
name|'self'
op|'.'
name|'pool'
op|'.'
name|'getExplorer'
op|'('
name|'function_crazy'
op|','
string|"'function_crazy'"
op|')'
newline|'\n'
nl|'\n'
name|'signature'
op|'='
name|'xplorer'
op|'.'
name|'signature'
newline|'\n'
nl|'\n'
name|'expected_signature'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'c'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'d'"
op|','
nl|'\n'
string|"'default'"
op|':'
name|'range'
op|'('
number|'4'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'kw'"
op|','
nl|'\n'
string|"'keywords'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\n'
nl|'\n'
comment|'# The name of the first argument seems to be indecipherable,'
nl|'\n'
comment|'# but make sure it has one (and no default).'
nl|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'signature'
op|'.'
name|'get_name'
op|'('
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'not'
name|'signature'
op|'.'
name|'get_default'
op|'('
number|'0'
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'signature'
op|'.'
name|'get_name'
op|'('
number|'1'
op|')'
op|','
string|"'c'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Get a list of values from a list of ExplorerImmutables.'
nl|'\n'
name|'arg_2_default'
op|'='
name|'map'
op|'('
name|'lambda'
name|'l'
op|':'
name|'l'
op|'.'
name|'value'
op|','
nl|'\n'
name|'signature'
op|'.'
name|'get_default'
op|'('
number|'2'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'get_elements'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'signature'
op|'.'
name|'get_name'
op|'('
number|'2'
op|')'
op|','
string|"'d'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'arg_2_default'
op|','
name|'range'
op|'('
number|'4'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'failUnlessEqual'
op|'('
name|'signature'
op|'.'
name|'get_name'
op|'('
number|'3'
op|')'
op|','
string|"'kw'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnless'
op|'('
name|'signature'
op|'.'
name|'is_keyword'
op|'('
number|'3'
op|')'
op|')'
newline|'\n'
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
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
