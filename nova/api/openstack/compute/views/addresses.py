begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'common'
op|'.'
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Models server addresses as a dictionary."""'
newline|'\n'
nl|'\n'
DECL|variable|_collection_name
name|'_collection_name'
op|'='
string|'"addresses"'
newline|'\n'
nl|'\n'
DECL|member|basic
name|'def'
name|'basic'
op|'('
name|'self'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary describing an IP address."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|'"version"'
op|':'
name|'ip'
op|'['
string|'"version"'
op|']'
op|','
nl|'\n'
string|'"addr"'
op|':'
name|'ip'
op|'['
string|'"address"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'network'
op|','
name|'label'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dictionary describing a network."""'
newline|'\n'
name|'all_ips'
op|'='
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'network'
op|'['
string|'"ips"'
op|']'
op|','
name|'network'
op|'['
string|'"floating_ips"'
op|']'
op|')'
newline|'\n'
name|'return'
op|'{'
name|'label'
op|':'
op|'['
name|'self'
op|'.'
name|'basic'
op|'('
name|'ip'
op|')'
name|'for'
name|'ip'
name|'in'
name|'all_ips'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'networks'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a dictionary describing a list of networks."""'
newline|'\n'
name|'addresses'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'label'
op|','
name|'network'
name|'in'
name|'networks'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_dict'
op|'='
name|'self'
op|'.'
name|'show'
op|'('
name|'network'
op|','
name|'label'
op|')'
newline|'\n'
name|'addresses'
op|'['
name|'label'
op|']'
op|'='
name|'network_dict'
op|'['
name|'label'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'dict'
op|'('
name|'addresses'
op|'='
name|'addresses'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
