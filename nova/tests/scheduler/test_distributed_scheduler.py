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
string|'"""\nTests For Distributed Scheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
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
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'distributed_scheduler'
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
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
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
nl|'\n'
DECL|function|fake_call_zone_method
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
number|'2'
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
number|'4'
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
number|'6'
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
number|'8'
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
number|'10'
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
number|'12'
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
number|'14'
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
number|'16'
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
number|'18'
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
number|'20'
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
number|'22'
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
number|'24'
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
DECL|function|fake_filter_hosts
dedent|''
name|'def'
name|'fake_filter_hosts'
op|'('
name|'hosts'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'list'
op|'('
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DistributedSchedulerTestCase
dedent|''
name|'class'
name|'DistributedSchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Distributed Scheduler."""'
newline|'\n'
nl|'\n'
DECL|member|test_adjust_child_weights
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
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
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
name|'weighted_hosts'
op|'='
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
name|'weighted_host'
name|'in'
name|'weighted_hosts'
op|':'
newline|'\n'
indent|'            '
name|'w'
op|'='
name|'weighted_host'
op|'.'
name|'weight'
newline|'\n'
name|'if'
name|'weighted_host'
op|'.'
name|'zone'
op|'=='
string|"'zone1'"
op|':'
comment|'# No change'
newline|'\n'
indent|'                '
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
name|'weighted_host'
op|'.'
name|'zone'
op|'=='
string|"'zone2'"
op|':'
comment|'# Offset +1000'
newline|'\n'
indent|'                '
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
name|'weighted_host'
op|'.'
name|'zone'
op|'=='
string|"'zone3'"
op|':'
comment|'# Scale x1000'
newline|'\n'
indent|'                '
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
DECL|member|test_run_instance_no_hosts
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_run_instance_no_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure empty hosts & child_zones result in NoValidHosts exception.\n        """'
newline|'\n'
DECL|function|_fake_empty_call_zone_method
name|'def'
name|'_fake_empty_call_zone_method'
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
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
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
nl|'\n'
name|'_fake_empty_call_zone_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
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
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1'
op|','
string|"'root_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_with_blob_hint
dedent|''
name|'def'
name|'test_run_instance_with_blob_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Check the local/child zone routing in the run_instance() call.\n        If the zone_blob hint was passed in, don\'t re-schedule.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'schedule_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'from_blob_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'locally_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'child_zone_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|_fake_schedule
name|'def'
name|'_fake_schedule'
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
name|'self'
op|'.'
name|'schedule_called'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
number|'1'
op|','
name|'host'
op|'='
string|"'x'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_make_weighted_host_from_blob
dedent|''
name|'def'
name|'_fake_make_weighted_host_from_blob'
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
name|'self'
op|'.'
name|'from_blob_called'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
number|'1'
op|','
name|'zone'
op|'='
string|"'x'"
op|','
name|'blob'
op|'='
string|"'y'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_provision_resource_locally
dedent|''
name|'def'
name|'_fake_provision_resource_locally'
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
name|'self'
op|'.'
name|'locally_called'
op|'='
name|'True'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|function|_fake_ask_child_zone_to_create_instance
dedent|''
name|'def'
name|'_fake_ask_child_zone_to_create_instance'
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
name|'self'
op|'.'
name|'child_zone_called'
op|'='
name|'True'
newline|'\n'
name|'return'
number|'2'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
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
string|"'_schedule'"
op|','
name|'_fake_schedule'
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
string|"'_make_weighted_host_from_blob'"
op|','
nl|'\n'
name|'_fake_make_weighted_host_from_blob'
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
string|"'_provision_resource_locally'"
op|','
nl|'\n'
name|'_fake_provision_resource_locally'
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
string|"'_ask_child_zone_to_create_instance'"
op|','
nl|'\n'
name|'_fake_ask_child_zone_to_create_instance'
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
name|'assertTrue'
op|'('
name|'instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'schedule_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'from_blob_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'child_zone_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'locally_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'instances'
op|','
op|'['
number|'2'
op|']'
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
name|'self'
op|'.'
name|'was_admin'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'was_admin'
op|'='
name|'context'
op|'.'
name|'is_admin'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
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
op|'.'
name|'host_manager'
op|','
string|"'get_all_host_states'"
op|','
name|'fake_get'
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
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'1'
op|','
string|"'local_gb'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'was_admin'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_bad_topic
dedent|''
name|'def'
name|'test_schedule_bad_topic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parameter checking."""'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
name|'sched'
op|'.'
name|'_schedule'
op|','
name|'fake_context'
op|','
nl|'\n'
string|'"foo"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_no_instance_type
dedent|''
name|'def'
name|'test_schedule_no_instance_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parameter checking."""'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'instance_properties'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
name|'sched'
op|'.'
name|'_schedule'
op|','
name|'fake_context'
op|','
nl|'\n'
string|'"compute"'
op|','
name|'request_spec'
op|'='
name|'request_spec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_happy_day
dedent|''
name|'def'
name|'test_schedule_happy_day'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure there\'s nothing glaringly wrong with _schedule()\n        by doing a happy day pass through."""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'1.0'
newline|'\n'
nl|'\n'
DECL|function|_fake_weighted_sum
name|'def'
name|'_fake_weighted_sum'
op|'('
name|'functions'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'next_weight'
op|'+='
number|'2.0'
newline|'\n'
name|'host'
op|','
name|'hostinfo'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
name|'self'
op|'.'
name|'next_weight'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'hostinfo'
op|'='
name|'hostinfo'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|'.'
name|'host_manager'
op|','
string|"'filter_hosts'"
op|','
nl|'\n'
name|'fake_filter_hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'least_cost'
op|','
string|"'weighted_sum'"
op|','
name|'_fake_weighted_sum'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
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
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'root_gb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'weighted_hosts'
op|'='
name|'sched'
op|'.'
name|'_schedule'
op|'('
name|'fake_context'
op|','
string|"'compute'"
op|','
nl|'\n'
name|'request_spec'
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
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'weighted_hosts'
op|')'
op|','
number|'10'
op|')'
newline|'\n'
name|'for'
name|'weighted_host'
name|'in'
name|'weighted_hosts'
op|':'
newline|'\n'
comment|'# We set this up so remote hosts have even weights ...'
nl|'\n'
indent|'            '
name|'if'
name|'int'
op|'('
name|'weighted_host'
op|'.'
name|'weight'
op|')'
op|'%'
number|'2'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'zone'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'host_state'
name|'is'
name|'None'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'host_state'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'zone'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_schedule_local_zone
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_schedule_local_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test to make sure _schedule makes no call out to zones if\n        local_zone_only in the filter_properties is True.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'1.0'
newline|'\n'
nl|'\n'
DECL|function|_fake_weighted_sum
name|'def'
name|'_fake_weighted_sum'
op|'('
name|'functions'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'next_weight'
op|'+='
number|'2.0'
newline|'\n'
name|'host'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
name|'self'
op|'.'
name|'next_weight'
op|','
name|'host_state'
op|'='
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user'"
op|','
string|"'project'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'fakes'
op|'.'
name|'mox_host_manager_db_calls'
op|'('
name|'self'
op|'.'
name|'mox'
op|','
name|'fake_context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'sched'
op|'.'
name|'host_manager'
op|','
string|"'filter_hosts'"
op|','
nl|'\n'
name|'fake_filter_hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'least_cost'
op|','
string|"'weighted_sum'"
op|','
name|'_fake_weighted_sum'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'fake_zone_get_all'
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
nl|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'root_gb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'256'
op|'}'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'project_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'local_zone_only'"
op|':'
name|'True'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'weighted_hosts'
op|'='
name|'sched'
op|'.'
name|'_schedule'
op|'('
name|'fake_context'
op|','
string|"'compute'"
op|','
nl|'\n'
name|'request_spec'
op|','
name|'filter_properties'
op|'='
name|'filter_properties'
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
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'weighted_hosts'
op|')'
op|','
number|'10'
op|')'
newline|'\n'
name|'for'
name|'weighted_host'
name|'in'
name|'weighted_hosts'
op|':'
newline|'\n'
comment|'# There should be no remote hosts'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'host_state'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'weighted_host'
op|'.'
name|'zone'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_decrypt_blob
dedent|''
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
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
name|'test_data'
op|'='
op|'{'
string|"'weight'"
op|':'
number|'1'
op|','
string|"'host'"
op|':'
string|"'x'"
op|','
string|"'blob'"
op|':'
string|"'y'"
op|','
string|"'zone'"
op|':'
string|"'z'"
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
name|'distributed_scheduler'
op|','
string|"'crypto'"
op|','
name|'StubDecryptor'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'weighted_host'
op|'='
name|'fixture'
op|'.'
name|'_make_weighted_host_from_blob'
op|'('
nl|'\n'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'test_data'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'weighted_host'
op|','
name|'least_cost'
op|'.'
name|'WeightedHost'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'weighted_host'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
name|'dict'
op|'('
name|'weight'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'x'"
op|','
nl|'\n'
name|'blob'
op|'='
string|"'y'"
op|','
name|'zone'
op|'='
string|"'z'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cost_functions
dedent|''
name|'def'
name|'test_get_cost_functions'
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
name|'reserved_host_memory_mb'
op|'='
number|'128'
op|')'
newline|'\n'
name|'fixture'
op|'='
name|'fakes'
op|'.'
name|'FakeDistributedScheduler'
op|'('
op|')'
newline|'\n'
name|'fns'
op|'='
name|'fixture'
op|'.'
name|'get_cost_functions'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'fns'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'weight'
op|','
name|'fn'
op|'='
name|'fns'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'weight'
op|','
number|'1.0'
op|')'
newline|'\n'
name|'hostinfo'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'hostinfo'
op|'.'
name|'update_from_compute_node'
op|'('
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'1000'
op|','
nl|'\n'
name|'local_gb'
op|'='
number|'0'
op|','
name|'vcpus'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1000'
op|'-'
number|'128'
op|','
name|'fn'
op|'('
name|'hostinfo'
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
