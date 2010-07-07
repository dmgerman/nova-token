begin_unit
comment|'#!/opt/local/bin/python'
nl|'\n'
nl|'\n'
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'# '
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
string|'"""\ndhcpleasor.py\n\nHandle lease database updates from DHCP servers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'append'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'__file__'
op|','
string|'"../../"'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'sys'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'import'
name|'getopt'
newline|'\n'
name|'from'
name|'os'
name|'import'
name|'environ'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'linux_net'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|add_lease
name|'def'
name|'add_lease'
op|'('
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'.'
name|'lease_ip'
op|'('
name|'ip'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'FLAGS'
op|'.'
name|'cloud_topic'
op|','
op|'{'
string|'"method"'
op|':'
string|'"lease_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"address"'
op|':'
name|'ip'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|old_lease
dedent|''
dedent|''
name|'def'
name|'old_lease'
op|'('
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Adopted old lease or got a change of mac/hostname"'
op|')'
newline|'\n'
nl|'\n'
DECL|function|del_lease
dedent|''
name|'def'
name|'del_lease'
op|'('
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'        '
name|'network'
op|'.'
name|'release_ip'
op|'('
name|'ip'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'FLAGS'
op|'.'
name|'cloud_topic'
op|','
op|'{'
string|'"method"'
op|':'
string|'"release_ip"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"address"'
op|':'
name|'ip'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|init_leases
dedent|''
dedent|''
name|'def'
name|'init_leases'
op|'('
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'net'
op|'='
name|'network'
op|'.'
name|'get_network_by_interface'
op|'('
name|'interface'
op|')'
newline|'\n'
name|'res'
op|'='
string|'""'
newline|'\n'
name|'for'
name|'host_name'
name|'in'
name|'net'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'+='
string|'"%s\\n"'
op|'%'
name|'linux_net'
op|'.'
name|'hostDHCP'
op|'('
name|'net'
op|','
name|'host_name'
op|','
name|'net'
op|'.'
name|'hosts'
op|'['
name|'host_name'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
name|'def'
name|'main'
op|'('
name|'argv'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'argv'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'argv'
op|'='
name|'sys'
op|'.'
name|'argv'
newline|'\n'
dedent|''
name|'interface'
op|'='
name|'environ'
op|'.'
name|'get'
op|'('
string|"'DNSMASQ_INTERFACE'"
op|','
string|"'br0'"
op|')'
newline|'\n'
name|'if'
name|'int'
op|'('
name|'environ'
op|'.'
name|'get'
op|'('
string|"'TESTING'"
op|','
string|"'0'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'redis_db'
op|'='
number|'8'
newline|'\n'
name|'FLAGS'
op|'.'
name|'network_size'
op|'='
number|'32'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_libvirt'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_network'
op|'='
name|'True'
newline|'\n'
name|'FLAGS'
op|'.'
name|'fake_users'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'action'
op|'='
name|'argv'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'action'
name|'in'
op|'['
string|"'add'"
op|','
string|"'del'"
op|','
string|"'old'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'mac'
op|'='
name|'argv'
op|'['
number|'2'
op|']'
newline|'\n'
name|'ip'
op|'='
name|'argv'
op|'['
number|'3'
op|']'
newline|'\n'
name|'hostname'
op|'='
name|'argv'
op|'['
number|'4'
op|']'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Called %s for mac %s with ip %s and hostname %s on interface %s"'
op|'%'
op|'('
name|'action'
op|','
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
name|'globals'
op|'('
op|')'
op|'['
name|'action'
op|'+'
string|"'_lease'"
op|']'
op|'('
name|'mac'
op|','
name|'ip'
op|','
name|'hostname'
op|','
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'init_leases'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'exit'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'exit'
op|'('
name|'main'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
