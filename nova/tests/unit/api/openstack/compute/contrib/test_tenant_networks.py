begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'os_tenant_networks'
name|'as'
name|'networks'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'tenant_networks'
name|'as'
name|'networks_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
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
DECL|variable|NETWORKS
name|'NETWORKS'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 1"'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 2"'
nl|'\n'
op|'}'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_NETWORK
name|'DEFAULT_NETWORK'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'3'
op|','
nl|'\n'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"default"'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|NETWORKS_WITH_DEFAULT_NET
name|'NETWORKS_WITH_DEFAULT_NET'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'NETWORKS'
op|')'
newline|'\n'
name|'NETWORKS_WITH_DEFAULT_NET'
op|'.'
name|'append'
op|'('
name|'DEFAULT_NETWORK'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_TENANT_ID
name|'DEFAULT_TENANT_ID'
op|'='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network_api_get_all
name|'def'
name|'fake_network_api_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
op|'('
name|'context'
op|'.'
name|'project_id'
op|'=='
name|'DEFAULT_TENANT_ID'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'NETWORKS_WITH_DEFAULT_NET'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'NETWORKS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_network_api_create
dedent|''
dedent|''
name|'def'
name|'fake_network_api_create'
op|'('
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'NETWORKS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TenantNetworksTestV21
dedent|''
name|'class'
name|'TenantNetworksTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|ctrlr
indent|'    '
name|'ctrlr'
op|'='
name|'networks_v21'
op|'.'
name|'TenantNetworkController'
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TenantNetworksTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'ctrlr'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_network_quota'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'original_value'
op|'='
name|'CONF'
op|'.'
name|'use_neutron_default_nets'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TenantNetworksTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|'"use_neutron_default_nets"'
op|','
name|'self'
op|'.'
name|'original_value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.reserve'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.rollback'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.disassociate'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.delete'"
op|')'
newline|'\n'
DECL|member|_test_network_delete_exception
name|'def'
name|'_test_network_delete_exception'
op|'('
name|'self'
op|','
name|'delete_ex'
op|','
name|'disassociate_ex'
op|','
name|'expex'
op|','
nl|'\n'
name|'delete_mock'
op|','
name|'disassociate_mock'
op|','
nl|'\n'
name|'rollback_mock'
op|','
name|'reserve_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'reserve_mock'
op|'.'
name|'return_value'
op|'='
string|"'rv'"
newline|'\n'
name|'if'
name|'delete_mock'
op|':'
newline|'\n'
indent|'            '
name|'delete_mock'
op|'.'
name|'side_effect'
op|'='
name|'delete_ex'
newline|'\n'
dedent|''
name|'if'
name|'disassociate_ex'
op|':'
newline|'\n'
indent|'            '
name|'disassociate_mock'
op|'.'
name|'side_effect'
op|'='
name|'disassociate_ex'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'expex'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'self'
op|'.'
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'disassociate_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'disassociate_ex'
op|':'
newline|'\n'
indent|'            '
name|'delete_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'rollback_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
string|"'rv'"
op|')'
newline|'\n'
name|'reserve_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
name|'networks'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_delete_exception_network_not_found
dedent|''
name|'def'
name|'test_network_delete_exception_network_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
name|'network_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'expex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_delete_exception'
op|'('
name|'None'
op|','
name|'ex'
op|','
name|'expex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_delete_exception_policy_failed
dedent|''
name|'def'
name|'test_network_delete_exception_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
name|'action'
op|'='
string|"'dummy'"
op|')'
newline|'\n'
name|'expex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_delete_exception'
op|'('
name|'ex'
op|','
name|'None'
op|','
name|'expex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_delete_exception_network_in_use
dedent|''
name|'def'
name|'test_network_delete_exception_network_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'NetworkInUse'
op|'('
name|'network_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'expex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_delete_exception'
op|'('
name|'ex'
op|','
name|'None'
op|','
name|'expex'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.reserve'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.commit'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.delete'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.disassociate'"
op|')'
newline|'\n'
DECL|member|test_network_delete
name|'def'
name|'test_network_delete'
op|'('
name|'self'
op|','
name|'disassociate_mock'
op|','
name|'delete_mock'
op|','
name|'commit_mock'
op|','
nl|'\n'
name|'reserve_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'reserve_mock'
op|'.'
name|'return_value'
op|'='
string|"'rv'"
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'networks_v21'
op|'.'
name|'TenantNetworkController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'res'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
name|'disassociate_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
name|'delete_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
name|'commit_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
string|"'rv'"
op|')'
newline|'\n'
name|'reserve_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
name|'networks'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.get'"
op|')'
newline|'\n'
DECL|member|test_network_show
name|'def'
name|'test_network_show'
op|'('
name|'self'
op|','
name|'get_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_mock'
op|'.'
name|'return_value'
op|'='
name|'NETWORKS'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'network'"
op|']'
op|','
name|'NETWORKS'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.get'"
op|')'
newline|'\n'
DECL|member|test_network_show_not_found
name|'def'
name|'test_network_show_not_found'
op|'('
name|'self'
op|','
name|'get_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'get_mock'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'NetworkNotFound'
op|'('
name|'network_id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'self'
op|'.'
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
name|'get_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.get_all'"
op|')'
newline|'\n'
DECL|member|_test_network_index
name|'def'
name|'_test_network_index'
op|'('
name|'self'
op|','
name|'get_all_mock'
op|','
name|'default_net'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|'"use_neutron_default_nets"'
op|','
name|'default_net'
op|')'
newline|'\n'
name|'get_all_mock'
op|'.'
name|'side_effect'
op|'='
name|'fake_network_api_get_all'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'NETWORKS'
newline|'\n'
name|'if'
name|'default_net'
name|'is'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'project_id'
op|'='
name|'DEFAULT_TENANT_ID'
newline|'\n'
name|'expected'
op|'='
name|'NETWORKS_WITH_DEFAULT_NET'
newline|'\n'
nl|'\n'
dedent|''
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'networks'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_index_with_default_net
dedent|''
name|'def'
name|'test_network_index_with_default_net'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_index'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_index_without_default_net
dedent|''
name|'def'
name|'test_network_index_without_default_net'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_network_index'
op|'('
name|'default_net'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.reserve'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.commit'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.create'"
op|')'
newline|'\n'
DECL|member|test_network_create
name|'def'
name|'test_network_create'
op|'('
name|'self'
op|','
name|'create_mock'
op|','
name|'commit_mock'
op|','
name|'reserve_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'reserve_mock'
op|'.'
name|'return_value'
op|'='
string|"'rv'"
newline|'\n'
name|'create_mock'
op|'.'
name|'side_effect'
op|'='
name|'fake_network_api_create'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'NETWORKS'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'del'
name|'body'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
name|'body'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'network'"
op|']'
op|','
name|'NETWORKS'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'commit_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
string|"'rv'"
op|')'
newline|'\n'
name|'reserve_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
name|'networks'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.reserve'"
op|')'
newline|'\n'
DECL|member|test_network_create_quota_error
name|'def'
name|'test_network_create_quota_error'
op|'('
name|'self'
op|','
name|'reserve_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'reserve_mock'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'OverQuota'
op|'('
name|'overs'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 1"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'reserve_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
name|'networks'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.reserve'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.quota.QUOTAS.rollback'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API.create'"
op|')'
newline|'\n'
DECL|member|_test_network_create_exception
name|'def'
name|'_test_network_create_exception'
op|'('
name|'self'
op|','
name|'ex'
op|','
name|'expex'
op|','
name|'create_mock'
op|','
nl|'\n'
name|'rollback_mock'
op|','
name|'reserve_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'reserve_mock'
op|'.'
name|'return_value'
op|'='
string|"'rv'"
newline|'\n'
name|'create_mock'
op|'.'
name|'side_effect'
op|'='
name|'ex'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 1"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'expex'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'reserve_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'ctxt'
op|','
name|'networks'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_exception_policy_failed
dedent|''
name|'def'
name|'test_network_create_exception_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
name|'action'
op|'='
string|"'dummy'"
op|')'
newline|'\n'
name|'expex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_create_exception'
op|'('
name|'ex'
op|','
name|'expex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_exception_service_unavailable
dedent|''
name|'def'
name|'test_network_create_exception_service_unavailable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'Exception'
newline|'\n'
name|'expex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPServiceUnavailable'
newline|'\n'
name|'self'
op|'.'
name|'_test_network_create_exception'
op|'('
name|'ex'
op|','
name|'expex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_empty_body
dedent|''
name|'def'
name|'test_network_create_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_without_cidr
dedent|''
name|'def'
name|'test_network_create_without_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|'"label"'
op|':'
string|'"new net 1"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_bad_format_cidr
dedent|''
name|'def'
name|'test_network_create_bad_format_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|'"cidr"'
op|':'
string|'"123"'
op|','
nl|'\n'
string|'"label"'
op|':'
string|'"new net 1"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_empty_network
dedent|''
name|'def'
name|'test_network_create_empty_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_without_label
dedent|''
name|'def'
name|'test_network_create_without_label'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|'"cidr"'
op|':'
string|'"10.20.105.0/24"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TenantNetworksTestV2
dedent|''
dedent|''
name|'class'
name|'TenantNetworksTestV2'
op|'('
name|'TenantNetworksTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ctrlr
indent|'    '
name|'ctrlr'
op|'='
name|'networks'
op|'.'
name|'NetworkController'
newline|'\n'
DECL|variable|validation_error
name|'validation_error'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|test_network_create_empty_body
name|'def'
name|'test_network_create_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TenantNetworksEnforcementV21
dedent|''
dedent|''
name|'class'
name|'TenantNetworksEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TenantNetworksEnforcementV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'networks_v21'
op|'.'
name|'TenantNetworkController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_policy_failed
dedent|''
name|'def'
name|'test_create_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-tenant-networks'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
op|'{'
string|"'network'"
op|':'
op|'{'
string|"'label'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'cidr'"
op|':'
string|"'10.0.0.0/32'"
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_policy_failed
dedent|''
name|'def'
name|'test_index_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-tenant-networks'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_policy_failed
dedent|''
name|'def'
name|'test_delete_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-tenant-networks'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_policy_failed
dedent|''
name|'def'
name|'test_show_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-tenant-networks'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
