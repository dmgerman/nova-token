begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'base64'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'user_data'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
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
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_gen_uuid
name|'def'
name|'fake_gen_uuid'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FAKE_UUID'
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
DECL|class|ServersControllerCreateTest
dedent|''
name|'class'
name|'ServersControllerCreateTest'
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
string|'"""Shared implementation for tests below that create instance."""'
newline|'\n'
name|'super'
op|'('
name|'ServersControllerCreateTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'enable_instance_password'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
string|"'os-user-data'"
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_user_data_controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_create
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
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
number|'3'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'def_image_ref'
op|'='
string|"'http://localhost/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'+='
number|'1'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|'**'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'instance_cache_num'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
name|'or'
string|"'test'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fead::1234'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'def_image_ref'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
name|'user_data'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'None'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"task_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"root_device_name"'
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'root_device_name'"
op|','
string|"'vda'"
op|')'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Stub for compute/api create() pulling in instance after\n            scheduling\n            """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'uuid'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|server_update
dedent|''
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance_uuid'
op|']'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
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
DECL|function|project_get_networks
dedent|''
name|'def'
name|'project_get_networks'
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
dedent|''
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
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
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
name|'uuid'
op|','
string|"'uuid4'"
op|','
name|'fake_gen_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
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
name|'db'
op|','
string|"'project_get_networks'"
op|','
nl|'\n'
name|'project_get_networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
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
name|'db'
op|','
string|"'instance_system_metadata_update'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get'"
op|','
name|'instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
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
name|'db'
op|','
string|"'instance_update_and_get_original'"
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
DECL|member|_test_create_extra
dedent|''
name|'def'
name|'_test_create_extra'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'False'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageRef'
op|'='
name|'image_uuid'
op|','
name|'flavorRef'
op|'='
number|'2'
op|')'
newline|'\n'
name|'if'
name|'no_image'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'pop'
op|'('
string|"'imageRef'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV21'
op|'.'
name|'blank'
op|'('
string|"'/servers'"
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
name|'jsonutils'
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
name|'if'
name|'override_controller'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'override_controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'server'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_user_data_disabled
dedent|''
name|'def'
name|'test_create_instance_with_user_data_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'user_data'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|"'fake'"
op|')'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
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
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'user_data'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
nl|'\n'
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_user_data_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_user_data_enabled
dedent|''
name|'def'
name|'test_create_instance_with_user_data_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'user_data'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|"'fake'"
op|')'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
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
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'user_data'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_user_data
dedent|''
name|'def'
name|'test_create_instance_with_user_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|'"A random string"'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
name|'user_data'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'value'
op|'}'
newline|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'FAKE_UUID'
op|','
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_bad_user_data
dedent|''
name|'def'
name|'test_create_instance_with_bad_user_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'value'
op|'='
string|'"A random string"'
newline|'\n'
name|'params'
op|'='
op|'{'
name|'user_data'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'value'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
