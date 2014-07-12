begin_unit
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
name|'functools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
name|'imagecache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'volumeops'
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
string|"'use_cow_images'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_os_version_requirement
name|'def'
name|'check_os_version_requirement'
op|'('
name|'function'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'function'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_livemigrutils'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|"'Live migration is supported '"
nl|'\n'
string|"'starting with Hyper-V Server '"
nl|'\n'
string|"'2012'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'function'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LiveMigrationOps
dedent|''
name|'class'
name|'LiveMigrationOps'
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
comment|'# Live migration is supported starting from Hyper-V Server 2012'
nl|'\n'
indent|'        '
name|'if'
name|'utilsfactory'
op|'.'
name|'get_hostutils'
op|'('
op|')'
op|'.'
name|'check_min_windows_version'
op|'('
number|'6'
op|','
number|'2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_livemigrutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_livemigrationutils'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_livemigrutils'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_pathutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'volumeops'
op|'.'
name|'VolumeOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'='
name|'imagecache'
op|'.'
name|'ImageCache'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|live_migration
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
nl|'\n'
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
string|'"live_migration called"'
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
name|'iscsi_targets'
op|'='
name|'self'
op|'.'
name|'_livemigrutils'
op|'.'
name|'live_migrate_vm'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'dest'
op|')'
newline|'\n'
name|'for'
op|'('
name|'target_iqn'
op|','
name|'target_lun'
op|')'
name|'in'
name|'iscsi_targets'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'logout_storage_target'
op|'('
name|'target_iqn'
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
string|'"Calling live migration recover_method "'
nl|'\n'
string|'"for instance: %s"'
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
string|'"Calling live migration post_method for instance: %s"'
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
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|pre_live_migration
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
string|'"pre_live_migration called"'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_livemigrutils'
op|'.'
name|'check_live_migration_config'
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
name|'boot_from_volume'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'ebs_root_in_block_devices'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'boot_from_volume'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'get_cached_image'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'login_storage_targets'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|post_live_migration_at_destination
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
string|'"post_live_migration_at_destination called"'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|check_can_live_migrate_destination
name|'def'
name|'check_can_live_migrate_destination'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'src_compute_info'
op|','
name|'dst_compute_info'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_destination called"'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|check_can_live_migrate_destination_cleanup
name|'def'
name|'check_can_live_migrate_destination_cleanup'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_destination_cleanup called"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_os_version_requirement'
newline|'\n'
DECL|member|check_can_live_migrate_source
name|'def'
name|'check_can_live_migrate_source'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"check_can_live_migrate_source called"'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'return'
name|'dest_check_data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
