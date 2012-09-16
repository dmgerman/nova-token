begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""\nA connection to Hyper-V .\nUses Windows Management Instrumentation (WMI) calls to interact with Hyper-V\nHyper-V WMI usage:\n    http://msdn.microsoft.com/en-us/library/cc723875%28v=VS.85%29.aspx\nThe Hyper-V object model briefly:\n    The physical computer and its hosted virtual machines are each represented\n    by the Msvm_ComputerSystem class.\n\n    Each virtual machine is associated with a\n    Msvm_VirtualSystemGlobalSettingData (vs_gs_data) instance and one or more\n    Msvm_VirtualSystemSettingData (vmsetting) instances. For each vmsetting\n    there is a series of Msvm_ResourceAllocationSettingData (rasd) objects.\n    The rasd objects describe the settings for each device in a VM.\n    Together, the vs_gs_data, vmsettings and rasds describe the configuration\n    of the virtual machine.\n\n    Creating new resources such as disks and nics involves cloning a default\n    rasd object and appropriately modifying the clone and calling the\n    AddVirtualSystemResources WMI method\n    Changing resources such as memory uses the ModifyVirtualSystemResources\n    WMI method\n\nUsing the Python WMI library:\n    Tutorial:\n        http://timgolden.me.uk/python/wmi/tutorial.html\n    Hyper-V WMI objects can be retrieved simply by using the class name\n    of the WMI object and optionally specifying a column to filter the\n    result set. More complex filters can be formed using WQL (sql-like)\n    queries.\n    The parameters and return tuples of WMI method calls can gleaned by\n    examining the doc string. For example:\n    >>> vs_man_svc.ModifyVirtualSystemResources.__doc__\n    ModifyVirtualSystemResources (ComputerSystem, ResourceSettingData[])\n                 => (Job, ReturnValue)\'\n    When passing setting data (ResourceSettingData) to the WMI method,\n    an XML representation of the data is passed in using GetText_(1).\n    Available methods on a service can be determined using method.keys():\n    >>> vs_man_svc.methods.keys()\n    vmsettings and rasds for a vm can be retrieved using the \'associators\'\n    method with the appropriate return class.\n    Long running WMI commands generally return a Job (an instance of\n    Msvm_ConcreteJob) whose state can be polled to determine when it finishes\n\n"""'
newline|'\n'
nl|'\n'
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
name|'livemigrationops'
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
op|')'
newline|'\n'
nl|'\n'
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
name|'self'
op|'.'
name|'_volumeops'
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
nl|'\n'
name|'self'
op|'.'
name|'_volumeops'
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
name|'self'
op|'.'
name|'_host'
op|'='
name|'host'
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
name|'network_info'
op|','
nl|'\n'
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
name|'instance'
op|','
name|'network_info'
op|'='
name|'None'
op|','
name|'cleanup'
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
name|'cleanup'
op|')'
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
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume storage to VM instance"""'
newline|'\n'
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
name|'instance_name'
op|','
nl|'\n'
name|'mountpoint'
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
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volume storage to VM instance"""'
newline|'\n'
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
name|'instance_name'
op|','
nl|'\n'
name|'mountpoint'
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
DECL|member|poll_rescued_instances
dedent|''
name|'def'
name|'poll_rescued_instances'
op|'('
name|'self'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_available_resource
dedent|''
name|'def'
name|'get_available_resource'
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
name|'get_available_resource'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_host_status
dedent|''
name|'def'
name|'update_host_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""See xenapi_conn.py implementation."""'
newline|'\n'
name|'pass'
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
string|'"""See xenapi_conn.py implementation."""'
newline|'\n'
name|'return'
op|'{'
op|'}'
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
string|'"""Reboots, shuts down or powers up the host."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|set_host_enabled
dedent|''
name|'def'
name|'set_host_enabled'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'enabled'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets the specified host\'s ability to accept new instances."""'
newline|'\n'
name|'pass'
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
name|'name'
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
name|'name'
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
name|'instance'
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
name|'instance'
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
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'post_method'
op|','
name|'recover_method'
op|','
name|'block_migration'
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
name|'return'
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'compare_cpu'
op|'('
name|'cpu_info'
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
name|'self'
op|'.'
name|'_livemigrationops'
op|'.'
name|'post_live_migration_at_destination'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_ref'
op|','
name|'network_info'
op|','
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
name|'ctxt'
op|','
name|'instance'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_destination_cleanup
dedent|''
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|check_can_live_migrate_source
dedent|''
name|'def'
name|'check_can_live_migrate_source'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance'
op|','
name|'dest_check_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"plug_vifs called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"plug_vifs called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
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
name|'instance_ref'
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
name|'_'
op|'('
string|'"ensure_filtering_rules_for_instance called"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_ref'
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
string|'"""Stop filtering instance"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"unfilter_instance called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
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
string|'"""Confirms a resize, destroying the source VM"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"confirm_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
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
string|'"""Finish reverting a resize, powering back on the instance"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"finish_revert_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
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
string|'"""Completes a resize, turning on the migrated instance"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"finish_migration called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
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
string|'"get_console_output called"'
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
DECL|member|legacy_nwinfo
dedent|''
name|'def'
name|'legacy_nwinfo'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
