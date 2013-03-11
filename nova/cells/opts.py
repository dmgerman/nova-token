begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nGlobal cells config options\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|cells_opts
name|'cells_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enable'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Enable cell functionality'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cells'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic cells nodes listen on'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cells.manager.CellsManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Manager for cells'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'name of this cell'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'capabilities'"
op|','
nl|'\n'
name|'default'
op|'='
op|'['
string|"'hypervisor=xenserver;kvm'"
op|','
string|"'os=linux;windows'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Key/Multi-value list with the capabilities of the cell'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'call_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds to wait for response from a call to a cell.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'reserve_percent'"
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
string|"'Percentage of cell capacity to hold in reserve. '"
nl|'\n'
string|"'Affects both memory and disk utilization'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'cells_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
endmarker|''
end_unit
