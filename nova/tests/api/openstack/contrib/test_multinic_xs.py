begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'json'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
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
name|'test'
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
DECL|variable|last_add_fixed_ip
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
DECL|variable|last_remove_fixed_ip
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_add_fixed_ip
name|'def'
name|'compute_api_add_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
nl|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'instance_id'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_remove_fixed_ip
dedent|''
name|'def'
name|'compute_api_remove_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
nl|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'instance_id'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FixedIpTest
dedent|''
name|'class'
name|'FixedIpTest'
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
name|'FixedIpTest'
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
name|'reset_fake_data'
op|'('
op|')'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"add_fixed_ip"'
op|','
nl|'\n'
name|'compute_api_add_fixed_ip'
op|')'
newline|'\n'
comment|'# TODO(Vek): Fails until remove_fixed_ip() added'
nl|'\n'
comment|'# self.stubs.Set(compute.api.API, "remove_fixed_ip",'
nl|'\n'
comment|'#                compute_api_remove_fixed_ip)'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
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
name|'super'
op|'('
name|'FixedIpTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip
dedent|''
name|'def'
name|'test_add_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addFixedIp'
op|'='
name|'dict'
op|'('
name|'networkId'
op|'='
string|"'test_net'"
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
string|"'/v1.1/servers/test_inst/action'"
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
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_add_fixed_ip'
op|','
op|'('
string|"'test_inst'"
op|','
string|"'test_net'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_fixed_ip_no_network
dedent|''
name|'def'
name|'test_add_fixed_ip_no_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_add_fixed_ip'
newline|'\n'
name|'last_add_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'addFixedIp'
op|'='
name|'dict'
op|'('
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
string|"'/v1.1/servers/test_inst/action'"
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
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'422'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_add_fixed_ip'
op|','
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip
dedent|''
name|'def'
name|'test_remove_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeFixedIp'
op|'='
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.10.1'"
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
string|"'/v1.1/servers/test_inst/action'"
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
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
comment|'# TODO(Vek): Fails until remove_fixed_ip() added'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'202'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_remove_fixed_ip'
op|','
op|'('
string|"'test_inst'"
op|','
string|"'10.10.10.1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_fixed_ip_no_address
dedent|''
name|'def'
name|'test_remove_fixed_ip_no_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'last_remove_fixed_ip'
newline|'\n'
name|'last_remove_fixed_ip'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'removeFixedIp'
op|'='
name|'dict'
op|'('
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
string|"'/v1.1/servers/test_inst/action'"
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
name|'req'
op|'.'
name|'headers'
op|'['
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
name|'resp'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'422'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'last_remove_fixed_ip'
op|','
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
