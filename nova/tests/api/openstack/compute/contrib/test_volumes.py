begin_unit
comment|'# Copyright 2013 Josh Durgin'
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
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
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
name|'contrib'
name|'import'
name|'volumes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
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
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
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
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
DECL|variable|FAKE_UUID_A
name|'FAKE_UUID_A'
op|'='
string|"'00000000-aaaa-aaaa-aaaa-000000000000'"
newline|'\n'
DECL|variable|FAKE_UUID_B
name|'FAKE_UUID_B'
op|'='
string|"'bbbbbbbb-bbbb-bbbb-bbbb-bbbbbbbbbbbb'"
newline|'\n'
DECL|variable|FAKE_UUID_C
name|'FAKE_UUID_C'
op|'='
string|"'cccccccc-cccc-cccc-cccc-cccccccccccc'"
newline|'\n'
DECL|variable|FAKE_UUID_D
name|'FAKE_UUID_D'
op|'='
string|"'dddddddd-dddd-dddd-dddd-dddddddddddd'"
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_UUID
name|'IMAGE_UUID'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_api_create
name|'def'
name|'fake_compute_api_create'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_type'
op|','
name|'image_href'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_block_device_mapping_seen'
newline|'\n'
name|'_block_device_mapping_seen'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'block_device_mapping'"
op|')'
newline|'\n'
nl|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
number|'2'
op|')'
newline|'\n'
name|'resv_id'
op|'='
name|'None'
newline|'\n'
name|'return'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'test_server'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'dict'
op|'('
name|'inst_type'
op|')'
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
name|'IMAGE_UUID'
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
string|"'created_at'"
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
string|"'updated_at'"
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
string|"'progress'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'['
op|']'
nl|'\n'
op|'}'
op|']'
op|','
name|'resv_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance
dedent|''
name|'def'
name|'fake_get_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
op|'{'
string|"'uuid'"
op|':'
name|'instance_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_volume
dedent|''
name|'def'
name|'fake_attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_detach_volume
dedent|''
name|'def'
name|'fake_detach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_instance_bdms
dedent|''
name|'def'
name|'fake_get_instance_bdms'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/fake0'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
string|"'False'"
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'MyNamesVirtual'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'FAKE_UUID_A'
op|','
nl|'\n'
string|"'volume_size'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/fake1'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
string|"'False'"
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'MyNamesVirtual'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
name|'FAKE_UUID_B'
op|','
nl|'\n'
string|"'volume_size'"
op|':'
number|'1'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BootFromVolumeTest
dedent|''
name|'class'
name|'BootFromVolumeTest'
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
name|'BootFromVolumeTest'
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
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'fake_compute_api_create'
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
nl|'\n'
DECL|member|test_create_root_volume
dedent|''
name|'def'
name|'test_create_root_volume'
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
string|"'test_server'"
op|','
name|'imageRef'
op|'='
name|'IMAGE_UUID'
op|','
nl|'\n'
name|'flavorRef'
op|'='
number|'2'
op|','
name|'min_count'
op|'='
number|'1'
op|','
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'block_device_mapping'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'volume_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'device_name'
op|'='
string|"'/dev/vda'"
op|','
nl|'\n'
name|'virtual'
op|'='
string|"'root'"
op|','
nl|'\n'
name|'delete_on_termination'
op|'='
name|'False'
op|','
nl|'\n'
op|')'
op|']'
nl|'\n'
op|')'
op|')'
newline|'\n'
name|'global'
name|'_block_device_mapping_seen'
newline|'\n'
name|'_block_device_mapping_seen'
op|'='
name|'None'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-volumes_boot'"
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
string|"'content-type'"
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
number|'202'
op|')'
newline|'\n'
name|'server'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'FLAGS'
op|'.'
name|'password_length'
op|','
name|'len'
op|'('
name|'server'
op|'['
string|"'adminPass'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'_block_device_mapping_seen'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_block_device_mapping_seen'
op|'['
number|'0'
op|']'
op|'['
string|"'volume_id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_block_device_mapping_seen'
op|'['
number|'0'
op|']'
op|'['
string|"'device_name'"
op|']'
op|','
nl|'\n'
string|"'/dev/vda'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_volume
dedent|''
dedent|''
name|'def'
name|'return_volume'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
name|'volume_id'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeApiTest
dedent|''
name|'class'
name|'VolumeApiTest'
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
name|'VolumeApiTest'
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
string|"'volume_get'"
op|','
name|'return_volume'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"delete"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_delete'
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
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
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
name|'api'
op|'.'
name|'API'
op|','
string|'"get_all"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_all'
op|')'
newline|'\n'
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
DECL|member|test_volume_create
dedent|''
name|'def'
name|'test_volume_create'
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
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"create"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_create'
op|')'
newline|'\n'
nl|'\n'
name|'vol'
op|'='
op|'{'
string|'"size"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"Volume Test Name"'
op|','
nl|'\n'
string|'"display_description"'
op|':'
string|'"Volume Test Desc"'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"zone1:host1"'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"volume"'
op|':'
name|'vol'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-volumes'"
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
string|"'content-type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'volume'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'volume'"
op|']'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'volume'"
op|']'
op|'['
string|"'displayName'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'volume'"
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'display_description'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'volume'"
op|']'
op|'['
string|"'availabilityZone'"
op|']'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_create_no_body
dedent|''
name|'def'
name|'test_volume_create_no_body'
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
string|"'/v2/fake/os-volumes'"
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
op|'{'
op|'}'
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
nl|'\n'
DECL|member|test_volume_index
dedent|''
name|'def'
name|'test_volume_index'
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
string|"'/v2/fake/os-volumes'"
op|')'
newline|'\n'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_detail
dedent|''
name|'def'
name|'test_volume_detail'
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
string|"'/v2/fake/os-volumes/detail'"
op|')'
newline|'\n'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show
dedent|''
name|'def'
name|'test_volume_show'
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
string|"'/v2/fake/os-volumes/123'"
op|')'
newline|'\n'
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show_no_volume
dedent|''
name|'def'
name|'test_volume_show_no_volume'
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
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_notfound'
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
string|"'/v2/fake/os-volumes/456'"
op|')'
newline|'\n'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_delete
dedent|''
name|'def'
name|'test_volume_delete'
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
string|"'/v2/fake/os-volumes/123'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
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
nl|'\n'
DECL|member|test_volume_delete_no_volume
dedent|''
name|'def'
name|'test_volume_delete_no_volume'
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
name|'volume'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_notfound'
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
string|"'/v2/fake/os-volumes/456'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeAttachTests
dedent|''
dedent|''
name|'class'
name|'VolumeAttachTests'
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
name|'VolumeAttachTests'
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
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'compute'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'get_instance_bdms'"
op|','
nl|'\n'
name|'fake_get_instance_bdms'
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
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get_instance'
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
name|'expected_show'
op|'='
op|'{'
string|"'volumeAttachment'"
op|':'
nl|'\n'
op|'{'
string|"'device'"
op|':'
string|"'/dev/fake0'"
op|','
nl|'\n'
string|"'serverId'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'FAKE_UUID_A'
op|','
nl|'\n'
string|"'volumeId'"
op|':'
name|'FAKE_UUID_A'
nl|'\n'
op|'}'
op|'}'
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
name|'attachments'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentController'
op|'('
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
string|"'/v2/fake/os-volumes/show'"
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
op|'{'
op|'}'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'FAKE_UUID_A'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'expected_show'
op|','
name|'result'
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
name|'compute'
op|'.'
name|'API'
op|','
string|"'detach_volume'"
op|','
name|'fake_detach_volume'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentController'
op|'('
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
string|"'/v2/fake/os-volumes/delete'"
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
op|'{'
op|'}'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'FAKE_UUID_A'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'202 Accepted'"
op|','
name|'result'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_vol_not_found
dedent|''
name|'def'
name|'test_delete_vol_not_found'
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
name|'compute'
op|'.'
name|'API'
op|','
string|"'detach_volume'"
op|','
name|'fake_detach_volume'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentController'
op|'('
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
string|"'/v2/fake/os-volumes/delete'"
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
op|'{'
op|'}'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'attachments'
op|'.'
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'FAKE_UUID_C'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume
dedent|''
name|'def'
name|'test_attach_volume'
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
name|'compute'
op|'.'
name|'API'
op|','
string|"'attach_volume'"
op|','
name|'fake_attach_volume'
op|')'
newline|'\n'
name|'attachments'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentController'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'volumeAttachment'"
op|':'
op|'{'
string|"'volumeId'"
op|':'
name|'FAKE_UUID_A'
op|','
nl|'\n'
string|"'device'"
op|':'
string|"'/dev/fake'"
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-volumes/attach'"
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
op|'{'
op|'}'
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
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'result'
op|'='
name|'attachments'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'volumeAttachment'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'00000000-aaaa-aaaa-aaaa-000000000000'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeSerializerTest
dedent|''
dedent|''
name|'class'
name|'VolumeSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_verify_volume_attachment
indent|'    '
name|'def'
name|'_verify_volume_attachment'
op|'('
name|'self'
op|','
name|'attach'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr'
name|'in'
op|'('
string|"'id'"
op|','
string|"'volumeId'"
op|','
string|"'serverId'"
op|','
string|"'device'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'attach'
op|'['
name|'attr'
op|']'
op|')'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_volume
dedent|''
dedent|''
name|'def'
name|'_verify_volume'
op|'('
name|'self'
op|','
name|'vol'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'tag'
op|','
string|"'volume'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'id'"
op|','
string|"'status'"
op|','
string|"'size'"
op|','
string|"'availabilityZone'"
op|','
string|"'createdAt'"
op|','
nl|'\n'
string|"'displayName'"
op|','
string|"'displayDescription'"
op|','
string|"'volumeType'"
op|','
nl|'\n'
string|"'snapshotId'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'vol'
op|'['
name|'attr'
op|']'
op|')'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
op|'('
string|"'attachments'"
op|','
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'attachments'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'child'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'attachment'"
op|','
name|'child'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_volume_attachment'
op|'('
name|'vol'
op|'['
string|"'attachments'"
op|']'
op|'['
number|'0'
op|']'
op|','
name|'child'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'metadata'"
op|':'
newline|'\n'
indent|'                '
name|'not_seen'
op|'='
name|'set'
op|'('
name|'vol'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'gr_child'
name|'in'
name|'child'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'gr_child'
op|'.'
name|'tag'
name|'in'
name|'not_seen'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'vol'
op|'['
string|"'metadata'"
op|']'
op|'['
name|'gr_child'
op|'.'
name|'tag'
op|']'
op|')'
op|','
nl|'\n'
name|'gr_child'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'not_seen'
op|'.'
name|'remove'
op|'('
name|'gr_child'
op|'.'
name|'tag'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'not_seen'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_show_create_serializer
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_attach_show_create_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_attach'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo'"
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'volumeAttachment'
op|'='
name|'raw_attach'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'volumeAttachment'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_volume_attachment'
op|'('
name|'raw_attach'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_index_serializer
dedent|''
name|'def'
name|'test_attach_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'VolumeAttachmentsTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_attaches'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id1'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol_id1'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance1_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id2'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol_id2'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance2_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo2'"
op|')'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'volumeAttachments'
op|'='
name|'raw_attaches'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'volumeAttachments'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'raw_attaches'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'volumeAttachment'"
op|','
name|'child'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_volume_attachment'
op|'('
name|'raw_attaches'
op|'['
name|'idx'
op|']'
op|','
name|'child'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show_create_serializer
dedent|''
dedent|''
name|'def'
name|'test_volume_show_create_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'VolumeTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_volume'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availabilityZone'
op|'='
string|"'vol_availability'"
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo'"
op|')'
op|']'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'vol_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'vol_desc'"
op|','
nl|'\n'
name|'volumeType'
op|'='
string|"'vol_type'"
op|','
nl|'\n'
name|'snapshotId'
op|'='
string|"'snap_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'bar'"
op|','
nl|'\n'
name|'baz'
op|'='
string|"'quux'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'volume'
op|'='
name|'raw_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_volume'
op|'('
name|'raw_volume'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_index_detail_serializer
dedent|''
name|'def'
name|'test_volume_index_detail_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'VolumesTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_volumes'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol1_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availabilityZone'
op|'='
string|"'vol1_availability'"
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo1'"
op|')'
op|']'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'vol1_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'vol1_desc'"
op|','
nl|'\n'
name|'volumeType'
op|'='
string|"'vol1_type'"
op|','
nl|'\n'
name|'snapshotId'
op|'='
string|"'snap1_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'vol1_foo'"
op|','
nl|'\n'
name|'bar'
op|'='
string|"'vol1_bar'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol2_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availabilityZone'
op|'='
string|"'vol2_availability'"
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
name|'serverId'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo2'"
op|')'
op|']'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'vol2_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'vol2_desc'"
op|','
nl|'\n'
name|'volumeType'
op|'='
string|"'vol2_type'"
op|','
nl|'\n'
name|'snapshotId'
op|'='
string|"'snap2_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'vol2_foo'"
op|','
nl|'\n'
name|'bar'
op|'='
string|"'vol2_bar'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|')'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'volumes'
op|'='
name|'raw_volumes'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'volumes'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'raw_volumes'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_verify_volume'
op|'('
name|'raw_volumes'
op|'['
name|'idx'
op|']'
op|','
name|'child'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
