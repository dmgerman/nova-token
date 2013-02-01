begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
nl|'\n'
comment|'#    Copyright 2012 University Of Minho'
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
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
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVolumeTestCase
name|'class'
name|'LibvirtVolumeTestCase'
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
name|'LibvirtVolumeTestCase'
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
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
DECL|class|FakeLibvirtDriver
name|'class'
name|'FakeLibvirtDriver'
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
name|'hyperv'
op|'='
string|'"QEMU"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'hyperv'
op|'='
name|'hyperv'
newline|'\n'
nl|'\n'
DECL|member|get_hypervisor_type
dedent|''
name|'def'
name|'get_hypervisor_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'hyperv'
newline|'\n'
nl|'\n'
DECL|member|get_all_block_devices
dedent|''
name|'def'
name|'get_all_block_devices'
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
name|'fake_conn'
op|'='
name|'FakeLibvirtDriver'
op|'('
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connr'
op|'='
op|'{'
nl|'\n'
string|"'ip'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'initiator'"
op|':'
string|"'fake_initiator'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_volume_driver_serial
dedent|''
name|'def'
name|'test_libvirt_volume_driver_serial'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'device_path'"
op|':'
string|"'/foo'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'serial'"
op|':'
string|"'fake_serial'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'block'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./serial'"
op|')'
op|'.'
name|'text'
op|','
string|"'fake_serial'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|iscsi_connection
dedent|''
name|'def'
name|'iscsi_connection'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'location'
op|','
name|'iqn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'iscsi'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'target_portal'"
op|':'
name|'location'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'iqn'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_iscsi_driver
dedent|''
name|'def'
name|'test_libvirt_iscsi_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish) exists is to make driver assume connecting worked'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'x'
op|':'
name|'True'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtISCSIVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'location'
op|'='
string|"'10.0.2.15:3260'"
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'iqn'
op|'='
string|"'iqn.2010-10.org.openstack:%s'"
op|'%'
name|'name'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'iscsi_connection'
op|'('
name|'vol'
op|','
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'dev_str'
op|'='
string|"'/dev/disk/by-path/ip-%s-iscsi-%s-lun-1'"
op|'%'
op|'('
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'block'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
op|','
name|'dev_str'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--login'"
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--op'"
op|','
string|"'update'"
op|','
nl|'\n'
string|"'-n'"
op|','
string|"'node.startup'"
op|','
string|"'-v'"
op|','
string|"'automatic'"
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--op'"
op|','
string|"'update'"
op|','
nl|'\n'
string|"'-n'"
op|','
string|"'node.startup'"
op|','
string|"'-v'"
op|','
string|"'manual'"
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--logout'"
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--op'"
op|','
string|"'delete'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'executes'
op|','
name|'expected_commands'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_iscsi_driver_still_in_use
dedent|''
name|'def'
name|'test_libvirt_iscsi_driver_still_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish) exists is to make driver assume connecting worked'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'x'
op|':'
name|'True'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtISCSIVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'location'
op|'='
string|"'10.0.2.15:3260'"
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'iqn'
op|'='
string|"'iqn.2010-10.org.openstack:%s'"
op|'%'
name|'name'
newline|'\n'
name|'devs'
op|'='
op|'['
string|"'/dev/disk/by-path/ip-%s-iscsi-%s-lun-1'"
op|'%'
op|'('
name|'location'
op|','
name|'iqn'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|','
string|"'get_all_block_devices'"
op|','
name|'lambda'
op|':'
name|'devs'
op|')'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'iscsi_connection'
op|'('
name|'vol'
op|','
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'dev_str'
op|'='
string|"'/dev/disk/by-path/ip-%s-iscsi-%s-lun-1'"
op|'%'
op|'('
name|'location'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'block'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
op|','
name|'dev_str'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--login'"
op|')'
op|','
nl|'\n'
op|'('
string|"'iscsiadm'"
op|','
string|"'-m'"
op|','
string|"'node'"
op|','
string|"'-T'"
op|','
name|'iqn'
op|','
nl|'\n'
string|"'-p'"
op|','
name|'location'
op|','
string|"'--op'"
op|','
string|"'update'"
op|','
nl|'\n'
string|"'-n'"
op|','
string|"'node.startup'"
op|','
string|"'-v'"
op|','
string|"'automatic'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'executes'
op|','
name|'expected_commands'
op|')'
newline|'\n'
nl|'\n'
DECL|member|sheepdog_connection
dedent|''
name|'def'
name|'sheepdog_connection'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'sheepdog'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'volume'
op|'['
string|"'name'"
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_sheepdog_driver
dedent|''
name|'def'
name|'test_libvirt_sheepdog_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'sheepdog_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'sheepdog'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rbd_connection
dedent|''
name|'def'
name|'rbd_connection'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'rbd'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|','
nl|'\n'
string|"'auth_enabled'"
op|':'
name|'CONF'
op|'.'
name|'rbd_secret_uuid'
name|'is'
name|'not'
name|'None'
op|','
nl|'\n'
string|"'auth_username'"
op|':'
name|'CONF'
op|'.'
name|'rbd_user'
op|','
nl|'\n'
string|"'secret_type'"
op|':'
string|"'ceph'"
op|','
nl|'\n'
string|"'secret_uuid'"
op|':'
name|'CONF'
op|'.'
name|'rbd_secret_uuid'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_rbd_driver
dedent|''
name|'def'
name|'test_libvirt_rbd_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'rbd'"
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'rbd_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source/auth'"
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_rbd_driver_auth_enabled
dedent|''
name|'def'
name|'test_libvirt_rbd_driver_auth_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'875a8070-d0b9-4949-8b31-104d125c9a64'"
newline|'\n'
name|'user'
op|'='
string|"'foo'"
newline|'\n'
name|'secret_type'
op|'='
string|"'ceph'"
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_enabled'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
op|'='
name|'user'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_type'"
op|']'
op|'='
name|'secret_type'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_uuid'"
op|']'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'rbd'"
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'rbd_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth'"
op|')'
op|'.'
name|'get'
op|'('
string|"'username'"
op|')'
op|','
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
name|'secret_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|','
name|'uuid'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_rbd_driver_auth_enabled_flags_override
dedent|''
name|'def'
name|'test_libvirt_rbd_driver_auth_enabled_flags_override'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'875a8070-d0b9-4949-8b31-104d125c9a64'"
newline|'\n'
name|'user'
op|'='
string|"'foo'"
newline|'\n'
name|'secret_type'
op|'='
string|"'ceph'"
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_enabled'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
op|'='
name|'user'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_type'"
op|']'
op|'='
name|'secret_type'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_uuid'"
op|']'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
name|'flags_uuid'
op|'='
string|"'37152720-1785-11e2-a740-af0c1d8b8e4b'"
newline|'\n'
name|'flags_user'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'rbd_user'
op|'='
name|'flags_user'
op|','
nl|'\n'
name|'rbd_secret_uuid'
op|'='
name|'flags_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'rbd'"
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'rbd_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth'"
op|')'
op|'.'
name|'get'
op|'('
string|"'username'"
op|')'
op|','
name|'flags_user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
name|'secret_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|','
name|'flags_uuid'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_rbd_driver_auth_disabled
dedent|''
name|'def'
name|'test_libvirt_rbd_driver_auth_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'875a8070-d0b9-4949-8b31-104d125c9a64'"
newline|'\n'
name|'user'
op|'='
string|"'foo'"
newline|'\n'
name|'secret_type'
op|'='
string|"'ceph'"
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_enabled'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
op|'='
name|'user'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_type'"
op|']'
op|'='
name|'secret_type'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_uuid'"
op|']'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'rbd'"
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'rbd_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth'"
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_rbd_driver_auth_disabled_flags_override
dedent|''
name|'def'
name|'test_libvirt_rbd_driver_auth_disabled_flags_override'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'name'
op|'='
string|"'volume-00000001'"
newline|'\n'
name|'vol'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'vol'
op|')'
newline|'\n'
name|'uuid'
op|'='
string|"'875a8070-d0b9-4949-8b31-104d125c9a64'"
newline|'\n'
name|'user'
op|'='
string|"'foo'"
newline|'\n'
name|'secret_type'
op|'='
string|"'ceph'"
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_enabled'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
op|'='
name|'user'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_type'"
op|']'
op|'='
name|'secret_type'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'secret_uuid'"
op|']'
op|'='
name|'uuid'
newline|'\n'
nl|'\n'
comment|'# NOTE: Supplying the rbd_secret_uuid will enable authentication'
nl|'\n'
comment|'# locally in nova-compute even if not enabled in nova-volume/cinder'
nl|'\n'
name|'flags_uuid'
op|'='
string|"'37152720-1785-11e2-a740-af0c1d8b8e4b'"
newline|'\n'
name|'flags_user'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'rbd_user'
op|'='
name|'flags_user'
op|','
nl|'\n'
name|'rbd_secret_uuid'
op|'='
name|'flags_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'network'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'protocol'"
op|')'
op|','
string|"'rbd'"
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
name|'rbd_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth'"
op|')'
op|'.'
name|'get'
op|'('
string|"'username'"
op|')'
op|','
name|'flags_user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
name|'secret_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth/secret'"
op|')'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
op|','
name|'flags_uuid'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_nfs_driver
dedent|''
name|'def'
name|'test_libvirt_nfs_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish) exists is to make driver assume connecting worked'
nl|'\n'
indent|'        '
name|'mnt_base'
op|'='
string|"'/mnt'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'nfs_mount_point_base'
op|'='
name|'mnt_base'
op|')'
newline|'\n'
nl|'\n'
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'export_string'
op|'='
string|"'192.168.1.1:/nfs/share1'"
newline|'\n'
name|'name'
op|'='
string|"'volume-00001'"
newline|'\n'
name|'export_mnt_base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mnt_base'
op|','
nl|'\n'
name|'libvirt_driver'
op|'.'
name|'get_hash_str'
op|'('
name|'export_string'
op|')'
op|')'
newline|'\n'
name|'file_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export_mnt_base'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'='
op|'{'
string|"'data'"
op|':'
op|'{'
string|"'export'"
op|':'
name|'export_string'
op|','
string|"'name'"
op|':'
name|'name'
op|'}'
op|'}'
newline|'\n'
name|'mount_device'
op|'='
string|'"vde"'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'file'"
op|')'
op|','
name|'file_path'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
nl|'\n'
op|'('
string|"'stat'"
op|','
name|'export_mnt_base'
op|')'
op|','
nl|'\n'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
string|"'nfs'"
op|','
name|'export_string'
op|','
name|'export_mnt_base'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'executes'
op|','
name|'expected_commands'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aoe_connection
dedent|''
name|'def'
name|'aoe_connection'
op|'('
name|'self'
op|','
name|'shelf'
op|','
name|'lun'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'aoe'"
op|','
nl|'\n'
string|"'data'"
op|':'
op|'{'
nl|'\n'
string|"'target_shelf'"
op|':'
name|'shelf'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
name|'lun'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_aoe_driver
dedent|''
name|'def'
name|'test_libvirt_aoe_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jbr_) exists is to make driver assume connecting worked'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'x'
op|':'
name|'True'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'='
name|'volume'
op|'.'
name|'LibvirtAOEVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'shelf'
op|'='
string|"'100'"
newline|'\n'
name|'lun'
op|'='
string|"'1'"
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'aoe_connection'
op|'('
name|'shelf'
op|','
name|'lun'
op|')'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
nl|'\n'
string|'"bus"'
op|':'
string|'"virtio"'
op|','
nl|'\n'
string|'"dev"'
op|':'
string|'"vde"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"disk"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
name|'disk_info'
op|')'
newline|'\n'
name|'tree'
op|'='
name|'conf'
op|'.'
name|'format_dom'
op|'('
op|')'
newline|'\n'
name|'aoedevpath'
op|'='
string|"'/dev/etherd/e%s.%s'"
op|'%'
op|'('
name|'shelf'
op|','
name|'lun'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|','
string|"'block'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source'"
op|')'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
op|','
name|'aoedevpath'
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|'"vde"'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
