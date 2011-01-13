begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nTests For Console proxy.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
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
name|'import'
name|'utils'
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
name|'console'
name|'import'
name|'manager'
name|'as'
name|'console_manager'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleTestCase
name|'class'
name|'ConsoleTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for console proxy"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ConsoleTestCase'
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
name|'console_driver'
op|'='
string|"'nova.console.fake.FakeConsoleProxy'"
op|','
nl|'\n'
name|'stub_compute'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'console'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'console_manager'
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
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
string|"'test_compute_host'"
newline|'\n'
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
name|'super'
op|'('
name|'ConsoleTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
comment|"#inst['host'] = self.host"
nl|'\n'
comment|"#inst['name'] = 'instance-1234'"
nl|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
string|"'ami-test'"
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.tiny'"
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_get_pool_for_instance_host
dedent|''
name|'def'
name|'test_get_pool_for_instance_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'get_pool_for_instance_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool'
op|'['
string|"'compute_host'"
op|']'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_pool_creates_new_pool_if_needed
dedent|''
name|'def'
name|'test_get_pool_creates_new_pool_if_needed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'console_pool_get_by_host_type'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'driver'
op|'.'
name|'console_type'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'get_pool_for_instance_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'pool2'
op|'='
name|'db'
op|'.'
name|'console_pool_get_by_host_type'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'driver'
op|'.'
name|'console_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool'
op|'['
string|"'id'"
op|']'
op|','
name|'pool2'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_pool_does_not_create_new_pool_if_exists
dedent|''
name|'def'
name|'test_get_pool_does_not_create_new_pool_if_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_info'
op|'='
op|'{'
string|"'address'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'1234pass'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'console'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'console_type'"
op|':'
name|'self'
op|'.'
name|'console'
op|'.'
name|'driver'
op|'.'
name|'console_type'
op|','
nl|'\n'
string|"'compute_host'"
op|':'
string|"'sometesthostname'"
op|'}'
newline|'\n'
name|'new_pool'
op|'='
name|'db'
op|'.'
name|'console_pool_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'pool_info'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'get_pool_for_instance_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'sometesthostname'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pool'
op|'['
string|"'id'"
op|']'
op|','
name|'new_pool'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_console
dedent|''
name|'def'
name|'test_add_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'add_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'db'
op|'.'
name|'console_pool_get_by_host_type'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'driver'
op|'.'
name|'console_type'
op|')'
newline|'\n'
nl|'\n'
name|'console_instances'
op|'='
op|'['
name|'con'
op|'['
string|"'instance_id'"
op|']'
name|'for'
name|'con'
name|'in'
name|'pool'
op|'.'
name|'consoles'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'instance_id'
name|'in'
name|'console_instances'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_console_does_not_duplicate
dedent|''
name|'def'
name|'test_add_console_does_not_duplicate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'cons1'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'add_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'cons2'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'add_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cons1'
op|','
name|'cons2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_console
dedent|''
name|'def'
name|'test_remove_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'console_id'
op|'='
name|'self'
op|'.'
name|'console'
op|'.'
name|'add_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'console'
op|'.'
name|'remove_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'console_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'console_get'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'console_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
