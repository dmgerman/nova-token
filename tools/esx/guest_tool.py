begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nGuest tools for ESX to set up network in the guest.\nOn Windows we require pyWin32 installed on Python.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'array'
newline|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'platform'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'struct'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|','
name|'unicode'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|PLATFORM_WIN
name|'PLATFORM_WIN'
op|'='
string|"'win32'"
newline|'\n'
DECL|variable|PLATFORM_LINUX
name|'PLATFORM_LINUX'
op|'='
string|"'linux2'"
newline|'\n'
DECL|variable|ARCH_32_BIT
name|'ARCH_32_BIT'
op|'='
string|"'32bit'"
newline|'\n'
DECL|variable|ARCH_64_BIT
name|'ARCH_64_BIT'
op|'='
string|"'64bit'"
newline|'\n'
DECL|variable|NO_MACHINE_ID
name|'NO_MACHINE_ID'
op|'='
string|"'No machine id'"
newline|'\n'
nl|'\n'
comment|'# Logging'
nl|'\n'
DECL|variable|FORMAT
name|'FORMAT'
op|'='
string|'"%(asctime)s - %(levelname)s - %(message)s"'
newline|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
name|'PLATFORM_WIN'
op|':'
newline|'\n'
DECL|variable|LOG_DIR
indent|'    '
name|'LOG_DIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'ALLUSERSPROFILE'"
op|')'
op|','
string|"'openstack'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'sys'
op|'.'
name|'platform'
op|'=='
name|'PLATFORM_LINUX'
op|':'
newline|'\n'
DECL|variable|LOG_DIR
indent|'    '
name|'LOG_DIR'
op|'='
string|"'/var/log/openstack'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|LOG_DIR
indent|'    '
name|'LOG_DIR'
op|'='
string|"'logs'"
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'LOG_DIR'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'LOG_DIR'
op|')'
newline|'\n'
DECL|variable|LOG_FILENAME
dedent|''
name|'LOG_FILENAME'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'LOG_DIR'
op|','
string|"'openstack-guest-tools.log'"
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'basicConfig'
op|'('
name|'filename'
op|'='
name|'LOG_FILENAME'
op|','
name|'format'
op|'='
name|'FORMAT'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'hexversion'
op|'<'
number|'0x3000000'
op|':'
newline|'\n'
DECL|variable|_byte
indent|'    '
name|'_byte'
op|'='
name|'ord'
comment|'# 2.x chr to integer'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|_byte
indent|'    '
name|'_byte'
op|'='
name|'int'
comment|'# 3.x byte to integer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
dedent|''
name|'class'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'    '
string|'"""Process Execution Error Class."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'exit_code'
op|','
name|'stdout'
op|','
name|'stderr'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exit_code'
op|'='
name|'exit_code'
newline|'\n'
name|'self'
op|'.'
name|'stdout'
op|'='
name|'stdout'
newline|'\n'
name|'self'
op|'.'
name|'stderr'
op|'='
name|'stderr'
newline|'\n'
name|'self'
op|'.'
name|'cmd'
op|'='
name|'cmd'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'exit_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_bytes2int
dedent|''
dedent|''
name|'def'
name|'_bytes2int'
op|'('
name|'bytes'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert bytes to int."""'
newline|'\n'
name|'intgr'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'byt'
name|'in'
name|'bytes'
op|':'
newline|'\n'
indent|'        '
name|'intgr'
op|'='
op|'('
name|'intgr'
op|'<<'
number|'8'
op|')'
op|'+'
name|'_byte'
op|'('
name|'byt'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'intgr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_network_details
dedent|''
name|'def'
name|'_parse_network_details'
op|'('
name|'machine_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Parse the machine_id to get MAC, IP, Netmask and Gateway fields per NIC.\n    machine_id is of the form (\'NIC_record#NIC_record#\', \'\')\n    Each of the NIC will have record NIC_record in the form\n    \'MAC;IP;Netmask;Gateway;Broadcast;DNS\' where \';\' is field separator.\n    Each record is separated by \'#\' from next record.\n    """'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Received machine_id from vmtools : %s"'
op|')'
op|'%'
name|'machine_id'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'network_details'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'machine_id'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'=='
string|'"1"'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'machine_id_str'
name|'in'
name|'machine_id'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|"'#'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'network_info_list'
op|'='
name|'machine_id_str'
op|'.'
name|'split'
op|'('
string|"';'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'network_info_list'
op|')'
op|'%'
number|'6'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'no_grps'
op|'='
name|'len'
op|'('
name|'network_info_list'
op|')'
op|'/'
number|'6'
newline|'\n'
name|'i'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'i'
op|'<'
name|'no_grps'
op|':'
newline|'\n'
indent|'                '
name|'k'
op|'='
name|'i'
op|'*'
number|'6'
newline|'\n'
name|'network_details'
op|'.'
name|'append'
op|'('
op|'('
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|'+'
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|'+'
number|'2'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|'+'
number|'3'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|'+'
number|'4'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'network_info_list'
op|'['
name|'k'
op|'+'
number|'5'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|')'
op|')'
newline|'\n'
name|'i'
op|'+='
number|'1'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"NIC information from vmtools : %s"'
op|')'
op|'%'
name|'network_details'
op|')'
newline|'\n'
name|'return'
name|'network_details'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_windows_network_adapters
dedent|''
name|'def'
name|'_get_windows_network_adapters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the list of windows network adapters."""'
newline|'\n'
name|'import'
name|'win32com'
op|'.'
name|'client'
newline|'\n'
name|'wbem_locator'
op|'='
name|'win32com'
op|'.'
name|'client'
op|'.'
name|'Dispatch'
op|'('
string|"'WbemScripting.SWbemLocator'"
op|')'
newline|'\n'
name|'wbem_service'
op|'='
name|'wbem_locator'
op|'.'
name|'ConnectServer'
op|'('
string|"'.'"
op|','
string|"'root\\cimv2'"
op|')'
newline|'\n'
name|'wbem_network_adapters'
op|'='
name|'wbem_service'
op|'.'
name|'InstancesOf'
op|'('
string|"'Win32_NetworkAdapter'"
op|')'
newline|'\n'
name|'network_adapters'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'wbem_network_adapter'
name|'in'
name|'wbem_network_adapters'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'wbem_network_adapter'
op|'.'
name|'NetConnectionStatus'
op|'=='
number|'2'
name|'or'
name|'wbem_network_adapter'
op|'.'
name|'NetConnectionStatus'
op|'=='
number|'7'
op|':'
newline|'\n'
indent|'            '
name|'adapter_name'
op|'='
name|'wbem_network_adapter'
op|'.'
name|'NetConnectionID'
newline|'\n'
name|'mac_address'
op|'='
name|'wbem_network_adapter'
op|'.'
name|'MacAddress'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'wbem_network_adapter_config'
op|'='
name|'wbem_network_adapter'
op|'.'
name|'associators_'
op|'('
nl|'\n'
string|"'Win32_NetworkAdapterSetting'"
op|','
nl|'\n'
string|"'Win32_NetworkAdapterConfiguration'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'ip_address'
op|'='
string|"''"
newline|'\n'
name|'subnet_mask'
op|'='
string|"''"
newline|'\n'
name|'if'
name|'wbem_network_adapter_config'
op|'.'
name|'IPEnabled'
op|':'
newline|'\n'
indent|'                '
name|'ip_address'
op|'='
name|'wbem_network_adapter_config'
op|'.'
name|'IPAddress'
op|'['
number|'0'
op|']'
newline|'\n'
name|'subnet_mask'
op|'='
name|'wbem_network_adapter_config'
op|'.'
name|'IPSubnet'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'#wbem_network_adapter_config.DefaultIPGateway[0]'
nl|'\n'
dedent|''
name|'network_adapters'
op|'.'
name|'append'
op|'('
op|'{'
string|"'name'"
op|':'
name|'adapter_name'
op|','
nl|'\n'
string|"'mac-address'"
op|':'
name|'mac_address'
op|','
nl|'\n'
string|"'ip-address'"
op|':'
name|'ip_address'
op|','
nl|'\n'
string|"'subnet-mask'"
op|':'
name|'subnet_mask'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'network_adapters'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_linux_network_adapters
dedent|''
name|'def'
name|'_get_linux_network_adapters'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the list of Linux network adapters."""'
newline|'\n'
name|'import'
name|'fcntl'
newline|'\n'
name|'max_bytes'
op|'='
number|'8096'
newline|'\n'
name|'arch'
op|'='
name|'platform'
op|'.'
name|'architecture'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'arch'
op|'=='
name|'ARCH_32_BIT'
op|':'
newline|'\n'
indent|'        '
name|'offset1'
op|'='
number|'32'
newline|'\n'
name|'offset2'
op|'='
number|'32'
newline|'\n'
dedent|''
name|'elif'
name|'arch'
op|'=='
name|'ARCH_64_BIT'
op|':'
newline|'\n'
indent|'        '
name|'offset1'
op|'='
number|'16'
newline|'\n'
name|'offset2'
op|'='
number|'40'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'OSError'
op|'('
name|'_'
op|'('
string|'"Unknown architecture: %s"'
op|')'
op|'%'
name|'arch'
op|')'
newline|'\n'
dedent|''
name|'sock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'names'
op|'='
name|'array'
op|'.'
name|'array'
op|'('
string|"'B'"
op|','
string|"'\\0'"
op|'*'
name|'max_bytes'
op|')'
newline|'\n'
name|'outbytes'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'iL'"
op|','
name|'fcntl'
op|'.'
name|'ioctl'
op|'('
nl|'\n'
name|'sock'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
nl|'\n'
number|'0x8912'
op|','
nl|'\n'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'iL'"
op|','
name|'max_bytes'
op|','
name|'names'
op|'.'
name|'buffer_info'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|')'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'adapter_names'
op|'='
op|'['
name|'names'
op|'.'
name|'tostring'
op|'('
op|')'
op|'['
name|'n_counter'
op|':'
name|'n_counter'
op|'+'
name|'offset1'
op|']'
op|'.'
name|'split'
op|'('
string|"'\\0'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
nl|'\n'
name|'for'
name|'n_counter'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
name|'outbytes'
op|','
name|'offset2'
op|')'
op|']'
newline|'\n'
name|'network_adapters'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'adapter_name'
name|'in'
name|'adapter_names'
op|':'
newline|'\n'
indent|'        '
name|'ip_address'
op|'='
name|'socket'
op|'.'
name|'inet_ntoa'
op|'('
name|'fcntl'
op|'.'
name|'ioctl'
op|'('
nl|'\n'
name|'sock'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
nl|'\n'
number|'0x8915'
op|','
nl|'\n'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'256s'"
op|','
name|'adapter_name'
op|')'
op|')'
op|'['
number|'20'
op|':'
number|'24'
op|']'
op|')'
newline|'\n'
name|'subnet_mask'
op|'='
name|'socket'
op|'.'
name|'inet_ntoa'
op|'('
name|'fcntl'
op|'.'
name|'ioctl'
op|'('
nl|'\n'
name|'sock'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
nl|'\n'
number|'0x891b'
op|','
nl|'\n'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'256s'"
op|','
name|'adapter_name'
op|')'
op|')'
op|'['
number|'20'
op|':'
number|'24'
op|']'
op|')'
newline|'\n'
name|'raw_mac_address'
op|'='
string|"'%012x'"
op|'%'
name|'_bytes2int'
op|'('
name|'fcntl'
op|'.'
name|'ioctl'
op|'('
nl|'\n'
name|'sock'
op|'.'
name|'fileno'
op|'('
op|')'
op|','
nl|'\n'
number|'0x8927'
op|','
nl|'\n'
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'256s'"
op|','
name|'adapter_name'
op|')'
op|')'
op|'['
number|'18'
op|':'
number|'24'
op|']'
op|')'
newline|'\n'
name|'mac_address'
op|'='
string|'":"'
op|'.'
name|'join'
op|'('
op|'['
name|'raw_mac_address'
op|'['
name|'m_counter'
op|':'
name|'m_counter'
op|'+'
number|'2'
op|']'
nl|'\n'
name|'for'
name|'m_counter'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'raw_mac_address'
op|')'
op|','
number|'2'
op|')'
op|']'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'network_adapters'
op|'.'
name|'append'
op|'('
op|'{'
string|"'name'"
op|':'
name|'adapter_name'
op|','
nl|'\n'
string|"'mac-address'"
op|':'
name|'mac_address'
op|','
nl|'\n'
string|"'ip-address'"
op|':'
name|'ip_address'
op|','
nl|'\n'
string|"'subnet-mask'"
op|':'
name|'subnet_mask'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'network_adapters'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_adapter_name_and_ip_address
dedent|''
name|'def'
name|'_get_adapter_name_and_ip_address'
op|'('
name|'network_adapters'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the adapter name based on the MAC address."""'
newline|'\n'
name|'adapter_name'
op|'='
name|'None'
newline|'\n'
name|'ip_address'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'network_adapter'
name|'in'
name|'network_adapters'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'network_adapter'
op|'['
string|"'mac-address'"
op|']'
op|'=='
name|'mac_address'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'adapter_name'
op|'='
name|'network_adapter'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'ip_address'
op|'='
name|'network_adapter'
op|'['
string|"'ip-address'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'adapter_name'
op|','
name|'ip_address'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_win_adapter_name_and_ip_address
dedent|''
name|'def'
name|'_get_win_adapter_name_and_ip_address'
op|'('
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get Windows network adapter name."""'
newline|'\n'
name|'network_adapters'
op|'='
name|'_get_windows_network_adapters'
op|'('
op|')'
newline|'\n'
name|'return'
name|'_get_adapter_name_and_ip_address'
op|'('
name|'network_adapters'
op|','
name|'mac_address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_linux_adapter_name_and_ip_address
dedent|''
name|'def'
name|'_get_linux_adapter_name_and_ip_address'
op|'('
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get Linux network adapter name."""'
newline|'\n'
name|'network_adapters'
op|'='
name|'_get_linux_network_adapters'
op|'('
op|')'
newline|'\n'
name|'return'
name|'_get_adapter_name_and_ip_address'
op|'('
name|'network_adapters'
op|','
name|'mac_address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_execute
dedent|''
name|'def'
name|'_execute'
op|'('
name|'cmd_list'
op|','
name|'process_input'
op|'='
name|'None'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Executes the command with the list of arguments specified."""'
newline|'\n'
name|'cmd'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd_list'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Executing command: \'%s\'"'
op|')'
op|'%'
name|'cmd'
op|')'
newline|'\n'
name|'env'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'obj'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|','
name|'stdin'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'stderr'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'process_input'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
name|'process_input'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'.'
name|'stdin'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'obj'
op|'.'
name|'returncode'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Result was %s"'
op|')'
op|'%'
name|'obj'
op|'.'
name|'returncode'
op|')'
newline|'\n'
name|'if'
name|'check_exit_code'
name|'and'
name|'obj'
op|'.'
name|'returncode'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|'='
name|'result'
newline|'\n'
name|'raise'
name|'ProcessExecutionError'
op|'('
name|'exit_code'
op|'='
name|'obj'
op|'.'
name|'returncode'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'stdout'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'stderr'
op|','
nl|'\n'
name|'cmd'
op|'='
name|'cmd'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_windows_set_networking
dedent|''
name|'def'
name|'_windows_set_networking'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set IP address for the windows VM."""'
newline|'\n'
name|'program_files'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'PROGRAMFILES'"
op|')'
newline|'\n'
name|'program_files_x86'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'PROGRAMFILES(X86)'"
op|')'
newline|'\n'
name|'vmware_tools_bin'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files'
op|','
string|"'VMware'"
op|','
string|"'VMware Tools'"
op|','
nl|'\n'
string|"'vmtoolsd.exe'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files'
op|','
string|"'VMware'"
op|','
nl|'\n'
string|"'VMware Tools'"
op|','
string|"'vmtoolsd.exe'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files'
op|','
string|"'VMware'"
op|','
string|"'VMware Tools'"
op|','
nl|'\n'
string|"'VMwareService.exe'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files'
op|','
string|"'VMware'"
op|','
nl|'\n'
string|"'VMware Tools'"
op|','
string|"'VMwareService.exe'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'program_files_x86'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files_x86'
op|','
nl|'\n'
string|"'VMware'"
op|','
string|"'VMware Tools'"
op|','
nl|'\n'
string|"'VMwareService.exe'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'program_files_x86'
op|','
string|"'VMware'"
op|','
nl|'\n'
string|"'VMware Tools'"
op|','
string|"'VMwareService.exe'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'vmware_tools_bin'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'['
string|'\'"\''
op|'+'
name|'vmware_tools_bin'
op|'+'
string|'\'"\''
op|','
string|"'--cmd'"
op|','
string|"'machine.id.get'"
op|']'
newline|'\n'
name|'for'
name|'network_detail'
name|'in'
name|'_parse_network_details'
op|'('
name|'_execute'
op|'('
name|'cmd'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mac_address'
op|','
name|'ip_address'
op|','
name|'subnet_mask'
op|','
name|'gateway'
op|','
name|'broadcast'
op|','
name|'dns_servers'
op|'='
name|'network_detail'
newline|'\n'
name|'adapter_name'
op|','
name|'current_ip_address'
op|'='
name|'_get_win_adapter_name_and_ip_address'
op|'('
name|'mac_address'
op|')'
newline|'\n'
name|'if'
name|'adapter_name'
name|'and'
name|'not'
name|'ip_address'
op|'=='
name|'current_ip_address'
op|':'
newline|'\n'
indent|'                '
name|'cmd'
op|'='
op|'['
string|"'netsh'"
op|','
string|"'interface'"
op|','
string|"'ip'"
op|','
string|"'set'"
op|','
string|"'address'"
op|','
nl|'\n'
string|'\'name="%s"\''
op|'%'
name|'adapter_name'
op|','
string|"'source=static'"
op|','
name|'ip_address'
op|','
nl|'\n'
name|'subnet_mask'
op|','
name|'gateway'
op|','
string|"'1'"
op|']'
newline|'\n'
name|'_execute'
op|'('
name|'cmd'
op|')'
newline|'\n'
comment|"# Windows doesn't let you manually set the broadcast address"
nl|'\n'
name|'for'
name|'dns_server'
name|'in'
name|'dns_servers'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'dns_server'
op|':'
newline|'\n'
indent|'                        '
name|'cmd'
op|'='
op|'['
string|"'netsh'"
op|','
string|"'interface'"
op|','
string|"'ip'"
op|','
string|"'add'"
op|','
string|"'dns'"
op|','
nl|'\n'
string|'\'name="%s"\''
op|'%'
name|'adapter_name'
op|','
name|'dns_server'
op|']'
newline|'\n'
name|'_execute'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"VMware Tools is not installed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_filter_duplicates
dedent|''
dedent|''
name|'def'
name|'_filter_duplicates'
op|'('
name|'all_entries'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'final_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'all_entries'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'entry'
name|'and'
name|'entry'
name|'not'
name|'in'
name|'final_list'
op|':'
newline|'\n'
indent|'            '
name|'final_list'
op|'.'
name|'append'
op|'('
name|'entry'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'final_list'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_set_rhel_networking
dedent|''
name|'def'
name|'_set_rhel_networking'
op|'('
name|'network_details'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set IPv4 network settings for RHEL distros."""'
newline|'\n'
name|'network_details'
op|'='
name|'network_details'
name|'or'
op|'['
op|']'
newline|'\n'
name|'all_dns_servers'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'network_detail'
name|'in'
name|'network_details'
op|':'
newline|'\n'
indent|'        '
name|'mac_address'
op|','
name|'ip_address'
op|','
name|'subnet_mask'
op|','
name|'gateway'
op|','
name|'broadcast'
op|','
name|'dns_servers'
op|'='
name|'network_detail'
newline|'\n'
name|'all_dns_servers'
op|'.'
name|'extend'
op|'('
name|'dns_servers'
op|')'
newline|'\n'
name|'adapter_name'
op|','
name|'current_ip_address'
op|'='
name|'_get_linux_adapter_name_and_ip_address'
op|'('
name|'mac_address'
op|')'
newline|'\n'
name|'if'
name|'adapter_name'
name|'and'
name|'not'
name|'ip_address'
op|'=='
name|'current_ip_address'
op|':'
newline|'\n'
indent|'            '
name|'interface_file_name'
op|'='
string|"'/etc/sysconfig/network-scripts/ifcfg-%s'"
op|'%'
name|'adapter_name'
newline|'\n'
comment|'# Remove file'
nl|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'interface_file_name'
op|')'
newline|'\n'
comment|'# Touch file'
nl|'\n'
name|'_execute'
op|'('
op|'['
string|"'touch'"
op|','
name|'interface_file_name'
op|']'
op|')'
newline|'\n'
name|'interface_file'
op|'='
name|'open'
op|'('
name|'interface_file_name'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nDEVICE=%s'"
op|'%'
name|'adapter_name'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nUSERCTL=yes'"
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nONBOOT=yes'"
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nBOOTPROTO=static'"
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nBROADCAST=%s'"
op|'%'
name|'broadcast'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nNETWORK='"
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nGATEWAY=%s'"
op|'%'
name|'gateway'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nNETMASK=%s'"
op|'%'
name|'subnet_mask'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nIPADDR=%s'"
op|'%'
name|'ip_address'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nMACADDR=%s'"
op|'%'
name|'mac_address'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'all_dns_servers'
op|':'
newline|'\n'
indent|'        '
name|'dns_file_name'
op|'='
string|'"/etc/resolv.conf"'
newline|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'dns_file_name'
op|')'
newline|'\n'
name|'_execute'
op|'('
op|'['
string|"'touch'"
op|','
name|'dns_file_name'
op|']'
op|')'
newline|'\n'
name|'dns_file'
op|'='
name|'open'
op|'('
name|'dns_file_name'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'dns_file'
op|'.'
name|'write'
op|'('
string|'"; generated by OpenStack guest tools"'
op|')'
newline|'\n'
name|'unique_entries'
op|'='
name|'_filter_duplicates'
op|'('
name|'all_dns_servers'
op|')'
newline|'\n'
name|'for'
name|'dns_server'
name|'in'
name|'unique_entries'
op|':'
newline|'\n'
indent|'            '
name|'dns_file'
op|'.'
name|'write'
op|'('
string|'"\\nnameserver %s"'
op|'%'
name|'dns_server'
op|')'
newline|'\n'
dedent|''
name|'dns_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'_execute'
op|'('
op|'['
string|"'/sbin/service'"
op|','
string|"'network'"
op|','
string|"'restart'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_set_ubuntu_networking
dedent|''
name|'def'
name|'_set_ubuntu_networking'
op|'('
name|'network_details'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set IPv4 network settings for Ubuntu."""'
newline|'\n'
name|'network_details'
op|'='
name|'network_details'
name|'or'
op|'['
op|']'
newline|'\n'
name|'all_dns_servers'
op|'='
op|'['
op|']'
newline|'\n'
name|'interface_file_name'
op|'='
string|"'/etc/network/interfaces'"
newline|'\n'
comment|'# Remove file'
nl|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'interface_file_name'
op|')'
newline|'\n'
comment|'# Touch file'
nl|'\n'
name|'_execute'
op|'('
op|'['
string|"'touch'"
op|','
name|'interface_file_name'
op|']'
op|')'
newline|'\n'
name|'interface_file'
op|'='
name|'open'
op|'('
name|'interface_file_name'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'for'
name|'device'
op|','
name|'network_detail'
name|'in'
name|'enumerate'
op|'('
name|'network_details'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mac_address'
op|','
name|'ip_address'
op|','
name|'subnet_mask'
op|','
name|'gateway'
op|','
name|'broadcast'
op|','
name|'dns_servers'
op|'='
name|'network_detail'
newline|'\n'
name|'all_dns_servers'
op|'.'
name|'extend'
op|'('
name|'dns_servers'
op|')'
newline|'\n'
name|'adapter_name'
op|','
name|'current_ip_address'
op|'='
name|'_get_linux_adapter_name_and_ip_address'
op|'('
name|'mac_address'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'adapter_name'
op|':'
newline|'\n'
indent|'            '
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nauto %s'"
op|'%'
name|'adapter_name'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\niface %s inet static'"
op|'%'
name|'adapter_name'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nbroadcast %s'"
op|'%'
name|'broadcast'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\ngateway %s'"
op|'%'
name|'gateway'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\nnetmask %s'"
op|'%'
name|'subnet_mask'
op|')'
newline|'\n'
name|'interface_file'
op|'.'
name|'write'
op|'('
string|"'\\naddress %s\\n'"
op|'%'
name|'ip_address'
op|')'
newline|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Successfully configured NIC %d with "'
nl|'\n'
string|'"NIC info %s"'
op|')'
op|'%'
op|'('
name|'device'
op|','
name|'network_detail'
op|')'
op|')'
newline|'\n'
dedent|''
name|'interface_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'all_dns_servers'
op|':'
newline|'\n'
indent|'        '
name|'dns_file_name'
op|'='
string|'"/etc/resolv.conf"'
newline|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'dns_file_name'
op|')'
newline|'\n'
name|'_execute'
op|'('
op|'['
string|"'touch'"
op|','
name|'dns_file_name'
op|']'
op|')'
newline|'\n'
name|'dns_file'
op|'='
name|'open'
op|'('
name|'dns_file_name'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'dns_file'
op|'.'
name|'write'
op|'('
string|'"; generated by OpenStack guest tools"'
op|')'
newline|'\n'
name|'unique_entries'
op|'='
name|'_filter_duplicates'
op|'('
name|'all_dns_servers'
op|')'
newline|'\n'
name|'for'
name|'dns_server'
name|'in'
name|'unique_entries'
op|':'
newline|'\n'
indent|'            '
name|'dns_file'
op|'.'
name|'write'
op|'('
string|'"\\nnameserver %s"'
op|'%'
name|'dns_server'
op|')'
newline|'\n'
dedent|''
name|'dns_file'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Restarting networking....\\n"'
op|')'
op|')'
newline|'\n'
name|'_execute'
op|'('
op|'['
string|"'/etc/init.d/networking'"
op|','
string|"'restart'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_linux_set_networking
dedent|''
name|'def'
name|'_linux_set_networking'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set IP address for the Linux VM."""'
newline|'\n'
name|'vmware_tools_bin'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|"'/usr/sbin/vmtoolsd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
string|"'/usr/sbin/vmtoolsd'"
newline|'\n'
dedent|''
name|'elif'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|"'/usr/bin/vmtoolsd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
string|"'/usr/bin/vmtoolsd'"
newline|'\n'
dedent|''
name|'elif'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|"'/usr/sbin/vmware-guestd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
string|"'/usr/sbin/vmware-guestd'"
newline|'\n'
dedent|''
name|'elif'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|"'/usr/bin/vmware-guestd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vmware_tools_bin'
op|'='
string|"'/usr/bin/vmware-guestd'"
newline|'\n'
dedent|''
name|'if'
name|'vmware_tools_bin'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'['
name|'vmware_tools_bin'
op|','
string|"'--cmd'"
op|','
string|"'machine.id.get'"
op|']'
newline|'\n'
name|'network_details'
op|'='
name|'_parse_network_details'
op|'('
name|'_execute'
op|'('
name|'cmd'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
comment|'# TODO(sateesh): For other distros like suse, debian, BSD, etc.'
nl|'\n'
name|'if'
op|'('
name|'platform'
op|'.'
name|'dist'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'=='
string|"'Ubuntu'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_set_ubuntu_networking'
op|'('
name|'network_details'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'platform'
op|'.'
name|'dist'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'=='
string|"'redhat'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_set_rhel_networking'
op|'('
name|'network_details'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Distro \'%s\' not supported"'
op|')'
op|'%'
name|'platform'
op|'.'
name|'dist'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"VMware Tools is not installed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
DECL|variable|pltfrm
indent|'    '
name|'pltfrm'
op|'='
name|'sys'
op|'.'
name|'platform'
newline|'\n'
name|'if'
name|'pltfrm'
op|'=='
name|'PLATFORM_WIN'
op|':'
newline|'\n'
indent|'        '
name|'_windows_set_networking'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'pltfrm'
op|'=='
name|'PLATFORM_LINUX'
op|':'
newline|'\n'
indent|'        '
name|'_linux_set_networking'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
name|'_'
op|'('
string|'"Platform not implemented: \'%s\'"'
op|')'
op|'%'
name|'pltfrm'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
