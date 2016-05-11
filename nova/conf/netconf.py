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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'netutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|netconf_opts
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
name|'netutils'
op|'.'
name|'get_my_ipv4'
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
string|"'my_block_storage_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Block storage IP address of this host'"
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
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'netconf_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'DEFAULT'"
op|':'
name|'netconf_opts'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit