begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'_id_translator'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'image'
op|'.'
name|'service'
newline|'\n'
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
nl|'\n'
DECL|variable|_serialization_metadata
indent|'    '
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
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
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
name|'_service'
op|'='
name|'nova'
op|'.'
name|'image'
op|'.'
name|'service'
op|'.'
name|'ImageService'
op|'.'
name|'load'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_id_translator'
op|'='
name|'_id_translator'
op|'.'
name|'RackspaceAPIIdTranslator'
op|'('
nl|'\n'
string|'"image"'
op|','
name|'self'
op|'.'
name|'_service'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
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
string|'"""Return all public images in brief."""'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'img'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'img'
op|'['
string|"'name'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'img'
name|'in'
name|'self'
op|'.'
name|'detail'
op|'('
name|'req'
op|')'
op|'['
string|"'images'"
op|']'
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
string|'"""Return all public images in detail."""'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_service'
op|'.'
name|'index'
op|'('
op|')'
newline|'\n'
name|'for'
name|'img'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'img'
op|'['
string|"'id'"
op|']'
op|'='
name|'self'
op|'.'
name|'_id_translator'
op|'.'
name|'to_rs_id'
op|'('
name|'img'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'images'
op|'='
name|'data'
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
string|'"""Return data about the given image id."""'
newline|'\n'
name|'opaque_id'
op|'='
name|'self'
op|'.'
name|'_id_translator'
op|'.'
name|'from_rs_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'img'
op|'='
name|'self'
op|'.'
name|'_service'
op|'.'
name|'show'
op|'('
name|'opaque_id'
op|')'
newline|'\n'
name|'img'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'img'
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
comment|'# Only public images are supported for now.'
nl|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
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
comment|'# Only public images are supported for now, so a request to'
nl|'\n'
comment|'# make a backup of a server cannot be supproted.'
nl|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
comment|"# Users may not modify public images, and that's all that "
nl|'\n'
comment|'# we support for now.'
nl|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
