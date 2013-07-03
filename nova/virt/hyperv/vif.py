begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
nl|'\n'
comment|'# Copyright 2013 Pedro Navarro Perez'
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
name|'abc'
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
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'networkutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
DECL|variable|hyperv_opts
name|'hyperv_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vswitch_name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'External virtual switch Name, '"
nl|'\n'
string|"'if not provided, the first external virtual '"
nl|'\n'
string|"'switch is used'"
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
name|'hyperv_opts'
op|','
string|"'hyperv'"
op|')'
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
DECL|class|HyperVBaseVIFDriver
name|'class'
name|'HyperVBaseVIFDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|plug
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|unplug
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HyperVNeutronVIFDriver
dedent|''
dedent|''
name|'class'
name|'HyperVNeutronVIFDriver'
op|'('
name|'HyperVBaseVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Neutron VIF driver."""'
newline|'\n'
nl|'\n'
DECL|member|plug
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
comment|'# Neutron takes care of plugging the port'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
comment|'# Neutron takes care of unplugging the port'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HyperVNovaNetworkVIFDriver
dedent|''
dedent|''
name|'class'
name|'HyperVNovaNetworkVIFDriver'
op|'('
name|'HyperVBaseVIFDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Nova network VIF driver."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_vmutils'
op|'='
name|'vmutils'
op|'.'
name|'VMUtils'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_netutils'
op|'='
name|'networkutils'
op|'.'
name|'NetworkUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|plug
dedent|''
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vswitch_path'
op|'='
name|'self'
op|'.'
name|'_netutils'
op|'.'
name|'get_external_vswitch'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'vswitch_name'
op|')'
newline|'\n'
nl|'\n'
name|'vm_name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating vswitch port for instance: %s'"
op|')'
op|'%'
name|'vm_name'
op|')'
newline|'\n'
name|'vswitch_port'
op|'='
name|'self'
op|'.'
name|'_netutils'
op|'.'
name|'create_vswitch_port'
op|'('
name|'vswitch_path'
op|','
nl|'\n'
name|'vm_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmutils'
op|'.'
name|'set_nic_connection'
op|'('
name|'vm_name'
op|','
name|'vif'
op|'['
string|"'id'"
op|']'
op|','
name|'vswitch_port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
comment|'#TODO(alepilotti) Not implemented'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
