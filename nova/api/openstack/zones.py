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
name|'common'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'_filter_keys'
op|'('
name|'zone'
op|','
op|'('
string|"'id'"
op|','
string|"'api_url'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Controller
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
op|'}'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'if'
name|'not'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'items'
op|'='
name|'db'
op|'.'
name|'zone_get_all'
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
dedent|''
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
name|'_exclude_keys'
op|'('
name|'item'
op|','
op|'['
string|"'username'"
op|','
string|"'password'"
op|']'
op|')'
nl|'\n'
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
name|'key_values'
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
name|'key_values'
op|'['
number|'0'
op|']'
op|']'
op|'='
name|'key_values'
op|'['
number|'1'
op|']'
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
name|'db'
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
name|'db'
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
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
newline|'\n'
name|'zone'
op|'='
name|'db'
op|'.'
name|'zone_create'
op|'('
name|'context'
op|','
name|'env'
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
name|'env'
op|'='
name|'self'
op|'.'
name|'_deserialize'
op|'('
name|'req'
op|'.'
name|'body'
op|','
name|'req'
op|'.'
name|'get_content_type'
op|'('
op|')'
op|')'
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
name|'db'
op|'.'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'env'
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
dedent|''
dedent|''
endmarker|''
end_unit
