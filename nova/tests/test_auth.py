begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'M2Crypto'
name|'import'
name|'X509'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.auth_unittest'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|user_generator
name|'class'
name|'user_generator'
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
name|'manager'
op|','
op|'**'
name|'user_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'name'"
name|'not'
name|'in'
name|'user_state'
op|':'
newline|'\n'
indent|'            '
name|'user_state'
op|'['
string|"'name'"
op|']'
op|'='
string|"'test1'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'manager'
op|'.'
name|'create_user'
op|'('
op|'**'
name|'user_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'user'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'type'
op|','
name|'trace'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|project_generator
dedent|''
dedent|''
name|'class'
name|'project_generator'
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
name|'manager'
op|','
op|'**'
name|'project_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'name'"
name|'not'
name|'in'
name|'project_state'
op|':'
newline|'\n'
indent|'            '
name|'project_state'
op|'['
string|"'name'"
op|']'
op|'='
string|"'testproj'"
newline|'\n'
dedent|''
name|'if'
string|"'manager_user'"
name|'not'
name|'in'
name|'project_state'
op|':'
newline|'\n'
indent|'            '
name|'project_state'
op|'['
string|"'manager_user'"
op|']'
op|'='
string|"'test1'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'manager'
op|'.'
name|'create_project'
op|'('
op|'**'
name|'project_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'project'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'type'
op|','
name|'trace'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|user_and_project_generator
dedent|''
dedent|''
name|'class'
name|'user_and_project_generator'
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
name|'manager'
op|','
name|'user_state'
op|'='
op|'{'
op|'}'
op|','
name|'project_state'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
newline|'\n'
name|'if'
string|"'name'"
name|'not'
name|'in'
name|'user_state'
op|':'
newline|'\n'
indent|'            '
name|'user_state'
op|'['
string|"'name'"
op|']'
op|'='
string|"'test1'"
newline|'\n'
dedent|''
name|'if'
string|"'name'"
name|'not'
name|'in'
name|'project_state'
op|':'
newline|'\n'
indent|'            '
name|'project_state'
op|'['
string|"'name'"
op|']'
op|'='
string|"'testproj'"
newline|'\n'
dedent|''
name|'if'
string|"'manager_user'"
name|'not'
name|'in'
name|'project_state'
op|':'
newline|'\n'
indent|'            '
name|'project_state'
op|'['
string|"'manager_user'"
op|']'
op|'='
string|"'test1'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'user'
op|'='
name|'manager'
op|'.'
name|'create_user'
op|'('
op|'**'
name|'user_state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'manager'
op|'.'
name|'create_project'
op|'('
op|'**'
name|'project_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'self'
op|'.'
name|'user'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'type'
op|','
name|'trace'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_AuthManagerBaseTestCase
dedent|''
dedent|''
name|'class'
name|'_AuthManagerBaseTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'FLAGS'
op|'.'
name|'auth_driver'
op|'='
name|'self'
op|'.'
name|'auth_driver'
newline|'\n'
name|'super'
op|'('
name|'_AuthManagerBaseTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
name|'new'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_find_user
dedent|''
name|'def'
name|'test_create_and_find_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_find_with_properties
dedent|''
dedent|''
name|'def'
name|'test_create_and_find_with_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|'"herbert"'
op|','
name|'secret'
op|'='
string|'"classified"'
op|','
nl|'\n'
name|'access'
op|'='
string|'"private-party"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'u'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'herbert'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'herbert'"
op|','
name|'u'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'herbert'"
op|','
name|'u'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'classified'"
op|','
name|'u'
op|'.'
name|'secret'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'private-party'"
op|','
name|'u'
op|'.'
name|'access'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_signature_is_valid
dedent|''
dedent|''
name|'def'
name|'test_004_signature_is_valid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'#self.assertTrue(self.manager.authenticate(**boto.generate_url ...? ))'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
comment|'#raise NotImplementedError'
nl|'\n'
nl|'\n'
DECL|member|test_005_can_get_credentials
dedent|''
name|'def'
name|'test_005_can_get_credentials'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
name|'credentials'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
op|'.'
name|'get_credentials'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'credentials'
op|','
nl|'\n'
string|'\'export EC2_ACCESS_KEY="access"\\n\''
op|'+'
nl|'\n'
string|'\'export EC2_SECRET_KEY="secret"\\n\''
op|'+'
nl|'\n'
string|'\'export EC2_URL="http://127.0.0.1:8773/services/Cloud"\\n\''
op|'+'
nl|'\n'
string|'\'export S3_URL="http://127.0.0.1:3333/"\\n\''
op|'+'
nl|'\n'
string|'\'export EC2_USER_ID="test1"\\n\''
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_list_users
dedent|''
name|'def'
name|'test_can_list_users'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|'"test2"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'users'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_users'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'u'
op|':'
name|'u'
op|'.'
name|'id'
op|'=='
string|"'test1'"
op|','
name|'users'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'u'
op|':'
name|'u'
op|'.'
name|'id'
op|'=='
string|"'test2'"
op|','
name|'users'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'filter'
op|'('
name|'lambda'
name|'u'
op|':'
name|'u'
op|'.'
name|'id'
op|'=='
string|"'test3'"
op|','
name|'users'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_add_and_remove_user_role
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_add_and_remove_user_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
string|"'test1'"
op|','
string|"'itsec'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
string|"'test1'"
op|','
string|"'itsec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
string|"'test1'"
op|','
string|"'itsec'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_role'
op|'('
string|"'test1'"
op|','
string|"'itsec'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
string|"'test1'"
op|','
string|"'itsec'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_create_and_get_project
dedent|''
dedent|''
name|'def'
name|'test_can_create_and_get_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'u'
op|','
name|'p'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_list_projects
dedent|''
dedent|''
name|'def'
name|'test_can_list_projects'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|'"testproj2"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'projects'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_projects'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'p'
op|':'
name|'p'
op|'.'
name|'name'
op|'=='
string|"'testproj'"
op|','
name|'projects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'p'
op|':'
name|'p'
op|'.'
name|'name'
op|'=='
string|"'testproj2'"
op|','
name|'projects'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'filter'
op|'('
name|'lambda'
name|'p'
op|':'
name|'p'
op|'.'
name|'name'
op|'=='
string|"'testproj3'"
op|','
nl|'\n'
name|'projects'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_create_and_get_project_with_attributes
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_create_and_get_project_with_attributes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'description'
op|'='
string|"'A test project'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'A test project'"
op|','
name|'project'
op|'.'
name|'description'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_create_project_with_manager
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_create_project_with_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test1'"
op|','
name|'project'
op|'.'
name|'project_manager_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_manager'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_project_assigns_manager_to_members
dedent|''
dedent|''
name|'def'
name|'test_create_project_assigns_manager_to_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_extra_project_members
dedent|''
dedent|''
name|'def'
name|'test_no_extra_project_members'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
name|'as'
name|'baduser'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'baduser'
op|','
nl|'\n'
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_extra_project_managers
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_no_extra_project_managers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
name|'as'
name|'baduser'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_manager'
op|'('
name|'baduser'
op|','
nl|'\n'
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_add_user_to_project
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_add_user_to_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
name|'as'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'_user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_to_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_remove_user_from_project
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_remove_user_from_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
name|'as'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'_user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_to_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_from_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_add_remove_user_with_role
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_add_remove_user_with_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
name|'as'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'_user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(todd): after modifying users you must reload project'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_to_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'developer'"
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_from_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'developer'"
op|','
nl|'\n'
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'is_project_member'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_generate_x509
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_generate_x509'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(todd): this doesn't assert against the auth manager"
nl|'\n'
comment|'#             so it probably belongs in crypto_unittest'
nl|'\n'
comment|"#             but I'm leaving it where I found it."
nl|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(vish): Setup runs genroot.sh if it hasn't been run"
nl|'\n'
indent|'            '
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'_key'
op|','
name|'cert_str'
op|'='
name|'crypto'
op|'.'
name|'generate_x509_cert'
op|'('
name|'user'
op|'.'
name|'id'
op|','
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'cert_str'
op|')'
newline|'\n'
nl|'\n'
name|'full_chain'
op|'='
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
name|'project'
op|'.'
name|'id'
op|','
name|'chain'
op|'='
name|'True'
op|')'
newline|'\n'
name|'int_cert'
op|'='
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
name|'project'
op|'.'
name|'id'
op|','
name|'chain'
op|'='
name|'False'
op|')'
newline|'\n'
name|'cloud_cert'
op|'='
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"CA chain:\\n\\n =====\\n%s\\n\\n====="'
op|','
name|'full_chain'
op|')'
newline|'\n'
name|'signed_cert'
op|'='
name|'X509'
op|'.'
name|'load_cert_string'
op|'('
name|'cert_str'
op|')'
newline|'\n'
name|'chain_cert'
op|'='
name|'X509'
op|'.'
name|'load_cert_string'
op|'('
name|'full_chain'
op|')'
newline|'\n'
name|'int_cert'
op|'='
name|'X509'
op|'.'
name|'load_cert_string'
op|'('
name|'int_cert'
op|')'
newline|'\n'
name|'cloud_cert'
op|'='
name|'X509'
op|'.'
name|'load_cert_string'
op|'('
name|'cloud_cert'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'signed_cert'
op|'.'
name|'verify'
op|'('
name|'chain_cert'
op|'.'
name|'get_pubkey'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'signed_cert'
op|'.'
name|'verify'
op|'('
name|'int_cert'
op|'.'
name|'get_pubkey'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'signed_cert'
op|'.'
name|'verify'
op|'('
name|'cloud_cert'
op|'.'
name|'get_pubkey'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'signed_cert'
op|'.'
name|'verify'
op|'('
name|'cloud_cert'
op|'.'
name|'get_pubkey'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_adding_role_to_project_is_ignored_unless_added_to_user
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_adding_role_to_project_is_ignored_unless_added_to_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
newline|'\n'
comment|'# NOTE(todd): it will still show up in get_user_roles(u, project)'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_user_role_doesnt_infect_project_roles
dedent|''
dedent|''
name|'def'
name|'test_add_user_role_doesnt_infect_project_roles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_list_user_roles
dedent|''
dedent|''
name|'def'
name|'test_can_list_user_roles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'roles'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user_roles'
op|'('
name|'user'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'sysadmin'"
name|'in'
name|'roles'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'netadmin'"
name|'in'
name|'roles'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_list_project_roles
dedent|''
dedent|''
name|'def'
name|'test_can_list_project_roles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'netadmin'"
op|','
name|'project'
op|')'
newline|'\n'
name|'project_roles'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user_roles'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'sysadmin'"
name|'in'
name|'project_roles'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'netadmin'"
name|'in'
name|'project_roles'
op|')'
newline|'\n'
comment|'# has role should be false user-level role is missing'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'netadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_remove_user_roles
dedent|''
dedent|''
name|'def'
name|'test_can_remove_user_roles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_removing_user_role_hides_it_from_project
dedent|''
dedent|''
name|'def'
name|'test_removing_user_role_hides_it_from_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_remove_project_role_but_keep_user_role
dedent|''
dedent|''
name|'def'
name|'test_can_remove_project_role_but_keep_user_role'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'remove_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|','
name|'project'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'has_role'
op|'('
name|'user'
op|','
string|"'sysadmin'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_retrieve_project_by_user
dedent|''
dedent|''
name|'def'
name|'test_can_retrieve_project_by_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
name|'as'
op|'('
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_projects'
op|'('
string|"'test1'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_modify_project
dedent|''
dedent|''
name|'def'
name|'test_can_modify_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'modify_project'
op|'('
string|"'testproj'"
op|','
string|"'test2'"
op|','
string|"'new desc'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test2'"
op|','
name|'project'
op|'.'
name|'project_manager_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'new desc'"
op|','
name|'project'
op|'.'
name|'description'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_modify_project_adds_new_manager
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_modify_project_adds_new_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_and_project_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|','
name|'name'
op|'='
string|"'test2'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'modify_project'
op|'('
string|"'testproj'"
op|','
string|"'test2'"
op|','
string|"'new desc'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'test2'"
name|'in'
name|'project'
op|'.'
name|'member_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_delete_project
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_can_delete_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'testproj'"
op|','
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_project'
op|'('
string|"'testproj'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
name|'projectlist'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_projects'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'filter'
op|'('
name|'lambda'
name|'p'
op|':'
name|'p'
op|'.'
name|'name'
op|'=='
string|"'testproj'"
op|','
nl|'\n'
name|'projectlist'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_delete_user
dedent|''
dedent|''
name|'def'
name|'test_can_delete_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
string|"'test1'"
op|')'
newline|'\n'
name|'userlist'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_users'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'not'
name|'filter'
op|'('
name|'lambda'
name|'u'
op|':'
name|'u'
op|'.'
name|'id'
op|'=='
string|"'test1'"
op|','
name|'userlist'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_can_modify_users
dedent|''
name|'def'
name|'test_can_modify_users'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'user_generator'
op|'('
name|'self'
op|'.'
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'manager'
op|'.'
name|'modify_user'
op|'('
string|"'test1'"
op|','
string|"'access'"
op|','
string|"'secret'"
op|','
name|'True'
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'get_user'
op|'('
string|"'test1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'access'"
op|','
name|'user'
op|'.'
name|'access'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'secret'"
op|','
name|'user'
op|'.'
name|'secret'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'user'
op|'.'
name|'is_admin'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthManagerLdapTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'AuthManagerLdapTestCase'
op|'('
name|'_AuthManagerBaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|auth_driver
indent|'    '
name|'auth_driver'
op|'='
string|"'nova.auth.ldapdriver.FakeLdapDriver'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AuthManagerDbTestCase
dedent|''
name|'class'
name|'AuthManagerDbTestCase'
op|'('
name|'_AuthManagerBaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|auth_driver
indent|'    '
name|'auth_driver'
op|'='
string|"'nova.auth.dbdriver.DbDriver'"
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
comment|'# TODO: Implement use_fake as an option'
nl|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
