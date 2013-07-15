begin_unit
comment|'# Copyright (c) 2013 NTT DOCOMO, INC.'
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
string|'"""The bare-metal admin extension."""'
newline|'\n'
nl|'\n'
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
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'os-baremetal-nodes'"
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
nl|'\n'
string|"'v3:'"
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|node_fields
name|'node_fields'
op|'='
op|'['
string|"'id'"
op|','
string|"'cpus'"
op|','
string|"'local_gb'"
op|','
string|"'memory_mb'"
op|','
string|"'pm_address'"
op|','
nl|'\n'
string|"'pm_user'"
op|','
nl|'\n'
string|"'service_host'"
op|','
string|"'terminal_port'"
op|','
string|"'instance_uuid'"
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|interface_fields
name|'interface_fields'
op|'='
op|'['
string|"'id'"
op|','
string|"'address'"
op|','
string|"'datapath_id'"
op|','
string|"'port_no'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_node_dict
name|'def'
name|'_node_dict'
op|'('
name|'node_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'node_fields'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
name|'f'
op|']'
op|'='
name|'node_ref'
op|'.'
name|'get'
op|'('
name|'f'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_interface_dict
dedent|''
name|'def'
name|'_interface_dict'
op|'('
name|'interface_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'interface_fields'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'['
name|'f'
op|']'
op|'='
name|'interface_ref'
op|'.'
name|'get'
op|'('
name|'f'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_node_elem
dedent|''
name|'def'
name|'_make_node_elem'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'f'
name|'in'
name|'node_fields'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'.'
name|'set'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_interface_elem
dedent|''
dedent|''
name|'def'
name|'_make_interface_elem'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'f'
name|'in'
name|'interface_fields'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'.'
name|'set'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NodeTemplate
dedent|''
dedent|''
name|'class'
name|'NodeTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node_elem'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'node'"
op|','
name|'selector'
op|'='
string|"'node'"
op|')'
newline|'\n'
name|'_make_node_elem'
op|'('
name|'node_elem'
op|')'
newline|'\n'
name|'ifs_elem'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'interfaces'"
op|')'
newline|'\n'
name|'if_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'ifs_elem'
op|','
string|"'interface'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'interfaces'"
op|')'
newline|'\n'
name|'_make_interface_elem'
op|'('
name|'if_elem'
op|')'
newline|'\n'
name|'node_elem'
op|'.'
name|'append'
op|'('
name|'ifs_elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'node_elem'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NodesTemplate
dedent|''
dedent|''
name|'class'
name|'NodesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'nodes'"
op|')'
newline|'\n'
name|'node_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'node'"
op|','
name|'selector'
op|'='
string|"'nodes'"
op|')'
newline|'\n'
name|'_make_node_elem'
op|'('
name|'node_elem'
op|')'
newline|'\n'
name|'ifs_elem'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'interfaces'"
op|')'
newline|'\n'
name|'if_elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'ifs_elem'
op|','
string|"'interface'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'interfaces'"
op|')'
newline|'\n'
name|'_make_interface_elem'
op|'('
name|'if_elem'
op|')'
newline|'\n'
name|'node_elem'
op|'.'
name|'append'
op|'('
name|'ifs_elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InterfaceTemplate
dedent|''
dedent|''
name|'class'
name|'InterfaceTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'interface'"
op|','
name|'selector'
op|'='
string|"'interface'"
op|')'
newline|'\n'
name|'_make_interface_elem'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalNodeController
dedent|''
dedent|''
name|'class'
name|'BareMetalNodeController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Bare-Metal Node API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'NodesTemplate'
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
name|'nodes_from_db'
op|'='
name|'db'
op|'.'
name|'bm_node_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'nodes'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'node_from_db'
name|'in'
name|'nodes_from_db'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'ifs'
op|'='
name|'db'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
nl|'\n'
name|'context'
op|','
name|'node_from_db'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NodeNotFound'
op|':'
newline|'\n'
indent|'                '
name|'ifs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'node'
op|'='
name|'_node_dict'
op|'('
name|'node_from_db'
op|')'
newline|'\n'
name|'node'
op|'['
string|"'interfaces'"
op|']'
op|'='
op|'['
name|'_interface_dict'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'ifs'
op|']'
newline|'\n'
name|'nodes'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'nodes'"
op|':'
name|'nodes'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'NodeTemplate'
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
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
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
name|'NodeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'ifs'
op|'='
name|'db'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
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
name|'NodeNotFound'
op|':'
newline|'\n'
indent|'            '
name|'ifs'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'node'
op|'='
name|'_node_dict'
op|'('
name|'node'
op|')'
newline|'\n'
name|'node'
op|'['
string|"'interfaces'"
op|']'
op|'='
op|'['
name|'_interface_dict'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'ifs'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'node'"
op|':'
name|'node'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'NodeTemplate'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'values'
op|'='
name|'body'
op|'['
string|"'node'"
op|']'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'prov_mac_address'
op|'='
name|'values'
op|'.'
name|'pop'
op|'('
string|"'prov_mac_address'"
op|','
name|'None'
op|')'
newline|'\n'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'node'
op|'='
name|'_node_dict'
op|'('
name|'node'
op|')'
newline|'\n'
name|'if'
name|'prov_mac_address'
op|':'
newline|'\n'
indent|'            '
name|'if_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'bm_node_id'
op|'='
name|'node'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'address'
op|'='
name|'prov_mac_address'
op|','
nl|'\n'
name|'datapath_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'port_no'
op|'='
name|'None'
op|')'
newline|'\n'
name|'if_ref'
op|'='
name|'db'
op|'.'
name|'bm_interface_get'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
newline|'\n'
name|'node'
op|'['
string|"'interfaces'"
op|']'
op|'='
op|'['
name|'_interface_dict'
op|'('
name|'if_ref'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'['
string|"'interfaces'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'node'"
op|':'
name|'node'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'bm_node_destroy'
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
name|'NodeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
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
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_node_exists
dedent|''
name|'def'
name|'_check_node_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'node_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NodeNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
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
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'InterfaceTemplate'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'add_interface'"
op|')'
newline|'\n'
DECL|member|_add_interface
name|'def'
name|'_add_interface'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_node_exists'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'body'
op|'='
name|'body'
op|'['
string|"'add_interface'"
op|']'
newline|'\n'
name|'address'
op|'='
name|'body'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'datapath_id'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'datapath_id'"
op|')'
newline|'\n'
name|'port_no'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'port_no'"
op|')'
newline|'\n'
name|'if_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'bm_node_id'
op|'='
name|'id'
op|','
nl|'\n'
name|'address'
op|'='
name|'address'
op|','
nl|'\n'
name|'datapath_id'
op|'='
name|'datapath_id'
op|','
nl|'\n'
name|'port_no'
op|'='
name|'port_no'
op|')'
newline|'\n'
name|'if_ref'
op|'='
name|'db'
op|'.'
name|'bm_interface_get'
op|'('
name|'context'
op|','
name|'if_id'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'interface'"
op|':'
name|'_interface_dict'
op|'('
name|'if_ref'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'remove_interface'"
op|')'
newline|'\n'
DECL|member|_remove_interface
name|'def'
name|'_remove_interface'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_node_exists'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'body'
op|'='
name|'body'
op|'['
string|"'remove_interface'"
op|']'
newline|'\n'
name|'if_id'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'address'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'address'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'if_id'
name|'and'
name|'not'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Must specify id or address"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'ifs'
op|'='
name|'db'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'ifs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'if_id'
name|'and'
name|'if_id'
op|'!='
name|'i'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'address'
name|'and'
name|'address'
op|'!='
name|'i'
op|'['
string|"'address'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'bm_interface_destroy'
op|'('
name|'context'
op|','
name|'i'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
op|')'
newline|'\n'
dedent|''
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaremetalNodes
dedent|''
dedent|''
name|'class'
name|'BaremetalNodes'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only bare-metal node administration."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"BareMetalNodes"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/baremetal_nodes/api/v3"'
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
op|']'
newline|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
name|'ALIAS'
op|','
nl|'\n'
name|'BareMetalNodeController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|'"action"'
op|':'
string|'"POST"'
op|','
op|'}'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
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
