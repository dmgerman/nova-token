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
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'rackspace'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'services'
op|'.'
name|'image'
name|'import'
name|'ImageService'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
DECL|class|Controller
name|'class'
name|'Controller'
op|'('
name|'base'
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
name|'_svc'
op|'='
name|'ImageService'
op|'.'
name|'load'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_id_xlator'
op|'='
name|'RackspaceApiImageIdTranslator'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_rs_id
dedent|''
name|'def'
name|'_to_rs_id'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Convert an image id from the format of our ImageService strategy\n        to the Rackspace API format (an int).\n        """'
newline|'\n'
name|'strategy'
op|'='
name|'self'
op|'.'
name|'_svc'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_id_xlator'
op|'.'
name|'to_rs_id'
op|'('
name|'strategy'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_from_rs_id
dedent|''
name|'def'
name|'_from_rs_id'
op|'('
name|'self'
op|','
name|'rs_image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Convert an image id from the Rackspace API format (an int) to the\n        format of our ImageService strategy.\n        """'
newline|'\n'
name|'strategy'
op|'='
name|'self'
op|'.'
name|'_svc'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_id_xlator'
op|'.'
name|'from_rs_id'
op|'('
name|'strategy'
op|','
name|'rs_image_id'
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
string|'"""Return all public images."""'
newline|'\n'
name|'data'
op|'='
name|'dict'
op|'('
op|'('
name|'self'
op|'.'
name|'_to_rs_id'
op|'('
name|'id'
op|')'
op|','
name|'val'
op|')'
nl|'\n'
name|'for'
name|'id'
op|','
name|'val'
name|'in'
name|'self'
op|'.'
name|'_svc'
op|'.'
name|'index'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
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
name|'_from_rs_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'_svc'
op|'.'
name|'show'
op|'('
name|'opaque_id'
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
nl|'\n'
nl|'\n'
DECL|class|RackspaceApiImageIdTranslator
dedent|''
dedent|''
name|'class'
name|'RackspaceApiImageIdTranslator'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Converts Rackspace API image ids to and from the id format for a given\n    strategy.\n    """'
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
name|'_store'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_key_template'
op|'='
string|'"rsapi.idstrategies.image.%s.%s"'
newline|'\n'
nl|'\n'
DECL|member|to_rs_id
dedent|''
name|'def'
name|'to_rs_id'
op|'('
name|'self'
op|','
name|'strategy_name'
op|','
name|'opaque_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert an id from a strategy-specific one to a Rackspace one."""'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'_key_template'
op|'%'
op|'('
name|'strategy_name'
op|','
string|'"fwd"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_store'
op|'.'
name|'hget'
op|'('
name|'key'
op|','
name|'str'
op|'('
name|'opaque_id'
op|')'
op|')'
newline|'\n'
name|'if'
name|'result'
op|':'
comment|'# we have a mapping from opaque to RS for this strategy'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Store the mapping.'
nl|'\n'
indent|'            '
name|'nextid'
op|'='
name|'self'
op|'.'
name|'_store'
op|'.'
name|'incr'
op|'('
string|'"%s.lastid"'
op|'%'
name|'key'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_store'
op|'.'
name|'hsetnx'
op|'('
name|'key'
op|','
name|'str'
op|'('
name|'opaque_id'
op|')'
op|','
name|'nextid'
op|')'
op|':'
newline|'\n'
comment|"# If someone else didn't beat us to it, store the reverse"
nl|'\n'
comment|'# mapping as well.'
nl|'\n'
indent|'                '
name|'key'
op|'='
name|'self'
op|'.'
name|'_key_template'
op|'%'
op|'('
name|'strategy_name'
op|','
string|'"rev"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_store'
op|'.'
name|'hset'
op|'('
name|'key'
op|','
name|'nextid'
op|','
name|'str'
op|'('
name|'opaque_id'
op|')'
op|')'
newline|'\n'
name|'return'
name|'nextid'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Someone beat us to it; use their number instead, and'
nl|'\n'
comment|"# discard nextid (which is OK -- we don't require that"
nl|'\n'
comment|'# every int id be used.)'
nl|'\n'
indent|'                '
name|'return'
name|'int'
op|'('
name|'self'
op|'.'
name|'_store'
op|'.'
name|'hget'
op|'('
name|'key'
op|','
name|'str'
op|'('
name|'opaque_id'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|from_rs_id
dedent|''
dedent|''
dedent|''
name|'def'
name|'from_rs_id'
op|'('
name|'self'
op|','
name|'strategy_name'
op|','
name|'rs_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert a Rackspace id to a strategy-specific one."""'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'_key_template'
op|'%'
op|'('
name|'strategy_name'
op|','
string|'"rev"'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_store'
op|'.'
name|'hget'
op|'('
name|'key'
op|','
name|'rs_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
