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
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uuid'"
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
string|"'oneOf'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'array'"
op|','
nl|'\n'
string|"'items'"
op|':'
name|'parameter_types'
op|'.'
name|'server_id'
nl|'\n'
op|'}'
nl|'\n'
op|']'
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
string|"'different_cell'"
op|':'
op|'{'
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
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'build_near_host_ip'"
op|':'
name|'parameter_types'
op|'.'
name|'ip_address'
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
comment|'# NOTE: As this Mail:'
nl|'\n'
comment|'# http://lists.openstack.org/pipermail/openstack-dev/2015-June/067996.html'
nl|'\n'
comment|'# pointed out the limit the scheduler-hints in the API is problematic. So'
nl|'\n'
comment|'# relax it.'
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'True'
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
