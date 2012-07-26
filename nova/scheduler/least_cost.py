begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""\nLeast Cost is an algorithm for choosing which host machines to\nprovision a set of resources to. The input is a WeightedHost object which\nis decided upon by a set of objective-functions, called the \'cost-functions\'.\nThe WeightedHost contains a combined weight for each cost-function.\n\nThe cost-function and weights are tabulated, and the host with the least cost\nis then selected for provisioning.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
DECL|variable|least_cost_opts
name|'least_cost_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'least_cost_functions'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'nova.scheduler.least_cost.compute_fill_first_cost_fn'"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Which cost functions the LeastCostScheduler should use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'noop_cost_fn_weight'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How much weight to give the noop cost function'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'compute_fill_first_cost_fn_weight'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How much weight to give the fill-first cost function. '"
nl|'\n'
string|"'A negative value will reverse behavior: '"
nl|'\n'
string|"'e.g. spread-first'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'least_cost_opts'
op|')'
newline|'\n'
nl|'\n'
comment|'# TODO(sirp): Once we have enough of these rules, we can break them out into a'
nl|'\n'
comment|'# cost_functions.py file (perhaps in a least_cost_scheduler directory)'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|WeightedHost
name|'class'
name|'WeightedHost'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Reduced set of information about a host that has been weighed.\n    This is an attempt to remove some of the ad-hoc dict structures\n    previously used."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'weight'
op|','
name|'host_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'weight'
op|'='
name|'weight'
newline|'\n'
name|'self'
op|'.'
name|'host_state'
op|'='
name|'host_state'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
name|'dict'
op|'('
name|'weight'
op|'='
name|'self'
op|'.'
name|'weight'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'host_state'
op|':'
newline|'\n'
indent|'            '
name|'x'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'host_state'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'return'
name|'x'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'host_state'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"WeightedHost host: %s"'
op|'%'
name|'self'
op|'.'
name|'host_state'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'return'
string|'"WeightedHost with no host_state"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|noop_cost_fn
dedent|''
dedent|''
name|'def'
name|'noop_cost_fn'
op|'('
name|'host_state'
op|','
name|'weighing_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a pre-weight cost of 1 for each host"""'
newline|'\n'
name|'return'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_fill_first_cost_fn
dedent|''
name|'def'
name|'compute_fill_first_cost_fn'
op|'('
name|'host_state'
op|','
name|'weighing_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""More free ram = higher weight. So servers with less free\n    ram will be preferred.\n\n    Note: the weight for this function in default configuration\n    is -1.0. With a -1.0 this function runs in reverse, so systems\n    with the most free memory will be preferred.\n    """'
newline|'\n'
name|'return'
name|'host_state'
op|'.'
name|'free_ram_mb'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|weighted_sum
dedent|''
name|'def'
name|'weighted_sum'
op|'('
name|'weighted_fns'
op|','
name|'host_states'
op|','
name|'weighing_properties'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use the weighted-sum method to compute a score for an array of objects.\n\n    Normalize the results of the objective-functions so that the weights are\n    meaningful regardless of objective-function\'s range.\n\n    :param host_list:    ``[(host, HostInfo()), ...]``\n    :param weighted_fns: list of weights and functions like::\n\n        [(weight, objective-functions), ...]\n\n    :param weighing_properties: an arbitrary dict of values that can\n        influence weights.\n\n    :returns: a single WeightedHost object which represents the best\n              candidate.\n    """'
newline|'\n'
nl|'\n'
name|'min_score'
op|','
name|'best_host'
op|'='
name|'None'
op|','
name|'None'
newline|'\n'
name|'for'
name|'host_state'
name|'in'
name|'host_states'
op|':'
newline|'\n'
indent|'        '
name|'score'
op|'='
name|'sum'
op|'('
name|'weight'
op|'*'
name|'fn'
op|'('
name|'host_state'
op|','
name|'weighing_properties'
op|')'
nl|'\n'
name|'for'
name|'weight'
op|','
name|'fn'
name|'in'
name|'weighted_fns'
op|')'
newline|'\n'
name|'if'
name|'min_score'
name|'is'
name|'None'
name|'or'
name|'score'
op|'<'
name|'min_score'
op|':'
newline|'\n'
indent|'            '
name|'min_score'
op|','
name|'best_host'
op|'='
name|'score'
op|','
name|'host_state'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'WeightedHost'
op|'('
name|'min_score'
op|','
name|'host_state'
op|'='
name|'best_host'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
