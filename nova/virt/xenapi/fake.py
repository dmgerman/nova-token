begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
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
comment|'#'
nl|'\n'
comment|'#============================================================================'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Parts of this file are based upon xmlrpclib.py, the XML-RPC client'
nl|'\n'
comment|'# interface included in the Python distribution.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 1999-2002 by Secret Labs AB'
nl|'\n'
comment|'# Copyright (c) 1999-2002 by Fredrik Lundh'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# By obtaining, using, and/or copying this software and/or its'
nl|'\n'
comment|'# associated documentation, you agree that you have read, understood,'
nl|'\n'
comment|'# and will comply with the following terms and conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission to use, copy, modify, and distribute this software and'
nl|'\n'
comment|'# its associated documentation for any purpose and without fee is'
nl|'\n'
comment|'# hereby granted, provided that the above copyright notice appears in'
nl|'\n'
comment|'# all copies, and that both that copyright notice and this permission'
nl|'\n'
comment|'# notice appear in supporting documentation, and that the name of'
nl|'\n'
comment|'# Secret Labs AB or the author not be used in advertising or publicity'
nl|'\n'
comment|'# pertaining to distribution of the software without specific, written'
nl|'\n'
comment|'# prior permission.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD'
nl|'\n'
comment|'# TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANT-'
nl|'\n'
comment|'# ABILITY AND FITNESS.  IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR'
nl|'\n'
comment|'# BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY'
nl|'\n'
comment|'# DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS'
nl|'\n'
comment|'# ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE'
nl|'\n'
comment|'# OF THIS SOFTWARE.'
nl|'\n'
comment|'# --------------------------------------------------------------------'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""\nA fake XenAPI SDK.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'pprint'
name|'import'
name|'pformat'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
name|'_CLASSES'
op|'='
op|'['
string|"'host'"
op|','
string|"'network'"
op|','
string|"'session'"
op|','
string|"'SR'"
op|','
string|"'VBD'"
op|','
DECL|variable|_CLASSES
string|"'PBD'"
op|','
string|"'VDI'"
op|','
string|"'VIF'"
op|','
string|"'VM'"
op|','
string|"'task'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|_db_content
name|'_db_content'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi.fake"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|log_db_contents
name|'def'
name|'log_db_contents'
op|'('
name|'msg'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%s: _db_content => %s"'
op|')'
op|','
name|'msg'
name|'or'
string|'""'
op|','
name|'pformat'
op|'('
name|'_db_content'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset
dedent|''
name|'def'
name|'reset'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'c'
name|'in'
name|'_CLASSES'
op|':'
newline|'\n'
indent|'        '
name|'_db_content'
op|'['
name|'c'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'create_host'
op|'('
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_host
dedent|''
name|'def'
name|'create_host'
op|'('
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'host'"
op|','
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_network
dedent|''
name|'def'
name|'create_network'
op|'('
name|'name_label'
op|','
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'network'"
op|','
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'bridge'"
op|':'
name|'bridge'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_vm
dedent|''
name|'def'
name|'create_vm'
op|'('
name|'name_label'
op|','
name|'status'
op|','
nl|'\n'
name|'is_a_template'
op|'='
name|'False'
op|','
name|'is_control_domain'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'VM'"
op|','
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'power-state'"
op|':'
name|'status'
op|','
nl|'\n'
string|"'is_a_template'"
op|':'
name|'is_a_template'
op|','
nl|'\n'
string|"'is_control_domain'"
op|':'
name|'is_control_domain'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy_vm
dedent|''
name|'def'
name|'destroy_vm'
op|'('
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vm_rec'
op|'='
name|'_db_content'
op|'['
string|"'VM'"
op|']'
op|'['
name|'vm_ref'
op|']'
newline|'\n'
nl|'\n'
name|'vbd_refs'
op|'='
name|'vm_rec'
op|'['
string|"'VBDs'"
op|']'
newline|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'        '
name|'destroy_vbd'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
name|'_db_content'
op|'['
string|"'VM'"
op|']'
op|'['
name|'vm_ref'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy_vbd
dedent|''
name|'def'
name|'destroy_vbd'
op|'('
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'del'
name|'_db_content'
op|'['
string|"'VBD'"
op|']'
op|'['
name|'vbd_ref'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy_vdi
dedent|''
name|'def'
name|'destroy_vdi'
op|'('
name|'vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'del'
name|'_db_content'
op|'['
string|"'VDI'"
op|']'
op|'['
name|'vdi_ref'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_vdi
dedent|''
name|'def'
name|'create_vdi'
op|'('
name|'name_label'
op|','
name|'read_only'
op|','
name|'sr_ref'
op|','
name|'sharable'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'VDI'"
op|','
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'read_only'"
op|':'
name|'read_only'
op|','
nl|'\n'
string|"'SR'"
op|':'
name|'sr_ref'
op|','
nl|'\n'
string|"'type'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'sharable'"
op|':'
name|'sharable'
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'location'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'xenstore_data'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'sm_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'VBDs'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_vbd
dedent|''
name|'def'
name|'create_vbd'
op|'('
name|'vm_ref'
op|','
name|'vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vbd_rec'
op|'='
op|'{'
string|"'VM'"
op|':'
name|'vm_ref'
op|','
string|"'VDI'"
op|':'
name|'vdi_ref'
op|'}'
newline|'\n'
name|'vbd_ref'
op|'='
name|'_create_object'
op|'('
string|"'VBD'"
op|','
name|'vbd_rec'
op|')'
newline|'\n'
name|'after_VBD_create'
op|'('
name|'vbd_ref'
op|','
name|'vbd_rec'
op|')'
newline|'\n'
name|'return'
name|'vbd_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|after_VBD_create
dedent|''
name|'def'
name|'after_VBD_create'
op|'('
name|'vbd_ref'
op|','
name|'vbd_rec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create backref from VM to VBD when VBD is created"""'
newline|'\n'
name|'vm_ref'
op|'='
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
newline|'\n'
name|'vm_rec'
op|'='
name|'_db_content'
op|'['
string|"'VM'"
op|']'
op|'['
name|'vm_ref'
op|']'
newline|'\n'
name|'vm_rec'
op|'['
string|"'VBDs'"
op|']'
op|'='
op|'['
name|'vbd_ref'
op|']'
newline|'\n'
nl|'\n'
name|'vm_name_label'
op|'='
name|'_db_content'
op|'['
string|"'VM'"
op|']'
op|'['
name|'vm_ref'
op|']'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'vm_name_label'"
op|']'
op|'='
name|'vm_name_label'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_pbd
dedent|''
name|'def'
name|'create_pbd'
op|'('
name|'config'
op|','
name|'sr_ref'
op|','
name|'attached'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'PBD'"
op|','
op|'{'
nl|'\n'
string|"'device-config'"
op|':'
name|'config'
op|','
nl|'\n'
string|"'SR'"
op|':'
name|'sr_ref'
op|','
nl|'\n'
string|"'currently-attached'"
op|':'
name|'attached'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_task
dedent|''
name|'def'
name|'create_task'
op|'('
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_create_object'
op|'('
string|"'task'"
op|','
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'name_label'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'pending'"
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_object
dedent|''
name|'def'
name|'_create_object'
op|'('
name|'table'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ref'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'obj'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'_db_content'
op|'['
name|'table'
op|']'
op|'['
name|'ref'
op|']'
op|'='
name|'obj'
newline|'\n'
name|'return'
name|'ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_sr
dedent|''
name|'def'
name|'_create_sr'
op|'('
name|'table'
op|','
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sr_type'
op|'='
name|'obj'
op|'['
number|'6'
op|']'
newline|'\n'
comment|'# Forces fake to support iscsi only'
nl|'\n'
name|'if'
name|'sr_type'
op|'!='
string|"'iscsi'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Failure'
op|'('
op|'['
string|"'SR_UNKNOWN_DRIVER'"
op|','
name|'sr_type'
op|']'
op|')'
newline|'\n'
dedent|''
name|'sr_ref'
op|'='
name|'_create_object'
op|'('
name|'table'
op|','
name|'obj'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'create_vdi'
op|'('
string|"''"
op|','
name|'False'
op|','
name|'sr_ref'
op|','
name|'False'
op|')'
newline|'\n'
name|'pbd_ref'
op|'='
name|'create_pbd'
op|'('
string|"''"
op|','
name|'sr_ref'
op|','
name|'True'
op|')'
newline|'\n'
name|'_db_content'
op|'['
string|"'SR'"
op|']'
op|'['
name|'sr_ref'
op|']'
op|'['
string|"'VDIs'"
op|']'
op|'='
op|'['
name|'vdi_ref'
op|']'
newline|'\n'
name|'_db_content'
op|'['
string|"'SR'"
op|']'
op|'['
name|'sr_ref'
op|']'
op|'['
string|"'PBDs'"
op|']'
op|'='
op|'['
name|'pbd_ref'
op|']'
newline|'\n'
name|'_db_content'
op|'['
string|"'VDI'"
op|']'
op|'['
name|'vdi_ref'
op|']'
op|'['
string|"'SR'"
op|']'
op|'='
name|'sr_ref'
newline|'\n'
name|'_db_content'
op|'['
string|"'PBD'"
op|']'
op|'['
name|'pbd_ref'
op|']'
op|'['
string|"'SR'"
op|']'
op|'='
name|'sr_ref'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'table'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_db_content'
op|'['
name|'table'
op|']'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_all_records
dedent|''
name|'def'
name|'get_all_records'
op|'('
name|'table'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_db_content'
op|'['
name|'table'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_record
dedent|''
name|'def'
name|'get_record'
op|'('
name|'table'
op|','
name|'ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'ref'
name|'in'
name|'_db_content'
op|'['
name|'table'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_db_content'
op|'['
name|'table'
op|']'
op|'.'
name|'get'
op|'('
name|'ref'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Failure'
op|'('
op|'['
string|"'HANDLE_INVALID'"
op|','
name|'table'
op|','
name|'ref'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_for_session_leaks
dedent|''
dedent|''
name|'def'
name|'check_for_session_leaks'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'len'
op|'('
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'Sessions have leaked: %s'"
op|'%'
nl|'\n'
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Failure
dedent|''
dedent|''
name|'class'
name|'Failure'
op|'('
name|'Exception'
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
name|'details'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'details'
op|'='
name|'details'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
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
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'details'
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
name|'return'
string|'"XenAPI Fake Failure: %s"'
op|'%'
name|'str'
op|'('
name|'self'
op|'.'
name|'details'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_details_map
dedent|''
dedent|''
name|'def'
name|'_details_map'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
op|'['
op|'('
name|'str'
op|'('
name|'i'
op|')'
op|','
name|'self'
op|'.'
name|'details'
op|'['
name|'i'
op|']'
op|')'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'details'
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SessionBase
dedent|''
dedent|''
name|'class'
name|'SessionBase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base class for Fake Sessions\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|xenapi_request
dedent|''
name|'def'
name|'xenapi_request'
op|'('
name|'self'
op|','
name|'methodname'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'methodname'
op|'.'
name|'startswith'
op|'('
string|"'login'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_login'
op|'('
name|'methodname'
op|','
name|'params'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'methodname'
op|'=='
string|"'logout'"
name|'or'
name|'methodname'
op|'=='
string|"'session.logout'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_logout'
op|'('
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'full_params'
op|'='
op|'('
name|'self'
op|'.'
name|'_session'
op|','
op|')'
op|'+'
name|'params'
newline|'\n'
name|'meth'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'methodname'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'meth'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Raising NotImplemented'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'xenapi.fake does not have an implementation for %s'"
op|')'
op|'%'
nl|'\n'
name|'methodname'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'meth'
op|'('
op|'*'
name|'full_params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_login
dedent|''
dedent|''
name|'def'
name|'_login'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_session'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|'['
name|'self'
op|'.'
name|'_session'
op|']'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'this_host'"
op|':'
name|'_db_content'
op|'['
string|"'host'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_logout
dedent|''
name|'def'
name|'_logout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'self'
op|'.'
name|'_session'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'s'
name|'not'
name|'in'
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
nl|'\n'
string|'"Logging out a session that is invalid or already logged "'
nl|'\n'
string|'"out: %s"'
op|'%'
name|'s'
op|')'
newline|'\n'
dedent|''
name|'del'
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|'['
name|'s'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'handle'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_session'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'xenapi'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_Dispatcher'
op|'('
name|'self'
op|'.'
name|'xenapi_request'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'login'"
op|')'
name|'or'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'slave_local'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'lambda'
op|'*'
name|'params'
op|':'
name|'self'
op|'.'
name|'_login'
op|'('
name|'name'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'Async'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'lambda'
op|'*'
name|'params'
op|':'
name|'self'
op|'.'
name|'_async'
op|'('
name|'name'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'elif'
string|"'.'"
name|'in'
name|'name'
op|':'
newline|'\n'
indent|'            '
name|'impl'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'name'
op|'.'
name|'replace'
op|'('
string|"'.'"
op|','
string|"'_'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'impl'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
nl|'\n'
DECL|function|callit
indent|'                '
name|'def'
name|'callit'
op|'('
op|'*'
name|'params'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Calling %s %s'"
op|')'
op|','
name|'name'
op|','
name|'impl'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_session'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
name|'impl'
op|'('
op|'*'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'callit'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'_is_gettersetter'
op|'('
name|'name'
op|','
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Calling getter %s'"
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'return'
name|'lambda'
op|'*'
name|'params'
op|':'
name|'self'
op|'.'
name|'_getter'
op|'('
name|'name'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'_is_create'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'lambda'
op|'*'
name|'params'
op|':'
name|'self'
op|'.'
name|'_create'
op|'('
name|'name'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_is_gettersetter
dedent|''
dedent|''
name|'def'
name|'_is_gettersetter'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'getter'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bits'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'len'
op|'('
name|'bits'
op|')'
op|'=='
number|'2'
name|'and'
nl|'\n'
name|'bits'
op|'['
number|'0'
op|']'
name|'in'
name|'_CLASSES'
name|'and'
nl|'\n'
name|'bits'
op|'['
number|'1'
op|']'
op|'.'
name|'startswith'
op|'('
name|'getter'
name|'and'
string|"'get_'"
name|'or'
string|"'set_'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_create
dedent|''
name|'def'
name|'_is_create'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bits'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'len'
op|'('
name|'bits'
op|')'
op|'=='
number|'2'
name|'and'
nl|'\n'
name|'bits'
op|'['
number|'0'
op|']'
name|'in'
name|'_CLASSES'
name|'and'
nl|'\n'
name|'bits'
op|'['
number|'1'
op|']'
op|'=='
string|"'create'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_getter
dedent|''
name|'def'
name|'_getter'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_session'
op|'('
name|'params'
op|')'
newline|'\n'
op|'('
name|'cls'
op|','
name|'func'
op|')'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'func'
op|'=='
string|"'get_all'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_arg_count'
op|'('
name|'params'
op|','
number|'1'
op|')'
newline|'\n'
name|'return'
name|'get_all'
op|'('
name|'cls'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
op|'=='
string|"'get_all_records'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_arg_count'
op|'('
name|'params'
op|','
number|'1'
op|')'
newline|'\n'
name|'return'
name|'get_all_records'
op|'('
name|'cls'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
op|'=='
string|"'get_record'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_arg_count'
op|'('
name|'params'
op|','
number|'2'
op|')'
newline|'\n'
name|'return'
name|'get_record'
op|'('
name|'cls'
op|','
name|'params'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'func'
name|'in'
op|'('
string|"'get_by_name_label'"
op|','
string|"'get_by_uuid'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_arg_count'
op|'('
name|'params'
op|','
number|'2'
op|')'
newline|'\n'
name|'return_singleton'
op|'='
op|'('
name|'func'
op|'=='
string|"'get_by_uuid'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_by_field'
op|'('
nl|'\n'
name|'_db_content'
op|'['
name|'cls'
op|']'
op|','
name|'func'
op|'['
name|'len'
op|'('
string|"'get_by_'"
op|')'
op|':'
op|']'
op|','
name|'params'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'return_singleton'
op|'='
name|'return_singleton'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'params'
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'field'
op|'='
name|'func'
op|'['
name|'len'
op|'('
string|"'get_'"
op|')'
op|':'
op|']'
newline|'\n'
name|'ref'
op|'='
name|'params'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'ref'
name|'in'
name|'_db_content'
op|'['
name|'cls'
op|']'
name|'and'
nl|'\n'
name|'field'
name|'in'
name|'_db_content'
op|'['
name|'cls'
op|']'
op|'['
name|'ref'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'_db_content'
op|'['
name|'cls'
op|']'
op|'['
name|'ref'
op|']'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debuug'
op|'('
name|'_'
op|'('
string|"'Raising NotImplemented'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'xenapi.fake does not have an implementation for %s or it has '"
nl|'\n'
string|"'been called with the wrong number of arguments'"
op|')'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setter
dedent|''
name|'def'
name|'_setter'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_session'
op|'('
name|'params'
op|')'
newline|'\n'
op|'('
name|'cls'
op|','
name|'func'
op|')'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'params'
op|')'
op|'=='
number|'3'
op|':'
newline|'\n'
indent|'            '
name|'field'
op|'='
name|'func'
op|'['
name|'len'
op|'('
string|"'set_'"
op|')'
op|':'
op|']'
newline|'\n'
name|'ref'
op|'='
name|'params'
op|'['
number|'1'
op|']'
newline|'\n'
name|'val'
op|'='
name|'params'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'ref'
name|'in'
name|'_db_content'
op|'['
name|'cls'
op|']'
name|'and'
nl|'\n'
name|'field'
name|'in'
name|'_db_content'
op|'['
name|'cls'
op|']'
op|'['
name|'ref'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'_db_content'
op|'['
name|'cls'
op|']'
op|'['
name|'ref'
op|']'
op|'['
name|'field'
op|']'
op|'='
name|'val'
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
string|"'Raising NotImplemented'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
string|"'xenapi.fake does not have an implementation for %s or it has '"
nl|'\n'
string|"'been called with the wrong number of arguments or the database '"
nl|'\n'
string|"'is missing that field'"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create
dedent|''
name|'def'
name|'_create'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_session'
op|'('
name|'params'
op|')'
newline|'\n'
name|'is_sr_create'
op|'='
name|'name'
op|'=='
string|"'SR.create'"
newline|'\n'
comment|'# Storage Repositories have a different API'
nl|'\n'
name|'expected'
op|'='
name|'is_sr_create'
name|'and'
number|'10'
name|'or'
number|'2'
newline|'\n'
name|'self'
op|'.'
name|'_check_arg_count'
op|'('
name|'params'
op|','
name|'expected'
op|')'
newline|'\n'
op|'('
name|'cls'
op|','
name|'_'
op|')'
op|'='
name|'name'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'ref'
op|'='
name|'is_sr_create'
name|'and'
name|'_create_sr'
op|'('
name|'cls'
op|','
name|'params'
op|')'
name|'or'
name|'_create_object'
op|'('
name|'cls'
op|','
name|'params'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Call hook to provide any fixups needed (ex. creating backrefs)'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'globals'
op|'('
op|')'
op|'['
string|'"after_%s_create"'
op|'%'
name|'cls'
op|']'
op|'('
name|'ref'
op|','
name|'params'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'obj'
op|'='
name|'get_record'
op|'('
name|'cls'
op|','
name|'ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add RO fields'
nl|'\n'
name|'if'
name|'cls'
op|'=='
string|"'VM'"
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'['
string|"'power_state'"
op|']'
op|'='
string|"'Halted'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ref'
newline|'\n'
nl|'\n'
DECL|member|_async
dedent|''
name|'def'
name|'_async'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'task_ref'
op|'='
name|'create_task'
op|'('
name|'name'
op|')'
newline|'\n'
name|'task'
op|'='
name|'_db_content'
op|'['
string|"'task'"
op|']'
op|'['
name|'task_ref'
op|']'
newline|'\n'
name|'func'
op|'='
name|'name'
op|'['
name|'len'
op|'('
string|"'Async.'"
op|')'
op|':'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'['
string|"'result'"
op|']'
op|'='
name|'self'
op|'.'
name|'xenapi_request'
op|'('
name|'func'
op|','
name|'params'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
name|'task'
op|'['
string|"'status'"
op|']'
op|'='
string|"'success'"
newline|'\n'
dedent|''
name|'except'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'task'
op|'['
string|"'error_info'"
op|']'
op|'='
name|'exc'
op|'.'
name|'details'
newline|'\n'
name|'task'
op|'['
string|"'status'"
op|']'
op|'='
string|"'failed'"
newline|'\n'
dedent|''
name|'task'
op|'['
string|"'finished'"
op|']'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
newline|'\n'
name|'return'
name|'task_ref'
newline|'\n'
nl|'\n'
DECL|member|_check_session
dedent|''
name|'def'
name|'_check_session'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'self'
op|'.'
name|'_session'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'self'
op|'.'
name|'_session'
name|'not'
name|'in'
name|'_db_content'
op|'['
string|"'session'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Failure'
op|'('
op|'['
string|"'HANDLE_INVALID'"
op|','
string|"'session'"
op|','
name|'self'
op|'.'
name|'_session'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'params'
op|')'
op|'=='
number|'0'
name|'or'
name|'params'
op|'['
number|'0'
op|']'
op|'!='
name|'self'
op|'.'
name|'_session'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Raising NotImplemented'"
op|')'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'Call to XenAPI without using .xenapi'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_arg_count
dedent|''
dedent|''
name|'def'
name|'_check_arg_count'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'actual'
op|'='
name|'len'
op|'('
name|'params'
op|')'
newline|'\n'
name|'if'
name|'actual'
op|'!='
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Failure'
op|'('
op|'['
string|"'MESSAGE_PARAMETER_COUNT_MISMATCH'"
op|','
nl|'\n'
name|'expected'
op|','
name|'actual'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_by_field
dedent|''
dedent|''
name|'def'
name|'_get_by_field'
op|'('
name|'self'
op|','
name|'recs'
op|','
name|'k'
op|','
name|'v'
op|','
name|'return_singleton'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ref'
op|','
name|'rec'
name|'in'
name|'recs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'rec'
op|'.'
name|'get'
op|'('
name|'k'
op|')'
op|'=='
name|'v'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'append'
op|'('
name|'ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'return_singleton'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'result'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Based upon _Method from xmlrpclib.'
nl|'\n'
DECL|class|_Dispatcher
dedent|''
dedent|''
name|'class'
name|'_Dispatcher'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'send'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__send'
op|'='
name|'send'
newline|'\n'
name|'self'
op|'.'
name|'__name'
op|'='
name|'name'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'__name'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'<xenapi.fake._Dispatcher for %s>'"
op|'%'
name|'self'
op|'.'
name|'__name'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'<xenapi.fake._Dispatcher>'"
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'__name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_Dispatcher'
op|'('
name|'self'
op|'.'
name|'__send'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_Dispatcher'
op|'('
name|'self'
op|'.'
name|'__send'
op|','
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__name'
op|','
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__send'
op|'('
name|'self'
op|'.'
name|'__name'
op|','
name|'args'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
