begin_unit
comment|'# Copyright (c) 2015 Cloudbase Solutions SRL'
nl|'\n'
comment|'# All Rights Reserved'
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
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Column'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Enum'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'keypair'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Function adds key_pairs type field."""'
newline|'\n'
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
name|'key_pairs'
op|'='
name|'Table'
op|'('
string|"'key_pairs'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'shadow_key_pairs'
op|'='
name|'Table'
op|'('
string|"'shadow_key_pairs'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'enum'
op|'='
name|'Enum'
op|'('
string|"'ssh'"
op|','
string|"'x509'"
op|','
name|'metadata'
op|'='
name|'meta'
op|','
name|'name'
op|'='
string|"'keypair_types'"
op|')'
newline|'\n'
name|'enum'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'keypair_type'
op|'='
name|'Column'
op|'('
string|"'type'"
op|','
name|'enum'
op|','
name|'nullable'
op|'='
name|'False'
op|','
nl|'\n'
name|'server_default'
op|'='
name|'keypair'
op|'.'
name|'KEYPAIR_TYPE_SSH'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'key_pairs'
op|'.'
name|'c'
op|','
string|"'type'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_pairs'
op|'.'
name|'c'
op|'.'
name|'type'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'shadow_key_pairs'
op|'.'
name|'c'
op|','
string|"'type'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shadow_key_pairs'
op|'.'
name|'c'
op|'.'
name|'type'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'key_pairs'
op|'.'
name|'create_column'
op|'('
name|'keypair_type'
op|')'
newline|'\n'
name|'shadow_key_pairs'
op|'.'
name|'create_column'
op|'('
name|'keypair_type'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
