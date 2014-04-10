begin_unit
comment|'# Copyright 2011 Eldar Nugaev'
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
name|'string'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
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
name|'jsonutils'
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
nl|'\n'
nl|'\n'
DECL|function|fake_get_console_output
name|'def'
name|'fake_get_console_output'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'_instance'
op|','
name|'tail_length'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fixture'
op|'='
op|'['
name|'str'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'tail_length'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'elif'
name|'tail_length'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'fixture'
op|'['
op|'-'
name|'int'
op|'('
name|'tail_length'
op|')'
op|':'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_console_output_not_ready
dedent|''
name|'def'
name|'fake_get_console_output_not_ready'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'_instance'
op|','
name|'tail_length'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotReady'
op|'('
name|'instance_id'
op|'='
name|'_instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_console_output_all_characters
dedent|''
name|'def'
name|'fake_get_console_output_all_characters'
op|'('
name|'self'
op|','
name|'_ctx'
op|','
name|'_instance'
op|','
name|'_tail_len'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'string'
op|'.'
name|'printable'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get
dedent|''
name|'def'
name|'fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'expected_attrs'
op|'='
name|'None'
op|','
nl|'\n'
name|'want_objects'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_not_found
dedent|''
name|'def'
name|'fake_get_not_found'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleOutputExtensionTest
dedent|''
name|'class'
name|'ConsoleOutputExtensionTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|application_type
indent|'    '
name|'application_type'
op|'='
string|'"application/json"'
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
name|'ConsoleOutputExtensionTest'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_console_output'"
op|','
nl|'\n'
name|'fake_get_console_output'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app_v3'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
nl|'\n'
string|"'os-console-output'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_request
dedent|''
name|'def'
name|'_create_request'
op|'('
name|'self'
op|','
name|'length_dict'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'get_console_output'"
op|':'
name|'length_dict'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/1/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
name|'self'
op|'.'
name|'application_type'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
DECL|member|test_get_text_console_instance_action
dedent|''
name|'def'
name|'test_get_text_console_instance_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'output'"
op|':'
string|"'0\\n1\\n2\\n3\\n4'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_tail
dedent|''
name|'def'
name|'test_get_console_output_with_tail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
number|'3'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'output'"
op|':'
string|"'2\\n3\\n4'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_length_as_str
dedent|''
name|'def'
name|'test_get_console_output_with_length_as_str'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
string|"'3'"
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'output'"
op|':'
string|"'2\\n3\\n4'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_unlimited_length
dedent|''
name|'def'
name|'test_get_console_output_with_unlimited_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'output'"
op|':'
string|"'0\\n1\\n2\\n3\\n4'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_unlimited_length_as_str
dedent|''
name|'def'
name|'test_get_console_output_with_unlimited_length_as_str'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
string|"'-1'"
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
op|'{'
string|"'output'"
op|':'
string|"'0\\n1\\n2\\n3\\n4'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_non_integer_length
dedent|''
name|'def'
name|'test_get_console_output_with_non_integer_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
string|"'NaN'"
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_text_console_no_instance
dedent|''
name|'def'
name|'test_get_text_console_no_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get_not_found'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_text_console_bad_body
dedent|''
name|'def'
name|'test_get_text_console_bad_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/v3/servers/1/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
name|'self'
op|'.'
name|'application_type'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_not_ready
dedent|''
name|'def'
name|'test_get_console_output_not_ready'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_console_output'"
op|','
nl|'\n'
name|'fake_get_console_output_not_ready'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
number|'3'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_length_as_float
dedent|''
name|'def'
name|'test_get_console_output_with_length_as_float'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
number|'2.5'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_not_implemented
dedent|''
name|'def'
name|'test_get_console_output_not_implemented'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_console_output'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_not_implemented'
op|')'
newline|'\n'
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'501'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_small_length
dedent|''
name|'def'
name|'test_get_console_output_with_small_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
op|'-'
number|'2'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_output_with_boolean_length
dedent|''
name|'def'
name|'test_get_console_output_with_boolean_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'self'
op|'.'
name|'_create_request'
op|'('
name|'length_dict'
op|'='
op|'{'
string|"'length'"
op|':'
name|'True'
op|'}'
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
