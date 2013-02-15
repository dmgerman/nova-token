begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
name|'socket'
newline|'\n'
name|'import'
name|'time'
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
name|'image'
name|'import'
name|'glance'
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
name|'powervm'
name|'import'
name|'operator'
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
DECL|variable|powervm_opts
name|'powervm_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ivm'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM manager type (ivm, hmc)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM manager host or ip'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_user'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM manager user name'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_mgr_passwd'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM manager user password'"
op|','
nl|'\n'
DECL|variable|secret
name|'secret'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_img_remote_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PowerVM image remote path'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'powervm_img_local_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Local directory to download glance images to'"
op|')'
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
name|'powervm_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerVMDriver
name|'class'
name|'PowerVMDriver'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""PowerVM Implementation of Compute Driver."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'PowerVMDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'='
name|'operator'
op|'.'
name|'PowerVMOperator'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|host_state
name|'def'
name|'host_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
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
string|'"""Initialize anything that is necessary for the driver to function,\n        including catching up with currently running VM\'s on the given host."""'
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
string|'"""Get the current status of an instance."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_num_instances
dedent|''
name|'def'
name|'get_num_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'list_instances'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_exists
dedent|''
name|'def'
name|'instance_exists'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'instance_exists'
op|'('
name|'instance_name'
op|')'
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
name|'_powervm'
op|'.'
name|'list_instances'
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
string|'"""Return currently known host stats."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_host_stats'
op|'('
name|'refresh'
op|'='
name|'refresh'
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
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|macs_for_instance
dedent|''
name|'def'
name|'macs_for_instance'
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
name|'_powervm'
op|'.'
name|'macs_for_instance'
op|'('
name|'instance'
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
string|'"""Create a new instance/VM/domain on powerVM."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'spawn'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_meta'
op|'['
string|"'id'"
op|']'
op|','
name|'network_info'
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
string|'"""Destroy (shutdown and delete) the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'destroy_disks'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot the specified instance.\n\n        :param instance: Instance object as returned by DB layer.\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param reboot_type: Either a HARD or SOFT reboot\n        """'
newline|'\n'
name|'pass'
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
string|'"""Retrieves the IP address of the hypervisor host."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"In get_host_ip_addr"'
op|')'
op|')'
newline|'\n'
comment|'# TODO(mrodden): use operator get_hostname instead'
nl|'\n'
name|'hostname'
op|'='
name|'CONF'
op|'.'
name|'powervm_mgr'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attempting to resolve %s"'
op|')'
op|'%'
name|'hostname'
op|')'
newline|'\n'
name|'ip_addr'
op|'='
name|'socket'
op|'.'
name|'gethostbyname'
op|'('
name|'hostname'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(hostname)s was successfully resolved to %(ip_addr)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'hostname'
op|','
string|"'ip_addr'"
op|':'
name|'ip_addr'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'ip_addr'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Snapshots the specified instance.\n\n        :param context: security context\n        :param instance: Instance object as returned by DB layer.\n        :param image_id: Reference to a pre-created image that will\n                         hold the snapshot.\n        """'
newline|'\n'
name|'snapshot_start'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# get current image info'
nl|'\n'
name|'glance_service'
op|','
name|'old_image_id'
op|'='
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'glance_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'old_image_id'
op|')'
newline|'\n'
name|'img_props'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
newline|'\n'
nl|'\n'
comment|'# build updated snapshot metadata'
nl|'\n'
name|'snapshot_meta'
op|'='
name|'glance_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'new_snapshot_meta'
op|'='
op|'{'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'snapshot_meta'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'image_location'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'image_state'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'owner_id'"
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'image_meta'
op|'['
string|"'disk_format'"
op|']'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'image_meta'
op|'['
string|"'container_format'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
string|"'architecture'"
name|'in'
name|'image_meta'
op|'['
string|"'properties'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'arch'
op|'='
name|'image_meta'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'architecture'"
op|']'
newline|'\n'
name|'new_snapshot_meta'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'architecture'"
op|']'
op|'='
name|'arch'
newline|'\n'
nl|'\n'
comment|'# disk capture and glance upload'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'capture_image'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'image_id'
op|','
nl|'\n'
name|'new_snapshot_meta'
op|')'
newline|'\n'
nl|'\n'
name|'snapshot_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'snapshot_start'
newline|'\n'
name|'inst_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"%(inst_name)s captured in %(snapshot_time)s seconds"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
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
string|'"""Pause the specified instance."""'
newline|'\n'
name|'pass'
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
string|'"""Unpause paused VM instance."""'
newline|'\n'
name|'pass'
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
string|'"""suspend the specified instance."""'
newline|'\n'
name|'pass'
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
string|'"""resume the specified instance."""'
newline|'\n'
name|'pass'
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
string|'"""Power off the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
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
string|'"""Power on the specified instance."""'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
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
string|'"""Retrieve resource info."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'get_available_resource'
op|'('
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
string|'"""Reboots, shuts down or powers up the host."""'
newline|'\n'
name|'pass'
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
string|'"""\n        Indicate if the driver requires the legacy network_info format.\n        """'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|manage_image_cache
dedent|''
name|'def'
name|'manage_image_cache'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'all_instances'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Manage the driver\'s local image cache.\n\n        Some drivers chose to cache images for instances on disk. This method\n        is an opportunity to do management of that cache which isn\'t directly\n        related to other calls into the driver. The prime example is to clean\n        the cache and remove images which are no longer of interest.\n        """'
newline|'\n'
name|'pass'
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
name|'instance_type'
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
string|'"""Transfers the disk of a running instance in multiple phases, turning\n           off the instance before the end.\n\n        :returns: disk_info dictionary that is passed as the\n                  disk_info parameter to finish_migration\n                  on the destination nova-compute host\n        """'
newline|'\n'
name|'src_host'
op|'='
name|'self'
op|'.'
name|'get_host_ip_addr'
op|'('
op|')'
newline|'\n'
name|'pvm_op'
op|'='
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'_operator'
newline|'\n'
name|'lpar_obj'
op|'='
name|'pvm_op'
op|'.'
name|'get_lpar'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'vhost'
op|'='
name|'pvm_op'
op|'.'
name|'get_vhost_by_instance_id'
op|'('
name|'lpar_obj'
op|'['
string|"'lpar_id'"
op|']'
op|')'
newline|'\n'
name|'diskname'
op|'='
name|'pvm_op'
op|'.'
name|'get_disk_name_by_vhost'
op|'('
name|'vhost'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_off'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'timeout'
op|'='
number|'120'
op|')'
newline|'\n'
nl|'\n'
name|'disk_info'
op|'='
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'migrate_disk'
op|'('
nl|'\n'
name|'diskname'
op|','
name|'src_host'
op|','
name|'dest'
op|','
name|'CONF'
op|'.'
name|'powervm_img_remote_path'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'disk_info'
op|'['
string|"'old_lv_size'"
op|']'
op|'='
name|'pvm_op'
op|'.'
name|'get_logical_vol_size'
op|'('
name|'diskname'
op|')'
newline|'\n'
name|'new_name'
op|'='
name|'self'
op|'.'
name|'_get_resize_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'pvm_op'
op|'.'
name|'rename_lpar'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'new_name'
op|')'
newline|'\n'
name|'return'
name|'disk_info'
newline|'\n'
nl|'\n'
DECL|member|_get_resize_name
dedent|''
name|'def'
name|'_get_resize_name'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rename the instance to be migrated to avoid naming conflicts\n\n        :param instance_name: name of instance to be migrated\n        :returns: the new instance name\n        """'
newline|'\n'
name|'name_tag'
op|'='
string|"'rsz_'"
newline|'\n'
nl|'\n'
comment|'# if the current name would overflow with new tag'
nl|'\n'
name|'if'
op|'('
op|'('
name|'len'
op|'('
name|'instance_name'
op|')'
op|'+'
name|'len'
op|'('
name|'name_tag'
op|')'
op|')'
op|'>'
number|'31'
op|')'
op|':'
newline|'\n'
comment|'# remove enough chars for the tag to fit'
nl|'\n'
indent|'            '
name|'num_chars'
op|'='
name|'len'
op|'('
name|'name_tag'
op|')'
newline|'\n'
name|'old_name'
op|'='
name|'instance_name'
op|'['
name|'num_chars'
op|':'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'old_name'
op|'='
name|'instance_name'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'name_tag'
op|','
name|'old_name'
op|']'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Completes a resize, turning on the migrated instance\n\n        :param network_info:\n           :py:meth:`~nova.network.manager.NetworkManager.get_instance_nw_info`\n        :param image_meta: image object returned by nova.image.glance that\n                           defines the image from which this instance\n                           was created\n        """'
newline|'\n'
name|'lpar_obj'
op|'='
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'_create_lpar_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'new_lv_size'
op|'='
name|'instance'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'root_gb'"
op|']'
newline|'\n'
name|'old_lv_size'
op|'='
name|'disk_info'
op|'['
string|"'old_lv_size'"
op|']'
newline|'\n'
name|'if'
string|"'root_disk_file'"
name|'in'
name|'disk_info'
op|':'
newline|'\n'
indent|'            '
name|'disk_size'
op|'='
name|'max'
op|'('
name|'int'
op|'('
name|'new_lv_size'
op|')'
op|','
name|'int'
op|'('
name|'old_lv_size'
op|')'
op|')'
newline|'\n'
name|'disk_size_bytes'
op|'='
name|'disk_size'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'deploy_from_migrated_file'
op|'('
nl|'\n'
name|'lpar_obj'
op|','
name|'disk_info'
op|'['
string|"'root_disk_file'"
op|']'
op|','
name|'disk_size_bytes'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# this shouldn't get hit unless someone forgot to handle"
nl|'\n'
comment|'# a certain migration type'
nl|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'Unrecognized root disk information: %s'"
op|')'
op|'%'
nl|'\n'
name|'disk_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|confirm_migration
dedent|''
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
string|'"""Confirms a resize, destroying the source VM."""'
newline|'\n'
nl|'\n'
name|'new_name'
op|'='
name|'self'
op|'.'
name|'_get_resize_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'destroy'
op|'('
name|'new_name'
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
string|'"""Finish reverting a resize, powering back on the instance."""'
newline|'\n'
nl|'\n'
comment|'# undo instance rename and start'
nl|'\n'
name|'new_name'
op|'='
name|'self'
op|'.'
name|'_get_resize_name'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'_operator'
op|'.'
name|'rename_lpar'
op|'('
name|'new_name'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_powervm'
op|'.'
name|'power_on'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
