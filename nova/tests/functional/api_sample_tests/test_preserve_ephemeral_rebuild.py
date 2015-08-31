begin_unit
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
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
op|'.'
name|'image'
name|'import'
name|'fake'
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
DECL|class|PreserveEphemeralOnRebuildJsonTest
name|'class'
name|'PreserveEphemeralOnRebuildJsonTest'
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
string|"'os-preserve-ephemeral-rebuild'"
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
name|'PreserveEphemeralOnRebuildJsonTest'
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
string|"'nova.api.openstack.compute.contrib.preserve_ephemeral_rebuild.'"
nl|'\n'
string|"'Preserve_ephemeral_rebuild'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_test_server_rebuild_preserve_ephemeral
dedent|''
name|'def'
name|'_test_server_rebuild_preserve_ephemeral'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'resp_tpl'
op|'='
name|'None'
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
name|'image'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'image'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'foobar'"
op|','
nl|'\n'
string|"'pass'"
op|':'
string|"'seekr3t'"
op|','
nl|'\n'
string|"'hostid'"
op|':'
string|"'[a-f0-9]+'"
op|','
nl|'\n'
string|"'preserve_ephemeral'"
op|':'
name|'str'
op|'('
name|'value'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|','
nl|'\n'
string|"'action'"
op|':'
string|"'rebuild'"
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'80fe::'"
nl|'\n'
op|'}'
newline|'\n'
name|'old_rebuild'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'rebuild'
newline|'\n'
nl|'\n'
DECL|function|fake_rebuild
name|'def'
name|'fake_rebuild'
op|'('
name|'self_'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_href'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'files_to_inject'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'preserve_ephemeral'"
op|']'
op|','
name|'value'
op|')'
newline|'\n'
name|'if'
name|'resp_tpl'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'old_rebuild'
op|'('
name|'self_'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'image_href'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'files_to_inject'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'rebuild'"
op|','
name|'fake_rebuild'
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
name|'uuid'
op|','
nl|'\n'
string|"'server-action-rebuild-preserve-ephemeral'"
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'if'
name|'resp_tpl'
op|':'
newline|'\n'
indent|'            '
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
name|'resp_tpl'
op|','
name|'subs'
op|','
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
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
DECL|member|test_server_rebuild_preserve_ephemeral_true
dedent|''
dedent|''
name|'def'
name|'test_server_rebuild_preserve_ephemeral_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_server_rebuild_preserve_ephemeral'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_preserve_ephemeral_false
dedent|''
name|'def'
name|'test_server_rebuild_preserve_ephemeral_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_server_rebuild_preserve_ephemeral'
op|'('
name|'False'
op|','
nl|'\n'
name|'resp_tpl'
op|'='
string|"'server-action-rebuild-preserve-ephemeral-resp'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
