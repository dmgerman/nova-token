begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""IPv6 address generation with account identifier embedded"""'
newline|'\n'
nl|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_global
name|'def'
name|'to_global'
op|'('
name|'prefix'
op|','
name|'mac'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'project_hash'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'int'
op|'('
name|'hashlib'
op|'.'
name|'sha1'
op|'('
name|'project_id'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|'['
op|':'
number|'8'
op|']'
op|','
number|'16'
op|')'
op|'<<'
number|'32'
op|')'
newline|'\n'
name|'static_num'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
number|'0xff'
op|'<<'
number|'24'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'mac_suffix'
op|'='
name|'netaddr'
op|'.'
name|'EUI'
op|'('
name|'mac'
op|')'
op|'.'
name|'words'
op|'['
number|'3'
op|':'
op|']'
newline|'\n'
name|'int_addr'
op|'='
name|'int'
op|'('
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'%02x'"
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'mac_suffix'
op|']'
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'mac_addr'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'int_addr'
op|')'
newline|'\n'
name|'maskIP'
op|'='
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'prefix'
op|')'
op|'.'
name|'ip'
newline|'\n'
name|'return'
op|'('
name|'project_hash'
op|'^'
name|'static_num'
op|'^'
name|'mac_addr'
op|'|'
name|'maskIP'
op|')'
op|'.'
name|'format'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'TypeError'
op|'('
name|'_'
op|'('
string|"'Bad mac for to_global_ipv6: %s'"
op|')'
op|'%'
name|'mac'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_mac
dedent|''
dedent|''
name|'def'
name|'to_mac'
op|'('
name|'ipv6_address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'address'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
name|'ipv6_address'
op|')'
newline|'\n'
name|'mask1'
op|'='
name|'netaddr'
op|'.'
name|'IPAddress'
op|'('
string|"'::ff:ffff'"
op|')'
newline|'\n'
name|'mac'
op|'='
name|'netaddr'
op|'.'
name|'EUI'
op|'('
name|'int'
op|'('
name|'address'
op|'&'
name|'mask1'
op|')'
op|')'
op|'.'
name|'words'
newline|'\n'
name|'return'
string|"':'"
op|'.'
name|'join'
op|'('
op|'['
string|"'02'"
op|','
string|"'16'"
op|','
string|"'3e'"
op|']'
op|'+'
op|'['
string|"'%02x'"
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'mac'
op|'['
number|'3'
op|':'
number|'6'
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
