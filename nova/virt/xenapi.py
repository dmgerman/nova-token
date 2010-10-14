begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nA connection to XenServer or Xen Cloud Platform.\n\nThe concurrency model for this class is as follows:\n\nAll XenAPI calls are on a thread (using t.i.t.deferToThread, via the decorator\ndeferredToThread).  They are remote calls, and so may hang for the usual\nreasons.  They should not be allowed to block the reactor thread.\n\nAll long-running XenAPI calls (VM.start, VM.reboot, etc) are called async\n(using XenAPI.VM.async_start etc).  These return a task, which can then be\npolled for completion.  Polling is handled using reactor.callLater.\n\nThis combination of techniques means that we don\'t block the reactor thread at\nall, and at the same time we don\'t hold lots of threads waiting for\nlong-running operations.\n\nFIXME: get_info currently doesn\'t conform to these rules, and will block the\nreactor thread if the VM.get_by_name_label or VM.get_record calls block.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'xmlrpclib'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'task'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'process'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'AuthManager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_url'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'URL for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Required if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_username'"
op|','
nl|'\n'
string|"'root'"
op|','
nl|'\n'
string|"'Username for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_password'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'Password for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'xenapi_task_poll_interval'"
op|','
nl|'\n'
number|'0.5'
op|','
nl|'\n'
string|"'The interval used for polling of remote tasks '"
nl|'\n'
string|"'(Async.VM.start, etc).  Used only if '"
nl|'\n'
string|"'connection_type=xenapi.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XENAPI_POWER_STATE
name|'XENAPI_POWER_STATE'
op|'='
op|'{'
nl|'\n'
string|"'Halted'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
string|"'Running'"
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
string|"'Paused'"
op|':'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
string|"'Suspended'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
comment|'# FIXME'
nl|'\n'
string|"'Crashed'"
op|':'
name|'power_state'
op|'.'
name|'CRASHED'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Note that XenAPI doesn\'t have a read-only connection mode, so\n    the read_only parameter is ignored."""'
newline|'\n'
comment|"# This is loaded late so that there's no need to install this"
nl|'\n'
comment|'# library when not using XenAPI.'
nl|'\n'
name|'global'
name|'XenAPI'
newline|'\n'
name|'if'
name|'XenAPI'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'       '
name|'XenAPI'
op|'='
name|'__import__'
op|'('
string|"'XenAPI'"
op|')'
newline|'\n'
dedent|''
name|'url'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
newline|'\n'
name|'username'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
newline|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
newline|'\n'
name|'if'
name|'not'
name|'url'
name|'or'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|"'Must specify xenapi_connection_url, xenapi_connection_username (optionally), and xenapi_connection_password to use connection_type=xenapi'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'XenAPIConnection'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIConnection
dedent|''
name|'class'
name|'XenAPIConnection'
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
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_conn'
op|'='
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
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
op|'['
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_name_label'
op|'('
name|'vm'
op|')'
name|'for'
name|'vm'
name|'in'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_all'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|spawn
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Attempted to create non-unique name %s'"
op|'%'
nl|'\n'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'None'
op|','
name|'instance'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_find_network_with_bridge'
op|'('
name|'network'
op|'.'
name|'bridge'
op|')'
newline|'\n'
nl|'\n'
name|'user'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'instance'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'project'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'instance'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'vdi_uuid'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_fetch_image'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'image_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'True'
op|')'
newline|'\n'
name|'kernel'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_fetch_image'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'kernel_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'False'
op|')'
newline|'\n'
name|'ramdisk'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_fetch_image'
op|'('
nl|'\n'
name|'instance'
op|'.'
name|'ramdisk_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'False'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'VDI.get_by_uuid'"
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'vm_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_create_vm'
op|'('
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_create_vbd'
op|'('
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
number|'0'
op|','
name|'True'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'_create_vif'
op|'('
name|'vm_ref'
op|','
name|'network_ref'
op|','
name|'instance'
op|'.'
name|'mac_address'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Starting VM %s...'"
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'VM.start'"
op|','
name|'vm_ref'
op|','
name|'False'
op|','
name|'False'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Spawning VM %s created %s.'"
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_create_vm
name|'def'
name|'_create_vm'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VM record.  Returns a Deferred that gives the new\n        VM reference."""'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'instance'
op|'.'
name|'instance_type'
op|']'
newline|'\n'
name|'mem'
op|'='
name|'str'
op|'('
name|'long'
op|'('
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'str'
op|'('
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'rec'
op|'='
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'is_a_template'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_static_min'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'memory_static_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_min'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'VCPUs_at_startup'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_max'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'actions_after_shutdown'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'actions_after_reboot'"
op|':'
string|"'restart'"
op|','
nl|'\n'
string|"'actions_after_crash'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'PV_bootloader'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_kernel'"
op|':'
name|'kernel'
op|','
nl|'\n'
string|"'PV_ramdisk'"
op|':'
name|'ramdisk'
op|','
nl|'\n'
string|"'PV_args'"
op|':'
string|"'root=/dev/xvda1'"
op|','
nl|'\n'
string|"'PV_bootloader_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_legacy_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_policy'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'platform'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'PCI_bus'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'recommendations'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'affinity'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'user_version'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VM %s...'"
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'VM.create'"
op|','
name|'rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VM %s as %s.'"
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_create_vbd
name|'def'
name|'_create_vbd'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
name|'userdevice'
op|','
name|'bootable'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VBD record.  Returns a Deferred that gives the new\n        VBD reference."""'
newline|'\n'
nl|'\n'
name|'vbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VDI'"
op|']'
op|'='
name|'vdi_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'='
name|'str'
op|'('
name|'userdevice'
op|')'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'bootable'"
op|']'
op|'='
name|'bootable'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'mode'"
op|']'
op|'='
string|"'RW'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'type'"
op|']'
op|'='
string|"'disk'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'unpluggable'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'empty'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_supported_algorithms'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Creating VBD for VM %s, VDI %s ... '"
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'vbd_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'VBD.create'"
op|','
name|'vbd_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VBD %s for VM %s, VDI %s.'"
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'vdi_ref'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_create_vif
name|'def'
name|'_create_vif'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'network_ref'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VIF record.  Returns a Deferred that gives the new\n        VIF reference."""'
newline|'\n'
nl|'\n'
name|'vif_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'device'"
op|']'
op|'='
string|"'0'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MAC'"
op|']'
op|'='
name|'mac_address'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MTU'"
op|']'
op|'='
string|"'1500'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Creating VIF for VM %s, network %s ... '"
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
name|'vif_ref'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'VIF.create'"
op|','
name|'vif_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VIF %s for VM %s, network %s.'"
op|','
name|'vif_ref'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'network_ref'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'vif_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_find_network_with_bridge
name|'def'
name|'_find_network_with_bridge'
op|'('
name|'self'
op|','
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expr'
op|'='
string|'\'field "bridge" = "%s"\''
op|'%'
name|'bridge'
newline|'\n'
name|'networks'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'network.get_all_records_where'"
op|','
nl|'\n'
name|'expr'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'networks'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'networks'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'networks'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Found non-unique network for bridge %s'"
op|'%'
name|'bridge'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'Found no network for bridge %s'"
op|'%'
name|'bridge'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_fetch_image
name|'def'
name|'_fetch_image'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'user'
op|','
name|'project'
op|','
name|'use_sr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""use_sr: True to put the image as a VDI in an SR, False to place\n        it on dom0\'s filesystem.  The former is for VM disks, the latter for\n        its kernel and ramdisk (if external kernels are being used).\n        Returns a Deferred that gives the new VDI UUID."""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'images'
op|'.'
name|'image_url'
op|'('
name|'image'
op|')'
newline|'\n'
name|'access'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Asking xapi to fetch %s as %s"'
op|'%'
op|'('
name|'url'
op|','
name|'access'
op|')'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'use_sr'
name|'and'
string|"'get_vdi'"
name|'or'
string|"'get_kernel'"
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'['
string|"'src_url'"
op|']'
op|'='
name|'url'
newline|'\n'
name|'args'
op|'['
string|"'username'"
op|']'
op|'='
name|'access'
newline|'\n'
name|'args'
op|'['
string|"'password'"
op|']'
op|'='
name|'user'
op|'.'
name|'secret'
newline|'\n'
name|'if'
name|'use_sr'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'add_partition'"
op|']'
op|'='
string|"'true'"
newline|'\n'
dedent|''
name|'task'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_async_call_plugin'
op|'('
string|"'objectstore'"
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|reboot
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'instance not present %s'"
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'Async.VM.clean_reboot'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_lookup'
op|'('
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|"# Don't complain, just return.  This lets us clean up instances"
nl|'\n'
comment|'# that have already disappeared from the underlying platform.'
nl|'\n'
indent|'            '
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'None'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'Async.VM.hard_shutdown'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_call_xenapi'
op|'('
string|"'Async.VM.destroy'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'self'
op|'.'
name|'_lookup_blocking'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'if'
name|'vm'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'instance not present %s'"
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'XENAPI_POWER_STATE'
op|'['
name|'rec'
op|'['
string|"'power_state'"
op|']'
op|']'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'long'
op|'('
name|'rec'
op|'['
string|"'memory_static_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'long'
op|'('
name|'rec'
op|'['
string|"'memory_dynamic_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'rec'
op|'['
string|"'VCPUs_max'"
op|']'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
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
name|'return'
string|"'FAKE CONSOLE OUTPUT'"
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|_lookup
name|'def'
name|'_lookup'
op|'('
name|'self'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_lookup_blocking'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_lookup_blocking
dedent|''
name|'def'
name|'_lookup_blocking'
op|'('
name|'self'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vms'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_by_name_label'
op|'('
name|'i'
op|')'
newline|'\n'
name|'n'
op|'='
name|'len'
op|'('
name|'vms'
op|')'
newline|'\n'
name|'if'
name|'n'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'n'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'duplicate name found: %s'"
op|'%'
name|'i'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_task
dedent|''
dedent|''
name|'def'
name|'_wait_for_task'
op|'('
name|'self'
op|','
name|'task'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a Deferred that will give the result of the given task.\n        The task is polled until it completes."""'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'callLater'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'task'
op|','
name|'d'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|_poll_task
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'task'
op|','
name|'deferred'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll the given XenAPI task, and fire the given Deferred if we\n        get a result."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|"#logging.debug('Polling task %s...', task)"
nl|'\n'
indent|'            '
name|'status'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_status'
op|'('
name|'task'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|"'pending'"
op|':'
newline|'\n'
indent|'                '
name|'reactor'
op|'.'
name|'callLater'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_task_poll_interval'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'task'
op|','
name|'deferred'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'status'
op|'=='
string|"'success'"
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_result'
op|'('
name|'task'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'info'
op|'('
string|"'Task %s status: success.  %s'"
op|','
name|'task'
op|','
name|'result'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'callback'
op|'('
name|'_parse_xmlrpc_value'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'error_info'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_error_info'
op|'('
name|'task'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'warn'
op|'('
string|"'Task %s status: %s.  %s'"
op|','
name|'task'
op|','
name|'status'
op|','
nl|'\n'
name|'error_info'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\n'
comment|"#logging.debug('Polling task %s done.', task)"
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'deferred'
op|'.'
name|'errback'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|_call_xenapi
name|'def'
name|'_call_xenapi'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the specified XenAPI method on a background thread.  Returns\n        a Deferred for the result."""'
newline|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'method'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'f'
op|'.'
name|'__getattr__'
op|'('
name|'m'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'deferredToThread'
newline|'\n'
DECL|member|_async_call_plugin
name|'def'
name|'_async_call_plugin'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call Async.host.call_plugin on a background thread.  Returns a\n        Deferred with the task reference."""'
newline|'\n'
name|'return'
name|'_unwrap_plugin_exceptions'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'Async'
op|'.'
name|'host'
op|'.'
name|'call_plugin'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_xenapi_host'
op|'('
op|')'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_xenapi_host
dedent|''
name|'def'
name|'_get_xenapi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'handle'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unwrap_plugin_exceptions
dedent|''
dedent|''
name|'def'
name|'_unwrap_plugin_exceptions'
op|'('
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Got exception: %s"'
op|','
name|'exc'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'exc'
op|'.'
name|'details'
op|')'
op|'=='
number|'4'
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'XENAPI_PLUGIN_EXCEPTION'"
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'2'
op|']'
op|'=='
string|"'Failure'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'eval'
op|'('
name|'exc'
op|'.'
name|'details'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
newline|'\n'
dedent|''
name|'raise'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'xmlrpclib'
op|'.'
name|'ProtocolError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Got exception: %s"'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_xmlrpc_value
dedent|''
dedent|''
name|'def'
name|'_parse_xmlrpc_value'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the given value as if it were an XML-RPC value.  This is\n    sometimes used as the format for the task.result field."""'
newline|'\n'
name|'if'
name|'not'
name|'val'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'val'
newline|'\n'
dedent|''
name|'x'
op|'='
name|'xmlrpclib'
op|'.'
name|'loads'
op|'('
nl|'\n'
string|'\'<?xml version="1.0"?><methodResponse><params><param>\''
op|'+'
nl|'\n'
name|'val'
op|'+'
nl|'\n'
string|"'</param></params></methodResponse>'"
op|')'
newline|'\n'
name|'return'
name|'x'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
