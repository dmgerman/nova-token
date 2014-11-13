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
DECL|variable|_hints
name|'_hints'
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
string|"'group'"
op|':'
op|'{'
nl|'\n'
comment|"# NOTE: The value of 'group' is stored to value which is"
nl|'\n'
comment|'# defined as varchar(255) in instance_system_metadata table.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'different_host'"
op|':'
op|'{'
nl|'\n'
comment|"# NOTE: The value of 'different_host' is the set of server"
nl|'\n'
comment|'# uuids where a new server is scheduled on a different host.'
nl|'\n'
comment|'# A user can specify one server as string parameter and should'
nl|'\n'
comment|'# specify multiple servers as array parameter instead.'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'array'"
op|']'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uuid'"
op|','
nl|'\n'
string|"'items'"
op|':'
name|'parameter_types'
op|'.'
name|'server_id'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'same_host'"
op|':'
op|'{'
nl|'\n'
comment|"# NOTE: The value of 'different_host' is the set of server"
nl|'\n'
comment|'# uuids where a new server is scheduled on the same host.'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'array'"
op|']'
op|','
nl|'\n'
string|"'items'"
op|':'
name|'parameter_types'
op|'.'
name|'server_id'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'query'"
op|':'
op|'{'
nl|'\n'
comment|"# NOTE: The value of 'query' is converted to dict data with"
nl|'\n'
comment|'# jsonutils.loads() and used for filtering hosts.'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'object'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
comment|"# NOTE: The value of 'target_cell' is the cell name what cell"
nl|'\n'
comment|'# a new server is scheduled on.'
nl|'\n'
string|"'target_cell'"
op|':'
name|'parameter_types'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'build_near_host_ip'"
op|':'
op|'{'
nl|'\n'
comment|"# NOTE: The combination string of 'build_near_host_ip' and 'cidr'"
nl|'\n'
comment|'# is passed to netaddr.IPNetwork().'
nl|'\n'
comment|'# This covers both ipv4 and ipv6.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'oneOf'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv4'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv6'"
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'cidr'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^\\/[0-9a-f.:]+$'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|server_create
name|'server_create'
op|'='
op|'{'
nl|'\n'
string|"'os:scheduler_hints'"
op|':'
name|'_hints'
op|','
nl|'\n'
string|"'OS-SCH-HNT:scheduler_hints'"
op|':'
name|'_hints'
op|','
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit
