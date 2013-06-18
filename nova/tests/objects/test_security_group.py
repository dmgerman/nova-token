begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
op|'.'
name|'objects'
name|'import'
name|'instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'security_group'
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
nl|'\n'
nl|'\n'
DECL|variable|fake_secgroup
name|'fake_secgroup'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake-name'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'fake-desc'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake-user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake-project'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestSecurityGroupObject
name|'class'
name|'_TestSecurityGroupObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_fix_deleted
indent|'    '
name|'def'
name|'_fix_deleted'
op|'('
name|'self'
op|','
name|'db_secgroup'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(danms): Account for the difference in 'deleted'"
nl|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'db_secgroup'
op|'.'
name|'items'
op|'('
op|')'
op|','
name|'deleted'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get
dedent|''
name|'def'
name|'test_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_secgroup'
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_fix_deleted'
op|'('
name|'fake_secgroup'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'secgroup'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secgroup'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_name
dedent|''
name|'def'
name|'test_get_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get_by_name'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
name|'ctxt'
op|','
string|"'fake-project'"
op|','
nl|'\n'
string|"'fake-name'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_secgroup'
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'.'
name|'get_by_name'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'fake-project'"
op|','
nl|'\n'
string|"'fake-name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_fix_deleted'
op|'('
name|'fake_secgroup'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'secgroup'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secgroup'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_in_use
dedent|''
name|'def'
name|'test_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_in_use'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_in_use'
op|'('
name|'ctxt'
op|','
number|'123'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'id'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'secgroup'
op|'.'
name|'in_use'
op|'('
name|'ctxt'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save
dedent|''
name|'def'
name|'test_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_update'"
op|')'
newline|'\n'
name|'updated_secgroup'
op|'='
name|'dict'
op|'('
name|'fake_secgroup'
op|','
name|'project_id'
op|'='
string|"'changed'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_update'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
nl|'\n'
op|'{'
string|"'description'"
op|':'
string|"'foobar'"
op|'}'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'updated_secgroup'
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
op|','
name|'fake_secgroup'
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'description'
op|'='
string|"'foobar'"
newline|'\n'
name|'secgroup'
op|'.'
name|'save'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_fix_deleted'
op|'('
name|'updated_secgroup'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'secgroup'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secgroup'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_no_changes
dedent|''
name|'def'
name|'test_save_no_changes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_update'"
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
op|','
name|'fake_secgroup'
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'save'
op|'('
name|'ctxt'
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
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'updated_secgroup'
op|'='
name|'dict'
op|'('
name|'fake_secgroup'
op|','
name|'description'
op|'='
string|"'changed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get'
op|'('
name|'ctxt'
op|','
number|'1'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'updated_secgroup'
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
name|'secgroup'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'.'
name|'_from_db_object'
op|'('
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|'('
op|')'
op|','
name|'fake_secgroup'
op|')'
newline|'\n'
name|'secgroup'
op|'.'
name|'refresh'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_fix_deleted'
op|'('
name|'updated_secgroup'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'secgroup'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'secgroup'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestSecurityGroupObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupObject
name|'_TestSecurityGroupObject'
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
name|'TestSecurityGroupObjectRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupObjectRemote
name|'_TestSecurityGroupObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_secgroups
dedent|''
name|'fake_secgroups'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'fake_secgroup'
op|','
name|'id'
op|'='
number|'1'
op|','
name|'name'
op|'='
string|"'secgroup1'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'fake_secgroup'
op|','
name|'id'
op|'='
number|'2'
op|','
name|'name'
op|'='
string|"'secgroup2'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestSecurityGroupListObject
name|'class'
name|'_TestSecurityGroupListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_all
indent|'    '
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get_all'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get_all'
op|'('
name|'ctxt'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'fake_secgroups'
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
name|'secgroup_list'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroupList'
op|'.'
name|'get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_secgroups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_secgroups'
op|'['
name|'i'
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'secgroup_list'
op|'['
name|'i'
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
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|'.'
name|'_context'
op|','
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_project
dedent|''
dedent|''
name|'def'
name|'test_get_by_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get_by_project'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get_by_project'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'fake-project'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_secgroups'
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
name|'secgroup_list'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroupList'
op|'.'
name|'get_by_project'
op|'('
nl|'\n'
name|'ctxt'
op|','
string|"'fake-project'"
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_secgroups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_secgroups'
op|'['
name|'i'
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_instance
dedent|''
dedent|''
name|'def'
name|'test_get_by_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-inst-uuid'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'security_group_get_by_instance'"
op|')'
newline|'\n'
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
string|"'fake-inst-uuid'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'fake_secgroups'
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
name|'secgroup_list'
op|'='
name|'security_group'
op|'.'
name|'SecurityGroupList'
op|'.'
name|'get_by_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'inst'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'fake_secgroups'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'security_group'
op|'.'
name|'SecurityGroup'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_secgroups'
op|'['
name|'i'
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'secgroup_list'
op|'['
name|'i'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestSecurityGroupListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupListObject
name|'_TestSecurityGroupListObject'
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
name|'TestSecurityGroupListObjectRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestSecurityGroupListObjectRemote
name|'_TestSecurityGroupListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
