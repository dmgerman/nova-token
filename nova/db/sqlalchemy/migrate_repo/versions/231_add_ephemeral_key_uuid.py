begin_unit
comment|'# Copyright (c) 2014 The Johns Hopkins University/Applied Physics Laboratory'
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
name|'String'
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
string|'"""Function adds ephemeral storage encryption key uuid field."""'
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
nl|'\n'
name|'instances'
op|'='
name|'Table'
op|'('
string|"'instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'shadow_instances'
op|'='
name|'Table'
op|'('
string|"'shadow_instances'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'ephemeral_key_uuid'
op|'='
name|'Column'
op|'('
string|"'ephemeral_key_uuid'"
op|','
name|'String'
op|'('
number|'36'
op|')'
op|')'
newline|'\n'
name|'instances'
op|'.'
name|'create_column'
op|'('
name|'ephemeral_key_uuid'
op|')'
newline|'\n'
name|'shadow_instances'
op|'.'
name|'create_column'
op|'('
name|'ephemeral_key_uuid'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'instances'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
nl|'\n'
name|'values'
op|'('
name|'ephemeral_key_uuid'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'shadow_instances'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
nl|'\n'
name|'values'
op|'('
name|'ephemeral_key_uuid'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
