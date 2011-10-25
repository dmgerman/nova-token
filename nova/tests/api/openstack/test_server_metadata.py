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
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'server_metadata'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
nl|'\n'
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
op|','
name|'delete'
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
op|','
name|'delete'
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
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'server_id'
op|','
name|'int'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
string|"'id %s must be int in return server metadata'"
op|'%'
name|'server_id'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
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
nl|'\n'
DECL|function|return_server
dedent|''
name|'def'
name|'return_server'
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
string|"'id'"
op|':'
name|'server_id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_by_uuid
dedent|''
name|'def'
name|'return_server_by_uuid'
op|'('
name|'context'
op|','
name|'server_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_server_nonexistant
dedent|''
name|'def'
name|'return_server_nonexistant'
op|'('
name|'context'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerMetaDataTest
dedent|''
name|'class'
name|'ServerMetaDataTest'
op|'('
name|'test'
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
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
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
op|','
string|"'instance_get'"
op|','
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
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server_by_uuid'
op|')'
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
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_metadata'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'server_metadata'
op|'.'
name|'Controller'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'uuid'
op|'='
name|'str'
op|'('
name|'utils'
op|'.'
name|'gen_uuid'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'url'
op|'='
string|"'/v1.1/fake/servers/%s/metadata'"
op|'%'
name|'self'
op|'.'
name|'uuid'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|','
nl|'\n'
string|"'key3'"
op|':'
string|"'value3'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_nonexistant_server
dedent|''
name|'def'
name|'test_index_nonexistant_server'
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'url'
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_empty_server_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key2'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key2'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'meta'"
op|':'
op|'{'
string|"'key2'"
op|':'
string|"'value2'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_nonexistant_server
dedent|''
name|'def'
name|'test_show_nonexistant_server'
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key2'"
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_empty_server_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key6'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key6'"
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_metadata'
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
string|"'instance_metadata_delete'"
op|','
nl|'\n'
name|'delete_server_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key2'"
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key2'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'None'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_nonexistant_server
dedent|''
name|'def'
name|'test_delete_nonexistant_server'
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
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_meta_not_found
dedent|''
name|'def'
name|'test_delete_meta_not_found'
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_empty_server_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key6'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key6'"
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
op|','
string|"'instance_metadata_get'"
op|','
nl|'\n'
name|'return_server_metadata'
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
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
string|'"application/json"'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key9"'
op|':'
string|'"value9"'
op|'}'
op|'}'
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'update'
op|'('
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
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_empty_body
dedent|''
name|'def'
name|'test_create_empty_body'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_nonexistant_server
dedent|''
name|'def'
name|'test_create_nonexistant_server'
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
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all
dedent|''
name|'def'
name|'test_update_all'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key10'"
op|':'
string|"'value10'"
op|','
nl|'\n'
string|"'key99'"
op|':'
string|"'value99'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_empty_container
dedent|''
name|'def'
name|'test_update_all_empty_container'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_malformed_container
dedent|''
name|'def'
name|'test_update_all_malformed_container'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'meta'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_malformed_data
dedent|''
name|'def'
name|'test_update_all_malformed_data'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'['
string|"'asdf'"
op|']'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all_nonexistant_server
dedent|''
name|'def'
name|'test_update_all_nonexistant_server'
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
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
string|"'key10'"
op|':'
string|"'value10'"
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
string|"'100'"
op|','
name|'body'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
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
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'meta'"
op|':'
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'res_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_nonexistant_server
dedent|''
name|'def'
name|'test_update_item_nonexistant_server'
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
op|','
string|"'instance_get'"
op|','
name|'return_server_nonexistant'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/fake/servers/asdf/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key1'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_empty_body
dedent|''
name|'def'
name|'test_update_item_empty_body'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key1'"
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
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key1'"
op|','
name|'None'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|','
string|'"key2"'
op|':'
string|'"value2"'
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'key1'"
op|','
name|'body'
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
op|','
string|"'instance_metadata_update'"
op|','
nl|'\n'
name|'return_create_instance_metadata'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/bad'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
string|"'bad'"
op|','
name|'body'
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
op|','
string|"'instance_metadata_update'"
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'data'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_metadata_items_on_update_item
dedent|''
name|'def'
name|'test_too_many_metadata_items_on_update_item'
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
op|','
string|"'instance_metadata_update'"
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
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
name|'data'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
name|'self'
op|'.'
name|'uuid'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
