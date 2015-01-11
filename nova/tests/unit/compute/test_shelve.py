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
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'claims'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'compute'
name|'import'
name|'test_compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
name|'as'
name|'fake_image'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'shelved_offload_time'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_resources
name|'def'
name|'_fake_resources'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'resources'
op|'='
op|'{'
nl|'\n'
string|"'memory_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'memory_mb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'free_ram_mb'"
op|':'
number|'2048'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'local_gb_used'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'free_disk_gb'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'vcpus_used'"
op|':'
number|'0'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelveComputeManagerTestCase
dedent|''
name|'class'
name|'ShelveComputeManagerTestCase'
op|'('
name|'test_compute'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_shelve_instance
indent|'    '
name|'def'
name|'_shelve_instance'
op|'('
name|'self'
op|','
name|'shelved_offload_time'
op|','
name|'clean_shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'shelved_offload_time'"
op|','
name|'shelved_offload_time'
op|')'
newline|'\n'
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
name|'params'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'image_id'
op|'='
string|"'fake_image_id'"
newline|'\n'
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'SHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'snapshot'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'power_off'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
name|'compute'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'cleanup_instance_network_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve.start'"
op|')'
newline|'\n'
name|'if'
name|'clean_shutdown'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'shutdown_timeout'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'SHUTDOWN_RETRY_INTERVAL'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'network_api'
op|'.'
name|'cleanup_instance_network_on_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'instance'
op|'.'
name|'host'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'snapshot'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'fake_image_id'"
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'tracking'
op|'='
op|'{'
string|"'last_state'"
op|':'
name|'instance'
op|'.'
name|'vm_state'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|check_save
name|'def'
name|'check_save'
op|'('
name|'expected_task_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'instance'
op|'.'
name|'power_state'
op|')'
newline|'\n'
name|'if'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'task_states'
op|'.'
name|'SHELVING_OFFLOADING'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'task_states'
op|'.'
name|'SHELVING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SHELVING_IMAGE_UPLOADING'
op|']'
op|','
nl|'\n'
name|'expected_task_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'shelved_at'"
op|','
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'system_metadata'
op|'['
string|"'shelved_image_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'system_metadata'
op|'['
string|"'shelved_host'"
op|']'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'='
name|'instance'
op|'.'
name|'vm_state'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'vm_states'
op|'.'
name|'SHELVED'
name|'and'
nl|'\n'
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'=='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'SHELVED_OFFLOADED'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'task_states'
op|'.'
name|'SHELVING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'SHELVING_OFFLOADING'
op|']'
op|','
nl|'\n'
name|'expected_task_state'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'='
name|'instance'
op|'.'
name|'vm_state'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unexpected save!'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
string|"'shelve.end'"
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.start'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.end'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'instance'
op|','
string|"'save'"
op|')'
name|'as'
name|'mock_save'
op|':'
newline|'\n'
indent|'            '
name|'mock_save'
op|'.'
name|'side_effect'
op|'='
name|'check_save'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'shelve_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'image_id'
op|'='
name|'image_id'
op|','
name|'clean_shutdown'
op|'='
name|'clean_shutdown'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve
dedent|''
dedent|''
name|'def'
name|'test_shelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shelve_instance'
op|'('
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_forced_shutdown
dedent|''
name|'def'
name|'test_shelve_forced_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shelve_instance'
op|'('
op|'-'
number|'1'
op|','
name|'clean_shutdown'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_and_offload
dedent|''
name|'def'
name|'test_shelve_and_offload'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shelve_instance'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_shelve_offload
dedent|''
name|'def'
name|'_shelve_offload'
op|'('
name|'self'
op|','
name|'clean_shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
string|"'fake-mini'"
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
name|'params'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'SHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'cur_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'cur_time'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'power_off'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
name|'compute'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'cleanup_instance_network_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.start'"
op|')'
newline|'\n'
name|'if'
name|'clean_shutdown'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'shutdown_timeout'
op|','
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'SHUTDOWN_RETRY_INTERVAL'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'compute'
op|'.'
name|'network_api'
op|'.'
name|'cleanup_instance_network_on_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'instance'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'shelve_offload.end'"
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
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'instance'
op|','
string|"'save'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute'
op|'.'
name|'shelve_offload_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'clean_shutdown'
op|'='
name|'clean_shutdown'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'SHELVED_OFFLOADED'
op|','
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload
dedent|''
name|'def'
name|'test_shelve_offload'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shelve_offload'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload_forced_shutdown
dedent|''
name|'def'
name|'test_shelve_offload_forced_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_shelve_offload'
op|'('
name|'clean_shutdown'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve
dedent|''
name|'def'
name|'test_unshelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'UNSHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake_id'"
op|'}'
newline|'\n'
name|'node'
op|'='
name|'test_compute'
op|'.'
name|'NODENAME'
newline|'\n'
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'limits'"
op|':'
name|'limits'
op|'}'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|','
string|"'_prep_block_device'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'spawn'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
name|'rt'
op|','
string|"'instance_claim'"
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
name|'compute'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'setup_instance_network_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'deleted_image_id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_delete
name|'def'
name|'fake_delete'
op|'('
name|'self2'
op|','
name|'ctxt'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deleted_image_id'
op|'='
name|'image_id'
newline|'\n'
nl|'\n'
DECL|function|fake_claim
dedent|''
name|'def'
name|'fake_claim'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'host'
op|'='
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
newline|'\n'
name|'return'
name|'claims'
op|'.'
name|'Claim'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'rt'
op|','
name|'_fake_resources'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'tracking'
op|'='
op|'{'
nl|'\n'
string|"'last_state'"
op|':'
name|'instance'
op|'.'
name|'task_state'
op|','
nl|'\n'
string|"'spawned'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|check_save
name|'def'
name|'check_save'
op|'('
name|'expected_task_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'task_states'
op|'.'
name|'UNSHELVING'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'tracking'
op|'['
string|"'spawned'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'spawned'"
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'instance'
op|'.'
name|'task_state'
newline|'\n'
dedent|''
name|'elif'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'task_states'
op|'.'
name|'SPAWNING'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'instance'
op|'.'
name|'task_state'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unexpected save!'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'delete'"
op|','
name|'fake_delete'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.start'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_prep_block_device'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'do_check_attach'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'network_api'
op|'.'
name|'setup_instance_network_on_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|'='
string|"'fake_bdm'"
op|','
nl|'\n'
name|'flavor'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.end'"
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
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'rt'
op|','
string|"'instance_claim'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'fake_claim'
op|')'
op|','
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'instance'
op|','
string|"'save'"
op|')'
name|'as'
name|'mock_save'
op|':'
newline|'\n'
indent|'            '
name|'mock_save'
op|'.'
name|'side_effect'
op|'='
name|'check_save'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'unshelve_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|'='
name|'image'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'node'
op|'='
name|'node'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'['
string|"'id'"
op|']'
op|','
name|'self'
op|'.'
name|'deleted_image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'instance'
op|'.'
name|'power_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'key_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
name|'instance'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'instance'
op|'.'
name|'auto_disk_config'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve_volume_backed
dedent|''
name|'def'
name|'test_unshelve_volume_backed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'test_compute'
op|'.'
name|'NODENAME'
newline|'\n'
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'limits'"
op|':'
name|'limits'
op|'}'
newline|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'task_states'
op|'.'
name|'UNSHELVING'
newline|'\n'
name|'instance'
op|'.'
name|'save'
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
name|'compute'
op|','
string|"'_notify_about_instance_usage'"
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
name|'compute'
op|','
string|"'_prep_block_device'"
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'spawn'"
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
name|'compute'
op|','
string|"'_get_power_state'"
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
name|'rt'
op|','
string|"'instance_claim'"
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
name|'compute'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'setup_instance_network_on_host'"
op|')'
newline|'\n'
nl|'\n'
name|'tracking'
op|'='
op|'{'
string|"'last_state'"
op|':'
name|'instance'
op|'.'
name|'task_state'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|check_save
name|'def'
name|'check_save'
op|'('
name|'expected_task_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'task_states'
op|'.'
name|'UNSHELVING'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'task_states'
op|'.'
name|'SPAWNING'
op|','
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'='
name|'instance'
op|'.'
name|'task_state'
newline|'\n'
dedent|''
name|'elif'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'=='
name|'task_states'
op|'.'
name|'SPAWNING'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'instance'
op|'.'
name|'power_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'instance'
op|'.'
name|'vm_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'key_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'instance'
op|'.'
name|'auto_disk_config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
newline|'\n'
name|'tracking'
op|'['
string|"'last_state'"
op|']'
op|'='
name|'instance'
op|'.'
name|'task_state'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Unexpected save!'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.start'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_prep_block_device'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'do_check_attach'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fake_bdm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'network_api'
op|'.'
name|'setup_instance_network_on_host'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rt'
op|'.'
name|'instance_claim'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'limits'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'claims'
op|'.'
name|'Claim'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'self'
op|'.'
name|'rt'
op|','
nl|'\n'
name|'_fake_resources'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'None'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|']'
op|','
name|'admin_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|'='
string|"'fake_bdm'"
op|','
nl|'\n'
name|'flavor'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_get_power_state'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'unshelve.end'"
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
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'instance'
op|','
string|"'save'"
op|')'
name|'as'
name|'mock_save'
op|':'
newline|'\n'
indent|'            '
name|'mock_save'
op|'.'
name|'side_effect'
op|'='
name|'check_save'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'unshelve_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
name|'image'
op|'='
name|'None'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
name|'node'
op|'='
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_none_exist
dedent|''
dedent|''
name|'def'
name|'test_shelved_poll_none_exist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'timeutils'
op|','
string|"'is_older_than'"
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_not_timedout
dedent|''
name|'def'
name|'test_shelved_poll_not_timedout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'instance'
op|'.'
name|'system_metadata'
newline|'\n'
name|'shelved_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'shelved_time'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'-'
number|'1'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'shelved_time'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
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
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelved_poll_timedout
dedent|''
name|'def'
name|'test_shelved_poll_timedout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'instance'
op|'.'
name|'system_metadata'
newline|'\n'
name|'shelved_time'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'shelved_time'
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'advance_time_seconds'
op|'('
name|'CONF'
op|'.'
name|'shelved_offload_time'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'sys_meta'
op|'['
string|"'shelved_at'"
op|']'
op|'='
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'shelved_time'
op|')'
newline|'\n'
op|'('
name|'old'
op|','
name|'instance'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'SHELVED'
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_destroy
name|'def'
name|'fake_destroy'
op|'('
name|'inst'
op|','
name|'nw_info'
op|','
name|'bdm'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(alaski) There are too many differences between an instance'
nl|'\n'
comment|'# as returned by instance_update_and_get_original and'
nl|'\n'
comment|'# instance_get_all_by_filters so just compare the uuid.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
name|'inst'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'driver'
op|','
string|"'destroy'"
op|','
name|'fake_destroy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_poll_shelved_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShelveComputeAPITestCase
dedent|''
dedent|''
name|'class'
name|'ShelveComputeAPITestCase'
op|'('
name|'test_compute'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_shelve
indent|'    '
name|'def'
name|'test_shelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure instance can be shelved.'
nl|'\n'
indent|'        '
name|'fake_instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
nl|'\n'
op|'{'
string|"'display_name'"
op|':'
string|"'vm01'"
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_init
name|'def'
name|'fake_init'
op|'('
name|'self2'
op|')'
op|':'
newline|'\n'
comment|'# In original _FakeImageService.__init__(), some fake images are'
nl|'\n'
comment|'# created. To verify the snapshot name of this test only, here'
nl|'\n'
comment|'# sets a fake method.'
nl|'\n'
indent|'            '
name|'self2'
op|'.'
name|'images'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_create
dedent|''
name|'def'
name|'fake_create'
op|'('
name|'self2'
op|','
name|'ctxt'
op|','
name|'metadata'
op|','
name|'data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|'['
string|"'name'"
op|']'
op|','
string|"'vm01-shelved'"
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'id'"
op|']'
op|'='
string|"'8b24ed3f-ee57-43bc-bc2e-fb2e9482bc42'"
newline|'\n'
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'__init__'"
op|','
name|'fake_init'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'fake_image'
op|'.'
name|'_FakeImageService'
op|','
string|"'create'"
op|','
name|'fake_create'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'shelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|','
name|'task_states'
op|'.'
name|'SHELVING'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve
dedent|''
name|'def'
name|'test_unshelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure instance can be unshelved.'
nl|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_fake_instance_obj'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'instance'
op|'['
string|"'task_state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'shelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'='
name|'None'
newline|'\n'
name|'instance'
op|'.'
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'SHELVED'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'unshelve'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|','
name|'task_states'
op|'.'
name|'UNSHELVING'
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
