begin_unit
comment|'# Copyright 2012 OpenStack LLC.'
nl|'\n'
comment|'# All Rights Reserved'
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
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
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
op|'.'
name|'network'
op|'.'
name|'api'
name|'import'
name|'refresh_cache'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'quantumv2'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
nl|'\n'
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
string|"'quantum_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http://127.0.0.1:9696'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'URL for connecting to quantum'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'quantum_url_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'30'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'timeout value for connecting to quantum in seconds'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_admin_username'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'username for connecting to quantum in admin context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_admin_password'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'password for connecting to quantum in admin context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_admin_tenant_name'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'tenant name for connecting to quantum in admin context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_admin_auth_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http://localhost:5000/v2.0'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'auth url for connecting to quantum in admin context'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'quantum_auth_strategy'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'keystone'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'auth strategy for connecting to '"
nl|'\n'
string|"'quantum in admin context'"
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
DECL|class|API
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the quantum 2.x API."""'
newline|'\n'
nl|'\n'
DECL|member|setup_networks_on_host
name|'def'
name|'setup_networks_on_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'teardown'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup or teardown the network structures."""'
newline|'\n'
nl|'\n'
DECL|member|allocate_for_instance
dedent|''
name|'def'
name|'allocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allocate all network resources for the instance."""'
newline|'\n'
name|'quantum'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'allocate_for_instance() for %s'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'search_opts'
op|'.'
name|'update'
op|'('
op|'{'
string|'"tenant_id"'
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'empty project id for instance %s'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'msg'
op|'%'
name|'instance'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# If user has specified to attach instance only to specific'
nl|'\n'
comment|'# networks, add them to **search_opts'
nl|'\n'
comment|'# Tenant-only network only allowed so far'
nl|'\n'
dedent|''
name|'requested_networks'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'requested_networks'"
op|')'
newline|'\n'
name|'ports'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fixed_ips'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'requested_networks'
op|':'
newline|'\n'
indent|'            '
name|'net_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'network_id'
op|','
name|'fixed_ip'
op|','
name|'port_id'
name|'in'
name|'requested_networks'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'port_id'
op|':'
newline|'\n'
indent|'                    '
name|'port'
op|'='
name|'quantum'
op|'.'
name|'show_port'
op|'('
name|'port_id'
op|')'
op|'.'
name|'get'
op|'('
string|"'port'"
op|')'
newline|'\n'
name|'network_id'
op|'='
name|'port'
op|'['
string|"'network_id'"
op|']'
newline|'\n'
name|'ports'
op|'['
name|'network_id'
op|']'
op|'='
name|'port'
newline|'\n'
dedent|''
name|'elif'
name|'fixed_ip'
op|':'
newline|'\n'
indent|'                    '
name|'fixed_ips'
op|'['
name|'network_id'
op|']'
op|'='
name|'fixed_ip'
newline|'\n'
dedent|''
name|'net_ids'
op|'.'
name|'append'
op|'('
name|'network_id'
op|')'
newline|'\n'
dedent|''
name|'search_opts'
op|'['
string|"'id'"
op|']'
op|'='
name|'net_ids'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'quantum'
op|'.'
name|'list_networks'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'nets'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'networks'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'touched_port_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'created_port_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'network'
name|'in'
name|'nets'
op|':'
newline|'\n'
indent|'            '
name|'network_id'
op|'='
name|'network'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'zone'
op|'='
string|"'compute:%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'node_availability_zone'
newline|'\n'
name|'port_req_body'
op|'='
op|'{'
string|"'port'"
op|':'
op|'{'
string|"'device_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'device_owner'"
op|':'
name|'zone'
op|'}'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'='
name|'ports'
op|'.'
name|'get'
op|'('
name|'network_id'
op|')'
newline|'\n'
name|'if'
name|'port'
op|':'
newline|'\n'
indent|'                    '
name|'quantum'
op|'.'
name|'update_port'
op|'('
name|'port'
op|'['
string|"'id'"
op|']'
op|','
name|'port_req_body'
op|')'
newline|'\n'
name|'touched_port_ids'
op|'.'
name|'append'
op|'('
name|'port'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'fixed_ips'
op|'.'
name|'get'
op|'('
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'port_req_body'
op|'['
string|"'port'"
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'fixed_ip'
newline|'\n'
dedent|''
name|'port_req_body'
op|'['
string|"'port'"
op|']'
op|'['
string|"'network_id'"
op|']'
op|'='
name|'network_id'
newline|'\n'
name|'port_req_body'
op|'['
string|"'port'"
op|']'
op|'['
string|"'admin_state_up'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'port_req_body'
op|'['
string|"'port'"
op|']'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'instance'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'created_port_ids'
op|'.'
name|'append'
op|'('
nl|'\n'
name|'quantum'
op|'.'
name|'create_port'
op|'('
name|'port_req_body'
op|')'
op|'['
string|"'port'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'port_id'
name|'in'
name|'touched_port_ids'
op|':'
newline|'\n'
indent|'                        '
name|'port_in_server'
op|'='
name|'quantum'
op|'.'
name|'show_port'
op|'('
name|'port_id'
op|')'
op|'.'
name|'get'
op|'('
string|"'port'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'port_in_server'
op|':'
newline|'\n'
indent|'                            '
name|'raise'
name|'Exception'
op|'('
string|"'Port have already lost'"
op|')'
newline|'\n'
dedent|''
name|'port_req_body'
op|'='
op|'{'
string|"'port'"
op|':'
op|'{'
string|"'device_id'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
name|'quantum'
op|'.'
name|'update_port'
op|'('
name|'port_id'
op|','
name|'port_req_body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'port_id'
name|'in'
name|'created_port_ids'
op|':'
newline|'\n'
indent|'                        '
name|'try'
op|':'
newline|'\n'
indent|'                            '
name|'quantum'
op|'.'
name|'delete_port'
op|'('
name|'port_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fail to delete port %(portid)s with"'
nl|'\n'
string|'" failure: %(exception)s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'portid'"
op|':'
name|'port_id'
op|','
nl|'\n'
string|"'exception'"
op|':'
name|'ex'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|'='
name|'nets'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deallocate_for_instance
dedent|''
name|'def'
name|'deallocate_for_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deallocate all network resources related to the instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'deallocate_for_instance() for %s'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'device_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'ports'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'ports'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'delete_port'
op|'('
name|'port'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fail to delete port %(portid)s with failure:"'
nl|'\n'
string|'"%(exception)s"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'portid'"
op|':'
name|'port'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'exception'"
op|':'
name|'ex'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|get_instance_nw_info
name|'def'
name|'get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance_nw_info
dedent|''
name|'def'
name|'_get_instance_nw_info'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'get_instance_nw_info() for %s'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'nw_info'
op|'='
name|'self'
op|'.'
name|'_build_network_info_model'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|')'
newline|'\n'
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_fixed_ip_to_instance
dedent|''
name|'def'
name|'add_fixed_ip_to_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a fixed ip to the instance from specified network."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_fixed_ip_from_instance
dedent|''
name|'def'
name|'remove_fixed_ip_from_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a fixed ip from the instance."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate_networks
dedent|''
name|'def'
name|'validate_networks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'requested_networks'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Validate that the tenant has the requested networks."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'validate_networks() for %s'"
op|')'
op|','
nl|'\n'
name|'requested_networks'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'requested_networks'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'search_opts'
op|'='
op|'{'
string|'"tenant_id"'
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
name|'net_ids'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'net_id'
op|','
name|'_i'
op|','
name|'port_id'
op|')'
name|'in'
name|'requested_networks'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'port_id'
op|':'
newline|'\n'
indent|'                '
name|'net_ids'
op|'.'
name|'append'
op|'('
name|'net_id'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'port'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'show_port'
op|'('
name|'port_id'
op|')'
op|'.'
name|'get'
op|'('
string|"'port'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'port'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PortNotFound'
op|'('
name|'port_id'
op|'='
name|'port_id'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'port'
op|'.'
name|'get'
op|'('
string|"'device_id'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PortInUse'
op|'('
name|'port_id'
op|'='
name|'port_id'
op|')'
newline|'\n'
dedent|''
name|'net_id'
op|'='
name|'port'
op|'['
string|"'network_id'"
op|']'
newline|'\n'
name|'if'
name|'net_id'
name|'in'
name|'net_ids'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NetworkDuplicated'
op|'('
name|'network_id'
op|'='
name|'net_id'
op|')'
newline|'\n'
dedent|''
name|'net_ids'
op|'.'
name|'append'
op|'('
name|'net_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'search_opts'
op|'['
string|"'id'"
op|']'
op|'='
name|'net_ids'
newline|'\n'
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_networks'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'nets'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'networks'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'nets'
op|')'
op|'!='
name|'len'
op|'('
name|'net_ids'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'requsted_netid_set'
op|'='
name|'set'
op|'('
name|'net_ids'
op|')'
newline|'\n'
name|'returned_netid_set'
op|'='
name|'set'
op|'('
op|'['
name|'net'
op|'['
string|"'id'"
op|']'
name|'for'
name|'net'
name|'in'
name|'nets'
op|']'
op|')'
newline|'\n'
name|'lostid_set'
op|'='
name|'requsted_netid_set'
op|'-'
name|'returned_netid_set'
newline|'\n'
name|'id_str'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'_id'
name|'in'
name|'lostid_set'
op|':'
newline|'\n'
indent|'                '
name|'id_str'
op|'='
name|'id_str'
name|'and'
name|'id_str'
op|'+'
string|"', '"
op|'+'
name|'_id'
name|'or'
name|'_id'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
name|'network_id'
op|'='
name|'id_str'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_uuids_by_ip_filter
dedent|''
dedent|''
name|'def'
name|'get_instance_uuids_by_ip_filter'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of dicts in the form of\n        [{\'instance_uuid\': uuid}] that matched the ip filter.\n        """'
newline|'\n'
comment|"# filters['ip'] is composed as '^%s$' % fixed_ip.replace('.', '\\\\.')"
nl|'\n'
name|'ip'
op|'='
name|'filters'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
newline|'\n'
comment|'# we remove ^$\\ in the ip filer'
nl|'\n'
name|'if'
name|'ip'
op|'['
number|'0'
op|']'
op|'=='
string|"'^'"
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'ip'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'ip'
op|'['
op|'-'
number|'1'
op|']'
op|'=='
string|"'$'"
op|':'
newline|'\n'
indent|'            '
name|'ip'
op|'='
name|'ip'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'ip'
op|'='
name|'ip'
op|'.'
name|'replace'
op|'('
string|"'\\\\.'"
op|','
string|"'.'"
op|')'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
string|'"fixed_ips"'
op|':'
op|'{'
string|"'ip_address'"
op|':'
name|'ip'
op|'}'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'ports'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'ports'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'['
op|'{'
string|"'instance_uuid'"
op|':'
name|'port'
op|'['
string|"'device_id'"
op|']'
op|'}'
name|'for'
name|'port'
name|'in'
name|'ports'
nl|'\n'
name|'if'
name|'port'
op|'['
string|"'device_id'"
op|']'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|associate_floating_ip
name|'def'
name|'associate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'floating_address'
op|','
name|'fixed_address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Associate a floating ip with a fixed ip."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate
dedent|''
name|'def'
name|'disassociate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip
dedent|''
name|'def'
name|'get_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_fixed_ip_by_address
dedent|''
name|'def'
name|'get_fixed_ip_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip
dedent|''
name|'def'
name|'get_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip_pools
dedent|''
name|'def'
name|'get_floating_ip_pools'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ip_by_address
dedent|''
name|'def'
name|'get_floating_ip_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_project
dedent|''
name|'def'
name|'get_floating_ips_by_project'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_floating_ips_by_fixed_address
dedent|''
name|'def'
name|'get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_id_by_floating_address
dedent|''
name|'def'
name|'get_instance_id_by_floating_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vifs_by_instance
dedent|''
name|'def'
name|'get_vifs_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vif_by_mac_address
dedent|''
name|'def'
name|'get_vif_by_mac_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
dedent|''
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a floating ip to a project from a pool."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_floating_ip
dedent|''
name|'def'
name|'release_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove a floating ip with the given address from a project."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'refresh_cache'
newline|'\n'
DECL|member|disassociate_floating_ip
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'address'
op|','
nl|'\n'
name|'affect_auto_assigned'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disassociate a floating ip from the fixed ip\n        it is associated with."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_network_to_project
dedent|''
name|'def'
name|'add_network_to_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'network_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Force add a network to the project."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_network_info_model
dedent|''
name|'def'
name|'_build_network_info_model'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'networks'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'search_opts'
op|'='
op|'{'
string|"'tenant_id'"
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'device_id'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'}'
newline|'\n'
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_ports'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'ports'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'ports'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'networks'
op|':'
newline|'\n'
indent|'            '
name|'search_opts'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'search_opts'
op|'.'
name|'update'
op|'('
op|'{'
string|'"tenant_id"'
op|':'
name|'instance'
op|'['
string|"'project_id'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_networks'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'networks'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|')'
newline|'\n'
name|'for'
name|'port'
name|'in'
name|'ports'
op|':'
newline|'\n'
indent|'            '
name|'network_name'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'networks'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'port'
op|'['
string|"'network_id'"
op|']'
op|'=='
name|'net'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'network_name'
op|'='
name|'net'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'subnets'
op|'='
name|'self'
op|'.'
name|'_get_subnets_from_port'
op|'('
name|'context'
op|','
name|'port'
op|')'
newline|'\n'
name|'network_IPs'
op|'='
op|'['
name|'network_model'
op|'.'
name|'FixedIP'
op|'('
name|'address'
op|'='
name|'ip_address'
op|')'
nl|'\n'
name|'for'
name|'ip_address'
name|'in'
op|'['
name|'ip'
op|'['
string|"'ip_address'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'port'
op|'['
string|"'fixed_ips'"
op|']'
op|']'
op|']'
newline|'\n'
comment|'# TODO(gongysh) get floating_ips for each fixed_ip'
nl|'\n'
nl|'\n'
name|'for'
name|'subnet'
name|'in'
name|'subnets'
op|':'
newline|'\n'
indent|'                '
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|'='
op|'['
name|'fixed_ip'
name|'for'
name|'fixed_ip'
name|'in'
name|'network_IPs'
nl|'\n'
name|'if'
name|'fixed_ip'
op|'.'
name|'is_in_subnet'
op|'('
name|'subnet'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'network'
op|'='
name|'network_model'
op|'.'
name|'Network'
op|'('
nl|'\n'
name|'id'
op|'='
name|'port'
op|'['
string|"'network_id'"
op|']'
op|','
nl|'\n'
name|'bridge'
op|'='
string|"''"
op|','
comment|'# Quantum ignores this field'
nl|'\n'
name|'injected'
op|'='
name|'FLAGS'
op|'.'
name|'flat_injected'
op|','
nl|'\n'
name|'label'
op|'='
name|'network_name'
op|','
nl|'\n'
name|'tenant_id'
op|'='
name|'net'
op|'['
string|"'tenant_id'"
op|']'
nl|'\n'
op|')'
newline|'\n'
name|'network'
op|'['
string|"'subnets'"
op|']'
op|'='
name|'subnets'
newline|'\n'
name|'nw_info'
op|'.'
name|'append'
op|'('
name|'network_model'
op|'.'
name|'VIF'
op|'('
nl|'\n'
name|'id'
op|'='
name|'port'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'address'
op|'='
name|'port'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'network'
op|'='
name|'network'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'nw_info'
newline|'\n'
nl|'\n'
DECL|member|_get_subnets_from_port
dedent|''
name|'def'
name|'_get_subnets_from_port'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the subnets for a given port."""'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'='
name|'port'
op|'['
string|"'fixed_ips'"
op|']'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'id'"
op|':'
op|'['
name|'ip'
op|'['
string|"'subnet_id'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'fixed_ips'
op|']'
op|'}'
newline|'\n'
name|'data'
op|'='
name|'quantumv2'
op|'.'
name|'get_client'
op|'('
name|'context'
op|')'
op|'.'
name|'list_subnets'
op|'('
op|'**'
name|'search_opts'
op|')'
newline|'\n'
name|'ipam_subnets'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'subnets'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'subnets'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'subnet'
name|'in'
name|'ipam_subnets'
op|':'
newline|'\n'
indent|'            '
name|'subnet_dict'
op|'='
op|'{'
string|"'cidr'"
op|':'
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'network_model'
op|'.'
name|'IP'
op|'('
nl|'\n'
name|'address'
op|'='
name|'subnet'
op|'['
string|"'gateway_ip'"
op|']'
op|','
nl|'\n'
name|'type'
op|'='
string|"'gateway'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'# TODO(gongysh) deal with dhcp'
nl|'\n'
nl|'\n'
name|'subnet_object'
op|'='
name|'network_model'
op|'.'
name|'Subnet'
op|'('
op|'**'
name|'subnet_dict'
op|')'
newline|'\n'
name|'for'
name|'dns'
name|'in'
name|'subnet'
op|'.'
name|'get'
op|'('
string|"'dns_nameservers'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'subnet_object'
op|'.'
name|'add_dns'
op|'('
nl|'\n'
name|'network_model'
op|'.'
name|'IP'
op|'('
name|'address'
op|'='
name|'dns'
op|','
name|'type'
op|'='
string|"'dns'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(gongysh) get the routes for this subnet'
nl|'\n'
dedent|''
name|'subnets'
op|'.'
name|'append'
op|'('
name|'subnet_object'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'subnets'
newline|'\n'
nl|'\n'
DECL|member|get_dns_domains
dedent|''
name|'def'
name|'get_dns_domains'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of available dns domains.\n\n        These can be used to create DNS entries for floating ips.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_dns_entry
dedent|''
name|'def'
name|'add_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'name'
op|','
name|'dns_type'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create specified DNS entry for address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_dns_entry
dedent|''
name|'def'
name|'modify_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create specified DNS entry for address."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_entry
dedent|''
name|'def'
name|'delete_dns_entry'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the specified dns entry."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_domain
dedent|''
name|'def'
name|'delete_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the specified dns domain."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_address
dedent|''
name|'def'
name|'get_dns_entries_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for address and domain."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dns_entries_by_name
dedent|''
name|'def'
name|'get_dns_entries_by_name'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get entries for name and domain."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_private_dns_domain
dedent|''
name|'def'
name|'create_private_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|','
name|'availability_zone'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a private DNS domain with nova availability zone."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_public_dns_domain
dedent|''
name|'def'
name|'create_public_dns_domain'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'domain'
op|','
name|'project'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a private DNS domain with optional nova project."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
