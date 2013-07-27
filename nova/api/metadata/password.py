begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CHUNKS
name|'CHUNKS'
op|'='
number|'4'
newline|'\n'
DECL|variable|CHUNK_LENGTH
name|'CHUNK_LENGTH'
op|'='
number|'255'
newline|'\n'
DECL|variable|MAX_SIZE
name|'MAX_SIZE'
op|'='
name|'CHUNKS'
op|'*'
name|'CHUNK_LENGTH'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_password
name|'def'
name|'extract_password'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
string|"''"
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'sorted'
op|'('
name|'sys_meta'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'password_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'+='
name|'sys_meta'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
name|'or'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_password
dedent|''
name|'def'
name|'convert_password'
op|'('
name|'context'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stores password as system_metadata items.\n\n    Password is stored with the keys \'password_0\' -> \'password_3\'.\n    """'
newline|'\n'
name|'password'
op|'='
name|'password'
name|'or'
string|"''"
newline|'\n'
name|'meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'CHUNKS'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'meta'
op|'['
string|"'password_%d'"
op|'%'
name|'i'
op|']'
op|'='
name|'password'
op|'['
op|':'
name|'CHUNK_LENGTH'
op|']'
newline|'\n'
name|'password'
op|'='
name|'password'
op|'['
name|'CHUNK_LENGTH'
op|':'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'meta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|handle_password
dedent|''
name|'def'
name|'handle_password'
op|'('
name|'req'
op|','
name|'meta_data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'if'
name|'req'
op|'.'
name|'method'
op|'=='
string|"'GET'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'meta_data'
op|'.'
name|'password'
newline|'\n'
dedent|''
name|'elif'
name|'req'
op|'.'
name|'method'
op|'=='
string|"'POST'"
op|':'
newline|'\n'
comment|'# NOTE(vish): The conflict will only happen once the metadata cache'
nl|'\n'
comment|"#             updates, but it isn't a huge issue if it can be set for"
nl|'\n'
comment|'#             a short window.'
nl|'\n'
indent|'        '
name|'if'
name|'meta_data'
op|'.'
name|'password'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'req'
op|'.'
name|'content_length'
op|'>'
name|'MAX_SIZE'
name|'or'
name|'len'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
op|'>'
name|'MAX_SIZE'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Request is too large."'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'conductor_api'
op|'='
name|'conductor'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'conductor_api'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'ctxt'
op|','
name|'meta_data'
op|'.'
name|'uuid'
op|')'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'metadata_to_dict'
op|'('
name|'instance'
op|'['
string|"'system_metadata'"
op|']'
op|')'
newline|'\n'
name|'sys_meta'
op|'.'
name|'update'
op|'('
name|'convert_password'
op|'('
name|'ctxt'
op|','
name|'req'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
name|'conductor_api'
op|'.'
name|'instance_update'
op|'('
name|'ctxt'
op|','
name|'meta_data'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'sys_meta'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
