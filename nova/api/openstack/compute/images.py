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
name|'views'
name|'import'
name|'images'
name|'as'
name|'views_images'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SUPPORTED_FILTERS
name|'SUPPORTED_FILTERS'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'name'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'status'"
op|','
nl|'\n'
string|"'changes-since'"
op|':'
string|"'changes-since'"
op|','
nl|'\n'
string|"'server'"
op|':'
string|"'property-instance_uuid'"
op|','
nl|'\n'
string|"'type'"
op|':'
string|"'property-image_type'"
op|','
nl|'\n'
string|"'minRam'"
op|':'
string|"'min_ram'"
op|','
nl|'\n'
string|"'minDisk'"
op|':'
string|"'min_disk'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_image
name|'def'
name|'make_image'
op|'('
name|'elem'
op|','
name|'detailed'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'updated'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'created'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'progress'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'minRam'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'minDisk'"
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'elem'
op|','
string|"'server'"
op|','
name|'selector'
op|'='
string|"'server'"
op|')'
newline|'\n'
name|'server'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'xmlutil'
op|'.'
name|'make_links'
op|'('
name|'server'
op|','
string|"'links'"
op|')'
newline|'\n'
nl|'\n'
name|'elem'
op|'.'
name|'append'
op|'('
name|'common'
op|'.'
name|'MetadataTemplate'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'xmlutil'
op|'.'
name|'make_links'
op|'('
name|'elem'
op|','
string|"'links'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|image_nsmap
dedent|''
name|'image_nsmap'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageTemplate
name|'class'
name|'ImageTemplate'
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
op|','
name|'detailed'
op|'='
name|'True'
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
op|','
name|'nsmap'
op|'='
name|'image_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MinimalImagesTemplate
dedent|''
dedent|''
name|'class'
name|'MinimalImagesTemplate'
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
name|'xmlutil'
op|'.'
name|'make_links'
op|'('
name|'root'
op|','
string|"'images_links'"
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
op|','
name|'nsmap'
op|'='
name|'image_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesTemplate
dedent|''
dedent|''
name|'class'
name|'ImagesTemplate'
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
op|','
name|'detailed'
op|'='
name|'True'
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
op|','
name|'nsmap'
op|'='
name|'image_nsmap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base controller for retrieving/displaying images."""'
newline|'\n'
nl|'\n'
DECL|variable|_view_builder_class
name|'_view_builder_class'
op|'='
name|'views_images'
op|'.'
name|'ViewBuilder'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image_service'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize new `ImageController`.\n\n        :param image_service: `nova.image.glance:GlanceImageService`\n\n        """'
newline|'\n'
name|'super'
op|'('
name|'Controller'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_service'
op|'='
op|'('
name|'image_service'
name|'or'
nl|'\n'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'get_default_image_service'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_filters
dedent|''
name|'def'
name|'_get_filters'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary of query param filters from the request.\n\n        :param req: the Request object coming from the wsgi layer\n        :retval a dict of key/value filters\n        """'
newline|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'param'
name|'in'
name|'req'
op|'.'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'param'
name|'in'
name|'SUPPORTED_FILTERS'
name|'or'
name|'param'
op|'.'
name|'startswith'
op|'('
string|"'property-'"
op|')'
op|':'
newline|'\n'
comment|'# map filter name or carry through if property-*'
nl|'\n'
indent|'                '
name|'filter_name'
op|'='
name|'SUPPORTED_FILTERS'
op|'.'
name|'get'
op|'('
name|'param'
op|','
name|'param'
op|')'
newline|'\n'
name|'filters'
op|'['
name|'filter_name'
op|']'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure server filter is the instance uuid'
nl|'\n'
dedent|''
dedent|''
name|'filter_name'
op|'='
string|"'property-instance_uuid'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'['
name|'filter_name'
op|']'
op|'='
name|'filters'
op|'['
name|'filter_name'
op|']'
op|'.'
name|'rsplit'
op|'('
string|"'/'"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'AttributeError'
op|','
name|'IndexError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'filter_name'
op|'='
string|"'status'"
newline|'\n'
name|'if'
name|'filter_name'
name|'in'
name|'filters'
op|':'
newline|'\n'
comment|'# The Image API expects us to use lowercase strings for status'
nl|'\n'
indent|'            '
name|'filters'
op|'['
name|'filter_name'
op|']'
op|'='
name|'filters'
op|'['
name|'filter_name'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'filters'
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
name|'ImageTemplate'
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
string|'"""Return detailed information about a specific image.\n\n        :param req: `wsgi.Request` object\n        :param id: Image identifier\n        """'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'show'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
name|'exception'
op|'.'
name|'InvalidImageRef'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Image not found."'
op|')'
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
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'cache_db_items'
op|'('
string|"'images'"
op|','
op|'['
name|'image'
op|']'
op|','
string|"'id'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'image'
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
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete an image, if allowed.\n\n        :param req: `wsgi.Request` object\n        :param id: Image identifier (integer)\n        """'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_image_service'
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
name|'ImageNotFound'
op|':'
newline|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Image not found."'
op|')'
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
name|'explanation'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|':'
newline|'\n'
comment|'# The image service raises this exception on delete if glanceclient'
nl|'\n'
comment|'# raises HTTPForbidden.'
nl|'\n'
indent|'            '
name|'explanation'
op|'='
name|'_'
op|'('
string|'"You are not allowed to delete the image."'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'explanation'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNoContent'
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
name|'MinimalImagesTemplate'
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
string|'"""Return an index listing of images available to the request.\n\n        :param req: `wsgi.Request` object\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
name|'params'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'page_params'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'page_params'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
name|'key'
op|']'
op|'='
name|'val'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'detail'
op|'('
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|','
nl|'\n'
op|'**'
name|'page_params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Invalid'
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
name|'HTTPBadRequest'
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
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'images'
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
name|'ImagesTemplate'
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
string|'"""Return a detailed index listing of images available to the request.\n\n        :param req: `wsgi.Request` object.\n\n        """'
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
name|'filters'
op|'='
name|'self'
op|'.'
name|'_get_filters'
op|'('
name|'req'
op|')'
newline|'\n'
name|'params'
op|'='
name|'req'
op|'.'
name|'GET'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'page_params'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'page_params'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
name|'key'
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'detail'
op|'('
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|','
nl|'\n'
op|'**'
name|'page_params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Invalid'
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
name|'HTTPBadRequest'
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
name|'req'
op|'.'
name|'cache_db_items'
op|'('
string|"'images'"
op|','
name|'images'
op|','
string|"'id'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'images'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPMethodNotAllowed'
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
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
