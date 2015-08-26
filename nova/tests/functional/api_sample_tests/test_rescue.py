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
DECL|class|RescueJsonTest
name|'class'
name|'RescueJsonTest'
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
string|'"os-rescue"'
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
name|'RescueJsonTest'
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
string|"'nova.api.openstack.compute.contrib.rescue.Rescue'"
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
string|"'nova.api.openstack.compute.contrib.extended_rescue_with_image.'"
nl|'\n'
string|"'Extended_rescue_with_image'"
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
DECL|member|_rescue
dedent|''
name|'def'
name|'_rescue'
op|'('
name|'self'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req_subs'
op|'='
op|'{'
nl|'\n'
string|"'password'"
op|':'
string|"'MySecretPass'"
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
string|"'server-rescue-req'"
op|','
name|'req_subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-rescue'"
op|','
name|'req_subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_unrescue
dedent|''
name|'def'
name|'_unrescue'
op|'('
name|'self'
op|','
name|'uuid'
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
string|"'server-unrescue-req'"
op|','
op|'{'
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
nl|'\n'
DECL|member|test_server_rescue
dedent|''
name|'def'
name|'test_server_rescue'
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
nl|'\n'
name|'self'
op|'.'
name|'_rescue'
op|'('
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
comment|"# Do a server get to make sure that the 'RESCUE' state is set"
nl|'\n'
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
string|"'status'"
op|']'
op|'='
string|"'RESCUE'"
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
string|"'server-get-resp-rescue'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rescue_with_image_ref_specified
dedent|''
name|'def'
name|'test_server_rescue_with_image_ref_specified'
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
nl|'\n'
name|'req_subs'
op|'='
op|'{'
nl|'\n'
string|"'password'"
op|':'
string|"'MySecretPass'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
string|"'2341-Abc'"
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
string|"'server-rescue-req-with-image-ref'"
op|','
name|'req_subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-rescue'"
op|','
name|'req_subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
comment|"# Do a server get to make sure that the 'RESCUE' state is set"
nl|'\n'
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
string|"'status'"
op|']'
op|'='
string|"'RESCUE'"
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
string|"'server-get-resp-rescue'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_unrescue
dedent|''
name|'def'
name|'test_server_unrescue'
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
nl|'\n'
name|'self'
op|'.'
name|'_rescue'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_unrescue'
op|'('
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
comment|"# Do a server get to make sure that the 'ACTIVE' state is back"
nl|'\n'
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
string|"'status'"
op|']'
op|'='
string|"'ACTIVE'"
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
string|"'server-get-resp-unrescue'"
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
