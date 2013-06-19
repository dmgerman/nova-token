begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'# Copyright (c) 2012 Cloudscaling'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
name|'extra_specs_ops'
newline|'\n'
nl|'\n'
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
DECL|class|AggregateInstanceExtraSpecsFilter
name|'class'
name|'AggregateInstanceExtraSpecsFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""AggregateInstanceExtraSpecsFilter works with InstanceType records."""'
newline|'\n'
nl|'\n'
comment|'# Aggregate data and instance type does not change within a request'
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
string|'"""Return a list of hosts that can create instance_type\n\n        Check that the extra specs associated with the instance type match\n        the metadata provided by aggregates.  If not present return False.\n        """'
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
name|'if'
string|"'extra_specs'"
name|'not'
name|'in'
name|'instance_type'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
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
name|'context'
op|','
name|'host_state'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
op|','
name|'req'
name|'in'
name|'instance_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jogo) any key containing a scope (scope is terminated'
nl|'\n'
comment|"# by a `:') will be ignored by this filter. (bug 1039386)"
nl|'\n'
indent|'            '
name|'if'
name|'key'
op|'.'
name|'count'
op|'('
string|"':'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'aggregate_vals'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'aggregate_vals'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s fails instance_type extra_specs "'
nl|'\n'
string|'"requirements. Extra_spec %(key)s is not in aggregate."'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
string|"'key'"
op|':'
name|'key'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'for'
name|'aggregate_val'
name|'in'
name|'aggregate_vals'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'extra_specs_ops'
op|'.'
name|'match'
op|'('
name|'aggregate_val'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s fails instance_type extra_specs "'
nl|'\n'
string|'"requirements. \'%(aggregate_vals)s\' do not "'
nl|'\n'
string|'"match \'%(req)s\'"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
string|"'req'"
op|':'
name|'req'
op|','
nl|'\n'
string|"'aggregate_vals'"
op|':'
name|'aggregate_vals'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
