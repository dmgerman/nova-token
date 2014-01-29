begin_unit
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
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
name|'compute'
op|'.'
name|'resources'
name|'import'
name|'base'
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
DECL|class|VCPU
name|'class'
name|'VCPU'
op|'('
name|'base'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""VCPU compute resource plugin.\n\n    This is effectively a simple counter based on the vcpu requirement of each\n    instance.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# initialize to a 'zero' resource."
nl|'\n'
comment|'# reset will be called to set real resource values'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_total'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'_used'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|reset
dedent|''
name|'def'
name|'reset'
op|'('
name|'self'
op|','
name|'resources'
op|','
name|'driver'
op|')'
op|':'
newline|'\n'
comment|'# total vcpu is reset to the value taken from resources.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_total'
op|'='
name|'int'
op|'('
name|'resources'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_used'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|_get_requested
dedent|''
name|'def'
name|'_get_requested'
op|'('
name|'self'
op|','
name|'usage'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'usage'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_limit
dedent|''
name|'def'
name|'_get_limit'
op|'('
name|'self'
op|','
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'limits'
name|'and'
string|"'vcpu'"
name|'in'
name|'limits'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'limits'
op|'.'
name|'get'
op|'('
string|"'vcpu'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test
dedent|''
dedent|''
name|'def'
name|'test'
op|'('
name|'self'
op|','
name|'usage'
op|','
name|'limits'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requested'
op|'='
name|'self'
op|'.'
name|'_get_requested'
op|'('
name|'usage'
op|')'
newline|'\n'
name|'limit'
op|'='
name|'self'
op|'.'
name|'_get_limit'
op|'('
name|'limits'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Total CPUs: %(total)d VCPUs, used: %(used).02f VCPUs'"
op|'%'
nl|'\n'
op|'{'
string|"'total'"
op|':'
name|'self'
op|'.'
name|'_total'
op|','
string|"'used'"
op|':'
name|'self'
op|'.'
name|'_used'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'limit'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# treat resource as unlimited:'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'CPUs limit not specified, defaulting to unlimited'"
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'free'
op|'='
name|'limit'
op|'-'
name|'self'
op|'.'
name|'_used'
newline|'\n'
nl|'\n'
comment|'# Oversubscribed resource policy info:'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'CPUs limit: %(limit).02f VCPUs, free: %(free).02f VCPUs'"
op|'%'
nl|'\n'
op|'{'
string|"'limit'"
op|':'
name|'limit'
op|','
string|"'free'"
op|':'
name|'free'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'requested'
op|'>'
name|'free'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
string|"'Free CPUs %(free).02f VCPUs < '"
nl|'\n'
string|"'requested %(requested)d VCPUs'"
op|'%'
nl|'\n'
op|'{'
string|"'free'"
op|':'
name|'free'
op|','
string|"'requested'"
op|':'
name|'requested'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_instance
dedent|''
dedent|''
name|'def'
name|'add_instance'
op|'('
name|'self'
op|','
name|'usage'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requested'
op|'='
name|'int'
op|'('
name|'usage'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_used'
op|'+='
name|'requested'
newline|'\n'
nl|'\n'
DECL|member|remove_instance
dedent|''
name|'def'
name|'remove_instance'
op|'('
name|'self'
op|','
name|'usage'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'requested'
op|'='
name|'int'
op|'('
name|'usage'
op|'.'
name|'get'
op|'('
string|"'vcpus'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_used'
op|'-='
name|'requested'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'resources'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'self'
op|'.'
name|'_total'
newline|'\n'
name|'resources'
op|'['
string|"'vcpus_used'"
op|']'
op|'='
name|'self'
op|'.'
name|'_used'
newline|'\n'
nl|'\n'
DECL|member|report_free
dedent|''
name|'def'
name|'report_free'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'free_vcpus'
op|'='
name|'self'
op|'.'
name|'_total'
op|'-'
name|'self'
op|'.'
name|'_used'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Free VCPUs: %s'"
op|'%'
name|'free_vcpus'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
