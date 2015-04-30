begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'importlib'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'migrate'
name|'import'
name|'exceptions'
name|'as'
name|'versioning_exceptions'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
name|'UniqueConstraint'
newline|'\n'
name|'from'
name|'migrate'
op|'.'
name|'versioning'
name|'import'
name|'api'
name|'as'
name|'versioning_api'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'migration'
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
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNullInstanceUuidScanDB
name|'class'
name|'TestNullInstanceUuidScanDB'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# NOTE(mriedem): Copied from the 267 database migration.'
nl|'\n'
DECL|member|downgrade
indent|'    '
name|'def'
name|'downgrade'
op|'('
name|'self'
op|','
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'UniqueConstraint'
op|'('
string|"'uuid'"
op|','
nl|'\n'
name|'table'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'migrate_engine'
op|','
string|"'instances'"
op|')'
op|','
nl|'\n'
name|'name'
op|'='
string|"'uniq_instances0uuid'"
op|')'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'for'
name|'table_name'
name|'in'
op|'('
string|"'instances'"
op|','
string|"'shadow_instances'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'migrate_engine'
op|','
name|'table_name'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'columns'
op|'.'
name|'uuid'
op|'.'
name|'alter'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
dedent|''
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
name|'TestNullInstanceUuidScanDB'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'engine'
op|'='
name|'db_api'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
comment|"# When this test runs, we've already run the schema migration to make"
nl|'\n'
comment|'# instances.uuid non-nullable, so we have to alter the table here'
nl|'\n'
comment|'# so we can test against a real database.'
nl|'\n'
name|'self'
op|'.'
name|'downgrade'
op|'('
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
comment|'# Now create fake entries in the fixed_ips, consoles and'
nl|'\n'
comment|'# instances table where (instance_)uuid is None for testing.'
nl|'\n'
name|'for'
name|'table_name'
name|'in'
op|'('
string|"'fixed_ips'"
op|','
string|"'instances'"
op|','
string|"'consoles'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
name|'fake_record'
op|'='
op|'{'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'table'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
name|'fake_record'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_db_null_instance_uuid_scan_readonly
dedent|''
dedent|''
name|'def'
name|'test_db_null_instance_uuid_scan_readonly'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'results'
op|'='
name|'migration'
op|'.'
name|'db_null_instance_uuid_scan'
op|'('
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'instances'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'consoles'"
op|')'
op|')'
newline|'\n'
comment|'# The fixed_ips table should be ignored.'
nl|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'fixed_ips'"
op|','
name|'results'
op|')'
newline|'\n'
comment|"# Now pick a random table with an instance_uuid column and show it's"
nl|'\n'
comment|'# in the results but with 0 hits.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'instance_info_caches'"
op|')'
op|')'
newline|'\n'
comment|'# Make sure nothing was deleted.'
nl|'\n'
name|'for'
name|'table_name'
name|'in'
op|'('
string|"'fixed_ips'"
op|','
string|"'instances'"
op|','
string|"'consoles'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'table'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
name|'table_name'
op|')'
newline|'\n'
name|'record'
op|'='
name|'table'
op|'.'
name|'select'
op|'('
name|'table'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
number|'1'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_db_null_instance_uuid_scan_delete
dedent|''
dedent|''
name|'def'
name|'test_db_null_instance_uuid_scan_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'results'
op|'='
name|'migration'
op|'.'
name|'db_null_instance_uuid_scan'
op|'('
name|'delete'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'instances'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'consoles'"
op|')'
op|')'
newline|'\n'
comment|'# The fixed_ips table should be ignored.'
nl|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'fixed_ips'"
op|','
name|'results'
op|')'
newline|'\n'
comment|"# Now pick a random table with an instance_uuid column and show it's"
nl|'\n'
comment|'# in the results but with 0 hits.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'results'
op|'.'
name|'get'
op|'('
string|"'instance_info_caches'"
op|')'
op|')'
newline|'\n'
comment|"# Make sure fixed_ips wasn't touched, but instances and instance_faults"
nl|'\n'
comment|'# records were deleted.'
nl|'\n'
name|'fixed_ips'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
string|"'fixed_ips'"
op|')'
newline|'\n'
name|'record'
op|'='
name|'fixed_ips'
op|'.'
name|'select'
op|'('
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
number|'1'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
name|'consoles'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
string|"'consoles'"
op|')'
newline|'\n'
name|'record'
op|'='
name|'consoles'
op|'.'
name|'select'
op|'('
name|'consoles'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
number|'1'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
name|'db_utils'
op|'.'
name|'get_table'
op|'('
name|'self'
op|'.'
name|'engine'
op|','
string|"'instances'"
op|')'
newline|'\n'
name|'record'
op|'='
name|'instances'
op|'.'
name|'select'
op|'('
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
number|'1'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'record'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'db_version'"
op|','
name|'return_value'
op|'='
number|'2'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'_find_migrate_repo'"
op|','
name|'return_value'
op|'='
string|"'repo'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'versioning_api'
op|','
string|"'upgrade'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'versioning_api'
op|','
string|"'downgrade'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'get_engine'"
op|','
name|'return_value'
op|'='
string|"'engine'"
op|')'
newline|'\n'
DECL|class|TestDbSync
name|'class'
name|'TestDbSync'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_version_none
indent|'    '
name|'def'
name|'test_version_none'
op|'('
name|'self'
op|','
name|'mock_get_engine'
op|','
name|'mock_downgrade'
op|','
name|'mock_upgrade'
op|','
nl|'\n'
name|'mock_find_repo'
op|','
name|'mock_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'database'
op|'='
string|"'fake'"
newline|'\n'
name|'migration'
op|'.'
name|'db_sync'
op|'('
name|'database'
op|'='
name|'database'
op|')'
newline|'\n'
name|'mock_version'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_find_repo'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_upgrade'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'engine'"
op|','
string|"'repo'"
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_downgrade'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_downgrade
dedent|''
name|'def'
name|'test_downgrade'
op|'('
name|'self'
op|','
name|'mock_get_engine'
op|','
name|'mock_downgrade'
op|','
name|'mock_upgrade'
op|','
nl|'\n'
name|'mock_find_repo'
op|','
name|'mock_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'database'
op|'='
string|"'fake'"
newline|'\n'
name|'migration'
op|'.'
name|'db_sync'
op|'('
number|'1'
op|','
name|'database'
op|'='
name|'database'
op|')'
newline|'\n'
name|'mock_version'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_find_repo'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_downgrade'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'engine'"
op|','
string|"'repo'"
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_upgrade'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'_find_migrate_repo'"
op|','
name|'return_value'
op|'='
string|"'repo'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'versioning_api'
op|','
string|"'db_version'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'get_engine'"
op|')'
newline|'\n'
DECL|class|TestDbVersion
name|'class'
name|'TestDbVersion'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_db_version
indent|'    '
name|'def'
name|'test_db_version'
op|'('
name|'self'
op|','
name|'mock_get_engine'
op|','
name|'mock_db_version'
op|','
nl|'\n'
name|'mock_find_repo'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'database'
op|'='
string|"'fake'"
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'return_value'
op|'='
string|"'engine'"
newline|'\n'
name|'migration'
op|'.'
name|'db_version'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_find_repo'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_db_version'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'engine'"
op|','
string|"'repo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_controlled
dedent|''
name|'def'
name|'test_not_controlled'
op|'('
name|'self'
op|','
name|'mock_get_engine'
op|','
name|'mock_db_version'
op|','
nl|'\n'
name|'mock_find_repo'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'database'
op|'='
string|"'api'"
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'side_effect'
op|'='
op|'['
string|"'engine'"
op|','
string|"'engine'"
op|','
string|"'engine'"
op|']'
newline|'\n'
name|'exc'
op|'='
name|'versioning_exceptions'
op|'.'
name|'DatabaseNotControlledError'
op|'('
op|')'
newline|'\n'
name|'mock_db_version'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'exc'
op|','
string|"''"
op|']'
newline|'\n'
name|'metadata'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'.'
name|'tables'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'sqlalchemy'
op|','
string|"'MetaData'"
op|','
nl|'\n'
name|'metadata'
op|')'
op|','
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
nl|'\n'
string|"'db_version_control'"
op|')'
name|'as'
name|'mock_version_control'
op|':'
newline|'\n'
indent|'            '
name|'migration'
op|'.'
name|'db_version'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_version_control'
op|'.'
name|'assert_called_once_with'
op|'('
number|'0'
op|','
name|'database'
op|')'
newline|'\n'
name|'db_version_calls'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'engine'"
op|','
string|"'repo'"
op|')'
op|']'
op|'*'
number|'2'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_version_calls'
op|','
name|'mock_db_version'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
dedent|''
name|'engine_calls'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'database'
op|')'
op|']'
op|'*'
number|'3'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'engine_calls'
op|','
name|'mock_get_engine'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'_find_migrate_repo'"
op|','
name|'return_value'
op|'='
string|"'repo'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'migration'
op|','
string|"'get_engine'"
op|','
name|'return_value'
op|'='
string|"'engine'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'versioning_api'
op|','
string|"'version_control'"
op|')'
newline|'\n'
DECL|class|TestDbVersionControl
name|'class'
name|'TestDbVersionControl'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_version_control
indent|'    '
name|'def'
name|'test_version_control'
op|'('
name|'self'
op|','
name|'mock_version_control'
op|','
name|'mock_get_engine'
op|','
nl|'\n'
name|'mock_find_repo'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'database'
op|'='
string|"'fake'"
newline|'\n'
name|'migration'
op|'.'
name|'db_version_control'
op|'('
name|'database'
op|'='
name|'database'
op|')'
newline|'\n'
name|'mock_find_repo'
op|'.'
name|'assert_called_once_with'
op|'('
name|'database'
op|')'
newline|'\n'
name|'mock_version_control'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'engine'"
op|','
string|"'repo'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGetEngine
dedent|''
dedent|''
name|'class'
name|'TestGetEngine'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_get_main_engine
indent|'    '
name|'def'
name|'test_get_main_engine'
op|'('
name|'self'
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
name|'db_api'
op|','
string|"'get_engine'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'engine'"
op|')'
name|'as'
name|'mock_get_engine'
op|':'
newline|'\n'
indent|'            '
name|'engine'
op|'='
name|'migration'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'engine'"
op|','
name|'engine'
op|')'
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_api_engine
dedent|''
dedent|''
name|'def'
name|'test_get_api_engine'
op|'('
name|'self'
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
name|'db_api'
op|','
string|"'get_api_engine'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|"'api_engine'"
op|')'
name|'as'
name|'mock_get_engine'
op|':'
newline|'\n'
indent|'            '
name|'engine'
op|'='
name|'migration'
op|'.'
name|'get_engine'
op|'('
string|"'api'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'api_engine'"
op|','
name|'engine'
op|')'
newline|'\n'
name|'mock_get_engine'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFlavorCheck
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestFlavorCheck'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestFlavorCheck'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'='
name|'importlib'
op|'.'
name|'import_module'
op|'('
nl|'\n'
string|"'nova.db.sqlalchemy.migrate_repo.versions.'"
nl|'\n'
string|"'291_enforce_flavors_migrated'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'engine'
op|'='
name|'db_api'
op|'.'
name|'get_engine'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upgrade_clean
dedent|''
name|'def'
name|'test_upgrade_clean'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'upgrade'
op|'('
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upgrade_dirty
dedent|''
name|'def'
name|'test_upgrade_dirty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'upgrade'
op|','
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upgrade_flavor_deleted_instances
dedent|''
name|'def'
name|'test_upgrade_flavor_deleted_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'system_metadata'
op|'='
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'upgrade'
op|'('
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upgrade_flavor_deleted_sysmeta
dedent|''
name|'def'
name|'test_upgrade_flavor_deleted_sysmeta'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
name|'sysmeta'
op|'='
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'flavor'
op|')'
newline|'\n'
name|'sysmeta'
op|'['
string|"'foo'"
op|']'
op|'='
string|"'bar'"
newline|'\n'
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'sysmeta'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'sysmeta'
op|'='
name|'db_api'
op|'.'
name|'instance_system_metadata_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'inst'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'sysmeta'
op|'='
op|'{'
name|'k'
op|':'
name|'v'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'sysmeta'
op|'.'
name|'items'
op|'('
op|')'
nl|'\n'
name|'if'
name|'not'
name|'k'
op|'.'
name|'startswith'
op|'('
string|"'instance_type_'"
op|')'
op|'}'
newline|'\n'
name|'db_api'
op|'.'
name|'instance_system_metadata_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'sysmeta'
op|','
name|'True'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
name|'inst'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'upgrade'
op|'('
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upgrade_flavor_already_migrated
dedent|''
name|'def'
name|'test_upgrade_flavor_already_migrated'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
name|'sysmeta'
op|'='
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'flavor'
op|')'
newline|'\n'
name|'sysmeta'
op|'['
string|"'foo'"
op|']'
op|'='
string|"'bar'"
newline|'\n'
name|'inst'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'sysmeta'
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
comment|'# Trigger the migration by lazy-loading flavor'
nl|'\n'
name|'inst'
op|'.'
name|'flavor'
newline|'\n'
name|'inst'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'instance_type_id'"
op|','
name|'inst'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'sysmeta'
op|'='
name|'db_api'
op|'.'
name|'instance_system_metadata_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'inst'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
name|'sysmeta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'upgrade'
op|'('
name|'self'
op|'.'
name|'engine'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
