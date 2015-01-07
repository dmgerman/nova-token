begin_unit
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
name|'from'
name|'oslo'
op|'.'
name|'serialization'
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
op|'.'
name|'contrib'
name|'import'
name|'extended_virtual_interfaces_net'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
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
DECL|variable|FAKE_VIFS
name|'FAKE_VIFS'
op|'='
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
op|','
nl|'\n'
string|"'net_uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000001'"
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
op|','
nl|'\n'
string|"'net_uuid'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111112'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|EXPECTED_NET_UUIDS
name|'EXPECTED_NET_UUIDS'
op|'='
op|'['
string|"'00000000-0000-0000-0000-00000000000000001'"
op|','
nl|'\n'
string|"'11111111-1111-1111-1111-11111111111111112'"
op|']'
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
name|'FAKE_VIFS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vif_by_mac_address
dedent|''
name|'def'
name|'get_vif_by_mac_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'mac_address'
op|'=='
string|'"00-00-00-00-00-00"'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'net_uuid'"
op|':'
string|"'00000000-0000-0000-0000-00000000000000001'"
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'net_uuid'"
op|':'
string|"'11111111-1111-1111-1111-11111111111111112'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedServerVIFNetTest
dedent|''
dedent|''
name|'class'
name|'ExtendedServerVIFNetTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|content_type
indent|'    '
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'prefix'
op|'='
string|'"%s:"'
op|'%'
name|'extended_virtual_interfaces_net'
op|'.'
DECL|variable|prefix
name|'Extended_virtual_interfaces_net'
op|'.'
name|'alias'
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
name|'ExtendedServerVIFNetTest'
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
string|'"get_vif_by_mac_address"'
op|','
nl|'\n'
name|'get_vif_by_mac_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Virtual_interfaces'"
op|','
nl|'\n'
string|"'Extended_virtual_interfaces_net'"
op|']'
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
name|'init_only'
op|'='
op|'('
nl|'\n'
string|"'os-virtual-interfaces'"
op|','
string|"'OS-EXT-VIF-NET'"
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
DECL|member|_get_vifs
dedent|''
name|'def'
name|'_get_vifs'
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
string|"'virtual_interfaces'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_net_id
dedent|''
name|'def'
name|'_get_net_id'
op|'('
name|'self'
op|','
name|'vifs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'vif'
name|'in'
name|'vifs'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'vif'
op|'['
string|"'%snet_id'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|']'
newline|'\n'
nl|'\n'
DECL|member|assertVIFs
dedent|''
dedent|''
name|'def'
name|'assertVIFs'
op|'('
name|'self'
op|','
name|'vifs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'net_id'
name|'in'
name|'self'
op|'.'
name|'_get_net_id'
op|'('
name|'vifs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'append'
op|'('
name|'net_id'
op|')'
newline|'\n'
dedent|''
name|'sorted'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'net_uuid'
name|'in'
name|'enumerate'
op|'('
name|'result'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'net_uuid'
op|','
name|'EXPECTED_NET_UUIDS'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_extend_virtual_interfaces_list
dedent|''
dedent|''
name|'def'
name|'test_get_extend_virtual_interfaces_list'
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
string|"'/v2/fake/servers/abcd/os-virtual-interfaces'"
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
name|'self'
op|'.'
name|'assertVIFs'
op|'('
name|'self'
op|'.'
name|'_get_vifs'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
