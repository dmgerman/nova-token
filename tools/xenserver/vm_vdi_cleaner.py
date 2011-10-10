begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack, LLC'
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
name|'optparse'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'XenAPI'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'nova'
name|'import'
name|'flags'
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
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vmops'
newline|'\n'
nl|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|'"resize_confirm_window"'
op|','
string|'"nova.compute.manager"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|'"xenapi_connection_url"'
op|','
string|'"nova.virt.xenapi_conn"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|'"xenapi_connection_username"'
op|','
string|'"nova.virt.xenapi_conn"'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|'"xenapi_connection_password"'
op|','
string|'"nova.virt.xenapi_conn"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
comment|'# NOTE(sirp): Nova futzs with the sys.argv in order to provide default'
nl|'\n'
comment|"# flagfile. To isolate this awful practice, we're supplying a dummy"
nl|'\n'
comment|'# argument list.'
nl|'\n'
DECL|variable|dummy
name|'dummy'
op|'='
op|'['
string|'"fakearg"'
op|']'
newline|'\n'
name|'utils'
op|'.'
name|'default_flagfile'
op|'('
name|'args'
op|'='
name|'dummy'
op|')'
newline|'\n'
name|'FLAGS'
op|'('
name|'dummy'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnrecognizedNameLabel
name|'class'
name|'UnrecognizedNameLabel'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_options
dedent|''
name|'def'
name|'parse_options'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate command line options."""'
newline|'\n'
nl|'\n'
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
name|'arg_str'
op|'='
string|'"|"'
op|'.'
name|'join'
op|'('
name|'ALLOWED_COMMANDS'
op|')'
newline|'\n'
name|'parser'
op|'='
name|'optparse'
op|'.'
name|'OptionParser'
op|'('
string|'"%prog [options] ["'
op|'+'
name|'arg_str'
op|'+'
string|'"]"'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_option'
op|'('
string|'"--verbose"'
op|','
name|'action'
op|'='
string|'"store_true"'
op|')'
newline|'\n'
nl|'\n'
name|'options'
op|','
name|'args'
op|'='
name|'parser'
op|'.'
name|'parse_args'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'args'
op|':'
newline|'\n'
indent|'        '
name|'parser'
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
name|'return'
name|'options'
op|','
name|'args'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_id_from_name_label
dedent|''
name|'def'
name|'get_instance_id_from_name_label'
op|'('
name|'name_label'
op|','
name|'template'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""In order to derive the instance_id from the name label on the VM, we\n    take the following steps:\n\n        1. We substitute a dummy value in to the instance_name_template so we\n           can figure out the prefix and the suffix of the template (the\n           instance_id is between the two)\n\n        2. We delete the prefix and suffix from the name_label.\n\n        3. What\'s left *should* be the instance_id which we cast to an int\n           and return.\n\n    >>> get_instance_id_from_name_label("", "instance-%08x")\n    Traceback (most recent call last):\n        ...\n    UnrecognizedNameLabel\n\n    >>> get_instance_id_from_name_label("instance-00000001", "instance-%08x")\n    1\n\n    >>> get_instance_id_from_name_label("instance-0000000A", "instance-%08x")\n    10\n\n    >>> get_instance_id_from_name_label("instance-42-suffix", \\\n            "instance-%d-suffix")\n    42\n    """'
newline|'\n'
nl|'\n'
comment|'# Interpolate template to figure out where to extract the instance_id from.'
nl|'\n'
comment|'# The instance_id may be in hex "%x" or decimal "%d", so try decimal first'
nl|'\n'
comment|'# then fall back to hex.'
nl|'\n'
name|'fake_instance_id'
op|'='
number|'123456789'
newline|'\n'
name|'result'
op|'='
name|'template'
op|'%'
name|'fake_instance_id'
newline|'\n'
name|'in_hex'
op|'='
name|'False'
newline|'\n'
name|'base_10'
op|'='
string|'"%d"'
op|'%'
name|'fake_instance_id'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|','
name|'suffix'
op|'='
name|'result'
op|'.'
name|'split'
op|'('
name|'base_10'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'base_16'
op|'='
string|'"%x"'
op|'%'
name|'fake_instance_id'
newline|'\n'
name|'prefix'
op|','
name|'suffix'
op|'='
name|'result'
op|'.'
name|'split'
op|'('
name|'base_16'
op|')'
newline|'\n'
name|'in_hex'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'prefix'
op|':'
newline|'\n'
indent|'        '
name|'name_label'
op|'='
name|'name_label'
op|'.'
name|'replace'
op|'('
name|'prefix'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'suffix'
op|':'
newline|'\n'
indent|'        '
name|'name_label'
op|'='
name|'name_label'
op|'.'
name|'replace'
op|'('
name|'suffix'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'in_hex'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'int'
op|'('
name|'name_label'
op|','
number|'16'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'int'
op|'('
name|'name_label'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnrecognizedNameLabel'
op|'('
name|'name_label'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'instance_id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_orphaned_instances
dedent|''
name|'def'
name|'find_orphaned_instances'
op|'('
name|'session'
op|','
name|'verbose'
op|'='
name|'False'
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
op|')'
newline|'\n'
name|'orphaned_instances'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'vm_rec'
name|'in'
name|'_get_applicable_vm_recs'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'get_instance_id_from_name_label'
op|'('
nl|'\n'
name|'vm_rec'
op|'['
string|'"name_label"'
op|']'
op|','
name|'FLAGS'
op|'.'
name|'instance_name_template'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'UnrecognizedNameLabel'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'print_xen_object'
op|'('
string|'"WARNING: Unrecognized VM"'
op|','
name|'vm_rec'
op|','
nl|'\n'
name|'indent_level'
op|'='
number|'0'
op|','
name|'verbose'
op|'='
name|'verbose'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'db'
op|'.'
name|'api'
op|'.'
name|'instance_get'
op|'('
name|'ctxt'
op|','
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
comment|"# NOTE(jk0): Err on the side of caution here. If we don't know"
nl|'\n'
comment|'# anything about the particular instance, print a warning and let'
nl|'\n'
comment|'# the operator handle it manually.'
nl|'\n'
indent|'            '
name|'print'
op|'>>'
name|'sys'
op|'.'
name|'stderr'
op|','
string|'"Instance %s not found"'
op|'%'
name|'instance_id'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
comment|"# NOTE(jk0): A zombie VM is an instance that is not active and hasn't"
nl|'\n'
comment|'# been updated in over the specified period.'
nl|'\n'
dedent|''
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
name|'utils'
op|'.'
name|'is_older_than'
op|'('
name|'instance'
op|'.'
name|'updated_at'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'zombie_instance_updated_at_window'
op|')'
op|')'
newline|'\n'
name|'if'
name|'is_zombie_vm'
op|':'
newline|'\n'
indent|'            '
name|'orphaned_instances'
op|'.'
name|'append'
op|'('
name|'instance'
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
name|'session'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete orphaned instances."""'
newline|'\n'
name|'vmops'
op|'='
name|'VMOps'
op|'('
name|'session'
op|')'
newline|'\n'
name|'network_info'
op|'='
name|'None'
newline|'\n'
name|'vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_applicable_vm_recs
dedent|''
name|'def'
name|'_get_applicable_vm_recs'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""An \'applicable\' VM is one that is not a template and not the control\n    domain.\n    """'
newline|'\n'
name|'for'
name|'vm_ref'
name|'in'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_rec'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VM'
op|'.'
name|'get_record'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pretty-print a Xen object.\n\n    Looks like:\n\n        VM (abcd-abcd-abcd): \'name label here\'\n    """'
newline|'\n'
name|'if'
name|'not'
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
name|'session'
op|','
name|'connected_vdi_uuids'
op|','
name|'verbose'
op|'='
name|'False'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'parent_vdi_uuid'
op|')'
newline|'\n'
name|'cur_vdi_rec'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
nl|'\n'
name|'cur_vdi_ref'
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
dedent|''
name|'for'
name|'vm_rec'
name|'in'
name|'_get_applicable_vm_recs'
op|'('
name|'session'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
name|'vbd_rec'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VBD'
op|'.'
name|'get_record'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vbd_vdi_ref'
op|')'
newline|'\n'
nl|'\n'
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
name|'session'
op|','
name|'all_vdi_uuids'
op|','
name|'connected_vdi_uuids'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'False'
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
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_all'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|','
name|'verbose'
op|'='
name|'False'
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
name|'session'
op|','
name|'connected_vdi_uuids'
op|','
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|','
name|'all_vdi_uuids'
op|','
name|'connected_vdi_uuids'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
op|','
name|'verbose'
op|'='
name|'False'
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
name|'session'
op|','
name|'vdi_uuids'
op|','
name|'verbose'
op|'='
name|'False'
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
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'get_by_uuid'
op|'('
name|'vdi_uuid'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'VDI'
op|'.'
name|'destroy'
op|'('
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
op|','
name|'verbose'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""List orphaned instances."""'
newline|'\n'
name|'for'
name|'orphaned_instance'
name|'in'
name|'orphaned_instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
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
name|'session'
op|','
name|'orphaned_instances'
op|','
name|'verbose'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Clean orphaned instances."""'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'orphaned_instances'
op|':'
newline|'\n'
indent|'        '
name|'if'
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
name|'session'
op|','
name|'instance'
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
name|'options'
op|','
name|'args'
op|'='
name|'parse_options'
op|'('
op|')'
newline|'\n'
name|'verbose'
op|'='
name|'options'
op|'.'
name|'verbose'
newline|'\n'
name|'command'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'zombie_instance_updated_at_window'
op|'<'
name|'FLAGS'
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
dedent|''
name|'session'
op|'='
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'xenapi'
op|'.'
name|'login_with_password'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
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
name|'session'
op|','
name|'verbose'
op|'='
name|'verbose'
op|')'
newline|'\n'
name|'if'
name|'verbose'
op|':'
newline|'\n'
indent|'            '
name|'print'
string|'"\\nOprhaned VDIs:\\n"'
newline|'\n'
dedent|''
name|'list_orphaned_vdis'
op|'('
name|'orphaned_vdi_uuids'
op|','
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|','
name|'verbose'
op|'='
name|'verbose'
op|')'
newline|'\n'
name|'clean_orphaned_vdis'
op|'('
name|'session'
op|','
name|'orphaned_vdi_uuids'
op|','
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|','
name|'verbose'
op|'='
name|'verbose'
op|')'
newline|'\n'
name|'list_orphaned_instances'
op|'('
name|'orphaned_instances'
op|','
name|'verbose'
op|'='
name|'verbose'
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
name|'session'
op|','
name|'verbose'
op|'='
name|'verbose'
op|')'
newline|'\n'
name|'clean_orphaned_instances'
op|'('
name|'session'
op|','
name|'orphaned_instances'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'verbose'
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
