begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 Justin Santa Barbara'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExecuteTestCase
name|'class'
name|'ExecuteTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_retry_on_failure
indent|'    '
name|'def'
name|'test_retry_on_failure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fd'
op|','
name|'tmpfilename'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'_'
op|','
name|'tmpfilename2'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fp'
op|'='
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'fd'
op|','
string|"'w+'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|'\'\'\'#!/bin/sh\n# If stdin fails to get passed during one of the runs, make a note.\nif ! grep -q foo\nthen\n    echo \'failure\' > "$1"\nfi\n# If stdin has failed to get passed during this or a previous run, exit early.\nif grep failure "$1"\nthen\n    exit 1\nfi\nruns="$(cat $1)"\nif [ -z "$runs" ]\nthen\n    runs=0\nfi\nruns=$(($runs + 1))\necho $runs > "$1"\nexit 1\n\'\'\''
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chmod'
op|'('
name|'tmpfilename'
op|','
number|'0755'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|','
nl|'\n'
name|'tmpfilename'
op|','
name|'tmpfilename2'
op|','
name|'attempts'
op|'='
number|'10'
op|','
nl|'\n'
name|'process_input'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'delay_on_retry'
op|'='
name|'False'
op|')'
newline|'\n'
name|'fp'
op|'='
name|'open'
op|'('
name|'tmpfilename2'
op|','
string|"'r+'"
op|')'
newline|'\n'
name|'runs'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEquals'
op|'('
name|'runs'
op|'.'
name|'strip'
op|'('
op|')'
op|','
string|"'failure'"
op|','
string|"'stdin did not '"
nl|'\n'
string|"'always get passed '"
nl|'\n'
string|"'correctly'"
op|')'
newline|'\n'
name|'runs'
op|'='
name|'int'
op|'('
name|'runs'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'runs'
op|','
number|'10'
op|','
nl|'\n'
string|"'Ran %d times instead of 10.'"
op|'%'
op|'('
name|'runs'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'tmpfilename'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'tmpfilename2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unknown_kwargs_raises_error
dedent|''
dedent|''
name|'def'
name|'test_unknown_kwargs_raises_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|','
nl|'\n'
string|"'/bin/true'"
op|','
name|'this_is_not_a_valid_kwarg'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_retry_on_success
dedent|''
name|'def'
name|'test_no_retry_on_success'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fd'
op|','
name|'tmpfilename'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'_'
op|','
name|'tmpfilename2'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fp'
op|'='
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'fd'
op|','
string|"'w+'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|'\'\'\'#!/bin/sh\n# If we\'ve already run, bail out.\ngrep -q foo "$1" && exit 1\n# Mark that we\'ve run before.\necho foo > "$1"\n# Check that stdin gets passed correctly.\ngrep foo\n\'\'\''
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chmod'
op|'('
name|'tmpfilename'
op|','
number|'0755'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'tmpfilename'
op|','
nl|'\n'
name|'tmpfilename2'
op|','
nl|'\n'
name|'process_input'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'attempts'
op|'='
number|'2'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'tmpfilename'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'tmpfilename2'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetFromPathTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'GetFromPathTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_tolerates_nones
indent|'    '
name|'def'
name|'test_tolerates_nones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|'}'
op|','
op|'{'
string|"'a'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|'}'
op|','
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|'}'
op|','
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_does_select
dedent|''
name|'def'
name|'test_does_select'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
string|"'a_1'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'a_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'b_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'c_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|'}'
op|','
op|'{'
string|"'a'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'c_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|','
op|'{'
string|"'b'"
op|':'
name|'None'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'c_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_2'"
op|'}'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|'}'
op|','
op|'{'
string|"'b'"
op|':'
op|'{'
string|"'c'"
op|':'
string|"'c_2'"
op|'}'
op|'}'
op|']'
op|','
nl|'\n'
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'c'"
op|':'
string|"'c_1'"
op|'}'
op|','
op|'{'
string|"'c'"
op|':'
string|"'c_2'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'c_1'"
op|','
string|"'c_2'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c/d"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"c/a/b/d"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"i/r/t"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flattens_lists
dedent|''
name|'def'
name|'test_flattens_lists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|'}'
op|','
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'['
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'['
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|','
op|'{'
string|"'b'"
op|':'
op|'['
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'['
op|'{'
string|"'a'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|']'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'b_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_xpath
dedent|''
name|'def'
name|'test_bad_xpath'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"/a"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"/a/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"//"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"//a"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"a//a"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"a//a/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'f'
op|','
op|'['
op|']'
op|','
string|'"a/a/"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_real_failure1
dedent|''
name|'def'
name|'test_real_failure1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Real world failure case...'
nl|'\n'
comment|"#  We weren't coping when the input was a Dictionary instead of a List"
nl|'\n'
comment|'# This led to test_accepts_dictionaries'
nl|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'inst'
op|'='
op|'{'
string|"'fixed_ip'"
op|':'
op|'{'
string|"'floating_ips'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
string|"'1.2.3.4'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'192.168.0.3'"
op|'}'
op|','
nl|'\n'
string|"'hostname'"
op|':'
string|"''"
op|'}'
newline|'\n'
nl|'\n'
name|'private_ips'
op|'='
name|'f'
op|'('
name|'inst'
op|','
string|"'fixed_ip/address'"
op|')'
newline|'\n'
name|'public_ips'
op|'='
name|'f'
op|'('
name|'inst'
op|','
string|"'fixed_ip/floating_ips/address'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'192.168.0.3'"
op|']'
op|','
name|'private_ips'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'1.2.3.4'"
op|']'
op|','
name|'public_ips'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accepts_dictionaries
dedent|''
name|'def'
name|'test_accepts_dictionaries'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'utils'
op|'.'
name|'get_from_path'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
string|"'a'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
string|"'a'"
op|':'
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
string|"'a'"
op|':'
op|'['
op|'{'
string|"'b'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|']'
op|'}'
op|','
op|'{'
string|"'b'"
op|':'
op|'['
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
number|'3'
op|','
number|'4'
op|','
number|'5'
op|','
number|'6'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b/c"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'input'
op|'='
op|'{'
string|"'a'"
op|':'
op|'['
number|'1'
op|','
number|'2'
op|','
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
number|'1'
op|','
number|'2'
op|','
op|'{'
string|"'b'"
op|':'
string|"'b_1'"
op|'}'
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
string|"'b_1'"
op|']'
op|','
name|'f'
op|'('
name|'input'
op|','
string|'"a/b"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GenericUtilsTestCase
dedent|''
dedent|''
name|'class'
name|'GenericUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_parse_server_string
indent|'    '
name|'def'
name|'test_parse_server_string'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'::1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'::1'"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'[::1]:8773'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'::1'"
op|','
string|"'8773'"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'2001:db8::192.168.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'2001:db8::192.168.1.1'"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'[2001:db8::192.168.1.1]:8773'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'2001:db8::192.168.1.1'"
op|','
string|"'8773'"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'192.168.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'192.168.1.1'"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'192.168.1.2:8773'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'192.168.1.2'"
op|','
string|"'8773'"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'192.168.1.3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'192.168.1.3'"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'www.example.com:8443'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'www.example.com'"
op|','
string|"'8443'"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'www.example.com'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"'www.example.com'"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
comment|'# error case'
nl|'\n'
name|'result'
op|'='
name|'utils'
op|'.'
name|'parse_server_string'
op|'('
string|"'www.exa:mple.com:8443'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
string|"''"
op|','
string|"''"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IsUUIDLikeTestCase
dedent|''
dedent|''
name|'class'
name|'IsUUIDLikeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|assertUUIDLike
indent|'    '
name|'def'
name|'assertUUIDLike'
op|'('
name|'self'
op|','
name|'val'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'utils'
op|'.'
name|'is_uuid_like'
op|'('
name|'val'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_good_uuid
dedent|''
name|'def'
name|'test_good_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'val'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
name|'self'
op|'.'
name|'assertUUIDLike'
op|'('
name|'val'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_integer_passed
dedent|''
name|'def'
name|'test_integer_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'val'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertUUIDLike'
op|'('
name|'val'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_uuid_string_passed
dedent|''
name|'def'
name|'test_non_uuid_string_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'val'
op|'='
string|"'foo-fooo'"
newline|'\n'
name|'self'
op|'.'
name|'assertUUIDLike'
op|'('
name|'val'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
