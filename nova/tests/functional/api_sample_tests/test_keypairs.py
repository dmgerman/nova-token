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
name|'uuid'
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
name|'objects'
name|'import'
name|'keypair'
name|'as'
name|'keypair_obj'
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
name|'api_sample_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_crypto'
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
DECL|class|KeyPairsSampleJsonTest
name|'class'
name|'KeyPairsSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|request_api_version
indent|'    '
name|'request_api_version'
op|'='
name|'None'
newline|'\n'
DECL|variable|sample_dir
name|'sample_dir'
op|'='
string|'"keypairs"'
newline|'\n'
DECL|variable|expected_delete_status_code
name|'expected_delete_status_code'
op|'='
number|'202'
newline|'\n'
DECL|variable|expected_post_status_code
name|'expected_post_status_code'
op|'='
number|'200'
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
name|'KeyPairsSampleJsonTest'
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
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|generalize_subs
dedent|''
name|'def'
name|'generalize_subs'
op|'('
name|'self'
op|','
name|'subs'
op|','
name|'vanilla_regexes'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'['
string|"'keypair_name'"
op|']'
op|'='
string|"'keypair-[0-9a-f-]+'"
newline|'\n'
name|'return'
name|'subs'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post
dedent|''
name|'def'
name|'test_keypairs_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_keypairs_post
dedent|''
name|'def'
name|'_check_keypairs_post'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of key pairs post request."""'
newline|'\n'
name|'key_name'
op|'='
string|"'keypair-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'dict'
op|'('
name|'keypair_name'
op|'='
name|'key_name'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-keypairs'"
op|','
string|"'keypairs-post-req'"
op|','
name|'subs'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
nl|'\n'
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
string|"'keypair_name'"
op|']'
op|'='
string|"'(%s)'"
op|'%'
name|'key_name'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'keypairs-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_post_status_code'
op|')'
newline|'\n'
comment|'# NOTE(maurosr): return the key_name is necessary cause the'
nl|'\n'
comment|'# verification returns the label of the last compared information in'
nl|'\n'
comment|'# the response, not necessarily the key name.'
nl|'\n'
name|'return'
name|'key_name'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_import_key_post
dedent|''
name|'def'
name|'test_keypairs_import_key_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'public_key'
op|'='
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_keypairs_import_key_post'
op|'('
name|'public_key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_keypairs_import_key_post
dedent|''
name|'def'
name|'_check_keypairs_import_key_post'
op|'('
name|'self'
op|','
name|'public_key'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# Get api sample of key pairs post to import user's key."
nl|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'keypair-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'keypair_name'"
op|':'
name|'key_name'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'public_key'
nl|'\n'
op|'}'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-keypairs'"
op|','
string|"'keypairs-import-post-req'"
op|','
nl|'\n'
name|'subs'
op|','
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
string|"'keypair_name'"
op|']'
op|'='
string|"'(%s)'"
op|'%'
name|'key_name'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'keypairs-import-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
nl|'\n'
name|'self'
op|'.'
name|'expected_post_status_code'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_list
dedent|''
name|'def'
name|'test_keypairs_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of key pairs list request.'
nl|'\n'
indent|'        '
name|'key_name'
op|'='
name|'self'
op|'.'
name|'test_keypairs_post'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-keypairs'"
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
string|"'keypair_name'"
op|']'
op|'='
string|"'(%s)'"
op|'%'
name|'key_name'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'keypairs-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_get
dedent|''
name|'def'
name|'test_keypairs_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of key pairs get request.'
nl|'\n'
indent|'        '
name|'key_name'
op|'='
name|'self'
op|'.'
name|'test_keypairs_post'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-keypairs/%s'"
op|'%'
name|'key_name'
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
string|"'keypair_name'"
op|']'
op|'='
string|"'(%s)'"
op|'%'
name|'key_name'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'keypairs-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_delete
dedent|''
name|'def'
name|'test_keypairs_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of key pairs delete request.'
nl|'\n'
indent|'        '
name|'key_name'
op|'='
name|'self'
op|'.'
name|'test_keypairs_post'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-keypairs/%s'"
op|'%'
name|'key_name'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'expected_delete_status_code'
op|','
nl|'\n'
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairsV22SampleJsonTest
dedent|''
dedent|''
name|'class'
name|'KeyPairsV22SampleJsonTest'
op|'('
name|'KeyPairsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|request_api_version
indent|'    '
name|'request_api_version'
op|'='
string|"'2.2'"
newline|'\n'
DECL|variable|expected_post_status_code
name|'expected_post_status_code'
op|'='
number|'201'
newline|'\n'
DECL|variable|expected_delete_status_code
name|'expected_delete_status_code'
op|'='
number|'204'
newline|'\n'
comment|'# NOTE(gmann): microversion tests do not need to run for v2 API'
nl|'\n'
comment|'# so defining scenarios only for v2.2 which will run the original tests'
nl|'\n'
comment|"# by appending '(v2_2)' in test_id."
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_2'"
op|','
op|'{'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post
name|'def'
name|'test_keypairs_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(claudiub): overrides the method with the same name in'
nl|'\n'
comment|'# KeypairsSampleJsonTest, as it is used by other tests.'
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post_x509
dedent|''
name|'def'
name|'test_keypairs_post_x509'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_X509'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post_invalid
dedent|''
name|'def'
name|'test_keypairs_post_invalid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'keypair-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'dict'
op|'('
name|'keypair_name'
op|'='
name|'key_name'
op|','
name|'keypair_type'
op|'='
string|"'fakey_type'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-keypairs'"
op|','
string|"'keypairs-post-req'"
op|','
name|'subs'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
DECL|member|test_keypairs_import_key_post
dedent|''
name|'def'
name|'test_keypairs_import_key_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(claudiub): overrides the method with the same name in'
nl|'\n'
comment|'# KeypairsSampleJsonTest, since the API sample expects a keypair_type.'
nl|'\n'
indent|'        '
name|'public_key'
op|'='
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_keypairs_import_key_post'
op|'('
nl|'\n'
name|'public_key'
op|','
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_import_key_post_x509
dedent|''
name|'def'
name|'test_keypairs_import_key_post_x509'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'public_key'
op|'='
name|'fake_crypto'
op|'.'
name|'get_x509_cert_and_fingerprint'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'public_key'
op|'='
name|'public_key'
op|'.'
name|'replace'
op|'('
string|"'\\n'"
op|','
string|"'\\\\n'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_keypairs_import_key_post'
op|'('
nl|'\n'
name|'public_key'
op|','
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_X509'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_keypairs_import_key_post_invalid
dedent|''
name|'def'
name|'_check_keypairs_import_key_post_invalid'
op|'('
name|'self'
op|','
name|'keypair_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'keypair-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'keypair_name'"
op|':'
name|'key_name'
op|','
nl|'\n'
string|"'keypair_type'"
op|':'
name|'keypair_type'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-keypairs'"
op|','
string|"'keypairs-import-post-req'"
op|','
nl|'\n'
name|'subs'
op|','
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
nl|'\n'
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
nl|'\n'
DECL|member|test_keypairs_import_key_post_invalid_type
dedent|''
name|'def'
name|'test_keypairs_import_key_post_invalid_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_keypairs_import_key_post_invalid'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
string|"'fakey_type'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_import_key_post_invalid_combination
dedent|''
name|'def'
name|'test_keypairs_import_key_post_invalid_combination'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_keypairs_import_key_post_invalid'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_X509'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairsV210SampleJsonTest
dedent|''
dedent|''
name|'class'
name|'KeyPairsV210SampleJsonTest'
op|'('
name|'KeyPairsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|request_api_version
name|'request_api_version'
op|'='
string|"'2.10'"
newline|'\n'
DECL|variable|expected_post_status_code
name|'expected_post_status_code'
op|'='
number|'201'
newline|'\n'
DECL|variable|expected_delete_status_code
name|'expected_delete_status_code'
op|'='
number|'204'
newline|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
op|'('
string|"'v2_10'"
op|','
op|'{'
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_keypair_create_for_user
name|'def'
name|'test_keypair_create_for_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'keypair_type'"
op|':'
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|'"fake"'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
op|'**'
name|'subs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post
dedent|''
name|'def'
name|'test_keypairs_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
name|'user_id'
op|'='
string|'"admin"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_import_key_post
dedent|''
name|'def'
name|'test_keypairs_import_key_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(claudiub): overrides the method with the same name in'
nl|'\n'
comment|'# KeypairsSampleJsonTest, since the API sample expects a keypair_type.'
nl|'\n'
indent|'        '
name|'public_key'
op|'='
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_keypairs_import_key_post'
op|'('
nl|'\n'
name|'public_key'
op|','
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
name|'user_id'
op|'='
string|'"fake"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_delete_for_user
dedent|''
name|'def'
name|'test_keypairs_delete_for_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Delete a keypair on behalf of a user'
nl|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'keypair_type'"
op|':'
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
string|"'public_key'"
op|':'
name|'fake_crypto'
op|'.'
name|'get_ssh_public_key'
op|'('
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|'"fake"'
nl|'\n'
op|'}'
newline|'\n'
name|'key_name'
op|'='
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
op|'**'
name|'subs'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-keypairs/%s?user_id=fake'"
op|'%'
name|'key_name'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'expected_delete_status_code'
op|','
nl|'\n'
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyPairsV210SampleJsonTestNotAdmin
dedent|''
dedent|''
name|'class'
name|'KeyPairsV210SampleJsonTestNotAdmin'
op|'('
name|'KeyPairsV210SampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post
name|'def'
name|'test_keypairs_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_check_keypairs_post'
op|'('
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
name|'user_id'
op|'='
string|'"fake"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_keypairs_post_for_other_user
dedent|''
name|'def'
name|'test_keypairs_post_for_other_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|"'keypair-'"
op|'+'
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'dict'
op|'('
name|'keypair_name'
op|'='
name|'key_name'
op|','
nl|'\n'
name|'keypair_type'
op|'='
name|'keypair_obj'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|','
nl|'\n'
name|'user_id'
op|'='
string|"'fake1'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'os-keypairs'"
op|','
string|"'keypairs-post-req'"
op|','
name|'subs'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'request_api_version'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'403'
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