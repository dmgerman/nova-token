begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
name|'import'
name|'context'
newline|'\n'
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
string|"'nova.virt.conn_common'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/interfaces.template'"
op|')'
op|','
nl|'\n'
string|"'Template file for injected network'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|get_injectables
name|'def'
name|'get_injectables'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'key'
op|'='
name|'str'
op|'('
name|'inst'
op|'['
string|"'key_data'"
op|']'
op|')'
newline|'\n'
name|'net'
op|'='
name|'None'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get_by_instance'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'network_ref'
op|'['
string|"'injected'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'address'
op|'='
name|'db'
op|'.'
name|'instance_get_fixed_address'
op|'('
name|'admin_context'
op|','
name|'inst'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'ra_server'
op|'='
name|'network_ref'
op|'['
string|"'ra_server'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'ra_server'
op|':'
newline|'\n'
indent|'            '
name|'ra_server'
op|'='
string|'"fd00::"'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'FLAGS'
op|'.'
name|'injected_network_template'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'net'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|'%'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'network_ref'
op|'['
string|"'netmask'"
op|']'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'network_ref'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"'broadcast'"
op|':'
name|'network_ref'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'network_ref'
op|'['
string|"'dns'"
op|']'
op|','
nl|'\n'
string|"'ra_server'"
op|':'
name|'ra_server'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'key'
op|','
name|'net'
newline|'\n'
dedent|''
endmarker|''
end_unit
