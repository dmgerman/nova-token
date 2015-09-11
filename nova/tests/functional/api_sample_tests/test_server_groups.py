begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
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
DECL|class|ServerGroupsSampleJsonTest
name|'class'
name|'ServerGroupsSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-server-groups"'
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
name|'ServerGroupsSampleJsonTest'
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
string|"'nova.api.openstack.compute.contrib.server_groups.Server_groups'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_get_create_subs
dedent|''
name|'def'
name|'_get_create_subs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'name'"
op|':'
string|"'test'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_post_server_group
dedent|''
name|'def'
name|'_post_server_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify the response status and returns the UUID of the\n        newly created server group.\n        """'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_create_subs'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-server-groups'"
op|','
nl|'\n'
string|"'server-groups-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'name'"
op|']'
op|'='
string|"'test'"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-groups-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_server_group
dedent|''
name|'def'
name|'_create_server_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_create_subs'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-server-groups'"
op|','
nl|'\n'
string|"'server-groups-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_groups_post
dedent|''
name|'def'
name|'test_server_groups_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_post_server_group'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_groups_list
dedent|''
name|'def'
name|'test_server_groups_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_create_subs'
op|'('
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server_group'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-server-groups'"
op|')'
newline|'\n'
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
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-groups-list-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_groups_get
dedent|''
name|'def'
name|'test_server_groups_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of server groups get request.'
nl|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test'"
op|'}'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server_group'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-server-groups/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-groups-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_groups_delete
dedent|''
name|'def'
name|'test_server_groups_delete'
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
name|'_post_server_group'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-server-groups/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'204'
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
