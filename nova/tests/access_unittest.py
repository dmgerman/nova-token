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
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'logging'
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
name|'flags'
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
op|'.'
name|'users'
name|'import'
name|'UserManager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'rbac'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|class|Context
name|'class'
name|'Context'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|AccessTestCase
dedent|''
name|'class'
name|'AccessTestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
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
name|'super'
op|'('
name|'AccessTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'='
string|"'fake'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_storage'
op|'='
name|'True'
newline|'\n'
name|'um'
op|'='
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
comment|'# Make test users'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'testadmin'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'error'
op|'('
name|'str'
op|'('
name|'err'
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'testpmsys'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testpmsys'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'testnet'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testnet'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'testsys'
op|'='
name|'um'
op|'.'
name|'create_user'
op|'('
string|"'testsys'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
comment|'# Assign some rules'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testadmin'"
op|','
string|"'cloudadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testpmsys'"
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testnet'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'um'
op|'.'
name|'add_role'
op|'('
string|"'testsys'"
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
nl|'\n'
comment|'# Make a test project'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'project'
op|'='
name|'um'
op|'.'
name|'create_project'
op|'('
string|"'testproj'"
op|','
string|"'testpmsys'"
op|','
string|"'a test project'"
op|','
op|'['
string|"'testpmsys'"
op|','
string|"'testnet'"
op|','
string|"'testsys'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'project'
op|'.'
name|'add_role'
op|'('
name|'self'
op|'.'
name|'testnet'
op|','
string|"'netadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'project'
op|'.'
name|'add_role'
op|'('
name|'self'
op|'.'
name|'testsys'
op|','
string|"'sysadmin'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
name|'pass'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'Context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
newline|'\n'
comment|'#user is set in each test'
nl|'\n'
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
name|'um'
op|'='
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
comment|'# Delete the test project'
nl|'\n'
name|'um'
op|'.'
name|'delete_project'
op|'('
string|"'testproj'"
op|')'
newline|'\n'
comment|'# Delete the test user'
nl|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testadmin'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testpmsys'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testnet'"
op|')'
newline|'\n'
name|'um'
op|'.'
name|'delete_user'
op|'('
string|"'testsys'"
op|')'
newline|'\n'
name|'super'
op|'('
name|'AccessTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_001_allow_all
dedent|''
name|'def'
name|'test_001_allow_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testadmin'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testpmsys'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testnet'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testsys'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_all'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_002_allow_none
dedent|''
name|'def'
name|'test_002_allow_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testadmin'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_none'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testpmsys'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_none'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testnet'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_none'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testsys'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_none'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_003_allow_project_manager
dedent|''
name|'def'
name|'test_003_allow_project_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testadmin'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_project_manager'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testpmsys'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_project_manager'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testnet'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_project_manager'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testsys'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_project_manager'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_004_allow_sys_and_net
dedent|''
name|'def'
name|'test_004_allow_sys_and_net'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testadmin'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_sys_and_net'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testpmsys'
comment|"# doesn't have the per project sysadmin"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_sys_and_net'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testnet'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_sys_and_net'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testsys'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_sys_and_net'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_005_allow_sys_no_pm
dedent|''
name|'def'
name|'test_005_allow_sys_no_pm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testadmin'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_sys_no_pm'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testpmsys'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_sys_no_pm'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testnet'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotAuthorized'
op|','
name|'self'
op|'.'
name|'_allow_sys_no_pm'
op|','
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'testsys'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'_allow_sys_no_pm'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rbac'
op|'.'
name|'allow'
op|'('
string|"'all'"
op|')'
newline|'\n'
DECL|member|_allow_all
name|'def'
name|'_allow_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rbac'
op|'.'
name|'allow'
op|'('
string|"'none'"
op|')'
newline|'\n'
DECL|member|_allow_none
name|'def'
name|'_allow_none'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rbac'
op|'.'
name|'allow'
op|'('
string|"'projectmanager'"
op|')'
newline|'\n'
DECL|member|_allow_project_manager
name|'def'
name|'_allow_project_manager'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rbac'
op|'.'
name|'allow'
op|'('
string|"'sysadmin'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
DECL|member|_allow_sys_and_net
name|'def'
name|'_allow_sys_and_net'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'rbac'
op|'.'
name|'allow'
op|'('
string|"'sysadmin'"
op|')'
newline|'\n'
op|'@'
name|'rbac'
op|'.'
name|'deny'
op|'('
string|"'projectmanager'"
op|')'
newline|'\n'
DECL|member|_allow_sys_no_pm
name|'def'
name|'_allow_sys_no_pm'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
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
