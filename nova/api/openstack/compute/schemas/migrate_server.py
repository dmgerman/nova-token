begin_unit
comment|'# Copyright 2014 NEC Corporation.  All rights reserved.'
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
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|host
name|'host'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'parameter_types'
op|'.'
name|'hostname'
op|')'
newline|'\n'
name|'host'
op|'['
string|"'type'"
op|']'
op|'='
op|'['
string|"'string'"
op|','
string|"'null'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|migrate_live
name|'migrate_live'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'os-migrateLive'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'block_migration'"
op|':'
name|'parameter_types'
op|'.'
name|'boolean'
op|','
nl|'\n'
string|"'disk_over_commit'"
op|':'
name|'parameter_types'
op|'.'
name|'boolean'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'host'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'block_migration'"
op|','
string|"'disk_over_commit'"
op|','
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'os-migrateLive'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|block_migration
name|'block_migration'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'parameter_types'
op|'.'
name|'boolean'
op|')'
newline|'\n'
name|'block_migration'
op|'['
string|"'enum'"
op|']'
op|'.'
name|'append'
op|'('
string|"'auto'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|migrate_live_v2_25
name|'migrate_live_v2_25'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'migrate_live'
op|')'
newline|'\n'
nl|'\n'
name|'del'
name|'migrate_live_v2_25'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'os-migrateLive'"
op|']'
op|'['
string|"'properties'"
op|']'
op|'['
nl|'\n'
string|"'disk_over_commit'"
op|']'
newline|'\n'
name|'migrate_live_v2_25'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'os-migrateLive'"
op|']'
op|'['
string|"'properties'"
op|']'
op|'['
nl|'\n'
string|"'block_migration'"
op|']'
op|'='
name|'block_migration'
newline|'\n'
name|'migrate_live_v2_25'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'os-migrateLive'"
op|']'
op|'['
string|"'required'"
op|']'
op|'='
op|'('
nl|'\n'
op|'['
string|"'block_migration'"
op|','
string|"'host'"
op|']'
op|')'
newline|'\n'
endmarker|''
end_unit
