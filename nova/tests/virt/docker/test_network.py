begin_unit
comment|'# Copyright 2014 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
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
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'docker'
name|'import'
name|'network'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkTestCase
name|'class'
name|'NetworkTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
DECL|member|test_teardown_delete_network
name|'def'
name|'test_teardown_delete_network'
op|'('
name|'self'
op|','
name|'utils_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'id'
op|'='
string|'"second-id"'
newline|'\n'
name|'utils_mock'
op|'.'
name|'return_value'
op|'='
op|'('
string|'"first-id\\nsecond-id\\nthird-id\\n"'
op|','
name|'None'
op|')'
newline|'\n'
name|'network'
op|'.'
name|'teardown_network'
op|'('
name|'id'
op|')'
newline|'\n'
name|'utils_mock'
op|'.'
name|'assert_called_with'
op|'('
string|"'ip'"
op|','
string|"'netns'"
op|','
string|"'delete'"
op|','
name|'id'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
DECL|member|test_teardown_network_not_in_list
name|'def'
name|'test_teardown_network_not_in_list'
op|'('
name|'self'
op|','
name|'utils_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils_mock'
op|'.'
name|'return_value'
op|'='
op|'('
string|'"first-id\\nsecond-id\\nthird-id\\n"'
op|','
name|'None'
op|')'
newline|'\n'
name|'network'
op|'.'
name|'teardown_network'
op|'('
string|'"not-in-list"'
op|')'
newline|'\n'
name|'utils_mock'
op|'.'
name|'assert_called_with'
op|'('
string|"'ip'"
op|','
string|"'-o'"
op|','
string|"'netns'"
op|','
string|"'list'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'network'
op|','
string|"'LOG'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|')'
newline|'\n'
DECL|member|test_teardown_network_fails
name|'def'
name|'test_teardown_network_fails'
op|'('
name|'self'
op|','
name|'utils_mock'
op|','
name|'log_mock'
op|')'
op|':'
newline|'\n'
comment|'# Call fails but method should not fail.'
nl|'\n'
comment|'# Error will be caught and logged.'
nl|'\n'
indent|'        '
name|'utils_mock'
op|'.'
name|'return_value'
op|'='
op|'('
string|'"first-id\\nsecond-id\\nthird-id\\n"'
op|','
name|'None'
op|')'
newline|'\n'
name|'id'
op|'='
string|'"third-id"'
newline|'\n'
name|'network'
op|'.'
name|'teardown_network'
op|'('
name|'id'
op|')'
newline|'\n'
name|'log_mock'
op|'.'
name|'warning'
op|'.'
name|'assert_called_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
