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
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeferredDeleteSampleJsonTests
name|'class'
name|'DeferredDeleteSampleJsonTests'
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
string|'"os-deferred-delete"'
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
name|'DeferredDeleteSampleJsonTests'
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
string|"'nova.api.openstack.compute.contrib.deferred_delete.'"
nl|'\n'
string|"'Deferred_delete'"
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
name|'DeferredDeleteSampleJsonTests'
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
name|'flags'
op|'('
name|'reclaim_instance_interval'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_restore
dedent|''
name|'def'
name|'test_restore'
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
name|'_do_delete'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
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
string|"'restore-post-req'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_force_delete
dedent|''
name|'def'
name|'test_force_delete'
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
name|'_do_delete'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
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
string|"'force-delete-post-req'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
