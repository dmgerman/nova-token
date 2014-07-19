begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright 2014 Hewlett-Packard Development Company, L.P.'
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
name|'errno'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
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
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'api'
name|'as'
name|'disk_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
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
DECL|function|cache_image
name|'def'
name|'cache_image'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'image_id'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
name|'clean'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'clean'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'target'
op|')'
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
name|'target'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'libvirt_utils'
op|'.'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'image_id'
op|','
nl|'\n'
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_into_image
dedent|''
dedent|''
name|'def'
name|'inject_into_image'
op|'('
name|'image'
op|','
name|'key'
op|','
name|'net'
op|','
name|'metadata'
op|','
name|'admin_password'
op|','
name|'files'
op|','
nl|'\n'
name|'partition'
op|','
name|'use_cow'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'disk_api'
op|'.'
name|'inject_data'
op|'('
name|'image'
op|','
name|'key'
op|','
name|'net'
op|','
name|'metadata'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'files'
op|','
name|'partition'
op|','
name|'use_cow'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|"'Image %s not found on disk storage. '"
nl|'\n'
string|"'Continue without injecting data'"
op|')'
op|','
name|'image'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to inject data into image %(image)s. "'
nl|'\n'
string|'"Error: %(e)s"'
op|')'
op|','
op|'{'
string|"'image'"
op|':'
name|'image'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unlink_without_raise
dedent|''
dedent|''
name|'def'
name|'unlink_without_raise'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to unlink %(path)s, error: %(e)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rmtree_without_raise
dedent|''
dedent|''
dedent|''
name|'def'
name|'rmtree_without_raise'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to remove dir %(path)s, error: %(e)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
dedent|''
name|'def'
name|'write_to_file'
op|'('
name|'path'
op|','
name|'contents'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'.'
name|'write'
op|'('
name|'contents'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_link_without_raise
dedent|''
dedent|''
name|'def'
name|'create_link_without_raise'
op|'('
name|'source'
op|','
name|'link'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'symlink'
op|'('
name|'source'
op|','
name|'link'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'EEXIST'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to create symlink from %(source)s to %(link)s"'
nl|'\n'
string|'", error: %(e)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'source'"
op|':'
name|'source'
op|','
string|"'link'"
op|':'
name|'link'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|random_alnum
dedent|''
dedent|''
dedent|''
name|'def'
name|'random_alnum'
op|'('
name|'count'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'chars'
op|'='
name|'string'
op|'.'
name|'ascii_uppercase'
op|'+'
name|'string'
op|'.'
name|'digits'
newline|'\n'
name|'return'
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
name|'chars'
op|')'
name|'for'
name|'_'
name|'in'
name|'range'
op|'('
name|'count'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|map_network_interfaces
dedent|''
name|'def'
name|'map_network_interfaces'
op|'('
name|'network_info'
op|','
name|'use_ipv6'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|'# TODO(deva): fix assumption that device names begin with "eth"'
nl|'\n'
comment|'#             and fix assumption about ordering'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'network_info'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_info'
op|'='
op|'['
name|'network_info'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'interfaces'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'id'
op|','
name|'vif'
name|'in'
name|'enumerate'
op|'('
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address_v6'
op|'='
name|'gateway_v6'
op|'='
name|'netmask_v6'
op|'='
name|'None'
newline|'\n'
name|'address_v4'
op|'='
name|'gateway_v4'
op|'='
name|'netmask_v4'
op|'='
name|'dns_v4'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'if'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'subnets_v6'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
nl|'\n'
name|'if'
name|'s'
op|'['
string|"'version'"
op|']'
op|'=='
number|'6'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'subnets_v6'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'address_v6'
op|'='
name|'subnets_v6'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask_v6'
op|'='
name|'subnets_v6'
op|'['
number|'0'
op|']'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'_prefixlen'
newline|'\n'
name|'gateway_v6'
op|'='
name|'subnets_v6'
op|'['
number|'0'
op|']'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'subnets_v4'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
nl|'\n'
name|'if'
name|'s'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'subnets_v4'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'address_v4'
op|'='
name|'subnets_v4'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'netmask_v4'
op|'='
name|'subnets_v4'
op|'['
number|'0'
op|']'
op|'.'
name|'as_netaddr'
op|'('
op|')'
op|'.'
name|'netmask'
newline|'\n'
name|'gateway_v4'
op|'='
name|'subnets_v4'
op|'['
number|'0'
op|']'
op|'['
string|"'gateway'"
op|']'
op|'['
string|"'address'"
op|']'
newline|'\n'
name|'dns_v4'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
op|'['
name|'x'
op|'['
string|"'address'"
op|']'
name|'for'
name|'x'
name|'in'
name|'subnets_v4'
op|'['
number|'0'
op|']'
op|'['
string|"'dns'"
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'interface'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'eth%d'"
op|'%'
name|'id'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'address_v4'
op|','
nl|'\n'
string|"'gateway'"
op|':'
name|'gateway_v4'
op|','
nl|'\n'
string|"'netmask'"
op|':'
name|'netmask_v4'
op|','
nl|'\n'
string|"'dns'"
op|':'
name|'dns_v4'
op|','
nl|'\n'
string|"'address_v6'"
op|':'
name|'address_v6'
op|','
nl|'\n'
string|"'gateway_v6'"
op|':'
name|'gateway_v6'
op|','
nl|'\n'
string|"'netmask_v6'"
op|':'
name|'netmask_v6'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'interfaces'
op|'.'
name|'append'
op|'('
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'interfaces'
newline|'\n'
dedent|''
endmarker|''
end_unit
