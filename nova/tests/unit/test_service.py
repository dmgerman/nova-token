begin_unit
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
string|'"""\nUnit Tests for remote procedure calls using queue\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'testtools'
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
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'service'
name|'as'
name|'_service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
DECL|variable|test_service_opts
name|'test_service_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"fake_manager"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.tests.unit.test_service.FakeManager"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Manager for testing"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"test_service_listen"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Host to bind test service to"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"test_service_listen_port"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Port number to bind test service to"'
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'test_service_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeManager
name|'class'
name|'FakeManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fake manager for tests."""'
newline|'\n'
DECL|member|test_method
name|'def'
name|'test_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'manager'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedService
dedent|''
dedent|''
name|'class'
name|'ExtendedService'
op|'('
name|'service'
op|'.'
name|'Service'
op|')'
op|':'
newline|'\n'
DECL|member|test_method
indent|'    '
name|'def'
name|'test_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'service'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceManagerTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for Services."""'
newline|'\n'
nl|'\n'
DECL|member|test_message_gets_to_manager
name|'def'
name|'test_message_gets_to_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serv'
op|'.'
name|'test_method'
op|'('
op|')'
op|','
string|"'manager'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_override_manager_method
dedent|''
name|'def'
name|'test_override_manager_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serv'
op|'='
name|'ExtendedService'
op|'('
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serv'
op|'.'
name|'test_method'
op|'('
op|')'
op|','
string|"'service'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_with_min_down_time
dedent|''
name|'def'
name|'test_service_with_min_down_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'service_down_time'"
op|','
number|'10'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'report_interval'"
op|','
number|'10'
op|')'
newline|'\n'
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'test'"
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'service_down_time'
op|','
number|'25'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceFlagsTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceFlagsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_service_enabled_on_create_based_on_flag
indent|'    '
name|'def'
name|'test_service_enabled_on_create_based_on_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_new_services'
op|'='
name|'True'
op|')'
newline|'\n'
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'app'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'ref'
op|'['
string|"'disabled'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_disabled_on_create_based_on_flag
dedent|''
name|'def'
name|'test_service_disabled_on_create_based_on_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_new_services'
op|'='
name|'False'
op|')'
newline|'\n'
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'app'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'ref'
op|'='
name|'db'
op|'.'
name|'service_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'app'
op|'.'
name|'service_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ref'
op|'['
string|"'disabled'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceTestCase
dedent|''
dedent|''
name|'class'
name|'ServiceTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for Services."""'
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
name|'ServiceTestCase'
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
name|'host'
op|'='
string|"'foo'"
newline|'\n'
name|'self'
op|'.'
name|'binary'
op|'='
string|"'nova-fake'"
newline|'\n'
name|'self'
op|'.'
name|'topic'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
string|"'service_create'"
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
string|"'service_get_by_args'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_local'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'conductor'"
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
nl|'\n'
comment|'# NOTE(vish): Create was moved out of mox replay to make sure that'
nl|'\n'
comment|'#             the looping calls are created in StartService.'
nl|'\n'
indent|'        '
name|'app'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|','
name|'binary'
op|'='
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'topic'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'app'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_service_start_mocks
dedent|''
name|'def'
name|'_service_start_mocks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service_create'
op|'='
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|'}'
newline|'\n'
name|'service_ref'
op|'='
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'binary'"
op|':'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
string|"'topic'"
op|':'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'report_count'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'binary'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'service_create'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'service_ref'
op|')'
newline|'\n'
name|'return'
name|'service_ref'
newline|'\n'
nl|'\n'
DECL|member|test_init_and_start_hooks
dedent|''
name|'def'
name|'test_init_and_start_hooks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'FakeManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
nl|'\n'
string|"'FakeManager'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'init_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'pre_start_hook'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'post_start_hook'"
op|')'
newline|'\n'
nl|'\n'
name|'FakeManager'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'service_name'
op|'='
name|'self'
op|'.'
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'additional_endpoints'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# init_host is called before any service record is created'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_service_start_mocks'
op|'('
op|')'
newline|'\n'
comment|'# pre_start_hook is called after service record is created,'
nl|'\n'
comment|'# but before RPC consumer is created'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'pre_start_hook'
op|'('
op|')'
newline|'\n'
comment|'# post_start_hook is called after RPC consumer is created.'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'post_start_hook'
op|'('
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_service_check_create_race
dedent|''
name|'def'
name|'_test_service_check_create_race'
op|'('
name|'self'
op|','
name|'ex'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'FakeManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
string|"'FakeManager'"
op|','
nl|'\n'
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'init_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'pre_start_hook'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'post_start_hook'"
op|')'
newline|'\n'
nl|'\n'
name|'FakeManager'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|')'
newline|'\n'
nl|'\n'
comment|'# init_host is called before any service record is created'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'binary'
nl|'\n'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'service_create'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
nl|'\n'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'ex'
op|')'
newline|'\n'
nl|'\n'
DECL|class|TestException
name|'class'
name|'TestException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'db'
op|'.'
name|'service_get_by_args'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'host'
op|','
name|'self'
op|'.'
name|'binary'
nl|'\n'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'TestException'
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TestException'
op|','
name|'serv'
op|'.'
name|'start'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_check_create_race_topic_exists
dedent|''
name|'def'
name|'test_service_check_create_race_topic_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'ServiceTopicExists'
op|'('
name|'host'
op|'='
string|"'foo'"
op|','
name|'topic'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_service_check_create_race'
op|'('
name|'ex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_check_create_race_binary_exists
dedent|''
name|'def'
name|'test_service_check_create_race_binary_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ex'
op|'='
name|'exception'
op|'.'
name|'ServiceBinaryExists'
op|'('
name|'host'
op|'='
string|"'foo'"
op|','
name|'binary'
op|'='
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_service_check_create_race'
op|'('
name|'ex'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_parent_graceful_shutdown
dedent|''
name|'def'
name|'test_parent_graceful_shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'manager_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'FakeManager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'__name__'
op|']'
op|','
nl|'\n'
string|"'FakeManager'"
op|','
name|'use_mock_anything'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'init_host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'pre_start_hook'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|','
string|"'post_start_hook'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'_service'
op|'.'
name|'Service'
op|','
string|"'stop'"
op|')'
newline|'\n'
nl|'\n'
name|'FakeManager'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'manager_mock'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'service_name'
op|'='
name|'self'
op|'.'
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'additional_endpoints'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# init_host is called before any service record is created'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_service_start_mocks'
op|'('
op|')'
newline|'\n'
comment|'# pre_start_hook is called after service record is created,'
nl|'\n'
comment|'# but before RPC consumer is created'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'pre_start_hook'
op|'('
op|')'
newline|'\n'
comment|'# post_start_hook is called after RPC consumer is created.'
nl|'\n'
name|'self'
op|'.'
name|'manager_mock'
op|'.'
name|'post_start_hook'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'_service'
op|'.'
name|'Service'
op|'.'
name|'stop'
op|'('
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
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serv'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.servicegroup.API'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.conductor.api.LocalAPI.service_get_by_args'"
op|')'
newline|'\n'
DECL|member|test_parent_graceful_shutdown_with_cleanup_host
name|'def'
name|'test_parent_graceful_shutdown_with_cleanup_host'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_svc_get_by_args'
op|','
nl|'\n'
name|'mock_API'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_svc_get_by_args'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'some_value'"
op|'}'
newline|'\n'
name|'mock_manager'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
nl|'\n'
name|'serv'
op|'.'
name|'manager'
op|'='
name|'mock_manager'
newline|'\n'
name|'serv'
op|'.'
name|'manager'
op|'.'
name|'additional_endpoints'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'manager'
op|'.'
name|'init_host'
op|'.'
name|'assert_called_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'serv'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'manager'
op|'.'
name|'cleanup_host'
op|'.'
name|'assert_called_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.servicegroup.API'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.conductor.api.LocalAPI.service_get_by_args'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rpc'
op|','
string|"'get_server'"
op|')'
newline|'\n'
DECL|member|test_service_stop_waits_for_rpcserver
name|'def'
name|'test_service_stop_waits_for_rpcserver'
op|'('
nl|'\n'
name|'self'
op|','
name|'mock_rpc'
op|','
name|'mock_svc_get_by_args'
op|','
name|'mock_API'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_svc_get_by_args'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'some_value'"
op|'}'
newline|'\n'
name|'serv'
op|'='
name|'service'
op|'.'
name|'Service'
op|'('
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'binary'
op|','
nl|'\n'
name|'self'
op|'.'
name|'topic'
op|','
nl|'\n'
string|"'nova.tests.unit.test_service.FakeManager'"
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'rpcserver'
op|'.'
name|'start'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'rpcserver'
op|'.'
name|'stop'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
name|'serv'
op|'.'
name|'rpcserver'
op|'.'
name|'wait'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWSGIService
dedent|''
dedent|''
name|'class'
name|'TestWSGIService'
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
name|'TestWSGIService'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'wsgi'
op|'.'
name|'Loader'
op|','
string|'"load_app"'
op|','
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_random_port
dedent|''
name|'def'
name|'test_service_random_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'test_service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_workers_set_default
dedent|''
name|'def'
name|'test_workers_set_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"osapi_compute"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_workers_set_good_user_setting
dedent|''
name|'def'
name|'test_workers_set_good_user_setting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'osapi_compute_workers'"
op|','
number|'8'
op|')'
newline|'\n'
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"osapi_compute"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
number|'8'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_workers_set_zero_user_setting
dedent|''
name|'def'
name|'test_workers_set_zero_user_setting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'osapi_compute_workers'"
op|','
number|'0'
op|')'
newline|'\n'
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"osapi_compute"'
op|')'
newline|'\n'
comment|'# If a value less than 1 is used, defaults to number of procs available'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_service_start_with_illegal_workers
dedent|''
name|'def'
name|'test_service_start_with_illegal_workers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|'"osapi_compute_workers"'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'service'
op|'.'
name|'WSGIService'
op|','
string|'"osapi_compute"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_openstack_compute_api_workers_set_default
dedent|''
name|'def'
name|'test_openstack_compute_api_workers_set_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"openstack_compute_api_v2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_openstack_compute_api_workers_set_good_user_setting
dedent|''
name|'def'
name|'test_openstack_compute_api_workers_set_good_user_setting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'osapi_compute_workers'"
op|','
number|'8'
op|')'
newline|'\n'
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"openstack_compute_api_v2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
number|'8'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_openstack_compute_api_workers_set_zero_user_setting
dedent|''
name|'def'
name|'test_openstack_compute_api_workers_set_zero_user_setting'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'osapi_compute_workers'"
op|','
number|'0'
op|')'
newline|'\n'
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"openstack_compute_api_v2"'
op|')'
newline|'\n'
comment|'# If a value less than 1 is used, defaults to number of procs available'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'workers'
op|','
name|'processutils'
op|'.'
name|'get_worker_count'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_openstack_compute_api_service_start_with_illegal_workers
dedent|''
name|'def'
name|'test_openstack_compute_api_service_start_with_illegal_workers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|'"osapi_compute_workers"'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'service'
op|'.'
name|'WSGIService'
op|','
string|'"openstack_compute_api_v2"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'testtools'
op|'.'
name|'skipIf'
op|'('
name|'not'
name|'utils'
op|'.'
name|'is_ipv6_supported'
op|'('
op|')'
op|','
string|'"no ipv6 support"'
op|')'
newline|'\n'
DECL|member|test_service_random_port_with_ipv6
name|'def'
name|'test_service_random_port_with_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|'"test_service_listen"'
op|','
string|'"::1"'
op|')'
newline|'\n'
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"::1"'
op|','
name|'test_service'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'test_service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reset_pool_size_to_default
dedent|''
name|'def'
name|'test_reset_pool_size_to_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Stopping the service, which in turn sets pool size to 0'
nl|'\n'
name|'test_service'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'server'
op|'.'
name|'_pool'
op|'.'
name|'size'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# Resetting pool size to default'
nl|'\n'
name|'test_service'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'test_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_service'
op|'.'
name|'server'
op|'.'
name|'_pool'
op|'.'
name|'size'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'wsgi_default_pool_size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLauncher
dedent|''
dedent|''
name|'class'
name|'TestLauncher'
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
name|'TestLauncher'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'wsgi'
op|'.'
name|'Loader'
op|','
string|'"load_app"'
op|','
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
op|'.'
name|'WSGIService'
op|'('
string|'"test_service"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_launch_app
dedent|''
name|'def'
name|'test_launch_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'.'
name|'serve'
op|'('
name|'self'
op|'.'
name|'service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'service'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'_launcher'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
