begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'extended_volumes'
newline|'\n'
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
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
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
op|'.'
name|'tests'
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
DECL|function|fake_compute_get_not_found
dedent|''
name|'def'
name|'fake_compute_get_not_found'
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
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'UUID1'
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
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|')'
op|','
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'2'
op|')'
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
name|'instance_obj'
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
DECL|function|fake_compute_get_instance_bdms
dedent|''
name|'def'
name|'fake_compute_get_instance_bdms'
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
op|'{'
string|"'volume_id'"
op|':'
name|'UUID1'
op|'}'
op|','
op|'{'
string|"'volume_id'"
op|':'
name|'UUID2'
op|'}'
op|']'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_volume_not_found_vol
dedent|''
name|'def'
name|'fake_attach_volume_not_found_vol'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume_id'
op|','
nl|'\n'
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_volume_invalid_device_path
dedent|''
name|'def'
name|'fake_attach_volume_invalid_device_path'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidDevicePath'
op|'('
name|'path'
op|'='
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_volume_instance_invalid_state
dedent|''
name|'def'
name|'fake_attach_volume_instance_invalid_state'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
name|'instance_uuid'
op|'='
name|'UUID1'
op|','
name|'state'
op|'='
string|"''"
op|','
nl|'\n'
name|'method'
op|'='
string|"''"
op|','
name|'attr'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_attach_volume_invalid_volume
dedent|''
name|'def'
name|'fake_attach_volume_invalid_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
string|"''"
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
name|'instance'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_swap_volume
dedent|''
name|'def'
name|'fake_swap_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'old_volume_id'
op|','
name|'new_volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_swap_volume_invalid_volume
dedent|''
name|'def'
name|'fake_swap_volume_invalid_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
string|"''"
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_swap_volume_unattached_volume
dedent|''
name|'def'
name|'fake_swap_volume_unattached_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'VolumeUnattached'
op|'('
name|'reason'
op|'='
string|"''"
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_detach_volume_invalid_volume
dedent|''
name|'def'
name|'fake_detach_volume_invalid_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
op|'('
name|'reason'
op|'='
string|"''"
op|')'
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
DECL|function|fake_volume_get_not_found
dedent|''
name|'def'
name|'fake_volume_get_not_found'
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
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'UUID1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesTest
dedent|''
name|'class'
name|'ExtendedVolumesTest'
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
name|'ExtendedVolumesTest'
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
name|'Controller'
op|'='
name|'extended_volumes'
op|'.'
name|'ExtendedVolumesController'
op|'('
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
string|"'get_instance_bdms'"
op|','
nl|'\n'
name|'fake_compute_get_instance_bdms'
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
string|"'detach_volume'"
op|','
name|'fake_detach_volume'
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
string|"'attach_volume'"
op|','
name|'fake_attach_volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
name|'return_server'
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
name|'dumps'
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
string|"'application/json'"
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
name|'url'
op|'='
string|"'/v3/servers/%s'"
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
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
name|'exp_volumes'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'UUID1'
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
name|'UUID2'
op|'}'
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'content_type'
op|'=='
string|"'application/json'"
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
dedent|''
name|'elif'
name|'self'
op|'.'
name|'content_type'
op|'=='
string|"'application/xml'"
op|':'
newline|'\n'
indent|'            '
name|'actual'
op|'='
op|'['
name|'dict'
op|'('
name|'elem'
op|'.'
name|'items'
op|'('
op|')'
op|')'
name|'for'
name|'elem'
name|'in'
nl|'\n'
name|'server'
op|'.'
name|'findall'
op|'('
string|"'%svolume_attached'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_volumes'
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
name|'url'
op|'='
string|"'/v3/servers/detail'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
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
name|'exp_volumes'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'UUID1'
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
name|'UUID2'
op|'}'
op|']'
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
name|'if'
name|'self'
op|'.'
name|'content_type'
op|'=='
string|"'application/json'"
op|':'
newline|'\n'
indent|'                '
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
dedent|''
name|'elif'
name|'self'
op|'.'
name|'content_type'
op|'=='
string|"'application/xml'"
op|':'
newline|'\n'
indent|'                '
name|'actual'
op|'='
op|'['
name|'dict'
op|'('
name|'elem'
op|'.'
name|'items'
op|'('
op|')'
op|')'
name|'for'
name|'elem'
name|'in'
nl|'\n'
name|'server'
op|'.'
name|'findall'
op|'('
string|"'%svolume_attached'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'exp_volumes'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach
dedent|''
dedent|''
name|'def'
name|'test_detach'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
DECL|member|test_detach_volume_from_locked_server
dedent|''
name|'def'
name|'test_detach_volume_from_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'detach_volume'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_with_non_existed_vol
dedent|''
name|'def'
name|'test_detach_with_non_existed_vol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
name|'fake_volume_get_not_found'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID2'
op|'}'
op|'}'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_with_non_existed_instance
dedent|''
name|'def'
name|'test_detach_with_non_existed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
name|'fake_compute_get_not_found'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID2'
op|'}'
op|'}'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_with_invalid_vol
dedent|''
name|'def'
name|'test_detach_with_invalid_vol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'detach_volume'"
op|','
nl|'\n'
name|'fake_detach_volume_invalid_volume'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID2'
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_with_bad_id
dedent|''
name|'def'
name|'test_detach_with_bad_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
string|"'xxx'"
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_without_id
dedent|''
name|'def'
name|'test_detach_without_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
op|'{'
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_volume_with_invalid_request
dedent|''
name|'def'
name|'test_detach_volume_with_invalid_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"detach"'
op|':'
name|'None'
op|'}'
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
number|'400'
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
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
DECL|member|test_attach_volume_to_locked_server
dedent|''
name|'def'
name|'test_attach_volume_to_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_bad_id
dedent|''
name|'def'
name|'test_attach_volume_with_bad_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
string|"'xxx'"
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_without_id
dedent|''
name|'def'
name|'test_attach_volume_without_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_invalid_request
dedent|''
name|'def'
name|'test_attach_volume_with_invalid_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
name|'None'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_non_existe_vol
dedent|''
name|'def'
name|'test_attach_volume_with_non_existe_vol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_not_found_vol'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_non_existed_instance
dedent|''
name|'def'
name|'test_attach_volume_with_non_existed_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
name|'fake_compute_get_not_found'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_invalid_device_path
dedent|''
name|'def'
name|'test_attach_volume_with_invalid_device_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_invalid_device_path'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|','
nl|'\n'
string|"'device'"
op|':'
string|"'xxx'"
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_instance_invalid_state
dedent|''
name|'def'
name|'test_attach_volume_with_instance_invalid_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_instance_invalid_state'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_invalid_volume
dedent|''
name|'def'
name|'test_attach_volume_with_invalid_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_invalid_volume'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'UUID1'
op|'}'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume_with_invalid_request_body
dedent|''
name|'def'
name|'test_attach_volume_with_invalid_request_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
string|'"/v3/servers/%s/action"'
op|'%'
name|'UUID1'
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
string|"'attach_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_invalid_volume'
op|')'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_make_request'
op|'('
name|'url'
op|','
op|'{'
string|'"attach"'
op|':'
name|'None'
op|'}'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_swap
dedent|''
name|'def'
name|'_test_swap'
op|'('
name|'self'
op|','
name|'uuid'
op|'='
name|'UUID1'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'body'
name|'or'
op|'{'
string|"'swap_volume_attachment'"
op|':'
op|'{'
string|"'old_volume_id'"
op|':'
name|'uuid'
op|','
nl|'\n'
string|"'new_volume_id'"
op|':'
name|'UUID2'
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
string|"'/v3/servers/%s/action'"
op|'%'
name|'UUID1'
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
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'Controller'
op|'.'
name|'swap'
op|'('
name|'req'
op|','
name|'UUID1'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume
dedent|''
name|'def'
name|'test_swap_volume'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
name|'fake_swap_volume'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_test_swap'
op|'('
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
DECL|member|test_swap_volume_for_locked_server
dedent|''
name|'def'
name|'test_swap_volume_for_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_swap_volume_for_locked_server
indent|'        '
name|'def'
name|'fake_swap_volume_for_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'old_volume'
op|','
name|'new_volume'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
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
string|"'swap_volume'"
op|','
nl|'\n'
name|'fake_swap_volume_for_locked_server'
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
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_for_locked_server_new
dedent|''
name|'def'
name|'test_swap_volume_for_locked_server_new'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_actions_to_locked_server'
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
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_instance_not_found
dedent|''
name|'def'
name|'test_swap_volume_instance_not_found'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_compute_get_not_found'
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
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_with_bad_action
dedent|''
name|'def'
name|'test_swap_volume_with_bad_action'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
name|'fake_swap_volume'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'swap_volume_attachment_bad_action'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'_test_swap'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_with_invalid_body
dedent|''
name|'def'
name|'test_swap_volume_with_invalid_body'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
name|'fake_swap_volume'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'swap_volume_attachment'"
op|':'
op|'{'
string|"'bad_volume_id_body'"
op|':'
name|'UUID1'
op|','
nl|'\n'
string|"'new_volume_id'"
op|':'
name|'UUID2'
op|'}'
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
name|'self'
op|'.'
name|'_test_swap'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_with_invalid_volume
dedent|''
name|'def'
name|'test_swap_volume_with_invalid_volume'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
nl|'\n'
name|'fake_swap_volume_invalid_volume'
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
name|'HTTPBadRequest'
op|','
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_with_unattached_volume
dedent|''
name|'def'
name|'test_swap_volume_with_unattached_volume'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
nl|'\n'
name|'fake_swap_volume_unattached_volume'
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
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_with_bad_state_instance
dedent|''
name|'def'
name|'test_swap_volume_with_bad_state_instance'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
nl|'\n'
name|'fake_attach_volume_instance_invalid_state'
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
name|'HTTPConflict'
op|','
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_no_attachment
dedent|''
name|'def'
name|'test_swap_volume_no_attachment'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
name|'fake_swap_volume'
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
name|'self'
op|'.'
name|'_test_swap'
op|','
name|'UUID3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_volume_not_found
dedent|''
name|'def'
name|'test_swap_volume_not_found'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|"'swap_volume'"
op|','
name|'fake_swap_volume'
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
name|'fake_volume_get_not_found'
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
name|'self'
op|'.'
name|'_test_swap'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedVolumesXmlTest
dedent|''
dedent|''
name|'class'
name|'ExtendedVolumesXmlTest'
op|'('
name|'ExtendedVolumesTest'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/xml'"
newline|'\n'
DECL|variable|prefix
name|'prefix'
op|'='
string|"'{%s}'"
op|'%'
name|'extended_volumes'
op|'.'
name|'ExtendedVolumes'
op|'.'
name|'namespace'
newline|'\n'
nl|'\n'
DECL|member|_get_server
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
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
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
name|'etree'
op|'.'
name|'XML'
op|'('
name|'body'
op|')'
op|'.'
name|'getchildren'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
