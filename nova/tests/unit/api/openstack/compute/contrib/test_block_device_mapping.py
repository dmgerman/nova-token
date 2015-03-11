begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
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
name|'from'
name|'webob'
name|'import'
name|'exc'
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
name|'extensions'
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
name|'plugins'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'block_device_mapping'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'servers'
name|'as'
name|'servers_v21'
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
name|'as'
name|'servers_v2'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'matchers'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BlockDeviceMappingTestV21
name|'class'
name|'BlockDeviceMappingTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
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
string|"'os-block-device-mapping'"
op|','
nl|'\n'
string|"'osapi_v3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_bdm_v2_controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
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
string|"''"
op|','
string|"'osapi_v3'"
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
name|'BlockDeviceMappingTestV21'
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
name|'_setup_controller'
op|'('
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
nl|'\n'
name|'self'
op|'.'
name|'bdm'
op|'='
op|'['
op|'{'
nl|'\n'
string|"'no_device'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'vdb'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_servers_body
dedent|''
name|'def'
name|'_get_servers_body'
op|'('
name|'self'
op|','
name|'no_image'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'http://localhost/123/flavors/3'"
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'no_image'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'imageRef'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|_test_create
dedent|''
name|'def'
name|'_test_create'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'False'
op|','
name|'override_controller'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'_get_servers_body'
op|'('
name|'no_image'
op|')'
newline|'\n'
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers'"
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
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'if'
name|'override_controller'
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
DECL|member|test_create_instance_with_block_device_mapping_disabled
dedent|''
dedent|''
name|'def'
name|'test_create_instance_with_block_device_mapping_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdm'
op|'='
op|'['
op|'{'
string|"'device_name'"
op|':'
string|"'foo'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
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
string|"'block_device_mapping'"
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_bdm_v2_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_volumes_enabled_no_image
dedent|''
name|'def'
name|'test_create_instance_with_volumes_enabled_no_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that the create will fail if there is no image\n        and no bdms supplied in the request\n        """'
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
string|"'imageRef'"
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
op|'{'
op|'}'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_bdms_and_no_image
dedent|''
name|'def'
name|'test_create_instance_with_bdms_and_no_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'assertThat'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|'['
number|'0'
op|']'
op|')'
nl|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'_validate_bdm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'_get_bdm_image_metadata'"
op|')'
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'_validate_bdm'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'_get_bdm_image_metadata'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_device_name_not_string
dedent|''
name|'def'
name|'test_create_instance_with_device_name_not_string'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
op|'='
number|'123'
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
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'self'
op|'.'
name|'bdm'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|')'
newline|'\n'
DECL|member|test_create_instance_with_bdm_param_not_list
name|'def'
name|'test_create_instance_with_bdm_param_not_list'
op|'('
name|'self'
op|','
name|'mock_create'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
string|"'/dev/vdb'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'self'
op|'.'
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_device_name_empty
dedent|''
name|'def'
name|'test_create_instance_with_device_name_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
op|'='
string|"''"
newline|'\n'
nl|'\n'
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
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'self'
op|'.'
name|'bdm'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_device_name_too_long
dedent|''
name|'def'
name|'test_create_instance_with_device_name_too_long'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
op|'='
string|"'a'"
op|'*'
number|'256'
newline|'\n'
nl|'\n'
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
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'self'
op|'.'
name|'bdm'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_space_in_device_name
dedent|''
name|'def'
name|'test_create_instance_with_space_in_device_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
op|'='
string|"'v da'"
newline|'\n'
nl|'\n'
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
name|'assertTrue'
op|'('
name|'kwargs'
op|'['
string|"'legacy_bdm'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'self'
op|'.'
name|'bdm'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_invalid_size
dedent|''
name|'def'
name|'test_create_instance_with_invalid_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'volume_size'"
op|']'
op|'='
string|"'hello world'"
newline|'\n'
nl|'\n'
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
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'self'
op|'.'
name|'bdm'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_bdm
dedent|''
name|'def'
name|'test_create_instance_bdm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdm'
op|'='
op|'['
op|'{'
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'fake_dev'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake_vol'"
nl|'\n'
op|'}'
op|']'
newline|'\n'
name|'bdm_expected'
op|'='
op|'['
op|'{'
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'fake_dev'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake_vol'"
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
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
name|'assertFalse'
op|'('
name|'kwargs'
op|'['
string|"'legacy_bdm'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'expected'
op|','
name|'received'
name|'in'
name|'zip'
op|'('
name|'bdm_expected'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'expected'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'received'
op|')'
op|')'
newline|'\n'
dedent|''
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
DECL|function|_validate_bdm
dedent|''
name|'def'
name|'_validate_bdm'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'_validate_bdm'"
op|','
name|'_validate_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_bdm_missing_device_name
dedent|''
name|'def'
name|'test_create_instance_bdm_missing_device_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
newline|'\n'
nl|'\n'
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
name|'assertFalse'
op|'('
name|'kwargs'
op|'['
string|"'legacy_bdm'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
name|'None'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
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
DECL|function|_validate_bdm
dedent|''
name|'def'
name|'_validate_bdm'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'_validate_bdm'"
op|','
name|'_validate_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_bdm_validation_error
dedent|''
name|'def'
name|'test_create_instance_bdm_validation_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_validate
indent|'        '
name|'def'
name|'_validate'
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
name|'raise'
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|'('
name|'details'
op|'='
string|"'Wrong BDM'"
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
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
string|"'_validate'"
op|','
name|'_validate'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API._get_bdm_image_metadata'"
op|')'
newline|'\n'
DECL|member|test_create_instance_non_bootable_volume_fails
name|'def'
name|'test_create_instance_non_bootable_volume_fails'
op|'('
name|'self'
op|','
name|'fake_bdm_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
newline|'\n'
name|'fake_bdm_meta'
op|'.'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'InvalidBDMVolumeNotBootable'
op|'('
name|'id'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
nl|'\n'
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_bdm_api_validation_fails
dedent|''
name|'def'
name|'test_create_instance_bdm_api_validation_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'validation_fail_test_validate_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'validation_fail_instance_destroy_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'bdm_exceptions'
op|'='
op|'('
op|'('
name|'exception'
op|'.'
name|'InvalidBDMSnapshot'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMVolume'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMImage'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMBootSequence'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMLocalsLimit'
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'ex_iter'
op|'='
name|'iter'
op|'('
name|'bdm_exceptions'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_validate_bdm
name|'def'
name|'_validate_bdm'
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
name|'validation_fail_test_validate_called'
op|'='
name|'True'
newline|'\n'
name|'ex'
op|','
name|'kargs'
op|'='
name|'ex_iter'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'ex'
op|'('
op|'**'
name|'kargs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_instance_destroy
dedent|''
name|'def'
name|'_instance_destroy'
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
name|'validation_fail_instance_destroy_called'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'_validate_bdm'"
op|','
name|'_validate_bdm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'objects'
op|'.'
name|'Instance'
op|','
string|"'destroy'"
op|','
name|'_instance_destroy'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'_unused'
name|'in'
name|'xrange'
op|'('
name|'len'
op|'('
name|'bdm_exceptions'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
nl|'\n'
op|'['
name|'self'
op|'.'
name|'bdm'
op|'['
number|'0'
op|']'
op|'.'
name|'copy'
op|'('
op|')'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'validation_fail_test_validate_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'validation_fail_instance_destroy_called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'validation_fail_test_validate_called'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'validation_fail_instance_destroy_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BlockDeviceMappingTestV2
dedent|''
dedent|''
dedent|''
name|'class'
name|'BlockDeviceMappingTestV2'
op|'('
name|'BlockDeviceMappingTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
nl|'\n'
DECL|member|_setup_controller
name|'def'
name|'_setup_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ext_mgr'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'='
op|'{'
string|"'os-volumes'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'os-block-device-mapping-v2-boot'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers_v2'
op|'.'
name|'Controller'
op|'('
name|'self'
op|'.'
name|'ext_mgr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr_bdm_v2'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr_bdm_v2'
op|'.'
name|'extensions'
op|'='
op|'{'
string|"'os-volumes'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'no_bdm_v2_controller'
op|'='
name|'servers_v2'
op|'.'
name|'Controller'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'ext_mgr_bdm_v2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_block_device_mapping_disabled
dedent|''
name|'def'
name|'test_create_instance_with_block_device_mapping_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdm'
op|'='
op|'['
op|'{'
string|"'device_name'"
op|':'
string|"'foo'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
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
name|'assertIsNone'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
name|'None'
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
nl|'\n'
name|'params'
op|'='
op|'{'
name|'block_device_mapping'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'bdm'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_bdm_v2_controller'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
