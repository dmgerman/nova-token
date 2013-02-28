begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'String'
op|','
name|'Column'
op|','
name|'MetaData'
op|','
name|'Table'
op|','
name|'select'
newline|'\n'
nl|'\n'
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
string|'""" Remove availability_zone column from services model and replace with\n    aggregate based zone."""'
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
name|'services'
op|'='
name|'Table'
op|'('
string|"'services'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregates'
op|'='
name|'Table'
op|'('
string|"'aggregates'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregate_metadata'
op|'='
name|'Table'
op|'('
string|"'aggregate_metadata'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'# migrate data'
nl|'\n'
name|'record_list'
op|'='
name|'list'
op|'('
name|'services'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'rec'
name|'in'
name|'record_list'
op|':'
newline|'\n'
comment|'# Only need to migrate nova-compute availability_zones'
nl|'\n'
indent|'        '
name|'if'
name|'rec'
op|'['
string|"'binary'"
op|']'
op|'!='
string|"'nova-compute'"
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
comment|"# if zone doesn't exist create"
nl|'\n'
dedent|''
name|'result'
op|'='
name|'aggregate_metadata'
op|'.'
name|'select'
op|'('
op|')'
op|'.'
name|'where'
op|'('
nl|'\n'
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'key'
op|'=='
string|"'availability_zone'"
op|')'
op|'.'
name|'where'
op|'('
nl|'\n'
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'value'
op|'=='
name|'rec'
op|'['
string|"'availability_zone'"
op|']'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
name|'r'
name|'for'
name|'r'
name|'in'
name|'result'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'result'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'agg_id'
op|'='
name|'result'
op|'['
number|'0'
op|']'
op|'.'
name|'aggregate_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'agg'
op|'='
name|'aggregates'
op|'.'
name|'insert'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'agg'
op|'.'
name|'execute'
op|'('
op|'{'
string|"'name'"
op|':'
name|'rec'
op|'['
string|"'availability_zone'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'agg_id'
op|'='
name|'result'
op|'.'
name|'inserted_primary_key'
op|'['
number|'0'
op|']'
newline|'\n'
name|'row'
op|'='
name|'aggregate_metadata'
op|'.'
name|'insert'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'execute'
op|'('
op|'{'
string|"'created_at'"
op|':'
name|'rec'
op|'['
string|"'created_at'"
op|']'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'rec'
op|'['
string|"'updated_at'"
op|']'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'rec'
op|'['
string|"'deleted_at'"
op|']'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'rec'
op|'['
string|"'deleted'"
op|']'
op|','
nl|'\n'
string|"'key'"
op|':'
string|"'availability_zone'"
op|','
nl|'\n'
string|"'value'"
op|':'
name|'rec'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
string|"'aggregate_id'"
op|':'
name|'agg_id'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
comment|'# add host to zone'
nl|'\n'
dedent|''
name|'agg_hosts'
op|'='
name|'Table'
op|'('
string|"'aggregate_hosts'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'num_hosts'
op|'='
name|'agg_hosts'
op|'.'
name|'count'
op|'('
op|')'
op|'.'
name|'where'
op|'('
nl|'\n'
name|'agg_hosts'
op|'.'
name|'c'
op|'.'
name|'host'
op|'=='
name|'rec'
op|'['
string|"'host'"
op|']'
op|')'
op|'.'
name|'where'
op|'('
nl|'\n'
name|'agg_hosts'
op|'.'
name|'c'
op|'.'
name|'aggregate_id'
op|'=='
name|'agg_id'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
op|'.'
name|'scalar'
op|'('
op|')'
newline|'\n'
name|'if'
name|'num_hosts'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'agg_hosts'
op|'.'
name|'insert'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
op|'{'
string|"'host'"
op|':'
name|'rec'
op|'['
string|"'host'"
op|']'
op|','
nl|'\n'
string|"'aggregate_id'"
op|':'
name|'agg_id'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'services'
op|'.'
name|'drop_column'
op|'('
string|"'availability_zone'"
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
name|'services'
op|'='
name|'Table'
op|'('
string|"'services'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'aggregate_metadata'
op|'='
name|'Table'
op|'('
string|"'aggregate_metadata'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'agg_hosts'
op|'='
name|'Table'
op|'('
string|"'aggregate_hosts'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'availability_zone'
op|'='
name|'Column'
op|'('
string|"'availability_zone'"
op|','
name|'String'
op|'('
number|'255'
op|')'
op|','
nl|'\n'
name|'default'
op|'='
string|"'nova'"
op|')'
newline|'\n'
name|'services'
op|'.'
name|'create_column'
op|'('
name|'availability_zone'
op|')'
newline|'\n'
comment|'# migrate data'
nl|'\n'
name|'services'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'values'
op|'('
name|'availability_zone'
op|'='
name|'select'
op|'('
nl|'\n'
op|'['
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'value'
op|']'
op|')'
op|'.'
nl|'\n'
name|'where'
op|'('
name|'agg_hosts'
op|'.'
name|'c'
op|'.'
name|'aggregate_id'
op|'=='
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'aggregate_id'
op|')'
op|'.'
nl|'\n'
name|'where'
op|'('
name|'aggregate_metadata'
op|'.'
name|'c'
op|'.'
name|'key'
op|'=='
string|"'availability_zone'"
op|')'
op|'.'
nl|'\n'
name|'where'
op|'('
name|'agg_hosts'
op|'.'
name|'c'
op|'.'
name|'host'
op|'=='
name|'services'
op|'.'
name|'c'
op|'.'
name|'host'
op|')'
op|'.'
nl|'\n'
name|'where'
op|'('
name|'services'
op|'.'
name|'c'
op|'.'
name|'binary'
op|'=='
string|"'nova-compute'"
op|')'
op|')'
op|'.'
name|'execute'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
