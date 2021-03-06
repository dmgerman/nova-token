begin_unit
comment|'# Copyright 2014 Intel Corp.'
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
nl|'\n'
DECL|variable|TEST_HYPER
name|'TEST_HYPER'
op|'='
name|'test_hypervisors'
op|'.'
name|'TEST_HYPERS_OBJ'
op|'['
number|'0'
op|']'
op|'.'
name|'obj_clone'
op|'('
op|')'
newline|'\n'
DECL|variable|TEST_SERVICE
name|'TEST_SERVICE'
op|'='
name|'objects'
op|'.'
name|'Service'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|'"compute1"'
op|','
nl|'\n'
DECL|variable|binary
name|'binary'
op|'='
string|'"nova-compute"'
op|','
nl|'\n'
DECL|variable|topic
name|'topic'
op|'='
string|'"compute_topic"'
op|','
nl|'\n'
DECL|variable|report_count
name|'report_count'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|disabled
name|'disabled'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|disabled_reason
name|'disabled_reason'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|availability_zone
name|'availability_zone'
op|'='
string|'"nova"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HypervisorStatusTestV21
name|'class'
name|'HypervisorStatusTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_prepare_extension
indent|'    '
name|'def'
name|'_prepare_extension'
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
DECL|member|test_view_hypervisor_service_status
dedent|''
name|'def'
name|'test_view_hypervisor_service_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_prepare_extension'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'TEST_HYPER'
op|','
name|'TEST_SERVICE'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'enabled'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'up'"
op|','
name|'result'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'enabled'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'TEST_HYPER'
op|','
name|'TEST_SERVICE'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'down'"
op|','
name|'result'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'hyper'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'TEST_HYPER'
op|')'
newline|'\n'
name|'service'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'TEST_SERVICE'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'disabled'
op|'='
name|'True'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
name|'hyper'
op|','
name|'service'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'disabled'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_view_hypervisor_detail_status
dedent|''
name|'def'
name|'test_view_hypervisor_detail_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_prepare_extension'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'TEST_HYPER'
op|','
name|'TEST_SERVICE'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'enabled'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'up'"
op|','
name|'result'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'result'
op|'['
string|"'service'"
op|']'
op|'['
string|"'disabled_reason'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'.'
name|'return_value'
op|'='
name|'False'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
nl|'\n'
name|'TEST_HYPER'
op|','
name|'TEST_SERVICE'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'down'"
op|','
name|'result'
op|'['
string|"'state'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'hyper'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'TEST_HYPER'
op|')'
newline|'\n'
name|'service'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'TEST_SERVICE'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'disabled'
op|'='
name|'True'
newline|'\n'
name|'service'
op|'.'
name|'disabled_reason'
op|'='
string|'"fake"'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_view_hypervisor'
op|'('
name|'hyper'
op|','
name|'service'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'disabled'"
op|','
name|'result'
op|'['
string|"'status'"
op|']'
op|','
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake'"
op|','
name|'result'
op|'['
string|"'service'"
op|']'
op|'['
string|"'disabled_reason'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
