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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
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
name|'test_servers'
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
DECL|class|MigrateServerSamplesJsonTest
name|'class'
name|'MigrateServerSamplesJsonTest'
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
string|'"os-migrate-server"'
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
name|'MigrateServerSamplesJsonTest'
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
string|"'nova.api.openstack.compute.contrib.admin_actions.'"
nl|'\n'
string|"'Admin_actions'"
op|')'
newline|'\n'
name|'return'
name|'f'
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
string|'"""setUp Method for MigrateServer api samples extension\n\n        This method creates the server that will be used in each tests\n        """'
newline|'\n'
name|'super'
op|'('
name|'MigrateServerSamplesJsonTest'
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
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.conductor.manager.ComputeTaskManager._cold_migrate'"
op|')'
newline|'\n'
DECL|member|test_post_migrate
name|'def'
name|'test_post_migrate'
op|'('
name|'self'
op|','
name|'mock_cold_migrate'
op|')'
op|':'
newline|'\n'
comment|'# Get api samples to migrate server request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
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
nl|'\n'
string|"'migrate-server'"
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
DECL|member|test_post_live_migrate_server
dedent|''
name|'def'
name|'test_post_live_migrate_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api samples to server live migrate request.'
nl|'\n'
DECL|function|fake_live_migrate
indent|'        '
name|'def'
name|'fake_live_migrate'
op|'('
name|'_self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'uuid'
op|','
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
name|'host'
op|'='
name|'scheduler_hint'
op|'['
string|'"host"'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
nl|'\n'
string|"'nova.conductor.manager.ComputeTaskManager._live_migrate'"
op|','
nl|'\n'
name|'fake_live_migrate'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_compute
name|'def'
name|'fake_get_compute'
op|'('
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'='
name|'dict'
op|'('
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'binary'
op|'='
string|"'nova-compute'"
op|','
nl|'\n'
name|'topic'
op|'='
string|"'compute'"
op|','
nl|'\n'
name|'report_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'updated_at'
op|'='
string|"'foo'"
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|"'bar'"
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
op|'('
nl|'\n'
name|'versionutils'
op|'.'
name|'convert_version_to_int'
op|'('
string|"'1.0'"
op|')'
op|')'
op|','
nl|'\n'
name|'disabled'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'compute_node'"
op|':'
op|'['
name|'service'
op|']'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stub_out'
op|'('
string|'"nova.db.service_get_by_compute_host"'
op|','
name|'fake_get_compute'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
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
nl|'\n'
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
dedent|''
dedent|''
endmarker|''
end_unit
