begin_unit
comment|'#!/usr/bin/python2.4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2008 Google Inc.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""A very basic test class derived from mox.MoxTestBase, used by mox_test.py.\n\nThe class defined in this module is used to test the features of\nMoxTestBase and is not intended to be a standalone test.  It needs to\nbe in a separate module, because otherwise the tests in this class\n(which should not all pass) would be executed as part of the\nmox_test.py test suite.\n\nSee mox_test.MoxTestBaseTest for how this class is actually used.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
DECL|class|ExampleMoxTestMixin
name|'class'
name|'ExampleMoxTestMixin'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'  '
string|'"""Mix-in class for mox test case class.\n\n  It stubs out the same function as one of the test methods in\n  the example test case.  Both tests must pass as meta class wraps\n  test methods in all base classes.\n  """'
newline|'\n'
nl|'\n'
DECL|member|testStat
name|'def'
name|'testStat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'stat'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'stat'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'stat'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExampleMoxTest
dedent|''
dedent|''
name|'class'
name|'ExampleMoxTest'
op|'('
name|'mox'
op|'.'
name|'MoxTestBase'
op|','
name|'ExampleMoxTestMixin'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|DIR_PATH
indent|'  '
name|'DIR_PATH'
op|'='
string|"'/path/to/some/directory'"
newline|'\n'
nl|'\n'
DECL|member|testSuccess
name|'def'
name|'testSuccess'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testExpectedNotCalled
dedent|''
name|'def'
name|'testExpectedNotCalled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|testUnexpectedCall
dedent|''
name|'def'
name|'testUnexpectedCall'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
string|"'/path/to/some/other/directory'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testFailure
dedent|''
name|'def'
name|'testFailure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testStatOther
dedent|''
name|'def'
name|'testStatOther'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'stat'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'stat'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'stat'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
nl|'\n'
DECL|member|testHasStubs
dedent|''
name|'def'
name|'testHasStubs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'listdir_list'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|MockListdir
name|'def'
name|'MockListdir'
op|'('
name|'directory'
op|')'
op|':'
newline|'\n'
indent|'      '
name|'listdir_list'
op|'.'
name|'append'
op|'('
name|'directory'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|','
string|"'listdir'"
op|','
name|'MockListdir'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'DIR_PATH'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'DIR_PATH'
op|']'
op|','
name|'listdir_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestClassFromAnotherModule
dedent|''
dedent|''
name|'class'
name|'TestClassFromAnotherModule'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'  '
name|'def'
name|'__init__'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|Value
dedent|''
name|'def'
name|'Value'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"Not mock"'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
