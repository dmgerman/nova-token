begin_unit
comment|'# Copyright (c) 2012 Red Hat, Inc.'
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
name|'sqlalchemy'
name|'import'
name|'MetaData'
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
comment|'# NOTE(dprince): Need to rename the leftover zones stuff and quota_new'
nl|'\n'
comment|'# stuff from Essex for PostgreSQL.'
nl|'\n'
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"postgresql"'
op|':'
newline|'\n'
indent|'        '
name|'sql'
op|'='
string|'"""ALTER TABLE zones_id_seq RENAME TO cells_id_seq;\n              ALTER TABLE ONLY cells DROP CONSTRAINT zones_pkey;\n              ALTER TABLE ONLY cells ADD CONSTRAINT cells_pkey\n              PRIMARY KEY (id);\n\n              ALTER TABLE quotas_new_id_seq RENAME TO quotas_id_seq;\n              ALTER TABLE ONLY quotas DROP CONSTRAINT quotas_new_pkey;\n              ALTER TABLE ONLY quotas ADD CONSTRAINT quotas_pkey\n              PRIMARY KEY (id);"""'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'sql'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
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
name|'if'
name|'migrate_engine'
op|'.'
name|'name'
op|'=='
string|'"postgresql"'
op|':'
newline|'\n'
indent|'        '
name|'sql'
op|'='
string|'"""ALTER TABLE cells_id_seq RENAME TO zones_id_seq;\n              ALTER TABLE ONLY cells DROP CONSTRAINT cells_pkey;\n              ALTER TABLE ONLY cells ADD CONSTRAINT zones_pkey\n              PRIMARY KEY (id);\n\n              ALTER TABLE quotas_id_seq RENAME TO quotas_new_id_seq;\n              ALTER TABLE ONLY quotas DROP CONSTRAINT quotas_pkey;\n              ALTER TABLE ONLY quotas ADD CONSTRAINT quotas_new_pkey\n              PRIMARY KEY (id);"""'
newline|'\n'
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
name|'sql'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
