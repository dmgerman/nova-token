begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nThis script is used to configure openvswitch flows on XenServer hosts.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
comment|'# This is written to Python 2.4, since that is what is available on XenServer'
nl|'\n'
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'novalib'
name|'import'
name|'execute'
op|','
name|'execute_get_output'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|OVS_OFCTL
name|'OVS_OFCTL'
op|'='
string|"'/usr/bin/ovs-ofctl'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OvsFlow
name|'class'
name|'OvsFlow'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'command'
op|'='
name|'command'
newline|'\n'
name|'self'
op|'.'
name|'bridge'
op|'='
name|'bridge'
newline|'\n'
name|'self'
op|'.'
name|'params'
op|'='
name|'params'
newline|'\n'
nl|'\n'
DECL|member|add
dedent|''
name|'def'
name|'add'
op|'('
name|'self'
op|','
name|'rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
name|'OVS_OFCTL'
op|','
string|"'add-flow'"
op|','
name|'self'
op|'.'
name|'bridge'
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
name|'OVS_OFCTL'
op|','
string|"'del-flows'"
op|','
name|'self'
op|'.'
name|'bridge'
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
DECL|member|apply
dedent|''
name|'def'
name|'apply'
op|'('
name|'self'
op|','
name|'rule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'command'
name|'in'
op|'('
string|"'offline'"
op|','
string|"'reset'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'delete'
op|'('
name|'rule'
op|'%'
name|'self'
op|'.'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'command'
name|'in'
op|'('
string|"'online'"
op|','
string|"'reset'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'add'
op|'('
name|'rule'
op|'%'
name|'self'
op|'.'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
name|'dom_id'
op|','
name|'command'
op|','
name|'net_type'
op|','
name|'only_this_vif'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'xsls'
op|'='
name|'execute_get_output'
op|'('
string|"'/usr/bin/xenstore-ls'"
op|','
nl|'\n'
string|"'/local/domain/%s/vm-data/networking'"
op|'%'
name|'dom_id'
op|')'
newline|'\n'
name|'macs'
op|'='
op|'['
name|'line'
op|'.'
name|'split'
op|'('
string|'"="'
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'line'
name|'in'
name|'xsls'
op|'.'
name|'splitlines'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'        '
name|'xsread'
op|'='
name|'execute_get_output'
op|'('
string|"'/usr/bin/xenstore-read'"
op|','
nl|'\n'
string|"'/local/domain/%s/vm-data/networking/%s'"
op|'%'
nl|'\n'
op|'('
name|'dom_id'
op|','
name|'mac'
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'xsread'
op|')'
newline|'\n'
name|'if'
name|'data'
op|'['
string|'"label"'
op|']'
op|'=='
string|'"public"'
op|':'
newline|'\n'
indent|'            '
name|'vif'
op|'='
string|'"vif%s.0"'
op|'%'
name|'dom_id'
newline|'\n'
name|'bridge'
op|'='
string|'"xenbr0"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vif'
op|'='
string|'"vif%s.1"'
op|'%'
name|'dom_id'
newline|'\n'
name|'bridge'
op|'='
string|'"xenbr1"'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'only_this_vif'
name|'is'
name|'None'
op|')'
name|'or'
op|'('
name|'vif'
op|'=='
name|'only_this_vif'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'vif_ofport'
op|'='
name|'execute_get_output'
op|'('
string|"'/usr/bin/ovs-vsctl'"
op|','
string|"'get'"
op|','
nl|'\n'
string|"'Interface'"
op|','
name|'vif'
op|','
string|"'ofport'"
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'='
name|'dict'
op|'('
name|'VIF_NAME'
op|'='
name|'vif'
op|','
nl|'\n'
name|'VIF_MAC'
op|'='
name|'data'
op|'['
string|"'mac'"
op|']'
op|','
nl|'\n'
name|'VIF_OFPORT'
op|'='
name|'vif_ofport'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'net_type'
name|'in'
op|'('
string|"'ipv4'"
op|','
string|"'all'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'ip4'
name|'in'
name|'data'
op|'['
string|"'ips'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'params'
op|'.'
name|'update'
op|'('
op|'{'
string|"'VIF_IPv4'"
op|':'
name|'ip4'
op|'['
string|"'ip'"
op|']'
op|'}'
op|')'
newline|'\n'
name|'apply_ovs_ipv4_flows'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'net_type'
name|'in'
op|'('
string|"'ipv6'"
op|','
string|"'all'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'ip6'
name|'in'
name|'data'
op|'['
string|"'ip6s'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'params'
op|'.'
name|'update'
op|'('
op|'{'
string|"'VIF_GLOBAL_IPv6'"
op|':'
name|'ip6'
op|'['
string|"'ip'"
op|']'
op|'}'
op|')'
newline|'\n'
comment|'# TODO(dubs) calculate v6 link local addr'
nl|'\n'
comment|"#params.update({'VIF_LOCAL_IPv6': XXX})"
nl|'\n'
name|'apply_ovs_ipv6_flows'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|apply_ovs_ipv4_flows
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'apply_ovs_ipv4_flows'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flow'
op|'='
name|'OvsFlow'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
comment|'# allow valid ARP outbound (both request / reply)'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=3,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,arp,"'
nl|'\n'
string|'"arp_sha=%(VIF_MAC)s,nw_src=%(VIF_IPv4)s,action=normal"'
op|')'
newline|'\n'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=3,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,arp,"'
nl|'\n'
string|'"arp_sha=%(VIF_MAC)s,nw_src=0.0.0.0,action=normal"'
op|')'
newline|'\n'
nl|'\n'
comment|'# allow valid IPv4 outbound'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=3,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,ip,"'
nl|'\n'
string|'"nw_src=%(VIF_IPv4)s,action=normal"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|apply_ovs_ipv6_flows
dedent|''
name|'def'
name|'apply_ovs_ipv6_flows'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flow'
op|'='
name|'OvsFlow'
op|'('
name|'command'
op|','
name|'bridge'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
comment|'# allow valid IPv6 ND outbound (are both global and local IPs needed?)'
nl|'\n'
comment|'# Neighbor Solicitation'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,icmp_type=135,nd_sll=%(VIF_MAC)s,"'
nl|'\n'
string|'"action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,icmp_type=135,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,icmp_type=135,nd_sll=%(VIF_MAC)s,"'
nl|'\n'
string|'"action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,icmp_type=135,action=normal"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Neighbor Advertisement'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,icmp_type=136,"'
nl|'\n'
string|'"nd_target=%(VIF_LOCAL_IPv6)s,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,icmp_type=136,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,icmp_type=136,"'
nl|'\n'
string|'"nd_target=%(VIF_GLOBAL_IPv6)s,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=6,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,icmp6,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,icmp_type=136,action=normal"'
op|')'
newline|'\n'
nl|'\n'
comment|'# drop all other neighbor discovery (required because we permit all icmp6 below) '
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=135,action=drop"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=136,action=drop"'
op|')'
newline|'\n'
nl|'\n'
comment|'# do not allow sending specifc ICMPv6 types'
nl|'\n'
comment|'# Router Advertisement'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=134,action=drop"'
op|')'
newline|'\n'
comment|'# Redirect Gateway'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=137,action=drop"'
op|')'
newline|'\n'
comment|'# Mobile Prefix Solicitation'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=146,action=drop"'
op|')'
newline|'\n'
comment|'# Mobile Prefix Advertisement'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=147,action=drop"'
op|')'
newline|'\n'
comment|'# Multicast Router Advertisement'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=151,action=drop"'
op|')'
newline|'\n'
comment|'# Multicast Router Solicitation'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=152,action=drop"'
op|')'
newline|'\n'
comment|'# Multicast Router Termination'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=5,in_port=%(VIF_OFPORT)s,icmp6,icmp_type=153,action=drop"'
op|')'
newline|'\n'
nl|'\n'
comment|'# allow valid IPv6 outbound, by type'
nl|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,icmp6,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,icmp6,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,tcp6,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,tcp6,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_GLOBAL_IPv6)s,udp6,action=normal"'
op|')'
newline|'\n'
name|'flow'
op|'.'
name|'apply'
op|'('
string|'"priority=4,in_port=%(VIF_OFPORT)s,dl_src=%(VIF_MAC)s,"'
nl|'\n'
string|'"ipv6_src=%(VIF_LOCAL_IPv6)s,udp6,action=normal"'
op|')'
newline|'\n'
comment|'# all else will be dropped ...'
nl|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'<'
number|'3'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"usage: %s dom_id online|offline|reset ipv4|ipv6|all [vif_name]"'
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'dom_id'
op|','
name|'command'
op|','
name|'net_type'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
number|'4'
op|']'
newline|'\n'
DECL|variable|vif_name
name|'vif_name'
op|'='
name|'len'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
op|'=='
number|'5'
name|'and'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'4'
op|']'
name|'or'
name|'None'
newline|'\n'
name|'main'
op|'('
name|'dom_id'
op|','
name|'command'
op|','
name|'net_type'
op|','
name|'vif_name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
