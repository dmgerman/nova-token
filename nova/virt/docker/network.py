begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2014 OpenStack Foundation'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
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
name|'log'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|teardown_network
name|'def'
name|'teardown_network'
op|'('
name|'container_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'output'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'-o'"
op|','
string|"'netns'"
op|','
string|"'list'"
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'output'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'container_id'
op|'=='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ip'"
op|','
string|"'netns'"
op|','
string|"'delete'"
op|','
name|'container_id'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Cannot remove network namespace, netns id: %s'"
op|')'
op|','
nl|'\n'
name|'container_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_fixed_ip
dedent|''
dedent|''
name|'def'
name|'find_fixed_ip'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'subnet'
name|'in'
name|'network_info'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'netmask'
op|'='
name|'subnet'
op|'['
string|"'cidr'"
op|']'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'subnet'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ip'
op|'['
string|"'type'"
op|']'
op|'=='
string|"'fixed'"
name|'and'
name|'ip'
op|'['
string|"'address'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ip'
op|'['
string|"'address'"
op|']'
op|'+'
string|'"/"'
op|'+'
name|'netmask'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
name|'_'
op|'('
string|"'Cannot find fixed ip'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_gateway
dedent|''
name|'def'
name|'find_gateway'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'subnet'
name|'in'
name|'network_info'
op|'['
string|"'subnets'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'subnet'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|'('
name|'_'
op|'('
string|"'Cannot find gateway'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
