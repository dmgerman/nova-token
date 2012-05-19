begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EC2APIErrorTestCase
name|'class'
name|'EC2APIErrorTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_return_valid_error
indent|'    '
name|'def'
name|'test_return_valid_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# without 'code' arg"
nl|'\n'
indent|'        '
name|'err'
op|'='
name|'exception'
op|'.'
name|'EC2APIError'
op|'('
string|"'fake error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'__str__'
op|'('
op|')'
op|','
string|"'fake error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'code'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'msg'
op|','
string|"'fake error'"
op|')'
newline|'\n'
comment|"# with 'code' arg"
nl|'\n'
name|'err'
op|'='
name|'exception'
op|'.'
name|'EC2APIError'
op|'('
string|"'fake error'"
op|','
string|"'blah code'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'__str__'
op|'('
op|')'
op|','
string|"'blah code: fake error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'code'
op|','
string|"'blah code'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'err'
op|'.'
name|'msg'
op|','
string|"'fake error'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNotifier
dedent|''
dedent|''
name|'class'
name|'FakeNotifier'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Acts like the nova.notifier.api module."""'
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
number|'88'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'provided_publisher'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'provided_event'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'provided_priority'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'provided_payload'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'publisher'
op|','
name|'event'
op|','
name|'priority'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'provided_publisher'
op|'='
name|'publisher'
newline|'\n'
name|'self'
op|'.'
name|'provided_event'
op|'='
name|'event'
newline|'\n'
name|'self'
op|'.'
name|'provided_priority'
op|'='
name|'priority'
newline|'\n'
name|'self'
op|'.'
name|'provided_payload'
op|'='
name|'payload'
newline|'\n'
name|'self'
op|'.'
name|'provided_context'
op|'='
name|'context'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|good_function
dedent|''
dedent|''
name|'def'
name|'good_function'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
number|'99'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bad_function_exception
dedent|''
name|'def'
name|'bad_function_exception'
op|'('
name|'blah'
op|'='
string|'"a"'
op|','
name|'boo'
op|'='
string|'"b"'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'test'
op|'.'
name|'TestingException'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WrapExceptionTestCase
dedent|''
name|'class'
name|'WrapExceptionTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_wrap_exception_good_return
indent|'    '
name|'def'
name|'test_wrap_exception_good_return'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'wrapped'
op|'='
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'99'
op|','
name|'wrapped'
op|'('
name|'good_function'
op|')'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wrap_exception_throws_exception
dedent|''
name|'def'
name|'test_wrap_exception_throws_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'wrapped'
op|'='
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
nl|'\n'
name|'wrapped'
op|'('
name|'bad_function_exception'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wrap_exception_with_notifier
dedent|''
name|'def'
name|'test_wrap_exception_with_notifier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifier'
op|'='
name|'FakeNotifier'
op|'('
op|')'
newline|'\n'
name|'wrapped'
op|'='
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
name|'notifier'
op|','
string|'"publisher"'
op|','
string|'"event"'
op|','
nl|'\n'
string|'"level"'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
nl|'\n'
name|'wrapped'
op|'('
name|'bad_function_exception'
op|')'
op|','
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_publisher'
op|','
string|'"publisher"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_event'
op|','
string|'"event"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_priority'
op|','
string|'"level"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_context'
op|','
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
op|'['
string|"'exception'"
op|','
string|"'args'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'key'
name|'in'
name|'notifier'
op|'.'
name|'provided_payload'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wrap_exception_with_notifier_defaults
dedent|''
dedent|''
name|'def'
name|'test_wrap_exception_with_notifier_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifier'
op|'='
name|'FakeNotifier'
op|'('
op|')'
newline|'\n'
name|'wrapped'
op|'='
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
name|'notifier'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|','
nl|'\n'
name|'wrapped'
op|'('
name|'bad_function_exception'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_publisher'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_event'
op|','
string|'"bad_function_exception"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_priority'
op|','
name|'notifier'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaExceptionTestCase
dedent|''
dedent|''
name|'class'
name|'NovaExceptionTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_default_error_msg
indent|'    '
name|'def'
name|'test_default_error_msg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException
indent|'        '
name|'class'
name|'FakeNovaException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'            '
name|'message'
op|'='
string|'"default message"'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'unicode'
op|'('
name|'exc'
op|')'
op|','
string|"'default message'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_error_msg
dedent|''
name|'def'
name|'test_error_msg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'unicode'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|'('
string|"'test'"
op|')'
op|')'
op|','
nl|'\n'
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_error_msg_with_kwargs
dedent|''
name|'def'
name|'test_default_error_msg_with_kwargs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException
indent|'        '
name|'class'
name|'FakeNovaException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'            '
name|'message'
op|'='
string|'"default message: %(code)s"'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
name|'code'
op|'='
number|'500'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'unicode'
op|'('
name|'exc'
op|')'
op|','
string|"'default message: 500'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_error_msg_exception_with_kwargs
dedent|''
name|'def'
name|'test_error_msg_exception_with_kwargs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException
indent|'        '
name|'class'
name|'FakeNovaException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'            '
name|'message'
op|'='
string|'"default message: %(mispelled_code)s"'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
name|'code'
op|'='
number|'500'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'unicode'
op|'('
name|'exc'
op|')'
op|','
string|"'default message: %(mispelled_code)s'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_default_error_code
dedent|''
name|'def'
name|'test_default_error_code'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException
indent|'        '
name|'class'
name|'FakeNovaException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|code
indent|'            '
name|'code'
op|'='
number|'404'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'kwargs'
op|'['
string|"'code'"
op|']'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_error_code_from_kwarg
dedent|''
name|'def'
name|'test_error_code_from_kwarg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException
indent|'        '
name|'class'
name|'FakeNovaException'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|code
indent|'            '
name|'code'
op|'='
number|'500'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
name|'code'
op|'='
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'kwargs'
op|'['
string|"'code'"
op|']'
op|','
number|'404'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
