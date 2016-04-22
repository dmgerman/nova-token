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
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
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
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'test_volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'host'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'net'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
name|'class'
name|'LibvirtNetVolumeDriverTestCase'
op|'('
nl|'\n'
DECL|class|LibvirtNetVolumeDriverTestCase
name|'test_volume'
op|'.'
name|'LibvirtISCSIVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests the libvirt network volume driver."""'
newline|'\n'
nl|'\n'
DECL|member|_assertNetworkAndProtocolEquals
name|'def'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'self'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'network'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'rbd'"
op|','
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
op|')'
newline|'\n'
name|'rbd_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
string|"'rbd'"
op|','
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rbd_name'
op|','
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assertISCSINetworkAndProtocolEquals
dedent|''
name|'def'
name|'_assertISCSINetworkAndProtocolEquals'
op|'('
name|'self'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'network'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'iscsi'"
op|','
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
op|')'
newline|'\n'
name|'iscsi_name'
op|'='
string|"'%s/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'iqn'
op|','
name|'self'
op|'.'
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'iscsi_name'
op|','
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'sheepdog_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'network'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'sheepdog'"
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'name'
op|','
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
name|'libvirt'
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
name|'libvirt'
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
name|'libvirt'
op|'.'
name|'rbd_secret_uuid'
op|','
nl|'\n'
string|"'qos_specs'"
op|':'
op|'{'
nl|'\n'
string|"'total_bytes_sec'"
op|':'
string|"'1048576'"
op|','
nl|'\n'
string|"'read_iops_sec'"
op|':'
string|"'500'"
op|','
nl|'\n'
op|'}'
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source/auth'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1048576'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/total_bytes_sec'"
op|')'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'500'"
op|','
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./iotune/read_iops_sec'"
op|')'
op|'.'
name|'text'
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
nl|'\n'
DECL|member|test_libvirt_rbd_driver_hosts
dedent|''
name|'def'
name|'test_libvirt_rbd_driver_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
string|"'example.com'"
op|','
string|"'1.2.3.4'"
op|','
string|"'::1'"
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
name|'None'
op|','
string|"'6790'"
op|','
string|"'6791'"
op|']'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'hosts'"
op|']'
op|'='
name|'hosts'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'ports'"
op|']'
op|'='
name|'ports'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./source/auth'"
op|')'
op|')'
newline|'\n'
name|'found_hosts'
op|'='
name|'tree'
op|'.'
name|'findall'
op|'('
string|"'./source/host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'hosts'
op|','
op|'['
name|'host'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
name|'for'
name|'host'
name|'in'
name|'found_hosts'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ports'
op|','
op|'['
name|'host'
op|'.'
name|'get'
op|'('
string|"'port'"
op|')'
name|'for'
name|'host'
name|'in'
name|'found_hosts'
op|']'
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
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
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'user'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secret_type'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
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
name|'self'
op|'.'
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
name|'self'
op|'.'
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
op|','
nl|'\n'
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flags_user'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secret_type'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flags_uuid'
op|','
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
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
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'tree'
op|'.'
name|'find'
op|'('
string|"'./auth'"
op|')'
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
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'rbd_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|')'
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
name|'self'
op|'.'
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
name|'self'
op|'.'
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
op|','
nl|'\n'
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertNetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flags_user'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secret_type'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flags_uuid'
op|','
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
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host'
op|'.'
name|'Host'
op|','
string|"'find_secret'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host'
op|'.'
name|'Host'
op|','
string|"'create_secret'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'host'
op|'.'
name|'Host'
op|','
string|"'delete_secret'"
op|')'
newline|'\n'
DECL|member|test_libvirt_iscsi_net_driver
name|'def'
name|'test_libvirt_iscsi_net_driver'
op|'('
name|'self'
op|','
name|'mock_delete'
op|','
name|'mock_create'
op|','
nl|'\n'
name|'mock_find'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_find'
op|'.'
name|'return_value'
op|'='
name|'test_volume'
op|'.'
name|'FakeSecret'
op|'('
op|')'
newline|'\n'
name|'mock_create'
op|'.'
name|'return_value'
op|'='
name|'test_volume'
op|'.'
name|'FakeSecret'
op|'('
op|')'
newline|'\n'
name|'libvirt_driver'
op|'='
name|'net'
op|'.'
name|'LibvirtNetVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'connection_info'
op|'='
name|'self'
op|'.'
name|'iscsi_connection'
op|'('
name|'self'
op|'.'
name|'vol'
op|','
name|'self'
op|'.'
name|'location'
op|','
nl|'\n'
name|'self'
op|'.'
name|'iqn'
op|','
name|'auth'
op|'='
name|'True'
op|')'
newline|'\n'
name|'secret_type'
op|'='
string|"'iscsi'"
newline|'\n'
name|'flags_user'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'auth_username'"
op|']'
newline|'\n'
name|'conf'
op|'='
name|'libvirt_driver'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_assertISCSINetworkAndProtocolEquals'
op|'('
name|'tree'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flags_user'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secret_type'
op|','
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_volume'
op|'.'
name|'SECRET_UUID'
op|','
nl|'\n'
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
op|')'
newline|'\n'
name|'libvirt_driver'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
string|"'vde'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
