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
string|'"""Keypair management extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'legacy_v2'
name|'import'
name|'servers'
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
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
string|"'keypairs'"
op|')'
newline|'\n'
DECL|variable|soft_authorize
name|'soft_authorize'
op|'='
name|'extensions'
op|'.'
name|'soft_extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'keypairs'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeypairController
name|'class'
name|'KeypairController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Keypair API controller for the OpenStack API."""'
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
name|'api'
op|'='
name|'compute_api'
op|'.'
name|'KeypairAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_filter_keypair
dedent|''
name|'def'
name|'_filter_keypair'
op|'('
name|'self'
op|','
name|'keypair'
op|','
op|'**'
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'clean'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'keypair'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'keypair'
op|'.'
name|'public_key'
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
name|'keypair'
op|'.'
name|'fingerprint'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'            '
name|'clean'
op|'['
name|'attr'
op|']'
op|'='
name|'keypair'
op|'['
name|'attr'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'clean'
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
string|'"""Create or import keypair.\n\n        Sending name will generate a key and return private_key\n        and fingerprint.\n\n        You can send a public_key to add an existing ssh key\n\n        params: keypair object with:\n            name (required) - string\n            public_key (optional) - string\n        """'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'body'
op|'['
string|"'keypair'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'params'
op|'['
string|"'name'"
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
string|'"Invalid request body"'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'public_key'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'                '
name|'keypair'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'import_key_pair'
op|'('
name|'context'
op|','
nl|'\n'
name|'context'
op|'.'
name|'user_id'
op|','
name|'name'
op|','
nl|'\n'
name|'params'
op|'['
string|"'public_key'"
op|']'
op|')'
newline|'\n'
name|'keypair'
op|'='
name|'self'
op|'.'
name|'_filter_keypair'
op|'('
name|'keypair'
op|','
name|'user_id'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'keypair'
op|','
name|'private_key'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'create_key_pair'
op|'('
nl|'\n'
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'name'
op|')'
newline|'\n'
name|'keypair'
op|'='
name|'self'
op|'.'
name|'_filter_keypair'
op|'('
name|'keypair'
op|','
name|'user_id'
op|'='
name|'True'
op|')'
newline|'\n'
name|'keypair'
op|'['
string|"'private_key'"
op|']'
op|'='
name|'private_key'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'keypair'"
op|':'
name|'keypair'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'KeypairLimitExceeded'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Quota exceeded, too many key pairs."'
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
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidKeypair'
name|'as'
name|'exc'
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
name|'exc'
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
name|'KeyPairExists'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
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
string|'"""Delete a keypair with a given name."""'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_key_pair'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'KeypairNotFound'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'202'
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
string|'"""Return data for the given key name."""'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|"# The return object needs to be a dict in order to pop the 'type'"
nl|'\n'
comment|'# field, since it is incompatible with API version <= 2.1.'
nl|'\n'
indent|'            '
name|'keypair'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_key_pair'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|','
name|'id'
op|')'
newline|'\n'
name|'keypair'
op|'='
name|'self'
op|'.'
name|'_filter_keypair'
op|'('
name|'keypair'
op|','
name|'created_at'
op|'='
name|'True'
op|','
nl|'\n'
name|'deleted'
op|'='
name|'True'
op|','
name|'deleted_at'
op|'='
name|'True'
op|','
nl|'\n'
name|'id'
op|'='
name|'True'
op|','
name|'user_id'
op|'='
name|'True'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'KeypairNotFound'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'keypair'"
op|':'
name|'keypair'
op|'}'
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
string|'"""List of keypairs for a user."""'
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
name|'key_pairs'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_key_pairs'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'rval'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key_pair'
name|'in'
name|'key_pairs'
op|':'
newline|'\n'
indent|'            '
name|'rval'
op|'.'
name|'append'
op|'('
op|'{'
string|"'keypair'"
op|':'
name|'self'
op|'.'
name|'_filter_keypair'
op|'('
name|'key_pair'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'keypairs'"
op|':'
name|'rval'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
dedent|''
name|'class'
name|'Controller'
op|'('
name|'servers'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_add_key_name
indent|'    '
name|'def'
name|'_add_key_name'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'servers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'db_server'
op|'='
name|'req'
op|'.'
name|'get_db_instance'
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
comment|"# server['id'] is guaranteed to be in the cache due to"
nl|'\n'
comment|"# the core API adding it in its 'show'/'detail' methods."
nl|'\n'
name|'server'
op|'['
string|"'key_name'"
op|']'
op|'='
name|'db_server'
op|'['
string|"'key_name'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_show
dedent|''
dedent|''
name|'def'
name|'_show'
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
name|'if'
string|"'server'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_key_name'
op|'('
name|'req'
op|','
op|'['
name|'server'
op|']'
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
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'soft_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_show'
op|'('
name|'req'
op|','
name|'resp_obj'
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
string|"'servers'"
name|'in'
name|'resp_obj'
op|'.'
name|'obj'
name|'and'
name|'soft_authorize'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'servers'
op|'='
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_add_key_name'
op|'('
name|'req'
op|','
name|'servers'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Keypairs
dedent|''
dedent|''
dedent|''
name|'class'
name|'Keypairs'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keypair Support."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Keypairs"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-keypairs"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/keypairs/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-08-08T00:00:00Z"'
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
string|"'os-keypairs'"
op|','
nl|'\n'
name|'KeypairController'
op|'('
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
name|'controller'
op|'='
name|'Controller'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
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
string|"'servers'"
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
