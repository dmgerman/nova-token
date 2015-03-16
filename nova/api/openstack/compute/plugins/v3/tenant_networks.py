begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'import'
name|'netaddr'
op|'.'
name|'core'
name|'as'
name|'netexc'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'schemas'
op|'.'
name|'v3'
name|'import'
name|'tenant_networks'
name|'as'
name|'schema'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'validation'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'quota'
newline|'\n'
nl|'\n'
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
string|"'enable_network_quota'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.contrib.os_tenant_networks'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_neutron_default_nets'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.contrib.os_tenant_networks'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'neutron_default_tenant_id'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.contrib.os_tenant_networks'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'quota_networks'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.contrib.os_tenant_networks'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-tenant-networks'"
newline|'\n'
nl|'\n'
DECL|variable|QUOTAS
name|'QUOTAS'
op|'='
name|'quota'
op|'.'
name|'QUOTAS'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'os_compute_authorizer'
op|'('
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_dict
name|'def'
name|'network_dict'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Here, network should be an object, which could have come'
nl|'\n'
comment|'# from neutron and thus be missing most of the attributes. Providing a'
nl|'\n'
comment|'# default to get() avoids trying to lazy-load missing attributes.'
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|'"id"'
op|':'
name|'network'
op|'.'
name|'get'
op|'('
string|'"uuid"'
op|','
name|'None'
op|')'
name|'or'
name|'network'
op|'.'
name|'get'
op|'('
string|'"id"'
op|','
name|'None'
op|')'
op|','
nl|'\n'
string|'"cidr"'
op|':'
name|'str'
op|'('
name|'network'
op|'.'
name|'get'
op|'('
string|'"cidr"'
op|','
name|'None'
op|')'
op|')'
op|','
nl|'\n'
string|'"label"'
op|':'
name|'network'
op|'.'
name|'get'
op|'('
string|'"label"'
op|','
name|'None'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TenantNetworkController
dedent|''
name|'class'
name|'TenantNetworkController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
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
name|'network_api'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_api'
op|'='
name|'nova'
op|'.'
name|'network'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_default_networks'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_refresh_default_networks
dedent|''
name|'def'
name|'_refresh_default_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_default_networks'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_neutron_default_nets'
op|'=='
string|'"True"'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_default_networks'
op|'='
name|'self'
op|'.'
name|'_get_default_networks'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to get default networks"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_default_networks
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_default_networks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'CONF'
op|'.'
name|'neutron_default_tenant_id'
newline|'\n'
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
name|'networks'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'n'
name|'in'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_all'
op|'('
name|'ctx'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'networks'
op|'['
name|'n'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'n'
op|'['
string|"'label'"
op|']'
newline|'\n'
dedent|''
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
name|'k'
op|','
string|"'label'"
op|':'
name|'v'
op|'}'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'networks'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_default_networks'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_refresh_default_networks'
op|'('
op|')'
newline|'\n'
dedent|''
name|'networks'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'_default_networks'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'networks'"
op|':'
op|'['
name|'network_dict'
op|'('
name|'n'
op|')'
name|'for'
name|'n'
name|'in'
name|'networks'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'network'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network not found"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'network'"
op|':'
name|'network_dict'
op|'('
name|'network'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'reservation'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
op|':'
newline|'\n'
indent|'                '
name|'reservation'
op|'='
name|'QUOTAS'
op|'.'
name|'reserve'
op|'('
name|'context'
op|','
name|'networks'
op|'='
op|'-'
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'reservation'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to update usages deallocating "'
nl|'\n'
string|'"network."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_rollback_quota
dedent|''
name|'def'
name|'_rollback_quota'
op|'('
name|'reservation'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
name|'and'
name|'reservation'
op|':'
newline|'\n'
indent|'                '
name|'QUOTAS'
op|'.'
name|'rollback'
op|'('
name|'context'
op|','
name|'reservation'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'disassociate'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'_rollback_quota'
op|'('
name|'reservation'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkInUse'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'_rollback_quota'
op|'('
name|'reservation'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NetworkNotFound'
op|':'
newline|'\n'
indent|'            '
name|'_rollback_quota'
op|'('
name|'reservation'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Network not found"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
name|'and'
name|'reservation'
op|':'
newline|'\n'
indent|'            '
name|'QUOTAS'
op|'.'
name|'commit'
op|'('
name|'context'
op|','
name|'reservation'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'403'
op|','
number|'503'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'schema'
op|'.'
name|'create'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|'"nova.context"'
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'network'
op|'='
name|'body'
op|'['
string|'"network"'
op|']'
newline|'\n'
name|'keys'
op|'='
op|'['
string|'"cidr"'
op|','
string|'"cidr_v6"'
op|','
string|'"ipam"'
op|','
string|'"vlan_start"'
op|','
string|'"network_size"'
op|','
nl|'\n'
string|'"num_networks"'
op|']'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
name|'k'
op|':'
name|'network'
op|'.'
name|'get'
op|'('
name|'k'
op|')'
name|'for'
name|'k'
name|'in'
name|'keys'
op|'}'
newline|'\n'
nl|'\n'
name|'label'
op|'='
name|'network'
op|'['
string|'"label"'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'kwargs'
op|'['
string|'"cidr"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'net'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'kwargs'
op|'['
string|'"cidr"'
op|']'
op|')'
newline|'\n'
name|'if'
name|'net'
op|'.'
name|'size'
op|'<'
number|'4'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Requested network does not contain "'
nl|'\n'
string|'"enough (2+) usable hosts"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'netexc'
op|'.'
name|'AddrConversionError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Address could not be converted."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'networks'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
op|':'
newline|'\n'
indent|'                '
name|'reservation'
op|'='
name|'QUOTAS'
op|'.'
name|'reserve'
op|'('
name|'context'
op|','
name|'networks'
op|'='
number|'1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'OverQuota'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota exceeded, too many networks."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'kwargs'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'context'
op|'.'
name|'project_id'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'networks'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
nl|'\n'
name|'label'
op|'='
name|'label'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
op|':'
newline|'\n'
indent|'                '
name|'QUOTAS'
op|'.'
name|'commit'
op|'('
name|'context'
op|','
name|'reservation'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
op|':'
newline|'\n'
indent|'                '
name|'QUOTAS'
op|'.'
name|'rollback'
op|'('
name|'context'
op|','
name|'reservation'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"Create networks failed"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|','
name|'extra'
op|'='
name|'network'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPServiceUnavailable'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"network"'
op|':'
name|'network_dict'
op|'('
name|'networks'
op|'['
number|'0'
op|']'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TenantNetworks
dedent|''
dedent|''
name|'class'
name|'TenantNetworks'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tenant-based Network Management Extension."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"OSTenantNetworks"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
name|'TenantNetworkController'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ext'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_sync_networks
dedent|''
dedent|''
name|'def'
name|'_sync_networks'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctx'
op|'='
name|'nova_context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
name|'ctx'
op|'='
name|'ctx'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'networks'
op|'='
name|'nova'
op|'.'
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_all'
op|'('
name|'ctx'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'networks'
op|'='
name|'len'
op|'('
name|'networks'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'enable_network_quota'
op|':'
newline|'\n'
indent|'    '
name|'QUOTAS'
op|'.'
name|'register_resource'
op|'('
name|'quota'
op|'.'
name|'ReservableResource'
op|'('
string|"'networks'"
op|','
nl|'\n'
name|'_sync_networks'
op|','
nl|'\n'
string|"'quota_networks'"
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
