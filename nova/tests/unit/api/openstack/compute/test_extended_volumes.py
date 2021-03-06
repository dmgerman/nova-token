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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
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
op|'.'
name|'compute'
name|'import'
op|'('
name|'extended_volumes'
nl|'\n'
name|'as'
name|'extended_volumes_v21'
op|')'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
name|'as'
name|'os_wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
name|'fake_block_device'
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
name|'import'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|UUID1
name|'UUID1'
op|'='
string|"'00000000-0000-0000-0000-000000000001'"
newline|'\n'
DECL|variable|UUID2
name|'UUID2'
op|'='
string|"'00000000-0000-0000-0000-000000000002'"
newline|'\n'
DECL|variable|UUID3
name|'UUID3'
op|'='
string|"'00000000-0000-0000-0000-000000000003'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get
name|'def'
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'inst'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|')'
newline|'\n'
name|'return'
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'args'
op|'['
number|'1'
op|']'
op|','
op|'**'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get_all
dedent|''
name|'def'
name|'fake_compute_get_all'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'db_list'
op|'='
op|'['
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|')'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'2'
op|','
name|'uuid'
op|'='
name|'UUID2'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'fields'
op|'='
name|'instance_obj'
op|'.'
name|'INSTANCE_DEFAULT_FIELDS'
newline|'\n'
name|'return'
name|'instance_obj'
op|'.'
name|'_make_instance_list'
op|'('
name|'args'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceList'
op|'('
op|')'
op|','
nl|'\n'
name|'db_list'
op|','
name|'fields'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_bdms_get_all_by_instance_uuids
dedent|''
name|'def'
name|'fake_bdms_get_all_by_instance_uuids'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'some_volume_1'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'UUID1'
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
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'some_volume_2'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'UUID2'
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
string|"'delete_on_termination'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
name|'fake_block_device'
op|'.'
name|'FakeDbBlockDeviceDict'
op|'('
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'3'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'some_volume_3'"
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'UUID2'
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
string|"'delete_on_termination'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_volume_get
dedent|''
name|'def'
name|'fake_volume_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesTestV21
dedent|''
name|'class'
name|'ExtendedVolumesTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'os-extended-volumes:'"
newline|'\n'
DECL|variable|exp_volumes_show
name|'exp_volumes_show'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
string|"'some_volume_1'"
op|'}'
op|']'
newline|'\n'
DECL|variable|exp_volumes_detail
name|'exp_volumes_detail'
op|'='
op|'['
nl|'\n'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'some_volume_1'"
op|'}'
op|']'
op|','
nl|'\n'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'some_volume_2'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'some_volume_3'"
op|'}'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|wsgi_api_version
name|'wsgi_api_version'
op|'='
name|'os_wsgi'
op|'.'
name|'DEFAULT_API_VERSION'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'ExtendedVolumesTestV21'
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
name|'stub_out_nw_api'
op|'('
name|'self'
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
string|"'get'"
op|','
name|'fake_compute_get'
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
string|"'get_all'"
op|','
name|'fake_compute_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.block_device_mapping_get_all_by_instance_uuids'"
op|','
nl|'\n'
name|'fake_bdms_get_all_by_instance_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'self'
op|'.'
name|'_setup_app'
op|'('
op|')'
newline|'\n'
name|'return_server'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_get_by_uuid'"
op|','
name|'return_server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_app
dedent|''
name|'def'
name|'_setup_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'wsgi_app_v21'
op|'('
name|'init_only'
op|'='
op|'('
string|"'os-extended-volumes'"
op|','
nl|'\n'
string|"'servers'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setUp
dedent|''
name|'def'
name|'_setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'Controller'
op|'='
name|'extended_volumes_v21'
op|'.'
name|'ExtendedVolumesController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'cinder'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_volume_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_request
dedent|''
name|'def'
name|'_make_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'body'
op|'='
name|'None'
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
string|"'/v2/fake/servers'"
op|'+'
name|'url'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'='
op|'{'
name|'os_wsgi'
op|'.'
name|'API_VERSION_REQUEST_HEADER'
op|':'
nl|'\n'
name|'self'
op|'.'
name|'wsgi_api_version'
op|'}'
newline|'\n'
name|'if'
name|'body'
op|':'
newline|'\n'
indent|'            '
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
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
dedent|''
name|'req'
op|'.'
name|'content_type'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_get_server
dedent|''
name|'def'
name|'_get_server'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_servers
dedent|''
name|'def'
name|'_get_servers'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'body'
op|')'
op|'.'
name|'get'
op|'('
string|"'servers'"
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
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
string|"'/%s'"
op|'%'
name|'UUID1'
op|')'
newline|'\n'
nl|'\n'
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
name|'server'
op|'='
name|'self'
op|'.'
name|'_get_server'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'server'
op|'.'
name|'get'
op|'('
string|"'%svolumes_attached'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'exp_volumes_show'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
string|"'/detail'"
op|')'
newline|'\n'
nl|'\n'
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
name|'for'
name|'i'
op|','
name|'server'
name|'in'
name|'enumerate'
op|'('
name|'self'
op|'.'
name|'_get_servers'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'actual'
op|'='
name|'server'
op|'.'
name|'get'
op|'('
string|"'%svolumes_attached'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'exp_volumes_detail'
op|'['
name|'i'
op|']'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesTestV2
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtendedVolumesTestV2'
op|'('
name|'ExtendedVolumesTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_setup_app
indent|'    '
name|'def'
name|'_setup_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setUp
dedent|''
name|'def'
name|'_setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
string|"'nova.api.openstack.compute.'"
nl|'\n'
string|"'contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Extended_volumes'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesTestV23
dedent|''
dedent|''
name|'class'
name|'ExtendedVolumesTestV23'
op|'('
name|'ExtendedVolumesTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|exp_volumes_show
indent|'    '
name|'exp_volumes_show'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'some_volume_1'"
op|','
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|exp_volumes_detail
name|'exp_volumes_detail'
op|'='
op|'['
nl|'\n'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'some_volume_1'"
op|','
string|"'delete_on_termination'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'some_volume_2'"
op|','
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'some_volume_3'"
op|','
string|"'delete_on_termination'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|wsgi_api_version
name|'wsgi_api_version'
op|'='
string|"'2.3'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesEnforcementV21
dedent|''
name|'class'
name|'ExtendedVolumesEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'ExtendedVolumesEnforcementV21'
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
name|'extended_volumes_v21'
op|'.'
name|'ExtendedVolumesController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
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
name|'extended_volumes_v21'
op|'.'
name|'ExtendedVolumesController'
op|','
nl|'\n'
string|"'_extend_server'"
op|')'
newline|'\n'
DECL|member|test_extend_show_policy_failed
name|'def'
name|'test_extend_show_policy_failed'
op|'('
name|'self'
op|','
name|'mock_extend'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-extended-volumes'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
comment|"# Pass ResponseObj as None, the code shouldn't touch the None."
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'None'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_extend'
op|'.'
name|'called'
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
name|'extended_volumes_v21'
op|'.'
name|'ExtendedVolumesController'
op|','
nl|'\n'
string|"'_extend_server'"
op|')'
newline|'\n'
DECL|member|test_extend_detail_policy_failed
name|'def'
name|'test_extend_detail_policy_failed'
op|'('
name|'self'
op|','
name|'mock_extend'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|"'os_compute_api:os-extended-volumes'"
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
comment|"# Pass ResponseObj as None, the code shouldn't touch the None."
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_extend'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
