begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
name|'httplib2'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
nl|'\n'
name|'from'
name|'cinderclient'
name|'import'
name|'exceptions'
name|'as'
name|'cinder_exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'cinder'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_stub_volume
name|'def'
name|'_stub_volume'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'display_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'None'
op|','
nl|'\n'
string|'"attachments"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"cinder"'
op|','
nl|'\n'
string|'"created_at"'
op|':'
string|'"2012-09-10T00:00:00.000000"'
op|','
nl|'\n'
string|'"id"'
op|':'
string|"'00000000-0000-0000-0000-000000000000'"
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"size"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"snapshot_id"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"available"'
op|','
nl|'\n'
string|'"volume_type"'
op|':'
string|'"None"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'volume'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|_image_metadata
dedent|''
name|'_image_metadata'
op|'='
op|'{'
nl|'\n'
string|"'kernel_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
string|"'fake'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHTTPClient
name|'class'
name|'FakeHTTPClient'
op|'('
name|'cinder'
op|'.'
name|'cinder_client'
op|'.'
name|'client'
op|'.'
name|'HTTPClient'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_cs_request
indent|'    '
name|'def'
name|'_cs_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Check that certain things are called correctly'
nl|'\n'
indent|'        '
name|'if'
name|'method'
name|'in'
op|'['
string|"'GET'"
op|','
string|"'DELETE'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'assert'
string|"'body'"
name|'not'
name|'in'
name|'kwargs'
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'PUT'"
op|':'
newline|'\n'
indent|'            '
name|'assert'
string|"'body'"
name|'in'
name|'kwargs'
newline|'\n'
nl|'\n'
comment|'# Call the method'
nl|'\n'
dedent|''
name|'args'
op|'='
name|'urlparse'
op|'.'
name|'parse_qsl'
op|'('
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
op|'['
number|'4'
op|']'
op|')'
newline|'\n'
name|'kwargs'
op|'.'
name|'update'
op|'('
name|'args'
op|')'
newline|'\n'
name|'munged_url'
op|'='
name|'url'
op|'.'
name|'rsplit'
op|'('
string|"'?'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'munged_url'
op|'='
name|'munged_url'
op|'.'
name|'strip'
op|'('
string|"'/'"
op|')'
op|'.'
name|'replace'
op|'('
string|"'/'"
op|','
string|"'_'"
op|')'
op|'.'
name|'replace'
op|'('
string|"'.'"
op|','
string|"'_'"
op|')'
newline|'\n'
name|'munged_url'
op|'='
name|'munged_url'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
newline|'\n'
nl|'\n'
name|'callback'
op|'='
string|'"%s_%s"'
op|'%'
op|'('
name|'method'
op|'.'
name|'lower'
op|'('
op|')'
op|','
name|'munged_url'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'self'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'AssertionError'
op|'('
string|"'Called unknown API method: %s %s, '"
nl|'\n'
string|"'expected fakes method name: %s'"
op|'%'
nl|'\n'
op|'('
name|'method'
op|','
name|'url'
op|','
name|'callback'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note the call'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'callstack'
op|'.'
name|'append'
op|'('
op|'('
name|'method'
op|','
name|'url'
op|','
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'body'"
op|','
name|'None'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'status'
op|','
name|'body'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'callback'
op|')'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'status'
op|','
string|"'items'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib2'
op|'.'
name|'Response'
op|'('
name|'status'
op|')'
op|','
name|'body'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'httplib2'
op|'.'
name|'Response'
op|'('
op|'{'
string|'"status"'
op|':'
name|'status'
op|'}'
op|')'
op|','
name|'body'
newline|'\n'
nl|'\n'
DECL|member|get_volumes_1234
dedent|''
dedent|''
name|'def'
name|'get_volumes_1234'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
op|'{'
string|"'volume'"
op|':'
name|'_stub_volume'
op|'('
name|'id'
op|'='
string|"'1234'"
op|')'
op|'}'
newline|'\n'
name|'return'
op|'('
number|'200'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volumes_nonexisting
dedent|''
name|'def'
name|'get_volumes_nonexisting'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'cinder_exception'
op|'.'
name|'NotFound'
op|'('
name|'code'
op|'='
number|'404'
op|','
name|'message'
op|'='
string|"'Resource not found'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_volumes_5678
dedent|''
name|'def'
name|'get_volumes_5678'
op|'('
name|'self'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Volume with image metadata"""'
newline|'\n'
name|'volume'
op|'='
op|'{'
string|"'volume'"
op|':'
name|'_stub_volume'
op|'('
name|'id'
op|'='
string|"'1234'"
op|','
nl|'\n'
name|'volume_image_metadata'
op|'='
name|'_image_metadata'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
op|'('
number|'200'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCinderClient
dedent|''
dedent|''
name|'class'
name|'FakeCinderClient'
op|'('
name|'cinder'
op|'.'
name|'cinder_client'
op|'.'
name|'Client'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'username'
op|','
name|'password'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'auth_url'
op|'='
name|'None'
op|','
nl|'\n'
name|'retries'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeCinderClient'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'username'
op|','
name|'password'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'auth_url'
op|'='
name|'auth_url'
op|','
nl|'\n'
name|'retries'
op|'='
name|'retries'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'FakeHTTPClient'
op|'('
name|'username'
op|','
name|'password'
op|','
name|'project_id'
op|','
name|'auth_url'
op|','
nl|'\n'
name|'retries'
op|'='
name|'retries'
op|')'
newline|'\n'
comment|"# keep a ref to the clients callstack for factory's assert_called"
nl|'\n'
name|'self'
op|'.'
name|'callstack'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'callstack'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeClientFactory
dedent|''
dedent|''
name|'class'
name|'FakeClientFactory'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Keep a ref to the FakeClient since volume.api.cinder throws it away."""'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'='
name|'FakeCinderClient'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'client'
newline|'\n'
nl|'\n'
DECL|member|assert_called
dedent|''
name|'def'
name|'assert_called'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'url'
op|','
name|'body'
op|'='
name|'None'
op|','
name|'pos'
op|'='
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'('
name|'method'
op|','
name|'url'
op|')'
newline|'\n'
name|'called'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'callstack'
op|'['
name|'pos'
op|']'
op|'['
number|'0'
op|':'
number|'2'
op|']'
newline|'\n'
nl|'\n'
name|'assert'
name|'self'
op|'.'
name|'client'
op|'.'
name|'callstack'
op|','
op|'('
string|'"Expected %s %s but no calls "'
nl|'\n'
string|'"were made."'
op|'%'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'assert'
name|'expected'
op|'=='
name|'called'
op|','
string|"'Expected %s %s; got %s %s'"
op|'%'
op|'('
name|'expected'
op|'+'
nl|'\n'
name|'called'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'body'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'assert'
name|'self'
op|'.'
name|'client'
op|'.'
name|'callstack'
op|'['
name|'pos'
op|']'
op|'['
number|'2'
op|']'
op|'=='
name|'body'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CinderTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'CinderTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for cinder volume api."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'CinderTestCase'
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
name|'fake_client_factory'
op|'='
name|'FakeClientFactory'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'cinder_client'
op|','
string|'"Client"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_client_factory'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'cinder'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'catalog'
op|'='
op|'['
op|'{'
nl|'\n'
string|'"type"'
op|':'
string|'"volume"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"cinder"'
op|','
nl|'\n'
string|'"endpoints"'
op|':'
op|'['
op|'{'
string|'"publicURL"'
op|':'
string|'"http://localhost:8776/v1/project_id"'
op|'}'
op|']'
nl|'\n'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'username'"
op|','
string|"'project_id'"
op|','
nl|'\n'
name|'service_catalog'
op|'='
name|'catalog'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assert_called
dedent|''
name|'def'
name|'assert_called'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fake_client_factory'
op|'.'
name|'assert_called'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_context_with_catalog
dedent|''
name|'def'
name|'test_context_with_catalog'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_called'
op|'('
string|"'GET'"
op|','
string|"'/volumes/1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_client_factory'
op|'.'
name|'client'
op|'.'
name|'client'
op|'.'
name|'management_url'
op|','
nl|'\n'
string|"'http://localhost:8776/v1/project_id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_endpoint_template
dedent|''
name|'def'
name|'test_cinder_endpoint_template'
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
nl|'\n'
name|'cinder_endpoint_template'
op|'='
string|"'http://other_host:8776/v1/%(project_id)s'"
nl|'\n'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_called'
op|'('
string|"'GET'"
op|','
string|"'/volumes/1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_client_factory'
op|'.'
name|'client'
op|'.'
name|'client'
op|'.'
name|'management_url'
op|','
nl|'\n'
string|"'http://other_host:8776/v1/project_id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_non_existing_volume
dedent|''
name|'def'
name|'test_get_non_existing_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'nonexisting'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_with_image_metadata
dedent|''
name|'def'
name|'test_volume_with_image_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'5678'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_called'
op|'('
string|"'GET'"
op|','
string|"'/volumes/5678'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'volume_image_metadata'"
name|'in'
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume'
op|'['
string|"'volume_image_metadata'"
op|']'
op|','
name|'_image_metadata'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cinder_http_retries
dedent|''
name|'def'
name|'test_cinder_http_retries'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'retries'
op|'='
number|'42'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cinder_http_retries'
op|'='
name|'retries'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_called'
op|'('
string|"'GET'"
op|','
string|"'/volumes/1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_client_factory'
op|'.'
name|'client'
op|'.'
name|'client'
op|'.'
name|'retries'
op|','
name|'retries'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
