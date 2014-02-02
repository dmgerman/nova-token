begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""\nUnit Tests for nova.scheduler.rpcapi\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
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
nl|'\n'
nl|'\n'
DECL|class|SchedulerRpcAPITestCase
name|'class'
name|'SchedulerRpcAPITestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_test_scheduler_api
indent|'    '
name|'def'
name|'_test_scheduler_api'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'rpc_method'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake_project'"
op|')'
newline|'\n'
nl|'\n'
name|'rpcapi'
op|'='
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'target'
op|'.'
name|'topic'
op|','
name|'CONF'
op|'.'
name|'scheduler_topic'
op|')'
newline|'\n'
nl|'\n'
name|'expected_retval'
op|'='
string|"'foo'"
name|'if'
name|'method'
op|'=='
string|"'call'"
name|'else'
name|'None'
newline|'\n'
name|'expected_version'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'version'"
op|','
name|'None'
op|')'
newline|'\n'
name|'expected_fanout'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'fanout'"
op|','
name|'None'
op|')'
newline|'\n'
name|'expected_kwargs'
op|'='
name|'kwargs'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'rpcapi'
op|','
string|"'client'"
op|')'
newline|'\n'
nl|'\n'
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'str'
op|')'
op|')'
op|'.'
name|'MultipleTimes'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'prepare_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'expected_fanout'
op|':'
newline|'\n'
indent|'            '
name|'prepare_kwargs'
op|'['
string|"'fanout'"
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'expected_version'
op|':'
newline|'\n'
indent|'            '
name|'prepare_kwargs'
op|'['
string|"'version'"
op|']'
op|'='
name|'expected_version'
newline|'\n'
dedent|''
name|'if'
name|'prepare_kwargs'
op|':'
newline|'\n'
indent|'            '
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|'**'
name|'prepare_kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc_method'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|'.'
name|'client'
op|','
name|'rpc_method'
op|')'
newline|'\n'
nl|'\n'
name|'rpc_method'
op|'('
name|'ctxt'
op|','
name|'method'
op|','
op|'**'
name|'expected_kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'expected_retval'
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
comment|'# NOTE(markmc): MultipleTimes() is OnceOrMore() not ZeroOrMore()'
nl|'\n'
name|'rpcapi'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'I fool you mox'"
op|')'
newline|'\n'
nl|'\n'
name|'retval'
op|'='
name|'getattr'
op|'('
name|'rpcapi'
op|','
name|'method'
op|')'
op|'('
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retval'
op|','
name|'expected_retval'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_instance
dedent|''
name|'def'
name|'test_run_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'run_instance'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"'pw'"
op|','
name|'injected_files'
op|'='
string|"'fake_injected_files'"
op|','
nl|'\n'
name|'requested_networks'
op|'='
string|"'fake_requested_networks'"
op|','
nl|'\n'
name|'is_first_time'
op|'='
name|'True'
op|','
name|'filter_properties'
op|'='
string|"'fake_filter_properties'"
op|','
nl|'\n'
name|'legacy_bdm_in_spec'
op|'='
name|'False'
op|','
name|'version'
op|'='
string|"'2.9'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_prep_resize
dedent|''
name|'def'
name|'test_prep_resize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'prep_resize'"
op|','
name|'rpc_method'
op|'='
string|"'cast'"
op|','
nl|'\n'
name|'instance'
op|'='
string|"'fake_instance'"
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'fake_type'"
op|','
name|'image'
op|'='
string|"'fake_image'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'filter_properties'
op|'='
string|"'fake_props'"
op|','
name|'reservations'
op|'='
name|'list'
op|'('
string|"'fake_res'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_select_destinations
dedent|''
name|'def'
name|'test_select_destinations'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_scheduler_api'
op|'('
string|"'select_destinations'"
op|','
name|'rpc_method'
op|'='
string|"'call'"
op|','
nl|'\n'
name|'request_spec'
op|'='
string|"'fake_request_spec'"
op|','
nl|'\n'
name|'filter_properties'
op|'='
string|"'fake_prop'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'2.7'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
