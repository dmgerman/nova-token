begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Cloudbase Solutions Srl'
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
string|'"""\nManagement class for live migration VM operations.\n"""'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'baseops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
comment|'# Check needed for unit testing on Unix'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'wmi'
newline|'\n'
nl|'\n'
DECL|variable|LOG
dedent|''
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LiveMigrationOps
name|'class'
name|'LiveMigrationOps'
op|'('
name|'baseops'
op|'.'
name|'BaseOps'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'volumeops'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LiveMigrationOps'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutils'
op|'.'
name|'VMUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
newline|'\n'
nl|'\n'
DECL|member|_check_live_migration_config
dedent|''
name|'def'
name|'_check_live_migration_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn_v2'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'\'Live migration is not supported " \\\n                    "by this version of Hyper-V\''
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'migration_svc'
op|'='
name|'self'
op|'.'
name|'_conn_v2'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vsmssd'
op|'='
name|'migration_svc'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_ElementSettingData'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemMigrationServiceSettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'vsmssd'
op|'.'
name|'EnableVirtualSystemMigration'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Live migration is not enabled on this host'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'migration_svc'
op|'.'
name|'MigrationServiceListenerIPAddressList'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Live migration networks are not configured on this host'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'post_method'
op|','
nl|'\n'
name|'recover_method'
op|','
name|'block_migration'
op|'='
name|'False'
op|','
name|'migrate_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"live_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
name|'instance_name'
op|'='
name|'instance_ref'
op|'['
string|'"name"'
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_live_migration_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vm_name'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_conn'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance'
op|'='
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'vm'
op|'='
name|'self'
op|'.'
name|'_conn_v2'
op|'.'
name|'Msvm_ComputerSystem'
op|'('
nl|'\n'
name|'ElementName'
op|'='
name|'instance_name'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vm_settings'
op|'='
name|'vm'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_SettingsDefineState'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_VirtualSystemSettingData'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'new_resource_setting_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'sasds'
op|'='
name|'vm_settings'
op|'.'
name|'associators'
op|'('
nl|'\n'
name|'wmi_association_class'
op|'='
string|"'Msvm_VirtualSystemSettingDataComponent'"
op|','
nl|'\n'
name|'wmi_result_class'
op|'='
string|"'Msvm_StorageAllocationSettingData'"
op|')'
newline|'\n'
name|'for'
name|'sasd'
name|'in'
name|'sasds'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'sasd'
op|'.'
name|'ResourceType'
op|'=='
number|'31'
name|'and'
name|'sasd'
op|'.'
name|'ResourceSubType'
op|'=='
string|'"Microsoft:Hyper-V:Virtual Hard Disk"'
op|':'
newline|'\n'
comment|'#sasd.PoolId = ""'
nl|'\n'
indent|'                    '
name|'new_resource_setting_data'
op|'.'
name|'append'
op|'('
name|'sasd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Getting live migration networks for remote "'
nl|'\n'
string|'"host: %s"'
op|')'
op|','
name|'dest'
op|')'
newline|'\n'
name|'_conn_v2_remote'
op|'='
name|'wmi'
op|'.'
name|'WMI'
op|'('
nl|'\n'
name|'moniker'
op|'='
string|"'//'"
op|'+'
name|'dest'
op|'+'
string|"'/root/virtualization/v2'"
op|')'
newline|'\n'
name|'migration_svc_remote'
op|'='
name|'_conn_v2_remote'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'remote_ip_address_list'
op|'='
name|'migration_svc_remote'
op|'.'
name|'MigrationServiceListenerIPAddressList'
newline|'\n'
nl|'\n'
comment|'# VirtualSystemAndStorage'
nl|'\n'
name|'vsmsd'
op|'='
name|'self'
op|'.'
name|'_conn_v2'
op|'.'
name|'query'
op|'('
string|'"select * from "'
nl|'\n'
string|'"Msvm_VirtualSystemMigrationSettingData "'
nl|'\n'
string|'"where MigrationType = 32771"'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vsmsd'
op|'.'
name|'DestinationIPAddressList'
op|'='
name|'remote_ip_address_list'
newline|'\n'
name|'migration_setting_data'
op|'='
name|'vsmsd'
op|'.'
name|'GetText_'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'migration_svc'
op|'='
name|'self'
op|'.'
name|'_conn_v2'
op|'.'
name|'Msvm_VirtualSystemMigrationService'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting live migration for instance: %s"'
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
op|'('
name|'job_path'
op|','
name|'ret_val'
op|')'
op|'='
name|'migration_svc'
op|'.'
name|'MigrateVirtualSystemToHost'
op|'('
nl|'\n'
name|'ComputerSystem'
op|'='
name|'vm'
op|'.'
name|'path_'
op|'('
op|')'
op|','
nl|'\n'
name|'DestinationHost'
op|'='
name|'dest'
op|','
nl|'\n'
name|'MigrationSettingData'
op|'='
name|'migration_setting_data'
op|','
nl|'\n'
name|'NewResourceSettingData'
op|'='
name|'new_resource_setting_data'
op|')'
newline|'\n'
name|'if'
name|'ret_val'
op|'=='
name|'constants'
op|'.'
name|'WMI_JOB_STATUS_STARTED'
op|':'
newline|'\n'
indent|'                '
name|'success'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'check_job_status'
op|'('
name|'job_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'success'
op|'='
op|'('
name|'ret_val'
op|'=='
number|'0'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'success'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'vmutils'
op|'.'
name|'HyperVException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Failed to live migrate VM %s'"
op|')'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
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
name|'debug'
op|'('
name|'_'
op|'('
string|'"Calling live migration recover_method "'
nl|'\n'
string|'"for instance: %s"'
op|')'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'recover_method'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Calling live migration post_method for instance: %s"'
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'post_method'
op|'('
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pre_live_migration
dedent|''
name|'def'
name|'pre_live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"pre_live_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_live_migration_config'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_cow_images'
op|':'
newline|'\n'
indent|'            '
name|'ebs_root'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'volume_in_mapping'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'get_default_root_device'
op|'('
op|')'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ebs_root'
op|':'
newline|'\n'
indent|'                '
name|'base_vhd_path'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_base_vhd_path'
op|'('
nl|'\n'
name|'instance'
op|'['
string|'"image_ref"'
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'base_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'fetch_image'
op|'('
name|'base_vhd_path'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"image_ref"'
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"user_id"'
op|']'
op|','
nl|'\n'
name|'instance'
op|'['
string|'"project_id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_live_migration_at_destination
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'post_live_migration_at_destination'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'network_info'
op|','
name|'block_migration'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"post_live_migration_at_destination called"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compare_cpu
dedent|''
name|'def'
name|'compare_cpu'
op|'('
name|'self'
op|','
name|'cpu_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"compare_cpu called %s"'
op|')'
op|','
name|'cpu_info'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
