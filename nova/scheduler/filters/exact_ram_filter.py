begin_unit
comment|'# Copyright (c) 2014 OpenStack Foundation'
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
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
DECL|class|ExactRamFilter
name|'class'
name|'ExactRamFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Exact RAM Filter."""'
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
name|'spec_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if host has the exact amount of RAM available."""'
newline|'\n'
name|'requested_ram'
op|'='
name|'spec_obj'
op|'.'
name|'memory_mb'
newline|'\n'
name|'if'
name|'requested_ram'
op|'!='
name|'host_state'
op|'.'
name|'free_ram_mb'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not have exactly "'
nl|'\n'
string|'"%(requested_ram)s MB usable RAM, it has "'
nl|'\n'
string|'"%(usable_ram)s MB."'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'requested_ram'"
op|':'
name|'requested_ram'
op|','
nl|'\n'
string|"'usable_ram'"
op|':'
name|'host_state'
op|'.'
name|'free_ram_mb'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# NOTE(mgoddard): Setting the limit ensures that it is enforced in'
nl|'\n'
comment|'# compute. This ensures that if multiple instances are scheduled to a'
nl|'\n'
comment|'# single host, then all after the first will fail in the claim.'
nl|'\n'
dedent|''
name|'host_state'
op|'.'
name|'limits'
op|'['
string|"'memory_mb'"
op|']'
op|'='
name|'host_state'
op|'.'
name|'total_usable_ram_mb'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
