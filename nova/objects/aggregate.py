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
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
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
name|'objects'
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
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'Aggregate'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|Aggregate
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: String attributes updated to support unicode'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hosts'"
op|':'
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|obj_extra_fields
name|'obj_extra_fields'
op|'='
op|'['
string|"'availability_zone'"
op|']'
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
name|'aggregate'
op|','
name|'db_aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'aggregate'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'=='
string|"'metadata'"
op|':'
newline|'\n'
indent|'                '
name|'db_key'
op|'='
string|"'metadetails'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'db_key'
op|'='
name|'key'
newline|'\n'
dedent|''
name|'aggregate'
op|'['
name|'key'
op|']'
op|'='
name|'db_aggregate'
op|'['
name|'db_key'
op|']'
newline|'\n'
dedent|''
name|'aggregate'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'aggregate'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'aggregate'
newline|'\n'
nl|'\n'
DECL|member|_assert_no_hosts
dedent|''
name|'def'
name|'_assert_no_hosts'
op|'('
name|'self'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'hosts'"
name|'in'
name|'self'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
nl|'\n'
name|'action'
op|'='
name|'action'
op|','
nl|'\n'
name|'reason'
op|'='
string|"'hosts updated inline'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_aggregate'
op|'='
name|'db'
op|'.'
name|'aggregate_get'
op|'('
name|'context'
op|','
name|'aggregate_id'
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
name|'db_aggregate'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'obj_attr_is_set'
op|'('
string|"'id'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ObjectActionError'
op|'('
name|'action'
op|'='
string|"'create'"
op|','
nl|'\n'
name|'reason'
op|'='
string|"'already created'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_assert_no_hosts'
op|'('
string|"'create'"
op|')'
newline|'\n'
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'if'
string|"'metadata'"
name|'in'
name|'updates'
op|':'
newline|'\n'
comment|'# NOTE(danms): For some reason the notification format is weird'
nl|'\n'
indent|'            '
name|'payload'
op|'['
string|"'meta_data'"
op|']'
op|'='
name|'payload'
op|'.'
name|'pop'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
dedent|''
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"create.start"'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'metadata'"
op|','
name|'None'
op|')'
newline|'\n'
name|'db_aggregate'
op|'='
name|'db'
op|'.'
name|'aggregate_create'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'updates'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_aggregate'
op|')'
newline|'\n'
name|'payload'
op|'['
string|"'aggregate_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'id'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"create.end"'
op|','
nl|'\n'
name|'payload'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_assert_no_hosts'
op|'('
string|"'save'"
op|')'
newline|'\n'
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'payload'
op|'='
op|'{'
string|"'aggregate_id'"
op|':'
name|'self'
op|'.'
name|'id'
op|'}'
newline|'\n'
name|'if'
string|"'metadata'"
name|'in'
name|'updates'
op|':'
newline|'\n'
indent|'            '
name|'payload'
op|'['
string|"'meta_data'"
op|']'
op|'='
name|'updates'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
dedent|''
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"updateprop.start"'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
name|'updates'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'db_aggregate'
op|'='
name|'db'
op|'.'
name|'aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"updateprop.end"'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_aggregate'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|update_metadata
name|'def'
name|'update_metadata'
op|'('
name|'self'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'='
op|'{'
string|"'aggregate_id'"
op|':'
name|'self'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'meta_data'"
op|':'
name|'updates'
op|'}'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"updatemetadata.start"'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
name|'to_add'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'updates'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateMetadataNotFound'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'metadata'
op|'.'
name|'pop'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'to_add'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'metadata'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'db'
op|'.'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'to_add'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_aggregate_update'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
nl|'\n'
string|'"updatemetadata.end"'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
name|'fields'
op|'='
op|'['
string|"'metadata'"
op|']'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'aggregate_delete'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|add_host
name|'def'
name|'add_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'aggregate_host_add'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'host'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'hosts'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
name|'fields'
op|'='
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|delete_host
name|'def'
name|'delete_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'id'
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'hosts'
op|'.'
name|'remove'
op|'('
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
name|'fields'
op|'='
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|availability_zone
name|'def'
name|'availability_zone'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|AggregateList
name|'class'
name|'AggregateList'
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
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added key argument to get_by_host()'
nl|'\n'
comment|'#              Aggregate <= version 1.1'
nl|'\n'
comment|'# Version 1.2: Added get_by_metadata_key'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Aggregate'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
comment|'# NOTE(danms): Aggregate was at 1.1 before we added this'
nl|'\n'
string|"'1.2'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_filter_db_aggregates
name|'def'
name|'_filter_db_aggregates'
op|'('
name|'cls'
op|','
name|'db_aggregates'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'hosts'
op|','
name|'set'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'hosts'
op|'='
name|'set'
op|'('
name|'hosts'
op|')'
newline|'\n'
dedent|''
name|'filtered_aggregates'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'db_aggregate'
name|'in'
name|'db_aggregates'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'host'
name|'in'
name|'db_aggregate'
op|'['
string|"'hosts'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'host'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'                    '
name|'filtered_aggregates'
op|'.'
name|'append'
op|'('
name|'db_aggregate'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'filtered_aggregates'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_aggregates'
op|'='
name|'db'
op|'.'
name|'aggregate_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Aggregate'
op|','
nl|'\n'
name|'db_aggregates'
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
op|','
name|'key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_aggregates'
op|'='
name|'db'
op|'.'
name|'aggregate_get_by_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'key'
op|'='
name|'key'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Aggregate'
op|','
nl|'\n'
name|'db_aggregates'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_metadata_key
name|'def'
name|'get_by_metadata_key'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'key'
op|','
name|'hosts'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_aggregates'
op|'='
name|'db'
op|'.'
name|'aggregate_get_by_metadata_key'
op|'('
name|'context'
op|','
name|'key'
op|'='
name|'key'
op|')'
newline|'\n'
name|'if'
name|'hosts'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'db_aggregates'
op|'='
name|'cls'
op|'.'
name|'_filter_db_aggregates'
op|'('
name|'db_aggregates'
op|','
name|'hosts'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
name|'context'
op|')'
op|','
name|'objects'
op|'.'
name|'Aggregate'
op|','
nl|'\n'
name|'db_aggregates'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
