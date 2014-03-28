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
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'api_sample_base'
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
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|'"keypairs"'
newline|'\n'
nl|'\n'
DECL|member|generalize_subs
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
op|','
name|'public_key'
op|'='
name|'None'
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
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'keypairs'"
op|','
string|"'keypairs-post-req'"
op|','
nl|'\n'
op|'{'
string|"'keypair_name'"
op|':'
name|'key_name'
op|'}'
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
string|"'keypairs-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'201'
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
string|'"ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAgQDx8nkQv/zgGg"'
nl|'\n'
string|'"B4rMYmIf+6A4l6Rr+o/6lHBQdW5aYd44bd8JttDCE/F/pNRr0l"'
nl|'\n'
string|'"RE+PiqSPO8nDPHw0010JeMH9gYgnnFlyY3/OcJ02RhIPyyxYpv"'
nl|'\n'
string|'"9FhY+2YiUkpwFOcLImyrxEsYXpD/0d3ac30bNH6Sw9JD9UZHYc"'
nl|'\n'
string|'"pSxsIbECHw== Generated by Nova"'
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'keypairs'"
op|','
string|"'keypairs-import-post-req'"
op|','
nl|'\n'
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
number|'201'
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
string|"'keypairs'"
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
dedent|''
dedent|''
endmarker|''
end_unit
