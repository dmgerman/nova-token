begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""The hypervisors admin extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
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
name|'import'
name|'compute'
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
name|'import'
name|'servicegroup'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'hypervisors'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorsController
name|'class'
name|'HypervisorsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Hypervisors API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host_api'
op|'='
name|'compute'
op|'.'
name|'HostAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'HypervisorsController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'ext_mgr'
newline|'\n'
nl|'\n'
DECL|member|_view_hypervisor
dedent|''
name|'def'
name|'_view_hypervisor'
op|'('
name|'self'
op|','
name|'hypervisor'
op|','
name|'service'
op|','
name|'detail'
op|','
name|'servers'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hyp_dict'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'hypervisor'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'hypervisor'
op|'.'
name|'hypervisor_hostname'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'ext_status_loaded'
op|'='
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-hypervisor-status'"
op|')'
newline|'\n'
name|'if'
name|'ext_status_loaded'
op|':'
newline|'\n'
indent|'            '
name|'alive'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
newline|'\n'
name|'hyp_dict'
op|'['
string|"'state'"
op|']'
op|'='
string|"'up'"
name|'if'
name|'alive'
name|'else'
string|'"down"'
newline|'\n'
name|'hyp_dict'
op|'['
string|"'status'"
op|']'
op|'='
op|'('
nl|'\n'
string|"'disabled'"
name|'if'
name|'service'
op|'.'
name|'disabled'
name|'else'
string|"'enabled'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'detail'
name|'and'
name|'not'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'fields'
op|'='
op|'('
string|"'vcpus'"
op|','
string|"'memory_mb'"
op|','
string|"'local_gb'"
op|','
string|"'vcpus_used'"
op|','
nl|'\n'
string|"'memory_mb_used'"
op|','
string|"'local_gb_used'"
op|','
nl|'\n'
string|"'hypervisor_type'"
op|','
string|"'hypervisor_version'"
op|','
nl|'\n'
string|"'free_ram_mb'"
op|','
string|"'free_disk_gb'"
op|','
string|"'current_workload'"
op|','
nl|'\n'
string|"'running_vms'"
op|','
string|"'cpu_info'"
op|','
string|"'disk_available_least'"
op|')'
newline|'\n'
name|'ext_loaded'
op|'='
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-extended-hypervisors'"
op|')'
newline|'\n'
name|'if'
name|'ext_loaded'
op|':'
newline|'\n'
indent|'                '
name|'fields'
op|'+='
op|'('
string|"'host_ip'"
op|','
op|')'
newline|'\n'
dedent|''
name|'for'
name|'field'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'                '
name|'hyp_dict'
op|'['
name|'field'
op|']'
op|'='
name|'hypervisor'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'hyp_dict'
op|'['
string|"'service'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'service'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'hypervisor'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'ext_status_loaded'
op|':'
newline|'\n'
indent|'                '
name|'hyp_dict'
op|'['
string|"'service'"
op|']'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'disabled_reason'
op|'='
name|'service'
op|'.'
name|'disabled_reason'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'hyp_dict'
op|'['
string|"'servers'"
op|']'
op|'='
op|'['
name|'dict'
op|'('
name|'name'
op|'='
name|'serv'
op|'['
string|"'name'"
op|']'
op|','
name|'uuid'
op|'='
name|'serv'
op|'['
string|"'uuid'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'serv'
name|'in'
name|'servers'
op|']'
newline|'\n'
nl|'\n'
comment|'# Add any additional info'
nl|'\n'
dedent|''
name|'if'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'hyp_dict'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hyp_dict'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
nl|'\n'
comment|'# NOTE(eliqiao): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'compute_nodes'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_compute_nodes'
op|'('
name|'compute_nodes'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'hyp'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'hyp'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'False'
op|')'
nl|'\n'
name|'for'
name|'hyp'
name|'in'
name|'compute_nodes'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detail
dedent|''
name|'def'
name|'detail'
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
nl|'\n'
comment|'# NOTE(eliqiao): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'compute_nodes'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_compute_nodes'
op|'('
name|'compute_nodes'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'hyp'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'hyp'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'True'
op|')'
nl|'\n'
name|'for'
name|'hyp'
name|'in'
name|'compute_nodes'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
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
name|'hyp'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_compute_node'
op|'('
name|'hyp'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Hypervisor with ID \'%s\' could not be found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'service'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'hyp'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
name|'hyp'
op|','
name|'service'
op|','
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|uptime
dedent|''
name|'def'
name|'uptime'
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
name|'hyp'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_get'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_compute_node'
op|'('
name|'hyp'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Hypervisor with ID \'%s\' could not be found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
comment|'# Get the uptime'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'hyp'
op|'.'
name|'host'
newline|'\n'
name|'uptime'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'get_host_uptime'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'NotImplementedError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Virt driver does not implement uptime function."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'service'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
name|'hyp'
op|','
name|'service'
op|','
name|'False'
op|','
nl|'\n'
name|'uptime'
op|'='
name|'uptime'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|search
dedent|''
name|'def'
name|'search'
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
nl|'\n'
comment|'# NOTE(eliqiao): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'hypervisors'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_search_by_hypervisor'
op|'('
nl|'\n'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'hypervisors'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'hyp'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'hyp'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'False'
op|')'
nl|'\n'
name|'for'
name|'hyp'
name|'in'
name|'hypervisors'
op|']'
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
string|'"No hypervisor matching \'%s\' could be found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
DECL|member|servers
dedent|''
dedent|''
name|'def'
name|'servers'
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
nl|'\n'
comment|'# NOTE(eliqiao): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'compute_nodes'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_search_by_hypervisor'
op|'('
nl|'\n'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"No hypervisor matching \'%s\' could be found."'
op|')'
op|'%'
name|'id'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'hypervisors'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'compute_node'
name|'in'
name|'compute_nodes'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'compute_node'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'service'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'service_get_by_compute_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'compute_node'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'hyp'
op|'='
name|'self'
op|'.'
name|'_view_hypervisor'
op|'('
name|'compute_node'
op|','
name|'service'
op|','
name|'False'
op|','
nl|'\n'
name|'instances'
op|')'
newline|'\n'
name|'hypervisors'
op|'.'
name|'append'
op|'('
name|'hyp'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'hypervisors'
op|'='
name|'hypervisors'
op|')'
newline|'\n'
nl|'\n'
DECL|member|statistics
dedent|''
name|'def'
name|'statistics'
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
name|'stats'
op|'='
name|'self'
op|'.'
name|'host_api'
op|'.'
name|'compute_node_statistics'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'hypervisor_statistics'
op|'='
name|'stats'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Hypervisors
dedent|''
dedent|''
name|'class'
name|'Hypervisors'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only hypervisor administration."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Hypervisors"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-hypervisors"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/hypervisors/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-06-21T00:00:00Z"'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-hypervisors'"
op|','
nl|'\n'
name|'HypervisorsController'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'statistics'"
op|':'
string|"'GET'"
op|'}'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'uptime'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'search'"
op|':'
string|"'GET'"
op|','
nl|'\n'
string|"'servers'"
op|':'
string|"'GET'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit