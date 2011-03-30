begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'unittest'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
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
name|'import'
name|'nova'
op|'.'
name|'wsgi'
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
nl|'\n'
DECL|function|return_create_instance_metadata_max
name|'def'
name|'return_create_instance_metadata_max'
op|'('
name|'context'
op|','
name|'server_id'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_max_server_metadata'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|return_create_instance_metadata
dedent|''
name|'def'
name|'return_create_instance_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_server_metadata'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_metadata
dedent|''
name|'def'
name|'return_server_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'stub_server_metadata'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_empty_server_metadata
dedent|''
name|'def'
name|'return_empty_server_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_server_metadata
dedent|''
name|'def'
name|'delete_server_metadata'
op|'('
name|'context'
op|','
name|'server_id'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_server_metadata
dedent|''
name|'def'
name|'stub_server_metadata'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"key1"'
op|':'
string|'"value1"'
op|','
nl|'\n'
string|'"key2"'
op|':'
string|'"value2"'
op|','
nl|'\n'
string|'"key3"'
op|':'
string|'"value3"'
op|','
nl|'\n'
string|'"key4"'
op|':'
string|'"value4"'
op|','
nl|'\n'
string|'"key5"'
op|':'
string|'"value5"'
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_max_server_metadata
dedent|''
name|'def'
name|'stub_max_server_metadata'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'key%i'"
op|'%'
name|'num'
op|']'
op|'='
string|'"blah"'
newline|'\n'
dedent|''
name|'return'
name|'metadata'
newline|'\n'
nl|'\n'
DECL|class|ServerMetaDataTest
dedent|''
name|'class'
name|'ServerMetaDataTest'
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
name|'super'
op|'('
name|'ServerMetaDataTest'
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
name|'ServerMetaDataTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_metadata'
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
string|"'/v1.1/servers/1/meta'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_no_data
dedent|''
name|'def'
name|'test_index_no_data'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_empty_server_metadata'
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
string|"'/v1.1/servers/1/meta'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
number|'0'
op|','
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_metadata'
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
string|"'/v1.1/servers/1/meta/key5'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|"'value5'"
op|','
name|'res_dict'
op|'['
string|"'key5'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_meta_not_found
dedent|''
name|'def'
name|'test_show_meta_not_found'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_empty_server_metadata'
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
string|"'/v1.1/servers/1/meta/key6'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_delete'"
op|','
nl|'\n'
name|'delete_server_metadata'
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
string|"'/v1.1/servers/1/meta/key5'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
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
string|"'/v1.1/servers/1/meta'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|'\'{"metadata": {"key1": "value1"}}\''
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
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item
dedent|''
name|'def'
name|'test_update_item'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
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
string|"'/v1.1/servers/1/meta/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|'\'{"key1": "value1"}\''
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
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
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
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_too_many_keys
dedent|''
name|'def'
name|'test_update_item_too_many_keys'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
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
string|"'/v1.1/servers/1/meta/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|'\'{"key1": "value1", "key2": "value2"}\''
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
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_body_uri_mismatch
dedent|''
name|'def'
name|'test_update_item_body_uri_mismatch'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
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
string|"'/v1.1/servers/1/meta/bad'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|'\'{"key1": "value1"}\''
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
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_metadata_items_on_create
dedent|''
name|'def'
name|'test_too_many_metadata_items_on_create'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'key%i'"
op|'%'
name|'num'
op|']'
op|'='
string|'"blah"'
newline|'\n'
dedent|''
name|'json_string'
op|'='
name|'str'
op|'('
name|'data'
op|')'
op|'.'
name|'replace'
op|'('
string|'"\\\'"'
op|','
string|'"\\""'
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
string|"'/v1.1/servers/1/meta'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
name|'json_string'
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
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_many_metadata_items_on_update_item
dedent|''
name|'def'
name|'test_to_many_metadata_items_on_update_item'
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
name|'nova'
op|'.'
name|'db'
op|'.'
name|'api'
op|','
string|"'instance_metadata_update_or_create'"
op|','
nl|'\n'
name|'return_create_instance_metadata_max'
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
string|"'/v1.1/servers/1/meta/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'api.version'"
op|']'
op|'='
string|"'1.1'"
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
string|'\'{"a new key": "a new value"}\''
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
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
