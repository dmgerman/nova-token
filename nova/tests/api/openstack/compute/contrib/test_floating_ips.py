begin_unit
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
nl|'\n'
comment|'# Copyright 2011 Eldar Nugaev'
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
name|'contrib'
name|'import'
name|'floating_ips'
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
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
name|'import'
name|'fake_network'
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
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_get_fixed_ip
name|'def'
name|'network_api_get_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'address'"
op|':'
string|"'10.0.0.1'"
op|','
string|"'id'"
op|':'
name|'id'
op|','
string|"'instance_id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_get_floating_ip
dedent|''
name|'def'
name|'network_api_get_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_get_floating_ip_by_address
dedent|''
name|'def'
name|'network_api_get_floating_ip_by_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
number|'10'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_get_floating_ips_by_project
dedent|''
name|'def'
name|'network_api_get_floating_ips_by_project'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
number|'20'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'pool'"
op|':'
string|"'nova'"
op|','
string|"'interface'"
op|':'
string|"'eth0'"
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'10.10.10.11'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'None'
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_get
dedent|''
name|'def'
name|'compute_api_get'
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
DECL|function|network_api_allocate
dedent|''
name|'def'
name|'network_api_allocate'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'10.10.10.10'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_release
dedent|''
name|'def'
name|'network_api_release'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_api_associate
dedent|''
name|'def'
name|'compute_api_associate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_associate
dedent|''
name|'def'
name|'network_api_associate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|','
name|'fixed_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|network_api_disassociate
dedent|''
name|'def'
name|'network_api_disassociate'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_instance_get
dedent|''
name|'def'
name|'fake_instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"uuid"'
op|':'
name|'utils'
op|'.'
name|'gen_uuid'
op|'('
op|')'
op|','
nl|'\n'
string|'"name"'
op|':'
string|"'fake'"
op|','
nl|'\n'
string|'"user_id"'
op|':'
string|"'fakeuser'"
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|"'123'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpTest
dedent|''
name|'class'
name|'FloatingIpTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|floating_ip
indent|'    '
name|'floating_ip'
op|'='
string|'"10.10.10.10"'
newline|'\n'
nl|'\n'
DECL|member|_create_floating_ip
name|'def'
name|'_create_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a floating ip object."""'
newline|'\n'
name|'host'
op|'='
string|'"fake_host"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'self'
op|'.'
name|'floating_ip'
op|','
nl|'\n'
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_floating_ip
dedent|''
name|'def'
name|'_delete_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'floating_ip'
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
name|'FloatingIpTest'
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
name|'network'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get_fixed_ip"'
op|','
nl|'\n'
name|'network_api_get_fixed_ip'
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
string|'"get_floating_ip"'
op|','
nl|'\n'
name|'network_api_get_floating_ip'
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
string|'"get_floating_ip_by_address"'
op|','
nl|'\n'
name|'network_api_get_floating_ip_by_address'
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
string|'"get_floating_ips_by_project"'
op|','
nl|'\n'
name|'network_api_get_floating_ips_by_project'
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
string|'"release_floating_ip"'
op|','
nl|'\n'
name|'network_api_release'
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
string|'"disassociate_floating_ip"'
op|','
nl|'\n'
name|'network_api_disassociate'
op|')'
newline|'\n'
nl|'\n'
name|'fake_network'
op|'.'
name|'fake_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'fake_network'
op|'.'
name|'stub_out_nw_api_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'True'
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
nl|'\n'
name|'fake_instance_get'
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
name|'self'
op|'.'
name|'_create_floating_ip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'floating_ips'
op|'.'
name|'FloatingIPController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'floating_ips'
op|'.'
name|'FloatingIPActionController'
op|'('
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
name|'_delete_floating_ip'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIpTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_translate_floating_ip_view
dedent|''
name|'def'
name|'test_translate_floating_ip_view'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip_address'
op|'='
name|'self'
op|'.'
name|'_create_floating_ip'
op|'('
op|')'
newline|'\n'
name|'floating_ip'
op|'='
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'floating_ip_address'
op|')'
newline|'\n'
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'floating_ip'
op|'['
string|"'instance'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'view'
op|'='
name|'floating_ips'
op|'.'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'floating_ip'"
name|'in'
name|'view'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'ip'"
op|']'
op|','
name|'self'
op|'.'
name|'floating_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'fixed_ip'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_translate_floating_ip_view_dict
dedent|''
name|'def'
name|'test_translate_floating_ip_view_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
string|"'address'"
op|':'
string|"'10.0.0.10'"
op|','
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'view'
op|'='
name|'floating_ips'
op|'.'
name|'_translate_floating_ip_view'
op|'('
name|'floating_ip'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'floating_ip'"
name|'in'
name|'view'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ips_list
dedent|''
name|'def'
name|'test_floating_ips_list'
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
string|"'/v2/fake/os-floating-ips'"
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
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'floating_ips'"
op|':'
op|'['
op|'{'
string|"'instance_id'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'10.10.10.10'"
op|','
nl|'\n'
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'10.10.10.11'"
op|','
nl|'\n'
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'2'
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
DECL|member|test_floating_ip_show
dedent|''
name|'def'
name|'test_floating_ip_show'
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
string|"'/v2/fake/os-floating-ips/1'"
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
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'ip'"
op|']'
op|','
string|"'10.10.10.10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_associated_floating_ip
dedent|''
name|'def'
name|'test_show_associated_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|get_floating_ip
indent|'        '
name|'def'
name|'get_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
string|"'pool'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
number|'11'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|get_fixed_ip
dedent|''
name|'def'
name|'get_fixed_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'address'"
op|':'
string|"'10.0.0.1'"
op|','
string|"'instance_id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"get_floating_ip"'
op|','
name|'get_floating_ip'
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
string|'"get_fixed_ip"'
op|','
name|'get_fixed_ip'
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
string|"'/v2/fake/os-floating-ips/1'"
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
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'ip'"
op|']'
op|','
string|"'10.10.10.10'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
comment|'# test floating ip allocate/release(deallocate)'
nl|'\n'
DECL|member|test_floating_ip_allocate_no_free_ips
dedent|''
name|'def'
name|'test_floating_ip_allocate_no_free_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call
indent|'        '
name|'def'
name|'fake_call'
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
op|'('
name|'rpc_common'
op|'.'
name|'RemoteError'
op|'('
string|"'NoMoreFloatingIps'"
op|','
string|"''"
op|','
string|"''"
op|')'
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
name|'rpc'
op|','
string|'"call"'
op|','
name|'fake_call'
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
string|"'/v2/fake/os-floating-ips'"
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
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_allocate
dedent|''
name|'def'
name|'test_floating_ip_allocate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake1
indent|'        '
name|'def'
name|'fake1'
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
DECL|function|fake2
dedent|''
name|'def'
name|'fake2'
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
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
string|"'10.10.10.10'"
op|','
string|"'pool'"
op|':'
string|"'nova'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"allocate_floating_ip"'
op|','
nl|'\n'
name|'fake1'
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
string|'"get_floating_ip_by_address"'
op|','
nl|'\n'
name|'fake2'
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
string|"'/v2/fake/os-floating-ips'"
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
op|')'
newline|'\n'
nl|'\n'
name|'ip'
op|'='
name|'res_dict'
op|'['
string|"'floating_ip'"
op|']'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"instance_id"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"ip"'
op|':'
string|'"10.10.10.10"'
op|','
nl|'\n'
string|'"fixed_ip"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"pool"'
op|':'
string|"'nova'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_release
dedent|''
name|'def'
name|'test_floating_ip_release'
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
string|"'/v2/fake/os-floating-ips/1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# test floating ip add/remove -> associate/disassociate'
nl|'\n'
nl|'\n'
DECL|member|test_floating_ip_associate
dedent|''
name|'def'
name|'test_floating_ip_associate'
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
name|'addFloatingIp'
op|'='
name|'dict'
op|'('
name|'address'
op|'='
name|'self'
op|'.'
name|'floating_ip'
op|')'
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
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_add_floating_ip'
op|'('
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_disassociate
dedent|''
name|'def'
name|'test_floating_ip_disassociate'
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
name|'removeFloatingIp'
op|'='
name|'dict'
op|'('
name|'address'
op|'='
string|"'10.10.10.10'"
op|')'
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
string|"'/v2/fake/servers/test_inst/action'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_remove_floating_ip'
op|'('
name|'req'
op|','
string|"'test_inst'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
comment|'# these are a few bad param tests'
nl|'\n'
nl|'\n'
DECL|member|test_bad_address_param_in_remove_floating_ip
dedent|''
name|'def'
name|'test_bad_address_param_in_remove_floating_ip'
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
name|'removeFloatingIp'
op|'='
name|'dict'
op|'('
name|'badparam'
op|'='
string|"'11.0.0.1'"
op|')'
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
string|"'/v2/fake/servers/test_inst/action'"
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
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_add_floating_ip'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_dict_param_in_remove_floating_ip
dedent|''
name|'def'
name|'test_missing_dict_param_in_remove_floating_ip'
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
name|'removeFloatingIp'
op|'='
string|"'11.0.0.1'"
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
string|"'/v2/fake/servers/test_inst/action'"
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
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_remove_floating_ip'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_dict_param_in_add_floating_ip
dedent|''
name|'def'
name|'test_missing_dict_param_in_add_floating_ip'
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
name|'addFloatingIp'
op|'='
string|"'11.0.0.1'"
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
string|"'/v2/fake/servers/test_inst/action'"
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
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_add_floating_ip'
op|','
name|'req'
op|','
string|"'test_inst'"
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpSerializerTest
dedent|''
dedent|''
name|'class'
name|'FloatingIpSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_default_serializer
indent|'    '
name|'def'
name|'test_default_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'floating_ips'
op|'.'
name|'FloatingIPTemplate'
op|'('
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
nl|'\n'
name|'floating_ip'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'ip'
op|'='
string|"'10.10.10.10'"
op|','
nl|'\n'
name|'fixed_ip'
op|'='
string|"'10.0.0.1'"
op|','
nl|'\n'
name|'id'
op|'='
number|'1'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
string|"'floating_ip'"
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
string|"'1'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'10.10.10.10'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'10.0.0.1'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_serializer
dedent|''
name|'def'
name|'test_index_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'floating_ips'
op|'.'
name|'FloatingIPsTemplate'
op|'('
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
nl|'\n'
name|'floating_ips'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'instance_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'ip'
op|'='
string|"'10.10.10.10'"
op|','
nl|'\n'
name|'fixed_ip'
op|'='
string|"'10.0.0.1'"
op|','
nl|'\n'
name|'id'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'instance_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'ip'
op|'='
string|"'10.10.10.11'"
op|','
nl|'\n'
name|'fixed_ip'
op|'='
name|'None'
op|','
nl|'\n'
name|'id'
op|'='
number|'2'
op|')'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
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
string|"'floating_ips'"
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
number|'2'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'floating_ip'"
op|','
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'floating_ip'"
op|','
name|'tree'
op|'['
number|'1'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1'"
op|','
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'None'"
op|','
name|'tree'
op|'['
number|'1'
op|']'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'10.10.10.10'"
op|','
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'10.10.10.11'"
op|','
name|'tree'
op|'['
number|'1'
op|']'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'10.0.0.1'"
op|','
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'None'"
op|','
name|'tree'
op|'['
number|'1'
op|']'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1'"
op|','
name|'tree'
op|'['
number|'0'
op|']'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'2'"
op|','
name|'tree'
op|'['
number|'1'
op|']'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
