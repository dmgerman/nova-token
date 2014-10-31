begin_unit
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'affinity_filter'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'my_ip'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.get_all'"
op|')'
newline|'\n'
DECL|class|TestDifferentHostFilter
name|'class'
name|'TestDifferentHostFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'super'
op|'('
name|'TestDifferentHostFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'affinity_filter'
op|'.'
name|'DifferentHostFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_different_filter_passes
dedent|''
name|'def'
name|'test_affinity_different_filter_passes'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'different_host'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_different_filter_no_list_passes
dedent|''
name|'def'
name|'test_affinity_different_filter_no_list_passes'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'different_host'"
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_different_filter_fails
dedent|''
name|'def'
name|'test_affinity_different_filter_fails'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instances'
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'different_host'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_different_filter_handles_none
dedent|''
name|'def'
name|'test_affinity_different_filter_handles_none'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'get_all_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.get_all'"
op|')'
newline|'\n'
DECL|class|TestSameHostFilter
name|'class'
name|'TestSameHostFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'super'
op|'('
name|'TestSameHostFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'affinity_filter'
op|'.'
name|'SameHostFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_same_filter_passes
dedent|''
name|'def'
name|'test_affinity_same_filter_passes'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'images'
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'same_host'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_same_filter_no_list_passes
dedent|''
name|'def'
name|'test_affinity_same_filter_no_list_passes'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'images'
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'same_host'"
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_same_filter_fails
dedent|''
name|'def'
name|'test_affinity_same_filter_fails'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'same_host'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'fake'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_same_filter_handles_none
dedent|''
name|'def'
name|'test_affinity_same_filter_handles_none'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'get_all_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestSimpleCIDRAffinityFilter
dedent|''
dedent|''
name|'class'
name|'TestSimpleCIDRAffinityFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'super'
op|'('
name|'TestSimpleCIDRAffinityFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'affinity_filter'
op|'.'
name|'SimpleCIDRAffinityFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_simple_cidr_filter_passes
dedent|''
name|'def'
name|'test_affinity_simple_cidr_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'host_ip'
op|'='
string|"'10.8.1.1'"
newline|'\n'
nl|'\n'
name|'affinity_ip'
op|'='
string|'"10.8.1.100"'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'/24'"
op|','
nl|'\n'
string|"'build_near_host_ip'"
op|':'
name|'affinity_ip'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_simple_cidr_filter_fails
dedent|''
name|'def'
name|'test_affinity_simple_cidr_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'host'
op|'.'
name|'host_ip'
op|'='
string|"'10.8.1.1'"
newline|'\n'
nl|'\n'
name|'affinity_ip'
op|'='
string|'"10.8.1.100"'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
op|'{'
nl|'\n'
string|"'cidr'"
op|':'
string|"'/32'"
op|','
nl|'\n'
string|"'build_near_host_ip'"
op|':'
name|'affinity_ip'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_affinity_simple_cidr_filter_handles_none
dedent|''
name|'def'
name|'test_affinity_simple_cidr_filter_handles_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'affinity_ip'
op|'='
name|'CONF'
op|'.'
name|'my_ip'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
number|'0'
op|':'
number|'3'
op|']'
newline|'\n'
name|'affinity_ip'
op|'.'
name|'append'
op|'('
string|"'100'"
op|')'
newline|'\n'
name|'affinity_ip'
op|'='
name|'str'
op|'.'
name|'join'
op|'('
string|"'.'"
op|','
name|'affinity_ip'
op|')'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'context'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
string|"'scheduler_hints'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGroupAffinityFilter
dedent|''
dedent|''
name|'class'
name|'TestGroupAffinityFilter'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_test_group_anti_affinity_filter_passes
indent|'    '
name|'def'
name|'_test_group_anti_affinity_filter_passes'
op|'('
name|'self'
op|','
name|'filt_cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'affinity'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|'}'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
op|'['
string|"'host2'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_passes
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_passes'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'ServerGroupAntiAffinityFilter'
op|'('
op|')'
op|','
nl|'\n'
string|"'anti-affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_passes_legacy
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_passes_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_passes'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'GroupAntiAffinityFilter'
op|'('
op|')'
op|','
nl|'\n'
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_anti_affinity_filter_fails
dedent|''
name|'def'
name|'_test_group_anti_affinity_filter_fails'
op|'('
name|'self'
op|','
name|'filt_cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_fails
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_fails'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'ServerGroupAntiAffinityFilter'
op|'('
op|')'
op|','
nl|'\n'
string|"'anti-affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_anti_affinity_filter_fails_legacy
dedent|''
name|'def'
name|'test_group_anti_affinity_filter_fails_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_anti_affinity_filter_fails'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'GroupAntiAffinityFilter'
op|'('
op|')'
op|','
nl|'\n'
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_affinity_filter_passes
dedent|''
name|'def'
name|'_test_group_affinity_filter_passes'
op|'('
name|'self'
op|','
name|'filt_cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'anti-affinity'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
string|"'affinity'"
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host1'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_passes
dedent|''
name|'def'
name|'test_group_affinity_filter_passes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_passes'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'ServerGroupAffinityFilter'
op|'('
op|')'
op|','
string|"'affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_passes_legacy
dedent|''
name|'def'
name|'test_group_affinity_filter_passes_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_passes'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'GroupAffinityFilter'
op|'('
op|')'
op|','
string|"'legacy'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_group_affinity_filter_fails
dedent|''
name|'def'
name|'_test_group_affinity_filter_fails'
op|'('
name|'self'
op|','
name|'filt_cls'
op|','
name|'policy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'group_policies'"
op|':'
op|'['
name|'policy'
op|']'
op|','
nl|'\n'
string|"'group_hosts'"
op|':'
op|'['
string|"'host2'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_fails
dedent|''
name|'def'
name|'test_group_affinity_filter_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_fails'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'ServerGroupAffinityFilter'
op|'('
op|')'
op|','
string|"'affinity'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_group_affinity_filter_fails_legacy
dedent|''
name|'def'
name|'test_group_affinity_filter_fails_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_group_affinity_filter_fails'
op|'('
nl|'\n'
name|'affinity_filter'
op|'.'
name|'GroupAffinityFilter'
op|'('
op|')'
op|','
string|"'legacy'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
