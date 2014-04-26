begin_unit
comment|'# Copyright (c) 2012 The Cloudscaling Group, Inc.'
nl|'\n'
comment|'#'
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
nl|'\n'
DECL|class|TypeAffinityFilter
name|'class'
name|'TypeAffinityFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""TypeAffinityFilter doesn\'t allow more than one VM type per host.\n\n    Note: this works best with ram_weight_multiplier\n    (spread) set to 1 (default).\n    """'
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
string|'"""Dynamically limits hosts to one instance type\n\n        Return False if host has any instance types other then the requested\n        type. Return True if all instance types match or if host is empty.\n        """'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
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
name|'instances_other_type'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host_and_not_type'
op|'('
nl|'\n'
name|'context'
op|','
name|'host_state'
op|'.'
name|'host'
op|','
name|'instance_type'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'len'
op|'('
name|'instances_other_type'
op|')'
op|'=='
number|'0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregateTypeAffinityFilter
dedent|''
dedent|''
name|'class'
name|'AggregateTypeAffinityFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateTypeAffinityFilter limits instance_type by aggregate\n\n    return True if no instance_type key is set or if the aggregate metadata\n    key \'instance_type\' has the instance_type name as a value\n    """'
newline|'\n'
nl|'\n'
comment|'# Aggregate data does not change within a request'
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
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
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
string|"'instance_type'"
op|')'
newline|'\n'
name|'return'
op|'('
name|'len'
op|'('
name|'metadata'
op|')'
op|'=='
number|'0'
name|'or'
nl|'\n'
name|'instance_type'
op|'['
string|"'name'"
op|']'
name|'in'
name|'metadata'
op|'['
string|"'instance_type'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
