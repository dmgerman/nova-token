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
name|'webob'
op|'.'
name|'exc'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
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
op|'.'
name|'views'
name|'import'
name|'images'
name|'as'
name|'images_view'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
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
string|'"""\n    Base `wsgi.Controller` for retrieving and displaying images in the\n    OpenStack API. Version-inspecific code goes here.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_serialization_metadata
name|'_serialization_metadata'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
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
op|','
nl|'\n'
op|'}'
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
string|'"""\n        Initialize new `ImageController`.\n\n        @param compute_service: `nova.compute.api:API`\n        @param image_service: `nova.image.service:BaseImageService`\n        """'
newline|'\n'
name|'_default_service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'image_service'
op|')'
newline|'\n'
nl|'\n'
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
name|'_default_service'
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
string|'"""\n        Return an index listing of images available to the request.\n\n        @param req: `wsgi.Request` object\n        """'
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
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'index'
op|'('
name|'context'
op|')'
newline|'\n'
name|'build'
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
name|'build'
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
string|'"""\n        Return a detailed index listing of images available to the request.\n\n        @param req: `wsgi.Request` object.\n        """'
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
name|'images'
op|'='
name|'self'
op|'.'
name|'_image_service'
op|'.'
name|'detail'
op|'('
name|'context'
op|')'
newline|'\n'
name|'build'
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
name|'build'
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
string|'"""\n        Return detailed information about a specific image.\n\n        @param req: `wsgi.Request` object\n        @param id: Image identifier (integer)\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'id'
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
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'ex'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Image not found."'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'ex'
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
string|'"""\n        Delete an image, if allowed.\n\n        @param req: `wsgi.Request` object\n        @param id: Image identifier (integer)\n        """'
newline|'\n'
name|'image_id'
op|'='
name|'id'
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
name|'image_id'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Snapshot a server instance and save the image.\n\n        @param req: `wsgi.Request` object\n        """'
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
name|'content_type'
op|'='
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
newline|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'content_type'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'image'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'server_id'
op|'='
name|'image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"serverId"'
op|']'
newline|'\n'
name|'image_name'
op|'='
name|'image'
op|'['
string|'"image"'
op|']'
op|'['
string|'"name"'
op|']'
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
name|'image'
op|'='
name|'self'
op|'.'
name|'_compute_service'
op|'.'
name|'snapshot'
op|'('
name|'context'
op|','
name|'server_id'
op|','
name|'image_name'
op|')'
newline|'\n'
name|'return'
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
string|'"""\n    Version 1.0 specific controller logic.\n    """'
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
string|'"""\n        Property to get the ViewBuilder class we need to use.\n        """'
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
indent|'    '
string|'"""\n    Version 1.1 specific controller logic.\n    """'
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
string|'"""\n        Property to get the ViewBuilder class we need to use.\n        """'
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
dedent|''
dedent|''
endmarker|''
end_unit
