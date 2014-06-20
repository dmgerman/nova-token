begin_unit
comment|'# Copyright (c) 2010 Cloud.com, Inc'
nl|'\n'
comment|'# Copyright (c) 2012 Cloudbase Solutions Srl'
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
string|'"""\nA Hyper-V Nova Compute driver.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'hostops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'livemigrationops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'migrationops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'rdpconsoleops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'snapshotops'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmops'
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
nl|'\n'
nl|'\n'
DECL|class|HyperVDriver
name|'class'
name|'HyperVDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
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
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HyperVDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_hostops'
op|'='
name|'hostops'
op|'.'
name|'HostOps'
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
name|'_vmops'
op|'='
name|'vmops'
op|'.'
name|'VMOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_snapshotops'
op|'='
name|'snapshotops'
op|'.'
name|'SnapshotOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_livemigrationops'
op|'='
name|'livemigrationops'
op|'.'
name|'LiveMigrationOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_migrationops'
op|'='
name|'migrationops'
op|'.'
name|'MigrationOps'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_rdpconsoleops'
op|'='
name|'rdpconsoleops'
op|'.'
name|'RDPConsoleOps'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'network_info'
op|'='
name|'None'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'reboot_type'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'bad_volumes_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'reboot_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'destroy_disks'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'destroy_disks'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cleanup after instance being destroyed by Hypervisor."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance'
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
name|'context'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|','
nl|'\n'
name|'disk_bus'
op|'='
name|'None'
op|','
name|'device_type'
op|'='
name|'None'
op|','
name|'encryption'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
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
name|'instance'
op|','
name|'mountpoint'
op|','
nl|'\n'
name|'encryption'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volume_connector
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
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'get_volume_connector'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
op|'('
name|'self'
op|','
name|'nodename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_available_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_stats
dedent|''
name|'def'
name|'get_host_stats'
op|'('
name|'self'
op|','
name|'refresh'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_stats'
op|'('
name|'refresh'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_power_action
dedent|''
name|'def'
name|'host_power_action'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'host_power_action'
op|'('
name|'host'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|','
name|'update_task_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_snapshotops'
op|'.'
name|'snapshot'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|','
nl|'\n'
name|'update_task_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'pause'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unpause'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'suspend'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'resume'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_off
dedent|''
name|'def'
name|'power_off'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|power_on
dedent|''
name|'def'
name|'power_on'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
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
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'live_migration'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'post_method'
op|','
name|'recover_method'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'migrate_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rollback_live_migration_at_destination
dedent|''
name|'def'
name|'rollback_live_migration_at_destination'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'destroy'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
name|'block_device_info'
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
op|','
name|'disk_info'
op|','
name|'migrate_data'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'pre_live_migration'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'block_device_info'
op|','
nl|'\n'
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|post_live_migration_at_destination
dedent|''
name|'def'
name|'post_live_migration_at_destination'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'False'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'post_live_migration_at_destination'
op|'('
nl|'\n'
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_migration'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination
dedent|''
name|'def'
name|'check_can_live_migrate_destination'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
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
name|'return'
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'check_can_live_migrate_destination'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'src_compute_info'
op|','
name|'dst_compute_info'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination_cleanup
dedent|''
name|'def'
name|'check_can_live_migrate_destination_cleanup'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'check_can_live_migrate_destination_cleanup'
op|'('
nl|'\n'
name|'context'
op|','
name|'dest_check_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_source
dedent|''
name|'def'
name|'check_can_live_migrate_source'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'check_can_live_migrate_source'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'dest_check_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug_vifs
dedent|''
name|'def'
name|'plug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Plug VIFs into networks."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"VIF plugging is not supported by the Hyper-V driver."'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug_vifs
dedent|''
name|'def'
name|'unplug_vifs'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unplug VIFs from networks."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"VIF unplugging is not supported by the Hyper-V driver."'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ensure_filtering_rules_for_instance
dedent|''
name|'def'
name|'ensure_filtering_rules_for_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"ensure_filtering_rules_for_instance called"'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"unfilter_instance called"'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_disk_and_power_off
dedent|''
name|'def'
name|'migrate_disk_and_power_off'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'flavor'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_migrationops'
op|'.'
name|'migrate_disk_and_power_off'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
name|'dest'
op|','
nl|'\n'
name|'flavor'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|confirm_migration
dedent|''
name|'def'
name|'confirm_migration'
op|'('
name|'self'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_migrationops'
op|'.'
name|'confirm_migration'
op|'('
name|'migration'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_revert_migration
dedent|''
name|'def'
name|'finish_revert_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_migrationops'
op|'.'
name|'finish_revert_migration'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|','
name|'power_on'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish_migration
dedent|''
name|'def'
name|'finish_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'instance'
op|','
name|'disk_info'
op|','
nl|'\n'
name|'network_info'
op|','
name|'image_meta'
op|','
name|'resize_instance'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
name|'power_on'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_migrationops'
op|'.'
name|'finish_migration'
op|'('
name|'context'
op|','
name|'migration'
op|','
name|'instance'
op|','
nl|'\n'
name|'disk_info'
op|','
name|'network_info'
op|','
nl|'\n'
name|'image_meta'
op|','
name|'resize_instance'
op|','
nl|'\n'
name|'block_device_info'
op|','
name|'power_on'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_host_ip_addr
dedent|''
name|'def'
name|'get_host_ip_addr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_ip_addr'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_rdp_console
dedent|''
name|'def'
name|'get_rdp_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_rdpconsoleops'
op|'.'
name|'get_rdp_console'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
