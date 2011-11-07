begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California'
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
comment|'#'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'tilera'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'fake'
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
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|global_opts
name|'global_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'baremetal_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'tilera'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Bare-metal driver runs on'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'FLAGS'
op|'.'
name|'add_options'
op|'('
name|'global_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_baremetal_nodes
name|'def'
name|'get_baremetal_nodes'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'d'
op|'='
name|'FLAGS'
op|'.'
name|'baremetal_driver'
newline|'\n'
name|'if'
name|'d'
op|'=='
string|"'tilera'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'tilera'
op|'.'
name|'get_baremetal_nodes'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'d'
op|'=='
string|"'fake'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fake'
op|'.'
name|'get_baremetal_nodes'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Unknown baremetal driver %(d)s"'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
