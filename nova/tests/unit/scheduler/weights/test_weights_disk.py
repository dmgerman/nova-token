begin_unit
comment|'# Copyright 2011-2016 OpenStack Foundation'
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
string|'"""\nTests For Scheduler disk weights.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'weights'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'weights'
name|'import'
name|'disk'
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
name|'unit'
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskWeigherTestCase
name|'class'
name|'DiskWeigherTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'DiskWeigherTestCase'
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
name|'weight_handler'
op|'='
name|'weights'
op|'.'
name|'HostWeightHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weighers'
op|'='
op|'['
name|'disk'
op|'.'
name|'DiskWeigher'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_weighed_host
dedent|''
name|'def'
name|'_get_weighed_host'
op|'('
name|'self'
op|','
name|'hosts'
op|','
name|'weight_properties'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'weight_properties'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'weight_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_weighed_objects'
op|'('
name|'self'
op|'.'
name|'weighers'
op|','
nl|'\n'
name|'hosts'
op|','
name|'weight_properties'
op|')'
op|'['
number|'0'
op|']'
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
name|'host_values'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
string|"'free_disk_mb'"
op|':'
number|'5120'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
string|"'node2'"
op|','
op|'{'
string|"'free_disk_mb'"
op|':'
number|'10240'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host3'"
op|','
string|"'node3'"
op|','
op|'{'
string|"'free_disk_mb'"
op|':'
number|'30720'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
string|"'host4'"
op|','
string|"'node4'"
op|','
op|'{'
string|"'free_disk_mb'"
op|':'
number|'81920'
op|'}'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'return'
op|'['
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
name|'host'
op|','
name|'node'
op|','
name|'values'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'node'
op|','
name|'values'
name|'in'
name|'host_values'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_default_of_spreading_first
dedent|''
name|'def'
name|'test_default_of_spreading_first'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hostinfo_list'
op|'='
name|'self'
op|'.'
name|'_get_all_hosts'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# host1: free_disk_mb=5120'
nl|'\n'
comment|'# host2: free_disk_mb=10240'
nl|'\n'
comment|'# host3: free_disk_mb=30720'
nl|'\n'
comment|'# host4: free_disk_mb=81920'
nl|'\n'
nl|'\n'
comment|'# so, host4 should win:'
nl|'\n'
name|'weighed_host'
op|'='
name|'self'
op|'.'
name|'_get_weighed_host'
op|'('
name|'hostinfo_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1.0'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host4'"
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_multiplier1
dedent|''
name|'def'
name|'test_disk_filter_multiplier1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'disk_weight_multiplier'
op|'='
number|'0.0'
op|')'
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
comment|'# host1: free_disk_mb=5120'
nl|'\n'
comment|'# host2: free_disk_mb=10240'
nl|'\n'
comment|'# host3: free_disk_mb=30720'
nl|'\n'
comment|'# host4: free_disk_mb=81920'
nl|'\n'
nl|'\n'
comment|'# We do not know the host, all have same weight.'
nl|'\n'
name|'weighed_host'
op|'='
name|'self'
op|'.'
name|'_get_weighed_host'
op|'('
name|'hostinfo_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0.0'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_multiplier2
dedent|''
name|'def'
name|'test_disk_filter_multiplier2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'disk_weight_multiplier'
op|'='
number|'2.0'
op|')'
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
comment|'# host1: free_disk_mb=5120'
nl|'\n'
comment|'# host2: free_disk_mb=10240'
nl|'\n'
comment|'# host3: free_disk_mb=30720'
nl|'\n'
comment|'# host4: free_disk_mb=81920'
nl|'\n'
nl|'\n'
comment|'# so, host4 should win:'
nl|'\n'
name|'weighed_host'
op|'='
name|'self'
op|'.'
name|'_get_weighed_host'
op|'('
name|'hostinfo_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1.0'
op|'*'
number|'2'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host4'"
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_disk_filter_negative
dedent|''
name|'def'
name|'test_disk_filter_negative'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'disk_weight_multiplier'
op|'='
number|'1.0'
op|')'
newline|'\n'
name|'hostinfo_list'
op|'='
name|'self'
op|'.'
name|'_get_all_hosts'
op|'('
op|')'
newline|'\n'
name|'host_attr'
op|'='
op|'{'
string|"'id'"
op|':'
number|'100'
op|','
string|"'disk_mb'"
op|':'
number|'81920'
op|','
string|"'free_disk_mb'"
op|':'
op|'-'
number|'5120'
op|'}'
newline|'\n'
name|'host_state'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'negative'"
op|','
string|"'negative'"
op|','
name|'host_attr'
op|')'
newline|'\n'
name|'hostinfo_list'
op|'='
name|'list'
op|'('
name|'hostinfo_list'
op|')'
op|'+'
op|'['
name|'host_state'
op|']'
newline|'\n'
nl|'\n'
comment|'# host1: free_disk_mb=5120'
nl|'\n'
comment|'# host2: free_disk_mb=10240'
nl|'\n'
comment|'# host3: free_disk_mb=30720'
nl|'\n'
comment|'# host4: free_disk_mb=81920'
nl|'\n'
comment|'# negativehost: free_disk_mb=-5120'
nl|'\n'
nl|'\n'
comment|'# so, host4 should win'
nl|'\n'
name|'weights'
op|'='
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_weighed_objects'
op|'('
name|'self'
op|'.'
name|'weighers'
op|','
nl|'\n'
name|'hostinfo_list'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'weighed_host'
op|'='
name|'weights'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host4'"
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
comment|'# and negativehost should lose'
nl|'\n'
name|'weighed_host'
op|'='
name|'weights'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'weighed_host'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'negative'"
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
