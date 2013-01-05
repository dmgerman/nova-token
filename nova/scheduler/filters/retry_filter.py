begin_unit
comment|'# Copyright (c) 2012 OpenStack, LLC.'
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
DECL|class|RetryFilter
name|'class'
name|'RetryFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Filter out nodes that have already been attempted for scheduling\n    purposes\n    """'
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
string|'"""Skip nodes that have already been attempted"""'
newline|'\n'
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'retry'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'retry'
op|':'
newline|'\n'
comment|'# Re-scheduling is disabled'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Re-scheduling is disabled"'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'hosts'
op|'='
name|'retry'
op|'.'
name|'get'
op|'('
string|"'hosts'"
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'host'
op|'='
op|'['
name|'host_state'
op|'.'
name|'host'
op|','
name|'host_state'
op|'.'
name|'nodename'
op|']'
newline|'\n'
nl|'\n'
name|'passes'
op|'='
name|'host'
name|'not'
name|'in'
name|'hosts'
newline|'\n'
name|'pass_msg'
op|'='
string|'"passes"'
name|'if'
name|'passes'
name|'else'
string|'"fails"'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Host %(host)s %(pass_msg)s.  Previously tried hosts: "'
nl|'\n'
string|'"%(hosts)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# Host passes if it's not in the list of previously attempted hosts:"
nl|'\n'
name|'return'
name|'passes'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
