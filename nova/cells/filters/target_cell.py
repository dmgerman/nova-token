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
string|'"""\nTarget cell filter.\n\nA scheduler hint of \'target_cell\' with a value of a full cell name may be\nspecified to route a build to a particular cell.  No error handling is\ndone as there\'s no way to know whether the full path is a valid.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
DECL|class|TargetCellFilter
name|'class'
name|'TargetCellFilter'
op|'('
name|'filters'
op|'.'
name|'BaseCellFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Target cell filter.  Works by specifying a scheduler hint of\n    \'target_cell\'. The value should be the full cell path.\n    """'
newline|'\n'
nl|'\n'
DECL|member|filter_all
name|'def'
name|'filter_all'
op|'('
name|'self'
op|','
name|'cells'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Override filter_all() which operates on the full list\n        of cells...\n        """'
newline|'\n'
name|'scheduler_hints'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'scheduler_hints'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'scheduler_hints'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cells'
newline|'\n'
nl|'\n'
comment|'# This filter only makes sense at the top level, as a full'
nl|'\n'
comment|"# cell name is specified.  So we pop 'target_cell' out of the"
nl|'\n'
comment|'# hints dict.'
nl|'\n'
dedent|''
name|'cell_name'
op|'='
name|'scheduler_hints'
op|'.'
name|'pop'
op|'('
string|"'target_cell'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cell_name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cells'
newline|'\n'
nl|'\n'
comment|'# This authorization is after popping off target_cell, so'
nl|'\n'
comment|"# that in case this fails, 'target_cell' is not left in the"
nl|'\n'
comment|'# dict when child cells go to schedule.'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'authorized'
op|'('
name|'filter_properties'
op|'['
string|"'context'"
op|']'
op|')'
op|':'
newline|'\n'
comment|'# No filtering, if not authorized.'
nl|'\n'
indent|'            '
name|'return'
name|'cells'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Forcing direct route to %(cell_name)s because "'
nl|'\n'
string|'"of \'target_cell\' scheduler hint"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'cell_name'"
op|':'
name|'cell_name'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'scheduler'
op|'='
name|'filter_properties'
op|'['
string|"'scheduler'"
op|']'
newline|'\n'
name|'if'
name|'cell_name'
op|'=='
name|'filter_properties'
op|'['
string|"'routing_path'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'scheduler'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
op|']'
newline|'\n'
dedent|''
name|'ctxt'
op|'='
name|'filter_properties'
op|'['
string|"'context'"
op|']'
newline|'\n'
nl|'\n'
name|'scheduler'
op|'.'
name|'msg_runner'
op|'.'
name|'build_instances'
op|'('
name|'ctxt'
op|','
name|'cell_name'
op|','
nl|'\n'
name|'filter_properties'
op|'['
string|"'host_sched_kwargs'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Returning None means to skip further scheduling, because we'
nl|'\n'
comment|'# handled it.'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
