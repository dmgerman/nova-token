begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'six'
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
name|'used_limits'
name|'as'
name|'used_limits_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'import'
name|'nova'
op|'.'
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
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
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
op|','
name|'reserved'
op|'='
name|'False'
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
name|'self'
op|'.'
name|'reserved'
op|'='
name|'reserved'
newline|'\n'
name|'self'
op|'.'
name|'GET'
op|'='
op|'{'
string|"'reserved'"
op|':'
number|'1'
op|'}'
name|'if'
name|'reserved'
name|'else'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsedLimitsTestCaseV21
dedent|''
dedent|''
name|'class'
name|'UsedLimitsTestCaseV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|used_limit_extension
indent|'    '
name|'used_limit_extension'
op|'='
string|'"os_compute_api:os-used-limits"'
newline|'\n'
DECL|variable|include_server_group_quotas
name|'include_server_group_quotas'
op|'='
name|'True'
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
string|'"""Run before each test."""'
newline|'\n'
name|'super'
op|'('
name|'UsedLimitsTestCaseV21'
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
name|'self'
op|'.'
name|'fake_context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_up_controller
dedent|''
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
name|'ext_mgr'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'used_limits_v21'
op|'.'
name|'UsedLimitsController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'used_limits_v21'
op|','
string|"'authorize'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'authorize'
op|'='
name|'used_limits_v21'
op|'.'
name|'authorize'
newline|'\n'
nl|'\n'
DECL|member|_do_test_used_limits
dedent|''
name|'def'
name|'_do_test_used_limits'
op|'('
name|'self'
op|','
name|'reserved'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'reserved'
op|'='
name|'reserved'
op|')'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'quota_map'
op|'='
op|'{'
nl|'\n'
string|"'totalRAMUsed'"
op|':'
string|"'ram'"
op|','
nl|'\n'
string|"'totalCoresUsed'"
op|':'
string|"'cores'"
op|','
nl|'\n'
string|"'totalInstancesUsed'"
op|':'
string|"'instances'"
op|','
nl|'\n'
string|"'totalFloatingIpsUsed'"
op|':'
string|"'floating_ips'"
op|','
nl|'\n'
string|"'totalSecurityGroupsUsed'"
op|':'
string|"'security_groups'"
op|','
nl|'\n'
string|"'totalServerGroupsUsed'"
op|':'
string|"'server_groups'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'limits'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'expected_abs_limits'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'display_name'
op|','
name|'q'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'quota_map'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'limits'
op|'['
name|'q'
op|']'
op|'='
op|'{'
string|"'limit'"
op|':'
name|'len'
op|'('
name|'display_name'
op|')'
op|','
nl|'\n'
string|"'in_use'"
op|':'
name|'len'
op|'('
name|'display_name'
op|')'
op|'/'
number|'2'
op|','
nl|'\n'
string|"'reserved'"
op|':'
name|'len'
op|'('
name|'display_name'
op|')'
op|'/'
number|'3'
op|'}'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'include_server_group_quotas'
name|'or'
nl|'\n'
name|'display_name'
op|'!='
string|"'totalServerGroupsUsed'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'expected_abs_limits'
op|'.'
name|'append'
op|'('
name|'display_name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|stub_get_project_quotas
dedent|''
dedent|''
name|'def'
name|'stub_get_project_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'usages'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'limits'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|'"get_project_quotas"'
op|','
nl|'\n'
name|'stub_get_project_quotas'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
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
dedent|''
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
name|'abs_limits'
op|'='
name|'res'
op|'.'
name|'obj'
op|'['
string|"'limits'"
op|']'
op|'['
string|"'absolute'"
op|']'
newline|'\n'
name|'for'
name|'limit'
name|'in'
name|'expected_abs_limits'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'abs_limits'
op|'['
name|'limit'
op|']'
newline|'\n'
name|'r'
op|'='
name|'limits'
op|'['
name|'quota_map'
op|'['
name|'limit'
op|']'
op|']'
op|'['
string|"'reserved'"
op|']'
name|'if'
name|'reserved'
name|'else'
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'limits'
op|'['
name|'quota_map'
op|'['
name|'limit'
op|']'
op|']'
op|'['
string|"'in_use'"
op|']'
op|'+'
name|'r'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_used_limits_basic
dedent|''
dedent|''
name|'def'
name|'test_used_limits_basic'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_used_limits'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_used_limits_with_reserved
dedent|''
name|'def'
name|'test_used_limits_with_reserved'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_used_limits'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_can_fetch_limits_for_a_given_tenant_id
dedent|''
name|'def'
name|'test_admin_can_fetch_limits_for_a_given_tenant_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
string|'"123456"'
newline|'\n'
name|'user_id'
op|'='
string|'"A1234"'
newline|'\n'
name|'tenant_id'
op|'='
string|"'abcd'"
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'target'
op|'='
op|'{'
nl|'\n'
string|'"project_id"'
op|':'
name|'tenant_id'
op|','
nl|'\n'
string|'"user_id"'
op|':'
name|'user_id'
nl|'\n'
op|'}'
newline|'\n'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'fake_req'
op|'.'
name|'GET'
op|'='
op|'{'
string|"'tenant_id'"
op|':'
name|'tenant_id'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'authorize'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'target'
op|'='
name|'target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|"'get_project_quotas'"
op|')'
newline|'\n'
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
string|"'%s'"
op|'%'
name|'tenant_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
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
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_admin_can_fetch_used_limits_for_own_project
dedent|''
name|'def'
name|'test_admin_can_fetch_used_limits_for_own_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
string|'"123456"'
newline|'\n'
name|'user_id'
op|'='
string|'"A1234"'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'fake_req'
op|'.'
name|'GET'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'extensions'
op|','
string|"'extension_authorizer'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|"'get_project_quotas'"
op|')'
newline|'\n'
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
string|"'%s'"
op|'%'
name|'project_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
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
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_admin_cannot_fetch_used_limits_for_any_other_project
dedent|''
name|'def'
name|'test_non_admin_cannot_fetch_used_limits_for_any_other_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
string|'"123456"'
newline|'\n'
name|'user_id'
op|'='
string|'"A1234"'
newline|'\n'
name|'tenant_id'
op|'='
string|'"abcd"'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'user_id'
op|'='
name|'user_id'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'target'
op|'='
op|'{'
nl|'\n'
string|'"project_id"'
op|':'
name|'tenant_id'
op|','
nl|'\n'
string|'"user_id"'
op|':'
name|'user_id'
nl|'\n'
op|'}'
newline|'\n'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'fake_req'
op|'.'
name|'GET'
op|'='
op|'{'
string|"'tenant_id'"
op|':'
name|'tenant_id'
op|'}'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'authorize'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'target'
op|'='
name|'target'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
nl|'\n'
name|'action'
op|'='
name|'self'
op|'.'
name|'used_limit_extension'
op|')'
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
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_used_limits_fetched_for_context_project_id
dedent|''
name|'def'
name|'test_used_limits_fetched_for_context_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
string|'"123456"'
newline|'\n'
name|'self'
op|'.'
name|'fake_context'
op|'.'
name|'project_id'
op|'='
name|'project_id'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|"'get_project_quotas'"
op|')'
newline|'\n'
name|'quota'
op|'.'
name|'QUOTAS'
op|'.'
name|'get_project_quotas'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|','
name|'project_id'
op|','
nl|'\n'
name|'usages'
op|'='
name|'True'
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
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_used_ram_added
dedent|''
name|'def'
name|'test_used_ram_added'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
nl|'\n'
string|'"maxTotalRAMSize"'
op|':'
number|'512'
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
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
nl|'\n'
DECL|function|stub_get_project_quotas
name|'def'
name|'stub_get_project_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'usages'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'ram'"
op|':'
op|'{'
string|"'limit'"
op|':'
number|'512'
op|','
string|"'in_use'"
op|':'
number|'256'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|'"get_project_quotas"'
op|','
nl|'\n'
name|'stub_get_project_quotas'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
name|'abs_limits'
op|'='
name|'res'
op|'.'
name|'obj'
op|'['
string|"'limits'"
op|']'
op|'['
string|"'absolute'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'totalRAMUsed'"
op|','
name|'abs_limits'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'256'
op|','
name|'abs_limits'
op|'['
string|"'totalRAMUsed'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_ram_quota
dedent|''
name|'def'
name|'test_no_ram_quota'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_req'
op|'='
name|'FakeRequest'
op|'('
name|'self'
op|'.'
name|'fake_context'
op|')'
newline|'\n'
name|'obj'
op|'='
op|'{'
nl|'\n'
string|'"limits"'
op|':'
op|'{'
nl|'\n'
string|'"rate"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"absolute"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'res'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
name|'obj'
op|')'
newline|'\n'
nl|'\n'
DECL|function|stub_get_project_quotas
name|'def'
name|'stub_get_project_quotas'
op|'('
name|'context'
op|','
name|'project_id'
op|','
name|'usages'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'ext_mgr'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-used-limits-for-admin'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ext_mgr'
op|'.'
name|'is_loaded'
op|'('
string|"'os-server-group-quotas'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'include_server_group_quotas'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'quota'
op|'.'
name|'QUOTAS'
op|','
string|'"get_project_quotas"'
op|','
nl|'\n'
name|'stub_get_project_quotas'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'fake_req'
op|','
name|'res'
op|')'
newline|'\n'
name|'abs_limits'
op|'='
name|'res'
op|'.'
name|'obj'
op|'['
string|"'limits'"
op|']'
op|'['
string|"'absolute'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'totalRAMUsed'"
op|','
name|'abs_limits'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
