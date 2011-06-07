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
name|'json'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'log'
name|'as'
name|'logging'
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
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.zones'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_filter_keys
name|'def'
name|'_filter_keys'
op|'('
name|'item'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Filters all model attributes except for keys\n    item is a dict\n\n    """'
newline|'\n'
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'item'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_exclude_keys
dedent|''
name|'def'
name|'_exclude_keys'
op|'('
name|'item'
op|','
name|'keys'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'item'
op|'.'
name|'iteritems'
op|'('
op|')'
name|'if'
name|'k'
name|'not'
name|'in'
name|'keys'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_scrub_zone
dedent|''
name|'def'
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_exclude_keys'
op|'('
name|'zone'
op|','
op|'('
string|"'username'"
op|','
string|"'password'"
op|','
string|"'created_at'"
op|','
nl|'\n'
string|"'deleted'"
op|','
string|"'deleted_at'"
op|','
string|"'updated_at'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|check_encryption_key
dedent|''
name|'def'
name|'check_encryption_key'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped
indent|'    '
name|'def'
name|'wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"--build_plan_encryption_key not set"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
dedent|''
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|index
indent|'    '
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
string|'"""Return all zones in brief"""'
newline|'\n'
comment|'# Ask the ZoneManager in the Scheduler for most recent data,'
nl|'\n'
comment|'# or fall-back to the database ...'
nl|'\n'
name|'items'
op|'='
name|'api'
op|'.'
name|'get_zone_list'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
name|'items'
op|'='
name|'common'
op|'.'
name|'limited'
op|'('
name|'items'
op|','
name|'req'
op|')'
newline|'\n'
name|'items'
op|'='
op|'['
name|'_scrub_zone'
op|'('
name|'item'
op|')'
name|'for'
name|'item'
name|'in'
name|'items'
op|']'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zones'
op|'='
name|'items'
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
string|'"""Return all zones in detail"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|info
dedent|''
name|'def'
name|'info'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return name and capabilities for this zone."""'
newline|'\n'
name|'items'
op|'='
name|'api'
op|'.'
name|'get_zone_capabilities'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'zone'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
name|'FLAGS'
op|'.'
name|'zone_name'
op|')'
newline|'\n'
name|'caps'
op|'='
name|'FLAGS'
op|'.'
name|'zone_capabilities'
newline|'\n'
name|'for'
name|'cap'
name|'in'
name|'caps'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|','
name|'value'
op|'='
name|'cap'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'zone'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'for'
name|'item'
op|','
op|'('
name|'min_value'
op|','
name|'max_value'
op|')'
name|'in'
name|'items'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'zone'
op|'['
name|'item'
op|']'
op|'='
string|'"%s,%s"'
op|'%'
op|'('
name|'min_value'
op|','
name|'max_value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'zone'
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
string|'"""Return data about the given zone id"""'
newline|'\n'
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'api'
op|'.'
name|'zone_get'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'zone_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
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
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'api'
op|'.'
name|'zone_delete'
op|'('
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|','
name|'zone_id'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'api'
op|'.'
name|'zone_create'
op|'('
name|'context'
op|','
name|'body'
op|'['
string|'"zone"'
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
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
name|'zone_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'api'
op|'.'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'body'
op|'['
string|'"zone"'
op|']'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'zone'
op|'='
name|'_scrub_zone'
op|'('
name|'zone'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'check_encryption_key'
newline|'\n'
DECL|member|select
name|'def'
name|'select'
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
string|'"""Returns a weighted list of costs to create instances\n           of desired capabilities."""'
newline|'\n'
name|'ctx'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'print'
string|'"**** ZONES "'
op|','
name|'body'
newline|'\n'
name|'specs'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
newline|'\n'
name|'build_plan'
op|'='
name|'api'
op|'.'
name|'select'
op|'('
name|'ctx'
op|','
name|'specs'
op|'='
name|'specs'
op|')'
newline|'\n'
name|'cooked'
op|'='
name|'self'
op|'.'
name|'_scrub_build_plan'
op|'('
name|'build_plan'
op|')'
newline|'\n'
name|'return'
op|'{'
string|'"weights"'
op|':'
name|'cooked'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_scrub_build_plan
dedent|''
name|'def'
name|'_scrub_build_plan'
op|'('
name|'self'
op|','
name|'build_plan'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove all the confidential data and return a sanitized\n        version of the build plan. Include an encrypted full version\n        of the weighting entry so we can get back to it later."""'
newline|'\n'
name|'encryptor'
op|'='
name|'crypto'
op|'.'
name|'encryptor'
op|'('
name|'FLAGS'
op|'.'
name|'build_plan_encryption_key'
op|')'
newline|'\n'
name|'cooked'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'build_plan'
op|':'
newline|'\n'
indent|'            '
name|'json_entry'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'entry'
op|')'
newline|'\n'
name|'cipher_text'
op|'='
name|'encryptor'
op|'('
name|'json_entry'
op|')'
newline|'\n'
name|'cooked'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'weight'
op|'='
name|'entry'
op|'['
string|"'weight'"
op|']'
op|','
nl|'\n'
name|'blob'
op|'='
name|'cipher_text'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cooked'
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
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"zone"'
op|':'
op|'['
string|'"id"'
op|','
string|'"api_url"'
op|','
string|'"name"'
op|','
string|'"capabilities"'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V10'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|','
name|'serializers'
op|'='
name|'serializers'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
