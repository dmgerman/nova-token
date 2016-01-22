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
name|'from'
name|'os_brick'
op|'.'
name|'initiator'
name|'import'
name|'connector'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
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
name|'libvirt'
op|'.'
name|'volume'
name|'import'
name|'volume'
name|'as'
name|'libvirt_volume'
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
string|"'num_iscsi_scan_tries'"
op|','
string|"'nova.virt.libvirt.volume.iscsi'"
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtFibreChannelVolumeDriver
name|'class'
name|'LibvirtFibreChannelVolumeDriver'
op|'('
name|'libvirt_volume'
op|'.'
name|'LibvirtBaseVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver to attach Fibre Channel Network volumes to libvirt."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtFibreChannelVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
comment|'# Call the factory here so we can support'
nl|'\n'
comment|'# more than x86 architectures.'
nl|'\n'
name|'self'
op|'.'
name|'connector'
op|'='
name|'connector'
op|'.'
name|'InitiatorConnector'
op|'.'
name|'factory'
op|'('
nl|'\n'
string|"'FIBRE_CHANNEL'"
op|','
name|'utils'
op|'.'
name|'get_root_helper'
op|'('
op|')'
op|','
nl|'\n'
name|'use_multipath'
op|'='
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'iscsi_use_multipath'
op|','
nl|'\n'
name|'device_scan_attempts'
op|'='
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'num_iscsi_scan_tries'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns xml for libvirt."""'
newline|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtFibreChannelVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'disk_info'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"block"'
newline|'\n'
name|'conf'
op|'.'
name|'source_path'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'driver_io'
op|'='
string|'"native"'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
dedent|''
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach the volume to instance_name."""'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Calling os-brick to attach FC Volume"'
op|')'
newline|'\n'
name|'device_info'
op|'='
name|'self'
op|'.'
name|'connector'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Attached FC volume %s"'
op|','
name|'device_info'
op|')'
newline|'\n'
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|'='
name|'device_info'
op|'['
string|"'path'"
op|']'
newline|'\n'
name|'if'
string|"'multipath_id'"
name|'in'
name|'device_info'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'multipath_id'"
op|']'
op|'='
name|'device_info'
op|'['
string|"'multipath_id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volume
dedent|''
dedent|''
name|'def'
name|'disconnect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach the volume from instance_name."""'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"calling os-brick to detach FC Volume"'
op|')'
newline|'\n'
comment|'# TODO(walter-boring) eliminated the need for preserving'
nl|'\n'
comment|'# multipath_id.  Use scsi_id instead of multipath -ll'
nl|'\n'
comment|'# This will then eliminate the need to pass anything in'
nl|'\n'
comment|'# the 2nd param of disconnect_volume and be consistent'
nl|'\n'
comment|'# with the rest of the connectors.'
nl|'\n'
name|'self'
op|'.'
name|'connector'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|','
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Disconnected FC Volume %s"'
op|','
name|'disk_dev'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'LibvirtFibreChannelVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'disconnect_volume'
op|'('
name|'connection_info'
op|','
name|'disk_dev'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
