begin_unit
comment|'# Copyright 2011 Eldar Nugaev'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'floating_ips'
name|'import'
name|'FloatingIPController'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'floating_ips'
name|'import'
name|'_translate_floating_ip_view'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_get_floating_ip
name|'def'
name|'network_api_get_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"'11.0.0.1'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_list_floating_ips
dedent|''
name|'def'
name|'network_api_list_floating_ips'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|"'instance'"
op|':'
op|'{'
string|"'id'"
op|':'
number|'11'
op|'}'
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
op|'{'
string|"'address'"
op|':'
string|"'10.0.0.1'"
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.11'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_allocate
dedent|''
name|'def'
name|'network_api_allocate'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'10.10.10.10'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_release
dedent|''
name|'def'
name|'network_api_release'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_associate
dedent|''
name|'def'
name|'network_api_associate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_disassociate
dedent|''
name|'def'
name|'network_api_disassociate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpTest
dedent|''
name|'class'
name|'FloatingIpTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|address
indent|'    '
name|'address'
op|'='
string|'"10.10.10.10"'
newline|'\n'
nl|'\n'
DECL|member|_create_floating_ip
name|'def'
name|'_create_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a floating ip object."""'
newline|'\n'
name|'host'
op|'='
string|'"fake_host"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_floating_ip
dedent|''
name|'def'
name|'_delete_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'FloatingIpTest'
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
name|'controller'
op|'='
name|'FloatingIPController'
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
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get_floating_ip"'
op|','
nl|'\n'
name|'network_api_get_floating_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"list_floating_ips"'
op|','
nl|'\n'
name|'network_api_list_floating_ips'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"allocate_floating_ip"'
op|','
nl|'\n'
name|'network_api_allocate'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"release_floating_ip"'
op|','
nl|'\n'
name|'network_api_release'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"associate_floating_ip"'
op|','
nl|'\n'
name|'network_api_associate'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"disassociate_floating_ip"'
op|','
nl|'\n'
name|'network_api_disassociate'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'_create_floating_ip'
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
name|'self'
op|'.'
name|'_delete_floating_ip'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIpTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_translate_floating_ip_view
dedent|''
name|'def'
name|'test_translate_floating_ip_view'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip_address'
op|'='
name|'self'
op|'.'
name|'_create_floating_ip'
op|'('
op|')'
newline|'\n'
name|'floating_ip'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'floating_ip_address'
op|')'
newline|'\n'
name|'view'
op|'='
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'floating_ip'"
name|'in'
name|'view'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'ip'"
op|']'
op|','
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_list
dedent|''
name|'def'
name|'test_floating_ips_list'
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
string|"'/v1.1/os-floating-ips'"
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
name|'response'
op|'='
op|'{'
string|"'floating_ips'"
op|':'
op|'['
op|'{'
string|"'floating_ip'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
number|'11'
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'floating_ip'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'10.10.10.11'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|'}'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_show
dedent|''
name|'def'
name|'test_floating_ip_show'
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
string|"'/v1.1/os-floating-ips/1'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
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
string|"'floating_ip'"
op|']'
op|'['
string|"'ip'"
op|']'
op|','
string|"'10.10.10.10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|','
string|"'11.0.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_allocate
dedent|''
name|'def'
name|'test_floating_ip_allocate'
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
string|"'/v1.1/os-floating-ips'"
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
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'print'
name|'res'
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
name|'ip'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'allocated'"
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
string|"'10.10.10.10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_release
dedent|''
name|'def'
name|'test_floating_ip_release'
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
string|"'/v1.1/os-floating-ips/1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
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
name|'actual'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'released'"
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
string|"'10.10.10.10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_associate
dedent|''
name|'def'
name|'test_floating_ip_associate'
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
name|'associate_address'
op|'='
name|'dict'
op|'('
name|'fixed_ip'
op|'='
string|"'1.2.3.4'"
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
string|"'/v1.1/os-floating-ips/1/associate'"
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
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
name|'actual'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'associated'"
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"floating_ip_id"'
op|':'
string|"'1'"
op|','
nl|'\n'
string|'"floating_ip"'
op|':'
string|'"10.10.10.10"'
op|','
nl|'\n'
string|'"fixed_ip"'
op|':'
string|'"1.2.3.4"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_disassociate
dedent|''
name|'def'
name|'test_floating_ip_disassociate'
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
string|"'/v1.1/os-floating-ips/1/disassociate'"
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
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
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
name|'ip'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'disassociated'"
op|']'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"floating_ip"'
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|'"fixed_ip"'
op|':'
string|"'11.0.0.1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip'
op|','
name|'expected'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
