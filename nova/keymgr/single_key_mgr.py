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
string|'"""\nAn implementation of a key manager that returns a single key in response to\nall invocations of get_key.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'mock_key_mgr'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
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
DECL|class|SingleKeyManager
name|'class'
name|'SingleKeyManager'
op|'('
name|'mock_key_mgr'
op|'.'
name|'MockKeyManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This key manager implementation supports all the methods specified by\n    the key manager interface. This implementation creates a single key in\n    response to all invocations of create_key. Side effects\n    (e.g., raising exceptions) for each method are handled as specified by\n    the key manager interface.\n    """'
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
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'This key manager is insecure and is not recommended for '"
nl|'\n'
string|"'production deployments'"
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'SingleKeyManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'key_id'
op|'='
string|"'00000000-0000-0000-0000-000000000000'"
newline|'\n'
name|'self'
op|'.'
name|'key'
op|'='
name|'self'
op|'.'
name|'_generate_key'
op|'('
name|'key_length'
op|'='
number|'256'
op|')'
newline|'\n'
nl|'\n'
comment|'# key should exist by default'
nl|'\n'
name|'self'
op|'.'
name|'keys'
op|'['
name|'self'
op|'.'
name|'key_id'
op|']'
op|'='
name|'self'
op|'.'
name|'key'
newline|'\n'
nl|'\n'
DECL|member|_generate_hex_key
dedent|''
name|'def'
name|'_generate_hex_key'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_length'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'key_length'"
op|','
number|'256'
op|')'
newline|'\n'
name|'return'
string|"'0'"
op|'*'
op|'('
name|'key_length'
op|'/'
number|'4'
op|')'
comment|'# hex digit => 4 bits'
newline|'\n'
nl|'\n'
DECL|member|_generate_key_id
dedent|''
name|'def'
name|'_generate_key_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'key_id'
newline|'\n'
nl|'\n'
DECL|member|store_key
dedent|''
name|'def'
name|'store_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
op|'!='
name|'self'
op|'.'
name|'key'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'KeyManagerError'
op|'('
nl|'\n'
name|'reason'
op|'='
string|'"cannot store arbitrary keys"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'super'
op|'('
name|'SingleKeyManager'
op|','
name|'self'
op|')'
op|'.'
name|'store_key'
op|'('
name|'ctxt'
op|','
name|'key'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_key
dedent|''
name|'def'
name|'delete_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'key_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ctxt'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Forbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'key_id'
op|'!='
name|'self'
op|'.'
name|'key_id'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'KeyManagerError'
op|'('
nl|'\n'
name|'reason'
op|'='
string|'"cannot delete non-existent key"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Not deleting key %s"'
op|')'
op|','
name|'key_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
