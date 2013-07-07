begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nHandle lease database updates from DHCP servers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
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
name|'config'
newline|'\n'
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
op|'.'
name|'network'
name|'import'
name|'rpcapi'
name|'as'
name|'network_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'network_manager'"
op|','
string|"'nova.service'"
op|')'
newline|'\n'
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
DECL|function|add_lease
name|'def'
name|'add_lease'
op|'('
name|'mac'
op|','
name|'ip_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the IP that was assigned by the DHCP server."""'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"leasing ip"'
op|')'
op|')'
newline|'\n'
name|'network_manager'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'network_manager'
op|'.'
name|'lease_fixed_ip'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'ip_address'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'api'
op|'='
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'lease_fixed_ip'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'ip_address'
op|','
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|old_lease
dedent|''
dedent|''
name|'def'
name|'old_lease'
op|'('
name|'mac'
op|','
name|'ip_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Called when an old lease is recognized."""'
newline|'\n'
comment|'# NOTE(vish): We assume we heard about this lease the first time.'
nl|'\n'
comment|'#             If not, we will get it the next time the lease is'
nl|'\n'
comment|'#             renewed.'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|del_lease
dedent|''
name|'def'
name|'del_lease'
op|'('
name|'mac'
op|','
name|'ip_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Called when a lease expires."""'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"releasing ip"'
op|')'
op|')'
newline|'\n'
name|'network_manager'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'network_manager'
op|'.'
name|'release_fixed_ip'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'ip_address'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'api'
op|'='
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'release_fixed_ip'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'ip_address'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init_leases
dedent|''
dedent|''
name|'def'
name|'init_leases'
op|'('
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the list of hosts for a network."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'ctxt'
op|','
name|'network_id'
op|')'
newline|'\n'
name|'network_manager'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'network_manager'
op|')'
newline|'\n'
name|'return'
name|'network_manager'
op|'.'
name|'get_dhcp_leases'
op|'('
name|'ctxt'
op|','
name|'network_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_action_parsers
dedent|''
name|'def'
name|'add_action_parsers'
op|'('
name|'subparsers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'parser'
op|'='
name|'subparsers'
op|'.'
name|'add_parser'
op|'('
string|"'init'"
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(cfb): dnsmasq always passes mac, and ip. hostname'
nl|'\n'
comment|"#            is passed if known. We don't care about"
nl|'\n'
comment|'#            hostname, but argparse will complain if we'
nl|'\n'
comment|'#            do not accept it.'
nl|'\n'
name|'for'
name|'action'
name|'in'
op|'['
string|"'add'"
op|','
string|"'del'"
op|','
string|"'old'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'parser'
op|'='
name|'subparsers'
op|'.'
name|'add_parser'
op|'('
name|'action'
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'mac'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'add_argument'
op|'('
string|"'hostname'"
op|','
name|'nargs'
op|'='
string|"'?'"
op|','
name|'default'
op|'='
string|"''"
op|')'
newline|'\n'
name|'parser'
op|'.'
name|'set_defaults'
op|'('
name|'func'
op|'='
name|'globals'
op|'('
op|')'
op|'['
name|'action'
op|'+'
string|"'_lease'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'CONF'
op|'.'
name|'register_cli_opt'
op|'('
nl|'\n'
name|'cfg'
op|'.'
name|'SubCommandOpt'
op|'('
string|"'action'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Action options'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Available dhcpbridge options'"
op|','
nl|'\n'
DECL|variable|handler
name|'handler'
op|'='
name|'add_action_parsers'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse environment and arguments and call the appropriate action."""'
newline|'\n'
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|','
nl|'\n'
name|'default_config_files'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'os'
op|'.'
name|'environ'
op|'['
string|"'CONFIG_FILE'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
name|'global'
name|'LOG'
newline|'\n'
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.dhcpbridge'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'name'
name|'in'
op|'['
string|"'add'"
op|','
string|"'del'"
op|','
string|"'old'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"Called \'%(action)s\' for mac \'%(mac)s\' with ip \'%(ip)s\'"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|'"action"'
op|':'
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'name'
op|','
nl|'\n'
string|'"mac"'
op|':'
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'mac'
op|','
nl|'\n'
string|'"ip"'
op|':'
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'ip'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'func'
op|'('
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'mac'
op|','
name|'CONF'
op|'.'
name|'action'
op|'.'
name|'ip'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network_id'
op|'='
name|'int'
op|'('
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'NETWORK_ID'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Environment variable \'NETWORK_ID\' must be set."'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'print'
name|'init_leases'
op|'('
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
