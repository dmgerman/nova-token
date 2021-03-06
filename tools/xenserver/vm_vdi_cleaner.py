begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'# you may not use this file except in compliance with the License.'
nl|'\n'
comment|'# You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'# See the License for the specific language governing permissions and'
nl|'\n'
comment|'# limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""vm_vdi_cleaner.py - List or clean orphaned VDIs/instances on XenServer."""'
newline|'\n'
nl|'\n'
name|'import'
name|'doctest'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'XenAPI'
newline|'\n'
nl|'\n'
DECL|variable|possible_topdir
name|'possible_topdir'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'possible_topdir'
op|','
string|'"nova"'
op|','
string|'"__init__.py"'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'possible_topdir'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'virtapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'driver'
name|'as'
name|'xenapi_driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cleaner_opts
name|'cleaner_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'zombie_instance_updated_at_window'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'172800'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds zombie instances are cleaned up.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cli_opt
name|'cli_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'command'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cleaner command'"
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
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'cleaner_opts'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_cli_opt'
op|'('
name|'cli_opt'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'verbose'"
op|','
string|"'nova.openstack.common.log'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALLOWED_COMMANDS
name|'ALLOWED_COMMANDS'
op|'='
op|'['
string|'"list-vdis"'
op|','
string|'"clean-vdis"'
op|','
string|'"list-instances"'
op|','
nl|'\n'
string|'"clean-instances"'
op|','
string|'"test"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call_xenapi
name|'def'
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a call to xapi."""'
newline|'\n'
name|'return'
name|'xenapi'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
name|'method'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_orphaned_instances
dedent|''
name|'def'
name|'find_orphaned_instances'
op|'('
name|'xenapi'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find and return a list of orphaned instances."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
string|'"only"'
op|')'
newline|'\n'
nl|'\n'
name|'orphaned_instances'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
name|'in'
name|'_get_applicable_vm_recs'
op|'('
name|'xenapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'uuid'
op|'='
name|'vm_rec'
op|'['
string|"'other_config'"
op|']'
op|'['
string|"'nova_uuid'"
op|']'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'exception'
op|'.'
name|'InstanceNotFound'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(jk0): Err on the side of caution here. If we don't know"
nl|'\n'
comment|'# anything about the particular instance, ignore it.'
nl|'\n'
indent|'            '
name|'print_xen_object'
op|'('
string|'"INFO: Ignoring VM"'
op|','
name|'vm_rec'
op|','
name|'indent_level'
op|'='
number|'0'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
comment|'# NOTE(jk0): This would be triggered if a VM was deleted but the'
nl|'\n'
comment|'# actual deletion process failed somewhere along the line.'
nl|'\n'
dedent|''
name|'is_active_and_deleting'
op|'='
op|'('
name|'instance'
op|'.'
name|'vm_state'
op|'=='
string|'"active"'
name|'and'
nl|'\n'
name|'instance'
op|'.'
name|'task_state'
op|'=='
string|'"deleting"'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(jk0): A zombie VM is an instance that is not active and hasn't"
nl|'\n'
comment|'# been updated in over the specified period.'
nl|'\n'
name|'is_zombie_vm'
op|'='
op|'('
name|'instance'
op|'.'
name|'vm_state'
op|'!='
string|'"active"'
nl|'\n'
name|'and'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
name|'instance'
op|'.'
name|'updated_at'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'zombie_instance_updated_at_window'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'is_active_and_deleting'
name|'or'
name|'is_zombie_vm'
op|':'
newline|'\n'
indent|'            '
name|'orphaned_instances'
op|'.'
name|'append'
op|'('
op|'('
name|'vm_ref'
op|','
name|'vm_rec'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'orphaned_instances'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup_instance
dedent|''
name|'def'
name|'cleanup_instance'
op|'('
name|'xenapi'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'vm_rec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete orphaned instances."""'
newline|'\n'
name|'xenapi'
op|'.'
name|'_vmops'
op|'.'
name|'_destroy'
op|'('
name|'instance'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_applicable_vm_recs
dedent|''
name|'def'
name|'_get_applicable_vm_recs'
op|'('
name|'xenapi'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An \'applicable\' VM is one that is not a template and not the control\n    domain.\n    """'
newline|'\n'
name|'for'
name|'vm_ref'
name|'in'
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VM.get_all'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_rec'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VM.get_record'"
op|','
name|'vm_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vm_rec'
op|'['
string|'"is_a_template"'
op|']'
name|'or'
name|'vm_rec'
op|'['
string|'"is_control_domain"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'yield'
name|'vm_ref'
op|','
name|'vm_rec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|print_xen_object
dedent|''
dedent|''
name|'def'
name|'print_xen_object'
op|'('
name|'obj_type'
op|','
name|'obj'
op|','
name|'indent_level'
op|'='
number|'0'
op|','
name|'spaces_per_indent'
op|'='
number|'4'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pretty-print a Xen object.\n\n    Looks like:\n\n        VM (abcd-abcd-abcd): \'name label here\'\n    """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'uuid'
op|'='
name|'obj'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'name_label'
op|'='
name|'obj'
op|'['
string|'"name_label"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'        '
name|'name_label'
op|'='
string|'""'
newline|'\n'
dedent|''
name|'msg'
op|'='
string|'"%(obj_type)s (%(uuid)s) \'%(name_label)s\'"'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'indent'
op|'='
string|'" "'
op|'*'
name|'spaces_per_indent'
op|'*'
name|'indent_level'
newline|'\n'
name|'print'
string|'""'
op|'.'
name|'join'
op|'('
op|'['
name|'indent'
op|','
name|'msg'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_vdis_connected_to_vm
dedent|''
name|'def'
name|'_find_vdis_connected_to_vm'
op|'('
name|'xenapi'
op|','
name|'connected_vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find VDIs which are connected to VBDs which are connected to VMs."""'
newline|'\n'
DECL|function|_is_null_ref
name|'def'
name|'_is_null_ref'
op|'('
name|'ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ref'
op|'=='
string|'"OpaqueRef:NULL"'
newline|'\n'
nl|'\n'
DECL|function|_add_vdi_and_parents_to_connected
dedent|''
name|'def'
name|'_add_vdi_and_parents_to_connected'
op|'('
name|'vdi_rec'
op|','
name|'indent_level'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'indent_level'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
name|'vdi_and_parent_uuids'
op|'='
op|'['
op|']'
newline|'\n'
name|'cur_vdi_rec'
op|'='
name|'vdi_rec'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'cur_vdi_uuid'
op|'='
name|'cur_vdi_rec'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
name|'print_xen_object'
op|'('
string|'"VDI"'
op|','
name|'vdi_rec'
op|','
name|'indent_level'
op|'='
name|'indent_level'
op|')'
newline|'\n'
name|'connected_vdi_uuids'
op|'.'
name|'add'
op|'('
name|'cur_vdi_uuid'
op|')'
newline|'\n'
name|'vdi_and_parent_uuids'
op|'.'
name|'append'
op|'('
name|'cur_vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'parent_vdi_uuid'
op|'='
name|'vdi_rec'
op|'['
string|'"sm_config"'
op|']'
op|'['
string|'"vhd-parent"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'parent_vdi_uuid'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|"# NOTE(sirp): VDI's can have themselves as a parent?!"
nl|'\n'
dedent|''
name|'if'
name|'parent_vdi_uuid'
name|'and'
name|'parent_vdi_uuid'
op|'!='
name|'cur_vdi_uuid'
op|':'
newline|'\n'
indent|'                '
name|'indent_level'
op|'+='
number|'1'
newline|'\n'
name|'cur_vdi_ref'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_by_uuid'"
op|','
nl|'\n'
name|'parent_vdi_uuid'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'cur_vdi_rec'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_record'"
op|','
nl|'\n'
name|'cur_vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
dedent|''
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
dedent|''
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
name|'in'
name|'_get_applicable_vm_recs'
op|'('
name|'xenapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'indent_level'
op|'='
number|'0'
newline|'\n'
name|'print_xen_object'
op|'('
string|'"VM"'
op|','
name|'vm_rec'
op|','
name|'indent_level'
op|'='
name|'indent_level'
op|')'
newline|'\n'
nl|'\n'
name|'vbd_refs'
op|'='
name|'vm_rec'
op|'['
string|'"VBDs"'
op|']'
newline|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'vbd_rec'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VBD.get_record'"
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'indent_level'
op|'='
number|'1'
newline|'\n'
name|'print_xen_object'
op|'('
string|'"VBD"'
op|','
name|'vbd_rec'
op|','
name|'indent_level'
op|'='
name|'indent_level'
op|')'
newline|'\n'
nl|'\n'
name|'vbd_vdi_ref'
op|'='
name|'vbd_rec'
op|'['
string|'"VDI"'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'_is_null_ref'
op|'('
name|'vbd_vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'vdi_rec'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_record'"
op|','
name|'vbd_vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'_add_vdi_and_parents_to_connected'
op|'('
name|'vdi_rec'
op|','
name|'indent_level'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_all_vdis_and_system_vdis
dedent|''
dedent|''
dedent|''
name|'def'
name|'_find_all_vdis_and_system_vdis'
op|'('
name|'xenapi'
op|','
name|'all_vdi_uuids'
op|','
name|'connected_vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Collects all VDIs and adds system VDIs to the connected set."""'
newline|'\n'
DECL|function|_system_owned
name|'def'
name|'_system_owned'
op|'('
name|'vdi_rec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vdi_name'
op|'='
name|'vdi_rec'
op|'['
string|'"name_label"'
op|']'
newline|'\n'
name|'return'
op|'('
name|'vdi_name'
op|'.'
name|'startswith'
op|'('
string|'"USB"'
op|')'
name|'or'
nl|'\n'
name|'vdi_name'
op|'.'
name|'endswith'
op|'('
string|'".iso"'
op|')'
name|'or'
nl|'\n'
name|'vdi_rec'
op|'['
string|'"type"'
op|']'
op|'=='
string|'"system"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'vdi_ref'
name|'in'
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_all'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdi_rec'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_record'"
op|','
name|'vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'!='
string|"'HANDLE_INVALID'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'continue'
newline|'\n'
dedent|''
name|'vdi_uuid'
op|'='
name|'vdi_rec'
op|'['
string|'"uuid"'
op|']'
newline|'\n'
name|'all_vdi_uuids'
op|'.'
name|'add'
op|'('
name|'vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
comment|"# System owned and non-managed VDIs should be considered 'connected'"
nl|'\n'
comment|'# for our purposes.'
nl|'\n'
name|'if'
name|'_system_owned'
op|'('
name|'vdi_rec'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'print_xen_object'
op|'('
string|'"SYSTEM VDI"'
op|','
name|'vdi_rec'
op|','
name|'indent_level'
op|'='
number|'0'
op|')'
newline|'\n'
name|'connected_vdi_uuids'
op|'.'
name|'add'
op|'('
name|'vdi_uuid'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'vdi_rec'
op|'['
string|'"managed"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'print_xen_object'
op|'('
string|'"UNMANAGED VDI"'
op|','
name|'vdi_rec'
op|','
name|'indent_level'
op|'='
number|'0'
op|')'
newline|'\n'
name|'connected_vdi_uuids'
op|'.'
name|'add'
op|'('
name|'vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_orphaned_vdi_uuids
dedent|''
dedent|''
dedent|''
name|'def'
name|'find_orphaned_vdi_uuids'
op|'('
name|'xenapi'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Walk VM -> VBD -> VDI change and accumulate connected VDIs."""'
newline|'\n'
name|'connected_vdi_uuids'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'_find_vdis_connected_to_vm'
op|'('
name|'xenapi'
op|','
name|'connected_vdi_uuids'
op|')'
newline|'\n'
nl|'\n'
name|'all_vdi_uuids'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'_find_all_vdis_and_system_vdis'
op|'('
name|'xenapi'
op|','
name|'all_vdi_uuids'
op|','
name|'connected_vdi_uuids'
op|')'
newline|'\n'
nl|'\n'
name|'orphaned_vdi_uuids'
op|'='
name|'all_vdi_uuids'
op|'-'
name|'connected_vdi_uuids'
newline|'\n'
name|'return'
name|'orphaned_vdi_uuids'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_orphaned_vdis
dedent|''
name|'def'
name|'list_orphaned_vdis'
op|'('
name|'vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""List orphaned VDIs."""'
newline|'\n'
name|'for'
name|'vdi_uuid'
name|'in'
name|'vdi_uuids'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"ORPHANED VDI (%s)"'
op|'%'
name|'vdi_uuid'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'vdi_uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clean_orphaned_vdis
dedent|''
dedent|''
dedent|''
name|'def'
name|'clean_orphaned_vdis'
op|'('
name|'xenapi'
op|','
name|'vdi_uuids'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Clean orphaned VDIs."""'
newline|'\n'
name|'for'
name|'vdi_uuid'
name|'in'
name|'vdi_uuids'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"CLEANING VDI (%s)"'
op|'%'
name|'vdi_uuid'
newline|'\n'
nl|'\n'
dedent|''
name|'vdi_ref'
op|'='
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.get_by_uuid'"
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'call_xenapi'
op|'('
name|'xenapi'
op|','
string|"'VDI.destroy'"
op|','
name|'vdi_ref'
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
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"Skipping %s: %s"'
op|'%'
op|'('
name|'vdi_uuid'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_orphaned_instances
dedent|''
dedent|''
dedent|''
name|'def'
name|'list_orphaned_instances'
op|'('
name|'orphaned_instances'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""List orphaned instances."""'
newline|'\n'
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
op|','
name|'orphaned_instance'
name|'in'
name|'orphaned_instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"ORPHANED INSTANCE (%s)"'
op|'%'
name|'orphaned_instance'
op|'.'
name|'name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'orphaned_instance'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clean_orphaned_instances
dedent|''
dedent|''
dedent|''
name|'def'
name|'clean_orphaned_instances'
op|'('
name|'xenapi'
op|','
name|'orphaned_instances'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Clean orphaned instances."""'
newline|'\n'
name|'for'
name|'vm_ref'
op|','
name|'vm_rec'
op|','
name|'instance'
name|'in'
name|'orphaned_instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"CLEANING INSTANCE (%s)"'
op|'%'
name|'instance'
op|'.'
name|'name'
newline|'\n'
nl|'\n'
dedent|''
name|'cleanup_instance'
op|'('
name|'xenapi'
op|','
name|'instance'
op|','
name|'vm_ref'
op|','
name|'vm_rec'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Main loop."""'
newline|'\n'
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'args'
op|'='
name|'CONF'
op|'('
name|'args'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|','
name|'usage'
op|'='
string|"'%(prog)s [options] --command={'"
op|'+'
nl|'\n'
string|"'|'"
op|'.'
name|'join'
op|'('
name|'ALLOWED_COMMANDS'
op|')'
op|'+'
string|"'}'"
op|')'
newline|'\n'
nl|'\n'
name|'command'
op|'='
name|'CONF'
op|'.'
name|'command'
newline|'\n'
name|'if'
name|'not'
name|'command'
name|'or'
name|'command'
name|'not'
name|'in'
name|'ALLOWED_COMMANDS'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'print_usage'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'zombie_instance_updated_at_window'
op|'<'
name|'CONF'
op|'.'
name|'resize_confirm_window'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"`zombie_instance_updated_at_window` has to be longer"'
nl|'\n'
string|'" than `resize_confirm_window`."'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(blamar) This tool does not require DB access, so passing in the'
nl|'\n'
comment|"# 'abstract' VirtAPI class is acceptable"
nl|'\n'
dedent|''
name|'xenapi'
op|'='
name|'xenapi_driver'
op|'.'
name|'XenAPIDriver'
op|'('
name|'virtapi'
op|'.'
name|'VirtAPI'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'command'
op|'=='
string|'"list-vdis"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"Connected VDIs:\\n"'
newline|'\n'
dedent|''
name|'orphaned_vdi_uuids'
op|'='
name|'find_orphaned_vdi_uuids'
op|'('
name|'xenapi'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"\\nOrphaned VDIs:\\n"'
newline|'\n'
dedent|''
name|'list_orphaned_vdis'
op|'('
name|'orphaned_vdi_uuids'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'command'
op|'=='
string|'"clean-vdis"'
op|':'
newline|'\n'
indent|'        '
name|'orphaned_vdi_uuids'
op|'='
name|'find_orphaned_vdi_uuids'
op|'('
name|'xenapi'
op|')'
newline|'\n'
name|'clean_orphaned_vdis'
op|'('
name|'xenapi'
op|','
name|'orphaned_vdi_uuids'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'command'
op|'=='
string|'"list-instances"'
op|':'
newline|'\n'
indent|'        '
name|'orphaned_instances'
op|'='
name|'find_orphaned_instances'
op|'('
name|'xenapi'
op|')'
newline|'\n'
name|'list_orphaned_instances'
op|'('
name|'orphaned_instances'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'command'
op|'=='
string|'"clean-instances"'
op|':'
newline|'\n'
indent|'        '
name|'orphaned_instances'
op|'='
name|'find_orphaned_instances'
op|'('
name|'xenapi'
op|')'
newline|'\n'
name|'clean_orphaned_instances'
op|'('
name|'xenapi'
op|','
name|'orphaned_instances'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'command'
op|'=='
string|'"test"'
op|':'
newline|'\n'
indent|'        '
name|'doctest'
op|'.'
name|'testmod'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"Unknown command \'%s\'"'
op|'%'
name|'command'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
