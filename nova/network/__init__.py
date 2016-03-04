begin_unit
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
name|'import'
name|'oslo_config'
op|'.'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
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
DECL|variable|NOVA_NET_API
name|'NOVA_NET_API'
op|'='
string|"'nova.network.api.API'"
newline|'\n'
DECL|variable|NEUTRON_NET_API
name|'NEUTRON_NET_API'
op|'='
string|"'nova.network.neutronv2.api.API'"
newline|'\n'
nl|'\n'
DECL|variable|_network_opts
name|'_network_opts'
op|'='
op|'['
nl|'\n'
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'network_api_class'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'NOVA_NET_API'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: The full class name of the '"
nl|'\n'
string|"'network API class to use. ``use_neutron`` '"
nl|'\n'
string|"'should be used instead.'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_neutron'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nWhether to use Neutron or Nova Network as the back end for networking.\nDefaults to False (indicating Nova network). Set to True to use neutron.\n"""'
op|')'
nl|'\n'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'_network_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|API
name|'def'
name|'API'
op|'('
name|'skip_policy_check'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'legacy_class'
op|'='
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'network_api_class'
newline|'\n'
name|'use_neutron'
op|'='
name|'oslo_config'
op|'.'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'use_neutron'
newline|'\n'
nl|'\n'
name|'if'
name|'legacy_class'
op|'=='
name|'NEUTRON_NET_API'
name|'and'
name|'not'
name|'use_neutron'
op|':'
newline|'\n'
comment|'# If they specified neutron via class, we should respect that'
nl|'\n'
indent|'        '
name|'network_api_class'
op|'='
name|'legacy_class'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Config mismatch. The network_api_class specifies %s, "'
nl|'\n'
string|'"however use_neutron is not set to True. Using Neutron "'
nl|'\n'
string|'"networking for now, however please set use_neutron to "'
nl|'\n'
string|'"True in your configuration as network_api_class is "'
nl|'\n'
string|'"deprecated and will be removed."'
op|')'
op|','
name|'legacy_class'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'use_neutron'
op|':'
newline|'\n'
indent|'        '
name|'network_api_class'
op|'='
name|'NEUTRON_NET_API'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'network_api_class'
op|'='
name|'NOVA_NET_API'
newline|'\n'
nl|'\n'
dedent|''
name|'cls'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'network_api_class'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'skip_policy_check'
op|'='
name|'skip_policy_check'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
