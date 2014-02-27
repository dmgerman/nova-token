begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
name|'def'
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the actual ip of the local machine.\n\n    This code figures out what source address would be used if some traffic\n    were to be sent out to some well known address on the Internet. In this\n    case, a Google DNS server is used, but the specific address does not\n    matter much.  No traffic is actually sent.\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'8.8.8.8'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'get_my_ipv4_address'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|netconf_opts
dedent|''
dedent|''
name|'netconf_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'my_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'_get_my_ip'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address of this host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of this node.  This can be an opaque identifier.  '"
nl|'\n'
string|"'It is not necessarily a hostname, FQDN, or IP address. '"
nl|'\n'
string|"'However, the node name must be valid within '"
nl|'\n'
string|"'an AMQP key, and if using ZeroMQ, a valid '"
nl|'\n'
string|"'hostname, FQDN, or IP address'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_ipv6'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use IPv6'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'netconf_opts'
op|')'
newline|'\n'
endmarker|''
end_unit
