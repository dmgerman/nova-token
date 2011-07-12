begin_unit
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
name|'urlparse'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
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
name|'import'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
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
name|'faults'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
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
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'images_view'
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
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.images'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|SUPPORTED_FILTERS
name|'SUPPORTED_FILTERS'
op|'='
op|'['
string|"'name'"
op|','
string|"'status'"
op|']'
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
string|'"""Base controller for retrieving/displaying images."""'
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
name|'compute_service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize new `ImageController`.\n\n        :param compute_service: `nova.compute.api:API`\n        :param image_service: `nova.image.service:BaseImageService`\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_compute_service'
op|'='
name|'compute_service'
name|'or'
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_image_service'
op|'='
name|'image_service'
name|'or'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'get_default_image_service'
op|'('
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
string|'"""\n        Return a dictionary of query param filters from the request\n\n        :param req: the Request object coming from the wsgi layer\n        :retval a dict of key/value filters\n        """'
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
name|'str_params'
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
indent|'                '
name|'filters'
op|'['
name|'param'
op|']'
op|'='
name|'req'
op|'.'
name|'str_params'
op|'.'
name|'get'
op|'('
name|'param'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'filters'
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
name|'faults'
op|'.'
name|'Fault'
op|'('
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
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
DECL|member|create
dedent|''
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
string|'"""Snapshot or backup a server instance and save the image.\n\n        Images now have an `image_type` associated with them, which can be\n        \'snapshot\' or the backup type, like \'daily\' or \'weekly\'.\n\n        If the image_type is backup-like, then the rotation factor can be\n        included and that will cause the oldest backups that exceed the\n        rotation factor to be deleted.\n\n        :param req: `wsgi.Request` object\n        """'
newline|'\n'
DECL|function|get_param
name|'def'
name|'get_param'
op|'('
name|'param'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'body'
op|'['
string|'"image"'
op|']'
op|'['
name|'param'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|'"Missing required "'
nl|'\n'
string|'"param: %s"'
op|'%'
name|'param'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'content_type'
op|'='
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'body'
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_type'
op|'='
name|'body'
op|'['
string|'"image"'
op|']'
op|'.'
name|'get'
op|'('
string|'"image_type"'
op|','
string|'"snapshot"'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server_id'
op|'='
name|'self'
op|'.'
name|'_server_id_from_req'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_name'
op|'='
name|'get_param'
op|'('
string|'"name"'
op|')'
newline|'\n'
name|'props'
op|'='
name|'self'
op|'.'
name|'_get_extra_properties'
op|'('
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'image_type'
op|'=='
string|'"snapshot"'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'='
name|'self'
op|'.'
name|'_compute_service'
op|'.'
name|'snapshot'
op|'('
nl|'\n'
name|'context'
op|','
name|'server_id'
op|','
name|'image_name'
op|','
nl|'\n'
name|'extra_properties'
op|'='
name|'props'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'image_type'
op|'=='
string|'"backup"'
op|':'
newline|'\n'
comment|'# NOTE(sirp): Unlike snapshot, backup is not a customer facing'
nl|'\n'
comment|"# API call; rather, it's used by the internal backup scheduler"
nl|'\n'
indent|'            '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|':'
newline|'\n'
indent|'                '
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
string|'"Admin API Required"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'backup_type'
op|'='
name|'get_param'
op|'('
string|'"backup_type"'
op|')'
newline|'\n'
name|'rotation'
op|'='
name|'int'
op|'('
name|'get_param'
op|'('
string|'"rotation"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_compute_service'
op|'.'
name|'backup'
op|'('
nl|'\n'
name|'context'
op|','
name|'server_id'
op|','
name|'image_name'
op|','
nl|'\n'
name|'backup_type'
op|','
name|'rotation'
op|','
name|'extra_properties'
op|'='
name|'props'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Invalid image_type \'%s\' passed"'
op|')'
op|'%'
name|'image_type'
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
string|'"Invalue image_type: "'
nl|'\n'
string|'"%s"'
op|'%'
name|'image_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_builder
dedent|''
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Indicates that you must use a Controller subclass."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req
dedent|''
name|'def'
name|'_server_id_from_req'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_extra_properties
dedent|''
name|'def'
name|'_get_extra_properties'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
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
indent|'    '
string|'"""Version 1.0 specific controller logic."""'
newline|'\n'
nl|'\n'
DECL|member|get_builder
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Property to get the ViewBuilder class we need to use."""'
newline|'\n'
name|'base_url'
op|'='
name|'request'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'images_view'
op|'.'
name|'ViewBuilderV10'
op|'('
name|'base_url'
op|')'
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
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
name|'images'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'images'
op|','
name|'req'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'False'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
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
op|')'
newline|'\n'
name|'images'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'images'
op|','
name|'req'
op|')'
newline|'\n'
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req
dedent|''
name|'def'
name|'_server_id_from_req'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
op|'['
string|"'image'"
op|']'
op|'['
string|"'serverId'"
op|']'
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
string|'"Expected serverId attribute on server entity."'
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
nl|'\n'
nl|'\n'
DECL|class|ControllerV11
dedent|''
dedent|''
dedent|''
name|'class'
name|'ControllerV11'
op|'('
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Version 1.1 specific controller logic."""'
newline|'\n'
nl|'\n'
DECL|member|get_builder
name|'def'
name|'get_builder'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Property to get the ViewBuilder class we need to use."""'
newline|'\n'
name|'base_url'
op|'='
name|'request'
op|'.'
name|'application_url'
newline|'\n'
name|'return'
name|'images_view'
op|'.'
name|'ViewBuilderV11'
op|'('
name|'base_url'
op|')'
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
name|'page_params'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'index'
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
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'False'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
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
name|'page_params'
op|'='
name|'common'
op|'.'
name|'get_pagination_params'
op|'('
name|'req'
op|')'
newline|'\n'
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
name|'builder'
op|'='
name|'self'
op|'.'
name|'get_builder'
op|'('
name|'req'
op|')'
op|'.'
name|'build'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'builder'
op|'('
name|'image'
op|','
name|'detail'
op|'='
name|'True'
op|')'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_server_id_from_req
dedent|''
name|'def'
name|'_server_id_from_req'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server_ref'
op|'='
name|'data'
op|'['
string|"'image'"
op|']'
op|'['
string|"'serverRef'"
op|']'
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
string|'"Expected serverRef attribute on server entity."'
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
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'server_ref'
op|'.'
name|'startswith'
op|'('
string|"'http'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'server_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'passed'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'server_ref'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'req'
op|'.'
name|'application_url'
op|')'
newline|'\n'
name|'version'
op|'='
name|'expected'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'expected_prefix'
op|'='
string|'"/%s/servers/"'
op|'%'
name|'version'
newline|'\n'
name|'_empty'
op|','
name|'_sep'
op|','
name|'server_id'
op|'='
name|'passed'
op|'.'
name|'path'
op|'.'
name|'partition'
op|'('
name|'expected_prefix'
op|')'
newline|'\n'
name|'scheme_ok'
op|'='
name|'passed'
op|'.'
name|'scheme'
op|'=='
name|'expected'
op|'.'
name|'scheme'
newline|'\n'
name|'host_ok'
op|'='
name|'passed'
op|'.'
name|'hostname'
op|'=='
name|'expected'
op|'.'
name|'hostname'
newline|'\n'
name|'port_ok'
op|'='
op|'('
name|'passed'
op|'.'
name|'port'
op|'=='
name|'expected'
op|'.'
name|'port'
name|'or'
nl|'\n'
name|'passed'
op|'.'
name|'port'
op|'=='
name|'FLAGS'
op|'.'
name|'osapi_port'
op|')'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'scheme_ok'
name|'and'
name|'port_ok'
name|'and'
name|'host_ok'
name|'and'
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"serverRef must match request url"'
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
nl|'\n'
dedent|''
name|'return'
name|'server_id'
newline|'\n'
nl|'\n'
DECL|member|_get_extra_properties
dedent|''
name|'def'
name|'_get_extra_properties'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_ref'
op|'='
name|'data'
op|'['
string|"'image'"
op|']'
op|'['
string|"'serverRef'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'server_ref'
op|'.'
name|'startswith'
op|'('
string|"'http'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'server_ref'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'req'
op|'.'
name|'application_url'
op|','
string|"'servers'"
op|','
nl|'\n'
name|'server_ref'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'instance_ref'"
op|':'
name|'server_ref'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageXMLSerializer
dedent|''
dedent|''
name|'class'
name|'ImageXMLSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|xmlns
indent|'    '
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
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
name|'metadata_serializer'
op|'='
name|'image_metadata'
op|'.'
name|'ImageMetadataXMLSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_image_to_xml
dedent|''
name|'def'
name|'_image_to_xml'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_node'
op|'='
name|'xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'image_node'
op|'.'
name|'setAttribute'
op|'('
string|"'id'"
op|','
name|'str'
op|'('
name|'image'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'image_node'
op|'.'
name|'setAttribute'
op|'('
string|"'name'"
op|','
name|'image'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'link_nodes'
op|'='
name|'self'
op|'.'
name|'_create_link_nodes'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'image'
op|'['
string|"'links'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'link_node'
name|'in'
name|'link_nodes'
op|':'
newline|'\n'
indent|'            '
name|'image_node'
op|'.'
name|'appendChild'
op|'('
name|'link_node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'image_node'
newline|'\n'
nl|'\n'
DECL|member|_image_to_xml_detailed
dedent|''
name|'def'
name|'_image_to_xml_detailed'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_node'
op|'='
name|'xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'image'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_image_attributes'
op|'('
name|'image_node'
op|','
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'server'"
name|'in'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'server_node'
op|'='
name|'self'
op|'.'
name|'_create_server_node'
op|'('
name|'xml_doc'
op|','
name|'image'
op|'['
string|"'server'"
op|']'
op|')'
newline|'\n'
name|'image_node'
op|'.'
name|'appendChild'
op|'('
name|'server_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'metadata'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'metadata'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'_create_metadata_node'
op|'('
name|'xml_doc'
op|','
name|'metadata'
op|')'
newline|'\n'
name|'image_node'
op|'.'
name|'appendChild'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'link_nodes'
op|'='
name|'self'
op|'.'
name|'_create_link_nodes'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'image'
op|'['
string|"'links'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'link_node'
name|'in'
name|'link_nodes'
op|':'
newline|'\n'
indent|'            '
name|'image_node'
op|'.'
name|'appendChild'
op|'('
name|'link_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'image_node'
newline|'\n'
nl|'\n'
DECL|member|_add_image_attributes
dedent|''
name|'def'
name|'_add_image_attributes'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'id'"
op|','
name|'str'
op|'('
name|'image'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'name'"
op|','
name|'image'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'created'"
op|','
name|'image'
op|'['
string|"'created'"
op|']'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'updated'"
op|','
name|'image'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'status'"
op|','
name|'image'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'progress'"
name|'in'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'progress'"
op|','
name|'str'
op|'('
name|'image'
op|'['
string|"'progress'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_metadata_node
dedent|''
dedent|''
name|'def'
name|'_create_metadata_node'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'metadata_serializer'
op|'.'
name|'meta_list_to_xml'
op|'('
name|'xml_doc'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_server_node
dedent|''
name|'def'
name|'_create_server_node'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'server'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_node'
op|'='
name|'xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'server'"
op|')'
newline|'\n'
name|'server_node'
op|'.'
name|'setAttribute'
op|'('
string|"'id'"
op|','
name|'str'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
comment|"#server_node.setAttribute('name', server['name'])"
nl|'\n'
comment|'#link_nodes = self._create_link_nodes(xml_doc,'
nl|'\n'
comment|"#                                     image['links'])"
nl|'\n'
comment|'#for link_node in link_nodes:'
nl|'\n'
comment|'#    server_node.appendChild(link_node)'
nl|'\n'
name|'return'
name|'server_node'
newline|'\n'
nl|'\n'
DECL|member|_image_list_to_xml
dedent|''
name|'def'
name|'_image_list_to_xml'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'images'
op|','
name|'detailed'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_node'
op|'='
name|'xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'images'"
op|')'
newline|'\n'
name|'if'
name|'detailed'
op|':'
newline|'\n'
indent|'            '
name|'image_to_xml'
op|'='
name|'self'
op|'.'
name|'_image_to_xml_detailed'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'image_to_xml'
op|'='
name|'self'
op|'.'
name|'_image_to_xml'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image'
name|'in'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'item_node'
op|'='
name|'image_to_xml'
op|'('
name|'xml_doc'
op|','
name|'image'
op|')'
newline|'\n'
name|'container_node'
op|'.'
name|'appendChild'
op|'('
name|'item_node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'container_node'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'images_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_image_list_to_xml'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'images_dict'
op|'['
string|"'images'"
op|']'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'to_xml_string'
op|'('
name|'node'
op|','
name|'True'
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
name|'images_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_image_list_to_xml'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'images_dict'
op|'['
string|"'images'"
op|']'
op|','
nl|'\n'
name|'detailed'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'to_xml_string'
op|'('
name|'node'
op|','
name|'True'
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
name|'image_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_image_to_xml_detailed'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'image_dict'
op|'['
string|"'image'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'to_xml_string'
op|'('
name|'node'
op|','
name|'True'
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
name|'image_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_image_to_xml_detailed'
op|'('
name|'xml_doc'
op|','
nl|'\n'
name|'image_dict'
op|'['
string|"'image'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'to_xml_string'
op|'('
name|'node'
op|','
name|'True'
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
op|'='
string|"'1.0'"
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
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"image"'
op|':'
op|'['
string|'"id"'
op|','
string|'"name"'
op|','
string|'"updated"'
op|','
string|'"created"'
op|','
string|'"status"'
op|','
nl|'\n'
string|'"serverId"'
op|','
string|'"progress"'
op|','
string|'"serverRef"'
op|']'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'['
string|'"rel"'
op|','
string|'"type"'
op|','
string|'"href"'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'xml_serializer'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|','
name|'wsgi'
op|'.'
name|'XMLNS_V10'
op|')'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'ImageXMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
newline|'\n'
nl|'\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'xml_serializer'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
