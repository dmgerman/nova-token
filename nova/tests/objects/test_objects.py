begin_unit
comment|'#    Copyright 2013 IBM Corp.'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'iso8601'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|')'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'rpcapi'
name|'as'
name|'conductor_rpcapi'
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
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'utils'
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
nl|'\n'
nl|'\n'
DECL|class|MyObj
name|'class'
name|'MyObj'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|version
indent|'    '
name|'version'
op|'='
string|"'1.5'"
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
string|"'foo'"
op|':'
name|'int'
op|','
nl|'\n'
string|"'bar'"
op|':'
name|'str'
op|','
nl|'\n'
string|"'missing'"
op|':'
name|'str'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|obj_load
name|'def'
name|'obj_load'
op|'('
name|'self'
op|','
name|'attrname'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'setattr'
op|'('
name|'self'
op|','
name|'attrname'
op|','
string|"'loaded!'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'1'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
string|"'bar'"
newline|'\n'
name|'obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'obj'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|marco
name|'def'
name|'marco'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'polo'"
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|update_test
name|'def'
name|'update_test'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'context'
op|'.'
name|'project_id'
op|'=='
string|"'alternate'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'bar'
op|'='
string|"'alternate-context'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'bar'
op|'='
string|"'updated'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|save
name|'def'
name|'save'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|refresh
name|'def'
name|'refresh'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'foo'
op|'='
number|'321'
newline|'\n'
name|'self'
op|'.'
name|'bar'
op|'='
string|"'refreshed'"
newline|'\n'
name|'self'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|modify_save_modify
name|'def'
name|'modify_save_modify'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'bar'
op|'='
string|"'meow'"
newline|'\n'
name|'self'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'foo'
op|'='
number|'42'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MyObj2
dedent|''
dedent|''
name|'class'
name|'MyObj2'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_name
name|'def'
name|'obj_name'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'MyObj'"
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get
name|'def'
name|'get'
op|'('
name|'cls'
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
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestMetaclass
dedent|''
dedent|''
name|'class'
name|'TestMetaclass'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_obj_tracking
indent|'    '
name|'def'
name|'test_obj_tracking'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|NewBaseClass
indent|'        '
name|'class'
name|'NewBaseClass'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|__metaclass__
indent|'            '
name|'__metaclass__'
op|'='
name|'base'
op|'.'
name|'NovaObjectMetaclass'
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|obj_name
name|'def'
name|'obj_name'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'cls'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
DECL|class|Test1
dedent|''
dedent|''
name|'class'
name|'Test1'
op|'('
name|'NewBaseClass'
op|')'
op|':'
newline|'\n'
indent|'            '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|obj_name
name|'def'
name|'obj_name'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'fake1'"
newline|'\n'
nl|'\n'
DECL|class|Test2
dedent|''
dedent|''
name|'class'
name|'Test2'
op|'('
name|'NewBaseClass'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|Test2v2
dedent|''
name|'class'
name|'Test2v2'
op|'('
name|'NewBaseClass'
op|')'
op|':'
newline|'\n'
indent|'            '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|obj_name
name|'def'
name|'obj_name'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'Test2'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'expected'
op|'='
op|'{'
string|"'fake1'"
op|':'
op|'['
name|'Test1'
op|']'
op|','
string|"'Test2'"
op|':'
op|'['
name|'Test2'
op|','
name|'Test2v2'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'NewBaseClass'
op|'.'
name|'_obj_classes'
op|')'
newline|'\n'
comment|'# The following should work, also.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'Test1'
op|'.'
name|'_obj_classes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'Test2'
op|'.'
name|'_obj_classes'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestUtils
dedent|''
dedent|''
name|'class'
name|'TestUtils'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_datetime_or_none
indent|'    '
name|'def'
name|'test_datetime_or_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'naive_dt'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
newline|'\n'
name|'dt'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'naive_dt'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_none'
op|'('
name|'dt'
op|')'
op|','
name|'dt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_none'
op|'('
name|'dt'
op|')'
op|','
nl|'\n'
name|'naive_dt'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|','
nl|'\n'
name|'microsecond'
op|'='
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_none'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'utils'
op|'.'
name|'datetime_or_none'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_datetime_or_str_or_none
dedent|''
name|'def'
name|'test_datetime_or_str_or_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dts'
op|'='
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
newline|'\n'
name|'dt'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'dts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_str_or_none'
op|'('
name|'dt'
op|')'
op|','
name|'dt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_str_or_none'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'datetime_or_str_or_none'
op|'('
name|'dts'
op|')'
op|','
name|'dt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'utils'
op|'.'
name|'datetime_or_str_or_none'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_int_or_none
dedent|''
name|'def'
name|'test_int_or_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'int_or_none'
op|'('
number|'1'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'int_or_none'
op|'('
string|"'1'"
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'int_or_none'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'utils'
op|'.'
name|'int_or_none'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_str_or_none
dedent|''
name|'def'
name|'test_str_or_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|Obj
indent|'        '
name|'class'
name|'Obj'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'str_or_none'
op|'('
string|"'foo'"
op|')'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'str_or_none'
op|'('
number|'1'
op|')'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'str_or_none'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ip_or_none
dedent|''
name|'def'
name|'test_ip_or_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip4'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|','
number|'4'
op|')'
newline|'\n'
name|'ip6'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1::2'"
op|','
number|'6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'4'
op|')'
op|'('
string|"'1.2.3.4'"
op|')'
op|','
name|'ip4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'6'
op|')'
op|'('
string|"'1::2'"
op|')'
op|','
name|'ip6'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'4'
op|')'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'6'
op|')'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|','
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'4'
op|')'
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|','
name|'utils'
op|'.'
name|'ip_or_none'
op|'('
number|'6'
op|')'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dt_serializer
dedent|''
name|'def'
name|'test_dt_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|Obj
indent|'        '
name|'class'
name|'Obj'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|foo
indent|'            '
name|'foo'
op|'='
name|'utils'
op|'.'
name|'dt_serializer'
op|'('
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'obj'
op|'='
name|'Obj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
string|"'1955-11-05T00:00:00Z'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|'('
op|')'
op|','
string|"'1955-11-05T00:00:00Z'"
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|'('
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
string|"'foo'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
name|'obj'
op|'.'
name|'foo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dt_deserializer
dedent|''
name|'def'
name|'test_dt_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dt'
op|'='
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
string|"'1955-11-05T00:00:00Z'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'dt_deserializer'
op|'('
name|'None'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'dt'
op|')'
op|')'
op|','
nl|'\n'
name|'dt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'utils'
op|'.'
name|'dt_deserializer'
op|'('
name|'None'
op|','
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'utils'
op|'.'
name|'dt_deserializer'
op|','
name|'None'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_BaseTestCase
dedent|''
dedent|''
name|'class'
name|'_BaseTestCase'
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
name|'_BaseTestCase'
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
name|'remote_object_calls'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_LocalTest
dedent|''
dedent|''
name|'class'
name|'_LocalTest'
op|'('
name|'_BaseTestCase'
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
name|'_LocalTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|'# Just in case'
nl|'\n'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|assertRemotes
dedent|''
name|'def'
name|'assertRemotes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'remote_object_calls'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|function|things_temporarily_local
name|'def'
name|'things_temporarily_local'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Temporarily go non-remote so the conductor handles'
nl|'\n'
comment|'# this request directly'
nl|'\n'
indent|'    '
name|'_api'
op|'='
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
newline|'\n'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'None'
newline|'\n'
name|'yield'
newline|'\n'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'_api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_RemoteTest
dedent|''
name|'class'
name|'_RemoteTest'
op|'('
name|'_BaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_testable_conductor
indent|'    '
name|'def'
name|'_testable_conductor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_service'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
nl|'\n'
string|"'conductor'"
op|','
name|'manager'
op|'='
string|"'nova.conductor.manager.ConductorManager'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remote_object_calls'
op|'='
name|'list'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'orig_object_class_action'
op|'='
name|'self'
op|'.'
name|'conductor_service'
op|'.'
name|'manager'
op|'.'
name|'object_class_action'
newline|'\n'
name|'orig_object_action'
op|'='
name|'self'
op|'.'
name|'conductor_service'
op|'.'
name|'manager'
op|'.'
name|'object_action'
newline|'\n'
nl|'\n'
DECL|function|fake_object_class_action
name|'def'
name|'fake_object_class_action'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'remote_object_calls'
op|'.'
name|'append'
op|'('
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'objname'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'objmethod'"
op|')'
op|')'
op|')'
newline|'\n'
name|'with'
name|'things_temporarily_local'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'orig_object_class_action'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'conductor_service'
op|'.'
name|'manager'
op|','
string|"'object_class_action'"
op|','
nl|'\n'
name|'fake_object_class_action'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_object_action
name|'def'
name|'fake_object_action'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'remote_object_calls'
op|'.'
name|'append'
op|'('
op|'('
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'objinst'"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'objmethod'"
op|')'
op|')'
op|')'
newline|'\n'
name|'with'
name|'things_temporarily_local'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'orig_object_action'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'conductor_service'
op|'.'
name|'manager'
op|','
string|"'object_action'"
op|','
nl|'\n'
name|'fake_object_action'
op|')'
newline|'\n'
nl|'\n'
comment|'# Things are remoted by default in this session'
nl|'\n'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'indirection_api'
op|'='
name|'conductor_rpcapi'
op|'.'
name|'ConductorAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'_RemoteTest'
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
name|'_testable_conductor'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertRemotes
dedent|''
name|'def'
name|'assertRemotes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'self'
op|'.'
name|'remote_object_calls'
op|','
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestObject
dedent|''
dedent|''
name|'class'
name|'_TestObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|test_hydration_type_error
indent|'    '
name|'def'
name|'test_hydration_type_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'primitive'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
op|'{'
string|"'foo'"
op|':'
string|"'a'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'MyObj'
op|'.'
name|'obj_from_primitive'
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydration
dedent|''
name|'def'
name|'test_hydration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'primitive'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'obj_from_primitive'
op|'('
name|'primitive'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_hydration_bad_ns
dedent|''
name|'def'
name|'test_hydration_bad_ns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'primitive'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'UnsupportedObjectError'
op|','
nl|'\n'
name|'MyObj'
op|'.'
name|'obj_from_primitive'
op|','
name|'primitive'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dehydration
dedent|''
name|'def'
name|'test_dehydration'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'1'
newline|'\n'
name|'obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_object_property
dedent|''
name|'def'
name|'test_object_property'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_object_property_type_error
dedent|''
name|'def'
name|'test_object_property_type_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fail
name|'def'
name|'fail'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'obj'
op|'.'
name|'foo'
op|'='
string|"'a'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'fail'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_object_dict_syntax
dedent|''
name|'def'
name|'test_object_dict_syntax'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'123'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
string|"'bar'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'['
string|"'foo'"
op|']'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sorted'
op|'('
name|'obj'
op|'.'
name|'items'
op|'('
op|')'
op|','
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
name|'x'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
op|'['
op|'('
string|"'bar'"
op|','
string|"'bar'"
op|')'
op|','
op|'('
string|"'foo'"
op|','
number|'123'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sorted'
op|'('
name|'list'
op|'('
name|'obj'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|','
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
name|'x'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
op|'['
op|'('
string|"'bar'"
op|','
string|"'bar'"
op|')'
op|','
op|'('
string|"'foo'"
op|','
number|'123'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_load
dedent|''
name|'def'
name|'test_load'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'loaded!'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_loaded_in_primitive
dedent|''
name|'def'
name|'test_loaded_in_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'1'
newline|'\n'
name|'obj'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'loaded!'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.changes'"
op|':'
op|'['
string|"'bar'"
op|']'
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
op|'{'
string|"'foo'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'bar'"
op|':'
string|"'loaded!'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_changes_in_primitive
dedent|''
name|'def'
name|'test_changes_in_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'primitive'
op|'='
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'nova_object.changes'"
name|'in'
name|'primitive'
op|')'
newline|'\n'
name|'obj2'
op|'='
name|'MyObj'
op|'.'
name|'obj_from_primitive'
op|'('
name|'primitive'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj2'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'obj2'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj2'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unknown_objtype
dedent|''
name|'def'
name|'test_unknown_objtype'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'UnsupportedObjectError'
op|','
nl|'\n'
name|'base'
op|'.'
name|'NovaObject'
op|'.'
name|'obj_class_from_name'
op|','
string|"'foo'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_with_alternate_context
dedent|''
name|'def'
name|'test_with_alternate_context'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt1'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'foo'"
op|','
string|"'foo'"
op|')'
newline|'\n'
name|'ctxt2'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'bar'"
op|','
string|"'alternate'"
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt1'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'update_test'
op|'('
name|'ctxt2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'alternate-context'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_orphaned_object
dedent|''
name|'def'
name|'test_orphaned_object'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'_context'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'OrphanedObjectError'
op|','
nl|'\n'
name|'obj'
op|'.'
name|'update_test'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_changed_1
dedent|''
name|'def'
name|'test_changed_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'update_test'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_changed_2
dedent|''
name|'def'
name|'test_changed_2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'save'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_changed_3
dedent|''
name|'def'
name|'test_changed_3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'foo'
op|'='
number|'123'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'refresh'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'321'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'refreshed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_changed_4
dedent|''
name|'def'
name|'test_changed_4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'bar'
op|'='
string|"'something'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'bar'"
op|']'
op|')'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'modify_save_modify'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|','
name|'set'
op|'('
op|'['
string|"'foo'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'42'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'meow'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_static_result
dedent|''
name|'def'
name|'test_static_result'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'bar'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'obj'
op|'.'
name|'marco'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|"'polo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_updates
dedent|''
name|'def'
name|'test_updates'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'foo'
op|','
number|'1'
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'update_test'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'updated'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_base_attributes
dedent|''
name|'def'
name|'test_base_attributes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dt'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1955'
op|','
number|'11'
op|','
number|'5'
op|')'
newline|'\n'
name|'obj'
op|'='
name|'MyObj'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'.'
name|'created_at'
op|'='
name|'dt'
newline|'\n'
name|'obj'
op|'.'
name|'updated_at'
op|'='
name|'dt'
newline|'\n'
name|'obj'
op|'.'
name|'deleted_at'
op|'='
name|'None'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'nova_object.name'"
op|':'
string|"'MyObj'"
op|','
nl|'\n'
string|"'nova_object.namespace'"
op|':'
string|"'nova'"
op|','
nl|'\n'
string|"'nova_object.version'"
op|':'
string|"'1.5'"
op|','
nl|'\n'
string|"'nova_object.changes'"
op|':'
nl|'\n'
op|'['
string|"'created_at'"
op|','
string|"'deleted_at'"
op|','
string|"'updated_at'"
op|']'
op|','
nl|'\n'
string|"'nova_object.data'"
op|':'
nl|'\n'
op|'{'
string|"'created_at'"
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'dt'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'dt'
op|')'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestObject
dedent|''
dedent|''
name|'class'
name|'TestObject'
op|'('
name|'_LocalTest'
op|','
name|'_TestObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestRemoteObject
dedent|''
name|'class'
name|'TestRemoteObject'
op|'('
name|'_RemoteTest'
op|','
name|'_TestObject'
op|')'
op|':'
newline|'\n'
DECL|member|test_major_version_mismatch
indent|'    '
name|'def'
name|'test_major_version_mismatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'MyObj2'
op|'.'
name|'version'
op|'='
string|"'2.0'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'IncompatibleObjectVersion'
op|','
nl|'\n'
name|'MyObj2'
op|'.'
name|'get'
op|','
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_minor_version_greater
dedent|''
name|'def'
name|'test_minor_version_greater'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'MyObj2'
op|'.'
name|'version'
op|'='
string|"'1.6'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'IncompatibleObjectVersion'
op|','
nl|'\n'
name|'MyObj2'
op|'.'
name|'get'
op|','
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_minor_version_less
dedent|''
name|'def'
name|'test_minor_version_less'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'MyObj2'
op|'.'
name|'version'
op|'='
string|"'1.2'"
newline|'\n'
name|'obj'
op|'='
name|'MyObj2'
op|'.'
name|'get'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'obj'
op|'.'
name|'bar'
op|','
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRemotes'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
