begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""VMRC console drivers."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'json'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|vmrc_opts
name|'vmrc_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'console_vmrc_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'443'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"port for VMware VMRC connections"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'console_vmrc_error_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"number of retries for retrieving VMRC information"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'vmrc_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMRCConsole
name|'class'
name|'VMRCConsole'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VMRC console driver with ESX credentials."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'VMRCConsole'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|console_type
name|'def'
name|'console_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'vmrc+credentials'"
newline|'\n'
nl|'\n'
DECL|member|get_port
dedent|''
name|'def'
name|'get_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get available port for consoles."""'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'console_vmrc_port'
newline|'\n'
nl|'\n'
DECL|member|setup_console
dedent|''
name|'def'
name|'setup_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'console'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up console."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|teardown_console
dedent|''
name|'def'
name|'teardown_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'console'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tears down console."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform console initialization."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|fix_pool_password
dedent|''
name|'def'
name|'fix_pool_password'
op|'('
name|'self'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Encode password."""'
newline|'\n'
comment|'# TODO(sateesh): Encrypt pool password'
nl|'\n'
name|'return'
name|'password'
newline|'\n'
nl|'\n'
DECL|member|generate_password
dedent|''
name|'def'
name|'generate_password'
op|'('
name|'self'
op|','
name|'vim_session'
op|','
name|'pool'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns VMRC Connection credentials.\n\n        Return string is of the form \'<VM PATH>:<ESX Username>@<ESX Password>\'.\n\n        """'
newline|'\n'
name|'username'
op|','
name|'password'
op|'='
name|'pool'
op|'['
string|"'username'"
op|']'
op|','
name|'pool'
op|'['
string|"'password'"
op|']'
newline|'\n'
name|'vms'
op|'='
name|'vim_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|"'get_objects'"
op|','
nl|'\n'
string|"'VirtualMachine'"
op|','
op|'['
string|"'name'"
op|','
string|"'config.files.vmPathName'"
op|']'
op|')'
newline|'\n'
name|'vm_ds_path_name'
op|'='
name|'None'
newline|'\n'
name|'vm_ref'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'vms'
op|':'
newline|'\n'
indent|'            '
name|'vm_name'
op|'='
name|'None'
newline|'\n'
name|'ds_path_name'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'prop'
name|'in'
name|'vm'
op|'.'
name|'propSet'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'prop'
op|'.'
name|'name'
op|'=='
string|"'name'"
op|':'
newline|'\n'
indent|'                    '
name|'vm_name'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|"'config.files.vmPathName'"
op|':'
newline|'\n'
indent|'                    '
name|'ds_path_name'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'vm_name'
op|'=='
name|'instance_name'
op|':'
newline|'\n'
indent|'                '
name|'vm_ref'
op|'='
name|'vm'
op|'.'
name|'obj'
newline|'\n'
name|'vm_ds_path_name'
op|'='
name|'ds_path_name'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'vm_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'json_data'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'vm_id'"
op|':'
name|'vm_ds_path_name'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'username'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'password'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'json_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_otp
dedent|''
name|'def'
name|'is_otp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Is one time password or not."""'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMRCSessionConsole
dedent|''
dedent|''
name|'class'
name|'VMRCSessionConsole'
op|'('
name|'VMRCConsole'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VMRC console driver with VMRC One Time Sessions."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'VMRCSessionConsole'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|console_type
name|'def'
name|'console_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'vmrc+session'"
newline|'\n'
nl|'\n'
DECL|member|generate_password
dedent|''
name|'def'
name|'generate_password'
op|'('
name|'self'
op|','
name|'vim_session'
op|','
name|'pool'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a VMRC Session.\n\n        Return string is of the form \'<VM MOID>:<VMRC Ticket>\'.\n\n        """'
newline|'\n'
name|'vms'
op|'='
name|'vim_session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|"'get_objects'"
op|','
nl|'\n'
string|"'VirtualMachine'"
op|','
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'vms'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'vm'
op|'.'
name|'propSet'
op|'['
number|'0'
op|']'
op|'.'
name|'val'
op|'=='
name|'instance_name'
op|':'
newline|'\n'
indent|'                '
name|'vm_ref'
op|'='
name|'vm'
op|'.'
name|'obj'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'vm_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'virtual_machine_ticket'
op|'='
name|'vim_session'
op|'.'
name|'_call_method'
op|'('
nl|'\n'
name|'vim_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|','
nl|'\n'
string|"'AcquireCloneTicket'"
op|','
nl|'\n'
name|'vim_session'
op|'.'
name|'_get_vim'
op|'('
op|')'
op|'.'
name|'get_service_content'
op|'('
op|')'
op|'.'
name|'sessionManager'
op|')'
newline|'\n'
name|'json_data'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'vm_id'"
op|':'
name|'str'
op|'('
name|'vm_ref'
op|'.'
name|'value'
op|')'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'virtual_machine_ticket'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'virtual_machine_ticket'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'json_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_otp
dedent|''
name|'def'
name|'is_otp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Is one time password or not."""'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
