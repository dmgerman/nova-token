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
name|'api_sample_base'
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
DECL|class|ServersSampleBase
name|'class'
name|'ServersSampleBase'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|extra_extensions_to_load
indent|'    '
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-access-ips"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_post_server
name|'def'
name|'_post_server'
op|'('
name|'self'
op|','
name|'use_common_server_api_samples'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
comment|'# param use_common_server_api_samples: Boolean to set whether tests use'
nl|'\n'
comment|'# common sample files for server post request and response.'
nl|'\n'
comment|'# Default is True which means _get_sample_path method will fetch the'
nl|'\n'
comment|"# common server sample files from 'servers' directory."
nl|'\n'
comment|'# Set False if tests need to use extension specific sample files'
nl|'\n'
nl|'\n'
indent|'        '
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
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
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
string|"'versioned_compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_vers_compute_endpoint'
op|'('
op|')'
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
name|'orig_value'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_use_common_server_api_samples'
newline|'\n'
name|'orig_sample_dir'
op|'='
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'sample_dir'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_use_common_server_api_samples'
op|'='
op|'('
nl|'\n'
name|'use_common_server_api_samples'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers'"
op|','
string|"'server-post-req'"
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
name|'status'
op|'='
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-post-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'202'
op|')'
newline|'\n'
name|'return'
name|'status'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_use_common_server_api_samples'
op|'='
name|'orig_value'
newline|'\n'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'sample_dir'
op|'='
name|'orig_sample_dir'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleJsonTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServersSampleJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
newline|'\n'
DECL|variable|request_api_version
name|'request_api_version'
op|'='
name|'None'
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
name|'ServersSampleBase'
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
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_servers_post
dedent|''
name|'def'
name|'test_servers_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_get
dedent|''
name|'def'
name|'test_servers_get'
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
name|'test_servers_post'
op|'('
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
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
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
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'subs'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"r'[\\w\\.\\-]+'"
newline|'\n'
name|'subs'
op|'['
string|"'mac_addr'"
op|']'
op|'='
string|"'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
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
DECL|member|test_servers_list
dedent|''
name|'def'
name|'test_servers_list'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers'"
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
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
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_details
dedent|''
name|'def'
name|'test_servers_details'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/detail'"
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
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
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'subs'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|'='
string|"r'[\\w\\.\\-]+'"
newline|'\n'
name|'subs'
op|'['
string|"'mac_addr'"
op|']'
op|'='
string|"'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v4'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'subs'
op|'['
string|"'access_ip_v6'"
op|']'
op|'='
string|"'80fe::'"
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-details-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleJson29Test
dedent|''
dedent|''
name|'class'
name|'ServersSampleJson29Test'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|request_api_version
indent|'    '
name|'request_api_version'
op|'='
string|"'2.9'"
newline|'\n'
comment|'# NOTE(gmann): microversion tests do not need to run for v2 API'
nl|'\n'
comment|'# so defining scenarios only for v2.9 which will run the original tests'
nl|'\n'
comment|"# by appending '(v2_9)' in test_id."
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_9'"
op|','
op|'{'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerSortKeysJsonTests
dedent|''
name|'class'
name|'ServerSortKeysJsonTests'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers-sort'"
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
name|'ServerSortKeysJsonTests'
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
string|"'nova.api.openstack.compute.contrib.server_sort_keys.'"
nl|'\n'
string|"'Server_sort_keys'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_servers_list
dedent|''
name|'def'
name|'test_servers_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers?sort_key=display_name&sort_dir=asc'"
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
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-sort-keys-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
nl|'\n'
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleAllExtensionJsonTest
dedent|''
dedent|''
name|'class'
name|'ServersSampleAllExtensionJsonTest'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
DECL|variable|sample_dir
name|'sample_dir'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersActionsJsonTest
dedent|''
name|'class'
name|'ServersActionsJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
newline|'\n'
nl|'\n'
DECL|member|_test_server_action
name|'def'
name|'_test_server_action'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'action'
op|','
name|'req_tpl'
op|','
nl|'\n'
name|'subs'
op|'='
name|'None'
op|','
name|'resp_tpl'
op|'='
name|'None'
op|','
name|'code'
op|'='
number|'202'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
name|'subs'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
op|'{'
string|"'action'"
op|':'
name|'action'
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|'}'
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
name|'req_tpl'
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
name|'code'
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
name|'code'
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
string|'""'
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_reboot_hard
dedent|''
dedent|''
name|'def'
name|'test_server_reboot_hard'
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
string|'"reboot"'
op|','
nl|'\n'
string|"'server-action-reboot'"
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"HARD"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_reboot_soft
dedent|''
name|'def'
name|'test_server_reboot_soft'
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
string|'"reboot"'
op|','
nl|'\n'
string|"'server-action-reboot'"
op|','
nl|'\n'
op|'{'
string|'"type"'
op|':'
string|'"SOFT"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild
dedent|''
name|'def'
name|'test_server_rebuild'
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
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
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
string|"'versioned_compute_endpoint'"
op|':'
name|'self'
op|'.'
name|'_get_vers_compute_endpoint'
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
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'80fe::'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'rebuild'"
op|','
nl|'\n'
string|"'server-action-rebuild'"
op|','
nl|'\n'
name|'subs'
op|','
nl|'\n'
string|"'server-action-rebuild-resp'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_resize
dedent|''
name|'def'
name|'test_server_resize'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"resize"'
op|','
nl|'\n'
string|"'server-action-resize'"
op|','
nl|'\n'
op|'{'
string|'"id"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"host"'
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'uuid'
newline|'\n'
nl|'\n'
DECL|member|test_server_revert_resize
dedent|''
name|'def'
name|'test_server_revert_resize'
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
name|'test_server_resize'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"revertResize"'
op|','
nl|'\n'
string|"'server-action-revert-resize'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_confirm_resize
dedent|''
name|'def'
name|'test_server_confirm_resize'
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
name|'test_server_resize'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|'"confirmResize"'
op|','
nl|'\n'
string|"'server-action-confirm-resize'"
op|','
nl|'\n'
name|'code'
op|'='
number|'204'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_image
dedent|''
name|'def'
name|'test_server_create_image'
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
string|"'createImage'"
op|','
nl|'\n'
string|"'server-action-create-image'"
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'foo-image'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersActionsAllJsonTest
dedent|''
dedent|''
name|'class'
name|'ServersActionsAllJsonTest'
op|'('
name|'ServersActionsJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
DECL|variable|sample_dir
name|'sample_dir'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerStartStopJsonTest
dedent|''
name|'class'
name|'ServerStartStopJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
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
name|'ServerStartStopJsonTest'
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
string|"'nova.api.openstack.compute.contrib.server_start_stop.'"
nl|'\n'
string|"'Server_start_stop'"
op|')'
newline|'\n'
name|'return'
name|'f'
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
name|'action'
op|','
name|'req_tpl'
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
name|'req_tpl'
op|','
nl|'\n'
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
string|'""'
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_start
dedent|''
name|'def'
name|'test_server_start'
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
string|"'os-stop'"
op|','
string|"'server-action-stop'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_server_action'
op|'('
name|'uuid'
op|','
string|"'os-start'"
op|','
string|"'server-action-start'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_stop
dedent|''
name|'def'
name|'test_server_stop'
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
string|"'os-stop'"
op|','
string|"'server-action-stop'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleMultiStatusJsonTest
dedent|''
dedent|''
name|'class'
name|'ServersSampleMultiStatusJsonTest'
op|'('
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|"'servers'"
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-access-ips"'
op|']'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
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
name|'ServersSampleMultiStatusJsonTest'
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
string|"'nova.api.openstack.compute.legacy_v2.contrib.'"
nl|'\n'
string|"'server_list_multi_status.Server_list_multi_status'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|test_servers_list
dedent|''
name|'def'
name|'test_servers_list'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers?status=active&status=error'"
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
string|"'id'"
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'servers-list-resp'"
op|','
name|'subs'
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
