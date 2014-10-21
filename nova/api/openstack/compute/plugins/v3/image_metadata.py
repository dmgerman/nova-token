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
op|'.'
name|'v3'
name|'import'
name|'image_metadata'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|"'image-metadata'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageMetadataController
name|'class'
name|'ImageMetadataController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The image metadata API controller for the OpenStack API."""'
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
name|'image_api'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_image
dedent|''
name|'def'
name|'_get_image'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'image_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
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
name|'ImageNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Image not found."'
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
number|'403'
op|','
number|'404'
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
op|','
name|'image_id'
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
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'metadata'
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
number|'403'
op|','
number|'404'
op|')'
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
name|'image_id'
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
name|'metadata'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'if'
name|'id'
name|'in'
name|'metadata'
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
name|'metadata'
op|'['
name|'id'
op|']'
op|'}'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
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
number|'404'
op|','
number|'413'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'image_metadata'
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
name|'image_id'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'body'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'context'
op|','
nl|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'image_api'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'image'
op|'['
string|"'properties'"
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'413'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'image_metadata'
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
name|'image_id'
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
nl|'\n'
name|'meta'
op|'='
name|'body'
op|'['
string|"'meta'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'meta'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|'['
name|'id'
op|']'
op|'='
name|'meta'
op|'['
name|'id'
op|']'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'context'
op|','
nl|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image_api'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'meta'
op|'='
name|'meta'
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
number|'400'
op|','
number|'403'
op|','
number|'404'
op|','
number|'413'
op|')'
op|')'
newline|'\n'
op|'@'
name|'validation'
op|'.'
name|'schema'
op|'('
name|'image_metadata'
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
name|'image_id'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'body'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
name|'common'
op|'.'
name|'check_img_metadata_properties_quota'
op|'('
name|'context'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'image'
op|'['
string|"'properties'"
op|']'
op|'='
name|'metadata'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image_api'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'metadata'
op|'='
name|'metadata'
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
number|'403'
op|','
number|'404'
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
name|'image_id'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'image'
op|'['
string|"'properties'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid metadata key"'
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
name|'image'
op|'['
string|"'properties'"
op|']'
op|'.'
name|'pop'
op|'('
name|'id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'image_api'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image'
op|','
name|'data'
op|'='
name|'None'
op|','
nl|'\n'
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageMetadata
dedent|''
dedent|''
dedent|''
name|'class'
name|'ImageMetadata'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Image Metadata API."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ImageMetadata"'
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
string|"'image'"
op|','
nl|'\n'
string|"'collection_name'"
op|':'
string|"'images'"
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
name|'ImageMetadataController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'image_meta'"
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
name|'image_metadata_map'
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
DECL|member|image_metadata_map
dedent|''
name|'def'
name|'image_metadata_map'
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
string|'"/images/{image_id}/metadata"'
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
