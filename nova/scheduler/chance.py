begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Openstack, LLC.'
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
string|'"""\nChance (Random) Scheduler implementation\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'base'
name|'import'
name|'Scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ChanceScheduler
name|'class'
name|'ChanceScheduler'
op|'('
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Implements Scheduler as a random node selector\n    """'
newline|'\n'
nl|'\n'
DECL|member|pick_node
name|'def'
name|'pick_node'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Picks a node that is up at random\n        """'
newline|'\n'
nl|'\n'
name|'nodes'
op|'='
name|'self'
op|'.'
name|'compute_nodes_up'
op|'('
op|')'
newline|'\n'
name|'return'
name|'nodes'
op|'['
name|'int'
op|'('
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'*'
name|'len'
op|'('
name|'nodes'
op|')'
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
