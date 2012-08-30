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
string|'"""\nTests For Filter Scheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
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
name|'filter_scheduler'
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
op|'.'
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'scheduler'
name|'import'
name|'test_scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_filter_hosts
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
DECL|class|FilterSchedulerTestCase
dedent|''
name|'class'
name|'FilterSchedulerTestCase'
op|'('
name|'test_scheduler'
op|'.'
name|'SchedulerTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Filter Scheduler."""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'filter_scheduler'
op|'.'
name|'FilterScheduler'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_no_hosts
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
name|'FakeFilterScheduler'
op|'('
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
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'None'
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
name|'FakeFilterScheduler'
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
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'None'
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
name|'FakeFilterScheduler'
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
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_scheduler_includes_launch_index
dedent|''
name|'def'
name|'test_scheduler_includes_launch_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
string|'"fake-context"'
newline|'\n'
name|'fake_kwargs'
op|'='
op|'{'
string|"'fake_kwarg1'"
op|':'
string|"'fake_value1'"
op|','
nl|'\n'
string|"'fake_kwarg2'"
op|':'
string|"'fake_value2'"
op|'}'
newline|'\n'
name|'instance_opts'
op|'='
op|'{'
string|"'fake_opt1'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'request_spec'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
name|'instance_opts'
op|'}'
newline|'\n'
name|'instance1'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid1'"
op|'}'
newline|'\n'
name|'instance2'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid2'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_has_launch_index
name|'def'
name|'_has_launch_index'
op|'('
name|'expected_index'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Return a function that verifies the expected index."""'
newline|'\n'
DECL|function|_check_launch_index
name|'def'
name|'_check_launch_index'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
string|"'instance_properties'"
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'launch_index'"
name|'in'
name|'value'
op|'['
string|"'instance_properties'"
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'index'
op|'='
name|'value'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'launch_index'"
op|']'
newline|'\n'
name|'if'
name|'index'
op|'=='
name|'expected_index'
op|':'
newline|'\n'
indent|'                            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'_check_launch_index'
newline|'\n'
nl|'\n'
DECL|class|ContextFake
dedent|''
name|'class'
name|'ContextFake'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|elevated
indent|'            '
name|'def'
name|'elevated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ctxt'
newline|'\n'
dedent|''
dedent|''
name|'context_fake'
op|'='
name|'ContextFake'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
string|"'_schedule'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
string|"'_provision_resource'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'context_fake'
op|','
string|"'compute'"
op|','
nl|'\n'
name|'request_spec'
op|','
op|'{'
op|'}'
nl|'\n'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|"'host1'"
op|','
string|"'host2'"
op|']'
op|')'
newline|'\n'
comment|'# instance 1'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_provision_resource'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'host1'"
op|','
nl|'\n'
name|'mox'
op|'.'
name|'Func'
op|'('
name|'_has_launch_index'
op|'('
number|'0'
op|')'
op|')'
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'reservations'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance1'
op|')'
newline|'\n'
comment|'# instance 2'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_provision_resource'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'host2'"
op|','
nl|'\n'
name|'mox'
op|'.'
name|'Func'
op|'('
name|'_has_launch_index'
op|'('
number|'1'
op|')'
op|')'
op|','
op|'{'
op|'}'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'reservations'
op|'='
name|'None'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'instance2'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'schedule_run_instance'
op|'('
name|'context_fake'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
op|'{'
op|'}'
op|','
name|'None'
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
name|'host_state'
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
nl|'\n'
name|'host_state'
op|'='
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
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
op|','
nl|'\n'
string|"'vcpus'"
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
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'memory_mb'"
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
op|'{'
op|'}'
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
nl|'\n'
DECL|member|test_schedule_prep_resize_doesnt_update_host
dedent|''
dedent|''
name|'def'
name|'test_schedule_prep_resize_doesnt_update_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_return_hosts
name|'def'
name|'_return_hosts'
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
name|'host_state'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host2'"
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'return'
op|'['
name|'least_cost'
op|'.'
name|'WeightedHost'
op|'('
number|'1.0'
op|','
name|'host_state'
op|'='
name|'host_state'
op|')'
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
name|'sched'
op|','
string|"'_schedule'"
op|','
name|'_return_hosts'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
op|'{'
string|"'called'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_fake_instance_update_db
name|'def'
name|'_fake_instance_update_db'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# This should not be called'
nl|'\n'
indent|'            '
name|'info'
op|'['
string|"'called'"
op|']'
op|'='
number|'1'
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
string|"'instance_update_db'"
op|','
nl|'\n'
name|'_fake_instance_update_db'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake-uuid'"
op|','
string|"'host'"
op|':'
string|"'host1'"
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'schedule_prep_resize'
op|'('
name|'fake_context'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|','
name|'instance'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'called'"
op|']'
op|','
number|'0'
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
name|'FakeFilterScheduler'
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
op|'-'
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
op|','
name|'disk_available_least'
op|'='
number|'1000'
op|','
nl|'\n'
name|'free_disk_mb'
op|'='
number|'1000'
op|','
name|'free_ram_mb'
op|'='
number|'1000'
op|','
name|'vcpus_used'
op|'='
number|'0'
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
nl|'\n'
DECL|member|test_max_attempts
dedent|''
name|'def'
name|'test_max_attempts'
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
name|'scheduler_max_attempts'
op|'='
number|'4'
op|')'
newline|'\n'
nl|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'sched'
op|'.'
name|'_max_attempts'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_max_attempts
dedent|''
name|'def'
name|'test_invalid_max_attempts'
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
name|'scheduler_max_attempts'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
name|'sched'
op|'.'
name|'_max_attempts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retry_disabled
dedent|''
name|'def'
name|'test_retry_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retry info should not get populated when re-scheduling is off"""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'1'
op|')'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'instance_properties'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
comment|'# should not have retry info in the populated filter properties:'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|'"retry"'
name|'in'
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retry_attempt_one
dedent|''
name|'def'
name|'test_retry_attempt_one'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test retry logic on initial scheduling attempt"""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'2'
op|')'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'instance_properties'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
name|'num_attempts'
op|'='
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'num_attempts'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'num_attempts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retry_attempt_two
dedent|''
name|'def'
name|'test_retry_attempt_two'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test retry logic when re-scheduling"""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'2'
op|')'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'instance_properties'
op|')'
newline|'\n'
nl|'\n'
name|'retry'
op|'='
name|'dict'
op|'('
name|'num_attempts'
op|'='
number|'1'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'retry'
op|')'
newline|'\n'
nl|'\n'
name|'sched'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
name|'num_attempts'
op|'='
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'num_attempts'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'num_attempts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retry_exceeded_max_attempts
dedent|''
name|'def'
name|'test_retry_exceeded_max_attempts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test for necessary explosion when max retries is exceeded"""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'2'
op|')'
newline|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_properties'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'request_spec'
op|'='
name|'dict'
op|'('
name|'instance_properties'
op|'='
name|'instance_properties'
op|')'
newline|'\n'
nl|'\n'
name|'retry'
op|'='
name|'dict'
op|'('
name|'num_attempts'
op|'='
number|'2'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'retry'
op|')'
newline|'\n'
nl|'\n'
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
name|'_schedule'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'compute'"
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_retry_host
dedent|''
name|'def'
name|'test_add_retry_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'retry'
op|'='
name|'dict'
op|'('
name|'num_attempts'
op|'='
number|'1'
op|','
name|'hosts'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'retry'
op|')'
newline|'\n'
name|'host'
op|'='
string|'"fakehost"'
newline|'\n'
nl|'\n'
name|'sched'
op|'='
name|'fakes'
op|'.'
name|'FakeFilterScheduler'
op|'('
op|')'
newline|'\n'
name|'sched'
op|'.'
name|'_add_retry_host'
op|'('
name|'filter_properties'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'hosts'
op|'='
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'hosts'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
name|'hosts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
