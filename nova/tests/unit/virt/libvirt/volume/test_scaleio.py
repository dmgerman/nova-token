begin_unit
comment|'# Copyright (c) 2015 EMC Corporation'
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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'os_brick'
op|'.'
name|'initiator'
name|'import'
name|'connector'
newline|'\n'
nl|'\n'
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
op|'.'
name|'volume'
name|'import'
name|'scaleio'
newline|'\n'
nl|'\n'
nl|'\n'
name|'class'
name|'LibvirtScaleIOVolumeDriverTestCase'
op|'('
nl|'\n'
DECL|class|LibvirtScaleIOVolumeDriverTestCase
name|'test_volume'
op|'.'
name|'LibvirtVolumeBaseTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_scaleio_driver
indent|'    '
name|'def'
name|'test_libvirt_scaleio_driver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_driver'
op|'='
name|'scaleio'
op|'.'
name|'LibvirtScaleIOVolumeDriver'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'libvirt_driver'
op|'.'
name|'connector'
op|','
nl|'\n'
name|'connector'
op|'.'
name|'ScaleIOConnector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_scaleio_driver_connect
dedent|''
name|'def'
name|'test_libvirt_scaleio_driver_connect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|brick_conn_vol
indent|'        '
name|'def'
name|'brick_conn_vol'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'path'"
op|':'
string|"'/dev/vol01'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'sio'
op|'='
name|'scaleio'
op|'.'
name|'LibvirtScaleIOVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'sio'
op|'.'
name|'connector'
op|'.'
name|'connect_volume'
op|'='
name|'brick_conn_vol'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
string|"'path'"
op|':'
string|"'/dev/vol01'"
op|','
string|"'name'"
op|':'
string|"'vol01'"
op|'}'
newline|'\n'
name|'conn'
op|'='
op|'{'
string|"'data'"
op|':'
name|'disk_info'
op|'}'
newline|'\n'
name|'sio'
op|'.'
name|'connect_volume'
op|'('
name|'conn'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/vol01'"
op|','
nl|'\n'
name|'conn'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_scaleio_driver_get_config
dedent|''
name|'def'
name|'test_libvirt_scaleio_driver_get_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sio'
op|'='
name|'scaleio'
op|'.'
name|'LibvirtScaleIOVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
string|"'path'"
op|':'
string|"'/dev/vol01'"
op|','
string|"'name'"
op|':'
string|"'vol01'"
op|','
string|"'type'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'dev'"
op|':'
string|"'vda1'"
op|','
string|"'bus'"
op|':'
string|"'pci0'"
op|','
string|"'device_path'"
op|':'
string|"'/dev/vol01'"
op|'}'
newline|'\n'
name|'conn'
op|'='
op|'{'
string|"'data'"
op|':'
name|'disk_info'
op|'}'
newline|'\n'
name|'conf'
op|'='
name|'sio'
op|'.'
name|'get_config'
op|'('
name|'conn'
op|','
name|'disk_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'block'"
op|','
name|'conf'
op|'.'
name|'source_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/vol01'"
op|','
name|'conf'
op|'.'
name|'source_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_libvirt_scaleio_driver_disconnect
dedent|''
name|'def'
name|'test_libvirt_scaleio_driver_disconnect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sio'
op|'='
name|'scaleio'
op|'.'
name|'LibvirtScaleIOVolumeDriver'
op|'('
name|'self'
op|'.'
name|'fake_conn'
op|')'
newline|'\n'
name|'sio'
op|'.'
name|'connector'
op|'.'
name|'disconnect_volume'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'disk_info'
op|'='
op|'{'
string|"'path'"
op|':'
string|"'/dev/vol01'"
op|','
string|"'name'"
op|':'
string|"'vol01'"
op|','
string|"'type'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'dev'"
op|':'
string|"'vda1'"
op|','
string|"'bus'"
op|':'
string|"'pci0'"
op|','
string|"'device_path'"
op|':'
string|"'/dev/vol01'"
op|'}'
newline|'\n'
name|'conn'
op|'='
op|'{'
string|"'data'"
op|':'
name|'disk_info'
op|'}'
newline|'\n'
name|'sio'
op|'.'
name|'disconnect_volume'
op|'('
name|'conn'
op|','
name|'disk_info'
op|')'
newline|'\n'
name|'sio'
op|'.'
name|'connector'
op|'.'
name|'disconnect_volume'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'disk_info'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
