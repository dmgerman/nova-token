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
name|'copy'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
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
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
DECL|variable|_TS_NOW
name|'_TS_NOW'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
name|'with_timezone'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'# o.vo.fields.DateTimeField converts to tz-aware and'
nl|'\n'
comment|'# in process we lose microsecond resolution.'
nl|'\n'
DECL|variable|_TS_NOW
name|'_TS_NOW'
op|'='
name|'_TS_NOW'
op|'.'
name|'replace'
op|'('
name|'microsecond'
op|'='
number|'0'
op|')'
newline|'\n'
DECL|variable|_DB_UUID
name|'_DB_UUID'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
newline|'\n'
DECL|variable|_INST_GROUP_DB
name|'_INST_GROUP_DB'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'_DB_UUID'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake_user'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake_name'"
op|','
nl|'\n'
string|"'policies'"
op|':'
op|'['
string|"'policy1'"
op|','
string|"'policy2'"
op|']'
op|','
nl|'\n'
string|"'members'"
op|':'
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceGroupObject
name|'class'
name|'_TestInstanceGroupObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|','
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_get_by_uuid
name|'def'
name|'test_get_by_uuid'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'_DB_UUID'
op|')'
newline|'\n'
name|'mock_db_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'members'"
op|']'
op|','
name|'obj'
op|'.'
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'policies'"
op|']'
op|','
name|'obj'
op|'.'
name|'policies'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_DB_UUID'
op|','
name|'obj'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'project_id'"
op|']'
op|','
name|'obj'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'user_id'"
op|']'
op|','
name|'obj'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'name'"
op|']'
op|','
name|'obj'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get_by_instance'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_get_by_instance_uuid
name|'def'
name|'test_get_by_instance_uuid'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_instance_uuid'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
name|'mock_db_get'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|')'
newline|'\n'
DECL|member|test_refresh
name|'def'
name|'test_refresh'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'changed_group'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
name|'changed_group'
op|'['
string|"'name'"
op|']'
op|'='
string|"'new_name'"
newline|'\n'
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'_INST_GROUP_DB'
op|','
name|'changed_group'
op|']'
newline|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'_DB_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'_INST_GROUP_DB'
op|'['
string|"'name'"
op|']'
op|','
name|'obj'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'refresh'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'new_name'"
op|','
name|'obj'
op|'.'
name|'name'
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
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_server_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|')'
newline|'\n'
DECL|member|test_save
name|'def'
name|'test_save'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|','
name|'mock_db_update'
op|','
name|'mock_notify'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'changed_group'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
name|'changed_group'
op|'['
string|"'name'"
op|']'
op|'='
string|"'new_name'"
newline|'\n'
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'_INST_GROUP_DB'
op|','
name|'changed_group'
op|']'
newline|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'_DB_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'name'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
string|"'new_name'"
newline|'\n'
name|'obj'
op|'.'
name|'policies'
op|'='
op|'['
string|"'policy1'"
op|']'
comment|'# Remove policy 2'
newline|'\n'
name|'obj'
op|'.'
name|'members'
op|'='
op|'['
string|"'instance_id1'"
op|']'
comment|'# Remove member 2'
newline|'\n'
name|'obj'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'mock_db_update'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'new_name'"
op|','
nl|'\n'
string|"'members'"
op|':'
op|'['
string|"'instance_id1'"
op|']'
op|','
nl|'\n'
string|"'policies'"
op|':'
op|'['
string|"'policy1'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'mock_notify'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|'"update"'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'new_name'"
op|','
nl|'\n'
string|"'members'"
op|':'
op|'['
string|"'instance_id1'"
op|']'
op|','
nl|'\n'
string|"'policies'"
op|':'
op|'['
string|"'policy1'"
op|']'
op|','
nl|'\n'
string|"'server_group_id'"
op|':'
name|'_DB_UUID'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_server_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|')'
newline|'\n'
DECL|member|test_save_without_hosts
name|'def'
name|'test_save_without_hosts'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|','
name|'mock_db_update'
op|','
nl|'\n'
name|'mock_notify'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'_INST_GROUP_DB'
op|','
name|'_INST_GROUP_DB'
op|']'
newline|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'hosts'
op|'='
op|'['
string|"'fake-host1'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceGroupSaveException'
op|','
nl|'\n'
name|'obj'
op|'.'
name|'save'
op|')'
newline|'\n'
comment|'# make sure that we can save by removing hosts from what is updated'
nl|'\n'
name|'obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'hosts'"
op|']'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
comment|'# since hosts was the only update, there is no actual call'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_db_update'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_notify'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_server_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_create'"
op|','
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'mock_db_create'
op|','
name|'mock_notify'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'uuid'
op|'='
name|'_DB_UUID'
newline|'\n'
name|'obj'
op|'.'
name|'name'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'obj'
op|'.'
name|'user_id'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'user_id'"
op|']'
newline|'\n'
name|'obj'
op|'.'
name|'project_id'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'obj'
op|'.'
name|'members'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'members'"
op|']'
newline|'\n'
name|'obj'
op|'.'
name|'policies'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'policies'"
op|']'
newline|'\n'
name|'obj'
op|'.'
name|'updated_at'
op|'='
name|'_TS_NOW'
newline|'\n'
name|'obj'
op|'.'
name|'created_at'
op|'='
name|'_TS_NOW'
newline|'\n'
name|'obj'
op|'.'
name|'deleted_at'
op|'='
name|'None'
newline|'\n'
name|'obj'
op|'.'
name|'deleted'
op|'='
name|'False'
newline|'\n'
name|'obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'mock_db_create'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'_DB_UUID'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
name|'members'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'members'"
op|']'
op|','
nl|'\n'
name|'policies'
op|'='
name|'_INST_GROUP_DB'
op|'['
string|"'policies'"
op|']'
op|')'
newline|'\n'
name|'mock_notify'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|'"create"'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'_DB_UUID'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'_TS_NOW'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'members'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'members'"
op|']'
op|','
nl|'\n'
string|"'policies'"
op|':'
name|'_INST_GROUP_DB'
op|'['
string|"'policies'"
op|']'
op|','
nl|'\n'
string|"'server_group_id'"
op|':'
name|'_DB_UUID'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'obj'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_server_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_delete'"
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|','
name|'mock_db_delete'
op|','
name|'mock_notify'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'uuid'
op|'='
name|'_DB_UUID'
newline|'\n'
name|'obj'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
name|'mock_db_delete'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'mock_notify'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|'"delete"'
op|','
nl|'\n'
op|'{'
string|"'server_group_id'"
op|':'
name|'_DB_UUID'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.utils.notify_about_server_group_update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_members_add'"
op|')'
newline|'\n'
DECL|member|test_add_members
name|'def'
name|'test_add_members'
op|'('
name|'self'
op|','
name|'mock_members_add_db'
op|','
name|'mock_notify'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_members_add_db'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'members'
op|']'
newline|'\n'
name|'members'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'add_members'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'_DB_UUID'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'members'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'members'
op|']'
op|','
name|'members'
op|')'
newline|'\n'
name|'mock_members_add_db'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'_DB_UUID'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'members'
op|')'
newline|'\n'
name|'mock_notify'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|'"addmember"'
op|','
nl|'\n'
op|'{'
string|"'instance_uuids'"
op|':'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'members'
op|','
nl|'\n'
string|"'server_group_id'"
op|':'
name|'_DB_UUID'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_filters'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|','
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_count_members_by_user
name|'def'
name|'test_count_members_by_user'
op|'('
name|'self'
op|','
name|'mock_get_db'
op|','
name|'mock_il_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_il_get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'ANY'
op|']'
newline|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'expected_filters'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake_user'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'obj'
op|'.'
name|'count_members_by_user'
op|'('
string|"'fake_user'"
op|')'
op|')'
newline|'\n'
name|'mock_il_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'filters'
op|'='
name|'expected_filters'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_filters'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|','
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_get_hosts
name|'def'
name|'test_get_hosts'
op|'('
name|'self'
op|','
name|'mock_get_db'
op|','
name|'mock_il_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_il_get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'host'
op|'='
string|"'host2'"
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'host'
op|'='
name|'None'
op|')'
op|']'
newline|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'obj'
op|'.'
name|'get_hosts'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
op|','
name|'obj'
op|'.'
name|'members'
op|')'
newline|'\n'
name|'expected_filters'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
op|'['
string|"'instance_id1'"
op|','
string|"'instance_id2'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
name|'mock_il_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'filters'
op|'='
name|'expected_filters'
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
string|"'host1'"
op|','
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'host2'"
op|','
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test manual exclusion'
nl|'\n'
name|'mock_il_get'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'obj'
op|'.'
name|'get_hosts'
op|'('
name|'exclude'
op|'='
op|'['
string|"'instance_id1'"
op|']'
op|')'
newline|'\n'
name|'expected_filters'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
name|'set'
op|'('
op|'['
string|"'instance_id2'"
op|']'
op|')'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
name|'mock_il_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'filters'
op|'='
name|'expected_filters'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get'"
op|','
name|'return_value'
op|'='
name|'_INST_GROUP_DB'
op|')'
newline|'\n'
DECL|member|test_obj_make_compatible
name|'def'
name|'test_obj_make_compatible'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_uuid'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'obj_primitive'
op|'='
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'metadetails'"
op|','
name|'obj_primitive'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'obj_make_compatible'
op|'('
name|'obj_primitive'
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
name|'obj_primitive'
op|'['
string|"'metadetails'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'InstanceList'
op|','
string|"'get_by_filters'"
op|')'
newline|'\n'
DECL|member|test_load_hosts
name|'def'
name|'test_load_hosts'
op|'('
name|'self'
op|','
name|'mock_get_by_filt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_by_filt'
op|'.'
name|'return_value'
op|'='
op|'['
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'host'
op|'='
string|"'host1'"
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'host'
op|'='
string|"'host2'"
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'members'
op|'='
op|'['
string|"'uuid1'"
op|']'
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
name|'obj'
op|'.'
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'host1'"
op|','
name|'obj'
op|'.'
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'host2'"
op|','
name|'obj'
op|'.'
name|'hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'hosts'"
op|','
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_load_anything_else_but_hosts
dedent|''
name|'def'
name|'test_load_anything_else_but_hosts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
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
name|'getattr'
op|','
name|'obj'
op|','
string|"'members'"
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
name|'_TestInstanceGroupObject'
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
name|'_TestInstanceGroupObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_mock_db_list_get
dedent|''
name|'def'
name|'_mock_db_list_get'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'_INST_GROUP_DB'
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
name|'result'
op|'.'
name|'append'
op|'('
name|'values'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestInstanceGroupListObject
dedent|''
name|'class'
name|'_TestInstanceGroupListObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get_all'"
op|')'
newline|'\n'
DECL|member|test_list_all
name|'def'
name|'test_list_all'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
name|'_mock_db_list_get'
newline|'\n'
name|'inst_list'
op|'='
name|'objects'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_all'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'inst_list'
op|'.'
name|'objects'
op|')'
op|')'
newline|'\n'
name|'mock_db_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get_all_by_project_id'"
op|')'
newline|'\n'
DECL|member|test_list_by_project_id
name|'def'
name|'test_list_by_project_id'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
name|'_mock_db_list_get'
newline|'\n'
name|'objects'
op|'.'
name|'InstanceGroupList'
op|'.'
name|'get_by_project_id'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'mock_db_get'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_group_get_all_by_project_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_name
name|'def'
name|'test_get_by_name'
op|'('
name|'self'
op|','
name|'mock_db_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_db_get'
op|'.'
name|'side_effect'
op|'='
name|'_mock_db_list_get'
newline|'\n'
comment|"# Need the project_id value set, otherwise we'd use mock.sentinel"
nl|'\n'
name|'mock_ctx'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_ctx'
op|'.'
name|'project_id'
op|'='
string|"'fake_project'"
newline|'\n'
name|'ig'
op|'='
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_name'
op|'('
name|'mock_ctx'
op|','
string|"'f1'"
op|')'
newline|'\n'
name|'mock_db_get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock_ctx'
op|','
string|"'fake_project'"
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceGroupNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_name'
op|','
nl|'\n'
name|'mock_ctx'
op|','
string|"'unknown'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceGroup.get_by_uuid'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceGroup.get_by_name'"
op|')'
newline|'\n'
DECL|member|test_get_by_hint
name|'def'
name|'test_get_by_hint'
op|'('
name|'self'
op|','
name|'mock_name'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_hint'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'mock_uuid'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
name|'_DB_UUID'
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'InstanceGroup'
op|'.'
name|'get_by_hint'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|"'name'"
op|')'
newline|'\n'
name|'mock_name'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
string|"'name'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestInstanceGroupListObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestInstanceGroupListObject
name|'_TestInstanceGroupListObject'
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
name|'TestRemoteInstanceGroupListObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteInstanceGroupListObject
name|'_TestInstanceGroupListObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
