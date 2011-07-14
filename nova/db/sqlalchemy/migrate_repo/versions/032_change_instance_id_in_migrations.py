begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
comment|'#    under the License.from sqlalchemy import *'
nl|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'Column'
op|','
name|'Integer'
op|','
name|'String'
op|','
name|'MetaData'
op|','
name|'Table'
newline|'\n'
nl|'\n'
DECL|variable|meta
name|'meta'
op|'='
name|'MetaData'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Tables to alter'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
DECL|variable|instance_id
name|'instance_id'
op|'='
name|'Column'
op|'('
string|"'instance_id'"
op|','
name|'Integer'
op|'('
op|')'
op|')'
newline|'\n'
DECL|variable|instance_uuid
name|'instance_uuid'
op|'='
name|'Column'
op|'('
string|"'instance_uuid'"
op|','
name|'String'
op|'('
number|'255'
op|')'
op|')'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'migrations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'create_column'
op|'('
name|'instance_uuid'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'instance_id'
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
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'migrations'
op|'='
name|'Table'
op|'('
string|"'migrations'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'c'
op|'.'
name|'instance_uuid'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
name|'migrations'
op|'.'
name|'create_column'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
