begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack, LLC'
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
string|'"""\nUnit Tests for \'common\' functons used through rpc code.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'sys'
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
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'amqp'
name|'as'
name|'rpc_amqp'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
name|'rpc'
name|'import'
name|'common'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|raise_exception
name|'def'
name|'raise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'Exception'
op|'('
string|'"test"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeUserDefinedException
dedent|''
name|'class'
name|'FakeUserDefinedException'
op|'('
name|'Exception'
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
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
string|'"Test Message"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RpcCommonTestCase
dedent|''
dedent|''
name|'class'
name|'RpcCommonTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_serialize_remote_exception
indent|'    '
name|'def'
name|'test_serialize_remote_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'Exception'"
op|','
nl|'\n'
string|"'module'"
op|':'
string|"'exceptions'"
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'test'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'raise_exception'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'failure'
op|'='
name|'rpc_common'
op|'.'
name|'serialize_remote_exception'
op|'('
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'failure'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'failure'
op|')'
newline|'\n'
comment|'#assure the traceback was added'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'class'"
op|']'
op|','
name|'failure'
op|'['
string|"'class'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'module'"
op|']'
op|','
name|'failure'
op|'['
string|"'module'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'message'"
op|']'
op|','
name|'failure'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_remote_nova_exception
dedent|''
name|'def'
name|'test_serialize_remote_nova_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|raise_nova_exception
indent|'        '
name|'def'
name|'raise_nova_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
string|'"test"'
op|','
name|'code'
op|'='
number|'500'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'NovaException'"
op|','
nl|'\n'
string|"'module'"
op|':'
string|"'nova.exception'"
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'code'"
op|':'
number|'500'
op|'}'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'test'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'raise_nova_exception'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'failure'
op|'='
name|'rpc_common'
op|'.'
name|'serialize_remote_exception'
op|'('
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'failure'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'failure'
op|')'
newline|'\n'
comment|'#assure the traceback was added'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'class'"
op|']'
op|','
name|'failure'
op|'['
string|"'class'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'module'"
op|']'
op|','
name|'failure'
op|'['
string|"'module'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'failure'
op|'['
string|"'kwargs'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'['
string|"'message'"
op|']'
op|','
name|'failure'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_remote_exception
dedent|''
name|'def'
name|'test_deserialize_remote_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'failure'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'NovaException'"
op|','
nl|'\n'
string|"'module'"
op|':'
string|"'nova.exception'"
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'test message'"
op|','
nl|'\n'
string|"'tb'"
op|':'
op|'['
string|"'raise NovaException'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serialized'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'failure'
op|')'
newline|'\n'
nl|'\n'
name|'after_exc'
op|'='
name|'rpc_common'
op|'.'
name|'deserialize_remote_exception'
op|'('
name|'FLAGS'
op|','
name|'serialized'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'after_exc'
op|','
name|'exception'
op|'.'
name|'NovaException'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'test message'"
name|'in'
name|'unicode'
op|'('
name|'after_exc'
op|')'
op|')'
newline|'\n'
comment|'#assure the traceback was added'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'raise NovaException'"
name|'in'
name|'unicode'
op|'('
name|'after_exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_remote_exception_bad_module
dedent|''
name|'def'
name|'test_deserialize_remote_exception_bad_module'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'failure'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'popen2'"
op|','
nl|'\n'
string|"'module'"
op|':'
string|"'os'"
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'cmd'"
op|':'
string|"'/bin/echo failed'"
op|'}'
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'foo'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serialized'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'failure'
op|')'
newline|'\n'
nl|'\n'
name|'after_exc'
op|'='
name|'rpc_common'
op|'.'
name|'deserialize_remote_exception'
op|'('
name|'FLAGS'
op|','
name|'serialized'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'after_exc'
op|','
name|'rpc_common'
op|'.'
name|'RemoteError'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_remote_exception_user_defined_exception
dedent|''
name|'def'
name|'test_deserialize_remote_exception_user_defined_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure a user defined exception can be deserialized."""'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'allowed_rpc_exception_modules'
op|'='
op|'['
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__module__'
op|']'
op|')'
newline|'\n'
name|'failure'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'FakeUserDefinedException'"
op|','
nl|'\n'
string|"'module'"
op|':'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__module__'
op|','
nl|'\n'
string|"'tb'"
op|':'
op|'['
string|"'raise FakeUserDefinedException'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serialized'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'failure'
op|')'
newline|'\n'
nl|'\n'
name|'after_exc'
op|'='
name|'rpc_common'
op|'.'
name|'deserialize_remote_exception'
op|'('
name|'FLAGS'
op|','
name|'serialized'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'after_exc'
op|','
name|'FakeUserDefinedException'
op|')'
op|')'
newline|'\n'
comment|'#assure the traceback was added'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'raise FakeUserDefinedException'"
name|'in'
name|'unicode'
op|'('
name|'after_exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize_remote_exception_cannot_recreate
dedent|''
name|'def'
name|'test_deserialize_remote_exception_cannot_recreate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure a RemoteError is returned on initialization failure.\n\n        If an exception cannot be recreated with it\'s original class then a\n        RemoteError with the exception informations should still be returned.\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'allowed_rpc_exception_modules'
op|'='
op|'['
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__module__'
op|']'
op|')'
newline|'\n'
name|'failure'
op|'='
op|'{'
nl|'\n'
string|"'class'"
op|':'
string|"'FakeIDontExistException'"
op|','
nl|'\n'
string|"'module'"
op|':'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__module__'
op|','
nl|'\n'
string|"'tb'"
op|':'
op|'['
string|"'raise FakeIDontExistException'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serialized'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'failure'
op|')'
newline|'\n'
nl|'\n'
name|'after_exc'
op|'='
name|'rpc_common'
op|'.'
name|'deserialize_remote_exception'
op|'('
name|'FLAGS'
op|','
name|'serialized'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'after_exc'
op|','
name|'rpc_common'
op|'.'
name|'RemoteError'
op|')'
op|')'
newline|'\n'
comment|'#assure the traceback was added'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'raise FakeIDontExistException'"
name|'in'
name|'unicode'
op|'('
name|'after_exc'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
