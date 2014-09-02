begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
nl|'\n'
comment|'# All Rights Reserved.'
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
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'type'
name|'as'
name|'ctype'
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
name|'utilsfactory'
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
DECL|class|RDPConsoleOps
name|'class'
name|'RDPConsoleOps'
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
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'_vmutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_vmutils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'='
name|'utilsfactory'
op|'.'
name|'get_rdpconsoleutils'
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
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"get_rdp_console called"'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'_hostops'
op|'.'
name|'get_host_ip_addr'
op|'('
op|')'
newline|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'.'
name|'get_rdp_console_port'
op|'('
op|')'
newline|'\n'
name|'vm_id'
op|'='
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_id'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"RDP console: %(host)s:%(port)s, %(vm_id)s"'
op|','
nl|'\n'
op|'{'
string|'"host"'
op|':'
name|'host'
op|','
string|'"port"'
op|':'
name|'port'
op|','
string|'"vm_id"'
op|':'
name|'vm_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'ctype'
op|'.'
name|'ConsoleRDP'
op|'('
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'port'
op|'='
name|'port'
op|','
name|'internal_access_path'
op|'='
name|'vm_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
