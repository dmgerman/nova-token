begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'manager'
name|'as'
name|'compute_manager'
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
name|'objects'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'virtapi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtAPIBaseTest
name|'class'
name|'VirtAPIBaseTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|','
name|'test'
op|'.'
name|'APICoverage'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|cover_api
indent|'    '
name|'cover_api'
op|'='
name|'virtapi'
op|'.'
name|'VirtAPI'
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
name|'VirtAPIBaseTest'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'set_up_virtapi'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_up_virtapi
dedent|''
name|'def'
name|'set_up_virtapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'virtapi'
op|'='
name|'virtapi'
op|'.'
name|'VirtAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertExpected
dedent|''
name|'def'
name|'assertExpected'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
nl|'\n'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'virtapi'
op|','
name|'method'
op|')'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wait_for_instance_event
dedent|''
name|'def'
name|'test_wait_for_instance_event'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertExpected'
op|'('
string|"'wait_for_instance_event'"
op|','
nl|'\n'
string|"'instance'"
op|','
op|'['
string|"'event'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVirtAPITest
dedent|''
dedent|''
name|'class'
name|'FakeVirtAPITest'
op|'('
name|'VirtAPIBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|cover_api
indent|'    '
name|'cover_api'
op|'='
name|'fake'
op|'.'
name|'FakeVirtAPI'
newline|'\n'
nl|'\n'
DECL|member|set_up_virtapi
name|'def'
name|'set_up_virtapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'virtapi'
op|'='
name|'fake'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertExpected
dedent|''
name|'def'
name|'assertExpected'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'method'
op|'=='
string|"'wait_for_instance_event'"
op|':'
newline|'\n'
indent|'            '
name|'run'
op|'='
name|'False'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'wait_for_instance_event'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'run'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'run'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'db'
op|','
name|'method'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'method'
name|'in'
op|'('
string|"'aggregate_metadata_add'"
op|','
string|"'aggregate_metadata_delete'"
op|','
nl|'\n'
string|"'security_group_rule_get_by_security_group'"
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): FakeVirtAPI will convert the first argument to'
nl|'\n'
comment|"# argument['id'], so expect that in the actual db call"
nl|'\n'
indent|'            '
name|'e_args'
op|'='
name|'tuple'
op|'('
op|'['
name|'args'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|']'
op|'+'
name|'list'
op|'('
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'security_group_get_by_instance'"
op|':'
newline|'\n'
indent|'            '
name|'e_args'
op|'='
name|'tuple'
op|'('
op|'['
name|'args'
op|'['
number|'0'
op|']'
op|'['
string|"'uuid'"
op|']'
op|']'
op|'+'
name|'list'
op|'('
name|'args'
op|'['
number|'1'
op|':'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'e_args'
op|'='
name|'args'
newline|'\n'
nl|'\n'
dedent|''
name|'getattr'
op|'('
name|'db'
op|','
name|'method'
op|')'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'*'
name|'e_args'
op|','
op|'**'
name|'kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|"'it worked'"
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
name|'result'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'virtapi'
op|','
name|'method'
op|')'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|"'it worked'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeCompute
dedent|''
dedent|''
name|'class'
name|'FakeCompute'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_api'
op|'='
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'='
name|'mox'
op|'.'
name|'MockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_events'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance_events'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_events'
op|'.'
name|'prepare_for_instance_event'
op|'.'
name|'side_effect'
op|'='
name|'self'
op|'.'
name|'_prepare_for_instance_event'
newline|'\n'
nl|'\n'
DECL|member|_event_waiter
dedent|''
name|'def'
name|'_event_waiter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'event'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'event'
op|'.'
name|'status'
op|'='
string|"'completed'"
newline|'\n'
name|'return'
name|'event'
newline|'\n'
nl|'\n'
DECL|member|_prepare_for_instance_event
dedent|''
name|'def'
name|'_prepare_for_instance_event'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'event_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'m'
op|'.'
name|'instance'
op|'='
name|'instance'
newline|'\n'
name|'m'
op|'.'
name|'event_name'
op|'='
name|'event_name'
newline|'\n'
name|'m'
op|'.'
name|'wait'
op|'.'
name|'side_effect'
op|'='
name|'self'
op|'.'
name|'_event_waiter'
newline|'\n'
name|'self'
op|'.'
name|'_events'
op|'.'
name|'append'
op|'('
name|'m'
op|')'
newline|'\n'
name|'return'
name|'m'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeVirtAPITest
dedent|''
dedent|''
name|'class'
name|'ComputeVirtAPITest'
op|'('
name|'VirtAPIBaseTest'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|cover_api
indent|'    '
name|'cover_api'
op|'='
name|'compute_manager'
op|'.'
name|'ComputeVirtAPI'
newline|'\n'
nl|'\n'
DECL|member|set_up_virtapi
name|'def'
name|'set_up_virtapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute'
op|'='
name|'FakeCompute'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'virtapi'
op|'='
name|'compute_manager'
op|'.'
name|'ComputeVirtAPI'
op|'('
name|'self'
op|'.'
name|'compute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertExpected
dedent|''
name|'def'
name|'assertExpected'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'conductor_api'
op|','
name|'method'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'conductor_api'
op|','
name|'method'
op|')'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'it worked'"
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
name|'result'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'virtapi'
op|','
name|'method'
op|')'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|"'it worked'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wait_for_instance_event
dedent|''
name|'def'
name|'test_wait_for_instance_event'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'and_i_ran'
op|'='
string|"''"
newline|'\n'
name|'event_1_tag'
op|'='
name|'objects'
op|'.'
name|'InstanceExternalEvent'
op|'.'
name|'make_key'
op|'('
nl|'\n'
string|"'event1'"
op|')'
newline|'\n'
name|'event_2_tag'
op|'='
name|'objects'
op|'.'
name|'InstanceExternalEvent'
op|'.'
name|'make_key'
op|'('
nl|'\n'
string|"'event2'"
op|','
string|"'tag'"
op|')'
newline|'\n'
name|'events'
op|'='
op|'{'
nl|'\n'
string|"'event1'"
op|':'
name|'event_1_tag'
op|','
nl|'\n'
op|'('
string|"'event2'"
op|','
string|"'tag'"
op|')'
op|':'
name|'event_2_tag'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'wait_for_instance_event'
op|'('
string|"'instance'"
op|','
name|'events'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'and_i_ran'
op|'='
string|"'I ran so far a-waa-y'"
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'I ran so far a-waa-y'"
op|','
name|'and_i_ran'
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
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_events'
op|')'
op|')'
newline|'\n'
name|'for'
name|'event'
name|'in'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_events'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'instance'"
op|','
name|'event'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'event'
op|'.'
name|'event_name'
op|','
name|'events'
op|'.'
name|'values'
op|'('
op|')'
op|')'
newline|'\n'
name|'event'
op|'.'
name|'wait'
op|'.'
name|'assert_called_once_with'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wait_for_instance_event_failed
dedent|''
dedent|''
name|'def'
name|'test_wait_for_instance_event_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_failer
indent|'        '
name|'def'
name|'_failer'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'event'
op|'.'
name|'status'
op|'='
string|"'failed'"
newline|'\n'
name|'return'
name|'event'
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
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'_compute'
op|','
string|"'_event_waiter'"
op|','
name|'_failer'
op|')'
newline|'\n'
DECL|function|do_test
name|'def'
name|'do_test'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'wait_for_instance_event'
op|'('
string|"'instance'"
op|','
op|'['
string|"'foo'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
name|'do_test'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wait_for_instance_event_failed_callback
dedent|''
name|'def'
name|'test_wait_for_instance_event_failed_callback'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|_failer
indent|'        '
name|'def'
name|'_failer'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'event'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'event'
op|'.'
name|'status'
op|'='
string|"'failed'"
newline|'\n'
name|'return'
name|'event'
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
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'_compute'
op|','
string|"'_event_waiter'"
op|','
name|'_failer'
op|')'
newline|'\n'
DECL|function|do_test
name|'def'
name|'do_test'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'callback'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'with'
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'wait_for_instance_event'
op|'('
string|"'instance'"
op|','
op|'['
string|"'foo'"
op|']'
op|','
nl|'\n'
name|'error_callback'
op|'='
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'callback'
op|'.'
name|'assert_called_with'
op|'('
string|"'foo'"
op|','
string|"'instance'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'do_test'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wait_for_instance_event_timeout
dedent|''
name|'def'
name|'test_wait_for_instance_event_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|TestException
indent|'        '
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
DECL|function|_failer
dedent|''
name|'def'
name|'_failer'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'TestException'
op|'('
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
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'_compute'
op|','
string|"'_event_waiter'"
op|','
name|'_failer'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'eventlet.timeout.Timeout'"
op|')'
newline|'\n'
DECL|function|do_test
name|'def'
name|'do_test'
op|'('
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'self'
op|'.'
name|'virtapi'
op|'.'
name|'wait_for_instance_event'
op|'('
string|"'instance'"
op|','
op|'['
string|"'foo'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TestException'
op|','
name|'do_test'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
