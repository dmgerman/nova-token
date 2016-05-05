begin_unit
comment|'# Copyright (c) 2014 IBM Corp.'
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
name|'block_device_mapping_v1'
name|'as'
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
name|'as'
name|'servers_v21'
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
name|'import'
name|'uuidsentinel'
name|'as'
name|'uuids'
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
name|'TestCase'
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
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
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
string|"'osapi_v21'"
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
nl|'\n'
op|'['
string|"'os-block-device-mapping-v1'"
op|','
nl|'\n'
string|"'os-block-device-mapping'"
op|']'
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_volumes_controller'
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
string|"'osapi_v21'"
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_id'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
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
string|"'virtual_name'"
op|':'
string|"'root'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'self'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'vda'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
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
name|'dump_as_bytes'
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
DECL|member|test_create_instance_with_volumes_enabled
dedent|''
dedent|''
name|'def'
name|'test_create_instance_with_volumes_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
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
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_volumes_enabled_and_bdms_no_image
dedent|''
name|'def'
name|'test_create_instance_with_volumes_enabled_and_bdms_no_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that the create works if there is no image supplied but\n        os-volumes extension is enabled and bdms are supplied\n        """'
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
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'uuids'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'volume_image_metadata'"
op|':'
nl|'\n'
op|'{'
string|"'test_key'"
op|':'
string|"'test_value'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'_validate_bdm'
op|'('
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
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'bdm'
op|','
nl|'\n'
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
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
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
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
DECL|member|test_create_instance_with_volumes_disabled
dedent|''
name|'def'
name|'test_create_instance_with_volumes_disabled'
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
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm'
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
name|'block_device_mapping'
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
name|'_test_create'
op|'('
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_volumes_controller'
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
name|'bdm'
op|'='
op|'['
op|'{'
nl|'\n'
string|"'volume_id'"
op|':'
name|'self'
op|'.'
name|'volume_id'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'vda'"
nl|'\n'
op|'}'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
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
name|'self'
op|'.'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
op|'}'
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
DECL|member|test_create_instance_with_snapshot_volume_id_none
dedent|''
name|'def'
name|'test_create_instance_with_snapshot_volume_id_none'
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
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'vda'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
nl|'\n'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm'
op|'}'
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
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
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
op|','
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
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
string|"'vd a'"
op|','
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'self'
op|'.'
name|'bdm'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_instance_with_size_error
dedent|''
name|'def'
name|'_test_create_instance_with_size_error'
op|'('
name|'self'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdm'
op|'='
op|'['
op|'{'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'vda'"
op|','
nl|'\n'
string|"'volume_size'"
op|':'
name|'size'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'11111111-1111-1111-1111-111111111111'"
op|'}'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm'
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
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|','
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
name|'_test_create_instance_with_size_error'
op|'('
string|'"hello world"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_size_empty_string
dedent|''
name|'def'
name|'test_create_instance_with_size_empty_string'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_instance_with_size_error'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_size_zero
dedent|''
name|'def'
name|'test_create_instance_with_size_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_instance_with_size_error'
op|'('
string|'"0"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_size_greater_than_limit
dedent|''
name|'def'
name|'test_create_instance_with_size_greater_than_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_instance_with_size_error'
op|'('
name|'db'
op|'.'
name|'MAX_INT'
op|'+'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_bdm_delete_on_termination
dedent|''
name|'def'
name|'test_create_instance_with_bdm_delete_on_termination'
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
string|"'foo1'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
string|"'True'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo2'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo3'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
string|"'invalid'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo4'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo5'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|']'
newline|'\n'
name|'expected_bdm'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo1'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo2'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo3'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo4'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'device_name'"
op|':'
string|"'foo5'"
op|','
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm'
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
name|'assertEqual'
op|'('
name|'expected_bdm'
op|','
name|'kwargs'
op|'['
string|"'block_device_mapping'"
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
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_decide_format_legacy
dedent|''
name|'def'
name|'test_create_instance_decide_format_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
nl|'\n'
op|'['
string|"'os-block-device-mapping'"
op|','
nl|'\n'
string|"'os-block-device-mapping-v1'"
op|']'
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'bdm'
op|'='
op|'['
op|'{'
string|"'device_name'"
op|':'
string|"'foo1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'expected_legacy_flag'
op|'='
name|'True'
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
name|'legacy_bdm'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'legacy_bdm'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'legacy_bdm'
op|','
name|'expected_legacy_flag'
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
nl|'\n'
name|'_validate_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
op|'{'
op|'}'
op|','
name|'override_controller'
op|'='
name|'controller'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
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
name|'override_controller'
op|'='
name|'controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_both_bdm_formats
dedent|''
name|'def'
name|'test_create_instance_both_bdm_formats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
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
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'both_controllers'
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
name|'bdm_v2'
op|'='
op|'['
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake_vol'"
op|'}'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm'
op|','
nl|'\n'
string|"'block_device_mapping_v2'"
op|':'
name|'bdm_v2'
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
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'both_controllers'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
