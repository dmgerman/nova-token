begin_unit
comment|'# Copyright 2013 Nicira, Inc.'
nl|'\n'
comment|'# All Rights Reserved'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
DECL|variable|security_group_opts
name|'security_group_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'security_group_api'"
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
string|"'The full class name of the security API class'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'security_group_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|NOVA_DRIVER
name|'NOVA_DRIVER'
op|'='
op|'('
string|"'nova.api.openstack.compute.contrib.security_groups.'"
nl|'\n'
string|"'NativeNovaSecurityGroupAPI'"
op|')'
newline|'\n'
DECL|variable|NEUTRON_DRIVER
name|'NEUTRON_DRIVER'
op|'='
op|'('
string|"'nova.api.openstack.compute.contrib.security_groups.'"
nl|'\n'
string|"'NativeNeutronSecurityGroupAPI'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_openstack_security_group_driver
name|'def'
name|'get_openstack_security_group_driver'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'CONF'
op|'.'
name|'security_group_api'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'nova'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'NOVA_DRIVER'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'security_group_api'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
op|'('
string|"'neutron'"
op|','
string|"'quantum'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'NEUTRON_DRIVER'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'security_group_api'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_neutron_security_groups
dedent|''
dedent|''
name|'def'
name|'is_neutron_security_groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'CONF'
op|'.'
name|'security_group_api'
op|'.'
name|'lower'
op|'('
op|')'
name|'in'
op|'('
string|"'neutron'"
op|','
string|"'quantum'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
