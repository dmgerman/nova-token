begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'import'
name|'contextlib'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
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
name|'exception'
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
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
name|'as'
name|'vmwareapi_fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vm_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'volumeops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareVolumeOpsTestCase
name|'class'
name|'VMwareVolumeOpsTestCase'
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
nl|'\n'
indent|'        '
name|'super'
op|'('
name|'VMwareVolumeOpsTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'vmwareapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'set_stubs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'driver'
op|'.'
name|'VMwareAPISession'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
op|'.'
name|'VMwareVolumeOps'
op|'('
name|'self'
op|'.'
name|'_session'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'fake_name'"
op|','
string|"'uuid'"
op|':'
string|"'fake_uuid'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_test_detach_disk_from_vm
dedent|''
name|'def'
name|'_test_detach_disk_from_vm'
op|'('
name|'self'
op|','
name|'destroy_disk'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'module'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vmdk_detach_config_spec'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'spec'"
op|')'
newline|'\n'
name|'virtual_device_config'
op|'='
name|'vmdk_detach_config_spec'
op|'.'
name|'deviceChange'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'remove'"
op|','
name|'virtual_device_config'
op|'.'
name|'operation'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|','
nl|'\n'
name|'virtual_device_config'
op|'.'
name|'obj_name'
op|')'
newline|'\n'
name|'if'
name|'destroy_disk'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'destroy'"
op|','
nl|'\n'
name|'virtual_device_config'
op|'.'
name|'fileOperation'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'hasattr'
op|'('
name|'virtual_device_config'
op|','
nl|'\n'
string|"'fileOperation'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'fake_configure_task'"
newline|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'_wait_for_task'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|"'_call_method'"
op|','
nl|'\n'
name|'fake_call_method'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_wait_for_task'
op|','
name|'_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fake_device'
op|'='
name|'vmwareapi_fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'fake_device'
op|'.'
name|'backing'
op|'='
name|'vmwareapi_fake'
op|'.'
name|'DataObject'
op|'('
op|')'
newline|'\n'
name|'fake_device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
op|'='
string|"'fake_path'"
newline|'\n'
name|'fake_device'
op|'.'
name|'key'
op|'='
string|"'fake_key'"
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_disk_from_vm'
op|'('
string|"'fake_vm_ref'"
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'fake_device'
op|','
name|'destroy_disk'
op|')'
newline|'\n'
name|'_wait_for_task'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'fake_configure_task'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_with_destroy_disk_from_vm
dedent|''
dedent|''
name|'def'
name|'test_detach_with_destroy_disk_from_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_detach_disk_from_vm'
op|'('
name|'destroy_disk'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_without_destroy_disk_from_vm
dedent|''
name|'def'
name|'test_detach_without_destroy_disk_from_vm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_detach_disk_from_vm'
op|'('
name|'destroy_disk'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_fake_call_get_dynamic_property
dedent|''
name|'def'
name|'_fake_call_get_dynamic_property'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_method
indent|'        '
name|'def'
name|'fake_call_method'
op|'('
name|'vim'
op|','
name|'method'
op|','
name|'vm_ref'
op|','
name|'type'
op|','
name|'prop'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'expected_prop'
op|'='
string|'\'config.extraConfig["volume-%s"]\''
op|'%'
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'VirtualMachine'"
op|','
name|'type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_prop'
op|','
name|'prop'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'fake_call_method'
newline|'\n'
nl|'\n'
DECL|member|test_get_volume_uuid
dedent|''
name|'def'
name|'test_get_volume_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'1234'"
newline|'\n'
name|'opt_val'
op|'='
name|'vmwareapi_fake'
op|'.'
name|'OptionValue'
op|'('
string|"'volume-%s'"
op|'%'
name|'uuid'
op|','
string|"'volume-val'"
op|')'
newline|'\n'
name|'fake_call'
op|'='
name|'self'
op|'.'
name|'_fake_call_get_dynamic_property'
op|'('
name|'uuid'
op|','
name|'opt_val'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"_call_method"'
op|','
name|'fake_call'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_get_volume_uuid'
op|'('
name|'vm_ref'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'volume-val'"
op|','
name|'val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_volume_uuid_not_found
dedent|''
dedent|''
name|'def'
name|'test_get_volume_uuid_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'1234'"
newline|'\n'
name|'fake_call'
op|'='
name|'self'
op|'.'
name|'_fake_call_get_dynamic_property'
op|'('
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
string|'"_call_method"'
op|','
name|'fake_call'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_get_volume_uuid'
op|'('
name|'vm_ref'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_vmdk_invalid
dedent|''
dedent|''
name|'def'
name|'test_attach_volume_vmdk_invalid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'connection_info'
op|'='
op|'{'
string|"'driver_volume_type'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'volume-fake-id'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
string|"'volume'"
op|':'
string|"'vm-10'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'volume-fake-id'"
op|'}'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'vmdk_info'
op|'='
name|'vm_util'
op|'.'
name|'VmdkInfo'
op|'('
string|"'fake-path'"
op|','
string|"'ide'"
op|','
string|"'preallocated'"
op|','
number|'1024'
op|')'
newline|'\n'
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_vm_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_volumeops'
op|','
string|"'_get_volume_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_vmdk_info'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'vmdk_info'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'get_vm_ref'
op|','
name|'get_volume_ref'
op|','
name|'get_vmdk_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_attach_volume_vmdk'
op|','
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'get_vm_ref'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'get_volume_ref'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'volume'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'get_vmdk_info'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_volume_vmdk_invalid
dedent|''
dedent|''
name|'def'
name|'test_detach_volume_vmdk_invalid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'connection_info'
op|'='
op|'{'
string|"'driver_volume_type'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'volume-fake-id'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
string|"'volume'"
op|':'
string|"'vm-10'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'volume-fake-id'"
op|'}'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'name'
op|'='
string|"'fake-name'"
op|','
name|'vm_state'
op|'='
name|'vm_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
name|'vmdk_info'
op|'='
name|'vm_util'
op|'.'
name|'VmdkInfo'
op|'('
string|"'fake-path'"
op|','
string|"'ide'"
op|','
string|"'preallocated'"
op|','
number|'1024'
op|')'
newline|'\n'
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_vm_ref'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_volumeops'
op|','
string|"'_get_volume_ref'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_volumeops'
op|','
nl|'\n'
string|"'_get_vmdk_backed_disk_device'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vm_util'
op|','
string|"'get_vmdk_info'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'vmdk_info'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'get_vm_ref'
op|','
name|'get_volume_ref'
op|','
name|'get_vmdk_backed_disk_device'
op|','
nl|'\n'
name|'get_vmdk_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_detach_volume_vmdk'
op|','
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'get_vm_ref'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'get_volume_ref'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'volume'"
op|']'
op|')'
newline|'\n'
name|'get_vmdk_backed_disk_device'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
op|','
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'get_vmdk_info'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
