begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MigrationsSamplesJsonTest
name|'class'
name|'MigrationsSamplesJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|'"os-migrations"'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'MigrationsSamplesJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.migrations.Migrations'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_stub_migrations
dedent|''
name|'def'
name|'_stub_migrations'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'return'
name|'fake_migrations'
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
name|'super'
op|'('
name|'MigrationsSamplesJsonTest'
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
name|'stub_out'
op|'('
string|"'nova.compute.api.API.get_migrations'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_stub_migrations'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_migrations
dedent|''
name|'def'
name|'test_get_migrations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-migrations'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'migrations-get'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
