begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nTests For Scheduler\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'mox'
name|'import'
name|'IgnoreArg'
newline|'\n'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
name|'as'
name|'auth_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'max_cores'"
op|','
string|"'nova.scheduler.simple'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDriver
name|'class'
name|'TestDriver'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Scheduler Driver for Tests"""'
newline|'\n'
DECL|member|schedule
name|'def'
name|'schedule'
op|'('
name|'context'
op|','
name|'topic'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'fallback_host'"
newline|'\n'
nl|'\n'
DECL|member|schedule_named_method
dedent|''
name|'def'
name|'schedule_named_method'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'num'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'named_host'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerTestCase
dedent|''
dedent|''
name|'class'
name|'SchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for scheduler"""'
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
name|'SchedulerTestCase'
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
name|'scheduler_driver'
op|'='
string|"'nova.tests.scheduler_unittest.TestDriver'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fallback
dedent|''
name|'def'
name|'test_fallback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'topic.fallback_host'"
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'noexist'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'num'"
op|':'
number|'7'
op|'}'
op|'}'
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
name|'scheduler'
op|'.'
name|'noexist'
op|'('
name|'ctxt'
op|','
string|"'topic'"
op|','
name|'num'
op|'='
number|'7'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_named_method
dedent|''
name|'def'
name|'test_named_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'topic.named_host'"
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'named_method'"
op|','
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'num'"
op|':'
number|'7'
op|'}'
op|'}'
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
name|'scheduler'
op|'.'
name|'named_method'
op|'('
name|'ctxt'
op|','
string|"'topic'"
op|','
name|'num'
op|'='
number|'7'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ZoneSchedulerTestCase
dedent|''
dedent|''
name|'class'
name|'ZoneSchedulerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for zone scheduler"""'
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
name|'ZoneSchedulerTestCase'
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
name|'scheduler_driver'
op|'='
string|"'nova.scheduler.zone.ZoneScheduler'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_service_model
dedent|''
name|'def'
name|'_create_service_model'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'models'
op|'.'
name|'Service'
op|'('
op|')'
newline|'\n'
name|'service'
op|'.'
name|'host'
op|'='
name|'kwargs'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'service'
op|'.'
name|'disabled'
op|'='
name|'False'
newline|'\n'
name|'service'
op|'.'
name|'deleted'
op|'='
name|'False'
newline|'\n'
name|'service'
op|'.'
name|'report_count'
op|'='
number|'0'
newline|'\n'
name|'service'
op|'.'
name|'binary'
op|'='
string|"'nova-compute'"
newline|'\n'
name|'service'
op|'.'
name|'topic'
op|'='
string|"'compute'"
newline|'\n'
name|'service'
op|'.'
name|'id'
op|'='
name|'kwargs'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'service'
op|'.'
name|'availability_zone'
op|'='
name|'kwargs'
op|'['
string|"'zone'"
op|']'
newline|'\n'
name|'service'
op|'.'
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_with_two_zones
dedent|''
name|'def'
name|'test_with_two_zones'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'service_list'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'_create_service_model'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'host1'"
op|','
name|'zone'
op|'='
string|"'zone1'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_service_model'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'host'
op|'='
string|"'host2'"
op|','
name|'zone'
op|'='
string|"'zone2'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_service_model'
op|'('
name|'id'
op|'='
number|'3'
op|','
name|'host'
op|'='
string|"'host3'"
op|','
name|'zone'
op|'='
string|"'zone2'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_service_model'
op|'('
name|'id'
op|'='
number|'4'
op|','
name|'host'
op|'='
string|"'host4'"
op|','
name|'zone'
op|'='
string|"'zone2'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_create_service_model'
op|'('
name|'id'
op|'='
number|'5'
op|','
name|'host'
op|'='
string|"'host5'"
op|','
name|'zone'
op|'='
string|"'zone2'"
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_get_all_by_topic'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'compute.host1'"
op|','
nl|'\n'
op|'{'
string|"'method'"
op|':'
string|"'create_instance'"
op|','
comment|'#TODO: check it'
nl|'\n'
string|"'args'"
op|':'
op|'{'
string|"'availability_zone'"
op|':'
string|"'zone1'"
op|'}'
op|'}'
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
name|'scheduler'
op|'.'
name|'create_instance'
op|'('
name|'ctxt'
op|','
string|"'compute'"
op|','
name|'availability_zone'
op|'='
string|"'zone1'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SimpleDriverTestCase
dedent|''
dedent|''
name|'class'
name|'SimpleDriverTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for simple driver"""'
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
name|'SimpleDriverTestCase'
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
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'max_cores'
op|'='
number|'4'
op|','
nl|'\n'
name|'max_gigabytes'
op|'='
number|'4'
op|','
nl|'\n'
name|'network_manager'
op|'='
string|"'nova.network.manager.FlatManager'"
op|','
nl|'\n'
name|'volume_driver'
op|'='
string|"'nova.volume.driver.FakeISCSIDriver'"
op|','
nl|'\n'
name|'scheduler_driver'
op|'='
string|"'nova.scheduler.simple.SimpleScheduler'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'='
name|'manager'
op|'.'
name|'SchedulerManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'auth_manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
string|"'ami-test'"
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.tiny'"
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test volume"""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'image_id'"
op|']'
op|'='
string|"'ami-test'"
newline|'\n'
name|'vol'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_hosts_are_up
dedent|''
name|'def'
name|'test_hosts_are_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures driver can find the hosts that are up"""'
newline|'\n'
comment|'# NOTE(vish): constructing service without create method'
nl|'\n'
comment|'#             because we are going to use it without queue'
nl|'\n'
name|'compute1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'hosts_up'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'compute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'hosts'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_least_busy_host_gets_instance
dedent|''
name|'def'
name|'test_least_busy_host_gets_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures the host with less cores gets the next one"""'
newline|'\n'
name|'compute1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'instance_id1'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id1'
op|')'
newline|'\n'
name|'instance_id2'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'schedule_run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
string|"'host2'"
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id1'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id2'
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_cores
dedent|''
name|'def'
name|'test_too_many_cores'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures we don\'t go over max cores"""'
newline|'\n'
name|'compute1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-compute'"
op|','
nl|'\n'
string|"'compute'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'instance_ids1'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance_ids2'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'max_cores'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'compute1'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ids1'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'run_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance_ids2'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'driver'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'schedule_run_instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids1'
op|':'
newline|'\n'
indent|'            '
name|'compute1'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids2'
op|':'
newline|'\n'
indent|'            '
name|'compute2'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'compute1'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'compute2'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_least_busy_host_gets_volume
dedent|''
name|'def'
name|'test_least_busy_host_gets_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures the host with less gigabytes gets the next one"""'
newline|'\n'
name|'volume1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-volume'"
op|','
nl|'\n'
string|"'volume'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'volume2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-volume'"
op|','
nl|'\n'
string|"'volume'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'volume2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'volume_id1'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id1'
op|')'
newline|'\n'
name|'volume_id2'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'schedule_create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
string|"'host2'"
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id1'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id2'
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'volume2'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_gigabytes
dedent|''
name|'def'
name|'test_too_many_gigabytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures we don\'t go over max gigabytes"""'
newline|'\n'
name|'volume1'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host1'"
op|','
nl|'\n'
string|"'nova-volume'"
op|','
nl|'\n'
string|"'volume'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'volume2'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'host2'"
op|','
nl|'\n'
string|"'nova-volume'"
op|','
nl|'\n'
string|"'volume'"
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_manager'
op|')'
newline|'\n'
name|'volume2'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'volume_ids1'
op|'='
op|'['
op|']'
newline|'\n'
name|'volume_ids2'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'index'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'max_gigabytes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'volume1'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ids1'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'volume2'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'volume_ids2'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'driver'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'self'
op|'.'
name|'scheduler'
op|'.'
name|'driver'
op|'.'
name|'schedule_create_volume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids1'
op|':'
newline|'\n'
indent|'            '
name|'volume1'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids2'
op|':'
newline|'\n'
indent|'            '
name|'volume2'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'volume1'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
name|'volume2'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
