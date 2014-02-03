begin_unit
comment|'# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory'
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
string|'"""\nTest cases for the key classes.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'array'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyTestCase
name|'class'
name|'KeyTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_create_key
indent|'    '
name|'def'
name|'_create_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
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
name|'KeyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'key'
op|'='
name|'self'
op|'.'
name|'_create_key'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SymmetricKeyTestCase
dedent|''
dedent|''
name|'class'
name|'SymmetricKeyTestCase'
op|'('
name|'KeyTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_create_key
indent|'    '
name|'def'
name|'_create_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'key'
op|'.'
name|'SymmetricKey'
op|'('
name|'self'
op|'.'
name|'algorithm'
op|','
name|'self'
op|'.'
name|'encoded'
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
name|'self'
op|'.'
name|'algorithm'
op|'='
string|"'AES'"
newline|'\n'
name|'self'
op|'.'
name|'encoded'
op|'='
name|'array'
op|'.'
name|'array'
op|'('
string|"'B'"
op|','
op|'('
string|"'0'"
op|'*'
number|'64'
op|')'
op|'.'
name|'decode'
op|'('
string|"'hex'"
op|')'
op|')'
op|'.'
name|'tolist'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'SymmetricKeyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_algorithm
dedent|''
name|'def'
name|'test_get_algorithm'
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
name|'key'
op|'.'
name|'get_algorithm'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'algorithm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_format
dedent|''
name|'def'
name|'test_get_format'
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
name|'key'
op|'.'
name|'get_format'
op|'('
op|')'
op|','
string|"'RAW'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_encoded
dedent|''
name|'def'
name|'test_get_encoded'
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
name|'key'
op|'.'
name|'get_encoded'
op|'('
op|')'
op|','
name|'self'
op|'.'
name|'encoded'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test___eq__
dedent|''
name|'def'
name|'test___eq__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'key'
op|'=='
name|'self'
op|'.'
name|'key'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'key'
op|'=='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'None'
op|'=='
name|'self'
op|'.'
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test___ne__
dedent|''
name|'def'
name|'test___ne__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'key'
op|'!='
name|'self'
op|'.'
name|'key'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'key'
op|'!='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'None'
op|'!='
name|'self'
op|'.'
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
