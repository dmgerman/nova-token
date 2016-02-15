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
string|'"""\nTests for database migrations.\nThere are "opportunistic" tests which allows testing against all 3 databases\n(sqlite in memory, mysql, pg) in a properly configured unit test environment.\n\nFor the opportunistic testing you need to set up db\'s named \'openstack_citest\'\nwith user \'openstack_citest\' and password \'openstack_citest\' on localhost. The\ntest will then use that db and u/p combo to run the tests.\n\nFor postgres on Ubuntu this can be done with the following commands::\n\n| sudo -u postgres psql\n| postgres=# create user openstack_citest with createdb login password\n|       \'openstack_citest\';\n| postgres=# create database openstack_citest with owner openstack_citest;\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'repository'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'test_migrations'
newline|'\n'
name|'from'
name|'oslo_db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'utils'
name|'as'
name|'db_utils'
newline|'\n'
name|'import'
name|'sqlalchemy'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'engine'
name|'import'
name|'reflection'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'api_migrations'
name|'import'
name|'migrate_repo'
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
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'migration'
name|'as'
name|'sa_migration'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaAPIModelsSync
name|'class'
name|'NovaAPIModelsSync'
op|'('
name|'test_migrations'
op|'.'
name|'ModelsMigrationsSync'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test that the models match the database after migrations are run."""'
newline|'\n'
nl|'\n'
DECL|member|db_sync
name|'def'
name|'db_sync'
op|'('
name|'self'
op|','
name|'engine'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'sa_migration'
op|','
string|"'get_engine'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'engine'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'sa_migration'
op|'.'
name|'db_sync'
op|'('
name|'database'
op|'='
string|"'api'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|migrate_engine
name|'def'
name|'migrate_engine'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'engine'
newline|'\n'
nl|'\n'
DECL|member|get_engine
dedent|''
name|'def'
name|'get_engine'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'migrate_engine'
newline|'\n'
nl|'\n'
DECL|member|get_metadata
dedent|''
name|'def'
name|'get_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'api_models'
op|'.'
name|'API_BASE'
op|'.'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|member|include_object
dedent|''
name|'def'
name|'include_object'
op|'('
name|'self'
op|','
name|'object_'
op|','
name|'name'
op|','
name|'type_'
op|','
name|'reflected'
op|','
name|'compare_to'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'type_'
op|'=='
string|"'table'"
op|':'
newline|'\n'
comment|'# migrate_version is a sqlalchemy-migrate control table and'
nl|'\n'
comment|"# isn't included in the model."
nl|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
string|"'migrate_version'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestNovaAPIMigrationsSQLite'
op|'('
name|'NovaAPIModelsSync'
op|','
nl|'\n'
name|'test_base'
op|'.'
name|'DbTestCase'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsSQLite
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestNovaAPIMigrationsMySQL'
op|'('
name|'NovaAPIModelsSync'
op|','
nl|'\n'
name|'test_base'
op|'.'
name|'MySQLOpportunisticTestCase'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsMySQL
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestNovaAPIMigrationsPostgreSQL'
op|'('
name|'NovaAPIModelsSync'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsPostgreSQL
name|'test_base'
op|'.'
name|'PostgreSQLOpportunisticTestCase'
op|','
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaAPIMigrationsWalk
dedent|''
name|'class'
name|'NovaAPIMigrationsWalk'
op|'('
name|'test_migrations'
op|'.'
name|'WalkVersionsMixin'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NovaAPIMigrationsWalk'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(viktors): We should reduce log output because it causes issues,'
nl|'\n'
comment|'#                when we run tests with testr'
nl|'\n'
name|'migrate_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'migrate'"
op|')'
newline|'\n'
name|'old_level'
op|'='
name|'migrate_log'
op|'.'
name|'level'
newline|'\n'
name|'migrate_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARN'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'migrate_log'
op|'.'
name|'setLevel'
op|','
name|'old_level'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|INIT_VERSION
name|'def'
name|'INIT_VERSION'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'migration'
op|'.'
name|'db_initial_version'
op|'('
string|"'api'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|REPOSITORY
name|'def'
name|'REPOSITORY'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'repository'
op|'.'
name|'Repository'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'migrate_repo'
op|'.'
name|'__file__'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|migration_api
name|'def'
name|'migration_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'sa_migration'
op|'.'
name|'versioning_api'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|migrate_engine
name|'def'
name|'migrate_engine'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'engine'
newline|'\n'
nl|'\n'
DECL|member|test_walk_versions
dedent|''
name|'def'
name|'test_walk_versions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'walk_versions'
op|'('
name|'snake_walk'
op|'='
name|'False'
op|','
name|'downgrade'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertColumnExists
dedent|''
name|'def'
name|'assertColumnExists'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'table_name'
op|','
name|'column'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'db_utils'
op|'.'
name|'column_exists'
op|'('
name|'engine'
op|','
name|'table_name'
op|','
name|'column'
op|')'
op|','
nl|'\n'
string|"'Column %s.%s does not exist'"
op|'%'
op|'('
name|'table_name'
op|','
name|'column'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertIndexExists
dedent|''
name|'def'
name|'assertIndexExists'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'table_name'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'db_utils'
op|'.'
name|'index_exists'
op|'('
name|'engine'
op|','
name|'table_name'
op|','
name|'index'
op|')'
op|','
nl|'\n'
string|"'Index %s on table %s does not exist'"
op|'%'
nl|'\n'
op|'('
name|'index'
op|','
name|'table_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertUniqueConstraintExists
dedent|''
name|'def'
name|'assertUniqueConstraintExists'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'table_name'
op|','
name|'columns'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inspector'
op|'='
name|'reflection'
op|'.'
name|'Inspector'
op|'.'
name|'from_engine'
op|'('
name|'engine'
op|')'
newline|'\n'
name|'constrs'
op|'='
name|'inspector'
op|'.'
name|'get_unique_constraints'
op|'('
name|'table_name'
op|')'
newline|'\n'
name|'constr_columns'
op|'='
op|'['
name|'constr'
op|'['
string|"'column_names'"
op|']'
name|'for'
name|'constr'
name|'in'
name|'constrs'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'columns'
op|','
name|'constr_columns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertTableNotExists
dedent|''
name|'def'
name|'assertTableNotExists'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'table_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'sqlalchemy'
op|'.'
name|'exc'
op|'.'
name|'NoSuchTableError'
op|','
nl|'\n'
name|'db_utils'
op|'.'
name|'get_table'
op|','
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_001
dedent|''
name|'def'
name|'_check_001'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'column'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'id'"
op|','
string|"'uuid'"
op|','
string|"'name'"
op|','
nl|'\n'
string|"'transport_url'"
op|','
string|"'database_connection'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertColumnExists'
op|'('
name|'engine'
op|','
string|"'cell_mappings'"
op|','
name|'column'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertIndexExists'
op|'('
name|'engine'
op|','
string|"'cell_mappings'"
op|','
string|"'uuid_idx'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertUniqueConstraintExists'
op|'('
name|'engine'
op|','
string|"'cell_mappings'"
op|','
nl|'\n'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_002
dedent|''
name|'def'
name|'_check_002'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'column'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'id'"
op|','
string|"'instance_uuid'"
op|','
nl|'\n'
string|"'cell_id'"
op|','
string|"'project_id'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertColumnExists'
op|'('
name|'engine'
op|','
string|"'instance_mappings'"
op|','
name|'column'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'index'
name|'in'
op|'['
string|"'instance_uuid_idx'"
op|','
string|"'project_id_idx'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIndexExists'
op|'('
name|'engine'
op|','
string|"'instance_mappings'"
op|','
name|'index'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertUniqueConstraintExists'
op|'('
name|'engine'
op|','
string|"'instance_mappings'"
op|','
nl|'\n'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'inspector'
op|'='
name|'reflection'
op|'.'
name|'Inspector'
op|'.'
name|'from_engine'
op|'('
name|'engine'
op|')'
newline|'\n'
comment|'# There should only be one foreign key here'
nl|'\n'
name|'fk'
op|'='
name|'inspector'
op|'.'
name|'get_foreign_keys'
op|'('
string|"'instance_mappings'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cell_mappings'"
op|','
name|'fk'
op|'['
string|"'referred_table'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'id'"
op|']'
op|','
name|'fk'
op|'['
string|"'referred_columns'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'cell_id'"
op|']'
op|','
name|'fk'
op|'['
string|"'constrained_columns'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_003
dedent|''
name|'def'
name|'_check_003'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'column'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'id'"
op|','
nl|'\n'
string|"'cell_id'"
op|','
string|"'host'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertColumnExists'
op|'('
name|'engine'
op|','
string|"'host_mappings'"
op|','
name|'column'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertIndexExists'
op|'('
name|'engine'
op|','
string|"'host_mappings'"
op|','
string|"'host_idx'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertUniqueConstraintExists'
op|'('
name|'engine'
op|','
string|"'host_mappings'"
op|','
nl|'\n'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'inspector'
op|'='
name|'reflection'
op|'.'
name|'Inspector'
op|'.'
name|'from_engine'
op|'('
name|'engine'
op|')'
newline|'\n'
comment|'# There should only be one foreign key here'
nl|'\n'
name|'fk'
op|'='
name|'inspector'
op|'.'
name|'get_foreign_keys'
op|'('
string|"'host_mappings'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cell_mappings'"
op|','
name|'fk'
op|'['
string|"'referred_table'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'id'"
op|']'
op|','
name|'fk'
op|'['
string|"'referred_columns'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'cell_id'"
op|']'
op|','
name|'fk'
op|'['
string|"'constrained_columns'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_004
dedent|''
name|'def'
name|'_check_004'
op|'('
name|'self'
op|','
name|'engine'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'columns'
op|'='
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'id'"
op|','
string|"'instance_uuid'"
op|','
string|"'spec'"
op|']'
newline|'\n'
name|'for'
name|'column'
name|'in'
name|'columns'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertColumnExists'
op|'('
name|'engine'
op|','
string|"'request_specs'"
op|','
name|'column'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertUniqueConstraintExists'
op|'('
name|'engine'
op|','
string|"'request_specs'"
op|','
nl|'\n'
op|'['
string|"'instance_uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'engine'
op|'.'
name|'name'
op|'!='
string|"'ibm_db_sa'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIndexExists'
op|'('
name|'engine'
op|','
string|"'request_specs'"
op|','
nl|'\n'
string|"'request_spec_instance_uuid_idx'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestNovaAPIMigrationsWalkSQLite'
op|'('
name|'NovaAPIMigrationsWalk'
op|','
nl|'\n'
name|'test_base'
op|'.'
name|'DbTestCase'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsWalkSQLite
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestNovaAPIMigrationsWalkMySQL'
op|'('
name|'NovaAPIMigrationsWalk'
op|','
nl|'\n'
name|'test_base'
op|'.'
name|'MySQLOpportunisticTestCase'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsWalkMySQL
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestNovaAPIMigrationsWalkPostgreSQL'
op|'('
name|'NovaAPIMigrationsWalk'
op|','
nl|'\n'
DECL|class|TestNovaAPIMigrationsWalkPostgreSQL
name|'test_base'
op|'.'
name|'PostgreSQLOpportunisticTestCase'
op|','
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
