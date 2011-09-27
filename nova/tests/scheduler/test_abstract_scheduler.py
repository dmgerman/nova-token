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
string|'"""\nTests For Abstract Scheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'abstract_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'base_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'zone_manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_host_caps
name|'def'
name|'_host_caps'
op|'('
name|'multiplier'
op|')'
op|':'
newline|'\n'
comment|'# Returns host capabilities in the following way:'
nl|'\n'
comment|'# host1 = memory:free 10 (100max)'
nl|'\n'
comment|'#         disk:available 100 (1000max)'
nl|'\n'
comment|'# hostN = memory:free 10 + 10N'
nl|'\n'
comment|'#         disk:available 100 + 100N'
nl|'\n'
comment|'# in other words: hostN has more resources than host0'
nl|'\n'
comment|"# which means ... don't go above 10 hosts."
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|"'host_name-description'"
op|':'
string|"'XenServer %s'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_hostname'"
op|':'
string|"'xs-%s'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_memory_total'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'host_memory_overhead'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'host_memory_free'"
op|':'
number|'10'
op|'+'
name|'multiplier'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'host_memory_free-computed'"
op|':'
number|'10'
op|'+'
name|'multiplier'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'host_other-config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'host_ip_address'"
op|':'
string|"'192.168.1.%d'"
op|'%'
op|'('
number|'100'
op|'+'
name|'multiplier'
op|')'
op|','
nl|'\n'
string|"'host_cpu_info'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'disk_available'"
op|':'
number|'100'
op|'+'
name|'multiplier'
op|'*'
number|'100'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'disk_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'host_uuid'"
op|':'
string|"'xxx-%d'"
op|'%'
name|'multiplier'
op|','
nl|'\n'
string|"'host_name-label'"
op|':'
string|"'xs-%s'"
op|'%'
name|'multiplier'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_zone_manager_service_states
dedent|''
name|'def'
name|'fake_zone_manager_service_states'
op|'('
name|'num_hosts'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'num_hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'states'
op|'['
string|"'host%02d'"
op|'%'
op|'('
name|'x'
op|'+'
number|'1'
op|')'
op|']'
op|'='
op|'{'
string|"'compute'"
op|':'
name|'_host_caps'
op|'('
name|'x'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'states'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAbstractScheduler
dedent|''
name|'class'
name|'FakeAbstractScheduler'
op|'('
name|'abstract_scheduler'
op|'.'
name|'AbstractScheduler'
op|')'
op|':'
newline|'\n'
comment|'# No need to stub anything at the moment'
nl|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeBaseScheduler
dedent|''
name|'class'
name|'FakeBaseScheduler'
op|'('
name|'base_scheduler'
op|'.'
name|'BaseScheduler'
op|')'
op|':'
newline|'\n'
comment|'# No need to stub anything at the moment'
nl|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeZoneManager
dedent|''
name|'class'
name|'FakeZoneManager'
op|'('
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'service_states'
op|'='
op|'{'
nl|'\n'
string|"'host1'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'1073741824'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host2'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'2147483648'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host3'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'3221225472'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'host4'"
op|':'
op|'{'
nl|'\n'
string|"'compute'"
op|':'
op|'{'
string|"'host_memory_free'"
op|':'
number|'999999999'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeEmptyZoneManager
dedent|''
dedent|''
name|'class'
name|'FakeEmptyZoneManager'
op|'('
name|'zone_manager'
op|'.'
name|'ZoneManager'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
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
name|'service_states'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_empty_call_zone_method
dedent|''
dedent|''
name|'def'
name|'fake_empty_call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Hmm, I should probably be using mox for this.'
nl|'\n'
DECL|variable|was_called
dedent|''
name|'was_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource
name|'def'
name|'fake_provision_resource'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_ask_child_zone_to_create_instance
dedent|''
name|'def'
name|'fake_ask_child_zone_to_create_instance'
op|'('
name|'context'
op|','
name|'zone_info'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource_locally
dedent|''
name|'def'
name|'fake_provision_resource_locally'
op|'('
name|'context'
op|','
name|'build_plan'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_provision_resource_from_blob
dedent|''
name|'def'
name|'fake_provision_resource_from_blob'
op|'('
name|'context'
op|','
name|'item'
op|','
name|'request_spec'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_decrypt_blob_returns_local_info
dedent|''
name|'def'
name|'fake_decrypt_blob_returns_local_info'
op|'('
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'hostname'"
op|':'
string|"'foooooo'"
op|'}'
comment|"# values aren't important."
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_decrypt_blob_returns_child_info
dedent|''
name|'def'
name|'fake_decrypt_blob_returns_child_info'
op|'('
name|'blob'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'child_zone'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'child_blob'"
op|':'
name|'True'
op|'}'
comment|"# values aren't important. Keys are."
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_call_zone_method
dedent|''
name|'def'
name|'fake_call_zone_method'
op|'('
name|'context'
op|','
name|'method'
op|','
name|'specs'
op|','
name|'zones'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
op|'('
number|'1'
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'blob'
op|'='
string|"'AAAAAAA'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'111'
op|','
name|'blob'
op|'='
string|"'BBBBBBB'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'112'
op|','
name|'blob'
op|'='
string|"'CCCCCCC'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'113'
op|','
name|'blob'
op|'='
string|"'DDDDDDD'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|'('
number|'2'
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'120'
op|','
name|'blob'
op|'='
string|"'EEEEEEE'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'2'
op|','
name|'blob'
op|'='
string|"'FFFFFFF'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'122'
op|','
name|'blob'
op|'='
string|"'GGGGGGG'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'123'
op|','
name|'blob'
op|'='
string|"'HHHHHHH'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|'('
number|'3'
op|','
op|'['
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'130'
op|','
name|'blob'
op|'='
string|"'IIIIIII'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'131'
op|','
name|'blob'
op|'='
string|"'JJJJJJJ'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'132'
op|','
name|'blob'
op|'='
string|"'KKKKKKK'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'weight'
op|'='
number|'3'
op|','
name|'blob'
op|'='
string|"'LLLLLLL'"
op|')'
op|','
nl|'\n'
op|']'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_zone_get_all
dedent|''
name|'def'
name|'fake_zone_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'zone1'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'admin'"
op|','
name|'password'
op|'='
string|"'password'"
op|','
nl|'\n'
name|'weight_offset'
op|'='
number|'0.0'
op|','
name|'weight_scale'
op|'='
number|'1.0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'api_url'
op|'='
string|"'zone2'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'admin'"
op|','
name|'password'
op|'='
string|"'password'"
op|','
nl|'\n'
name|'weight_offset'
op|'='
number|'1000.0'
op|','
name|'weight_scale'
op|'='
number|'1.0'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'3'
op|','
name|'api_url'
op|'='
string|"'zone3'"
op|','
nl|'\n'
name|'username'
op|'='
string|"'admin'"
op|','
name|'password'
op|'='
string|"'password'"
op|','
nl|'\n'
name|'weight_offset'
op|'='
number|'0.0'
op|','
name|'weight_scale'
op|'='
number|'1000.0'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AbstractSchedulerTestCase
dedent|''
name|'class'
name|'AbstractSchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Abstract Scheduler."""'
newline|'\n'
nl|'\n'
DECL|member|test_abstract_scheduler
name|'def'
name|'test_abstract_scheduler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a nested set of FakeZones, try to build multiple instances\n        and ensure that a select call returns the appropriate build plan.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_call_zone_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|')'
newline|'\n'
name|'build_plan'
op|'='
name|'sched'
op|'.'
name|'select'
op|'('
name|'fake_context'
op|','
nl|'\n'
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'512'
op|'}'
op|','
nl|'\n'
string|"'num_instances'"
op|':'
number|'4'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# 4 from local zones, 12 from remotes'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'16'
op|','
name|'len'
op|'('
name|'build_plan'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'hostnames'
op|'='
op|'['
name|'plan_item'
op|'['
string|"'hostname'"
op|']'
nl|'\n'
name|'for'
name|'plan_item'
name|'in'
name|'build_plan'
name|'if'
string|"'hostname'"
name|'in'
name|'plan_item'
op|']'
newline|'\n'
comment|'# 4 local hosts'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'hostnames'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_adjust_child_weights
dedent|''
name|'def'
name|'test_adjust_child_weights'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure the weights returned by child zones are\n        properly adjusted based on the scale/offset in the zone\n        db entries.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'child_results'
op|'='
name|'fake_call_zone_method'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'zones'
op|'='
name|'fake_zone_get_all'
op|'('
name|'None'
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'_adjust_child_weights'
op|'('
name|'child_results'
op|','
name|'zones'
op|')'
newline|'\n'
name|'scaled'
op|'='
op|'['
number|'130000'
op|','
number|'131000'
op|','
number|'132000'
op|','
number|'3000'
op|']'
newline|'\n'
name|'for'
name|'zone'
op|','
name|'results'
name|'in'
name|'child_results'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'item'
name|'in'
name|'results'
op|':'
newline|'\n'
indent|'                '
name|'w'
op|'='
name|'item'
op|'['
string|"'weight'"
op|']'
newline|'\n'
name|'if'
name|'zone'
op|'=='
string|"'zone1'"
op|':'
comment|'# No change'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'w'
op|'<'
number|'1000.0'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'zone'
op|'=='
string|"'zone2'"
op|':'
comment|'# Offset +1000'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'w'
op|'>='
number|'1000.0'
name|'and'
name|'w'
op|'<'
number|'2000'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'zone'
op|'=='
string|"'zone3'"
op|':'
comment|'# Scale x1000'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'scaled'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
op|','
name|'w'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_empty_abstract_scheduler
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_empty_abstract_scheduler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure empty hosts & child_zones result in NoValidHosts exception.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_empty_call_zone_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeEmptyZoneManager'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'driver'
op|'.'
name|'NoValidHost'
op|','
name|'sched'
op|'.'
name|'schedule_run_instance'
op|','
nl|'\n'
name|'fake_context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host_filter'
op|'='
name|'None'
op|','
name|'instance_type'
op|'='
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_do_not_schedule_with_hint
dedent|''
name|'def'
name|'test_schedule_do_not_schedule_with_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check the local/child zone routing in the run_instance() call.\n        If the zone_blob hint was passed in, don\'t re-schedule.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource'"
op|','
name|'fake_provision_resource'
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'filter_driver'"
op|':'
string|"'nova.scheduler.host_filter.AllHostsFilter'"
op|','
nl|'\n'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'sched'
op|'.'
name|'schedule_run_instance'
op|'('
name|'None'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_local
dedent|''
name|'def'
name|'test_provision_resource_local'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource_locally'"
op|','
nl|'\n'
name|'fake_provision_resource_locally'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'hostname'"
op|':'
string|'"foo"'
op|'}'
newline|'\n'
name|'sched'
op|'.'
name|'_provision_resource'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_remote
dedent|''
name|'def'
name|'test_provision_resource_remote'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_provision_resource_from_blob'"
op|','
nl|'\n'
name|'fake_provision_resource_from_blob'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sched'
op|'.'
name|'_provision_resource'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_empty
dedent|''
name|'def'
name|'test_provision_resource_from_blob_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision a resource locally or remotely given no hints."""'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'abstract_scheduler'
op|'.'
name|'InvalidBlob'
op|','
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|','
nl|'\n'
name|'None'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_local_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_local_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when blob hint passed in.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|fake_create_db_entry_for_new_instance
name|'def'
name|'fake_create_db_entry_for_new_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'image'
op|','
name|'base_options'
op|','
name|'security_group'
op|','
nl|'\n'
name|'block_device_mapping'
op|','
name|'num'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'global'
name|'was_called'
newline|'\n'
name|'was_called'
op|'='
name|'True'
newline|'\n'
comment|'# return fake instances'
nl|'\n'
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
string|"'f874093c-7b17-49c0-89c3-22a5348497f9'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_cast_to_compute_host
dedent|''
name|'def'
name|'fake_cast_to_compute_host'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_decrypt_blob'"
op|','
nl|'\n'
name|'fake_decrypt_blob_returns_local_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|','
string|"'cast_to_compute_host'"
op|','
nl|'\n'
name|'fake_cast_to_compute_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'create_db_entry_for_new_instance'"
op|','
nl|'\n'
name|'fake_create_db_entry_for_new_instance'
op|')'
newline|'\n'
nl|'\n'
name|'build_plan_item'
op|'='
op|'{'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'image'"
op|':'
op|'{'
op|'}'
op|','
string|"'instance_properties'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'build_plan_item'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_child_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_child_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when child blob hint\n        passed in.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_decrypt_blob'"
op|','
nl|'\n'
name|'fake_decrypt_blob_returns_child_info'
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_ask_child_zone_to_create_instance'"
op|','
nl|'\n'
name|'fake_ask_child_zone_to_create_instance'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'blob'"
op|':'
string|'"Non-None blob data"'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_provision_resource_from_blob_with_immediate_child_blob
dedent|''
name|'def'
name|'test_provision_resource_from_blob_with_immediate_child_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Provision a resource locally or remotely when blob hint passed in\n        from an immediate child.\n        """'
newline|'\n'
name|'global'
name|'was_called'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'was_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_ask_child_zone_to_create_instance'"
op|','
nl|'\n'
name|'fake_ask_child_zone_to_create_instance'
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'child_blob'"
op|':'
name|'True'
op|','
string|"'child_zone'"
op|':'
name|'True'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_provision_resource_from_blob'
op|'('
name|'None'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'was_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_decrypt_blob
dedent|''
name|'def'
name|'test_decrypt_blob'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that the decrypt method works."""'
newline|'\n'
nl|'\n'
name|'fixture'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'test_data'
op|'='
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|StubDecryptor
name|'class'
name|'StubDecryptor'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|decryptor
indent|'            '
name|'def'
name|'decryptor'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'lambda'
name|'blob'
op|':'
name|'blob'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'abstract_scheduler'
op|','
string|"'crypto'"
op|','
nl|'\n'
name|'StubDecryptor'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fixture'
op|'.'
name|'_decrypt_blob'
op|'('
name|'test_data'
op|')'
op|','
nl|'\n'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'test_data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_empty_local_hosts
dedent|''
name|'def'
name|'test_empty_local_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a nested set of FakeZones, try to build multiple instances\n        and ensure that a select call returns the appropriate build plan.\n        """'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_call_zone_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
comment|'# patch this to have no local hosts'
nl|'\n'
name|'zm'
op|'.'
name|'service_states'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|')'
newline|'\n'
name|'build_plan'
op|'='
name|'sched'
op|'.'
name|'select'
op|'('
name|'fake_context'
op|','
nl|'\n'
op|'{'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'512'
op|'}'
op|','
nl|'\n'
string|"'num_instances'"
op|':'
number|'4'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# 0 from local zones, 12 from remotes'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'12'
op|','
name|'len'
op|'('
name|'build_plan'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_non_admin
dedent|''
name|'def'
name|'test_run_instance_non_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test creating an instance locally using run_instance, passing\n        a non-admin context.  DB actions should work."""'
newline|'\n'
name|'sched'
op|'='
name|'FakeAbstractScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_cast_to_compute_host
name|'def'
name|'fake_cast_to_compute_host'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_zone_get_all_zero
dedent|''
name|'def'
name|'fake_zone_get_all_zero'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# make sure this is called with admin context, even though'
nl|'\n'
comment|"# we're using user context below"
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'context'
op|'.'
name|'is_admin'
op|')'
newline|'\n'
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|','
string|"'cast_to_compute_host'"
op|','
nl|'\n'
name|'fake_cast_to_compute_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|','
string|"'_call_zone_method'"
op|','
name|'fake_call_zone_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all_zero'
op|')'
newline|'\n'
nl|'\n'
name|'zm'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'set_zone_manager'
op|'('
name|'zm'
op|')'
newline|'\n'
nl|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|')'
newline|'\n'
nl|'\n'
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'image'"
op|':'
op|'{'
string|"'properties'"
op|':'
op|'{'
op|'}'
op|'}'
op|','
nl|'\n'
string|"'security_group'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
nl|'\n'
string|"'project_id'"
op|':'
name|'fake_context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'fake_context'
op|'.'
name|'user_id'
op|'}'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'256'
op|'}'
op|','
nl|'\n'
string|"'filter_driver'"
op|':'
string|"'nova.scheduler.host_filter.AllHostsFilter'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'sched'
op|'.'
name|'schedule_run_instance'
op|'('
name|'fake_context'
op|','
name|'request_spec'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'instances'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'instances'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'_is_precooked'"
op|','
name|'False'
op|')'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'fake_context'
op|','
name|'instances'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseSchedulerTestCase
dedent|''
dedent|''
name|'class'
name|'BaseSchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Base Scheduler."""'
newline|'\n'
nl|'\n'
DECL|member|test_weigh_hosts
name|'def'
name|'test_weigh_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Try to weigh a short list of hosts and make sure enough\n        entries for a larger number instances are returned.\n        """'
newline|'\n'
nl|'\n'
name|'sched'
op|'='
name|'FakeBaseScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Fake out a list of hosts'
nl|'\n'
name|'zm'
op|'='
name|'FakeZoneManager'
op|'('
op|')'
newline|'\n'
name|'hostlist'
op|'='
op|'['
op|'('
name|'host'
op|','
name|'services'
op|'['
string|"'compute'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'host'
op|','
name|'services'
name|'in'
name|'zm'
op|'.'
name|'service_states'
op|'.'
name|'items'
op|'('
op|')'
nl|'\n'
name|'if'
string|"'compute'"
name|'in'
name|'services'
op|']'
newline|'\n'
nl|'\n'
comment|'# Call weigh_hosts()'
nl|'\n'
name|'num_instances'
op|'='
name|'len'
op|'('
name|'hostlist'
op|')'
op|'*'
number|'2'
op|'+'
name|'len'
op|'('
name|'hostlist'
op|')'
op|'/'
number|'2'
newline|'\n'
name|'instlist'
op|'='
name|'sched'
op|'.'
name|'weigh_hosts'
op|'('
string|"'compute'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'num_instances'
op|'='
name|'num_instances'
op|')'
op|','
nl|'\n'
name|'hostlist'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be enough entries to cover all instances'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'instlist'
op|')'
op|','
name|'num_instances'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
