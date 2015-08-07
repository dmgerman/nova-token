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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
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
op|'.'
name|'i18n'
name|'import'
name|'_LE'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
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
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
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
DECL|variable|volume_opts
name|'volume_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nfs_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'mnt'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Directory where the NFS volume is mounted on the'"
nl|'\n'
string|"' compute node'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nfs_mount_options'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Mount options passed to the NFS client. See section '"
nl|'\n'
string|"'of the nfs man page for details'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'volume_opts'
op|','
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtNFSVolumeDriver
name|'class'
name|'LibvirtNFSVolumeDriver'
op|'('
name|'libvirt_volume'
op|'.'
name|'LibvirtBaseVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class implements libvirt part of volume driver for NFS."""'
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
string|'"""Create back-end to nfs."""'
newline|'\n'
name|'super'
op|'('
name|'LibvirtNFSVolumeDriver'
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
DECL|member|_get_device_path
dedent|''
name|'def'
name|'_get_device_path'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'nfs_mount_point_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'export'"
op|']'
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'path'
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
name|'LibvirtNFSVolumeDriver'
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
string|"'file'"
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
name|'driver_format'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'get'
op|'('
string|"'format'"
op|','
string|"'raw'"
op|')'
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
string|'"""Connect the volume. Returns xml for libvirt."""'
newline|'\n'
name|'options'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'get'
op|'('
string|"'options'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_mounted'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'export'"
op|']'
op|','
name|'options'
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
name|'self'
op|'.'
name|'_get_device_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volume
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
string|'"""Disconnect the volume."""'
newline|'\n'
nl|'\n'
name|'export'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'export'"
op|']'
newline|'\n'
name|'mount_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'nfs_mount_point_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'export'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'mount_path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
string|"'device is busy'"
name|'in'
name|'exc'
op|'.'
name|'message'
name|'or'
nl|'\n'
string|"'target is busy'"
name|'in'
name|'exc'
op|'.'
name|'message'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"The NFS share %s is still in use."'
op|','
name|'export'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Couldn\'t unmount the NFS share %s"'
op|')'
op|','
name|'export'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ensure_mounted
dedent|''
dedent|''
dedent|''
name|'def'
name|'_ensure_mounted'
op|'('
name|'self'
op|','
name|'nfs_export'
op|','
name|'options'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""@type nfs_export: string\n           @type options: string\n        """'
newline|'\n'
name|'mount_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'nfs_mount_point_base'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'get_hash_str'
op|'('
name|'nfs_export'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'libvirt_utils'
op|'.'
name|'is_mounted'
op|'('
name|'mount_path'
op|','
name|'nfs_export'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_mount_nfs'
op|'('
name|'mount_path'
op|','
name|'nfs_export'
op|','
name|'options'
op|','
name|'ensure'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'mount_path'
newline|'\n'
nl|'\n'
DECL|member|_mount_nfs
dedent|''
name|'def'
name|'_mount_nfs'
op|'('
name|'self'
op|','
name|'mount_path'
op|','
name|'nfs_share'
op|','
name|'options'
op|'='
name|'None'
op|','
name|'ensure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mount nfs export to mount path."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'mount_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Construct the NFS mount command.'
nl|'\n'
name|'nfs_cmd'
op|'='
op|'['
string|"'mount'"
op|','
string|"'-t'"
op|','
string|"'nfs'"
op|']'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'nfs_mount_options'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'nfs_cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|"'-o'"
op|','
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'nfs_mount_options'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'options'
op|':'
newline|'\n'
indent|'            '
name|'nfs_cmd'
op|'.'
name|'extend'
op|'('
name|'options'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|')'
newline|'\n'
dedent|''
name|'nfs_cmd'
op|'.'
name|'extend'
op|'('
op|'['
name|'nfs_share'
op|','
name|'mount_path'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'nfs_cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ensure'
name|'and'
string|"'already mounted'"
name|'in'
name|'exc'
op|'.'
name|'message'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"%s is already mounted"'
op|')'
op|','
name|'nfs_share'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit