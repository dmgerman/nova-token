begin_unit
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
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(berrange): Remove NovaObjectDictCompat'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
name|'class'
name|'BandwidthUsage'
op|'('
name|'base'
op|'.'
name|'NovaPersistentObject'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|','
nl|'\n'
DECL|class|BandwidthUsage
name|'base'
op|'.'
name|'NovaObjectDictCompat'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add use_slave to get_by_instance_uuid_and_mac'
nl|'\n'
comment|'# Version 1.2: Add update_cells to create'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
op|')'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'start_period'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'last_refreshed'"
op|':'
name|'fields'
op|'.'
name|'DateTimeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'bw_in'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'bw_out'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'last_ctr_in'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
string|"'last_ctr_out'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_from_db_object
name|'def'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'bw_usage'
op|','
name|'db_bw_usage'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'bw_usage'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
op|'=='
string|"'instance_uuid'"
op|':'
newline|'\n'
indent|'                '
name|'bw_usage'
op|'['
name|'field'
op|']'
op|'='
name|'db_bw_usage'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'bw_usage'
op|'['
name|'field'
op|']'
op|'='
name|'db_bw_usage'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'bw_usage'
op|'.'
name|'_context'
op|'='
name|'context'
newline|'\n'
name|'bw_usage'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'bw_usage'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'base'
op|'.'
name|'serialize_args'
newline|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_instance_uuid_and_mac
name|'def'
name|'get_by_instance_uuid_and_mac'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'mac'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'None'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_bw_usage'
op|'='
name|'db'
op|'.'
name|'bw_usage_get'
op|'('
name|'context'
op|','
name|'uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'start_period'
op|','
name|'mac'
op|'='
name|'mac'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'if'
name|'db_bw_usage'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_from_db_object'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'db_bw_usage'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'serialize_args'
newline|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'bw_in'
op|','
name|'bw_out'
op|','
name|'last_ctr_in'
op|','
nl|'\n'
name|'last_ctr_out'
op|','
name|'start_period'
op|'='
name|'None'
op|','
name|'last_refreshed'
op|'='
name|'None'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_bw_usage'
op|'='
name|'db'
op|'.'
name|'bw_usage_update'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
name|'bw_in'
op|','
name|'bw_out'
op|','
nl|'\n'
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|','
name|'last_refreshed'
op|'='
name|'last_refreshed'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'update_cells'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_from_db_object'
op|'('
name|'self'
op|'.'
name|'_context'
op|','
name|'self'
op|','
name|'db_bw_usage'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|BandwidthUsageList
name|'class'
name|'BandwidthUsageList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Add use_slave to get_by_uuids'
nl|'\n'
comment|'# Version 1.2: BandwidthUsage <= version 1.2'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'BandwidthUsage'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'base'
op|'.'
name|'serialize_args'
newline|'\n'
op|'@'
name|'base'
op|'.'
name|'remotable_classmethod'
newline|'\n'
DECL|member|get_by_uuids
name|'def'
name|'get_by_uuids'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'uuids'
op|','
name|'start_period'
op|'='
name|'None'
op|','
name|'use_slave'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_bw_usages'
op|'='
name|'db'
op|'.'
name|'bw_usage_get_by_uuids'
op|'('
name|'context'
op|','
name|'uuids'
op|'='
name|'uuids'
op|','
nl|'\n'
name|'start_period'
op|'='
name|'start_period'
op|','
nl|'\n'
name|'use_slave'
op|'='
name|'use_slave'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'obj_make_list'
op|'('
name|'context'
op|','
name|'cls'
op|'('
op|')'
op|','
name|'BandwidthUsage'
op|','
name|'db_bw_usages'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
