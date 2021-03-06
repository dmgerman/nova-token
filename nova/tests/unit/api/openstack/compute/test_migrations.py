begin_unit
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
name|'datetime'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'oslotest'
name|'import'
name|'moxstubout'
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
name|'import'
name|'migrations'
name|'as'
name|'migrations_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'uuidsentinel'
name|'as'
name|'uuids'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_migrations
name|'fake_migrations'
op|'='
op|'['
nl|'\n'
comment|'# in-progress live migration'
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'source_node'"
op|':'
string|"'node1'"
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node2'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute1'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute2'"
op|','
nl|'\n'
string|"'dest_host'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'running'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'instance1'
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'live-migration'"
op|','
nl|'\n'
string|"'hidden'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_total'"
op|':'
number|'123456'
op|','
nl|'\n'
string|"'memory_processed'"
op|':'
number|'12345'
op|','
nl|'\n'
string|"'memory_remaining'"
op|':'
number|'120000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'234567'
op|','
nl|'\n'
string|"'disk_processed'"
op|':'
number|'23456'
op|','
nl|'\n'
string|"'disk_remaining'"
op|':'
number|'230000'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
op|','
nl|'\n'
comment|'# non in-progress live migration'
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'source_node'"
op|':'
string|"'node1'"
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node2'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute1'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute2'"
op|','
nl|'\n'
string|"'dest_host'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'error'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'instance1'
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'live-migration'"
op|','
nl|'\n'
string|"'hidden'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_total'"
op|':'
number|'123456'
op|','
nl|'\n'
string|"'memory_processed'"
op|':'
number|'12345'
op|','
nl|'\n'
string|"'memory_remaining'"
op|':'
number|'120000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'234567'
op|','
nl|'\n'
string|"'disk_processed'"
op|':'
number|'23456'
op|','
nl|'\n'
string|"'disk_remaining'"
op|':'
number|'230000'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'10'
op|','
number|'29'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
op|','
nl|'\n'
comment|'# in-progress resize'
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'4'
op|','
nl|'\n'
string|"'source_node'"
op|':'
string|"'node10'"
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node20'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute10'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute20'"
op|','
nl|'\n'
string|"'dest_host'"
op|':'
string|"'5.6.7.8'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'migrating'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'instance2'
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
number|'6'
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'resize'"
op|','
nl|'\n'
string|"'hidden'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_total'"
op|':'
number|'456789'
op|','
nl|'\n'
string|"'memory_processed'"
op|':'
number|'56789'
op|','
nl|'\n'
string|"'memory_remaining'"
op|':'
number|'45000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'96789'
op|','
nl|'\n'
string|"'disk_processed'"
op|':'
number|'6789'
op|','
nl|'\n'
string|"'disk_remaining'"
op|':'
number|'96000'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'10'
op|','
number|'22'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'10'
op|','
number|'22'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
op|','
nl|'\n'
comment|'# non in-progress resize'
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'source_node'"
op|':'
string|"'node10'"
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node20'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute10'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute20'"
op|','
nl|'\n'
string|"'dest_host'"
op|':'
string|"'5.6.7.8'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'error'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'uuids'
op|'.'
name|'instance2'
op|','
nl|'\n'
string|"'old_instance_type_id'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'new_instance_type_id'"
op|':'
number|'6'
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'resize'"
op|','
nl|'\n'
string|"'hidden'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_total'"
op|':'
number|'456789'
op|','
nl|'\n'
string|"'memory_processed'"
op|':'
number|'56789'
op|','
nl|'\n'
string|"'memory_remaining'"
op|':'
number|'45000'
op|','
nl|'\n'
string|"'disk_total'"
op|':'
number|'96789'
op|','
nl|'\n'
string|"'disk_processed'"
op|':'
number|'6789'
op|','
nl|'\n'
string|"'disk_remaining'"
op|':'
number|'96000'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'10'
op|','
number|'22'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'10'
op|','
number|'22'
op|','
number|'13'
op|','
number|'42'
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|migrations_obj
name|'migrations_obj'
op|'='
name|'base'
op|'.'
name|'obj_make_list'
op|'('
nl|'\n'
string|"'fake-context'"
op|','
nl|'\n'
name|'objects'
op|'.'
name|'MigrationList'
op|'('
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Migration'
op|','
nl|'\n'
name|'fake_migrations'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|','
nl|'\n'
DECL|variable|is_admin
name|'is_admin'
op|'='
name|'True'
op|')'
op|'}'
newline|'\n'
DECL|variable|GET
name|'GET'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsTestCaseV21
dedent|''
name|'class'
name|'MigrationsTestCaseV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|migrations
indent|'    '
name|'migrations'
op|'='
name|'migrations_v21'
newline|'\n'
nl|'\n'
DECL|member|_migrations_output
name|'def'
name|'_migrations_output'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_output'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'migrations_obj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run before each test."""'
newline|'\n'
name|'super'
op|'('
name|'MigrationsTestCaseV21'
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
name|'controller'
op|'='
name|'self'
op|'.'
name|'migrations'
op|'.'
name|'MigrationsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'mox_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'moxstubout'
op|'.'
name|'MoxStubout'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'='
name|'mox_fixture'
op|'.'
name|'mox'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migrations_in_progress'
op|'='
op|'{'
string|"'migrations'"
op|':'
name|'self'
op|'.'
name|'_migrations_output'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'mig'
name|'in'
name|'migrations_in_progress'
op|'['
string|"'migrations'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'id'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'deleted'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'deleted_at'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'links'"
op|','
name|'mig'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'filters'
op|'='
op|'{'
string|"'host'"
op|':'
string|"'host1'"
op|','
string|"'status'"
op|':'
string|"'migrating'"
op|','
nl|'\n'
string|"'cell_name'"
op|':'
string|"'ChildCell'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'GET'
op|'.'
name|'update'
op|'('
name|'filters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|'"get_migrations"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|'.'
name|'get_migrations'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'filters'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'migrations_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'migrations_in_progress'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsTestCaseV223
dedent|''
dedent|''
name|'class'
name|'MigrationsTestCaseV223'
op|'('
name|'MigrationsTestCaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|wsgi_api_version
indent|'    '
name|'wsgi_api_version'
op|'='
string|"'2.23'"
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run before each test."""'
newline|'\n'
name|'super'
op|'('
name|'MigrationsTestCaseV223'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"''"
op|','
name|'version'
op|'='
name|'self'
op|'.'
name|'wsgi_api_version'
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migrations'
op|'='
op|'{'
string|"'migrations'"
op|':'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_output'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'migrations_obj'
op|','
name|'True'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'mig'
name|'in'
name|'enumerate'
op|'('
name|'migrations'
op|'['
string|"'migrations'"
op|']'
op|')'
op|':'
newline|'\n'
comment|'# first item is in-progress live migration'
nl|'\n'
indent|'            '
name|'if'
name|'i'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'links'"
op|','
name|'mig'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'links'"
op|','
name|'mig'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'migration_type'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'id'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'deleted'"
op|','
name|'mig'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'deleted_at'"
op|','
name|'mig'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|"'get_migrations'"
op|')'
name|'as'
name|'m_get'
op|':'
newline|'\n'
indent|'            '
name|'m_get'
op|'.'
name|'return_value'
op|'='
name|'migrations_obj'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'migrations'
op|','
name|'response'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'links'"
op|','
name|'response'
op|'['
string|"'migrations'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'migration_type'"
op|','
name|'response'
op|'['
string|"'migrations'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsPolicyEnforcement
dedent|''
dedent|''
dedent|''
name|'class'
name|'MigrationsPolicyEnforcement'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'MigrationsPolicyEnforcement'
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
name|'controller'
op|'='
name|'migrations_v21'
op|'.'
name|'MigrationsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_policy_failed
dedent|''
name|'def'
name|'test_list_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-migrations:index"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project_id:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsPolicyEnforcementV223
dedent|''
dedent|''
name|'class'
name|'MigrationsPolicyEnforcementV223'
op|'('
name|'MigrationsPolicyEnforcement'
op|')'
op|':'
newline|'\n'
DECL|variable|wsgi_api_version
indent|'    '
name|'wsgi_api_version'
op|'='
string|"'2.23'"
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'MigrationsPolicyEnforcementV223'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|','
name|'version'
op|'='
name|'self'
op|'.'
name|'wsgi_api_version'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
