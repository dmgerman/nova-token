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
string|'"""\nA mock implementation of a key manager. This module should NOT be used for\nanything but integration testing.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'array'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key_mgr'
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
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|class|MockKeyManager
name|'class'
name|'MockKeyManager'
op|'('
name|'key_mgr'
op|'.'
name|'KeyManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This mock key manager implementation supports all the methods specified\n    by the key manager interface. This implementation creates a single key in\n    response to all invocations of create_key. Side effects (e.g., raising\n    exceptions) for each method are handled as specified by the key manager\n    interface.\n\n    This class should NOT be used for anything but integration testing because\n    the same key is created for all invocations of create_key and keys are not\n    stored persistently.\n    """'
newline|'\n'
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
name|'keys'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create_key
dedent|''
name|'def'
name|'create_key'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a key.\n\n        This implementation returns a UUID for the created key. A\n        NotAuthorized exception is raised if the specified context is None.\n        """'
newline|'\n'
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
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# generate the key'
nl|'\n'
dedent|''
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
comment|'# hex digit => 4 bits'
nl|'\n'
name|'hex_string'
op|'='
name|'utils'
op|'.'
name|'generate_password'
op|'('
name|'length'
op|'='
name|'key_length'
op|'/'
number|'4'
op|','
nl|'\n'
name|'symbolgroups'
op|'='
string|"'0123456789ABCDEF'"
op|')'
newline|'\n'
nl|'\n'
name|'_bytes'
op|'='
name|'array'
op|'.'
name|'array'
op|'('
string|"'B'"
op|','
name|'hex_string'
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
name|'_key'
op|'='
name|'key'
op|'.'
name|'SymmetricKey'
op|'('
string|"'AES'"
op|','
name|'_bytes'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'store_key'
op|'('
name|'ctxt'
op|','
name|'_key'
op|')'
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
string|'"""Stores (i.e., registers) a key with the key manager.\n\n        This implementation does nothing -- i.e., the specified key is\n        discarded.\n        """'
newline|'\n'
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
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# generate UUID and ensure that it isn't in use"
nl|'\n'
dedent|''
name|'key_id'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
name|'while'
name|'key_id'
name|'in'
name|'self'
op|'.'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'key_id'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'keys'
op|'['
name|'key_id'
op|']'
op|'='
name|'key'
newline|'\n'
nl|'\n'
name|'return'
name|'key_id'
newline|'\n'
nl|'\n'
DECL|member|get_key
dedent|''
name|'def'
name|'get_key'
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
string|'"""Retrieves the key identified by the specified id.\n\n        This implementation returns a fixed key that is associated with the\n        UUID returned by the create_key method. A NotAuthorized exception is\n        raised if the specified context is None; a KeyError is raised if the\n        UUID is invalid.\n        """'
newline|'\n'
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
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'keys'
op|'['
name|'key_id'
op|']'
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
string|'"""Deletes the key identified by the specified id.\n\n        This implementation intentionally does nothing except raise a\n        NotAuthorized exception is the context is None or a KeyError if the\n        UUID is invalid.\n        """'
newline|'\n'
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
name|'NotAuthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'del'
name|'self'
op|'.'
name|'keys'
op|'['
name|'key_id'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
