begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Nicira Networks'
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
name|'import'
name|'flags'
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
op|'.'
name|'network'
op|'.'
name|'quantum'
name|'import'
name|'client'
name|'as'
name|'quantum_client'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.network.quantum"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'quantum_connection_host'"
op|','
nl|'\n'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'HOST for connecting to quantum'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'quantum_connection_port'"
op|','
nl|'\n'
string|"'9696'"
op|','
nl|'\n'
string|"'PORT for connecting to quantum'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'quantum_default_tenant_id'"
op|','
nl|'\n'
string|'"default"'
op|','
nl|'\n'
string|"'Default tenant id when creating quantum networks'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumClientConnection
name|'class'
name|'QuantumClientConnection'
op|':'
newline|'\n'
nl|'\n'
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
name|'client'
op|'='
name|'quantum_client'
op|'.'
name|'Client'
op|'('
name|'FLAGS'
op|'.'
name|'quantum_connection_host'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'quantum_connection_port'
op|','
nl|'\n'
name|'format'
op|'='
string|'"json"'
op|','
nl|'\n'
name|'logger'
op|'='
name|'LOG'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_network
dedent|''
name|'def'
name|'create_network'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'network_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|"'name'"
op|':'
name|'network_name'
op|'}'
op|'}'
newline|'\n'
name|'resdict'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'create_network'
op|'('
name|'data'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'return'
name|'resdict'
op|'['
string|'"network"'
op|']'
op|'['
string|'"id"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|delete_network
dedent|''
name|'def'
name|'delete_network'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'.'
name|'delete_network'
op|'('
name|'net_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|network_exists
dedent|''
name|'def'
name|'network_exists'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'.'
name|'show_network_details'
op|'('
name|'net_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
comment|'# FIXME: client lib should expose more granular exceptions'
nl|'\n'
comment|"# so we can confirm we're getting a 404 and not some other error"
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|create_and_attach_port
dedent|''
name|'def'
name|'create_and_attach_port'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|','
name|'interface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Connecting interface %s to net %s for %s"'
op|'%'
op|'('
name|'interface_id'
op|','
name|'net_id'
op|','
name|'tenant_id'
op|')'
op|')'
newline|'\n'
name|'port_data'
op|'='
op|'{'
string|"'port'"
op|':'
op|'{'
string|"'state'"
op|':'
string|"'ACTIVE'"
op|'}'
op|'}'
newline|'\n'
name|'resdict'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'create_port'
op|'('
name|'net_id'
op|','
name|'port_data'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'port_id'
op|'='
name|'resdict'
op|'['
string|'"port"'
op|']'
op|'['
string|'"id"'
op|']'
newline|'\n'
nl|'\n'
name|'attach_data'
op|'='
op|'{'
string|"'attachment'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'interface_id'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'attach_resource'
op|'('
name|'net_id'
op|','
name|'port_id'
op|','
name|'attach_data'
op|','
nl|'\n'
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_and_delete_port
dedent|''
name|'def'
name|'detach_and_delete_port'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|','
name|'port_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Deleting port %s on net %s for %s"'
op|'%'
op|'('
name|'port_id'
op|','
name|'net_id'
op|','
name|'tenant_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'detach_resource'
op|'('
name|'net_id'
op|','
name|'port_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'delete_port'
op|'('
name|'net_id'
op|','
name|'port_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME: (danwent) this will be inefficient until API implements querying'
nl|'\n'
DECL|member|get_port_by_attachment
dedent|''
name|'def'
name|'get_port_by_attachment'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'attachment_id'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'net_list_resdict'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'list_networks'
op|'('
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'net_list_resdict'
op|'['
string|'"networks"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'net_id'
op|'='
name|'n'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'port_list_resdict'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'list_ports'
op|'('
name|'net_id'
op|','
nl|'\n'
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'p'
name|'in'
name|'port_list_resdict'
op|'['
string|'"ports"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'port_id'
op|'='
name|'p'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'port_get_resdict'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'show_port_attachment'
op|'('
name|'net_id'
op|','
nl|'\n'
name|'port_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'if'
name|'attachment_id'
op|'=='
name|'port_get_resdict'
op|'['
string|'"attachment"'
op|']'
op|'['
string|'"id"'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
op|'('
name|'net_id'
op|','
name|'port_id'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
