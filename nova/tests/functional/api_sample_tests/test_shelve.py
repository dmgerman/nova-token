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
string|"'shelved_offload_time'"
op|','
string|"'nova.compute.manager'"
op|')'
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
DECL|class|ShelveJsonTest
name|'class'
name|'ShelveJsonTest'
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
string|'"os-shelve"'
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
name|'ShelveJsonTest'
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
string|"'nova.api.openstack.compute.contrib.shelve.Shelve'"
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
name|'super'
op|'('
name|'ShelveJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|"# Don't offload instance, so we can test the offload call."
nl|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'shelved_offload_time'"
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_server_action
dedent|''
name|'def'
name|'_test_server_action'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'template'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
name|'template'
op|','
op|'{'
string|"'action'"
op|':'
name|'action'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve
dedent|''
name|'def'
name|'test_shelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-shelve'"
op|','
string|"'shelve'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_shelve_offload
dedent|''
name|'def'
name|'test_shelve_offload'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-shelve'"
op|','
string|"'shelve'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-shelve-offload'"
op|','
string|"'shelveOffload'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unshelve
dedent|''
name|'def'
name|'test_unshelve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-shelve'"
op|','
string|"'shelve'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-unshelve'"
op|','
string|"'unshelve'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
