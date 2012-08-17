begin_unit
comment|'# Copyright (c) 2012 OpenStack, LLC'
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
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'instance_usage_audit_log'
name|'as'
name|'ial'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_COMPUTE_SERVICES
name|'TEST_COMPUTE_SERVICES'
op|'='
op|'['
name|'dict'
op|'('
name|'host'
op|'='
string|"'foo'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|"'bar'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|"'baz'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|"'plonk'"
op|','
name|'topic'
op|'='
string|"'compute'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|"'wibble'"
op|','
name|'topic'
op|'='
string|"'bogus'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|begin1
name|'begin1'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'7'
op|','
number|'4'
op|','
number|'6'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
name|'begin2'
op|'='
name|'end1'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'7'
op|','
number|'5'
op|','
number|'6'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
name|'begin3'
op|'='
name|'end2'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'7'
op|','
number|'6'
op|','
number|'6'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
DECL|variable|end3
name|'end3'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'7'
op|','
number|'7'
op|','
number|'6'
op|','
number|'0'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#test data'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_LOGS1
name|'TEST_LOGS1'
op|'='
op|'['
nl|'\n'
comment|'#all services done, no errors.'
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"plonk"'
op|','
name|'period_beginning'
op|'='
name|'begin1'
op|','
name|'period_ending'
op|'='
name|'end1'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'23'
op|','
name|'message'
op|'='
string|'"test1"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"baz"'
op|','
name|'period_beginning'
op|'='
name|'begin1'
op|','
name|'period_ending'
op|'='
name|'end1'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'17'
op|','
name|'message'
op|'='
string|'"test2"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"bar"'
op|','
name|'period_beginning'
op|'='
name|'begin1'
op|','
name|'period_ending'
op|'='
name|'end1'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'10'
op|','
name|'message'
op|'='
string|'"test3"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"foo"'
op|','
name|'period_beginning'
op|'='
name|'begin1'
op|','
name|'period_ending'
op|'='
name|'end1'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'7'
op|','
name|'message'
op|'='
string|'"test4"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_LOGS2
name|'TEST_LOGS2'
op|'='
op|'['
nl|'\n'
comment|'#some still running...'
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"plonk"'
op|','
name|'period_beginning'
op|'='
name|'begin2'
op|','
name|'period_ending'
op|'='
name|'end2'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'23'
op|','
name|'message'
op|'='
string|'"test5"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"baz"'
op|','
name|'period_beginning'
op|'='
name|'begin2'
op|','
name|'period_ending'
op|'='
name|'end2'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'17'
op|','
name|'message'
op|'='
string|'"test6"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"bar"'
op|','
name|'period_beginning'
op|'='
name|'begin2'
op|','
name|'period_ending'
op|'='
name|'end2'
op|','
nl|'\n'
name|'state'
op|'='
string|'"RUNNING"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'10'
op|','
name|'message'
op|'='
string|'"test7"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"foo"'
op|','
name|'period_beginning'
op|'='
name|'begin2'
op|','
name|'period_ending'
op|'='
name|'end2'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'7'
op|','
name|'message'
op|'='
string|'"test8"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_LOGS3
name|'TEST_LOGS3'
op|'='
op|'['
nl|'\n'
comment|'#some errors..'
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"plonk"'
op|','
name|'period_beginning'
op|'='
name|'begin3'
op|','
name|'period_ending'
op|'='
name|'end3'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'23'
op|','
name|'message'
op|'='
string|'"test9"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"baz"'
op|','
name|'period_beginning'
op|'='
name|'begin3'
op|','
name|'period_ending'
op|'='
name|'end3'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'2'
op|','
name|'task_items'
op|'='
number|'17'
op|','
name|'message'
op|'='
string|'"test10"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"bar"'
op|','
name|'period_beginning'
op|'='
name|'begin3'
op|','
name|'period_ending'
op|'='
name|'end3'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'0'
op|','
name|'task_items'
op|'='
number|'10'
op|','
name|'message'
op|'='
string|'"test11"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'host'
op|'='
string|'"foo"'
op|','
name|'period_beginning'
op|'='
name|'begin3'
op|','
name|'period_ending'
op|'='
name|'end3'
op|','
nl|'\n'
name|'state'
op|'='
string|'"DONE"'
op|','
name|'errors'
op|'='
number|'1'
op|','
name|'task_items'
op|'='
number|'7'
op|','
name|'message'
op|'='
string|'"test12"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_service_get_all
name|'def'
name|'fake_service_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'TEST_COMPUTE_SERVICES'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_task_log_get_all
dedent|''
name|'def'
name|'fake_task_log_get_all'
op|'('
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'assert'
name|'task_name'
op|'=='
string|'"instance_usage_audit"'
newline|'\n'
nl|'\n'
name|'if'
name|'begin'
op|'=='
name|'begin1'
name|'and'
name|'end'
op|'=='
name|'end1'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'TEST_LOGS1'
newline|'\n'
dedent|''
name|'if'
name|'begin'
op|'=='
name|'begin2'
name|'and'
name|'end'
op|'=='
name|'end2'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'TEST_LOGS2'
newline|'\n'
dedent|''
name|'if'
name|'begin'
op|'=='
name|'begin3'
name|'and'
name|'end'
op|'=='
name|'end3'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'TEST_LOGS3'
newline|'\n'
dedent|''
name|'raise'
name|'AssertionError'
op|'('
string|'"Invalid date %s to %s"'
op|'%'
op|'('
name|'begin'
op|','
name|'end'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_last_completed_audit_period
dedent|''
name|'def'
name|'fake_last_completed_audit_period'
op|'('
name|'unit'
op|'='
name|'None'
op|','
name|'before'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'audit_periods'
op|'='
op|'['
op|'('
name|'begin3'
op|','
name|'end3'
op|')'
op|','
nl|'\n'
op|'('
name|'begin2'
op|','
name|'end2'
op|')'
op|','
nl|'\n'
op|'('
name|'begin1'
op|','
name|'end1'
op|')'
op|']'
newline|'\n'
name|'if'
name|'before'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'begin'
op|','
name|'end'
name|'in'
name|'audit_periods'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'before'
op|'>'
name|'end'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'begin'
op|','
name|'end'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'AssertionError'
op|'('
string|'"Invalid before date %s"'
op|'%'
op|'('
name|'before'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'begin1'
op|','
name|'end1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceUsageAuditLogTest
dedent|''
name|'class'
name|'InstanceUsageAuditLogTest'
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
name|'super'
op|'('
name|'InstanceUsageAuditLogTest'
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
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'7'
op|','
number|'5'
op|','
number|'10'
op|','
number|'0'
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'ial'
op|'.'
name|'InstanceUsageAuditLogController'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'last_completed_audit_period'"
op|','
nl|'\n'
name|'fake_last_completed_audit_period'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'service_get_all'"
op|','
nl|'\n'
name|'fake_service_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'task_log_get_all'"
op|','
nl|'\n'
name|'fake_task_log_get_all'
op|')'
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
name|'super'
op|'('
name|'InstanceUsageAuditLogTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'timeutils'
op|'.'
name|'clear_time_override'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-instance_usage_audit_log'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'instance_usage_audit_logs'"
op|','
name|'result'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'result'
op|'['
string|"'instance_usage_audit_logs'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'57'
op|','
name|'logs'
op|'['
string|"'total_instances'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'total_errors'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'logs'
op|'['
string|"'log'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts_done'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_running'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_not_run'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"ALL hosts done. 0 errors."'
op|','
name|'logs'
op|'['
string|"'overall_status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-instance_usage_audit_log/show'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'2012-07-05 10:00:00'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'instance_usage_audit_log'"
op|','
name|'result'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'result'
op|'['
string|"'instance_usage_audit_log'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'57'
op|','
name|'logs'
op|'['
string|"'total_instances'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'total_errors'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'logs'
op|'['
string|"'log'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts_done'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_running'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_not_run'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"ALL hosts done. 0 errors."'
op|','
name|'logs'
op|'['
string|"'overall_status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_with_running
dedent|''
name|'def'
name|'test_show_with_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-instance_usage_audit_log/show'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'2012-07-06 10:00:00'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'instance_usage_audit_log'"
op|','
name|'result'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'result'
op|'['
string|"'instance_usage_audit_log'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'57'
op|','
name|'logs'
op|'['
string|"'total_instances'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'total_errors'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'logs'
op|'['
string|"'log'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'3'
op|','
name|'logs'
op|'['
string|"'num_hosts_done'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'logs'
op|'['
string|"'num_hosts_running'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_not_run'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"3 of 4 hosts done. 0 errors."'
op|','
nl|'\n'
name|'logs'
op|'['
string|"'overall_status'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_with_errors
dedent|''
name|'def'
name|'test_show_with_errors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake/os-instance_usage_audit_log/show'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'2012-07-07 10:00:00'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'instance_usage_audit_log'"
op|','
name|'result'
op|')'
newline|'\n'
name|'logs'
op|'='
name|'result'
op|'['
string|"'instance_usage_audit_log'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'57'
op|','
name|'logs'
op|'['
string|"'total_instances'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'3'
op|','
name|'logs'
op|'['
string|"'total_errors'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'len'
op|'('
name|'logs'
op|'['
string|"'log'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'4'
op|','
name|'logs'
op|'['
string|"'num_hosts_done'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_running'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'logs'
op|'['
string|"'num_hosts_not_run'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"ALL hosts done. 3 errors."'
op|','
nl|'\n'
name|'logs'
op|'['
string|"'overall_status'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
