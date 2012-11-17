begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
string|'"""Tests For Console proxy."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'api'
name|'as'
name|'console_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'rpcapi'
name|'as'
name|'console_rpcapi'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'console_driver'"
op|','
string|"'nova.console.manager'"
op|')'
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
string|'"""Test case for console proxy manager"""'
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
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'console_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
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
name|'self'
op|'.'
name|'host'
op|'='
string|"'test_compute_host'"
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
number|'1'
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
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project_id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
number|'1'
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
nl|'\n'
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
name|'instance'
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
name|'instance'
op|'['
string|"'id'"
op|']'
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
name|'instance'
op|'['
string|"'id'"
op|']'
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
string|"'instance_uuid'"
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
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
name|'instance'
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
name|'instance'
op|'['
string|"'id'"
op|']'
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
name|'instance'
op|'['
string|"'id'"
op|']'
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
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
name|'instance'
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
name|'instance'
op|'['
string|"'id'"
op|']'
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAPITestCase
dedent|''
dedent|''
name|'class'
name|'ConsoleAPITestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for console API"""'
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
name|'super'
op|'('
name|'ConsoleAPITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'console_api'
op|'='
name|'console_api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_uuid'
op|'='
string|"'00000000-aaaa-bbbb-cccc-000000000000'"
newline|'\n'
name|'self'
op|'.'
name|'fake_instance'
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
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fake_host'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'fake_console'
op|'='
op|'{'
nl|'\n'
string|"'pool'"
op|':'
op|'{'
string|"'host'"
op|':'
string|"'fake_host'"
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'fake_id'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_fake_cast
name|'def'
name|'_fake_cast'
op|'('
name|'_ctxt'
op|','
name|'_topic'
op|','
name|'_msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'_fake_cast'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_db_console_get
name|'def'
name|'_fake_db_console_get'
op|'('
name|'_ctxt'
op|','
name|'_console_uuid'
op|','
name|'_instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'fake_console'
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
string|"'console_get'"
op|','
name|'_fake_db_console_get'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_db_console_get_all_by_instance
name|'def'
name|'_fake_db_console_get_all_by_instance'
op|'('
name|'_ctxt'
op|','
name|'_instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'self'
op|'.'
name|'fake_console'
op|']'
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
string|"'console_get_all_by_instance'"
op|','
nl|'\n'
name|'_fake_db_console_get_all_by_instance'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fake_instance_get_by_uuid
name|'def'
name|'_fake_instance_get_by_uuid'
op|'('
name|'_ctxt'
op|','
name|'_instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'fake_instance'
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
string|"'instance_get_by_uuid'"
op|','
name|'_fake_instance_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_consoles
dedent|''
name|'def'
name|'test_get_consoles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'console'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_consoles'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console'
op|','
op|'['
name|'self'
op|'.'
name|'fake_console'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console
dedent|''
name|'def'
name|'test_get_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'console'
op|'='
name|'self'
op|'.'
name|'console_api'
op|'.'
name|'get_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
string|"'fake_id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'console'
op|','
name|'self'
op|'.'
name|'fake_console'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_console
dedent|''
name|'def'
name|'test_delete_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|','
string|"'remove_console'"
op|')'
newline|'\n'
nl|'\n'
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|'.'
name|'remove_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'fake_id'"
op|')'
newline|'\n'
nl|'\n'
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
name|'console_api'
op|'.'
name|'delete_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|','
nl|'\n'
string|"'fake_id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_console
dedent|''
name|'def'
name|'test_create_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|','
string|"'add_console'"
op|')'
newline|'\n'
nl|'\n'
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|'.'
name|'add_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
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
name|'console_api'
op|'.'
name|'create_console'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'fake_uuid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
