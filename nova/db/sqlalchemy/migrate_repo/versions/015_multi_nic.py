begin_unit
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
comment|'#    under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
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
name|'log'
name|'as'
name|'logging'
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
comment|'# mac address table to add to DB'
nl|'\n'
DECL|variable|mac_addresses
name|'mac_addresses'
op|'='
name|'Table'
op|'('
string|"'mac_addresses'"
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
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
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
op|','
nl|'\n'
DECL|variable|onupdate
name|'onupdate'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
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
string|"'address'"
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
op|','
nl|'\n'
DECL|variable|unique
name|'unique'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'network_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'networks.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'Column'
op|'('
string|"'instance_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'instances.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
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
comment|'# bridge_interface column to add to networks table'
nl|'\n'
DECL|variable|interface
name|'interface'
op|'='
name|'Column'
op|'('
string|"'bridge_interface'"
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
nl|'\n'
name|'assert_unicode'
op|'='
name|'None'
op|','
name|'unicode_error'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|_warn_on_bytestring
name|'_warn_on_bytestring'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# mac_address column to add to fixed_ips table'
nl|'\n'
DECL|variable|mac_address
name|'mac_address'
op|'='
name|'Column'
op|'('
string|"'mac_address_id'"
op|','
nl|'\n'
name|'Integer'
op|'('
op|')'
op|','
nl|'\n'
name|'ForeignKey'
op|'('
string|"'mac_addresses.id'"
op|')'
op|','
nl|'\n'
DECL|variable|nullable
name|'nullable'
op|'='
name|'True'
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
nl|'\n'
comment|'# grab tables and (column for dropping later)'
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
name|'fixed_ips'
op|'='
name|'Table'
op|'('
string|"'fixed_ips'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'networks'
op|'='
name|'Table'
op|'('
string|"'networks'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'c'
op|'='
name|'instances'
op|'.'
name|'columns'
op|'['
string|"'mac_address'"
op|']'
newline|'\n'
nl|'\n'
comment|'# add interface column to networks table'
nl|'\n'
comment|'# values will have to be set manually before running nova'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'networks'
op|'.'
name|'create_column'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"interface column not added to networks table"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
comment|'# create mac_addresses table'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'mac_addresses'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Table |%s| not created!"'
op|')'
op|','
name|'repr'
op|'('
name|'mac_addresses'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
comment|'# add mac_address column to fixed_ips table'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ips'
op|'.'
name|'create_column'
op|'('
name|'mac_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"mac_address column not added to fixed_ips table"'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'e'
newline|'\n'
nl|'\n'
comment|'# populate the mac_addresses table'
nl|'\n'
comment|'# extract data from existing instance and fixed_ip tables'
nl|'\n'
dedent|''
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'instances'
op|'.'
name|'c'
op|'.'
name|'mac_address'
op|','
nl|'\n'
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'network_id'
op|']'
op|','
nl|'\n'
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'=='
name|'instances'
op|'.'
name|'c'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'keys'
op|'='
op|'('
string|"'instance_id'"
op|','
string|"'address'"
op|','
string|"'network_id'"
op|')'
newline|'\n'
name|'join_list'
op|'='
op|'['
name|'dict'
op|'('
name|'zip'
op|'('
name|'keys'
op|','
name|'row'
op|')'
op|')'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"join list for moving mac_addresses |%s|"'
op|')'
op|','
name|'join_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# insert data into the table'
nl|'\n'
name|'if'
name|'join_list'
op|':'
newline|'\n'
indent|'        '
name|'i'
op|'='
name|'mac_addresses'
op|'.'
name|'insert'
op|'('
op|')'
newline|'\n'
name|'i'
op|'.'
name|'execute'
op|'('
name|'join_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# populate the fixed_ips mac_address column'
nl|'\n'
dedent|''
name|'s'
op|'='
name|'select'
op|'('
op|'['
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'id'
op|','
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|']'
op|','
nl|'\n'
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'!='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'row'
name|'in'
name|'s'
op|'.'
name|'execute'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'select'
op|'('
op|'['
name|'mac_addresses'
op|'.'
name|'c'
op|'.'
name|'id'
op|']'
op|'.'
name|'where'
op|'('
name|'mac_addresses'
op|'.'
name|'c'
op|'.'
name|'instance_id'
op|'=='
name|'row'
op|'['
string|"'instance_id'"
op|']'
op|')'
op|'.'
name|'as_scalar'
op|'('
op|')'
nl|'\n'
name|'u'
op|'='
name|'fixed_ips'
op|'.'
name|'update'
op|'('
op|')'
op|'.'
name|'values'
op|'('
name|'mac_address_id'
op|'='
name|'m'
op|')'
op|'.'
name|'where'
op|'('
name|'fixed_ips'
op|'.'
name|'c'
op|'.'
name|'id'
op|'=='
name|'row'
op|'['
string|"'id'"
op|']'
op|')'
nl|'\n'
name|'u'
op|'.'
name|'execute'
op|'('
op|')'
nl|'\n'
nl|'\n'
comment|'# drop the mac_address column from instances'
nl|'\n'
name|'c'
op|'.'
name|'drop'
op|'('
op|')'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
name|'def'
name|'downgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
nl|'\n'
name|'logging'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Can\'t downgrade without losing data"'
op|')'
op|')'
nl|'\n'
name|'raise'
name|'Exception'
nl|'\n'
end_unit
