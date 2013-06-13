begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
op|','
name|'String'
op|','
name|'Table'
newline|'\n'
name|'from'
name|'sqlalchemy'
op|'.'
name|'dialects'
name|'import'
name|'postgresql'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TABLE_COLUMNS
name|'TABLE_COLUMNS'
op|'='
op|'['
nl|'\n'
comment|'# table name, column name'
nl|'\n'
op|'('
string|"'instances'"
op|','
string|"'access_ip_v4'"
op|')'
op|','
nl|'\n'
op|'('
string|"'instances'"
op|','
string|"'access_ip_v6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'security_group_rules'"
op|','
string|"'cidr'"
op|')'
op|','
nl|'\n'
op|'('
string|"'provider_fw_rules'"
op|','
string|"'cidr'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'cidr'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'cidr_v6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'gateway'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'gateway_v6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'netmask'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'netmask_v6'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'broadcast'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'dns1'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'dns2'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'vpn_public_address'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'vpn_private_address'"
op|')'
op|','
nl|'\n'
op|'('
string|"'networks'"
op|','
string|"'dhcp_start'"
op|')'
op|','
nl|'\n'
op|'('
string|"'fixed_ips'"
op|','
string|"'address'"
op|')'
op|','
nl|'\n'
op|'('
string|"'floating_ips'"
op|','
string|"'address'"
op|')'
op|','
nl|'\n'
op|'('
string|"'console_pools'"
op|','
string|"'address'"
op|')'
op|']'
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
string|'"""Convert String columns holding IP addresses to INET for postgresql."""'
newline|'\n'
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
name|'dialect'
op|'='
name|'migrate_engine'
op|'.'
name|'url'
op|'.'
name|'get_dialect'
op|'('
op|')'
newline|'\n'
name|'if'
name|'dialect'
name|'is'
name|'postgresql'
op|'.'
name|'dialect'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'table'
op|','
name|'column'
name|'in'
name|'TABLE_COLUMNS'
op|':'
newline|'\n'
comment|"# can't use migrate's alter() because it does not support"
nl|'\n'
comment|'# explicit casting'
nl|'\n'
indent|'            '
name|'migrate_engine'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|'"ALTER TABLE %(table)s "'
nl|'\n'
string|'"ALTER COLUMN %(column)s TYPE INET USING %(column)s::INET"'
nl|'\n'
op|'%'
op|'{'
string|"'table'"
op|':'
name|'table'
op|','
string|"'column'"
op|':'
name|'column'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'table'
op|','
name|'column'
name|'in'
name|'TABLE_COLUMNS'
op|':'
newline|'\n'
indent|'            '
name|'t'
op|'='
name|'Table'
op|'('
name|'table'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'t'
op|'.'
name|'c'
op|','
name|'column'
op|')'
op|'.'
name|'alter'
op|'('
name|'type'
op|'='
name|'String'
op|'('
number|'43'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|downgrade
dedent|''
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
string|'"""Convert columns back to the larger String(255)."""'
newline|'\n'
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
name|'for'
name|'table'
op|','
name|'column'
name|'in'
name|'TABLE_COLUMNS'
op|':'
newline|'\n'
indent|'        '
name|'t'
op|'='
name|'Table'
op|'('
name|'table'
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'t'
op|'.'
name|'c'
op|','
name|'column'
op|')'
op|'.'
name|'alter'
op|'('
name|'type'
op|'='
name|'String'
op|'('
number|'255'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
