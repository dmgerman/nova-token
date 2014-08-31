begin_unit
comment|'# Copyright (c) 2014 Red Hat, Inc.'
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'api'
name|'as'
name|'conductor_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'client'
name|'as'
name|'scheduler_client'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
string|'"""Tests for Scheduler Client."""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerClientTestCase
name|'class'
name|'SchedulerClientTestCase'
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
name|'SchedulerClientTestCase'
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
nl|'\n'
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
name|'self'
op|'.'
name|'client'
op|'='
name|'scheduler_client'
op|'.'
name|'SchedulerClient'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_constructor
dedent|''
name|'def'
name|'test_constructor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'self'
op|'.'
name|'client'
op|'.'
name|'conductor_api'
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
name|'conductor_api'
op|'.'
name|'LocalAPI'
op|','
string|"'compute_node_update'"
op|')'
newline|'\n'
DECL|member|test_update_compute_node_works
name|'def'
name|'test_update_compute_node_works'
op|'('
name|'self'
op|','
name|'mock_cn_update'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
op|'{'
string|'"id"'
op|':'
number|'1'
op|','
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'update_resource_stats'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'('
string|"'fakehost'"
op|','
string|"'fakenode'"
op|')'
op|','
nl|'\n'
name|'stats'
op|')'
newline|'\n'
name|'mock_cn_update'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|'"id"'
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_compute_node_raises
dedent|''
name|'def'
name|'test_update_compute_node_raises'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ComputeHostNotCreated'
op|','
nl|'\n'
name|'self'
op|'.'
name|'client'
op|'.'
name|'update_resource_stats'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'('
string|"'fakehost'"
op|','
string|"'fakenode'"
op|')'
op|','
name|'stats'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
