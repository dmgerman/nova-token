begin_unit
comment|'# Copyright (c) 2011-2012 OpenStack Foundation'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'default_availability_zone'"
op|','
string|"'nova.availability_zones'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AvailabilityZoneFilter
name|'class'
name|'AvailabilityZoneFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filters Hosts by availability zone.\n\n    Works with aggregate metadata availability zones, using the key\n    \'availability_zone\'\n    Note: in theory a compute node can be part of multiple availability_zones\n    """'
newline|'\n'
nl|'\n'
comment|'# Availabilty zones do not change within a request'
nl|'\n'
DECL|variable|run_filter_once_per_request
name|'run_filter_once_per_request'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'spec'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'request_spec'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'props'
op|'='
name|'spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'availability_zone'
op|'='
name|'props'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'availability_zone'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'filter_properties'
op|'['
string|"'context'"
op|']'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'db'
op|'.'
name|'aggregate_metadata_get_by_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'host_state'
op|'.'
name|'host'
op|','
name|'key'
op|'='
string|"'availability_zone'"
op|')'
newline|'\n'
name|'if'
string|"'availability_zone'"
name|'in'
name|'metadata'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'availability_zone'
name|'in'
name|'metadata'
op|'['
string|"'availability_zone'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'availability_zone'
op|'=='
name|'CONF'
op|'.'
name|'default_availability_zone'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
