begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Citrix Systems, Inc.'
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
name|'collections'
newline|'\n'
nl|'\n'
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
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'volumeops'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeAttachTestCase
name|'class'
name|'VolumeAttachTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_detach_volume_call
indent|'    '
name|'def'
name|'test_detach_volume_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'registered_calls'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|regcall
name|'def'
name|'regcall'
op|'('
name|'label'
op|')'
op|':'
newline|'\n'
DECL|function|side_effect
indent|'            '
name|'def'
name|'side_effect'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'registered_calls'
op|'.'
name|'append'
op|'('
name|'label'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'side_effect'
newline|'\n'
nl|'\n'
dedent|''
name|'ops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
string|"'session'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'find_vbd_by_number'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'is_vm_shutdown'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'unplug_vbd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'destroy_vbd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'get_device_number'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'find_sr_from_vbd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'purge_sr'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
string|"'session'"
op|','
string|"'instance_1'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'vmref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'get_device_number'
op|'('
string|"'mountpoint'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'devnumber'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'find_vbd_by_number'
op|'('
nl|'\n'
string|"'session'"
op|','
string|"'vmref'"
op|','
string|"'devnumber'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'vbdref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'is_vm_shutdown'
op|'('
string|"'session'"
op|','
string|"'vmref'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'unplug_vbd'
op|'('
string|"'session'"
op|','
string|"'vbdref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'destroy_vbd'
op|'('
string|"'session'"
op|','
string|"'vbdref'"
op|')'
op|'.'
name|'WithSideEffects'
op|'('
nl|'\n'
name|'regcall'
op|'('
string|"'destroy_vbd'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'find_sr_from_vbd'
op|'('
nl|'\n'
string|"'session'"
op|','
string|"'vbdref'"
op|')'
op|'.'
name|'WithSideEffects'
op|'('
nl|'\n'
name|'regcall'
op|'('
string|"'find_sr_from_vbd'"
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'srref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'purge_sr'
op|'('
string|"'session'"
op|','
string|"'srref'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ops'
op|'.'
name|'detach_volume'
op|'('
nl|'\n'
name|'dict'
op|'('
name|'driver_volume_type'
op|'='
string|"'iscsi'"
op|','
name|'data'
op|'='
string|"'conn_data'"
op|')'
op|','
nl|'\n'
string|"'instance_1'"
op|','
string|"'mountpoint'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
op|'['
string|"'find_sr_from_vbd'"
op|','
string|"'destroy_vbd'"
op|']'
op|','
name|'registered_calls'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_call
dedent|''
name|'def'
name|'test_attach_volume_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
string|"'session'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ops'
op|','
string|"'_connect_volume'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'vm_ref_or_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'get_device_number'"
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
name|'dict'
op|'('
name|'driver_volume_type'
op|'='
string|"'iscsi'"
op|','
name|'data'
op|'='
string|"'conn_data'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'instance_1'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'vmref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'get_device_number'
op|'('
string|"'mountpoint'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'devnumber'"
op|')'
newline|'\n'
nl|'\n'
name|'ops'
op|'.'
name|'_connect_volume'
op|'('
nl|'\n'
name|'connection_info'
op|','
string|"'devnumber'"
op|','
string|"'instance_1'"
op|','
string|"'vmref'"
op|','
nl|'\n'
name|'hotplug'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
string|"'sruuid'"
op|','
string|"'vdiuuid'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'ops'
op|'.'
name|'attach_volume'
op|'('
nl|'\n'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_1'"
op|','
string|"'mountpoint'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_no_hotplug
dedent|''
name|'def'
name|'test_attach_volume_no_hotplug'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
string|"'session'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ops'
op|','
string|"'_connect_volume'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'vm_ref_or_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'get_device_number'"
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
name|'dict'
op|'('
name|'driver_volume_type'
op|'='
string|"'iscsi'"
op|','
name|'data'
op|'='
string|"'conn_data'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'instance_1'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'vmref'"
op|')'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'get_device_number'
op|'('
string|"'mountpoint'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'devnumber'"
op|')'
newline|'\n'
nl|'\n'
name|'ops'
op|'.'
name|'_connect_volume'
op|'('
nl|'\n'
name|'connection_info'
op|','
string|"'devnumber'"
op|','
string|"'instance_1'"
op|','
string|"'vmref'"
op|','
nl|'\n'
name|'hotplug'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
string|"'sruuid'"
op|','
string|"'vdiuuid'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'ops'
op|'.'
name|'attach_volume'
op|'('
nl|'\n'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_1'"
op|','
string|"'mountpoint'"
op|','
name|'hotplug'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_connect_volume
dedent|''
name|'def'
name|'_test_connect_volume'
op|'('
name|'self'
op|','
name|'hotplug'
op|','
name|'vm_running'
op|','
name|'plugged'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'stubs'
op|'.'
name|'FakeSessionForVolumeTests'
op|'('
string|"'fake_uri'"
op|')'
newline|'\n'
name|'ops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
name|'session'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'parse_sr_info'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'find_sr_by_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'introduce_sr'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'introduce_vdi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'create_vbd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'vm_utils'
op|','
string|"'is_vm_shutdown'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ops'
op|'.'
name|'_session'
op|','
string|"'call_xenapi'"
op|')'
newline|'\n'
nl|'\n'
name|'instance_name'
op|'='
string|"'instance_1'"
newline|'\n'
name|'sr_uuid'
op|'='
string|"'1'"
newline|'\n'
name|'sr_label'
op|'='
string|"'Disk-for:%s'"
op|'%'
name|'instance_name'
newline|'\n'
name|'sr_params'
op|'='
string|"''"
newline|'\n'
name|'sr_ref'
op|'='
string|"'sr_ref'"
newline|'\n'
name|'vdi_uuid'
op|'='
string|"'2'"
newline|'\n'
name|'vdi_ref'
op|'='
string|"'vdi_ref'"
newline|'\n'
name|'vbd_ref'
op|'='
string|"'vbd_ref'"
newline|'\n'
name|'connection_data'
op|'='
op|'{'
string|"'vdi_uuid'"
op|':'
name|'vdi_uuid'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
name|'connection_data'
op|','
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|'}'
newline|'\n'
name|'vm_ref'
op|'='
string|"'vm_ref'"
newline|'\n'
name|'dev_number'
op|'='
number|'1'
newline|'\n'
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'parse_sr_info'
op|'('
nl|'\n'
name|'connection_data'
op|','
name|'sr_label'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'tuple'
op|'('
op|'['
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|']'
op|')'
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'session'
op|','
name|'sr_uuid'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'None'
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'introduce_sr'
op|'('
nl|'\n'
name|'session'
op|','
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
nl|'\n'
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|'='
name|'vdi_uuid'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'create_vbd'
op|'('
nl|'\n'
name|'session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
name|'dev_number'
op|','
nl|'\n'
name|'bootable'
op|'='
name|'False'
op|','
name|'osvol'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'vm_utils'
op|'.'
name|'is_vm_shutdown'
op|'('
name|'session'
op|','
nl|'\n'
name|'vm_ref'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'not'
name|'vm_running'
op|')'
newline|'\n'
name|'if'
name|'plugged'
op|':'
newline|'\n'
indent|'            '
name|'ops'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.plug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'ops'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_uuid"'
op|','
nl|'\n'
name|'vdi_ref'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'ops'
op|'.'
name|'_connect_volume'
op|'('
name|'connection_info'
op|','
name|'dev_number'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'vm_ref'
op|','
name|'hotplug'
op|'='
name|'hotplug'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
name|'sr_uuid'
op|','
name|'vdi_uuid'
op|')'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_connect_volume_no_hotplug_vm_running
dedent|''
name|'def'
name|'test_connect_volume_no_hotplug_vm_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_connect_volume'
op|'('
name|'hotplug'
op|'='
name|'False'
op|','
name|'vm_running'
op|'='
name|'True'
op|','
nl|'\n'
name|'plugged'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_connect_volume_no_hotplug_vm_not_running
dedent|''
name|'def'
name|'test_connect_volume_no_hotplug_vm_not_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_connect_volume'
op|'('
name|'hotplug'
op|'='
name|'False'
op|','
name|'vm_running'
op|'='
name|'False'
op|','
nl|'\n'
name|'plugged'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_connect_volume_hotplug_vm_stopped
dedent|''
name|'def'
name|'test_connect_volume_hotplug_vm_stopped'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_connect_volume'
op|'('
name|'hotplug'
op|'='
name|'True'
op|','
name|'vm_running'
op|'='
name|'False'
op|','
nl|'\n'
name|'plugged'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_connect_volume_hotplug_vm_running
dedent|''
name|'def'
name|'test_connect_volume_hotplug_vm_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_connect_volume'
op|'('
name|'hotplug'
op|'='
name|'True'
op|','
name|'vm_running'
op|'='
name|'True'
op|','
nl|'\n'
name|'plugged'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_connect_volume
dedent|''
name|'def'
name|'test_connect_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'stubs'
op|'.'
name|'FakeSessionForVolumeTests'
op|'('
string|"'fake_uri'"
op|')'
newline|'\n'
name|'ops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
name|'session'
op|')'
newline|'\n'
name|'sr_uuid'
op|'='
string|"'1'"
newline|'\n'
name|'sr_label'
op|'='
string|"'Disk-for:None'"
newline|'\n'
name|'sr_params'
op|'='
string|"''"
newline|'\n'
name|'sr_ref'
op|'='
string|"'sr_ref'"
newline|'\n'
name|'vdi_uuid'
op|'='
string|"'2'"
newline|'\n'
name|'vdi_ref'
op|'='
string|"'vdi_ref'"
newline|'\n'
name|'vbd_ref'
op|'='
string|"'vbd_ref'"
newline|'\n'
name|'connection_data'
op|'='
op|'{'
string|"'vdi_uuid'"
op|':'
name|'vdi_uuid'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
name|'connection_data'
op|','
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|'}'
newline|'\n'
nl|'\n'
name|'called'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'bool'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_call_xenapi
name|'def'
name|'fake_call_xenapi'
op|'('
name|'self'
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
name|'called'
op|'['
name|'method'
op|']'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'ops'
op|'.'
name|'_session'
op|','
string|"'call_xenapi'"
op|','
name|'fake_call_xenapi'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'parse_sr_info'"
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'parse_sr_info'
op|'('
nl|'\n'
name|'connection_data'
op|','
name|'sr_label'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'tuple'
op|'('
op|'['
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'find_sr_by_uuid'"
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'session'
op|','
name|'sr_uuid'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'introduce_sr'"
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'introduce_sr'
op|'('
nl|'\n'
name|'session'
op|','
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'volumeops'
op|'.'
name|'volume_utils'
op|','
string|"'introduce_vdi'"
op|')'
newline|'\n'
name|'volumeops'
op|'.'
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
nl|'\n'
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|'='
name|'vdi_uuid'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ops'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'False'
op|','
name|'called'
op|'['
string|"'VBD.plug'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
