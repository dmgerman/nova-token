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
DECL|class|Migration
name|'class'
name|'Migration'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
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
string|"'source_compute'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'source_node'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dest_node'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'dest_host'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'fields'
op|'.'
name|'StringField'
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
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'migration'
op|','
name|'db_migration'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'key'
name|'in'
name|'migration'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'migration'
op|'['
name|'key'
op|']'
op|'='
name|'db_migration'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'migration'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'migration'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'migration'
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
name|'migration_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migration'
op|'='
name|'db'
op|'.'
name|'migration_get'
op|'('
name|'context'
op|','
name|'migration_id'
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
name|'db_migration'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_and_status
name|'def'
name|'get_by_instance_and_status'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migration'
op|'='
name|'db'
op|'.'
name|'migration_get_by_instance_and_status'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance_uuid'
op|','
name|'status'
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
name|'db_migration'
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
name|'updates'
op|'='
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
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
name|'db_migration'
op|'='
name|'db'
op|'.'
name|'migration_create'
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
name|'db_migration'
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
name|'self'
op|'.'
name|'obj_get_changes'
op|'('
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
name|'db_migration'
op|'='
name|'db'
op|'.'
name|'migration_update'
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
name|'db_migration'
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
name|'property'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'objects'
op|'.'
name|'Instance'
op|'.'
name|'get_by_uuid'
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
DECL|class|MigrationList
dedent|''
dedent|''
name|'class'
name|'MigrationList'
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
comment|'#              Migration <= 1.1'
nl|'\n'
comment|'# Version 1.1: Added use_slave to get_unconfirmed_by_dest_compute'
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
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'Migration'"
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
comment|'# NOTE(danms): Migration was at 1.1 before we added this'
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_unconfirmed_by_dest_compute
name|'def'
name|'get_unconfirmed_by_dest_compute'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'confirm_window'
op|','
nl|'\n'
name|'dest_compute'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migrations'
op|'='
name|'db'
op|'.'
name|'migration_get_unconfirmed_by_dest_compute'
op|'('
nl|'\n'
name|'context'
op|','
name|'confirm_window'
op|','
name|'dest_compute'
op|','
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'MigrationList'
op|'('
op|')'
op|','
name|'Migration'
op|','
nl|'\n'
name|'db_migrations'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_in_progress_by_host_and_node
name|'def'
name|'get_in_progress_by_host_and_node'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migrations'
op|'='
name|'db'
op|'.'
name|'migration_get_in_progress_by_host_and_node'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'MigrationList'
op|'('
op|')'
op|','
name|'Migration'
op|','
nl|'\n'
name|'db_migrations'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_filters
name|'def'
name|'get_by_filters'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_migrations'
op|'='
name|'db'
op|'.'
name|'migration_get_all_by_filters'
op|'('
name|'context'
op|','
name|'filters'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'MigrationList'
op|'('
op|')'
op|','
name|'Migration'
op|','
nl|'\n'
name|'db_migrations'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
