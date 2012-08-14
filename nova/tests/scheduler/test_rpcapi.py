begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nUnit Tests for nova.scheduler.rpcapi\n"""'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
nl|'\n'
nl|'\n'
DECL|class|SchedulerRpcAPITestCase
name|'class'
name|'SchedulerRpcAPITestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'SchedulerRpcAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
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
name|'super'
op|'('
name|'SchedulerRpcAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_scheduler_api
dedent|''
name|'def'
name|'_test_scheduler_api'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'rpc_method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
name|'rpcapi'
op|'='
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|'('
op|')'
newline|'\n'
name|'expected_retval'
op|'='
string|"'foo'"
name|'if'
name|'method'
op|'=='
string|"'call'"
name|'else'
name|'None'
newline|'\n'
name|'expected_version'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'rpcapi'
op|'.'
name|'BASE_RPC_API_VERSION'
op|')'
newline|'\n'
name|'expected_msg'
op|'='
name|'rpcapi'
op|'.'
name|'make_msg'
op|'('
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'expected_msg'
op|'['
string|"'version'"
op|']'
op|'='
name|'expected_version'
newline|'\n'
name|'if'
name|'rpc_method'
op|'=='
string|"'cast'"
name|'and'
name|'method'
op|'=='
string|"'run_instance'"
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'call'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fake_args'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'fake_kwargs'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|_fake_rpc_method
name|'def'
name|'_fake_rpc_method'
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
name|'fake_args'
op|'='
name|'args'
newline|'\n'
name|'self'
op|'.'
name|'fake_kwargs'
op|'='
name|'kwargs'
newline|'\n'
name|'if'
name|'expected_retval'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'expected_retval'
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
name|'rpc'
op|','
name|'rpc_method'
op|','
name|'_fake_rpc_method'
op|')'
newline|'\n'
nl|'\n'
name|'retval'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|','
name|'method'
op|')'
op|'('
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retval'
op|','
name|'expected_retval'
op|')'
newline|'\n'
name|'expected_args'
op|'='
op|'['
name|'ctxt'
op|','
name|'FLAGS'
op|'.'
name|'scheduler_topic'
op|','
name|'expected_msg'
op|']'
newline|'\n'
name|'for'
name|'arg'
op|','
name|'expected_arg'
name|'in'
name|'zip'
op|'('
name|'self'
op|'.'
name|'fake_args'
op|','
name|'expected_args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'arg'
op|','
name|'expected_arg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_call
dedent|''
dedent|''
name|'def'
name|'test_run_instance_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'run_instance'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"'pw'"
op|','
name|'injected_files'
op|'='
string|"'fake_injected_files'"
op|','
nl|'\n'
name|'requested_networks'
op|'='
string|"'fake_requested_networks'"
op|','
nl|'\n'
name|'is_first_time'
op|'='
name|'True'
op|','
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'None'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance_cast
dedent|''
name|'def'
name|'test_run_instance_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'run_instance'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"'pw'"
op|','
name|'injected_files'
op|'='
string|"'fake_injected_files'"
op|','
nl|'\n'
name|'requested_networks'
op|'='
string|"'fake_requested_networks'"
op|','
nl|'\n'
name|'is_first_time'
op|'='
name|'True'
op|','
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'None'
op|','
name|'version'
op|'='
string|"'1.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_prep_resize
dedent|''
name|'def'
name|'test_prep_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'prep_resize'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
string|"'fake_instance'"
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'fake_type'"
op|','
name|'image'
op|'='
string|"'fake_image'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'filter_properties'
op|'='
string|"'fake_props'"
op|','
name|'version'
op|'='
string|"'1.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_host_resources
dedent|''
name|'def'
name|'test_show_host_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'show_host_resources'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_live_migration
dedent|''
name|'def'
name|'test_live_migration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'live_migration'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'block_migration'
op|'='
string|"'fake_block_migration'"
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
string|"'fake_disk_over_commit'"
op|','
nl|'\n'
name|'instance'
op|'='
string|"'fake_instance'"
op|','
name|'dest'
op|'='
string|"'fake_dest'"
op|','
name|'topic'
op|'='
string|"'fake_topic'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_service_capabilities
dedent|''
name|'def'
name|'test_update_service_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'rpc_method'
op|'='
string|"'fanout_cast'"
op|','
name|'service_name'
op|'='
string|"'fake_name'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'fake_host'"
op|','
name|'capabilities'
op|'='
string|"'fake_capabilities'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
