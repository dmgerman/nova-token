begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nManagement class for VM-related functions (spawn, reboot, etc).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
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
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'network_utils'
name|'import'
name|'NetworkHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
name|'import'
name|'VMHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
name|'import'
name|'ImageType'
newline|'\n'
nl|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi.vmops"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMOps
name|'class'
name|'VMOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Management class for VM-related tasks\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'session'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
name|'VMHelper'
op|'.'
name|'XenAPI'
op|'='
name|'self'
op|'.'
name|'XenAPI'
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
string|'"""List VM instances"""'
newline|'\n'
name|'vms'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'rec'
op|'['
string|'"is_a_template"'
op|']'
name|'and'
name|'not'
name|'rec'
op|'['
string|'"is_control_domain"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'vms'
op|'.'
name|'append'
op|'('
name|'rec'
op|'['
string|'"name_label"'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'vms'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
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
string|'"""Create VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
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
name|'exception'
op|'.'
name|'Duplicate'
op|'('
name|'_'
op|'('
string|"'Attempted to create'"
nl|'\n'
string|"' non-unique name %s'"
op|')'
op|'%'
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bridge'
op|'='
name|'db'
op|'.'
name|'network_get_by_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
op|'['
string|"'bridge'"
op|']'
newline|'\n'
name|'network_ref'
op|'='
name|'NetworkHelper'
op|'.'
name|'find_network_with_bridge'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
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
comment|'#if kernel is not present we must download a raw disk'
nl|'\n'
name|'if'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'disk_image_type'
op|'='
name|'ImageType'
op|'.'
name|'DISK'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'disk_image_type'
op|'='
name|'ImageType'
op|'.'
name|'DISK_RAW'
newline|'\n'
dedent|''
name|'vdi_uuid'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'image_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'disk_image_type'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VDI.get_by_uuid'"
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
comment|'#Have a look at the VDI and see if it has a PV kernel'
nl|'\n'
name|'pv_kernel'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'pv_kernel'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'kernel'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'kernel_id'
op|':'
newline|'\n'
indent|'            '
name|'kernel'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'kernel_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|')'
newline|'\n'
dedent|''
name|'ramdisk'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'instance'
op|'.'
name|'ramdisk_id'
op|':'
newline|'\n'
indent|'            '
name|'ramdisk'
op|'='
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'ramdisk_id'
op|','
name|'user'
op|','
name|'project'
op|','
name|'ImageType'
op|'.'
name|'KERNEL_RAMDISK'
op|')'
newline|'\n'
dedent|''
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'create_vm'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|','
name|'pv_kernel'
op|')'
newline|'\n'
name|'VMHelper'
op|'.'
name|'create_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
number|'0'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'            '
name|'VMHelper'
op|'.'
name|'create_vif'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'network_ref'
op|','
name|'instance'
op|'.'
name|'mac_address'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Starting VM %s...'"
op|')'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Spawning VM %s created %s.'"
op|')'
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(armando): Do we really need to do this in virt?'
nl|'\n'
name|'timer'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'f'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_wait_for_boot
name|'def'
name|'_wait_for_boot'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'state'
op|'='
name|'self'
op|'.'
name|'get_info'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
op|'['
string|"'state'"
op|']'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'state'
op|')'
newline|'\n'
name|'if'
name|'state'
op|'=='
name|'power_state'
op|'.'
name|'RUNNING'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Instance %s: booted'"
op|')'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'instance %s: failed to boot'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_set_state'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'timer'
op|'.'
name|'f'
op|'='
name|'_wait_for_boot'
newline|'\n'
name|'return'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_vm_opaque_ref
dedent|''
name|'def'
name|'_get_vm_opaque_ref'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Refactored out the common code of many methods that receive either\n        a vm name or a vm instance, and want a vm instance in return.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_name'
op|'='
name|'instance_or_vm'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|'# A vm opaque ref was passed'
nl|'\n'
indent|'            '
name|'vm'
op|'='
name|'instance_or_vm'
newline|'\n'
dedent|''
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
name|'_'
op|'('
string|"'Instance not present %s'"
op|')'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'vm'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create snapshot from a running VM instance\n\n        :param instance: instance to be snapshotted\n        :param name: name/label to be given to the snapshot\n\n        Steps involved in a XenServer snapshot:\n\n        1. XAPI-Snapshot: Snapshotting the instance using XenAPI. This\n            creates: Snapshot (Template) VM, Snapshot VBD, Snapshot VDI,\n            Snapshot VHD\n\n        2. Wait-for-coalesce: The Snapshot VDI and Instance VDI both point to\n            a \'base-copy\' VDI.  The base_copy is immutable and may be chained\n            with other base_copies.  If chained, the base_copies\n            coalesce together, so, we must wait for this coalescing to occur to\n            get a stable representation of the data on disk.\n\n        3. Push-to-glance: Once coalesced, we call a plugin on the XenServer\n            that will bundle the VHDs together and then push the bundle into\n            Glance.\n        """'
newline|'\n'
nl|'\n'
comment|'#TODO(sirp): Add quiesce and VSS locking support when Windows support'
nl|'\n'
comment|'# is added'
nl|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting snapshot for VM %s"'
op|')'
op|','
name|'instance'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
name|'label'
op|'='
string|'"%s-snapshot"'
op|'%'
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'template_vm_ref'
op|','
name|'template_vdi_uuids'
op|'='
name|'VMHelper'
op|'.'
name|'create_snapshot'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
name|'vm_ref'
op|','
name|'label'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unable to Snapshot %s: %s"'
op|')'
op|','
name|'vm_ref'
op|','
name|'exc'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# call plugin to ship snapshot off to glance'
nl|'\n'
indent|'            '
name|'VMHelper'
op|'.'
name|'upload_image'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'id'
op|','
name|'template_vdi_uuids'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
name|'template_vm_ref'
op|','
name|'shutdown'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Finished snapshot and upload for VM %s"'
op|')'
op|','
name|'instance'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reboot VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.clean_reboot'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
name|'vm'
op|','
name|'shutdown'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_destroy
dedent|''
name|'def'
name|'_destroy'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vm'
op|','
name|'shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Destroy VM instance """'
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
name|'return'
newline|'\n'
comment|'# Get the VDIs related to the VM'
nl|'\n'
dedent|''
name|'vdis'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_vm_vdis'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm'
op|')'
newline|'\n'
name|'if'
name|'shutdown'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.hard_shutdown'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
comment|'# Disk clean-up'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'vdis'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vdi'
name|'in'
name|'vdis'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VDI.destroy'"
op|','
name|'vdi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
comment|'# VM Destroy'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.destroy'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wait_with_callback
dedent|''
dedent|''
name|'def'
name|'_wait_with_callback'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'task'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'instance_id'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'callback'
op|'('
name|'ret'
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
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pause VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.pause'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|','
name|'callback'
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
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unpause VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.unpause'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'instance'
op|'.'
name|'id'
op|','
name|'task'
op|','
name|'callback'
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
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""suspend the specified instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
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
name|'_'
op|'('
string|'"suspend: instance not present %s"'
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.suspend'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'task'
op|','
name|'callback'
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
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""resume the specified instance"""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
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
name|'_'
op|'('
string|'"resume: instance not present %s"'
op|')'
op|'%'
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.resume'"
op|','
name|'vm'
op|','
name|'False'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_wait_with_callback'
op|'('
name|'task'
op|','
name|'callback'
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
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM instance"""'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
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
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance not'"
nl|'\n'
string|"' found %s'"
op|')'
op|'%'
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'compile_info'
op|'('
name|'rec'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM diagnostics"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'compile_diagnostics'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'rec'
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
string|'"""Return snapshot of console"""'
newline|'\n'
comment|'# TODO: implement this to fix pylint!'
nl|'\n'
name|'return'
string|"'FAKE CONSOLE OUTPUT of instance'"
newline|'\n'
nl|'\n'
DECL|member|list_from_xenstore
dedent|''
name|'def'
name|'list_from_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Runs the xenstore-ls command to get a listing of all records\n        from \'path\' downward. Returns a dict with the sub-paths as keys,\n        and the value stored in those paths as values. If nothing is\n        found at that path, returns None.\n        """'
newline|'\n'
name|'ret'
op|'='
name|'self'
op|'.'
name|'_make_xenstore_call'
op|'('
string|"'list_records'"
op|','
name|'vm'
op|','
name|'path'
op|')'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
nl|'\n'
DECL|member|read_from_xenstore
dedent|''
name|'def'
name|'read_from_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the value stored in the xenstore record for the given VM\n        at the specified location. A XenAPIPlugin.PluginError will be raised\n        if any error is encountered in the read process.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'self'
op|'.'
name|'_make_xenstore_call'
op|'('
string|"'read_record'"
op|','
name|'vm'
op|','
name|'path'
op|','
nl|'\n'
op|'{'
string|"'ignore_missing_path'"
op|':'
string|"'True'"
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'ret'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
name|'if'
name|'ret'
op|'=='
string|'"None"'
op|':'
newline|'\n'
comment|"# Can't marshall None over RPC calls."
nl|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|write_to_xenstore
dedent|''
name|'def'
name|'write_to_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Writes the passed value to the xenstore record for the given VM\n        at the specified location. A XenAPIPlugin.PluginError will be raised\n        if any error is encountered in the write process.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_xenstore_call'
op|'('
string|"'write_record'"
op|','
name|'vm'
op|','
name|'path'
op|','
nl|'\n'
op|'{'
string|"'value'"
op|':'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear_xenstore
dedent|''
name|'def'
name|'clear_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes the VM\'s xenstore record for the specified path.\n        If there is no such record, the request is ignored.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_make_xenstore_call'
op|'('
string|"'delete_record'"
op|','
name|'vm'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_xenstore_call
dedent|''
name|'def'
name|'_make_xenstore_call'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'addl_args'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Handles calls to the xenstore xenapi plugin."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_make_plugin_call'
op|'('
string|"'xenstore.py'"
op|','
name|'method'
op|'='
name|'method'
op|','
name|'vm'
op|'='
name|'vm'
op|','
nl|'\n'
name|'path'
op|'='
name|'path'
op|','
name|'addl_args'
op|'='
name|'addl_args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_plugin_call
dedent|''
name|'def'
name|'_make_plugin_call'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'method'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'addl_args'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Abstracts out the process of calling a method of a xenapi plugin.\n        Any errors raised by the plugin will in turn raise a RuntimeError here.\n        """'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'rec'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'args'
op|'='
op|'{'
string|"'dom_id'"
op|':'
name|'rec'
op|'['
string|"'domid'"
op|']'
op|','
string|"'path'"
op|':'
name|'path'
op|'}'
newline|'\n'
name|'args'
op|'.'
name|'update'
op|'('
name|'addl_args'
op|')'
newline|'\n'
comment|"# If the 'testing_mode' attribute is set, add that to the args."
nl|'\n'
name|'if'
name|'getattr'
op|'('
name|'self'
op|','
string|"'testing_mode'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'testing_mode'"
op|']'
op|'='
string|"'true'"
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'async_call_plugin'
op|'('
name|'plugin'
op|','
name|'method'
op|','
name|'args'
op|')'
newline|'\n'
name|'ret'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
number|'0'
op|','
name|'task'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"%s"'
op|'%'
name|'e'
op|'.'
name|'details'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|add_to_xenstore
dedent|''
name|'def'
name|'add_to_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds the passed key/value pair to the xenstore record for\n        the given VM at the specified location. A XenAPIPlugin.PluginError\n        will be raised if any error is encountered in the write process.\n        """'
newline|'\n'
name|'current'
op|'='
name|'self'
op|'.'
name|'read_from_xenstore'
op|'('
name|'vm'
op|','
name|'path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'current'
op|':'
newline|'\n'
comment|'# Nothing at that location'
nl|'\n'
indent|'            '
name|'current'
op|'='
op|'{'
name|'key'
op|':'
name|'value'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'current'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'write_to_xenstore'
op|'('
name|'vm'
op|','
name|'path'
op|','
name|'current'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_xenstore
dedent|''
name|'def'
name|'remove_from_xenstore'
op|'('
name|'self'
op|','
name|'vm'
op|','
name|'path'
op|','
name|'key_or_keys'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Takes either a single key or a list of keys and removes\n        them from the xenstoreirecord data for the given VM.\n        If the key doesn\'t exist, the request is ignored.\n        """'
newline|'\n'
name|'current'
op|'='
name|'self'
op|'.'
name|'list_from_xenstore'
op|'('
name|'vm'
op|','
name|'path'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'current'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'key_or_keys'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
op|'['
name|'key_or_keys'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
name|'key_or_keys'
newline|'\n'
dedent|''
name|'keys'
op|'.'
name|'sort'
op|'('
name|'lambda'
name|'x'
op|','
name|'y'
op|':'
name|'cmp'
op|'('
name|'y'
op|'.'
name|'count'
op|'('
string|"'/'"
op|')'
op|','
name|'x'
op|'.'
name|'count'
op|'('
string|"'/'"
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|':'
newline|'\n'
indent|'                '
name|'keypath'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'path'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'keypath'
op|'='
name|'key'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_make_xenstore_call'
op|'('
string|"'delete_record'"
op|','
name|'vm'
op|','
name|'keypath'
op|')'
newline|'\n'
nl|'\n'
comment|'########################################################################'
nl|'\n'
comment|'###### The following methods interact with the xenstore parameter'
nl|'\n'
comment|'###### record, not the live xenstore. They were created before I'
nl|'\n'
comment|'###### knew the difference, and are left in here in case they prove'
nl|'\n'
comment|"###### to be useful. They all have '_param' added to their method"
nl|'\n'
comment|'###### names to distinguish them. (dabo)'
nl|'\n'
comment|'########################################################################'
nl|'\n'
DECL|member|read_partial_from_param_xenstore
dedent|''
dedent|''
name|'def'
name|'read_partial_from_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|','
name|'key_prefix'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict of all the keys in the xenstore parameter record\n        for the given instance that begin with the key_prefix.\n        """'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'read_from_param_xenstore'
op|'('
name|'instance_or_vm'
op|')'
newline|'\n'
name|'badkeys'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
nl|'\n'
name|'if'
name|'not'
name|'k'
op|'.'
name|'startswith'
op|'('
name|'key_prefix'
op|')'
op|']'
newline|'\n'
name|'for'
name|'badkey'
name|'in'
name|'badkeys'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'data'
op|'['
name|'badkey'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|read_from_param_xenstore
dedent|''
name|'def'
name|'read_from_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|','
name|'keys'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the xenstore parameter record data for the specified VM\n        instance as a dict. Accepts an optional key or list of keys; if a\n        value for \'keys\' is passed, the returned dict is filtered to only\n        return the values for those keys.\n        """'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance_or_vm'
op|')'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi_request'
op|'('
string|"'VM.get_xenstore_data'"
op|','
nl|'\n'
op|'('
name|'vm'
op|','
op|')'
op|')'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'keys'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'keys'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
op|'['
name|'keys'
op|']'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'raw'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'raw'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'['
name|'key'
op|']'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'raw'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'['
name|'key'
op|']'
op|'='
name|'raw'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|add_to_param_xenstore
dedent|''
name|'def'
name|'add_to_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|','
name|'key'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Takes a key/value pair and adds it to the xenstore parameter\n        record for the given vm instance. If the key exists in xenstore,\n        it is overwritten"""'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance_or_vm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remove_from_param_xenstore'
op|'('
name|'instance_or_vm'
op|','
name|'key'
op|')'
newline|'\n'
name|'jsonval'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'val'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi_request'
op|'('
string|"'VM.add_to_xenstore_data'"
op|','
nl|'\n'
op|'('
name|'vm'
op|','
name|'key'
op|','
name|'jsonval'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write_to_param_xenstore
dedent|''
name|'def'
name|'write_to_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Takes a dict and writes each key/value pair to the xenstore\n        parameter record for the given vm instance. Any existing data for\n        those keys is overwritten.\n        """'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'mapping'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'add_to_param_xenstore'
op|'('
name|'instance_or_vm'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_from_param_xenstore
dedent|''
dedent|''
name|'def'
name|'remove_from_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|','
name|'key_or_keys'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Takes either a single key or a list of keys and removes\n        them from the xenstore parameter record data for the given VM.\n        If the key doesn\'t exist, the request is ignored.\n        """'
newline|'\n'
name|'vm'
op|'='
name|'self'
op|'.'
name|'_get_vm_opaque_ref'
op|'('
name|'instance_or_vm'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'key_or_keys'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
op|'['
name|'key_or_keys'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
name|'key_or_keys'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi_request'
op|'('
string|"'VM.remove_from_xenstore_data'"
op|','
nl|'\n'
op|'('
name|'vm'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear_param_xenstore
dedent|''
dedent|''
name|'def'
name|'clear_param_xenstore'
op|'('
name|'self'
op|','
name|'instance_or_vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes all data from the xenstore parameter record for this VM."""'
newline|'\n'
name|'self'
op|'.'
name|'write_to_param_xenstore'
op|'('
name|'instance_or_vm'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
comment|'########################################################################'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
