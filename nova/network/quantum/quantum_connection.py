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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|quantum_opts
name|'quantum_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_connection_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'HOST for connecting to quantum'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_connection_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'9696'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'PORT for connecting to quantum'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_default_tenant_id'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"default"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default tenant id when creating quantum networks'"
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
name|'quantum_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuantumClientConnection
name|'class'
name|'QuantumClientConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts connection to Quantum service into higher level\n       operations performed by the QuantumManager.\n\n       Separating this out as a class also let\'s us create a \'fake\'\n       version of this class for unit tests.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'client'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize Quantum client class based on flags."""'
newline|'\n'
name|'if'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'client'
op|'='
name|'client'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
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
dedent|''
name|'def'
name|'create_network'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'network_name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create network using specified name, return Quantum\n           network UUID.\n        """'
newline|'\n'
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
name|'for'
name|'kw'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'network'"
op|']'
op|'['
name|'kw'
op|']'
op|'='
name|'kwargs'
op|'['
name|'kw'
op|']'
newline|'\n'
dedent|''
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
DECL|member|get_network_name
dedent|''
name|'def'
name|'get_network_name'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'net'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'show_network_details'
op|'('
name|'network_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'return'
name|'net'
op|'['
string|'"network"'
op|']'
op|'['
string|'"name"'
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
string|'"""Deletes Quantum network with specified UUID."""'
newline|'\n'
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
string|'"""Determine if a Quantum network exists for the\n           specified tenant.\n        """'
newline|'\n'
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
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'quantum_client'
op|'.'
name|'QuantumNotFoundException'
op|':'
newline|'\n'
comment|'# Not really an error.  Real errors will be propogated to caller'
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|get_networks
dedent|''
dedent|''
name|'def'
name|'get_networks'
op|'('
name|'self'
op|','
name|'tenant_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Retrieve all networks for this tenant"""'
newline|'\n'
name|'return'
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
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a Quantum port on the specified network, sets\n           status to ACTIVE to enable traffic, and attaches the\n           vNIC with the specified interface-id.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Connecting interface %(interface_id)s to "'
nl|'\n'
string|'"net %(net_id)s for %(tenant_id)s"'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'for'
name|'kw'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'port_data'
op|'['
string|"'port'"
op|']'
op|'['
name|'kw'
op|']'
op|'='
name|'kwargs'
op|'['
name|'kw'
op|']'
newline|'\n'
dedent|''
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
string|'"""Detach and delete the specified Quantum port."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Deleting port %(port_id)s on net %(net_id)s"'
nl|'\n'
string|'" for %(tenant_id)s"'
op|'%'
name|'locals'
op|'('
op|')'
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
DECL|member|get_port_by_attachment
dedent|''
name|'def'
name|'get_port_by_attachment'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'net_id'
op|','
name|'attachment_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Given a tenant and network, search for the port UUID that\n           has the specified interface-id attachment.\n        """'
newline|'\n'
name|'port_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
op|','
nl|'\n'
name|'filter_ops'
op|'='
op|'{'
string|"'attachment'"
op|':'
name|'attachment_id'
op|'}'
op|')'
newline|'\n'
name|'port_list'
op|'='
name|'port_list_resdict'
op|'['
string|'"ports"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'quantum_client'
op|'.'
name|'QuantumNotFoundException'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'port_list_len'
op|'='
name|'len'
op|'('
name|'port_list'
op|')'
newline|'\n'
name|'if'
name|'port_list_len'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'port_list'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'port_list_len'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Expected single port with attachment "'
nl|'\n'
string|'"%(attachment_id)s, found %(port_list_len)s"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_attached_ports
dedent|''
name|'def'
name|'get_attached_ports'
op|'('
name|'self'
op|','
name|'tenant_id'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'='
op|'['
op|']'
newline|'\n'
name|'port_list'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'list_ports'
op|'('
name|'network_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
name|'for'
name|'p'
name|'in'
name|'port_list'
op|'['
string|'"ports"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'port_id'
op|'='
name|'p'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'show_port_attachment'
op|'('
name|'network_id'
op|','
nl|'\n'
name|'port_id'
op|','
name|'tenant'
op|'='
name|'tenant_id'
op|')'
newline|'\n'
comment|'# Skip ports without an attachment'
nl|'\n'
name|'if'
string|'"id"'
name|'not'
name|'in'
name|'port'
op|'['
string|'"attachment"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'rv'
op|'.'
name|'append'
op|'('
op|'{'
string|"'port-id'"
op|':'
name|'port_id'
op|','
string|"'attachment'"
op|':'
nl|'\n'
name|'port'
op|'['
string|'"attachment"'
op|']'
op|'['
string|'"id"'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rv'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
