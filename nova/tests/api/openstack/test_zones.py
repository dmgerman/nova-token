begin_unit
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'zones'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_get
name|'def'
name|'zone_get'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'bob'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'xxx'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_create
dedent|''
name|'def'
name|'zone_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'zone'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'zone'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'zone'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_update
dedent|''
name|'def'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'zone'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
name|'zone_id'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'bob'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'xxx'"
op|')'
newline|'\n'
name|'zone'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'zone'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_delete
dedent|''
name|'def'
name|'zone_delete'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_get_all_scheduler
dedent|''
name|'def'
name|'zone_get_all_scheduler'
op|'('
name|'x'
op|','
name|'y'
op|','
name|'z'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'bob'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'xxx'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'api_url'
op|'='
string|"'http://blah.com'"
op|','
name|'username'
op|'='
string|"'alice'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'qwerty'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_get_all_scheduler_empty
dedent|''
name|'def'
name|'zone_get_all_scheduler_empty'
op|'('
name|'x'
op|','
name|'y'
op|','
name|'z'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_get_all_db
dedent|''
name|'def'
name|'zone_get_all_db'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'api_url'
op|'='
string|"'http://foo.com'"
op|','
name|'username'
op|'='
string|"'bob'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'xxx'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'api_url'
op|'='
string|"'http://blah.com'"
op|','
name|'username'
op|'='
string|"'alice'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'qwerty'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZonesTest
dedent|''
name|'class'
name|'ZonesTest'
op|'('
name|'unittest'
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
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_networking'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'fakes'
op|'.'
name|'stub_out_auth'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'allow_admin'
op|'='
name|'FLAGS'
op|'.'
name|'allow_admin_api'
newline|'\n'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get'"
op|','
name|'zone_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_update'"
op|','
name|'zone_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_create'"
op|','
name|'zone_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_delete'"
op|','
name|'zone_delete'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'self'
op|'.'
name|'allow_admin'
newline|'\n'
nl|'\n'
DECL|member|test_get_zone_list_scheduler
dedent|''
name|'def'
name|'test_get_zone_list_scheduler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'zones'
op|'.'
name|'Controller'
op|','
string|"'_call_scheduler'"
op|','
nl|'\n'
name|'zone_get_all_scheduler'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/zones'"
op|')'
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
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'zones'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_zone_list_db
dedent|''
name|'def'
name|'test_get_zone_list_db'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'zones'
op|'.'
name|'Controller'
op|','
string|"'_call_scheduler'"
op|','
nl|'\n'
name|'zone_get_all_scheduler_empty'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'zone_get_all'"
op|','
name|'zone_get_all_db'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/zones'"
op|')'
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
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'zones'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_zone_by_id
dedent|''
name|'def'
name|'test_get_zone_by_id'
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
string|"'/v1.0/zones/1'"
op|')'
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
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'api_url'"
op|']'
op|','
string|"'http://foo.com'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'password'"
name|'in'
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_zone_delete
dedent|''
name|'def'
name|'test_zone_delete'
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
string|"'/v1.0/zones/1'"
op|')'
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
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_zone_create
dedent|''
name|'def'
name|'test_zone_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'zone'
op|'='
name|'dict'
op|'('
name|'api_url'
op|'='
string|"'http://blah.zoo'"
op|','
name|'username'
op|'='
string|"'fred'"
op|','
nl|'\n'
name|'password'
op|'='
string|"'fubar'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/zones'"
op|')'
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
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
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
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'api_url'"
op|']'
op|','
string|"'http://blah.zoo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'username'"
name|'in'
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_zone_update
dedent|''
name|'def'
name|'test_zone_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'zone'
op|'='
name|'dict'
op|'('
name|'username'
op|'='
string|"'zeb'"
op|','
name|'password'
op|'='
string|"'sneaky'"
op|')'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/zones/1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
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
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|'['
string|"'api_url'"
op|']'
op|','
string|"'http://foo.com'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'username'"
name|'in'
name|'res_dict'
op|'['
string|"'zone'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
