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
name|'datetime'
newline|'\n'
nl|'\n'
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
name|'import'
name|'api_version_request'
name|'as'
name|'api_version'
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
name|'flavor_access'
name|'as'
name|'flavor_access_v2'
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
name|'flavors'
name|'as'
name|'flavors_api'
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
name|'flavor_access'
name|'as'
name|'flavor_access_v3'
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
DECL|function|generate_flavor
name|'def'
name|'generate_flavor'
op|'('
name|'flavorid'
op|','
name|'ispublic'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'flavorid'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'str'
op|'('
name|'flavorid'
op|')'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"u'test'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'512'
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'extra_specs'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'vcpu_weight'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'bool'
op|'('
name|'ispublic'
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|INSTANCE_TYPES
dedent|''
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'0'"
op|':'
name|'generate_flavor'
op|'('
number|'0'
op|','
name|'True'
op|')'
op|','
nl|'\n'
string|"'1'"
op|':'
name|'generate_flavor'
op|'('
number|'1'
op|','
name|'True'
op|')'
op|','
nl|'\n'
string|"'2'"
op|':'
name|'generate_flavor'
op|'('
number|'2'
op|','
name|'False'
op|')'
op|','
nl|'\n'
string|"'3'"
op|':'
name|'generate_flavor'
op|'('
number|'3'
op|','
name|'False'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ACCESS_LIST
name|'ACCESS_LIST'
op|'='
op|'['
op|'{'
string|"'flavor_id'"
op|':'
string|"'2'"
op|','
string|"'project_id'"
op|':'
string|"'proj2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'flavor_id'"
op|':'
string|"'2'"
op|','
string|"'project_id'"
op|':'
string|"'proj3'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'flavor_id'"
op|':'
string|"'3'"
op|','
string|"'project_id'"
op|':'
string|"'proj3'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_flavor_access_by_flavor_id
name|'def'
name|'fake_get_flavor_access_by_flavor_id'
op|'('
name|'context'
op|','
name|'flavorid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'res'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'access'
name|'in'
name|'ACCESS_LIST'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'access'
op|'['
string|"'flavor_id'"
op|']'
op|'=='
name|'flavorid'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'.'
name|'append'
op|'('
name|'access'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_flavor_by_flavor_id
dedent|''
name|'def'
name|'fake_get_flavor_by_flavor_id'
op|'('
name|'context'
op|','
name|'flavorid'
op|','
name|'read_deleted'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'flavorid'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_has_flavor_access
dedent|''
name|'def'
name|'_has_flavor_access'
op|'('
name|'flavorid'
op|','
name|'projectid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'access'
name|'in'
name|'ACCESS_LIST'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'access'
op|'['
string|"'flavor_id'"
op|']'
op|'=='
name|'flavorid'
name|'and'
name|'access'
op|'['
string|"'project_id'"
op|']'
op|'=='
name|'projectid'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_all_flavors_sorted_list
dedent|''
name|'def'
name|'fake_get_all_flavors_sorted_list'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
name|'False'
op|','
nl|'\n'
name|'filters'
op|'='
name|'None'
op|','
name|'sort_key'
op|'='
string|"'flavorid'"
op|','
nl|'\n'
name|'sort_dir'
op|'='
string|"'asc'"
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'marker'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'filters'
name|'is'
name|'None'
name|'or'
name|'filters'
op|'['
string|"'is_public'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'sorted'
op|'('
name|'INSTANCE_TYPES'
op|'.'
name|'values'
op|'('
op|')'
op|','
name|'key'
op|'='
name|'lambda'
name|'item'
op|':'
name|'item'
op|'['
name|'sort_key'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'res'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'filters'
op|'['
string|"'is_public'"
op|']'
name|'and'
name|'_has_flavor_access'
op|'('
name|'k'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'.'
name|'update'
op|'('
op|'{'
name|'k'
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'v'
op|'['
string|"'is_public'"
op|']'
op|'=='
name|'filters'
op|'['
string|"'is_public'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'.'
name|'update'
op|'('
op|'{'
name|'k'
op|':'
name|'v'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'res'
op|'='
name|'sorted'
op|'('
name|'res'
op|'.'
name|'values'
op|'('
op|')'
op|','
name|'key'
op|'='
name|'lambda'
name|'item'
op|':'
name|'item'
op|'['
name|'sort_key'
op|']'
op|')'
newline|'\n'
name|'return'
name|'res'
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
DECL|variable|environ
indent|'    '
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|'}'
newline|'\n'
DECL|variable|api_version_request
name|'api_version_request'
op|'='
name|'api_version'
op|'.'
name|'APIVersionRequest'
op|'('
string|'"2.1"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_db_flavor
name|'def'
name|'get_db_flavor'
op|'('
name|'self'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'flavor_id'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeResponse
dedent|''
dedent|''
name|'class'
name|'FakeResponse'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|obj
indent|'    '
name|'obj'
op|'='
op|'{'
string|"'flavor'"
op|':'
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
nl|'\n'
string|"'flavors'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|'}'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|attach
name|'def'
name|'attach'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccessTestV21
dedent|''
dedent|''
name|'class'
name|'FlavorAccessTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|api_version
indent|'    '
name|'api_version'
op|'='
string|'"2.1"'
newline|'\n'
DECL|variable|FlavorAccessController
name|'FlavorAccessController'
op|'='
name|'flavor_access_v3'
op|'.'
name|'FlavorAccessController'
newline|'\n'
DECL|variable|FlavorActionController
name|'FlavorActionController'
op|'='
name|'flavor_access_v3'
op|'.'
name|'FlavorActionController'
newline|'\n'
DECL|variable|_prefix
name|'_prefix'
op|'='
string|'"/v3"'
newline|'\n'
DECL|variable|validation_ex
name|'validation_ex'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'FlavorAccessTestV21'
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
name|'flavor_controller'
op|'='
name|'flavors_api'
op|'.'
name|'Controller'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'FakeRequest'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'self'
op|'.'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'flavor_get_by_flavor_id'"
op|','
nl|'\n'
name|'fake_get_flavor_by_flavor_id'
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
string|"'flavor_get_all'"
op|','
nl|'\n'
name|'fake_get_all_flavors_sorted_list'
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
string|"'flavor_access_get_by_flavor_id'"
op|','
nl|'\n'
name|'fake_get_flavor_access_by_flavor_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flavor_access_controller'
op|'='
name|'self'
op|'.'
name|'FlavorAccessController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'='
name|'self'
op|'.'
name|'FlavorActionController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_verify_flavor_list
dedent|''
name|'def'
name|'_verify_flavor_list'
op|'('
name|'self'
op|','
name|'result'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
comment|'# result already sorted by flavor_id'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'result'
op|')'
op|','
name|'len'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'d1'
op|','
name|'d2'
name|'in'
name|'zip'
op|'('
name|'result'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'d1'
op|'['
string|"'id'"
op|']'
op|','
name|'d2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_access_public
dedent|''
dedent|''
name|'def'
name|'test_list_flavor_access_public'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# query os-flavor-access on public flavor should return 404'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'flavor_access_controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_access_private
dedent|''
name|'def'
name|'test_list_flavor_access_private'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavor_access'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'flavor_id'"
op|':'
string|"'2'"
op|','
string|"'tenant_id'"
op|':'
string|"'proj2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'flavor_id'"
op|':'
string|"'2'"
op|','
string|"'tenant_id'"
op|':'
string|"'proj3'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_access_controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|"'2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_with_no_context
dedent|''
name|'def'
name|'test_list_with_no_context'
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
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/fake/flavors'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_authorize
name|'def'
name|'fake_authorize'
op|'('
name|'context'
op|','
name|'target'
op|'='
name|'None'
op|','
name|'action'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
name|'action'
op|'='
string|"'index'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'api_version'
op|'=='
string|'"2.1"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'flavor_access_v3'
op|','
nl|'\n'
string|"'authorize'"
op|','
nl|'\n'
name|'fake_authorize'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'flavor_access_v2'
op|','
nl|'\n'
string|"'authorize'"
op|','
nl|'\n'
name|'fake_authorize'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'flavor_access_controller'
op|'.'
name|'index'
op|','
nl|'\n'
name|'req'
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_default_proj1
dedent|''
name|'def'
name|'test_list_flavor_with_admin_default_proj1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/fake/flavors'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'project_id'
op|'='
string|"'proj1'"
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_default_proj2
dedent|''
name|'def'
name|'test_list_flavor_with_admin_default_proj2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'project_id'
op|'='
string|"'proj2'"
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_ispublic_true
dedent|''
name|'def'
name|'test_list_flavor_with_admin_ispublic_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=true'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_ispublic_false
dedent|''
name|'def'
name|'test_list_flavor_with_admin_ispublic_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'3'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=false'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_ispublic_false_proj2
dedent|''
name|'def'
name|'test_list_flavor_with_admin_ispublic_false_proj2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'3'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=false'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'.'
name|'project_id'
op|'='
string|"'proj2'"
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_admin_ispublic_none
dedent|''
name|'def'
name|'test_list_flavor_with_admin_ispublic_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'3'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=none'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_no_admin_default
dedent|''
name|'def'
name|'test_list_flavor_with_no_admin_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_no_admin_ispublic_true
dedent|''
name|'def'
name|'test_list_flavor_with_no_admin_ispublic_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=true'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_no_admin_ispublic_false
dedent|''
name|'def'
name|'test_list_flavor_with_no_admin_ispublic_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=false'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_flavor_with_no_admin_ispublic_none
dedent|''
name|'def'
name|'test_list_flavor_with_no_admin_ispublic_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'flavors'"
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors?is_public=none'"
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'url'
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'flavor_controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_flavor_list'
op|'('
name|'result'
op|'['
string|"'flavors'"
op|']'
op|','
name|'expected'
op|'['
string|"'flavors'"
op|']'
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
name|'resp'
op|'='
name|'FakeResponse'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'resp'
op|','
string|"'0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|','
string|"'os-flavor-access:is_public'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'resp'
op|','
string|"'2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|','
string|"'os-flavor-access:is_public'"
op|':'
name|'False'
op|'}'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
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
name|'resp'
op|'='
name|'FakeResponse'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'resp'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|','
string|"'os-flavor-access:is_public'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'2'"
op|','
string|"'os-flavor-access:is_public'"
op|':'
name|'False'
op|'}'
op|']'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'flavors'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'FakeResponse'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
op|'{'
op|'}'
op|','
name|'resp'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'id'"
op|':'
string|"'0'"
op|','
string|"'os-flavor-access:is_public'"
op|':'
name|'True'
op|'}'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'flavor'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_add_access
dedent|''
name|'def'
name|'_get_add_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'api_version'
op|'=='
string|'"2.1"'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'_add_tenant_access'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'_addTenantAccess'
newline|'\n'
nl|'\n'
DECL|member|_get_remove_access
dedent|''
dedent|''
name|'def'
name|'_get_remove_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'api_version'
op|'=='
string|'"2.1"'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'_remove_tenant_access'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'flavor_action_controller'
op|'.'
name|'_removeTenantAccess'
newline|'\n'
nl|'\n'
DECL|member|test_add_tenant_access
dedent|''
dedent|''
name|'def'
name|'test_add_tenant_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_add_flavor_access
indent|'        '
name|'def'
name|'stub_add_flavor_access'
op|'('
name|'context'
op|','
name|'flavorid'
op|','
name|'projectid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'3'"
op|','
name|'flavorid'
op|','
string|'"flavorid"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"proj2"'
op|','
name|'projectid'
op|','
string|'"projectid"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'flavor_access_add'"
op|','
nl|'\n'
name|'stub_add_flavor_access'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'flavor_access'"
op|':'
nl|'\n'
op|'['
op|'{'
string|"'flavor_id'"
op|':'
string|"'3'"
op|','
string|"'tenant_id'"
op|':'
string|"'proj3'"
op|'}'
op|']'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'addTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/2/action'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'add_access'
op|'='
name|'self'
op|'.'
name|'_get_add_access'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'add_access'
op|'('
name|'req'
op|','
string|"'3'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_tenant_access_with_no_admin_user
dedent|''
name|'def'
name|'test_add_tenant_access_with_no_admin_user'
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
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/2/action'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'addTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'add_access'
op|'='
name|'self'
op|'.'
name|'_get_add_access'
op|'('
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
nl|'\n'
name|'add_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_tenant_access_with_no_tenant
dedent|''
name|'def'
name|'test_add_tenant_access_with_no_tenant'
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
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/2/action'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'addTenantAccess'"
op|':'
op|'{'
string|"'foo'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'add_access'
op|'='
name|'self'
op|'.'
name|'_get_add_access'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_ex'
op|','
nl|'\n'
name|'add_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'addTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_ex'
op|','
nl|'\n'
name|'add_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_tenant_access_with_already_added_access
dedent|''
name|'def'
name|'test_add_tenant_access_with_already_added_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_add_flavor_access
indent|'        '
name|'def'
name|'stub_add_flavor_access'
op|'('
name|'context'
op|','
name|'flavorid'
op|','
name|'projectid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FlavorAccessExists'
op|'('
name|'flavor_id'
op|'='
name|'flavorid'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'projectid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'flavor_access_add'"
op|','
nl|'\n'
name|'stub_add_flavor_access'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'addTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'add_access'
op|'='
name|'self'
op|'.'
name|'_get_add_access'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'add_access'
op|','
name|'self'
op|'.'
name|'req'
op|','
string|"'3'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_tenant_access_with_bad_access
dedent|''
name|'def'
name|'test_remove_tenant_access_with_bad_access'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_remove_flavor_access
indent|'        '
name|'def'
name|'stub_remove_flavor_access'
op|'('
name|'context'
op|','
name|'flavorid'
op|','
name|'projectid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FlavorAccessNotFound'
op|'('
name|'flavor_id'
op|'='
name|'flavorid'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'projectid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'flavor_access_remove'"
op|','
nl|'\n'
name|'stub_remove_flavor_access'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'removeTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'remove_access'
op|'='
name|'self'
op|'.'
name|'_get_remove_access'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'remove_access'
op|','
name|'self'
op|'.'
name|'req'
op|','
string|"'3'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_tenant_access_with_no_tenant
dedent|''
name|'def'
name|'test_delete_tenant_access_with_no_tenant'
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
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/2/action'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'remove_access'
op|'='
name|'self'
op|'.'
name|'_get_remove_access'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'removeTenantAccess'"
op|':'
op|'{'
string|"'foo'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_ex'
op|','
nl|'\n'
name|'remove_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'removeTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"''"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_ex'
op|','
nl|'\n'
name|'remove_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_tenant_access_with_no_admin_user
dedent|''
name|'def'
name|'test_remove_tenant_access_with_no_admin_user'
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
name|'self'
op|'.'
name|'_prefix'
op|'+'
string|"'/flavors/2/action'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'False'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'removeTenantAccess'"
op|':'
op|'{'
string|"'tenant'"
op|':'
string|"'proj2'"
op|'}'
op|'}'
newline|'\n'
name|'remove_access'
op|'='
name|'self'
op|'.'
name|'_get_remove_access'
op|'('
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
nl|'\n'
name|'remove_access'
op|','
name|'req'
op|','
string|"'2'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccessTestV20
dedent|''
dedent|''
name|'class'
name|'FlavorAccessTestV20'
op|'('
name|'FlavorAccessTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|api_version
indent|'    '
name|'api_version'
op|'='
string|'"2.0"'
newline|'\n'
DECL|variable|FlavorAccessController
name|'FlavorAccessController'
op|'='
name|'flavor_access_v2'
op|'.'
name|'FlavorAccessController'
newline|'\n'
DECL|variable|FlavorActionController
name|'FlavorActionController'
op|'='
name|'flavor_access_v2'
op|'.'
name|'FlavorActionController'
newline|'\n'
DECL|variable|_prefix
name|'_prefix'
op|'='
string|'"/v2/fake"'
newline|'\n'
DECL|variable|validation_ex
name|'validation_ex'
op|'='
name|'exc'
op|'.'
name|'HTTPBadRequest'
newline|'\n'
dedent|''
endmarker|''
end_unit
