begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
op|'*'
newline|'\n'
name|'from'
name|'migrate'
name|'import'
op|'*'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
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
comment|'# New Tables'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|instance_types
name|'instance_types'
op|'='
name|'Table'
op|'('
string|"'instance_types'"
op|','
name|'meta'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'created_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'updated_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted_at'"
op|','
name|'DateTime'
op|'('
name|'timezone'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'deleted'"
op|','
name|'Boolean'
op|'('
name|'create_constraint'
op|'='
name|'True'
op|','
name|'name'
op|'='
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'name'"
op|','
nl|'\n'
name|'String'
op|'('
name|'length'
op|'='
number|'255'
op|','
name|'convert_unicode'
op|'='
name|'False'
op|','
name|'assert_unicode'
op|'='
name|'None'
op|','
nl|'\n'
name|'unicode_error'
op|'='
name|'None'
op|','
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'id'"
op|','
name|'Integer'
op|'('
op|')'
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
string|"'memory_mb'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'vcpus'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'local_gb'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'flavorid'"
op|','
name|'Integer'
op|'('
op|')'
op|','
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
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
comment|'# Upgrade operations go here'
nl|'\n'
comment|"# Don't create your own engine; bind migrate_engine"
nl|'\n'
comment|'# to your metadata'
nl|'\n'
indent|'    '
name|'meta'
op|'.'
name|'bind'
op|'='
name|'migrate_engine'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'instance_types'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'info'
op|'('
name|'repr'
op|'('
name|'table'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'Exception while creating instance_types table'"
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
comment|'# Here are the old static instance types'
nl|'\n'
dedent|''
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\n'
string|"'m1.medium'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\n'
string|"'m1.xlarge'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'local_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'='
name|'instance_types'
op|'.'
name|'insert'
op|'('
op|')'
newline|'\n'
name|'for'
name|'name'
op|','
name|'values'
name|'in'
name|'INSTANCE_TYPES'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# FIXME(kpepple) should we be seeding created_at / updated_at ?'
nl|'\n'
comment|'# the_time = time.strftime("%Y-%m-%d %H:%M:%S")'
nl|'\n'
indent|'            '
name|'i'
op|'.'
name|'execute'
op|'('
op|'{'
string|"'name'"
op|':'
name|'name'
op|','
string|"'memory_mb'"
op|':'
name|'values'
op|'['
string|'"memory_mb"'
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'values'
op|'['
string|'"vcpus"'
op|']'
op|','
string|"'deleted'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'values'
op|'['
string|'"local_gb"'
op|']'
op|','
nl|'\n'
string|"'flavorid'"
op|':'
name|'values'
op|'['
string|'"flavorid"'
op|']'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'info'
op|'('
name|'repr'
op|'('
name|'table'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'Exception while seeding instance_types table'"
op|')'
newline|'\n'
name|'raise'
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
comment|'# Operations to reverse the above upgrade go here.'
nl|'\n'
indent|'    '
name|'for'
name|'table'
name|'in'
op|'('
name|'instance_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'table'
op|'.'
name|'drop'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
