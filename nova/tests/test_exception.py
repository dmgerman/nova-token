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
name|'import'
name|'inspect'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'gettextutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeNotifier
name|'class'
name|'FakeNotifier'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Acts like messaging.Notifier."""'
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
name|'provided_context'
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
name|'provided_payload'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|error
dedent|''
name|'def'
name|'error'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'event'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'provided_context'
op|'='
name|'context'
newline|'\n'
name|'self'
op|'.'
name|'provided_event'
op|'='
name|'event'
newline|'\n'
name|'self'
op|'.'
name|'provided_payload'
op|'='
name|'payload'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|good_function
dedent|''
dedent|''
name|'def'
name|'good_function'
op|'('
name|'self'
op|','
name|'context'
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
name|'self'
op|','
name|'context'
op|','
name|'extra'
op|','
name|'blah'
op|'='
string|'"a"'
op|','
name|'boo'
op|'='
string|'"b"'
op|','
name|'zoo'
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
name|'NoDBTestCase'
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
string|"'foo'"
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
number|'1'
op|','
number|'2'
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
number|'1'
op|','
name|'ctxt'
op|','
number|'3'
op|','
name|'zoo'
op|'='
number|'3'
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
name|'provided_context'
op|','
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'notifier'
op|'.'
name|'provided_payload'
op|'['
string|"'args'"
op|']'
op|'['
string|"'extra'"
op|']'
op|','
number|'3'
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
name|'assertIn'
op|'('
name|'key'
op|','
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
nl|'\n'
DECL|class|NovaExceptionTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaExceptionTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
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
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
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
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'message'
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
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
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
op|','
name|'mispelled_code'
op|'='
string|"'blah'"
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
string|"'default message: blah'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'message'
op|','
string|"'default message: blah'"
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
nl|'\n'
DECL|member|test_cleanse_dict
dedent|''
name|'def'
name|'test_cleanse_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
string|"'foo'"
op|':'
number|'1'
op|','
string|"'blah_pass'"
op|':'
number|'2'
op|','
string|"'zoo_password'"
op|':'
number|'3'
op|','
string|"'_pass'"
op|':'
number|'4'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exception'
op|'.'
name|'_cleanse_dict'
op|'('
name|'kwargs'
op|')'
op|','
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exception'
op|'.'
name|'_cleanse_dict'
op|'('
name|'kwargs'
op|')'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_message_local
dedent|''
name|'def'
name|'test_format_message_local'
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
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
op|'='
string|'"some message"'
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
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_message_remote
dedent|''
name|'def'
name|'test_format_message_remote'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException_Remote
indent|'        '
name|'class'
name|'FakeNovaException_Remote'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
op|'='
string|'"some message"'
newline|'\n'
nl|'\n'
DECL|member|__unicode__
name|'def'
name|'__unicode__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|'u"print the whole trace"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'exc'
op|'='
name|'FakeNovaException_Remote'
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
string|'u"print the whole trace"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|','
string|'"some message"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_message_remote_error
dedent|''
name|'def'
name|'test_format_message_remote_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNovaException_Remote
indent|'        '
name|'class'
name|'FakeNovaException_Remote'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
op|'='
string|'"some message %(somearg)s"'
newline|'\n'
nl|'\n'
DECL|member|__unicode__
name|'def'
name|'__unicode__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|'u"print the whole trace"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'fatal_exception_format_errors'
op|'='
name|'False'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'FakeNovaException_Remote'
op|'('
name|'lame_arg'
op|'='
string|"'lame'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|','
string|'"some message %(somearg)s"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_message_gettext_msg_returned
dedent|''
name|'def'
name|'test_format_message_gettext_msg_returned'
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
DECL|variable|msg_fmt
indent|'            '
name|'msg_fmt'
op|'='
name|'gettextutils'
op|'.'
name|'Message'
op|'('
string|'"Some message %(param)s"'
op|','
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'exc'
op|'='
name|'FakeNovaException'
op|'('
name|'param'
op|'='
string|"'blah'"
op|')'
newline|'\n'
name|'msg'
op|'='
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'msg'
op|','
name|'gettextutils'
op|'.'
name|'Message'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|','
string|'"Some message blah"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExceptionTestCase
dedent|''
dedent|''
name|'class'
name|'ExceptionTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_raise_exc
name|'def'
name|'_raise_exc'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exceptions_raise
dedent|''
name|'def'
name|'test_exceptions_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(dprince): disable format errors since we are not passing kwargs'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'fatal_exception_format_errors'
op|'='
name|'False'
op|')'
newline|'\n'
name|'for'
name|'name'
name|'in'
name|'dir'
op|'('
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'getattr'
op|'('
name|'exception'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'exc'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exc'
op|','
name|'self'
op|'.'
name|'_raise_exc'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExceptionValidMessageTestCase
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExceptionValidMessageTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_messages
indent|'    '
name|'def'
name|'test_messages'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'failures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'name'
op|','
name|'obj'
name|'in'
name|'inspect'
op|'.'
name|'getmembers'
op|'('
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
name|'in'
op|'['
string|"'NovaException'"
op|','
string|"'InstanceFaultRollback'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'inspect'
op|'.'
name|'isclass'
op|'('
name|'obj'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'issubclass'
op|'('
name|'obj'
op|','
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'e'
op|'='
name|'obj'
newline|'\n'
name|'if'
name|'e'
op|'.'
name|'msg_fmt'
op|'=='
string|'"An unknown exception occurred."'
op|':'
newline|'\n'
indent|'                '
name|'failures'
op|'.'
name|'append'
op|'('
string|"'%s needs a more specific msg_fmt'"
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'failures'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fail'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'failures'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
