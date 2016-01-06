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
DECL|class|DiskConfigJsonTest
name|'class'
name|'DiskConfigJsonTest'
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
string|"'os-disk-config'"
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-access-ips"'
op|']'
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
name|'DiskConfigJsonTest'
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
string|"'nova.api.openstack.compute.contrib.keypairs.Keypairs'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips.Extended_ips'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.extended_ips_mac.'"
nl|'\n'
string|"'Extended_ips_mac'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.disk_config.'"
nl|'\n'
string|"'Disk_config'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_list_servers_detail
dedent|''
name|'def'
name|'test_list_servers_detail'
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
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"''"
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
string|"'list-servers-detail-get'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_server
dedent|''
name|'def'
name|'test_get_server'
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
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server
dedent|''
name|'def'
name|'test_update_server'
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
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'server-update-put-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-update-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_resize_server
dedent|''
name|'def'
name|'test_resize_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'allow_resize_to_same_host'
op|'='
name|'True'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
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
string|"'server-resize-post-req'"
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
comment|'# NOTE(tmello): Resize does not return response body'
nl|'\n'
comment|'# Bug #1085213.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'""'
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_server
dedent|''
name|'def'
name|'test_rebuild_server'
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
name|'use_common_server_api_samples'
op|'='
name|'False'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_compute_endpoint'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
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
string|"'server-action-rebuild-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-action-rebuild-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
