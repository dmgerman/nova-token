begin_unit
comment|'# Copyright (c) 2013 Akira Yoshiyama <akirayoshiyama at gmail dot com>'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# This is derived from test_db_servicegroup.py.'
nl|'\n'
comment|'# Copyright 2012 IBM Corp.'
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
name|'import'
name|'servicegroup'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MemcachedServiceGroupTestCase
name|'class'
name|'MemcachedServiceGroupTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.cache_utils.get_memcached_client'"
op|')'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|','
name|'mgc_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MemcachedServiceGroupTestCase'
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
name|'mc_client'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mgc_mock'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'mc_client'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'memcached_servers'
op|'='
string|"'ignored'"
op|','
nl|'\n'
name|'servicegroup_driver'
op|'='
string|"'mc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_up
dedent|''
name|'def'
name|'test_is_up'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service_ref'
op|'='
op|'{'
nl|'\n'
string|"'host'"
op|':'
string|"'fake-host'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'compute'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'get'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'get'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'compute:fake-host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'get'
op|'.'
name|'return_value'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service_ref'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'get'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'compute:fake-host'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_join
dedent|''
name|'def'
name|'test_join'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'report_interval'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'join'
op|'('
string|"'fake-host'"
op|','
string|"'fake-topic'"
op|','
name|'service'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
newline|'\n'
name|'service'
op|'.'
name|'tg'
op|'.'
name|'add_timer'
op|'.'
name|'assert_called_once_with'
op|'('
number|'1'
op|','
name|'fn'
op|','
number|'5'
op|','
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_state
dedent|''
name|'def'
name|'test_report_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service_ref'
op|'='
op|'{'
nl|'\n'
string|"'host'"
op|':'
string|"'fake-host'"
op|','
nl|'\n'
string|"'topic'"
op|':'
string|"'compute'"
nl|'\n'
op|'}'
newline|'\n'
name|'service'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'model_disconnected'
op|'='
name|'False'
op|','
nl|'\n'
name|'service_ref'
op|'='
name|'service_ref'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'_driver'
op|'.'
name|'_report_state'
newline|'\n'
name|'fn'
op|'('
name|'service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mc_client'
op|'.'
name|'set'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'compute:fake-host'"
op|','
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
