begin_unit
comment|'# Copyright 2013 Rackspace Hosting'
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
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'image_size'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_image
name|'def'
name|'make_image'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'{%s}size'"
op|'%'
name|'Image_size'
op|'.'
name|'namespace'
op|','
string|"'%s:size'"
op|'%'
name|'Image_size'
op|'.'
name|'alias'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesSizeTemplate
dedent|''
name|'class'
name|'ImagesSizeTemplate'
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
string|"'images'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'image'"
op|','
name|'selector'
op|'='
string|"'images'"
op|')'
newline|'\n'
name|'make_image'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'Image_size'
op|'.'
name|'alias'
op|':'
name|'Image_size'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageSizeTemplate
dedent|''
dedent|''
name|'class'
name|'ImageSizeTemplate'
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
string|"'image'"
op|','
name|'selector'
op|'='
string|"'image'"
op|')'
newline|'\n'
name|'make_image'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'SlaveTemplate'
op|'('
name|'root'
op|','
number|'1'
op|','
name|'nsmap'
op|'='
op|'{'
nl|'\n'
name|'Image_size'
op|'.'
name|'alias'
op|':'
name|'Image_size'
op|'.'
name|'namespace'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageSizeController
dedent|''
dedent|''
name|'class'
name|'ImageSizeController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_extend_image
indent|'    '
name|'def'
name|'_extend_image'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'image_cache'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"%s:size"'
op|'%'
name|'Image_size'
op|'.'
name|'alias'
newline|'\n'
name|'image'
op|'['
name|'key'
op|']'
op|'='
name|'image_cache'
op|'['
string|"'size'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
string|'"nova.context"'
op|']'
newline|'\n'
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ImageSizeTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'image_resp'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'image'"
op|']'
newline|'\n'
comment|'# image guaranteed to be in the cache due to the core API adding'
nl|'\n'
comment|"# it in its 'show' method"
nl|'\n'
name|'image_cached'
op|'='
name|'req'
op|'.'
name|'get_db_item'
op|'('
string|"'images'"
op|','
name|'image_resp'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_image'
op|'('
name|'image_resp'
op|','
name|'image_cached'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'resp_obj'
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
name|'if'
name|'authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
comment|'# Attach our slave template to the response object'
nl|'\n'
indent|'            '
name|'resp_obj'
op|'.'
name|'attach'
op|'('
name|'xml'
op|'='
name|'ImagesSizeTemplate'
op|'('
op|')'
op|')'
newline|'\n'
name|'images_resp'
op|'='
name|'list'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'images'"
op|']'
op|')'
newline|'\n'
comment|'# images guaranteed to be in the cache due to the core API adding'
nl|'\n'
comment|"# it in its 'detail' method"
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'images_resp'
op|':'
newline|'\n'
indent|'                '
name|'image_cached'
op|'='
name|'req'
op|'.'
name|'get_db_item'
op|'('
string|"'images'"
op|','
name|'image'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_extend_image'
op|'('
name|'image'
op|','
name|'image_cached'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Image_size
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Image_size'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Adds image size to image listings."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"ImageSize"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"OS-EXT-IMG-SIZE"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"image_size/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2013-02-19T00:00:00Z"'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'ImageSizeController'
op|'('
op|')'
newline|'\n'
name|'extension'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'images'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'extension'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
