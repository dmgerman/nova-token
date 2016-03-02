begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
name|'datetime'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'manager'
name|'as'
name|'conductor_manager'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerMigrationsSampleJsonTest
name|'class'
name|'ServerMigrationsSampleJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|"'server-migrations'"
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_22'"
op|','
op|'{'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-migrate-server"'
op|','
string|'"os-access-ips"'
op|']'
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
string|'"""setUp method for server usage."""'
newline|'\n'
name|'super'
op|'('
name|'ServerMigrationsSampleJsonTest'
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
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'microversion'
op|'='
string|"'2.22'"
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'conductor_manager'
op|'.'
name|'ComputeTaskManager'
op|','
string|"'_live_migrate'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'db'
op|','
string|"'service_get_by_compute_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'Migration'
op|','
string|"'get_by_id_and_instance'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.manager.ComputeManager.'"
nl|'\n'
string|"'live_migration_force_complete'"
op|')'
newline|'\n'
DECL|member|test_live_migrate_force_complete
name|'def'
name|'test_live_migrate_force_complete'
op|'('
name|'self'
op|','
name|'live_migration_pause_instance'
op|','
nl|'\n'
name|'get_by_id_and_instance'
op|','
nl|'\n'
name|'service_get_by_compute_host'
op|','
nl|'\n'
name|'_live_migrate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'migration'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
op|')'
newline|'\n'
name|'migration'
op|'.'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'migration'
op|'.'
name|'status'
op|'='
string|"'running'"
newline|'\n'
name|'get_by_id_and_instance'
op|'.'
name|'return_value'
op|'='
name|'migration'
newline|'\n'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
string|"'live-migrate-server'"
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/migrations/%s/action'"
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
string|"'3'"
op|')'
op|','
string|"'force_complete'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_migration
dedent|''
name|'def'
name|'test_get_migration'
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
string|"'servers/fake_id/migrations/1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_migrations
dedent|''
name|'def'
name|'test_list_migrations'
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
string|"'servers/fake_id/migrations'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerMigrationsSamplesJsonTestV2_23
dedent|''
dedent|''
name|'class'
name|'ServerMigrationsSamplesJsonTestV2_23'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
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
string|'"server-migrations"'
newline|'\n'
DECL|variable|microversion
name|'microversion'
op|'='
string|"'2.23'"
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_23'"
op|','
op|'{'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
DECL|variable|UUID_1
name|'UUID_1'
op|'='
string|"'4cfba335-03d8-49b2-8c52-e69043d1e8fe'"
newline|'\n'
DECL|variable|UUID_2
name|'UUID_2'
op|'='
string|"'058fc419-a8a8-4e08-b62c-a9841ef9cd3f'"
newline|'\n'
nl|'\n'
DECL|variable|fake_migrations
name|'fake_migrations'
op|'='
op|'['
nl|'\n'
op|'{'
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
name|'UUID_1'
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
number|'2016'
op|','
number|'0o1'
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
number|'2016'
op|','
number|'0o1'
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
name|'UUID_2'
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
number|'2016'
op|','
number|'0o1'
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
number|'2016'
op|','
number|'0o1'
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
name|'ServerMigrationsSamplesJsonTestV2_23'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mig1'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
nl|'\n'
name|'context'
op|'='
name|'fake_context'
op|','
op|'**'
name|'self'
op|'.'
name|'fake_migrations'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mig1'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mig2'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
nl|'\n'
name|'context'
op|'='
name|'fake_context'
op|','
op|'**'
name|'self'
op|'.'
name|'fake_migrations'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mig2'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'fake_ins'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
name|'uuid'
op|'='
name|'self'
op|'.'
name|'UUID_1'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"pci_devices"'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"security_groups"'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"services"'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"tags"'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"info_cache"'
op|')'
newline|'\n'
name|'fake_ins'
op|'.'
name|'pop'
op|'('
string|'"id"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
nl|'\n'
name|'context'
op|'='
name|'fake_context'
op|','
nl|'\n'
op|'**'
name|'fake_ins'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_migration
dedent|''
name|'def'
name|'test_get_migration'
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
string|"'servers/%s/migrations/%s'"
op|'%'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'fake_migrations'
op|'['
number|'0'
op|']'
op|'['
string|'"instance_uuid"'
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'mig1'
op|'.'
name|'id'
op|')'
op|')'
newline|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'migrations-get'"
op|','
nl|'\n'
op|'{'
string|'"server_uuid"'
op|':'
name|'self'
op|'.'
name|'UUID_1'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_migrations
dedent|''
name|'def'
name|'test_list_migrations'
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
string|"'servers/%s/migrations'"
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'fake_migrations'
op|'['
number|'0'
op|']'
op|'['
string|'"instance_uuid"'
op|']'
op|')'
newline|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'migrations-index'"
op|','
nl|'\n'
op|'{'
string|'"server_uuid_1"'
op|':'
name|'self'
op|'.'
name|'UUID_1'
op|'}'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerMigrationsSampleJsonTestV2_24
dedent|''
dedent|''
name|'class'
name|'ServerMigrationsSampleJsonTestV2_24'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
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
string|'"server-migrations"'
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_24'"
op|','
op|'{'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|']'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-migrate-server"'
op|','
string|'"os-access-ips"'
op|']'
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
string|'"""setUp method for server usage."""'
newline|'\n'
name|'super'
op|'('
name|'ServerMigrationsSampleJsonTestV2_24'
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
name|'api'
op|'.'
name|'microversion'
op|'='
string|"'2.24'"
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'fake_migration'
op|'='
op|'{'
nl|'\n'
string|"'source_node'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'dest_node'"
op|':'
string|"'node10'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'compute1'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'compute12'"
op|','
nl|'\n'
string|"'migration_type'"
op|':'
string|"'live-migration'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'running'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'migration'
op|'='
name|'objects'
op|'.'
name|'Migration'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'**'
name|'fake_migration'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'conductor_manager'
op|'.'
name|'ComputeTaskManager'
op|','
string|"'_live_migrate'"
op|')'
newline|'\n'
DECL|member|test_live_migrate_abort
name|'def'
name|'test_live_migrate_abort'
op|'('
name|'self'
op|','
name|'_live_migrate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
string|"'live-migrate-server'"
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'uri'
op|'='
string|"'servers/%s/migrations/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
name|'self'
op|'.'
name|'migration'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'conductor_manager'
op|'.'
name|'ComputeTaskManager'
op|','
string|"'_live_migrate'"
op|')'
newline|'\n'
DECL|member|test_live_migrate_abort_migration_not_found
name|'def'
name|'test_live_migrate_abort_migration_not_found'
op|'('
name|'self'
op|','
name|'_live_migrate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
string|"'live-migrate-server'"
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'uri'
op|'='
string|"'servers/%s/migrations/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
string|"'45'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'conductor_manager'
op|'.'
name|'ComputeTaskManager'
op|','
string|"'_live_migrate'"
op|')'
newline|'\n'
DECL|member|test_live_migrate_abort_migration_not_running
name|'def'
name|'test_live_migrate_abort_migration_not_running'
op|'('
name|'self'
op|','
name|'_live_migrate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'migration'
op|'.'
name|'status'
op|'='
string|"'completed'"
newline|'\n'
name|'self'
op|'.'
name|'migration'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
string|"'live-migrate-server'"
op|','
nl|'\n'
op|'{'
string|"'hostname'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'uri'
op|'='
string|"'servers/%s/migrations/%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
name|'self'
op|'.'
name|'migration'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
