begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'import'
name|'common'
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
name|'schemas'
name|'import'
name|'server_metadata'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'server-metadata'"
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
DECL|class|ServerMetadataController
name|'class'
name|'ServerMetadataController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The server metadata API controller for the OpenStack API."""'
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
name|'compute'
op|'.'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'True'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ServerMetadataController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_metadata
dedent|''
name|'def'
name|'_get_metadata'
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
name|'server'
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
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(mikal): get_instanc_metadata sometimes returns'
nl|'\n'
comment|'# InstanceNotFound in unit tests, even though the instance is'
nl|'\n'
comment|'# fetched on the line above. I blame mocking.'
nl|'\n'
indent|'            '
name|'meta'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_instance_metadata'
op|'('
name|'context'
op|','
name|'server'
op|')'
newline|'\n'
dedent|''
name|'except'
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
string|"'Server does not exist'"
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
name|'meta_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'meta'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'meta_dict'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'meta_dict'
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
string|'"""Returns the list of metadata for a given instance."""'
newline|'\n'
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
op|','
name|'action'
op|'='
string|"'index'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(gmann): Returns 200 for backwards compatibility but should be 201'
nl|'\n'
comment|'# as this operation complete the creation of metadata.'
nl|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'server_metadata'
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
name|'server_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
name|'body'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
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
op|','
name|'action'
op|'='
string|"'create'"
op|')'
newline|'\n'
name|'new_metadata'
op|'='
name|'self'
op|'.'
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'new_metadata'
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'server_metadata'
op|'.'
name|'update'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'server_id'
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
op|','
name|'action'
op|'='
string|"'update'"
op|')'
newline|'\n'
name|'meta_item'
op|'='
name|'body'
op|'['
string|"'meta'"
op|']'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'meta_item'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body and URI mismatch'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'meta_item'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'meta'"
op|':'
name|'meta_item'
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'server_metadata'
op|'.'
name|'update_all'
op|')'
newline|'\n'
DECL|member|update_all
name|'def'
name|'update_all'
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
op|','
name|'action'
op|'='
string|"'update_all'"
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'body'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'new_metadata'
op|'='
name|'self'
op|'.'
name|'_update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server_id'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'metadata'"
op|':'
name|'new_metadata'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_update_instance_metadata
dedent|''
name|'def'
name|'_update_instance_metadata'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'server_id'
op|','
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server'
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
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'update_instance_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'server'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'delete'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceUnknownCell'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'except'
name|'exception'
op|'.'
name|'QuotaError'
name|'as'
name|'error'
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
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceIsLocked'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceInvalidState'
name|'as'
name|'state_error'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
name|'state_error'
op|','
nl|'\n'
string|"'update metadata'"
op|','
name|'server_id'
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
name|'server_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a single metadata item."""'
newline|'\n'
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
op|','
name|'action'
op|'='
string|"'show'"
op|')'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'meta'"
op|':'
op|'{'
name|'id'
op|':'
name|'data'
op|'['
name|'id'
op|']'
op|'}'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Metadata item was not found"'
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
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
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
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes an existing metadata."""'
newline|'\n'
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
op|','
name|'action'
op|'='
string|"'delete'"
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Metadata item was not found"'
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
name|'server'
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
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete_instance_metadata'
op|'('
name|'context'
op|','
name|'server'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceUnknownCell'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
name|'except'
name|'exception'
op|'.'
name|'InstanceIsLocked'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceInvalidState'
name|'as'
name|'state_error'
op|':'
newline|'\n'
indent|'            '
name|'common'
op|'.'
name|'raise_http_conflict_for_instance_invalid_state'
op|'('
name|'state_error'
op|','
nl|'\n'
string|"'delete metadata'"
op|','
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerMetadata
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServerMetadata'
op|'('
name|'extensions'
op|'.'
name|'V21APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Server Metadata API."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ServerMetadata"'
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
name|'parent'
op|'='
op|'{'
string|"'member_name'"
op|':'
string|"'server'"
op|','
nl|'\n'
string|"'collection_name'"
op|':'
string|"'servers'"
op|'}'
newline|'\n'
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'metadata'"
op|','
nl|'\n'
name|'ServerMetadataController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'server_meta'"
op|','
nl|'\n'
name|'parent'
op|'='
name|'parent'
op|','
nl|'\n'
name|'custom_routes_fn'
op|'='
nl|'\n'
name|'self'
op|'.'
name|'server_metadata_map'
nl|'\n'
op|')'
op|']'
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
nl|'\n'
DECL|member|server_metadata_map
dedent|''
name|'def'
name|'server_metadata_map'
op|'('
name|'self'
op|','
name|'mapper'
op|','
name|'wsgi_resource'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"metadata"'
op|','
nl|'\n'
string|'"/{project_id}/servers/{server_id}/metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'wsgi_resource'
op|','
nl|'\n'
name|'action'
op|'='
string|"'update_all'"
op|','
name|'conditions'
op|'='
op|'{'
string|'"method"'
op|':'
op|'['
string|"'PUT'"
op|']'
op|'}'
op|')'
newline|'\n'
comment|'# Also connect the non project_id routes'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"metadata"'
op|','
nl|'\n'
string|'"/servers/{server_id}/metadata"'
op|','
nl|'\n'
name|'controller'
op|'='
name|'wsgi_resource'
op|','
nl|'\n'
name|'action'
op|'='
string|"'update_all'"
op|','
name|'conditions'
op|'='
op|'{'
string|'"method"'
op|':'
op|'['
string|"'PUT'"
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
