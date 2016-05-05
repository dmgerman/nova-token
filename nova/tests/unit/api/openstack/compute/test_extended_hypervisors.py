begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'hypervisors'
name|'as'
name|'hypervisors_v21'
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
op|'.'
name|'compute'
name|'import'
name|'test_hypervisors'
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
DECL|function|fake_compute_node_get
name|'def'
name|'fake_compute_node_get'
op|'('
name|'context'
op|','
name|'compute_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'hyper'
name|'in'
name|'test_hypervisors'
op|'.'
name|'TEST_HYPERS_OBJ'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hyper'
op|'.'
name|'id'
op|'=='
name|'int'
op|'('
name|'compute_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'hyper'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|'('
name|'host'
op|'='
name|'compute_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_node_get_all
dedent|''
name|'def'
name|'fake_compute_node_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'test_hypervisors'
op|'.'
name|'TEST_HYPERS_OBJ'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_service_get_by_compute_host
name|'def'
name|'fake_service_get_by_compute_host'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'service'
name|'in'
name|'test_hypervisors'
op|'.'
name|'TEST_SERVICES'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'service'
op|'.'
name|'host'
op|'=='
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedHypervisorsTestV21
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtendedHypervisorsTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|DETAIL_HYPERS_DICTS
indent|'    '
name|'DETAIL_HYPERS_DICTS'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'test_hypervisors'
op|'.'
name|'TEST_HYPERS'
op|')'
newline|'\n'
name|'del'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'0'
op|']'
op|'['
string|"'service_id'"
op|']'
newline|'\n'
name|'del'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'1'
op|']'
op|'['
string|"'service_id'"
op|']'
newline|'\n'
name|'del'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'del'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'1'
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'0'
op|']'
op|'.'
name|'update'
op|'('
op|'{'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'enabled'"
op|','
nl|'\n'
string|"'service'"
op|':'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|"'compute1'"
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
name|'None'
op|')'
op|'}'
op|')'
newline|'\n'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'1'
op|']'
op|'.'
name|'update'
op|'('
op|'{'
string|"'state'"
op|':'
string|"'up'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'enabled'"
op|','
nl|'\n'
string|"'service'"
op|':'
name|'dict'
op|'('
name|'id'
op|'='
number|'2'
op|','
name|'host'
op|'='
string|"'compute2'"
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
name|'None'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_up_controller
name|'def'
name|'_set_up_controller'
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
name|'hypervisors_v21'
op|'.'
name|'HypervisorsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_request
dedent|''
name|'def'
name|'_get_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-hypervisors/detail'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
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
name|'ExtendedHypervisorsTestV21'
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
name|'_set_up_controller'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|"'compute_node_get_all'"
op|','
nl|'\n'
name|'fake_compute_node_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'host_api'
op|','
string|"'compute_node_get'"
op|','
nl|'\n'
name|'fake_compute_node_get'
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
name|'Service'
op|','
string|"'get_by_compute_host'"
op|','
nl|'\n'
name|'fake_service_get_by_compute_host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_view_hypervisor_detail_noservers
dedent|''
name|'def'
name|'test_view_hypervisor_detail_noservers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'test_hypervisors'
op|'.'
name|'TEST_HYPERS_OBJ'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'test_hypervisors'
op|'.'
name|'TEST_SERVICES'
op|'['
number|'0'
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'self'
op|'.'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'0'
op|']'
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
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisors'
op|'='
name|'self'
op|'.'
name|'DETAIL_HYPERS_DICTS'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_withid
dedent|''
name|'def'
name|'test_show_withid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_get_request'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'self'
op|'.'
name|'DETAIL_HYPERS_DICTS'
op|'['
number|'0'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
