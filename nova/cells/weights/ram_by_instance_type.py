begin_unit
comment|'# Copyright (c) 2012-2013 Rackspace Hosting'
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
string|'"""\nWeigh cells by memory needed in a way that spreads instances.\n"""'
newline|'\n'
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
op|'.'
name|'cells'
name|'import'
name|'weights'
newline|'\n'
nl|'\n'
DECL|variable|ram_weigher_opts
name|'ram_weigher_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'ram_weight_multiplier'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Multiplier used for weighing ram.  Negative '"
nl|'\n'
string|"'numbers mean to stack vs spread.'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'ram_weigher_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RamByInstanceTypeWeigher
name|'class'
name|'RamByInstanceTypeWeigher'
op|'('
name|'weights'
op|'.'
name|'BaseCellWeigher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Weigh cells by instance_type requested."""'
newline|'\n'
nl|'\n'
DECL|member|weight_multiplier
name|'def'
name|'weight_multiplier'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'ram_weight_multiplier'
newline|'\n'
nl|'\n'
DECL|member|_weigh_object
dedent|''
name|'def'
name|'_weigh_object'
op|'('
name|'self'
op|','
name|'cell'
op|','
name|'weight_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Use the \'ram_free\' for a particular instance_type advertised from a\n        child cell\'s capacity to compute a weight.  We want to direct the\n        build to a cell with a higher capacity.  Since higher weights win,\n        we just return the number of units available for the instance_type.\n        """'
newline|'\n'
name|'request_spec'
op|'='
name|'weight_properties'
op|'['
string|"'request_spec'"
op|']'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'memory_needed'
op|'='
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
newline|'\n'
nl|'\n'
name|'ram_free'
op|'='
name|'cell'
op|'.'
name|'capacities'
op|'.'
name|'get'
op|'('
string|"'ram_free'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'units_by_mb'
op|'='
name|'ram_free'
op|'.'
name|'get'
op|'('
string|"'units_by_mb'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'units_by_mb'
op|'.'
name|'get'
op|'('
name|'str'
op|'('
name|'memory_needed'
op|')'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
