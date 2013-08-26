begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'availability_zones'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Service
name|'class'
name|'Service'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'report_count'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'bool'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'utils'
op|'.'
name|'str_or_none'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'db_service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'allow_missing'
op|'='
op|'('
string|"'availability_zone'"
op|','
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'service'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'allow_missing'
name|'and'
name|'key'
name|'not'
name|'in'
name|'db_service'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'service'
op|'['
name|'key'
op|']'
op|'='
name|'db_service'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'service'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'service'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'service'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host_and_topic
name|'def'
name|'get_by_host_and_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_host_and_topic'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_compute_host
name|'def'
name|'get_by_compute_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_args
name|'def'
name|'get_by_args'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
name|'key'
op|']'
op|'='
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'db_service'
op|'='
name|'db'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'self'
op|','
name|'db_service'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|destroy
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_list
dedent|''
dedent|''
name|'def'
name|'_make_list'
op|'('
name|'context'
op|','
name|'list_obj'
op|','
name|'item_cls'
op|','
name|'db_list'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'list_obj'
op|'.'
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'db_item'
name|'in'
name|'db_list'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'item_cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'item_cls'
op|'('
op|')'
op|','
name|'db_item'
op|')'
newline|'\n'
name|'list_obj'
op|'.'
name|'objects'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
name|'list_obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'list_obj'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceList
dedent|''
name|'class'
name|'ServiceList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_topic
name|'def'
name|'get_by_topic'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
name|'_make_list'
op|'('
name|'context'
op|','
name|'ServiceList'
op|'('
op|')'
op|','
name|'Service'
op|','
name|'db_services'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_host
name|'def'
name|'get_by_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'return'
name|'_make_list'
op|'('
name|'context'
op|','
name|'ServiceList'
op|'('
op|')'
op|','
name|'Service'
op|','
name|'db_services'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_all
name|'def'
name|'get_all'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'disabled'
op|'='
name|'None'
op|','
name|'set_zones'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'disabled'
op|'='
name|'disabled'
op|')'
newline|'\n'
name|'if'
name|'set_zones'
op|':'
newline|'\n'
indent|'            '
name|'db_services'
op|'='
name|'availability_zones'
op|'.'
name|'set_availability_zones'
op|'('
nl|'\n'
name|'context'
op|','
name|'db_services'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_make_list'
op|'('
name|'context'
op|','
name|'ServiceList'
op|'('
op|')'
op|','
name|'Service'
op|','
name|'db_services'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
