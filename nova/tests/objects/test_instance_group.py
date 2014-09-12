begin_unit
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
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
name|'instance_group'
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
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'utils'
name|'as'
name|'tests_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceGroupObjects
name|'class'
name|'_TestInstanceGroupObjects'
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
name|'_TestInstanceGroupObjects'
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
name|'user_id'
op|'='
string|"'fake_user'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake_project'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_default_values
dedent|''
name|'def'
name|'_get_default_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'name'"
op|':'
string|"'fake_name'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_create_instance_group
dedent|''
name|'def'
name|'_create_instance_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|','
name|'policies'
op|'='
name|'None'
op|','
nl|'\n'
name|'members'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'db'
op|'.'
name|'instance_group_create'
op|'('
name|'context'
op|','
name|'values'
op|','
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_uuid
dedent|''
name|'def'
name|'test_get_by_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'members'
op|'='
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|','
nl|'\n'
name|'policies'
op|'='
name|'policies'
op|','
nl|'\n'
name|'members'
op|'='
name|'members'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'members'
op|','
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'policies'
op|','
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_refresh
dedent|''
name|'def'
name|'test_refresh'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'new_name'"
op|','
string|"'user_id'"
op|':'
string|"'new_user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'new_project'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_group_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'new_name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|'['
op|']'
op|')'
op|','
name|'obj_result'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_simple
dedent|''
name|'def'
name|'test_save_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj_result'
op|'.'
name|'name'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'obj_result'
op|'.'
name|'name'
op|'='
string|"'new_name'"
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'name'"
op|']'
op|','
string|"'new_name'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_policies
dedent|''
name|'def'
name|'test_save_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'obj_result'
op|'.'
name|'policies'
op|'='
name|'policies'
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'policies'"
op|']'
op|','
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_members
dedent|''
name|'def'
name|'test_save_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'db_result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'obj_result'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'db_result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'members'
op|'='
op|'['
string|"'instance1'"
op|','
string|"'instance2'"
op|']'
newline|'\n'
name|'obj_result'
op|'.'
name|'members'
op|'='
name|'members'
newline|'\n'
name|'obj_result'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'db_result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'['
string|"'members'"
op|']'
op|','
name|'members'
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
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'uuid'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'group1'
op|'.'
name|'name'
op|'='
string|"'fake-name'"
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'uuid'
op|','
name|'group2'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'name'
op|','
name|'group2'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'result'
op|'='
name|'db'
op|'.'
name|'instance_group_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'result'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'uuid'
op|','
name|'result'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'name'
op|','
name|'result'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_policies
dedent|''
name|'def'
name|'test_create_with_policies'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'policies'
op|','
name|'group2'
op|'.'
name|'policies'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_members
dedent|''
name|'def'
name|'test_create_with_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group1'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group1'
op|'.'
name|'members'
op|'='
op|'['
string|"'instance1'"
op|','
string|"'instance2'"
op|']'
newline|'\n'
name|'group1'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group2'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group1'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'id'
op|','
name|'group2'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'group1'
op|'.'
name|'members'
op|','
name|'group2'
op|'.'
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_recreate_fails
dedent|''
name|'def'
name|'test_recreate_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'group'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_destroy
dedent|''
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'id'
op|'='
name|'result'
op|'.'
name|'id'
newline|'\n'
name|'group'
op|'.'
name|'uuid'
op|'='
name|'result'
op|'.'
name|'uuid'
newline|'\n'
name|'group'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'instance_group_get'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'result'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_populate_instances
dedent|''
name|'def'
name|'_populate_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
op|'['
op|'('
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
string|"'f1'"
op|','
string|"'p1'"
op|')'
op|','
nl|'\n'
op|'('
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
string|"'f2'"
op|','
string|"'p1'"
op|')'
op|','
nl|'\n'
op|'('
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
string|"'f3'"
op|','
string|"'p2'"
op|')'
op|','
nl|'\n'
op|'('
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
string|"'f4'"
op|','
string|"'p2'"
op|')'
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'values'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'instance'
op|'['
number|'0'
op|']'
newline|'\n'
name|'values'
op|'['
string|"'name'"
op|']'
op|'='
name|'instance'
op|'['
number|'1'
op|']'
newline|'\n'
name|'values'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'instance'
op|'['
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instances'
newline|'\n'
nl|'\n'
DECL|member|test_list_all
dedent|''
name|'def'
name|'test_list_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'inst_list'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
name|'len'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
number|'4'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'groups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'groups'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_by_project_id
dedent|''
dedent|''
name|'def'
name|'test_list_by_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'project_ids'
op|'='
op|'['
string|"'p1'"
op|','
string|"'p2'"
op|']'
newline|'\n'
name|'for'
name|'id'
name|'in'
name|'project_ids'
op|':'
newline|'\n'
indent|'            '
name|'il'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_by_project_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'groups'
op|'='
name|'db'
op|'.'
name|'instance_group_get_all_by_project_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
name|'len'
op|'('
name|'il'
op|'.'
name|'objects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'groups'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'groups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'uuid'
op|','
name|'groups'
op|'['
name|'i'
op|']'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'name'
op|','
name|'groups'
op|'['
name|'i'
op|']'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'il'
op|'.'
name|'objects'
op|'['
name|'i'
op|']'
op|'.'
name|'project_id'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_name
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_get_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'p1'"
op|')'
newline|'\n'
name|'ig'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_name'
op|'('
name|'ctxt'
op|','
string|"'f1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'f1'"
op|','
name|'ig'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_hint
dedent|''
name|'def'
name|'test_get_by_hint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances'
op|'='
name|'self'
op|'.'
name|'_populate_instances'
op|'('
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
name|'instance'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'ig'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_hint'
op|'('
name|'ctxt'
op|','
name|'instance'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
number|'1'
op|']'
op|','
name|'ig'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'ig'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_hint'
op|'('
name|'ctxt'
op|','
name|'instance'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance'
op|'['
number|'0'
op|']'
op|','
name|'ig'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_members
dedent|''
dedent|''
name|'def'
name|'test_add_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ids'
op|'='
op|'['
string|"'fakeid1'"
op|','
string|"'fakeid2'"
op|']'
newline|'\n'
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'members'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'add_members'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group'
op|'.'
name|'uuid'
op|','
name|'instance_ids'
op|')'
newline|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'instance'
op|','
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'instance'
op|','
name|'group'
op|'.'
name|'members'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hosts
dedent|''
dedent|''
name|'def'
name|'test_get_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance1'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance1'
op|'.'
name|'host'
op|'='
string|"'hostA'"
newline|'\n'
name|'instance1'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'instance2'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance2'
op|'.'
name|'host'
op|'='
string|"'hostB'"
newline|'\n'
name|'instance2'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'instance3'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance3'
op|'.'
name|'host'
op|'='
string|"'hostB'"
newline|'\n'
name|'instance3'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_ids'
op|'='
op|'['
name|'instance1'
op|'.'
name|'uuid'
op|','
name|'instance2'
op|'.'
name|'uuid'
op|','
name|'instance3'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'add_members'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'instance_ids'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'group'
op|'.'
name|'get_hosts'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'hostA'"
op|','
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'hostB'"
op|','
name|'hosts'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'group'
op|'.'
name|'get_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'exclude'
op|'='
op|'['
name|'instance1'
op|'.'
name|'uuid'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'hostB'"
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_hosts_with_some_none
dedent|''
name|'def'
name|'test_get_hosts_with_some_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance1'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance1'
op|'.'
name|'host'
op|'='
name|'None'
newline|'\n'
name|'instance1'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'instance2'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance2'
op|'.'
name|'host'
op|'='
string|"'hostB'"
newline|'\n'
name|'instance2'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_ids'
op|'='
op|'['
name|'instance1'
op|'.'
name|'uuid'
op|','
name|'instance2'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'add_members'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'instance_ids'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'group'
op|'.'
name|'get_hosts'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'hostB'"
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_obj_make_compatible
dedent|''
name|'def'
name|'test_obj_make_compatible'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'('
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'name'
op|'='
string|"'fake-name'"
op|')'
newline|'\n'
name|'group'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'group_primitive'
op|'='
name|'group'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'obj_make_compatible'
op|'('
name|'group_primitive'
op|','
string|"'1.6'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'group_primitive'
op|'['
string|"'metadetails'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_count_members_by_user
dedent|''
name|'def'
name|'test_count_members_by_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance1'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance1'
op|'.'
name|'user_id'
op|'='
string|"'user1'"
newline|'\n'
name|'instance1'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'instance2'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance2'
op|'.'
name|'user_id'
op|'='
string|"'user2'"
newline|'\n'
name|'instance2'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'instance3'
op|'='
name|'tests_utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
op|','
name|'obj'
op|'='
name|'True'
op|')'
newline|'\n'
name|'instance3'
op|'.'
name|'user_id'
op|'='
string|"'user2'"
newline|'\n'
name|'instance3'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'instance_ids'
op|'='
op|'['
name|'instance1'
op|'.'
name|'uuid'
op|','
name|'instance2'
op|'.'
name|'uuid'
op|','
name|'instance3'
op|'.'
name|'uuid'
op|']'
newline|'\n'
name|'values'
op|'='
name|'self'
op|'.'
name|'_get_default_values'
op|'('
op|')'
newline|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'_create_instance_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'add_members'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'group'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'instance_ids'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'instance_group'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'group'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'count_user1'
op|'='
name|'group'
op|'.'
name|'count_members_by_user'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'user1'"
op|')'
newline|'\n'
name|'count_user2'
op|'='
name|'group'
op|'.'
name|'count_members_by_user'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'user2'"
op|')'
newline|'\n'
name|'count_user3'
op|'='
name|'group'
op|'.'
name|'count_members_by_user'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'user3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'count_user1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'count_user2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'count_user3'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceGroupObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceGroupObject
name|'_TestInstanceGroupObjects'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteInstanceGroupObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceGroupObject
name|'_TestInstanceGroupObjects'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
