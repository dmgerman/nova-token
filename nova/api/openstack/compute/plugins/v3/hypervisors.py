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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-hypervisors"'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'v3:'"
op|'+'
name|'ALIAS'
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
name|'detail'
op|','
name|'servers'
op|'='
name|'None'
op|','
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
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'hypervisor_hostname'"
op|':'
name|'hypervisor'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'detail'
name|'and'
name|'not'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'field'
name|'in'
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
op|','
nl|'\n'
string|"'host_ip'"
op|')'
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
name|'hypervisor'
op|'['
string|"'service_id'"
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'hypervisor'
op|'['
string|"'service'"
op|']'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'servers'
op|'!='
name|'None'
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
name|'id'
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
name|'hyp'
op|','
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
DECL|member|detail
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
name|'hyp'
op|','
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
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'501'
op|')'
op|')'
newline|'\n'
DECL|member|uptime
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
op|'['
string|"'service'"
op|']'
op|'['
string|"'host'"
op|']'
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
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
DECL|member|search
name|'def'
name|'search'
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
name|'query'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'query'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'query'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Need parameter \'query\' to specify "'
nl|'\n'
string|'"which hypervisor to filter on"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
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
name|'query'
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
name|'hyp'
op|','
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
DECL|member|servers
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'compute_node'
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
op|'['
string|"'service'"
op|']'
op|'['
string|"'host'"
op|']'
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
name|'compute_node'
op|','
name|'False'
op|','
nl|'\n'
name|'instances'
op|')'
op|')'
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
DECL|member|statistics
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
name|'V3APIExtensionBase'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'HypervisorsController'
op|'('
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
string|"'search'"
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
dedent|''
dedent|''
endmarker|''
end_unit
