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
string|'"""\nUnit Tests for nova.compute.rpcapi\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|class|ComputeRpcAPITestCase
name|'class'
name|'ComputeRpcAPITestCase'
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
name|'inst'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
string|"'fake_host'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
number|'1'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'inst'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ComputeRpcAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialized_instance_has_name
dedent|''
name|'def'
name|'test_serialized_instance_has_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'name'"
name|'in'
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_compute_api
dedent|''
name|'def'
name|'_test_compute_api'
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
nl|'\n'
name|'if'
string|"'rpcapi_class'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'rpcapi_class'
op|'='
name|'kwargs'
op|'['
string|"'rpcapi_class'"
op|']'
newline|'\n'
name|'del'
name|'kwargs'
op|'['
string|"'rpcapi_class'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rpcapi_class'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
newline|'\n'
dedent|''
name|'rpcapi'
op|'='
name|'rpcapi_class'
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
nl|'\n'
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
name|'if'
string|"'host_param'"
name|'in'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'host_param'
op|'='
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|'['
string|"'host_param'"
op|']'
newline|'\n'
name|'del'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|'['
string|"'host_param'"
op|']'
newline|'\n'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|'['
string|"'host'"
op|']'
op|'='
name|'host_param'
newline|'\n'
dedent|''
name|'elif'
string|"'host'"
name|'in'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'destination'"
name|'in'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'expected_msg'
op|'['
string|"'args'"
op|']'
op|'['
string|"'destination'"
op|']'
newline|'\n'
dedent|''
name|'expected_msg'
op|'['
string|"'version'"
op|']'
op|'='
name|'expected_version'
newline|'\n'
nl|'\n'
name|'cast_and_call'
op|'='
op|'['
string|"'confirm_resize'"
op|','
string|"'stop_instance'"
op|']'
newline|'\n'
name|'if'
name|'rpc_method'
op|'=='
string|"'call'"
name|'and'
name|'method'
name|'in'
name|'cast_and_call'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'['
string|"'cast'"
op|']'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'if'
string|"'host'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'kwargs'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'elif'
string|"'destination'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'kwargs'
op|'['
string|"'destination'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'kwargs'
op|'['
string|"'instance'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
dedent|''
name|'expected_topic'
op|'='
string|"'%s.%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'compute_topic'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
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
name|'expected_topic'
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
DECL|member|test_add_aggregate_host
dedent|''
dedent|''
name|'def'
name|'test_add_aggregate_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'add_aggregate_host'"
op|','
string|"'cast'"
op|','
name|'aggregate_id'
op|'='
string|"'id'"
op|','
nl|'\n'
name|'host_param'
op|'='
string|"'host'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
name|'slave_info'
op|'='
op|'{'
op|'}'
op|','
name|'version'
op|'='
string|"'2.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_to_instance
dedent|''
name|'def'
name|'test_add_fixed_ip_to_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'add_fixed_ip_to_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'network_id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume
dedent|''
name|'def'
name|'test_attach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'attach_volume'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'volume_id'
op|'='
string|"'id'"
op|','
name|'mountpoint'
op|'='
string|"'mp'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_change_instance_metadata
dedent|''
name|'def'
name|'test_change_instance_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'change_instance_metadata'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'diff'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_can_live_migrate_destination
dedent|''
name|'def'
name|'test_check_can_live_migrate_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'check_can_live_migrate_destination'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
nl|'\n'
name|'destination'
op|'='
string|"'dest'"
op|','
name|'block_migration'
op|'='
name|'True'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_can_live_migrate_source
dedent|''
name|'def'
name|'test_check_can_live_migrate_source'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'check_can_live_migrate_source'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
nl|'\n'
name|'dest_check_data'
op|'='
op|'{'
string|'"test"'
op|':'
string|'"data"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_confirm_resize_cast
dedent|''
name|'def'
name|'test_confirm_resize_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'confirm_resize'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|','
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|','
name|'version'
op|'='
string|"'2.7'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_confirm_resize_call
dedent|''
name|'def'
name|'test_confirm_resize_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'confirm_resize'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|','
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|','
name|'version'
op|'='
string|"'2.7'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_volume
dedent|''
name|'def'
name|'test_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'detach_volume'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'volume_id'
op|'='
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_finish_resize
dedent|''
name|'def'
name|'test_finish_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'finish_resize'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'image'
op|'='
string|"'image'"
op|','
name|'disk_info'
op|'='
string|"'disk_info'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|','
name|'version'
op|'='
string|"'2.8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_finish_revert_resize
dedent|''
name|'def'
name|'test_finish_revert_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'finish_revert_resize'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration_id'
op|'='
string|"'id'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output
dedent|''
name|'def'
name|'test_get_console_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_console_output'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'tail_length'
op|'='
string|"'tl'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_pool_info
dedent|''
name|'def'
name|'test_get_console_pool_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_console_pool_info'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'console_type'
op|'='
string|"'type'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_topic
dedent|''
name|'def'
name|'test_get_console_topic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_console_topic'"
op|','
string|"'call'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_diagnostics
dedent|''
name|'def'
name|'test_get_diagnostics'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_diagnostics'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_console
dedent|''
name|'def'
name|'test_get_vnc_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_vnc_console'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'console_type'
op|'='
string|"'type'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_maintenance_mode
dedent|''
name|'def'
name|'test_host_maintenance_mode'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'host_maintenance_mode'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'host_param'
op|'='
string|"'param'"
op|','
name|'mode'
op|'='
string|"'mode'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_host_power_action
dedent|''
name|'def'
name|'test_host_power_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'host_power_action'"
op|','
string|"'call'"
op|','
name|'action'
op|'='
string|"'action'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_file
dedent|''
name|'def'
name|'test_inject_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'inject_file'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'path'
op|'='
string|"'path'"
op|','
name|'file_contents'
op|'='
string|"'fc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_network_info
dedent|''
name|'def'
name|'test_inject_network_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'inject_network_info'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
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
name|'_test_compute_api'
op|'('
string|"'live_migration'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'dest'
op|'='
string|"'dest'"
op|','
nl|'\n'
name|'block_migration'
op|'='
string|"'blockity_block'"
op|','
name|'host'
op|'='
string|"'tsoh'"
op|','
nl|'\n'
name|'migrate_data'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_live_migration_at_destination
dedent|''
name|'def'
name|'test_post_live_migration_at_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'post_live_migration_at_destination'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'block_migration'
op|'='
string|"'block_migration'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pause_instance
dedent|''
name|'def'
name|'test_pause_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'pause_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_off_instance
dedent|''
name|'def'
name|'test_power_off_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'power_off_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_instance
dedent|''
name|'def'
name|'test_power_on_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'power_on_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pre_live_migration
dedent|''
name|'def'
name|'test_pre_live_migration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'pre_live_migration'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'block_migration'
op|'='
string|"'block_migration'"
op|','
nl|'\n'
name|'disk'
op|'='
string|"'disk'"
op|','
name|'host'
op|'='
string|"'host'"
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
name|'_test_compute_api'
op|'('
string|"'prep_resize'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'instance_type'
op|'='
string|"'fake_type'"
op|','
nl|'\n'
name|'image'
op|'='
string|"'fake_image'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_spec'"
op|','
nl|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'fakeprop'"
op|':'
string|"'fakeval'"
op|'}'
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.10'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot_instance
dedent|''
name|'def'
name|'test_reboot_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'maxDiff'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'reboot_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
nl|'\n'
name|'block_device_info'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'network_info'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'reboot_type'
op|'='
string|"'type'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.5'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_instance
dedent|''
name|'def'
name|'test_rebuild_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'rebuild_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'new_pass'
op|'='
string|"'pass'"
op|','
nl|'\n'
name|'injected_files'
op|'='
string|"'files'"
op|','
name|'image_ref'
op|'='
string|"'ref'"
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
string|"'orig_ref'"
op|','
nl|'\n'
name|'orig_sys_metadata'
op|'='
string|"'orig_sys_metadata'"
op|','
name|'version'
op|'='
string|"'2.1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reserve_block_device_name
dedent|''
name|'def'
name|'test_reserve_block_device_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'reserve_block_device_name'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'device'
op|'='
string|"'device'"
op|','
name|'volume_id'
op|'='
string|"'id'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.3'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'refresh_provider_fw_rules'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_security_group_rules
dedent|''
name|'def'
name|'test_refresh_security_group_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'refresh_security_group_rules'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'rpcapi_class'
op|'='
name|'compute_rpcapi'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
name|'security_group_id'
op|'='
string|"'id'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh_security_group_members
dedent|''
name|'def'
name|'test_refresh_security_group_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'refresh_security_group_members'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'rpcapi_class'
op|'='
name|'compute_rpcapi'
op|'.'
name|'SecurityGroupAPI'
op|','
nl|'\n'
name|'security_group_id'
op|'='
string|"'id'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_aggregate_host
dedent|''
name|'def'
name|'test_remove_aggregate_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'remove_aggregate_host'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'aggregate_id'
op|'='
string|"'id'"
op|','
name|'host_param'
op|'='
string|"'host'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'slave_info'
op|'='
op|'{'
op|'}'
op|','
name|'version'
op|'='
string|"'2.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'test_remove_fixed_ip_from_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'remove_fixed_ip_from_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'address'
op|'='
string|"'addr'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_volume_connection
dedent|''
name|'def'
name|'test_remove_volume_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'remove_volume_connection'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'volume_id'
op|'='
string|"'id'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_instance
dedent|''
name|'def'
name|'test_rescue_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'rescue_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'rescue_password'
op|'='
string|"'pw'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_network
dedent|''
name|'def'
name|'test_reset_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'reset_network'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resize_instance
dedent|''
name|'def'
name|'test_resize_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'resize_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_id'"
op|'}'
op|','
nl|'\n'
name|'image'
op|'='
string|"'image'"
op|','
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|','
name|'version'
op|'='
string|"'2.6'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resume_instance
dedent|''
name|'def'
name|'test_resume_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'resume_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_revert_resize
dedent|''
name|'def'
name|'test_revert_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'revert_resize'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'migration_id'
op|'='
string|"'id'"
op|','
name|'host'
op|'='
string|"'host'"
op|','
nl|'\n'
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rollback_live_migration_at_destination
dedent|''
name|'def'
name|'test_rollback_live_migration_at_destination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'rollback_live_migration_at_destination'"
op|','
nl|'\n'
string|"'cast'"
op|','
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance
dedent|''
name|'def'
name|'test_run_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'run_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'host'
op|'='
string|"'fake_host'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_spec'"
op|','
name|'filter_properties'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'requested_networks'
op|'='
string|"'networks'"
op|','
name|'injected_files'
op|'='
string|"'files'"
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"'pw'"
op|','
name|'is_first_time'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_admin_password
dedent|''
name|'def'
name|'test_set_admin_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'set_admin_password'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'new_pass'
op|'='
string|"'pw'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_host_enabled
dedent|''
name|'def'
name|'test_set_host_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'set_host_enabled'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'enabled'
op|'='
string|"'enabled'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_uptime
dedent|''
name|'def'
name|'test_get_host_uptime'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'get_host_uptime'"
op|','
string|"'call'"
op|','
name|'host'
op|'='
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_instance
dedent|''
name|'def'
name|'test_snapshot_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'snapshot_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'image_id'
op|'='
string|"'id'"
op|','
name|'image_type'
op|'='
string|"'type'"
op|','
nl|'\n'
name|'backup_type'
op|'='
string|"'type'"
op|','
name|'rotation'
op|'='
string|"'rotation'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_instance
dedent|''
name|'def'
name|'test_start_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'start_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_instance_cast
dedent|''
name|'def'
name|'test_stop_instance_cast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'stop_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_instance_call
dedent|''
name|'def'
name|'test_stop_instance_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'stop_instance'"
op|','
string|"'call'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_suspend_instance
dedent|''
name|'def'
name|'test_suspend_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'suspend_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_terminate_instance
dedent|''
name|'def'
name|'test_terminate_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'terminate_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|','
name|'bdms'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.4'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unpause_instance
dedent|''
name|'def'
name|'test_unpause_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'unpause_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unrescue_instance
dedent|''
name|'def'
name|'test_unrescue_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_compute_api'
op|'('
string|"'unrescue_instance'"
op|','
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'fake_instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
