begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UrlmapTest
name|'class'
name|'UrlmapTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'UrlmapTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'UrlmapTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_version_v2
dedent|''
name|'def'
name|'test_path_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test URL path specifying v2 returns v2 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.0'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_version_v2
dedent|''
name|'def'
name|'test_content_type_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Content-Type specifying v2 returns v2 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|'"application/json;version=2"'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.0'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_version_v2
dedent|''
name|'def'
name|'test_accept_version_v2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Accept header specifying v2 returns v2 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json;version=2"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.0'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_content_type
dedent|''
name|'def'
name|'test_path_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test URL path specifying JSON returns JSON content.'
nl|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v2/fake/images/cedef40a-ed67-4d10-800e-17455edce175.json'"
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/xml"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'images'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_content_type
dedent|''
name|'def'
name|'test_accept_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Accept header specifying JSON returns JSON content.'
nl|'\n'
indent|'        '
name|'url'
op|'='
string|"'/v2/fake/images/cedef40a-ed67-4d10-800e-17455edce175'"
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/xml;q=0.8, application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'images'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_path_version_v21
dedent|''
name|'def'
name|'test_path_version_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test URL path specifying v2.1 returns v2.1 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2.1/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.1'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_version_v21
dedent|''
name|'def'
name|'test_content_type_version_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Content-Type specifying v2.1 returns v2 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|'"application/json;version=2.1"'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.1'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_version_v21
dedent|''
name|'def'
name|'test_accept_version_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Accept header specifying v2.1 returns v2.1 content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/json;version=2.1"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.1'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_accept_content_type_v21
dedent|''
name|'def'
name|'test_accept_content_type_v21'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test Accept header specifying JSON returns JSON content.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|'"application/json;version=2.1"'
newline|'\n'
name|'req'
op|'.'
name|'accept'
op|'='
string|'"application/xml;q=0.8, application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'versions'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"application/json"'
op|','
name|'res'
op|'.'
name|'content_type'
op|')'
newline|'\n'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'v2.1'"
op|','
name|'body'
op|'['
string|"'version'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
