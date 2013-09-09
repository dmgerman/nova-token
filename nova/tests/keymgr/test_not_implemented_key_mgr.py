begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nTest cases for the not implemented key manager.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'not_implemented_key_mgr'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'keymgr'
name|'import'
name|'test_key_mgr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotImplementedKeyManagerTestCase
name|'class'
name|'NotImplementedKeyManagerTestCase'
op|'('
name|'test_key_mgr'
op|'.'
name|'KeyManagerTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_create_key_manager
indent|'    '
name|'def'
name|'_create_key_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'not_implemented_key_mgr'
op|'.'
name|'NotImplementedKeyManager'
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
name|'NotImplementedKeyManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_key
dedent|''
name|'def'
name|'test_create_key'
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
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'key_mgr'
op|'.'
name|'create_key'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_store_key
dedent|''
name|'def'
name|'test_store_key'
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
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'key_mgr'
op|'.'
name|'store_key'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_key
dedent|''
name|'def'
name|'test_copy_key'
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
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'key_mgr'
op|'.'
name|'copy_key'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_key
dedent|''
name|'def'
name|'test_get_key'
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
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'key_mgr'
op|'.'
name|'get_key'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_key
dedent|''
name|'def'
name|'test_delete_key'
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
name|'NotImplementedError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'key_mgr'
op|'.'
name|'delete_key'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
