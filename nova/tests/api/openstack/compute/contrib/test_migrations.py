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
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'contrib'
name|'import'
name|'migrations'
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
name|'migration'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'fixture'
name|'import'
name|'moxstubout'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|fake_migrations
name|'fake_migrations'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1234'
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
string|"'Done'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'instance_id_123'"
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
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'5678'
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
string|"'Done'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'instance_id_456'"
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
name|'migration'
op|'.'
name|'MigrationList'
op|'('
op|')'
op|','
nl|'\n'
name|'migration'
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
name|'get_admin_context'
op|'('
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
DECL|class|MigrationsTestCase
dedent|''
name|'class'
name|'MigrationsTestCase'
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
string|'"""Run before each test."""'
newline|'\n'
name|'super'
op|'('
name|'MigrationsTestCase'
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
name|'migrations'
op|'.'
name|'MigrationsController'
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
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
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
nl|'\n'
string|"'migrations'"
op|':'
name|'migrations'
op|'.'
name|'output'
op|'('
name|'migrations_obj'
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
op|'='
name|'filters'
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
DECL|member|test_index_needs_authorization
dedent|''
name|'def'
name|'test_index_needs_authorization'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'False'
op|','
nl|'\n'
name|'read_deleted'
op|'='
string|'"no"'
op|','
nl|'\n'
name|'overwrite'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'user_context'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsTemplateTest
dedent|''
dedent|''
name|'class'
name|'MigrationsTemplateTest'
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
name|'MigrationsTemplateTest'
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
name|'serializer'
op|'='
name|'migrations'
op|'.'
name|'MigrationsTemplate'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serialization
dedent|''
name|'def'
name|'test_index_serialization'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migrations_out'
op|'='
name|'migrations'
op|'.'
name|'output'
op|'('
name|'migrations_obj'
op|')'
newline|'\n'
name|'res_xml'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|'('
nl|'\n'
op|'{'
string|"'migrations'"
op|':'
name|'migrations_out'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'res_xml'
op|')'
newline|'\n'
name|'children'
op|'='
name|'tree'
op|'.'
name|'findall'
op|'('
string|"'migration'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'tag'
op|','
string|"'migrations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'children'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'children'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'child'
op|'.'
name|'tag'
op|','
string|"'migration'"
op|')'
newline|'\n'
name|'migration'
op|'='
name|'migrations_out'
op|'['
name|'idx'
op|']'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'migration'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'migration'
op|'['
name|'attr'
op|']'
op|')'
op|','
nl|'\n'
name|'child'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
