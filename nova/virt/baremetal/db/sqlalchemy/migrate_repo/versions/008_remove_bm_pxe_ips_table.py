begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Mirantis Inc.'
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
name|'Boolean'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'DateTime'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Index'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Integer'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'String'
newline|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Table'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|table_name
name|'table_name'
op|'='
string|"'bm_pxe_ips'"
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
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
nl|'\n'
name|'bm_pxe_ips'
op|'='
name|'Table'
op|'('
name|'table_name'
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|','
name|'primary_key'
op|'='
name|'True'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'address'"
op|','
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'bm_node_id'"
op|','
name|'Integer'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'server_address'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|')'
op|','
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'mysql_engine'
op|'='
string|"'InnoDB'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'bm_pxe_ips'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'Index'
op|'('
nl|'\n'
string|"'idx_bm_pxe_ips_bm_node_id_deleted'"
op|','
nl|'\n'
name|'bm_pxe_ips'
op|'.'
name|'c'
op|'.'
name|'bm_node_id'
op|','
nl|'\n'
name|'bm_pxe_ips'
op|'.'
name|'c'
op|'.'
name|'deleted'
nl|'\n'
op|')'
op|'.'
name|'create'
op|'('
name|'migrate_engine'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
