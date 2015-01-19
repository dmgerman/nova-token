begin_unit
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'tag'
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
DECL|variable|RESOURCE_ID
name|'RESOURCE_ID'
op|'='
string|"'123'"
newline|'\n'
DECL|variable|TAG_NAME1
name|'TAG_NAME1'
op|'='
string|"'fake-tag1'"
newline|'\n'
DECL|variable|TAG_NAME2
name|'TAG_NAME2'
op|'='
string|"'fake-tag2'"
newline|'\n'
nl|'\n'
DECL|variable|fake_tag1
name|'fake_tag1'
op|'='
op|'{'
nl|'\n'
string|"'resource_id'"
op|':'
name|'RESOURCE_ID'
op|','
nl|'\n'
string|"'tag'"
op|':'
name|'TAG_NAME1'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|fake_tag2
name|'fake_tag2'
op|'='
op|'{'
nl|'\n'
string|"'resource_id'"
op|':'
name|'RESOURCE_ID'
op|','
nl|'\n'
string|"'tag'"
op|':'
name|'TAG_NAME1'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|fake_tag_list
name|'fake_tag_list'
op|'='
op|'['
name|'fake_tag1'
op|','
name|'fake_tag2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_tag
name|'def'
name|'_get_tag'
op|'('
name|'resource_id'
op|','
name|'tag_name'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'t'
op|'='
name|'tag'
op|'.'
name|'Tag'
op|'('
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'t'
op|'.'
name|'resource_id'
op|'='
name|'resource_id'
newline|'\n'
name|'t'
op|'.'
name|'tag'
op|'='
name|'tag_name'
newline|'\n'
name|'return'
name|'t'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestTagObject
dedent|''
name|'class'
name|'_TestTagObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_add'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'tag_add'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag_add'
op|'.'
name|'return_value'
op|'='
name|'fake_tag1'
newline|'\n'
name|'tag_obj'
op|'='
name|'_get_tag'
op|'('
name|'RESOURCE_ID'
op|','
name|'TAG_NAME1'
op|','
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'tag_obj'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'tag_add'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|','
name|'TAG_NAME1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compare_obj'
op|'('
name|'tag_obj'
op|','
name|'fake_tag1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_delete'"
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|','
name|'tag_delete'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag'
op|'.'
name|'Tag'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|','
name|'TAG_NAME1'
op|')'
newline|'\n'
name|'tag_delete'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'RESOURCE_ID'
op|','
name|'TAG_NAME1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestMigrationObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestMigrationObject
name|'_TestTagObject'
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
name|'TestRemoteMigrationObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteMigrationObject
name|'_TestTagObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestTagList
dedent|''
name|'class'
name|'_TestTagList'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_compare_tag_list
indent|'    '
name|'def'
name|'_compare_tag_list'
op|'('
name|'self'
op|','
name|'tag_list'
op|','
name|'tag_list_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'tag_list'
op|')'
op|','
name|'len'
op|'('
name|'tag_list_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'obj'
op|','
name|'fake'
name|'in'
name|'zip'
op|'('
name|'tag_list_obj'
op|','
name|'tag_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'obj'
op|','
name|'tag'
op|'.'
name|'Tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'tag'
op|','
name|'fake'
op|'['
string|"'tag'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'resource_id'
op|','
name|'fake'
op|'['
string|"'resource_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_get_by_resource_id
name|'def'
name|'test_get_by_resource_id'
op|'('
name|'self'
op|','
name|'get_by_inst'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_by_inst'
op|'.'
name|'return_value'
op|'='
name|'fake_tag_list'
newline|'\n'
nl|'\n'
name|'tag_list_obj'
op|'='
name|'tag'
op|'.'
name|'TagList'
op|'.'
name|'get_by_resource_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|')'
newline|'\n'
nl|'\n'
name|'get_by_inst'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare_tag_list'
op|'('
name|'fake_tag_list'
op|','
name|'tag_list_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_set'"
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'tag_set'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag_set'
op|'.'
name|'return_value'
op|'='
name|'fake_tag_list'
newline|'\n'
name|'tag_list_obj'
op|'='
name|'tag'
op|'.'
name|'TagList'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|','
op|'['
name|'TAG_NAME1'
op|','
name|'TAG_NAME2'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'tag_set'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'RESOURCE_ID'
op|','
op|'['
name|'TAG_NAME1'
op|','
name|'TAG_NAME2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare_tag_list'
op|'('
name|'fake_tag_list'
op|','
name|'tag_list_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_tag_delete_all'"
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|','
name|'tag_delete_all'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tag'
op|'.'
name|'TagList'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|')'
newline|'\n'
name|'tag_delete_all'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'RESOURCE_ID'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTagList
dedent|''
dedent|''
name|'class'
name|'TestTagList'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
name|'_TestTagList'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestTagListRemote
dedent|''
name|'class'
name|'TestTagListRemote'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
name|'_TestTagList'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
