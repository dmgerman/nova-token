begin_unit
comment|'# Copyright (C) 2011 Midokura KK'
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
name|'contrib'
name|'import'
name|'virtual_interfaces'
name|'as'
name|'vi20'
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
name|'virtual_interfaces'
name|'as'
name|'vi21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
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
nl|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get
name|'def'
name|'compute_api_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'dict'
op|'('
name|'uuid'
op|'='
name|'FAKE_UUID'
op|','
name|'id'
op|'='
name|'instance_id'
op|','
name|'instance_type_id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'bob'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vifs_by_instance
dedent|''
name|'def'
name|'get_vifs_by_instance'
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
op|'['
op|'{'
string|"'uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000000'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'00-00-00-00-00-00'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111111'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'11-11-11-11-11-11'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
dedent|''
name|'class'
name|'FakeRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'environ'
op|'='
op|'{'
string|"'nova.context'"
op|':'
name|'context'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerVirtualInterfaceTestV21
dedent|''
dedent|''
name|'class'
name|'ServerVirtualInterfaceTestV21'
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
name|'ServerVirtualInterfaceTestV21'
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
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
nl|'\n'
name|'compute_api_get'
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
string|'"get_vifs_by_instance"'
op|','
nl|'\n'
name|'get_vifs_by_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_controller'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_controller
dedent|''
name|'def'
name|'_set_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'vi21'
op|'.'
name|'ServerVirtualInterfaceController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_virtual_interfaces_list
dedent|''
name|'def'
name|'test_get_virtual_interfaces_list'
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
string|"''"
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
string|"'fake_uuid'"
op|')'
newline|'\n'
name|'response'
op|'='
op|'{'
string|"'virtual_interfaces'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000000'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'00-00-00-00-00-00'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111111'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'11-11-11-11-11-11'"
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
DECL|member|test_vif_instance_not_found
dedent|''
name|'def'
name|'test_vif_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
string|"'get'"
op|')'
newline|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'fake_context'
op|')'
newline|'\n'
nl|'\n'
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'get'
op|'('
name|'fake_context'
op|','
string|"'fake_uuid'"
op|','
nl|'\n'
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"'instance-0000'"
op|')'
op|')'
newline|'\n'
nl|'\n'
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
name|'assertRaises'
op|'('
nl|'\n'
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
nl|'\n'
name|'fake_req'
op|','
string|"'fake_uuid'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerVirtualInterfaceTestV20
dedent|''
dedent|''
name|'class'
name|'ServerVirtualInterfaceTestV20'
op|'('
name|'ServerVirtualInterfaceTestV21'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_set_controller
indent|'    '
name|'def'
name|'_set_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'vi20'
op|'.'
name|'ServerVirtualInterfaceController'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
