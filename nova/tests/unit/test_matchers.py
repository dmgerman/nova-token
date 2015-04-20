begin_unit
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
name|'from'
name|'collections'
name|'import'
name|'OrderedDict'
newline|'\n'
name|'import'
name|'testtools'
newline|'\n'
name|'from'
name|'testtools'
op|'.'
name|'tests'
op|'.'
name|'matchers'
name|'import'
name|'helpers'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'matchers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDictMatches
name|'class'
name|'TestDictMatches'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|','
name|'helpers'
op|'.'
name|'TestMatchersInterface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|matches_dict
indent|'    '
name|'matches_dict'
op|'='
name|'OrderedDict'
op|'('
name|'sorted'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
DECL|variable|matches_matcher
name|'matches_matcher'
op|'='
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
nl|'\n'
name|'matches_dict'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|matches_matches
name|'matches_matches'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'noox'"
op|','
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|matches_mismatches
name|'matches_mismatches'
op|'='
op|'['
nl|'\n'
op|'{'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'qux'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bop'"
op|','
string|"'baz'"
op|':'
string|"'qux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|str_examples
name|'str_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"DictMatches({0})"'
op|'.'
name|'format'
op|'('
name|'matches_dict'
op|')'
op|','
nl|'\n'
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|describe_examples
name|'describe_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"Keys in d1 and not d2: {0}. Keys in d2 and not d1: []"'
nl|'\n'
op|'.'
name|'format'
op|'('
name|'str'
op|'('
name|'sorted'
op|'('
name|'matches_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|')'
op|')'
op|','
op|'{'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"Dictionaries do not match at fluffy. d1: False d2: True"'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"Dictionaries do not match at foo. d1: bar d2: bop"'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bop'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDictListMatches
dedent|''
name|'class'
name|'TestDictListMatches'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|','
name|'helpers'
op|'.'
name|'TestMatchersInterface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|matches_matcher
indent|'    '
name|'matches_matcher'
op|'='
name|'matchers'
op|'.'
name|'DictListMatches'
op|'('
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|matches_matches
name|'matches_matches'
op|'='
op|'['
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'qoox'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|matches_mismatches
name|'matches_mismatches'
op|'='
op|'['
nl|'\n'
op|'['
op|']'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'qoox'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'cat'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bop'"
op|','
string|"'baz'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|str_examples
name|'str_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"DictListMatches([{\'baz\': \'DONTCARE\', \'cat\':"'
nl|'\n'
string|'" {\'fluffy\': False, \'tabby\': True}, \'foo\': \'bar\'},\\n"'
nl|'\n'
string|'" {\'dog\': \'yorkie\'}])"'
op|','
nl|'\n'
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|describe_examples
name|'describe_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"Length mismatch: len(L1)=2 != len(L2)=0"'
op|','
op|'{'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"Dictionaries do not match at fluffy. d1: True d2: False"'
op|','
nl|'\n'
op|'['
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'qoox'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'dog'"
op|':'
string|"'yorkie'"
op|'}'
op|']'
op|','
nl|'\n'
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIsSubDictOf
dedent|''
name|'class'
name|'TestIsSubDictOf'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|','
name|'helpers'
op|'.'
name|'TestMatchersInterface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|matches_matcher
indent|'    '
name|'matches_matcher'
op|'='
name|'matchers'
op|'.'
name|'IsSubDictOf'
op|'('
nl|'\n'
name|'OrderedDict'
op|'('
name|'sorted'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|matches_matches
name|'matches_matches'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'noox'"
op|','
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|'}'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|matches_mismatches
name|'matches_mismatches'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bop'"
op|','
string|"'baz'"
op|':'
string|"'qux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|','
string|"'dog'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|str_examples
name|'str_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"IsSubDictOf({0})"'
op|'.'
name|'format'
op|'('
nl|'\n'
name|'str'
op|'('
name|'OrderedDict'
op|'('
name|'sorted'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
op|')'
op|')'
op|','
nl|'\n'
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|describe_examples
name|'describe_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"Dictionaries do not match at fluffy. d1: False d2: True"'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"Dictionaries do not match at foo. d1: bar d2: bop"'
op|','
nl|'\n'
op|'{'
string|"'foo'"
op|':'
string|"'bop'"
op|','
string|"'baz'"
op|':'
string|"'quux'"
op|','
nl|'\n'
string|"'cat'"
op|':'
op|'{'
string|"'tabby'"
op|':'
name|'True'
op|','
string|"'fluffy'"
op|':'
name|'False'
op|'}'
op|'}'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestXMLMatches
dedent|''
name|'class'
name|'TestXMLMatches'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|','
name|'helpers'
op|'.'
name|'TestMatchersInterface'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'matches_matcher'
op|'='
name|'matchers'
op|'.'
name|'XMLMatches'
op|'('
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="DONTCARE"/>\n  <children>\n    <!--This is a comment-->\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>DONTCARE</child3>\n    <?spam processing instruction?>\n  </children>\n</root>"""'
op|','
name|'allow_mixed_nodes'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'matches_matches'
op|'='
op|'['
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key2="spam" key1="spam"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children><child1>child 1</child1>\n<child2>child 2</child2>\n<child3>blah</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'matches_mismatches'
op|'='
op|'['
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>mismatch text</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key3="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="quux" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child4>child 4</child4>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n    <child4>child 4</child4>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="DONTCARE"/>\n  <children>\n    <!--This is a comment-->\n    <child2>child 2</child2>\n    <child1>child 1</child1>\n    <child3>DONTCARE</child3>\n    <?spam processing instruction?>\n  </children>\n</root>"""'
op|','
nl|'\n'
string|'"""<?xml version="1.1"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="DONTCARE"/>\n  <children>\n    <!--This is a comment-->\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>DONTCARE</child3>\n    <?spam processing instruction?>\n  </children>\n</root>"""'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|str_examples
name|'str_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"XMLMatches(\'<?xml version=\\"1.0\\"?>\\\\n"'
nl|'\n'
string|'"<root>\\\\n"'
nl|'\n'
string|'"  <text>some text here</text>\\\\n"'
nl|'\n'
string|'"  <text>some other text here</text>\\\\n"'
nl|'\n'
string|'"  <attrs key1=\\"spam\\" key2=\\"DONTCARE\\"/>\\\\n"'
nl|'\n'
string|'"  <children>\\\\n"'
nl|'\n'
string|'"    <!--This is a comment-->\\\\n"'
nl|'\n'
string|'"    <child1>child 1</child1>\\\\n"'
nl|'\n'
string|'"    <child2>child 2</child2>\\\\n"'
nl|'\n'
string|'"    <child3>DONTCARE</child3>\\\\n"'
nl|'\n'
string|'"    <?spam processing instruction?>\\\\n"'
nl|'\n'
string|'"  </children>\\\\n"'
nl|'\n'
string|'"</root>\')"'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|describe_examples
name|'describe_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"/root/text[1]: XML text value mismatch: expected text value: "'
nl|'\n'
string|'"[\'some other text here\']; actual value: [\'mismatch text\']"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>mismatch text</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/attrs[2]: XML attributes mismatch: keys only in expected: "'
nl|'\n'
string|'"key2; keys only in actual: key3"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key3="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/attrs[2]: XML attribute value mismatch: expected value of "'
nl|'\n'
string|'"attribute key1: \'spam\'; actual value: \'quux\'"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="quux" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/children[3]: XML tag mismatch at index 1: expected tag "'
nl|'\n'
string|'"<child2>; actual tag <child4>"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child4>child 4</child4>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/children[3]: XML expected child element <child3> not "'
nl|'\n'
string|'"present at index 2"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/children[3]: XML unexpected child element <child4> "'
nl|'\n'
string|'"present at index 3"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n    <child4>child 4</child4>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/root/children[3]: XML tag mismatch at index 0: "'
nl|'\n'
string|'"expected tag <child1>; actual tag <child2>"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child2>child 2</child2>\n    <child1>child 1</child1>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|'('
string|'"/: XML information mismatch(version, encoding) "'
nl|'\n'
string|'"expected version 1.0, expected encoding UTF-8; "'
nl|'\n'
string|'"actual version 1.1, actual encoding UTF-8"'
op|','
nl|'\n'
string|'"""<?xml version="1.1"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="DONTCARE"/>\n  <children>\n    <!--This is a comment-->\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>DONTCARE</child3>\n    <?spam processing instruction?>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestXMLMatchesUnorderedNodes'
op|'('
name|'testtools'
op|'.'
name|'TestCase'
op|','
nl|'\n'
DECL|class|TestXMLMatchesUnorderedNodes
name|'helpers'
op|'.'
name|'TestMatchersInterface'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'matches_matcher'
op|'='
name|'matchers'
op|'.'
name|'XMLMatches'
op|'('
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>some other text here</text>\n  <attrs key1="spam" key2="DONTCARE"/>\n  <children>\n    <child3>DONTCARE</child3>\n    <!--This is a comment-->\n    <child2>child 2</child2>\n    <child1>child 1</child1>\n    <?spam processing instruction?>\n  </children>\n</root>"""'
op|','
name|'allow_mixed_nodes'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'matches_matches'
op|'='
op|'['
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <attrs key2="spam" key1="spam"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n  <text>some other text here</text>\n</root>"""'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'matches_mismatches'
op|'='
op|'['
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>mismatch text</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|describe_examples
name|'describe_examples'
op|'='
op|'['
nl|'\n'
op|'('
string|'"/root: XML expected child element <text> not present at index 4"'
op|','
nl|'\n'
string|'"""<?xml version="1.0"?>\n<root>\n  <text>some text here</text>\n  <text>mismatch text</text>\n  <attrs key1="spam" key2="quux"/>\n  <children>\n    <child1>child 1</child1>\n    <child2>child 2</child2>\n    <child3>child 3</child3>\n  </children>\n</root>"""'
op|','
name|'matches_matcher'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|str_examples
name|'str_examples'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
