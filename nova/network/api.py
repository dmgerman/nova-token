begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nHandles all requests relating to instances (guest vms).\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
name|'import'
name|'quota'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.network'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the network manager."""'
newline|'\n'
nl|'\n'
DECL|member|allocate_floating_ip
name|'def'
name|'allocate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'quota'
op|'.'
name|'allowed_floating_ips'
op|'('
name|'context'
op|','
number|'1'
op|')'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Quota exceeeded for %s, tried to allocate "'
nl|'\n'
string|'"address"'
op|')'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'raise'
name|'quota'
op|'.'
name|'QuotaError'
op|'('
name|'_'
op|'('
string|'"Address quota exceeded. You cannot "'
nl|'\n'
string|'"allocate any more addresses"'
op|')'
op|')'
newline|'\n'
comment|"# NOTE(vish): We don't know which network host should get the ip"
nl|'\n'
comment|'#             when we allocate, so just send it to any one.  This'
nl|'\n'
comment|'#             will probably need to move into a network supervisor'
nl|'\n'
comment|'#             at some point.'
nl|'\n'
dedent|''
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"allocate_floating_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"project_id"'
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release_floating_ip
dedent|''
name|'def'
name|'release_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
comment|"# NOTE(vish): We don't know which network host should get the ip"
nl|'\n'
comment|'#             when we deallocate, so just send it to any one.  This'
nl|'\n'
comment|'#             will probably need to move into a network supervisor'
nl|'\n'
comment|'#             at some point.'
nl|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"deallocate_floating_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"floating_address"'
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|associate_floating_ip
dedent|''
name|'def'
name|'associate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'fixed_ip'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'fixed_ip'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'fixed_ip_get_by_address'
op|'('
name|'context'
op|','
name|'fixed_ip'
op|')'
newline|'\n'
dedent|''
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'floating_ip'
op|')'
newline|'\n'
comment|'# Check if the floating ip address is allocated'
nl|'\n'
name|'if'
name|'floating_ip'
op|'['
string|"'project_id'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Address (%(address)s) is not "'
nl|'\n'
string|'"allocated"'
op|')'
op|'%'
op|'{'
string|"'address'"
op|':'
nl|'\n'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|')'
newline|'\n'
comment|'# Check if the floating ip address is allocated to the same project'
nl|'\n'
dedent|''
name|'if'
name|'floating_ip'
op|'['
string|"'project_id'"
op|']'
op|'!='
name|'context'
op|'.'
name|'project_id'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Address (%(address)s) is not allocated to your "'
nl|'\n'
string|'"project (%(project)s)"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|'"Address (%(address)s) is not "'
nl|'\n'
string|'"allocated to your project"'
nl|'\n'
string|'"(%(project)s)"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
op|')'
newline|'\n'
comment|'# NOTE(vish): Perhaps we should just pass this on to compute and'
nl|'\n'
comment|'#             let compute communicate with network.'
nl|'\n'
dedent|''
name|'host'
op|'='
name|'fixed_ip'
op|'['
string|"'network'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"associate_floating_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"floating_address"'
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
string|'"fixed_address"'
op|':'
name|'fixed_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|disassociate_floating_ip
dedent|''
name|'def'
name|'disassociate_floating_ip'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'floating_ip_get_by_address'
op|'('
name|'context'
op|','
name|'address'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'floating_ip'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
string|"'Address is not associated.'"
op|')'
newline|'\n'
comment|'# NOTE(vish): Get the topic from the host name of the network of'
nl|'\n'
comment|'#             the associated fixed ip.'
nl|'\n'
dedent|''
name|'host'
op|'='
name|'floating_ip'
op|'['
string|"'fixed_ip'"
op|']'
op|'['
string|"'network'"
op|']'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'network_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"disassociate_floating_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"floating_address"'
op|':'
name|'floating_ip'
op|'['
string|"'address'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
