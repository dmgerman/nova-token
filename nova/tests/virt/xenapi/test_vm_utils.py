begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 OpenStack Foundation'
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
nl|'\n'
nl|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'fixtures'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|function|contextified
name|'def'
name|'contextified'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'yield'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_noop
dedent|''
name|'def'
name|'_fake_noop'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GenerateConfigDriveTestCase
dedent|''
name|'class'
name|'GenerateConfigDriveTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_no_admin_pass
indent|'    '
name|'def'
name|'test_no_admin_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# This is here to avoid masking errors, it shouldn't be used normally"
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.xenapi.vm_utils.destroy_vdi'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Mocks'
nl|'\n'
name|'instance'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'safe_find_sr'"
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'safe_find_sr'
op|'('
string|"'session'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'sr_ref'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'create_vdi'"
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'create_vdi'
op|'('
string|"'session'"
op|','
string|"'sr_ref'"
op|','
name|'instance'
op|','
string|"'config-2'"
op|','
nl|'\n'
string|"'configdrive'"
op|','
nl|'\n'
number|'64'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'vdi_ref'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'vdi_attached_here'"
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'vdi_attached_here'
op|'('
nl|'\n'
string|"'session'"
op|','
string|"'vdi_ref'"
op|','
name|'read_only'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'contextified'
op|'('
string|"'mounted_dev'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeInstanceMetadata
name|'class'
name|'FakeInstanceMetadata'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'content'
op|'='
name|'None'
op|','
name|'extra_md'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|metadata_for_config_drive
dedent|''
name|'def'
name|'metadata_for_config_drive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.api.metadata.base.InstanceMetadata'"
op|','
nl|'\n'
name|'FakeInstanceMetadata'
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
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'genisoimage'"
op|','
string|"'-o'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'-ldots'"
op|','
nl|'\n'
string|"'-allow-lowercase'"
op|','
string|"'-allow-multidot'"
op|','
string|"'-l'"
op|','
nl|'\n'
string|"'-publisher'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'-quiet'"
op|','
nl|'\n'
string|"'-J'"
op|','
string|"'-r'"
op|','
string|"'-V'"
op|','
string|"'config-2'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'1'
op|','
name|'run_as_root'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
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
name|'vm_utils'
op|','
string|"'create_vbd'"
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'create_vbd'
op|'('
string|"'session'"
op|','
string|"'vm_ref'"
op|','
string|"'vdi_ref'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'bootable'
op|'='
name|'False'
op|','
name|'read_only'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
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
comment|"# And the actual call we're testing"
nl|'\n'
name|'vm_utils'
op|'.'
name|'generate_configdrive'
op|'('
string|"'session'"
op|','
name|'instance'
op|','
string|"'vm_ref'"
op|','
nl|'\n'
string|"'userdevice'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIGetUUID
dedent|''
dedent|''
name|'class'
name|'XenAPIGetUUID'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_this_vm_uuid_new_kernel
indent|'    '
name|'def'
name|'test_get_this_vm_uuid_new_kernel'
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
name|'vm_utils'
op|','
string|"'_get_sys_hypervisor_uuid'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'_get_sys_hypervisor_uuid'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'2f46f0f5-f14c-ef1b-1fac-9eeca0888a3f'"
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
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'2f46f0f5-f14c-ef1b-1fac-9eeca0888a3f'"
op|','
nl|'\n'
name|'vm_utils'
op|'.'
name|'get_this_vm_uuid'
op|'('
op|')'
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
nl|'\n'
DECL|member|test_get_this_vm_uuid_old_kernel_reboot
dedent|''
name|'def'
name|'test_get_this_vm_uuid_old_kernel_reboot'
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
name|'vm_utils'
op|','
string|"'_get_sys_hypervisor_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'_get_sys_hypervisor_uuid'
op|'('
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'IOError'
op|'('
number|'13'
op|','
string|"'Permission denied'"
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'xenstore-read'"
op|','
string|"'domid'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
string|"'27'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'xenstore-read'"
op|','
string|"'/local/domain/27/vm'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
string|"'/vm/2f46f0f5-f14c-ef1b-1fac-9eeca0888a3f'"
op|','
string|"''"
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
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'2f46f0f5-f14c-ef1b-1fac-9eeca0888a3f'"
op|','
nl|'\n'
name|'vm_utils'
op|'.'
name|'get_this_vm_uuid'
op|'('
op|')'
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
dedent|''
dedent|''
endmarker|''
end_unit
