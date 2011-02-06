begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nTests For Nova-Manage\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaManageTestCase
name|'class'
name|'NovaManageTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for nova-manage"""'
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
name|'super'
op|'('
name|'NovaManageTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_instance_types
dedent|''
name|'def'
name|'test_create_and_delete_instance_types'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"create"'
op|','
string|'"test"'
op|','
string|'"256"'
op|','
string|'"1"'
op|','
string|'"120"'
op|','
string|'"99"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'retcode'
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"delete"'
op|','
string|'"test"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'retcode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_instance_types
dedent|''
name|'def'
name|'test_list_instance_types'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"list"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'retcode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_specific_instance_type
dedent|''
name|'def'
name|'test_list_specific_instance_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"list"'
op|','
nl|'\n'
string|'"m1.medium"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'retcode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_should_raise_on_bad_create_args
dedent|''
name|'def'
name|'test_should_raise_on_bad_create_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"create"'
op|','
string|'"test"'
op|','
string|'"256"'
op|','
string|'"0"'
op|','
string|'"120"'
op|','
string|'"99"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'retcode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_should_fail_on_duplicate_flavorid
dedent|''
name|'def'
name|'test_should_fail_on_duplicate_flavorid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"create"'
op|','
string|'"test"'
op|','
string|'"256"'
op|','
string|'"1"'
op|','
string|'"120"'
op|','
string|'"1"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'retcode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_delete_should_fail_without_valid_name
dedent|''
name|'def'
name|'test_instance_type_delete_should_fail_without_valid_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fnull'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'devnull'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'retcode'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
op|'['
string|'"bin/nova-manage"'
op|','
string|'"instance_type"'
op|','
string|'"delete"'
op|','
string|'"saefasff"'
op|']'
op|','
name|'stdout'
op|'='
name|'fnull'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'retcode'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
