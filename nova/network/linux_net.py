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
string|'"""\nImplements vlans, bridges, and iptables rules using linux utilities.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.linux_net"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_bin_file
name|'def'
name|'_bin_file'
op|'('
name|'script'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the absolute path to scipt in the bin directory"""'
newline|'\n'
name|'return'
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
string|'"../../../bin"'
op|','
name|'script'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'dhcpbridge_flagfile'"
op|','
nl|'\n'
string|"'/etc/nova/nova-dhcpbridge.conf'"
op|','
nl|'\n'
string|"'location of flagfile for dhcpbridge'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'networks_path'"
op|','
string|"'$state_path/networks'"
op|','
nl|'\n'
string|"'Location to keep network config files'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'public_interface'"
op|','
string|"'vlan1'"
op|','
nl|'\n'
string|"'Interface for public IP addresses'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vlan_interface'"
op|','
string|"'eth0'"
op|','
nl|'\n'
string|"'network device for vlans'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'dhcpbridge'"
op|','
name|'_bin_file'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
string|"'location of nova-dhcpbridge'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'routing_source_ip'"
op|','
string|"'$my_ip'"
op|','
nl|'\n'
string|"'Public IP of network host'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'use_nova_chains'"
op|','
name|'False'
op|','
nl|'\n'
string|"'use the nova_ routing chains instead of default'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'dns_server'"
op|','
name|'None'
op|','
nl|'\n'
string|"'if set, uses specific dns server for dnsmasq'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'dmz_cidr'"
op|','
string|"'10.128.0.0/24'"
op|','
nl|'\n'
string|"'dmz range that should be accepted'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|metadata_forward
name|'def'
name|'metadata_forward'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create forwarding rule for metadata"""'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"PREROUTING"'
op|','
string|'"-t nat -s 0.0.0.0/0 "'
nl|'\n'
string|'"-d 169.254.169.254/32 -p tcp -m tcp --dport 80 -j DNAT "'
nl|'\n'
string|'"--to-destination %s:%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'cc_dmz'
op|','
name|'FLAGS'
op|'.'
name|'cc_port'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Basic networking setup goes here"""'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_nova_chains'
op|':'
newline|'\n'
indent|'        '
name|'_execute'
op|'('
string|'"sudo iptables -N nova_input"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -D %s -j nova_input"'
op|'%'
name|'FLAGS'
op|'.'
name|'input_chain'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -A %s -j nova_input"'
op|'%'
name|'FLAGS'
op|'.'
name|'input_chain'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -N nova_forward"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -D FORWARD -j nova_forward"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -A FORWARD -j nova_forward"'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -N nova_output"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -D OUTPUT -j nova_output"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -A OUTPUT -j nova_output"'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -N nova_prerouting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -D PREROUTING -j nova_prerouting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -A PREROUTING -j nova_prerouting"'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -N nova_postrouting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -D POSTROUTING -j nova_postrouting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -A POSTROUTING -j nova_postrouting"'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -N nova_snatting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -D POSTROUTING -j nova_snatting"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -A POSTROUTING -j nova_snatting"'
op|')'
newline|'\n'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -N nova_output"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -D OUTPUT -j nova_output"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -A OUTPUT -j nova_output"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(vish): This makes it easy to ensure snatting rules always'
nl|'\n'
comment|'#             come after the accept rules in the postrouting chain'
nl|'\n'
indent|'        '
name|'_execute'
op|'('
string|'"sudo iptables -t nat -N SNATTING"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -D POSTROUTING -j SNATTING"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -t nat -A POSTROUTING -j SNATTING"'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(devcamcar): Cloud public SNAT entries and the default'
nl|'\n'
comment|'# SNAT rule for outbound traffic.'
nl|'\n'
dedent|''
name|'_confirm_rule'
op|'('
string|'"SNATTING"'
op|','
string|'"-t nat -s %s "'
nl|'\n'
string|'"-j SNAT --to-source %s"'
nl|'\n'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'fixed_range'
op|','
name|'FLAGS'
op|'.'
name|'routing_source_ip'
op|')'
op|','
name|'append'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'_confirm_rule'
op|'('
string|'"POSTROUTING"'
op|','
string|'"-t nat -s %s -d %s -j ACCEPT"'
op|'%'
nl|'\n'
op|'('
name|'FLAGS'
op|'.'
name|'fixed_range'
op|','
name|'FLAGS'
op|'.'
name|'dmz_cidr'
op|')'
op|')'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"POSTROUTING"'
op|','
string|'"-t nat -s %(range)s -d %(range)s -j ACCEPT"'
op|'%'
nl|'\n'
op|'{'
string|"'range'"
op|':'
name|'FLAGS'
op|'.'
name|'fixed_range'
op|'}'
op|')'
newline|'\n'
name|'if'
op|'('
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_execute'
op|'('
string|"'sudo bash -c '"
op|'+'
nl|'\n'
string|'\'"echo 1 > /proc/sys/net/ipv6/conf/all/forwarding"\''
op|')'
newline|'\n'
name|'_execute'
op|'('
string|"'sudo bash -c '"
op|'+'
nl|'\n'
string|'\'"echo 0 > /proc/sys/net/ipv6/conf/all/accept_ra"\''
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bind_floating_ip
dedent|''
dedent|''
name|'def'
name|'bind_floating_ip'
op|'('
name|'floating_ip'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bind ip to public interface"""'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo ip addr add %s dev %s"'
op|'%'
op|'('
name|'floating_ip'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'public_interface'
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unbind_floating_ip
dedent|''
name|'def'
name|'unbind_floating_ip'
op|'('
name|'floating_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unbind a public ip from public interface"""'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo ip addr del %s dev %s"'
op|'%'
op|'('
name|'floating_ip'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'public_interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_forward
dedent|''
name|'def'
name|'ensure_vlan_forward'
op|'('
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets up forwarding rules for vlan"""'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"FORWARD"'
op|','
string|'"-d %s -p udp --dport 1194 -j ACCEPT"'
op|'%'
nl|'\n'
name|'private_ip'
op|')'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"PREROUTING"'
op|','
nl|'\n'
string|'"-t nat -d %s -p udp --dport %s -j DNAT --to %s:1194"'
nl|'\n'
op|'%'
op|'('
name|'public_ip'
op|','
name|'port'
op|','
name|'private_ip'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_floating_forward
dedent|''
name|'def'
name|'ensure_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure floating ip forwarding rule"""'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"PREROUTING"'
op|','
string|'"-t nat -d %s -j DNAT --to %s"'
nl|'\n'
op|'%'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|')'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"SNATTING"'
op|','
string|'"-t nat -s %s -j SNAT --to %s"'
nl|'\n'
op|'%'
op|'('
name|'fixed_ip'
op|','
name|'floating_ip'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_floating_forward
dedent|''
name|'def'
name|'remove_floating_forward'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove forwarding for floating ip"""'
newline|'\n'
name|'_remove_rule'
op|'('
string|'"PREROUTING"'
op|','
string|'"-t nat -d %s -j DNAT --to %s"'
nl|'\n'
op|'%'
op|'('
name|'floating_ip'
op|','
name|'fixed_ip'
op|')'
op|')'
newline|'\n'
name|'_remove_rule'
op|'('
string|'"SNATTING"'
op|','
string|'"-t nat -s %s -j SNAT --to %s"'
nl|'\n'
op|'%'
op|'('
name|'fixed_ip'
op|','
name|'floating_ip'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan_bridge
dedent|''
name|'def'
name|'ensure_vlan_bridge'
op|'('
name|'vlan_num'
op|','
name|'bridge'
op|','
name|'net_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan and bridge unless they already exist"""'
newline|'\n'
name|'interface'
op|'='
name|'ensure_vlan'
op|'('
name|'vlan_num'
op|')'
newline|'\n'
name|'ensure_bridge'
op|'('
name|'bridge'
op|','
name|'interface'
op|','
name|'net_attrs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_vlan
dedent|''
name|'def'
name|'ensure_vlan'
op|'('
name|'vlan_num'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a vlan unless it already exists"""'
newline|'\n'
name|'interface'
op|'='
string|'"vlan%s"'
op|'%'
name|'vlan_num'
newline|'\n'
name|'if'
name|'not'
name|'_device_exists'
op|'('
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting VLAN inteface %s"'
op|')'
op|','
name|'interface'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo vconfig set_name_type VLAN_PLUS_VID_NO_PAD"'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo vconfig add %s %s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'vlan_interface'
op|','
name|'vlan_num'
op|')'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo ifconfig %s up"'
op|'%'
name|'interface'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'interface'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_bridge
dedent|''
name|'def'
name|'ensure_bridge'
op|'('
name|'bridge'
op|','
name|'interface'
op|','
name|'net_attrs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a bridge unless it already exists"""'
newline|'\n'
name|'if'
name|'not'
name|'_device_exists'
op|'('
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Starting Bridge interface for %s"'
op|')'
op|','
name|'interface'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo brctl addbr %s"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo brctl setfd %s 0"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
comment|'# _execute("sudo brctl setageing %s 10" % bridge)'
nl|'\n'
name|'_execute'
op|'('
string|'"sudo brctl stp %s off"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
name|'if'
name|'interface'
op|':'
newline|'\n'
indent|'            '
name|'_execute'
op|'('
string|'"sudo brctl addif %s %s"'
op|'%'
op|'('
name|'bridge'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'net_attrs'
op|':'
newline|'\n'
indent|'        '
name|'_execute'
op|'('
string|'"sudo ifconfig %s %s broadcast %s netmask %s up"'
op|'%'
op|'('
name|'bridge'
op|','
nl|'\n'
name|'net_attrs'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
name|'net_attrs'
op|'['
string|"'broadcast'"
op|']'
op|','
nl|'\n'
name|'net_attrs'
op|'['
string|"'netmask'"
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
op|'('
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_execute'
op|'('
string|'"sudo ifconfig %s add %s up"'
op|'%'
op|'('
name|'bridge'
op|','
nl|'\n'
name|'net_attrs'
op|'['
string|"'cidr_v6'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'_execute'
op|'('
string|'"sudo ifconfig %s up"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_nova_chains'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'_execute'
op|'('
string|'"sudo iptables -N nova_forward"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'err'
op|'!='
string|"'iptables: Chain already exists.\\n'"
op|':'
newline|'\n'
comment|"# NOTE(vish): chain didn't exist link chain"
nl|'\n'
indent|'            '
name|'_execute'
op|'('
string|'"sudo iptables -D FORWARD -j nova_forward"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -A FORWARD -j nova_forward"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'_confirm_rule'
op|'('
string|'"FORWARD"'
op|','
string|'"--in-interface %s -j ACCEPT"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"FORWARD"'
op|','
string|'"--out-interface %s -j ACCEPT"'
op|'%'
name|'bridge'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables -N nova-local"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_confirm_rule'
op|'('
string|'"FORWARD"'
op|','
string|'"-j nova-local"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dhcp_hosts
dedent|''
name|'def'
name|'get_dhcp_hosts'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a string containing a network\'s hosts config in dnsmasq format"""'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'fixed_ip_ref'
name|'in'
name|'db'
op|'.'
name|'network_get_associated_fixed_ips'
op|'('
name|'context'
op|','
nl|'\n'
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hosts'
op|'.'
name|'append'
op|'('
name|'_host_dhcp'
op|'('
name|'fixed_ip_ref'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(ja): Sending a HUP only reloads the hostfile, so any'
nl|'\n'
comment|'#           configuration options (like dchp-range, vlan, ...)'
nl|'\n'
comment|"#           aren't reloaded."
nl|'\n'
DECL|function|update_dhcp
dedent|''
name|'def'
name|'update_dhcp'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""(Re)starts a dnsmasq server for a given network\n\n    if a dnsmasq instance is already running then send a HUP\n    signal causing it to reload, otherwise spawn a new instance\n    """'
newline|'\n'
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
name|'conffile'
op|'='
name|'_dhcp_file'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'conf'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'conffile'
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
name|'get_dhcp_hosts'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure dnsmasq can actually read it (it setuid()s to "nobody")'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'chmod'
op|'('
name|'conffile'
op|','
number|'0644'
op|')'
newline|'\n'
nl|'\n'
name|'pid'
op|'='
name|'_dnsmasq_pid_for'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# if dnsmasq is already running, then tell it to reload'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'_err'
op|'='
name|'_execute'
op|'('
string|"'cat /proc/%d/cmdline'"
op|'%'
name|'pid'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'conffile'
name|'in'
name|'out'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_execute'
op|'('
string|"'sudo kill -HUP %d'"
op|'%'
name|'pid'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Hupping dnsmasq threw %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Pid %d is stale, relaunching dnsmasq"'
op|')'
op|','
name|'pid'
op|')'
newline|'\n'
nl|'\n'
comment|'# FLAGFILE and DNSMASQ_INTERFACE in env'
nl|'\n'
dedent|''
dedent|''
name|'env'
op|'='
op|'{'
string|"'FLAGFILE'"
op|':'
name|'FLAGS'
op|'.'
name|'dhcpbridge_flagfile'
op|','
nl|'\n'
string|"'DNSMASQ_INTERFACE'"
op|':'
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|'}'
newline|'\n'
name|'command'
op|'='
name|'_dnsmasq_cmd'
op|'('
name|'network_ref'
op|')'
newline|'\n'
name|'_execute'
op|'('
name|'command'
op|','
name|'addl_env'
op|'='
name|'env'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_ra
dedent|''
name|'def'
name|'update_ra'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'network_ref'
op|'='
name|'db'
op|'.'
name|'network_get'
op|'('
name|'context'
op|','
name|'network_id'
op|')'
newline|'\n'
nl|'\n'
name|'conffile'
op|'='
name|'_ra_file'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'conf'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'conffile'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'conf_str'
op|'='
string|'"""\ninterface %s\n{\n   AdvSendAdvert on;\n   MinRtrAdvInterval 3;\n   MaxRtrAdvInterval 10;\n   prefix %s\n   {\n        AdvOnLink on;\n        AdvAutonomous on;\n   };\n};\n"""'
op|'%'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|','
name|'network_ref'
op|'['
string|"'cidr_v6'"
op|']'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'conf_str'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure dnsmasq can actually read it (it setuid()s to "nobody")'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'chmod'
op|'('
name|'conffile'
op|','
number|'0644'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|pid
name|'pid'
op|'='
name|'_ra_pid_for'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# if dnsmasq is already running, then tell it to reload'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'_err'
op|'='
name|'_execute'
op|'('
string|"'cat /proc/%d/cmdline'"
nl|'\n'
op|'%'
name|'pid'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'if'
name|'conffile'
name|'in'
name|'out'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_execute'
op|'('
string|"'sudo kill -HUP %d'"
op|'%'
name|'pid'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Hupping radvd threw %s"'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Pid %d is stale, relaunching radvd"'
op|','
name|'pid'
op|')'
newline|'\n'
DECL|variable|command
dedent|''
dedent|''
name|'command'
op|'='
name|'_ra_cmd'
op|'('
name|'network_ref'
op|')'
newline|'\n'
name|'_execute'
op|'('
name|'command'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'network_update'
op|'('
name|'context'
op|','
name|'network_id'
op|','
nl|'\n'
op|'{'
string|'"ra_server"'
op|':'
nl|'\n'
name|'utils'
op|'.'
name|'get_my_linklocal'
op|'('
name|'network_ref'
op|'['
string|"'bridge'"
op|']'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_host_dhcp
dedent|''
name|'def'
name|'_host_dhcp'
op|'('
name|'fixed_ip_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a host string for an address"""'
newline|'\n'
name|'instance_ref'
op|'='
name|'fixed_ip_ref'
op|'['
string|"'instance'"
op|']'
newline|'\n'
name|'return'
string|'"%s,%s.novalocal,%s"'
op|'%'
op|'('
name|'instance_ref'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
op|','
nl|'\n'
name|'fixed_ip_ref'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_execute
dedent|''
name|'def'
name|'_execute'
op|'('
name|'cmd'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around utils._execute for fake_network"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"FAKE NET: %s"'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'return'
string|'"fake"'
op|','
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_device_exists
dedent|''
dedent|''
name|'def'
name|'_device_exists'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if ethernet device exists"""'
newline|'\n'
op|'('
name|'_out'
op|','
name|'err'
op|')'
op|'='
name|'_execute'
op|'('
string|'"ifconfig %s"'
op|'%'
name|'device'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return'
name|'not'
name|'err'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_confirm_rule
dedent|''
name|'def'
name|'_confirm_rule'
op|'('
name|'chain'
op|','
name|'cmd'
op|','
name|'append'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete and re-add iptables rule"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_nova_chains'
op|':'
newline|'\n'
indent|'        '
name|'chain'
op|'='
string|'"nova_%s"'
op|'%'
name|'chain'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'append'
op|':'
newline|'\n'
indent|'        '
name|'loc'
op|'='
string|'"-A"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'loc'
op|'='
string|'"-I"'
newline|'\n'
dedent|''
name|'_execute'
op|'('
string|'"sudo iptables --delete %s %s"'
op|'%'
op|'('
name|'chain'
op|','
name|'cmd'
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'_execute'
op|'('
string|'"sudo iptables %s %s %s"'
op|'%'
op|'('
name|'loc'
op|','
name|'chain'
op|','
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_remove_rule
dedent|''
name|'def'
name|'_remove_rule'
op|'('
name|'chain'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove iptables rule"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_nova_chains'
op|':'
newline|'\n'
indent|'        '
name|'chain'
op|'='
string|'"%s"'
op|'%'
name|'chain'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
dedent|''
name|'_execute'
op|'('
string|'"sudo iptables --delete %s %s"'
op|'%'
op|'('
name|'chain'
op|','
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dnsmasq_cmd
dedent|''
name|'def'
name|'_dnsmasq_cmd'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds dnsmasq command"""'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|"'sudo -E dnsmasq'"
op|','
nl|'\n'
string|"' --strict-order'"
op|','
nl|'\n'
string|"' --bind-interfaces'"
op|','
nl|'\n'
string|"' --conf-file='"
op|','
nl|'\n'
string|"' --pid-file=%s'"
op|'%'
name|'_dhcp_file'
op|'('
name|'net'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'pid'"
op|')'
op|','
nl|'\n'
string|"' --listen-address=%s'"
op|'%'
name|'net'
op|'['
string|"'gateway'"
op|']'
op|','
nl|'\n'
string|"' --except-interface=lo'"
op|','
nl|'\n'
string|"' --dhcp-range=%s,static,120s'"
op|'%'
name|'net'
op|'['
string|"'dhcp_start'"
op|']'
op|','
nl|'\n'
string|"' --dhcp-hostsfile=%s'"
op|'%'
name|'_dhcp_file'
op|'('
name|'net'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'conf'"
op|')'
op|','
nl|'\n'
string|"' --dhcp-script=%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'dhcpbridge'
op|','
nl|'\n'
string|"' --leasefile-ro'"
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'dns_server'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'.'
name|'append'
op|'('
string|"' -h -R --server=%s'"
op|'%'
name|'FLAGS'
op|'.'
name|'dns_server'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ra_cmd
dedent|''
name|'def'
name|'_ra_cmd'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds dnsmasq command"""'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|"'sudo -E radvd'"
op|','
nl|'\n'
comment|"#           ' -u nobody',"
nl|'\n'
string|"' -C %s'"
op|'%'
name|'_ra_file'
op|'('
name|'net'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'conf'"
op|')'
op|','
nl|'\n'
string|"' -p %s'"
op|'%'
name|'_ra_file'
op|'('
name|'net'
op|'['
string|"'bridge'"
op|']'
op|','
string|"'pid'"
op|')'
op|']'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_stop_dnsmasq
dedent|''
name|'def'
name|'_stop_dnsmasq'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stops the dnsmasq instance for a given network"""'
newline|'\n'
name|'pid'
op|'='
name|'_dnsmasq_pid_for'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'_execute'
op|'('
string|"'sudo kill -TERM %d'"
op|'%'
name|'pid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Killing dnsmasq threw %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dhcp_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'_dhcp_file'
op|'('
name|'bridge'
op|','
name|'kind'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return path to a pid, leases or conf file for a bridge"""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|'"%s/nova-%s.%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|','
nl|'\n'
name|'bridge'
op|','
nl|'\n'
name|'kind'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ra_file
dedent|''
name|'def'
name|'_ra_file'
op|'('
name|'bridge'
op|','
name|'kind'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return path to a pid, leases or conf file for a bridge"""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
string|'"%s/nova-ra-%s.%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'networks_path'
op|','
nl|'\n'
name|'bridge'
op|','
nl|'\n'
name|'kind'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_dnsmasq_pid_for
dedent|''
name|'def'
name|'_dnsmasq_pid_for'
op|'('
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the pid for prior dnsmasq instance for a bridge\n\n    Returns None if no pid file exists\n\n    If machine has rebooted pid might be incorrect (caller should check)\n    """'
newline|'\n'
nl|'\n'
name|'pid_file'
op|'='
name|'_dhcp_file'
op|'('
name|'bridge'
op|','
string|"'pid'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pid_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'pid_file'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ra_pid_for
dedent|''
dedent|''
dedent|''
name|'def'
name|'_ra_pid_for'
op|'('
name|'bridge'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the pid for prior dnsmasq instance for a bridge\n\n    Returns None if no pid file exists\n\n    If machine has rebooted pid might be incorrect (caller should check)\n    """'
newline|'\n'
nl|'\n'
name|'pid_file'
op|'='
name|'_ra_file'
op|'('
name|'bridge'
op|','
string|"'pid'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pid_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'pid_file'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
