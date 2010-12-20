begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'json'
newline|'\n'
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
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'servers'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'models'
name|'import'
name|'Instance'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'rpc'
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
DECL|function|return_server
name|'def'
name|'return_server'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_instance'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_servers
dedent|''
name|'def'
name|'return_servers'
op|'('
name|'context'
op|','
name|'user_id'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
name|'stub_instance'
op|'('
name|'i'
op|','
name|'user_id'
op|')'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'5'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_security_group
dedent|''
name|'def'
name|'return_security_group'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_instance'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_address
dedent|''
name|'def'
name|'instance_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_instance
dedent|''
name|'def'
name|'stub_instance'
op|'('
name|'id'
op|','
name|'user_id'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'Instance'
op|'('
name|'id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
op|'+'
number|'123456'
op|','
name|'state'
op|'='
number|'0'
op|','
name|'image_id'
op|'='
number|'10'
op|','
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'server%s'"
op|'%'
name|'id'
op|','
name|'internal_id'
op|'='
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_api
dedent|''
name|'def'
name|'fake_compute_api'
op|'('
name|'cls'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersTest
dedent|''
name|'class'
name|'ServersTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_image_service'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_get_all'"
op|','
name|'return_servers'
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
op|'.'
name|'api'
op|','
string|"'instance_get_by_internal_id'"
op|','
nl|'\n'
name|'return_server'
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
op|'.'
name|'api'
op|','
string|"'instance_get_all_by_user'"
op|','
nl|'\n'
name|'return_servers'
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
op|'.'
name|'api'
op|','
string|"'instance_add_security_group'"
op|','
nl|'\n'
name|'return_security_group'
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
op|'.'
name|'api'
op|','
string|"'instance_update'"
op|','
name|'instance_update'
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
op|'.'
name|'api'
op|','
string|"'instance_get_fixed_address'"
op|','
nl|'\n'
name|'instance_address'
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
op|'.'
name|'api'
op|','
string|"'instance_get_floating_address'"
op|','
nl|'\n'
name|'instance_address'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'ComputeAPI'
op|','
string|"'pause'"
op|','
nl|'\n'
name|'fake_compute_api'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'ComputeAPI'
op|','
string|"'unpause'"
op|','
nl|'\n'
name|'fake_compute_api'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'allow_admin'
op|'='
name|'FLAGS'
op|'.'
name|'allow_admin_api'
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
DECL|member|test_get_server_by_id
dedent|''
name|'def'
name|'test_get_server_by_id'
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
string|"'/v1.0/servers/1'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'server'"
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
string|"'server'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
string|"'server1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_server_list
dedent|''
name|'def'
name|'test_get_server_list'
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
string|"'/v1.0/servers'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
name|'i'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'s'
name|'in'
name|'res_dict'
op|'['
string|"'servers'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'['
string|"'id'"
op|']'
op|','
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'['
string|"'name'"
op|']'
op|','
string|"'server%d'"
op|'%'
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'.'
name|'get'
op|'('
string|"'imageId'"
op|','
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'i'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance
dedent|''
dedent|''
name|'def'
name|'test_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|instance_create
indent|'        '
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'internal_id'"
op|':'
number|'1'
op|','
string|"'display_name'"
op|':'
string|"''"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|server_update
dedent|''
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance_create'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_method
dedent|''
name|'def'
name|'fake_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|project_get_network
dedent|''
name|'def'
name|'project_get_network'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'1'"
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'network_topic'"
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'project_get_network'"
op|','
name|'project_get_network'
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
op|'.'
name|'api'
op|','
string|"'instance_create'"
op|','
name|'instance_create'
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
name|'rpc'
op|','
string|"'cast'"
op|','
name|'fake_method'
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
name|'rpc'
op|','
string|"'call'"
op|','
name|'fake_method'
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
op|'.'
name|'api'
op|','
string|"'instance_update'"
op|','
nl|'\n'
name|'server_update'
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
op|'.'
name|'api'
op|','
string|"'queue_get_for'"
op|','
name|'queue_get_for'
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
name|'network'
op|'.'
name|'manager'
op|'.'
name|'VlanManager'
op|','
string|"'allocate_fixed_ip'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers'"
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
DECL|member|test_update_no_body
dedent|''
name|'def'
name|'test_update_no_body'
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
string|"'/v1.0/servers/1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
number|'422'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_bad_params
dedent|''
name|'def'
name|'test_update_bad_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Confirm that update is filtering params """'
newline|'\n'
name|'inst_dict'
op|'='
name|'dict'
op|'('
name|'cat'
op|'='
string|"'leopard'"
op|','
name|'name'
op|'='
string|"'server_test'"
op|','
name|'adminPass'
op|'='
string|"'bacon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'dict'
op|'('
name|'server'
op|'='
name|'inst_dict'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|server_update
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'update_called'
op|'='
name|'True'
newline|'\n'
name|'filtered_dict'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'admin_pass'
op|'='
string|"'bacon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'params'
op|','
name|'filtered_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_update'"
op|','
nl|'\n'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/servers/1'"
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
name|'self'
op|'.'
name|'body'
newline|'\n'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server
dedent|''
name|'def'
name|'test_update_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_dict'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'adminPass'
op|'='
string|"'bacon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'dict'
op|'('
name|'server'
op|'='
name|'inst_dict'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|server_update
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'filtered_dict'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'admin_pass'
op|'='
string|"'bacon'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'params'
op|','
name|'filtered_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_update'"
op|','
nl|'\n'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/servers/1'"
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
name|'self'
op|'.'
name|'body'
newline|'\n'
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_backup_schedules
dedent|''
name|'def'
name|'test_create_backup_schedules'
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
string|"'/v1.0/servers/1/backup_schedules'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status'
op|','
string|"'404 Not Found'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_backup_schedules
dedent|''
name|'def'
name|'test_delete_backup_schedules'
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
string|"'/v1.0/servers/1/backup_schedules'"
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status'
op|','
string|"'404 Not Found'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_server_backup_schedules
dedent|''
name|'def'
name|'test_get_server_backup_schedules'
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
string|"'/v1.0/servers/1/backup_schedules'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status'
op|','
string|"'404 Not Found'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_server_details
dedent|''
name|'def'
name|'test_get_all_server_details'
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
string|"'/v1.0/servers/detail'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
name|'i'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'s'
name|'in'
name|'res_dict'
op|'['
string|"'servers'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'['
string|"'id'"
op|']'
op|','
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'['
string|"'name'"
op|']'
op|','
string|"'server%d'"
op|'%'
name|'i'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'s'
op|'['
string|"'imageId'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'i'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_server_pause
dedent|''
dedent|''
name|'def'
name|'test_server_pause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'True'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers/1/pause'"
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
name|'content_type'
op|'='
string|"'application/json'"
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_unpause
dedent|''
name|'def'
name|'test_server_unpause'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'allow_admin_api'
op|'='
name|'True'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers/1/unpause'"
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
name|'content_type'
op|'='
string|"'application/json'"
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
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
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_reboot
dedent|''
name|'def'
name|'test_server_reboot'
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
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers/1/action'"
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
name|'content_type'
op|'='
string|"'application/json'"
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
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
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers/1/action'"
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
name|'content_type'
op|'='
string|"'application/json'"
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
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
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageId'
op|'='
number|'2'
op|','
name|'flavorId'
op|'='
number|'2'
op|','
name|'metadata'
op|'='
op|'{'
op|'}'
op|','
nl|'\n'
name|'personality'
op|'='
op|'{'
op|'}'
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
string|"'/v1.0/servers/1/action'"
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
name|'content_type'
op|'='
string|"'application/json'"
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
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_server_instance
dedent|''
name|'def'
name|'test_delete_server_instance'
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
string|"'/v1.0/servers/1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'server_delete_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|instance_destroy_mock
name|'def'
name|'instance_destroy_mock'
op|'('
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'server_delete_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_destroy'"
op|','
nl|'\n'
name|'instance_destroy_mock'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'API'
op|'('
string|"'os'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status'
op|','
string|"'202 Accepted'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'server_delete_called'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
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
