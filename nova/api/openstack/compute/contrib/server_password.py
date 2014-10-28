begin_unit
comment|'# Copyright (c) 2012 Nebula, Inc.'
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
string|'"""The server password extension."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'password'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
string|"'server_password'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerPasswordTemplate
name|'class'
name|'ServerPasswordTemplate'
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
string|"'password'"
op|','
name|'selector'
op|'='
string|"'password'"
op|')'
newline|'\n'
name|'root'
op|'.'
name|'text'
op|'='
name|'unicode'
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
DECL|class|ServerPasswordController
dedent|''
dedent|''
name|'class'
name|'ServerPasswordController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Server Password API controller for the OpenStack API."""'
newline|'\n'
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
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
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
name|'ServerPasswordTemplate'
op|')'
newline|'\n'
DECL|member|index
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'common'
op|'.'
name|'get_instance'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'context'
op|','
name|'server_id'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'passw'
op|'='
name|'password'
op|'.'
name|'extract_password'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'password'"
op|':'
name|'passw'
name|'or'
string|"''"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'common'
op|'.'
name|'get_instance'
op|'('
name|'self'
op|'.'
name|'compute_api'
op|','
name|'context'
op|','
name|'server_id'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
newline|'\n'
name|'meta'
op|'='
name|'password'
op|'.'
name|'convert_password'
op|'('
name|'context'
op|','
name|'None'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'system_metadata'
op|'.'
name|'update'
op|'('
name|'meta'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Server_password
dedent|''
dedent|''
name|'class'
name|'Server_password'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server password support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ServerPassword"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-server-password"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"server-password/api/v2"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-11-29T00:00:00Z"'
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
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-server-password'"
op|','
nl|'\n'
name|'controller'
op|'='
name|'ServerPasswordController'
op|'('
op|')'
op|','
nl|'\n'
name|'collection_actions'
op|'='
op|'{'
string|"'delete'"
op|':'
string|"'DELETE'"
op|'}'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'server'"
op|','
name|'collection_name'
op|'='
string|"'servers'"
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
