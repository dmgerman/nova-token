begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nTests For PickledScheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'scheduler_options'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSchedulerOptions
name|'class'
name|'FakeSchedulerOptions'
op|'('
name|'scheduler_options'
op|'.'
name|'SchedulerOptions'
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
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
name|'data'
op|','
name|'filedata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSchedulerOptions'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
comment|'# Change internals ...'
nl|'\n'
name|'self'
op|'.'
name|'last_modified'
op|'='
name|'file_old'
newline|'\n'
name|'self'
op|'.'
name|'last_checked'
op|'='
name|'last_checked'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
name|'data'
newline|'\n'
nl|'\n'
comment|'# For overrides ...'
nl|'\n'
name|'self'
op|'.'
name|'_time_now'
op|'='
name|'now'
newline|'\n'
name|'self'
op|'.'
name|'_file_now'
op|'='
name|'file_now'
newline|'\n'
name|'self'
op|'.'
name|'_file_data'
op|'='
name|'filedata'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'file_was_loaded'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_get_file_timestamp
dedent|''
name|'def'
name|'_get_file_timestamp'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_file_now'
newline|'\n'
nl|'\n'
DECL|member|_get_file_handle
dedent|''
name|'def'
name|'_get_file_handle'
op|'('
name|'self'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'file_was_loaded'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
name|'self'
op|'.'
name|'_file_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_time_now
dedent|''
name|'def'
name|'_get_time_now'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_time_now'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerOptionsTestCase
dedent|''
dedent|''
name|'class'
name|'SchedulerOptionsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_configuration_first_time_no_flag
indent|'    '
name|'def'
name|'test_get_configuration_first_time_no_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'None'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'None'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'1'
op|','
name|'b'
op|'='
number|'2'
op|','
name|'c'
op|'='
number|'3'
op|')'
newline|'\n'
name|'jdata'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_configuration_first_time_empty_file
dedent|''
name|'def'
name|'test_get_configuration_first_time_empty_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'None'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'None'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'jdata'
op|'='
string|'""'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
string|"'foo.json'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_configuration_first_time_happy_day
dedent|''
name|'def'
name|'test_get_configuration_first_time_happy_day'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'None'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'None'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'1'
op|','
name|'b'
op|'='
number|'2'
op|','
name|'c'
op|'='
number|'3'
op|')'
newline|'\n'
name|'jdata'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
op|'{'
op|'}'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
string|"'foo.json'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_configuration_second_time_no_change
dedent|''
name|'def'
name|'test_get_configuration_second_time_no_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'1'
op|','
name|'b'
op|'='
number|'2'
op|','
name|'c'
op|'='
number|'3'
op|')'
newline|'\n'
name|'jdata'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
name|'data'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
string|"'foo.json'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_configuration_second_time_too_fast
dedent|''
name|'def'
name|'test_get_configuration_second_time_too_fast'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'2'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'old_data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'1'
op|','
name|'b'
op|'='
number|'2'
op|','
name|'c'
op|'='
number|'3'
op|')'
newline|'\n'
name|'data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'11'
op|','
name|'b'
op|'='
number|'12'
op|','
name|'c'
op|'='
number|'13'
op|')'
newline|'\n'
name|'jdata'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
name|'old_data'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'old_data'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
string|"'foo.json'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_configuration_second_time_change
dedent|''
name|'def'
name|'test_get_configuration_second_time_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'last_checked'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_old'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'file_now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2013'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'old_data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'1'
op|','
name|'b'
op|'='
number|'2'
op|','
name|'c'
op|'='
number|'3'
op|')'
newline|'\n'
name|'data'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
number|'11'
op|','
name|'b'
op|'='
number|'12'
op|','
name|'c'
op|'='
number|'13'
op|')'
newline|'\n'
name|'jdata'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'='
name|'FakeSchedulerOptions'
op|'('
name|'last_checked'
op|','
name|'now'
op|','
name|'file_old'
op|','
name|'file_now'
op|','
nl|'\n'
name|'old_data'
op|','
name|'jdata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|','
name|'fake'
op|'.'
name|'get_configuration'
op|'('
string|"'foo.json'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'fake'
op|'.'
name|'file_was_loaded'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
