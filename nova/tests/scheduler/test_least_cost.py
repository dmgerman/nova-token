begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nTests For Least Cost functions.\n"""'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'least_cost'
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
name|'import'
name|'matchers'
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
nl|'\n'
DECL|function|offset
name|'def'
name|'offset'
op|'('
name|'hostinfo'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'hostinfo'
op|'.'
name|'free_ram_mb'
op|'+'
number|'10000'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|scale
dedent|''
name|'def'
name|'scale'
op|'('
name|'hostinfo'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'hostinfo'
op|'.'
name|'free_ram_mb'
op|'*'
number|'2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LeastCostTestCase
dedent|''
name|'class'
name|'LeastCostTestCase'
op|'('
name|'test'
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
name|'super'
op|'('
name|'LeastCostTestCase'
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
name|'flags'
op|'('
name|'reserved_host_disk_mb'
op|'='
number|'0'
op|','
name|'reserved_host_memory_mb'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host_manager'
op|'='
name|'fakes'
op|'.'
name|'FakeHostManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_all_hosts
dedent|''
name|'def'
name|'_get_all_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'mox_host_manager_db_calls'
op|'('
name|'self'
op|'.'
name|'mox'
op|','
name|'ctxt'
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
name|'host_states'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ResetAll'
op|'('
op|')'
newline|'\n'
name|'return'
name|'host_states'
newline|'\n'
nl|'\n'
DECL|member|test_weighted_sum_happy_day
dedent|''
name|'def'
name|'test_weighted_sum_happy_day'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn_tuples'
op|'='
op|'['
op|'('
number|'1.0'
op|','
name|'offset'
op|')'
op|','
op|'('
number|'1.0'
op|','
name|'scale'
op|')'
op|']'
newline|'\n'
name|'hostinfo_list'
op|'='
name|'self'
op|'.'
name|'_get_all_hosts'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# host1: free_ram_mb=512'
nl|'\n'
comment|'# host2: free_ram_mb=1024'
nl|'\n'
comment|'# host3: free_ram_mb=3072'
nl|'\n'
comment|'# host4: free_ram_mb=8192'
nl|'\n'
nl|'\n'
comment|'# [offset, scale]='
nl|'\n'
comment|'# [10512, 11024, 13072, 18192]'
nl|'\n'
comment|'# [1024,  2048, 6144, 16384]'
nl|'\n'
nl|'\n'
comment|'# adjusted [ 1.0 * x + 1.0 * y] ='
nl|'\n'
comment|'# [11536, 13072, 19216, 34576]'
nl|'\n'
nl|'\n'
comment|'# so, host1 should win:'
nl|'\n'
name|'options'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'weighted_host'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
name|'fn_tuples'
op|','
name|'hostinfo_list'
op|','
nl|'\n'
name|'options'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'weighted_host'
op|'.'
name|'weight'
op|','
number|'11536'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'weighted_host'
op|'.'
name|'host_state'
op|'.'
name|'host'
op|','
string|"'host1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_weighted_sum_single_function
dedent|''
name|'def'
name|'test_weighted_sum_single_function'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fn_tuples'
op|'='
op|'['
op|'('
number|'1.0'
op|','
name|'offset'
op|')'
op|','
op|']'
newline|'\n'
name|'hostinfo_list'
op|'='
name|'self'
op|'.'
name|'_get_all_hosts'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# host1: free_ram_mb=0'
nl|'\n'
comment|'# host2: free_ram_mb=1536'
nl|'\n'
comment|'# host3: free_ram_mb=3072'
nl|'\n'
comment|'# host4: free_ram_mb=8192'
nl|'\n'
nl|'\n'
comment|'# [offset, ]='
nl|'\n'
comment|'# [10512, 11024, 13072, 18192]'
nl|'\n'
nl|'\n'
comment|'# so, host1 should win:'
nl|'\n'
name|'options'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'weighted_host'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
name|'fn_tuples'
op|','
name|'hostinfo_list'
op|','
nl|'\n'
name|'options'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'weighted_host'
op|'.'
name|'weight'
op|','
number|'10512'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'weighted_host'
op|'.'
name|'host_state'
op|'.'
name|'host'
op|','
string|"'host1'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWeightedHost
dedent|''
dedent|''
name|'class'
name|'TestWeightedHost'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_dict_conversion_without_host_state
indent|'    '
name|'def'
name|'test_dict_conversion_without_host_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
string|"'someweight'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'weight'"
op|':'
string|"'someweight'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'host'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dict_conversion_with_host_state
dedent|''
name|'def'
name|'test_dict_conversion_with_host_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host_state'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'somehost'"
op|','
name|'None'
op|')'
newline|'\n'
name|'host'
op|'='
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
string|"'someweight'"
op|','
name|'host_state'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'weight'"
op|':'
string|"'someweight'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'somehost'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'host'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
