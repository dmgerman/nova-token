begin_unit
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
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'db_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api_models'
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
DECL|class|InstanceMapping
name|'class'
name|'InstanceMapping'
op|'('
name|'base'
op|'.'
name|'NovaTimestampObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
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
name|'read_only'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'cell_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
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
name|'instance_mapping'
op|','
name|'db_instance_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'instance_mapping'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'instance_mapping'
op|','
name|'key'
op|','
name|'db_instance_mapping'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'instance_mapping'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'instance_mapping'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'return'
name|'instance_mapping'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_by_instance_uuid_from_db
name|'def'
name|'_get_by_instance_uuid_from_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_api'
op|'.'
name|'get_api_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_mapping'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
nl|'\n'
name|'api_models'
op|'.'
name|'InstanceMapping'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_mapping'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceMappingNotFound'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'db_mapping'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid
name|'def'
name|'get_by_instance_uuid'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mapping'
op|'='
name|'cls'
op|'.'
name|'_get_by_instance_uuid_from_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
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
name|'db_mapping'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_create_in_db
name|'def'
name|'_create_in_db'
op|'('
name|'context'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_api'
op|'.'
name|'get_api_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db_mapping'
op|'='
name|'api_models'
op|'.'
name|'InstanceMapping'
op|'('
op|')'
newline|'\n'
name|'db_mapping'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'db_mapping'
op|'.'
name|'save'
op|'('
name|'session'
op|')'
newline|'\n'
name|'return'
name|'db_mapping'
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
name|'db_mapping'
op|'='
name|'self'
op|'.'
name|'_create_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
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
name|'db_mapping'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_save_in_db
name|'def'
name|'_save_in_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_api'
op|'.'
name|'get_api_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_mapping'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
nl|'\n'
name|'api_models'
op|'.'
name|'InstanceMapping'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'db_mapping'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceMappingNotFound'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'db_mapping'
op|'.'
name|'update'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'add'
op|'('
name|'db_mapping'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'db_mapping'
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
name|'changes'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
op|')'
newline|'\n'
name|'db_mapping'
op|'='
name|'self'
op|'.'
name|'_save_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'changes'
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
name|'db_mapping'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_destroy_in_db
name|'def'
name|'_destroy_in_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_api'
op|'.'
name|'get_api_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'InstanceMapping'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceMappingNotFound'
op|'('
name|'uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
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
name|'self'
op|'.'
name|'_destroy_in_db'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceMappingList
dedent|''
dedent|''
name|'class'
name|'InstanceMappingList'
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
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
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
string|"'InstanceMapping'"
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
string|"'1.0'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_by_project_id_from_db
name|'def'
name|'_get_by_project_id_from_db'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'db_api'
op|'.'
name|'get_api_session'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'session'
op|'.'
name|'begin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db_mappings'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'api_models'
op|'.'
name|'InstanceMapping'
op|')'
op|'.'
name|'filter_by'
op|'('
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|')'
op|'.'
name|'all'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db_mappings'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_project_id
name|'def'
name|'get_by_project_id'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_mappings'
op|'='
name|'cls'
op|'.'
name|'_get_by_project_id_from_db'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'objects'
op|'.'
name|'InstanceMapping'
op|','
nl|'\n'
name|'db_mappings'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
