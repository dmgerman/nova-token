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
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'utils'
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
string|'"""Dynamically limits hosts to one instance type\n\n        Return False if host has any instance types other than the requested\n        type. Return True if all instance types match or if host is empty.\n        """'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'instance_type_id'
op|'='
name|'instance_type'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'other_types_on_host'
op|'='
name|'utils'
op|'.'
name|'other_types_on_host'
op|'('
name|'host_state'
op|','
nl|'\n'
name|'instance_type_id'
op|')'
newline|'\n'
name|'return'
name|'not'
name|'other_types_on_host'
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
nl|'\n'
comment|'# TODO(uni): DB query in filter is a performance hit, especially for'
nl|'\n'
comment|'# system with lots of hosts. Will need a general solution here to fix'
nl|'\n'
comment|'# all filters with aggregate DB call things.'
nl|'\n'
name|'aggregate_vals'
op|'='
name|'utils'
op|'.'
name|'aggregate_values_from_key'
op|'('
nl|'\n'
name|'host_state'
op|','
string|"'instance_type'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'aggregate_vals'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'instance_type'
op|'['
string|"'name'"
op|']'
name|'in'
name|'aggregate_vals'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
