begin_unit
comment|'# Copyright 2012 Pedro Navarro Perez'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
newline|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'os_win'
name|'import'
name|'exceptions'
name|'as'
name|'os_win_exc'
newline|'\n'
name|'from'
name|'os_win'
name|'import'
name|'utilsfactory'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'six'
op|'.'
name|'moves'
name|'import'
name|'range'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
op|','
name|'_LW'
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
name|'driver'
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
DECL|class|VolumeOps
name|'class'
name|'VolumeOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Management class for Volume-related tasks\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_iscsi_initiator_utils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_default_root_device'
op|'='
string|"'vda'"
newline|'\n'
name|'self'
op|'.'
name|'volume_drivers'
op|'='
op|'{'
string|"'smbfs'"
op|':'
name|'SMBFSVolumeDriver'
op|'('
op|')'
op|','
nl|'\n'
string|"'iscsi'"
op|':'
name|'ISCSIVolumeDriver'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_volume_driver
dedent|''
name|'def'
name|'_get_volume_driver'
op|'('
name|'self'
op|','
name|'driver_type'
op|'='
name|'None'
op|','
name|'connection_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'connection_info'
op|':'
newline|'\n'
indent|'            '
name|'driver_type'
op|'='
name|'connection_info'
op|'.'
name|'get'
op|'('
string|"'driver_volume_type'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'driver_type'
name|'not'
name|'in'
name|'self'
op|'.'
name|'volume_drivers'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeDriverNotFound'
op|'('
name|'driver_type'
op|'='
name|'driver_type'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'volume_drivers'
op|'['
name|'driver_type'
op|']'
newline|'\n'
nl|'\n'
DECL|member|attach_volumes
dedent|''
name|'def'
name|'attach_volumes'
op|'('
name|'self'
op|','
name|'block_device_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'ebs_root'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_volume'
op|'('
name|'mapping'
op|'['
number|'0'
op|']'
op|'['
string|"'connection_info'"
op|']'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'True'
op|')'
newline|'\n'
name|'mapping'
op|'='
name|'mapping'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_volume'
op|'('
name|'vol'
op|'['
string|"'connection_info'"
op|']'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volumes
dedent|''
dedent|''
name|'def'
name|'disconnect_volumes'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'block_devices'
op|'='
name|'self'
op|'.'
name|'_group_block_devices_by_type'
op|'('
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
name|'for'
name|'driver_type'
op|','
name|'block_device_mapping'
name|'in'
name|'block_devices'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'_get_volume_driver'
op|'('
name|'driver_type'
op|')'
newline|'\n'
name|'volume_driver'
op|'.'
name|'disconnect_volumes'
op|'('
name|'block_device_mapping'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'_get_volume_driver'
op|'('
nl|'\n'
name|'connection_info'
op|'='
name|'connection_info'
op|')'
newline|'\n'
name|'volume_driver'
op|'.'
name|'attach_volume'
op|'('
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'_get_volume_driver'
op|'('
nl|'\n'
name|'connection_info'
op|'='
name|'connection_info'
op|')'
newline|'\n'
name|'volume_driver'
op|'.'
name|'detach_volume'
op|'('
name|'connection_info'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ebs_root_in_block_devices
dedent|''
name|'def'
name|'ebs_root_in_block_devices'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'block_device_info'
op|':'
newline|'\n'
indent|'            '
name|'root_device'
op|'='
name|'block_device_info'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'root_device'
op|':'
newline|'\n'
indent|'                '
name|'root_device'
op|'='
name|'self'
op|'.'
name|'_default_root_device'
newline|'\n'
dedent|''
name|'return'
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
name|'root_device'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fix_instance_volume_disk_paths
dedent|''
dedent|''
name|'def'
name|'fix_instance_volume_disk_paths'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
comment|'# Mapping containing the current disk paths for each volume.'
nl|'\n'
indent|'        '
name|'actual_disk_mapping'
op|'='
name|'self'
op|'.'
name|'get_disk_path_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'actual_disk_mapping'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
comment|'# Mapping containing virtual disk resource path and the physical'
nl|'\n'
comment|'# disk path for each volume serial number. The physical path'
nl|'\n'
comment|'# associated with this resource may not be the right one,'
nl|'\n'
comment|'# as physical disk paths can get swapped after host reboots.'
nl|'\n'
dedent|''
name|'vm_disk_mapping'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_physical_disk_mapping'
op|'('
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'serial'
op|','
name|'vm_disk'
name|'in'
name|'vm_disk_mapping'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'actual_disk_path'
op|'='
name|'actual_disk_mapping'
op|'['
name|'serial'
op|']'
newline|'\n'
name|'if'
name|'vm_disk'
op|'['
string|"'mounted_disk_path'"
op|']'
op|'!='
name|'actual_disk_path'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'set_disk_host_res'
op|'('
name|'vm_disk'
op|'['
string|"'resource_path'"
op|']'
op|','
nl|'\n'
name|'actual_disk_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volume_connector
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_volume_connector'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'Could not determine iscsi initiator name'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'ip'"
op|':'
name|'CONF'
op|'.'
name|'my_block_storage_ip'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'initiator'"
op|':'
name|'self'
op|'.'
name|'_initiator'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|initialize_volumes_connection
dedent|''
name|'def'
name|'initialize_volumes_connection'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'_get_volume_driver'
op|'('
nl|'\n'
name|'connection_info'
op|'='
name|'connection_info'
op|')'
newline|'\n'
name|'volume_driver'
op|'.'
name|'initialize_volume_connection'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_disk_path_mapping
dedent|''
dedent|''
name|'def'
name|'get_disk_path_mapping'
op|'('
name|'self'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'block_mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'disk_path_mapping'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_mapping'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'disk_serial'
op|'='
name|'connection_info'
op|'['
string|"'serial'"
op|']'
newline|'\n'
nl|'\n'
name|'disk_path'
op|'='
name|'self'
op|'.'
name|'get_mounted_disk_path_from_volume'
op|'('
name|'connection_info'
op|')'
newline|'\n'
name|'disk_path_mapping'
op|'['
name|'disk_serial'
op|']'
op|'='
name|'disk_path'
newline|'\n'
dedent|''
name|'return'
name|'disk_path_mapping'
newline|'\n'
nl|'\n'
DECL|member|_group_block_devices_by_type
dedent|''
name|'def'
name|'_group_block_devices_by_type'
op|'('
name|'self'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'block_devices'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'='
name|'volume'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'volume_type'
op|'='
name|'connection_info'
op|'.'
name|'get'
op|'('
string|"'driver_volume_type'"
op|')'
newline|'\n'
name|'block_devices'
op|'['
name|'volume_type'
op|']'
op|'.'
name|'append'
op|'('
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'block_devices'
newline|'\n'
nl|'\n'
DECL|member|get_mounted_disk_path_from_volume
dedent|''
name|'def'
name|'get_mounted_disk_path_from_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_driver'
op|'='
name|'self'
op|'.'
name|'_get_volume_driver'
op|'('
nl|'\n'
name|'connection_info'
op|'='
name|'connection_info'
op|')'
newline|'\n'
name|'return'
name|'volume_driver'
op|'.'
name|'get_mounted_disk_path_from_volume'
op|'('
nl|'\n'
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ISCSIVolumeDriver
dedent|''
dedent|''
name|'class'
name|'ISCSIVolumeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_iscsi_initiator_utils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|login_storage_target
dedent|''
name|'def'
name|'login_storage_target'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'target_lun'
op|'='
name|'data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'target_portal'
op|'='
name|'data'
op|'['
string|"'target_portal'"
op|']'
newline|'\n'
name|'auth_method'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_method'"
op|')'
newline|'\n'
name|'auth_username'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_username'"
op|')'
newline|'\n'
name|'auth_password'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'auth_password'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'auth_method'
name|'and'
name|'auth_method'
op|'.'
name|'upper'
op|'('
op|')'
op|'!='
string|"'CHAP'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Cannot log in target %(target_iqn)s. Unsupported "'
nl|'\n'
string|'"iSCSI authentication method: %(auth_method)s."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
nl|'\n'
string|"'auth_method'"
op|':'
name|'auth_method'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedBDMVolumeAuthMethod'
op|'('
nl|'\n'
name|'auth_method'
op|'='
name|'auth_method'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if we already logged in'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_device_number_for_target'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Already logged in on storage target. No need to "'
nl|'\n'
string|'"login. Portal: %(target_portal)s, "'
nl|'\n'
string|'"IQN: %(target_iqn)s, LUN: %(target_lun)s"'
op|','
nl|'\n'
op|'{'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logging in on storage target. Portal: "'
nl|'\n'
string|'"%(target_portal)s, IQN: %(target_iqn)s, "'
nl|'\n'
string|'"LUN: %(target_lun)s"'
op|','
nl|'\n'
op|'{'
string|"'target_portal'"
op|':'
name|'target_portal'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
name|'target_iqn'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'login_storage_target'
op|'('
name|'target_lun'
op|','
name|'target_iqn'
op|','
nl|'\n'
name|'target_portal'
op|','
name|'auth_username'
op|','
nl|'\n'
name|'auth_password'
op|')'
newline|'\n'
comment|'# Wait for the target to be mounted'
nl|'\n'
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volumes
dedent|''
dedent|''
name|'def'
name|'disconnect_volumes'
op|'('
name|'self'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'iscsi_targets'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'int'
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'            '
name|'target_iqn'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
op|'['
string|"'data'"
op|']'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'iscsi_targets'
op|'['
name|'target_iqn'
op|']'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'target_iqn'
op|','
name|'disconnected_luns'
name|'in'
name|'iscsi_targets'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|','
name|'disconnected_luns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|logout_storage_target
dedent|''
dedent|''
name|'def'
name|'logout_storage_target'
op|'('
name|'self'
op|','
name|'target_iqn'
op|','
name|'disconnected_luns_count'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'total_available_luns'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_lun_count'
op|'('
nl|'\n'
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'total_available_luns'
op|'=='
name|'disconnected_luns_count'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Logging off storage target %s"'
op|','
name|'target_iqn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Skipping disconnecting target %s as there "'
nl|'\n'
string|'"are LUNs still being used."'
op|','
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_mounted_disk_path_from_volume
dedent|''
dedent|''
name|'def'
name|'get_mounted_disk_path_from_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'target_lun'
op|'='
name|'data'
op|'['
string|"'target_lun'"
op|']'
newline|'\n'
name|'target_iqn'
op|'='
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Getting the mounted disk'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_mounted_disk_from_lun'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|','
nl|'\n'
name|'wait_for_device'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach a volume to the SCSI controller or to the IDE controller if\n        ebs_root is True\n        """'
newline|'\n'
name|'target_iqn'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Attach_volume: %(connection_info)s to %(instance_name)s"'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'login_storage_target'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'serial'
op|'='
name|'connection_info'
op|'['
string|"'serial'"
op|']'
newline|'\n'
comment|'# Getting the mounted disk'
nl|'\n'
name|'mounted_disk_path'
op|'='
name|'self'
op|'.'
name|'get_mounted_disk_path_from_volume'
op|'('
nl|'\n'
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'ebs_root'
op|':'
newline|'\n'
comment|'# Find the IDE controller for the vm.'
nl|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_ide_controller'
op|'('
nl|'\n'
name|'instance_name'
op|','
number|'0'
op|')'
newline|'\n'
comment|'# Attaching to the first slot'
nl|'\n'
name|'slot'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Find the SCSI controller for the vm'
nl|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_scsi_controller'
op|'('
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'slot'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_free_controller_slot'
op|'('
name|'ctrller_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'attach_volume_to_controller'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'ctrller_path'
op|','
nl|'\n'
name|'slot'
op|','
nl|'\n'
name|'mounted_disk_path'
op|','
nl|'\n'
name|'serial'
op|'='
name|'serial'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Unable to attach volume to instance %s'"
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'target_iqn'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'if'
name|'target_iqn'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach a volume to the SCSI controller."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Detach_volume: %(connection_info)s "'
nl|'\n'
string|'"from %(instance_name)s"'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'target_iqn'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'mounted_disk_path'
op|'='
name|'self'
op|'.'
name|'get_mounted_disk_path_from_volume'
op|'('
nl|'\n'
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Detaching physical disk from instance: %s"'
op|','
nl|'\n'
name|'mounted_disk_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'detach_vm_disk'
op|'('
name|'instance_name'
op|','
name|'mounted_disk_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_mounted_disk_from_lun
dedent|''
name|'def'
name|'_get_mounted_disk_from_lun'
op|'('
name|'self'
op|','
name|'target_iqn'
op|','
name|'target_lun'
op|','
nl|'\n'
name|'wait_for_device'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# The WMI query in get_device_number_for_target can incorrectly'
nl|'\n'
comment|'# return no data when the system is under load.  This issue can'
nl|'\n'
comment|'# be avoided by adding a retry.'
nl|'\n'
indent|'        '
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'mounted_disk_query_retry_count'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'device_number'
op|'='
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_device_number_for_target'
op|'('
nl|'\n'
name|'target_iqn'
op|','
name|'target_lun'
op|')'
newline|'\n'
name|'if'
name|'device_number'
name|'in'
op|'('
name|'None'
op|','
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'attempt'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Attempt %d to get device_number '"
nl|'\n'
string|"'from get_device_number_for_target failed. '"
nl|'\n'
string|"'Retrying...'"
op|','
name|'attempt'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'mounted_disk_query_retry_interval'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'device_number'
name|'in'
op|'('
name|'None'
op|','
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Unable to find a mounted disk for '"
nl|'\n'
string|"'target_iqn: %s'"
op|')'
op|'%'
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Device number: %(device_number)s, '"
nl|'\n'
string|"'target lun: %(target_lun)s'"
op|','
nl|'\n'
op|'{'
string|"'device_number'"
op|':'
name|'device_number'
op|','
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
newline|'\n'
comment|'# Finding Mounted disk drive'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'volume_attach_retry_count'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mounted_disk_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_mounted_disk_by_drive_number'
op|'('
nl|'\n'
name|'device_number'
op|')'
newline|'\n'
name|'if'
name|'mounted_disk_path'
name|'or'
name|'not'
name|'wait_for_device'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'volume_attach_retry_interval'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'mounted_disk_path'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Unable to find a mounted disk for '"
nl|'\n'
string|"'target_iqn: %s. Please ensure that '"
nl|'\n'
string|"'the host\\'s SAN policy is set to '"
nl|'\n'
string|'\'"OfflineAll" or "OfflineShared"\''
op|')'
op|'%'
nl|'\n'
name|'target_iqn'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'mounted_disk_path'
newline|'\n'
nl|'\n'
DECL|member|get_target_from_disk_path
dedent|''
name|'def'
name|'get_target_from_disk_path'
op|'('
name|'self'
op|','
name|'physical_drive_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_from_disk_path'
op|'('
name|'physical_drive_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_target_lun_count
dedent|''
name|'def'
name|'get_target_lun_count'
op|'('
name|'self'
op|','
name|'target_iqn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volutils'
op|'.'
name|'get_target_lun_count'
op|'('
name|'target_iqn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize_volume_connection
dedent|''
name|'def'
name|'initialize_volume_connection'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'login_storage_target'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|export_path_synchronized
dedent|''
dedent|''
name|'def'
name|'export_path_synchronized'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|wrapper
indent|'    '
name|'def'
name|'wrapper'
op|'('
name|'inst'
op|','
name|'connection_info'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'export_path'
op|'='
name|'inst'
op|'.'
name|'_get_export_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'export_path'
op|')'
newline|'\n'
DECL|function|inner
name|'def'
name|'inner'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'f'
op|'('
name|'inst'
op|','
name|'connection_info'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'inner'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SMBFSVolumeDriver
dedent|''
name|'class'
name|'SMBFSVolumeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_smbutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_smbutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_username_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'user(?:name)?=([^, ]+)'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_password_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'pass(?:word)?=([^, ]+)'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_mounted_disk_path_from_volume
dedent|''
name|'def'
name|'get_mounted_disk_path_from_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_disk_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'export_path_synchronized'
newline|'\n'
DECL|member|attach_volume
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'ebs_root'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ensure_share_mounted'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'disk_path'
op|'='
name|'self'
op|'.'
name|'_get_disk_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ebs_root'
op|':'
newline|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_ide_controller'
op|'('
nl|'\n'
name|'instance_name'
op|','
number|'0'
op|')'
newline|'\n'
name|'slot'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'ctrller_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_scsi_controller'
op|'('
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'slot'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_free_controller_slot'
op|'('
name|'ctrller_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'attach_drive'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'disk_path'
op|','
nl|'\n'
name|'ctrller_path'
op|','
nl|'\n'
name|'slot'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'os_win_exc'
op|'.'
name|'HyperVException'
name|'as'
name|'exn'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Attach volume failed to %(instance_name)s: '"
nl|'\n'
string|"'%(exn)s'"
op|')'
op|','
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
nl|'\n'
string|"'exn'"
op|':'
name|'exn'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'VolumeAttachFailed'
op|'('
nl|'\n'
name|'volume_id'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
name|'reason'
op|'='
name|'exn'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Detaching volume: %(connection_info)s "'
nl|'\n'
string|'"from %(instance_name)s"'
op|','
nl|'\n'
op|'{'
string|"'connection_info'"
op|':'
name|'connection_info'
op|','
nl|'\n'
string|"'instance_name'"
op|':'
name|'instance_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'disk_path'
op|'='
name|'self'
op|'.'
name|'_get_disk_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
name|'export_path'
op|'='
name|'self'
op|'.'
name|'_get_export_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'detach_vm_disk'
op|'('
name|'instance_name'
op|','
name|'disk_path'
op|','
nl|'\n'
name|'is_physical'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_unmount_smb_share'
op|'('
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volumes
dedent|''
name|'def'
name|'disconnect_volumes'
op|'('
name|'self'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'export_paths'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'            '
name|'connection_info'
op|'='
name|'vol'
op|'['
string|"'connection_info'"
op|']'
newline|'\n'
name|'export_path'
op|'='
name|'self'
op|'.'
name|'_get_export_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
name|'export_paths'
op|'.'
name|'add'
op|'('
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'export_path'
name|'in'
name|'export_paths'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_unmount_smb_share'
op|'('
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_export_path
dedent|''
dedent|''
name|'def'
name|'_get_export_path'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'export'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'/'"
op|','
string|"'\\\\'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_disk_path
dedent|''
name|'def'
name|'_get_disk_path'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'export'
op|'='
name|'self'
op|'.'
name|'_get_export_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
name|'disk_name'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'export'
op|','
name|'disk_name'
op|')'
newline|'\n'
name|'return'
name|'disk_path'
newline|'\n'
nl|'\n'
DECL|member|ensure_share_mounted
dedent|''
name|'def'
name|'ensure_share_mounted'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'export_path'
op|'='
name|'self'
op|'.'
name|'_get_export_path'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_smbutils'
op|'.'
name|'check_smb_mapping'
op|'('
name|'export_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'opts_str'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'get'
op|'('
string|"'options'"
op|','
string|"''"
op|')'
newline|'\n'
name|'username'
op|','
name|'password'
op|'='
name|'self'
op|'.'
name|'_parse_credentials'
op|'('
name|'opts_str'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_smbutils'
op|'.'
name|'mount_smb_share'
op|'('
name|'export_path'
op|','
nl|'\n'
name|'username'
op|'='
name|'username'
op|','
nl|'\n'
name|'password'
op|'='
name|'password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse_credentials
dedent|''
dedent|''
name|'def'
name|'_parse_credentials'
op|'('
name|'self'
op|','
name|'opts_str'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'match'
op|'='
name|'self'
op|'.'
name|'_username_regex'
op|'.'
name|'findall'
op|'('
name|'opts_str'
op|')'
newline|'\n'
name|'username'
op|'='
name|'match'
op|'['
number|'0'
op|']'
name|'if'
name|'match'
name|'and'
name|'match'
op|'['
number|'0'
op|']'
op|'!='
string|"'guest'"
name|'else'
name|'None'
newline|'\n'
nl|'\n'
name|'match'
op|'='
name|'self'
op|'.'
name|'_password_regex'
op|'.'
name|'findall'
op|'('
name|'opts_str'
op|')'
newline|'\n'
name|'password'
op|'='
name|'match'
op|'['
number|'0'
op|']'
name|'if'
name|'match'
name|'else'
name|'None'
newline|'\n'
nl|'\n'
name|'return'
name|'username'
op|','
name|'password'
newline|'\n'
nl|'\n'
DECL|member|initialize_volume_connection
dedent|''
name|'def'
name|'initialize_volume_connection'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ensure_share_mounted'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_unmount_smb_share
dedent|''
name|'def'
name|'_unmount_smb_share'
op|'('
name|'self'
op|','
name|'export_path'
op|')'
op|':'
newline|'\n'
comment|'# We synchronize share unmount and volume attach operations based on'
nl|'\n'
comment|'# the share path in order to avoid the situation when a SMB share is'
nl|'\n'
comment|'# unmounted while a volume exported by it is about to be attached to'
nl|'\n'
comment|'# an instance.'
nl|'\n'
indent|'        '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
name|'export_path'
op|')'
newline|'\n'
DECL|function|unmount_synchronized
name|'def'
name|'unmount_synchronized'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_smbutils'
op|'.'
name|'unmount_smb_share'
op|'('
name|'export_path'
op|')'
newline|'\n'
dedent|''
name|'unmount_synchronized'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
