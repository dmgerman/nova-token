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
string|'"""\nManagement class for VM-related functions (spawn, reboot, etc).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
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
nl|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
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
name|'global'
name|'XenAPI'
newline|'\n'
name|'if'
name|'XenAPI'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'XenAPI'
op|'='
name|'__import__'
op|'('
string|"'XenAPI'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
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
string|'""" List VM instances """'
newline|'\n'
name|'return'
op|'['
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
name|'get_name_label'
op|'('
name|'vm'
op|')'
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
string|'""" Create VM instance """'
newline|'\n'
name|'vm'
op|'='
name|'yield'
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
name|'bridge'
op|'='
name|'db'
op|'.'
name|'project_get_network'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'.'
name|'project_id'
op|')'
op|'.'
name|'bridge'
newline|'\n'
name|'network_ref'
op|'='
name|'yield'
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
name|'vdi_uuid'
op|'='
name|'yield'
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
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
name|'True'
op|')'
newline|'\n'
name|'kernel'
op|'='
name|'yield'
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
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
name|'False'
op|')'
newline|'\n'
name|'ramdisk'
op|'='
name|'yield'
name|'VMHelper'
op|'.'
name|'fetch_image'
op|'('
name|'self'
op|'.'
name|'_session'
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
name|'False'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'yield'
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
name|'vm_ref'
op|'='
name|'yield'
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
op|')'
newline|'\n'
name|'yield'
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
name|'if'
name|'network_ref'
op|':'
newline|'\n'
indent|'            '
name|'yield'
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
nl|'\n'
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
string|'""" Reboot VM instance """'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'vm'
op|'='
name|'yield'
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
string|"'instance not present %s'"
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'task'
op|'='
name|'yield'
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
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
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
string|'""" Destroy VM instance """'
newline|'\n'
name|'vm'
op|'='
name|'yield'
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
comment|'# Get the VDIs related to the VM'
nl|'\n'
dedent|''
name|'vdis'
op|'='
name|'yield'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'='
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.hard_shutdown'"
op|','
nl|'\n'
name|'vm'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
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
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
comment|'# Disk clean-up'
nl|'\n'
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
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VDI.destroy'"
op|','
nl|'\n'
name|'vdi'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
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
indent|'                    '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
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
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VM.destroy'"
op|','
name|'vm'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
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
string|'""" Return data about VM instance """'
newline|'\n'
name|'vm'
op|'='
name|'VMHelper'
op|'.'
name|'lookup_blocking'
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
string|'""" Return snapshot of console """'
newline|'\n'
comment|'# TODO: implement this to fix pylint!'
nl|'\n'
name|'return'
string|"'FAKE CONSOLE OUTPUT of instance'"
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
