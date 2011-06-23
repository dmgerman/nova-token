begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nLeast Cost Scheduler is a mechanism for choosing which host machines to\nprovision a set of resources to. The input of the least-cost-scheduler is a\nset of objective-functions, called the \'cost-functions\', a weight for each\ncost-function, and a list of candidate hosts (gathered via FilterHosts).\n\nThe cost-function and weights are tabulated, and the host with the least cost\nis then selected for provisioning.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
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
name|'zone_aware_scheduler'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.least_cost'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_list'
op|'('
string|"'least_cost_scheduler_cost_functions'"
op|','
nl|'\n'
op|'['
string|"'nova.scheduler.least_cost.noop_cost_fn'"
op|']'
op|','
nl|'\n'
string|"'Which cost functions the LeastCostScheduler should use.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO(sirp): Once we have enough of these rules, we can break them out into a'
nl|'\n'
comment|'# cost_functions.py file (perhaps in a least_cost_scheduler directory)'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'noop_cost_fn_weight'"
op|','
number|'1'
op|','
nl|'\n'
string|"'How much weight to give the noop cost function'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|noop_cost_fn
name|'def'
name|'noop_cost_fn'
op|'('
name|'host'
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
dedent|''
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'compute_fill_first_cost_fn_weight'"
op|','
number|'1'
op|','
nl|'\n'
string|"'How much weight to give the fill-first cost function'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|compute_fill_first_cost_fn
name|'def'
name|'compute_fill_first_cost_fn'
op|'('
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Prefer hosts that have less ram available, filter_hosts will exclude\n    hosts that don\'t have enough ram"""'
newline|'\n'
name|'hostname'
op|','
name|'caps'
op|'='
name|'host'
newline|'\n'
name|'free_mem'
op|'='
name|'caps'
op|'['
string|"'host_memory_free'"
op|']'
newline|'\n'
name|'return'
name|'free_mem'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LeastCostScheduler
dedent|''
name|'class'
name|'LeastCostScheduler'
op|'('
name|'zone_aware_scheduler'
op|'.'
name|'ZoneAwareScheduler'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cost_fns_cache'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'LeastCoastScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_cost_fns
dedent|''
name|'def'
name|'get_cost_fns'
op|'('
name|'self'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of tuples containing weights and cost functions to\n        use for weighing hosts\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'topic'
name|'in'
name|'self'
op|'.'
name|'cost_fns_cache'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'cost_fns_cache'
op|'['
name|'topic'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'cost_fns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cost_fn_str'
name|'in'
name|'FLAGS'
op|'.'
name|'least_cost_scheduler_cost_functions'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'cost_fn_str'
op|'.'
name|'startswith'
op|'('
string|"'%s_'"
op|'%'
name|'topic'
op|')'
name|'and'
name|'not'
name|'cost_fn_str'
op|'.'
name|'startswith'
op|'('
string|"'noop'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(sirp): import_class is somewhat misnamed since it can'
nl|'\n'
comment|'# any callable from a module'
nl|'\n'
indent|'                '
name|'cost_fn'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'cost_fn_str'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ClassNotFound'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerCostFunctionNotFound'
op|'('
nl|'\n'
name|'cost_fn_str'
op|'='
name|'cost_fn_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'weight'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|'"%s_weight"'
op|'%'
name|'cost_fn'
op|'.'
name|'__name__'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerWeightFlagNotFound'
op|'('
nl|'\n'
name|'flag_name'
op|'='
name|'flag_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cost_fns'
op|'.'
name|'append'
op|'('
op|'('
name|'weight'
op|','
name|'cost_fn'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'cost_fns_cache'
op|'['
name|'topic'
op|']'
op|'='
name|'cost_fns'
newline|'\n'
name|'return'
name|'cost_fns'
newline|'\n'
nl|'\n'
DECL|member|weigh_hosts
dedent|''
name|'def'
name|'weigh_hosts'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of dictionaries of form:\n           [ {weight: weight, hostname: hostname, capabilities: capabs} ]\n        """'
newline|'\n'
nl|'\n'
name|'cost_fns'
op|'='
name|'self'
op|'.'
name|'get_cost_fns'
op|'('
name|'topic'
op|')'
newline|'\n'
name|'costs'
op|'='
name|'weighted_sum'
op|'('
name|'domain'
op|'='
name|'hosts'
op|','
name|'weighted_fns'
op|'='
name|'cost_fns'
op|')'
newline|'\n'
nl|'\n'
name|'weighted'
op|'='
op|'['
op|']'
newline|'\n'
name|'weight_log'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cost'
op|','
op|'('
name|'hostname'
op|','
name|'caps'
op|')'
name|'in'
name|'zip'
op|'('
name|'costs'
op|','
name|'hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'weight_log'
op|'.'
name|'append'
op|'('
string|'"%s: %s"'
op|'%'
op|'('
name|'hostname'
op|','
string|'"%.2f"'
op|'%'
name|'cost'
op|')'
op|')'
newline|'\n'
name|'weight_dict'
op|'='
name|'dict'
op|'('
name|'weight'
op|'='
name|'cost'
op|','
name|'hostname'
op|'='
name|'hostname'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'caps'
op|')'
newline|'\n'
name|'weighted'
op|'.'
name|'append'
op|'('
name|'weight_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Weighted Costs => %s"'
op|')'
op|'%'
name|'weight_log'
op|')'
newline|'\n'
name|'return'
name|'weighted'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|normalize_list
dedent|''
dedent|''
name|'def'
name|'normalize_list'
op|'('
name|'L'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Normalize an array of numbers such that each element satisfies:\n        0 <= e <= 1"""'
newline|'\n'
name|'if'
name|'not'
name|'L'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'L'
newline|'\n'
dedent|''
name|'max_'
op|'='
name|'max'
op|'('
name|'L'
op|')'
newline|'\n'
name|'if'
name|'max_'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'('
name|'float'
op|'('
name|'e'
op|')'
op|'/'
name|'max_'
op|')'
name|'for'
name|'e'
name|'in'
name|'L'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'L'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|weighted_sum
dedent|''
name|'def'
name|'weighted_sum'
op|'('
name|'domain'
op|','
name|'weighted_fns'
op|','
name|'normalize'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use the weighted-sum method to compute a score for an array of objects.\n    Normalize the results of the objective-functions so that the weights are\n    meaningful regardless of objective-function\'s range.\n\n    domain - input to be scored\n    weighted_fns - list of weights and functions like:\n        [(weight, objective-functions)]\n\n    Returns an unsorted list of scores. To pair with hosts do:\n        zip(scores, hosts)\n    """'
newline|'\n'
comment|'# Table of form:'
nl|'\n'
comment|'#   { domain1: [score1, score2, ..., scoreM]'
nl|'\n'
comment|'#     ...'
nl|'\n'
comment|'#     domainN: [score1, score2, ..., scoreM] }'
nl|'\n'
name|'score_table'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'for'
name|'weight'
op|','
name|'fn'
name|'in'
name|'weighted_fns'
op|':'
newline|'\n'
indent|'        '
name|'scores'
op|'='
op|'['
name|'fn'
op|'('
name|'elem'
op|')'
name|'for'
name|'elem'
name|'in'
name|'domain'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'normalize'
op|':'
newline|'\n'
indent|'            '
name|'norm_scores'
op|'='
name|'normalize_list'
op|'('
name|'scores'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'norm_scores'
op|'='
name|'scores'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'idx'
op|','
name|'score'
name|'in'
name|'enumerate'
op|'('
name|'norm_scores'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'weighted_score'
op|'='
name|'score'
op|'*'
name|'weight'
newline|'\n'
name|'score_table'
op|'['
name|'idx'
op|']'
op|'.'
name|'append'
op|'('
name|'weighted_score'
op|')'
newline|'\n'
nl|'\n'
comment|'# Sum rows in table to compute score for each element in domain'
nl|'\n'
dedent|''
dedent|''
name|'domain_scores'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'idx'
name|'in'
name|'sorted'
op|'('
name|'score_table'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'elem_score'
op|'='
name|'sum'
op|'('
name|'score_table'
op|'['
name|'idx'
op|']'
op|')'
newline|'\n'
name|'domain_scores'
op|'.'
name|'append'
op|'('
name|'elem_score'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'domain_scores'
newline|'\n'
dedent|''
endmarker|''
end_unit
