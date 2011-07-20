begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'faults'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
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
name|'import'
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The servers addresses API controller for the Openstack API."""'
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
name|'compute_api'
op|'='
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance
dedent|''
name|'def'
name|'_get_instance'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
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
name|'req'
op|','
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotImplemented'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV10
dedent|''
dedent|''
name|'class'
name|'ControllerV10'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'req'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'addresses'"
op|':'
name|'builder'
op|'.'
name|'build'
op|'('
name|'instance'
op|')'
op|'}'
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
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'req'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'if'
name|'id'
op|'=='
string|"'private'"
op|':'
newline|'\n'
indent|'            '
name|'view'
op|'='
name|'builder'
op|'.'
name|'build_private_parts'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'id'
op|'=='
string|"'public'"
op|':'
newline|'\n'
indent|'            '
name|'view'
op|'='
name|'builder'
op|'.'
name|'build_public_parts'
op|'('
name|'instance'
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
string|'"Only private and public networks available"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
name|'id'
op|':'
name|'view'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_view_builder
dedent|''
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV10'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ControllerV11
dedent|''
dedent|''
name|'class'
name|'ControllerV11'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
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
name|'interfaces'
op|'='
name|'self'
op|'.'
name|'_get_virtual_interfaces'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'interfaces'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'addresses'"
op|':'
name|'networks'
op|'}'
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
name|'server_id'
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
name|'interfaces'
op|'='
name|'self'
op|'.'
name|'_get_virtual_interfaces'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
name|'network'
op|'='
name|'self'
op|'.'
name|'_get_view_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build_network'
op|'('
name|'interfaces'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance is not a member of specified network"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'network'
newline|'\n'
nl|'\n'
DECL|member|_get_virtual_interfaces
dedent|''
name|'def'
name|'_get_virtual_interfaces'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'db'
op|'.'
name|'api'
op|'.'
name|'virtual_interface_get_by_instance'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Instance does not exist"'
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
DECL|member|_get_view_builder
dedent|''
dedent|''
name|'def'
name|'_get_view_builder'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'addresses'
op|'.'
name|'ViewBuilderV11'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'controller'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'ControllerV10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'ControllerV11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'xmlns'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'wsgi'
op|'.'
name|'XMLNS_V10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|"'list_collections'"
op|':'
op|'{'
nl|'\n'
string|"'public'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
string|"'private'"
op|':'
op|'{'
string|"'item_name'"
op|':'
string|"'ip'"
op|','
string|"'item_key'"
op|':'
string|"'addr'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'xmlns'
op|'='
name|'xmlns'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'body_serializers'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'controller'
op|','
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
