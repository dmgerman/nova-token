begin_unit
comment|'#    Copyright 2013 Red Hat, Inc.'
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
name|'import'
name|'iso8601'
newline|'\n'
nl|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
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
DECL|class|FakeFieldType
name|'class'
name|'FakeFieldType'
op|'('
name|'fields'
op|'.'
name|'FieldType'
op|')'
op|':'
newline|'\n'
DECL|member|coerce
indent|'    '
name|'def'
name|'coerce'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'attr'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'*%s*'"
op|'%'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|to_primitive
dedent|''
name|'def'
name|'to_primitive'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'attr'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'!%s!'"
op|'%'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|from_primitive
dedent|''
name|'def'
name|'from_primitive'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'attr'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestField
dedent|''
dedent|''
name|'class'
name|'TestField'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'TestField'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'FakeFieldType'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
string|"'foo'"
op|','
string|"'*foo*'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
string|"'foo'"
op|','
string|"'!foo!'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
string|"'!foo!'"
op|','
string|"'foo'"
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_coerce_good_values
dedent|''
name|'def'
name|'test_coerce_good_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'in_val'
op|','
name|'out_val'
name|'in'
name|'self'
op|'.'
name|'coerce_good_values'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'out_val'
op|','
name|'self'
op|'.'
name|'field'
op|'.'
name|'coerce'
op|'('
string|"'obj'"
op|','
string|"'attr'"
op|','
name|'in_val'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_coerce_bad_values
dedent|''
dedent|''
name|'def'
name|'test_coerce_bad_values'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'in_val'
name|'in'
name|'self'
op|'.'
name|'coerce_bad_values'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
op|'('
name|'TypeError'
op|','
name|'ValueError'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'field'
op|'.'
name|'coerce'
op|','
string|"'obj'"
op|','
string|"'attr'"
op|','
name|'in_val'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_to_primitive
dedent|''
dedent|''
name|'def'
name|'test_to_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'in_val'
op|','
name|'prim_val'
name|'in'
name|'self'
op|'.'
name|'to_primitive_values'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'prim_val'
op|','
name|'self'
op|'.'
name|'field'
op|'.'
name|'to_primitive'
op|'('
string|"'obj'"
op|','
string|"'attr'"
op|','
nl|'\n'
name|'in_val'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_primitive
dedent|''
dedent|''
name|'def'
name|'test_from_primitive'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|ObjectLikeThing
indent|'        '
name|'class'
name|'ObjectLikeThing'
op|':'
newline|'\n'
DECL|variable|_context
indent|'            '
name|'_context'
op|'='
string|"'context'"
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'prim_val'
op|','
name|'out_val'
name|'in'
name|'self'
op|'.'
name|'from_primitive_values'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'out_val'
op|','
name|'self'
op|'.'
name|'field'
op|'.'
name|'from_primitive'
op|'('
nl|'\n'
name|'ObjectLikeThing'
op|','
string|"'attr'"
op|','
name|'prim_val'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestString
dedent|''
dedent|''
dedent|''
name|'class'
name|'TestString'
op|'('
name|'TestField'
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
name|'TestField'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
string|"'foo'"
op|','
string|"'foo'"
op|')'
op|','
op|'('
number|'1'
op|','
string|"'1'"
op|')'
op|','
op|'('
number|'1L'
op|','
string|"'1'"
op|')'
op|','
nl|'\n'
op|'('
name|'True'
op|','
string|"'True'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestInteger
dedent|''
dedent|''
name|'class'
name|'TestInteger'
op|'('
name|'TestField'
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
name|'TestField'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
number|'1'
op|','
number|'1'
op|')'
op|','
op|'('
string|"'1'"
op|','
number|'1'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'foo'"
op|','
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFloat
dedent|''
dedent|''
name|'class'
name|'TestFloat'
op|'('
name|'TestField'
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
name|'TestFloat'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'FloatField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
number|'1.1'
op|','
number|'1.1'
op|')'
op|','
op|'('
string|"'1.1'"
op|','
number|'1.1'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'foo'"
op|','
name|'None'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestBoolean
dedent|''
dedent|''
name|'class'
name|'TestBoolean'
op|'('
name|'TestField'
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
name|'TestField'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'BooleanField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
name|'True'
op|','
name|'True'
op|')'
op|','
op|'('
name|'False'
op|','
name|'False'
op|')'
op|','
op|'('
number|'1'
op|','
name|'True'
op|')'
op|','
nl|'\n'
op|'('
string|"'foo'"
op|','
name|'True'
op|')'
op|','
op|'('
number|'0'
op|','
name|'False'
op|')'
op|','
op|'('
string|"''"
op|','
name|'False'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
name|'self'
op|'.'
name|'coerce_good_values'
op|'['
number|'0'
op|':'
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDateTime
dedent|''
dedent|''
name|'class'
name|'TestDateTime'
op|'('
name|'TestField'
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
name|'TestDateTime'
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
op|','
name|'tzinfo'
op|'='
name|'iso8601'
op|'.'
name|'iso8601'
op|'.'
name|'Utc'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'field'
op|'='
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
name|'self'
op|'.'
name|'dt'
op|','
name|'self'
op|'.'
name|'dt'
op|')'
op|','
nl|'\n'
op|'('
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'self'
op|'.'
name|'dt'
op|')'
op|','
name|'self'
op|'.'
name|'dt'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
number|'1'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'self'
op|'.'
name|'dt'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'self'
op|'.'
name|'dt'
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
name|'timeutils'
op|'.'
name|'isotime'
op|'('
name|'self'
op|'.'
name|'dt'
op|')'
op|','
name|'self'
op|'.'
name|'dt'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIPAddress
dedent|''
dedent|''
name|'class'
name|'TestIPAddress'
op|'('
name|'TestField'
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
name|'TestIPAddress'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
string|"'1.2.3.4'"
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'::1'"
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|','
nl|'\n'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'1-2'"
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|','
string|"'1.2.3.4'"
op|')'
op|','
nl|'\n'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|','
string|"'::1'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
op|'('
string|"'::1'"
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIPAddressV4
dedent|''
dedent|''
name|'class'
name|'TestIPAddressV4'
op|'('
name|'TestField'
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
name|'TestIPAddressV4'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'IPV4AddressField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
string|"'1.2.3.4'"
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
op|','
nl|'\n'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'1-2'"
op|','
string|"'foo'"
op|','
string|"'::1'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|','
string|"'1.2.3.4'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'1.2.3.4'"
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIPAddressV6
dedent|''
dedent|''
name|'class'
name|'TestIPAddressV6'
op|'('
name|'TestField'
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
name|'TestIPAddressV6'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'IPV6AddressField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
string|"'::1'"
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|','
nl|'\n'
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'1.2'"
op|','
string|"'foo'"
op|','
string|"'1.2.3.4'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|','
string|"'::1'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
string|"'::1'"
op|','
nl|'\n'
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::1'"
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDict
dedent|''
dedent|''
name|'class'
name|'TestDict'
op|'('
name|'TestField'
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
name|'TestDict'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'Dict'
op|'('
name|'FakeFieldType'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'*bar*'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'*1*'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|'{'
number|'1'
op|':'
string|"'bar'"
op|'}'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'!bar!'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'!bar!'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDictOfStrings
dedent|''
dedent|''
name|'class'
name|'TestDictOfStrings'
op|'('
name|'TestField'
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
name|'TestDictOfStrings'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'DictOfStringsField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'1'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|'{'
number|'1'
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
name|'None'
op|'}'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestDictOfStringsNone
dedent|''
dedent|''
name|'class'
name|'TestDictOfStringsNone'
op|'('
name|'TestField'
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
name|'TestDictOfStringsNone'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'DictOfNullableStringsField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'{'
string|"'foo'"
op|':'
number|'1'
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'1'"
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'{'
string|"'foo'"
op|':'
name|'None'
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
name|'None'
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|'{'
number|'1'
op|':'
string|"'bar'"
op|'}'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|','
op|'{'
string|"'foo'"
op|':'
string|"'bar'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestList
dedent|''
dedent|''
name|'class'
name|'TestList'
op|'('
name|'TestField'
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
name|'TestList'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'List'
op|'('
name|'FakeFieldType'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|','
op|'['
string|"'*foo*'"
op|','
string|"'*bar*'"
op|']'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
op|'['
string|"'foo'"
op|']'
op|','
op|'['
string|"'!foo!'"
op|']'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
op|'['
string|"'!foo!'"
op|']'
op|','
op|'['
string|"'foo'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestListOfStrings
dedent|''
dedent|''
name|'class'
name|'TestListOfStrings'
op|'('
name|'TestField'
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
name|'TestListOfStrings'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'ListOfStringsField'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|','
op|'['
string|"'foo'"
op|','
string|"'bar'"
op|']'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
op|'['
string|"'foo'"
op|']'
op|','
op|'['
string|"'foo'"
op|']'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
op|'['
string|"'foo'"
op|']'
op|','
op|'['
string|"'foo'"
op|']'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestObject
dedent|''
dedent|''
name|'class'
name|'TestObject'
op|'('
name|'TestField'
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
DECL|class|TestableObject
indent|'        '
name|'class'
name|'TestableObject'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|member|__eq__
indent|'            '
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Be rather lax about this equality thing to'
nl|'\n'
comment|'# satisfy the assertEqual() in test_from_primitive(). We'
nl|'\n'
comment|'# just want to make sure the right type of object is re-created'
nl|'\n'
indent|'                '
name|'return'
name|'value'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
name|'TestableObject'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
DECL|class|OtherTestableObject
dedent|''
dedent|''
name|'class'
name|'OtherTestableObject'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'test_inst'
op|'='
name|'TestableObject'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'TestObject'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'Object'
op|'('
string|"'TestableObject'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
name|'test_inst'
op|','
name|'test_inst'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
name|'OtherTestableObject'
op|'('
op|')'
op|','
number|'1'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'test_inst'
op|','
name|'test_inst'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
name|'test_inst'
op|'.'
name|'obj_to_primitive'
op|'('
op|')'
op|','
nl|'\n'
name|'test_inst'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNetworkModel
dedent|''
dedent|''
name|'class'
name|'TestNetworkModel'
op|'('
name|'TestField'
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
name|'TestNetworkModel'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'model'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'NetworkModel'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
name|'model'
op|','
name|'model'
op|')'
op|','
op|'('
name|'model'
op|'.'
name|'json'
op|'('
op|')'
op|','
name|'model'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
op|'['
op|']'
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'model'
op|','
name|'model'
op|'.'
name|'json'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
op|'['
op|'('
name|'model'
op|'.'
name|'json'
op|'('
op|')'
op|','
name|'model'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCIDR
dedent|''
dedent|''
name|'class'
name|'TestCIDR'
op|'('
name|'TestField'
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
name|'TestCIDR'
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
name|'field'
op|'='
name|'fields'
op|'.'
name|'Field'
op|'('
name|'fields'
op|'.'
name|'CIDR'
op|'('
op|')'
op|')'
newline|'\n'
name|'good'
op|'='
op|'['
string|"'192.168.0.1/24'"
op|','
string|"'192.168.0.0/16'"
op|','
string|"'192.168.0.0/8'"
op|','
nl|'\n'
string|"'192.168.0.0/0'"
op|','
string|"'1.2.3.4/32'"
op|','
string|"'1.2.3.4/22'"
op|','
string|"'0/0'"
op|','
nl|'\n'
string|"'::1/128'"
op|','
string|"'::1/64'"
op|','
string|"'::1/0'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_good_values'
op|'='
op|'['
op|'('
name|'x'
op|','
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'good'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'coerce_bad_values'
op|'='
op|'['
string|"'192.168.0.0'"
op|','
string|"'192.168.0.0/f'"
op|','
nl|'\n'
string|"'192.168.0.0/foo'"
op|','
string|"'192.168.0.0/33'"
op|','
nl|'\n'
string|"'::1/129'"
op|','
string|"'192.168.0.0/-1'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'to_primitive_values'
op|'='
op|'['
op|'('
name|'x'
op|','
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'good'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'from_primitive_values'
op|'='
name|'self'
op|'.'
name|'to_primitive_values'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
