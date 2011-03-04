begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""Tests for Direct API."""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'direct'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'test_cloud'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeService
name|'class'
name|'FakeService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|echo
indent|'    '
name|'def'
name|'echo'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'data'"
op|':'
name|'data'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|context
dedent|''
name|'def'
name|'context'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'user'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectTestCase
dedent|''
dedent|''
name|'class'
name|'DirectTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'DirectTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'direct'
op|'.'
name|'register_service'
op|'('
string|"'fake'"
op|','
name|'FakeService'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'router'
op|'='
name|'direct'
op|'.'
name|'PostParamsMiddleware'
op|'('
nl|'\n'
name|'direct'
op|'.'
name|'JsonParamsMiddleware'
op|'('
nl|'\n'
name|'direct'
op|'.'
name|'Router'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_router'
op|'='
name|'direct'
op|'.'
name|'DelegatedAuthMiddleware'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
string|"'proj1'"
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
name|'direct'
op|'.'
name|'ROUTES'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'DirectTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delegated_auth
dedent|''
name|'def'
name|'test_delegated_auth'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/context'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-Project'"
op|']'
op|'='
string|"'proj1'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'auth_router'
op|')'
newline|'\n'
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'user'"
op|']'
op|','
string|"'user1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'project'"
op|']'
op|','
string|"'proj1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_params
dedent|''
name|'def'
name|'test_json_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/echo'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'json=%s'"
op|'%'
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'data'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'resp_parsed'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_parsed'
op|'['
string|"'data'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_params
dedent|''
name|'def'
name|'test_post_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/echo'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'data=foo'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'resp_parsed'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_parsed'
op|'['
string|"'data'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_proxy
dedent|''
name|'def'
name|'test_proxy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proxy'
op|'='
name|'direct'
op|'.'
name|'Proxy'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'proxy'
op|'.'
name|'fake'
op|'.'
name|'echo'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'data'
op|'='
string|"'baz'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
string|"'data'"
op|']'
op|','
string|"'baz'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectCloudTestCase
dedent|''
dedent|''
name|'class'
name|'DirectCloudTestCase'
op|'('
name|'test_cloud'
op|'.'
name|'CloudTestCase'
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
name|'DirectCloudTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'compute_handle'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
name|'network_api'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'network_api'
op|','
nl|'\n'
name|'volume_api'
op|'='
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'volume_api'
op|')'
newline|'\n'
name|'direct'
op|'.'
name|'register_service'
op|'('
string|"'compute'"
op|','
name|'compute_handle'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'router'
op|'='
name|'direct'
op|'.'
name|'JsonParamsMiddleware'
op|'('
name|'direct'
op|'.'
name|'Router'
op|'('
op|')'
op|')'
newline|'\n'
name|'proxy'
op|'='
name|'direct'
op|'.'
name|'Proxy'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'compute_api'
op|'='
name|'proxy'
op|'.'
name|'compute'
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
name|'DirectCloudTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'direct'
op|'.'
name|'ROUTES'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
