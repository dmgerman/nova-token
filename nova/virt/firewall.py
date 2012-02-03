begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
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
name|'context'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'netutils'
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
string|'"nova.virt.firewall"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|allow_same_net_traffic_opt
name|'allow_same_net_traffic_opt'
op|'='
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'allow_same_net_traffic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Whether to allow network traffic from same network'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_option'
op|'('
name|'allow_same_net_traffic_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FirewallDriver
name|'class'
name|'FirewallDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Firewall Driver base class.\n\n        Defines methods that any driver providing security groups\n        and provider fireall functionality should implement.\n    """'
newline|'\n'
DECL|member|prepare_instance_filter
name|'def'
name|'prepare_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Prepare filters for the instance.\n        At this point, the instance isn\'t running yet."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop filtering instance"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|apply_instance_filter
dedent|''
name|'def'
name|'apply_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Apply instance filter.\n\n        Once this method returns, the instance should be firewalled\n        appropriately. This method should as far as possible be a\n        no-op. It\'s vastly preferred to get everything set up in\n        prepare_instance_filter.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Refresh security group rules from data store\n\n        Gets called when a rule has been added to or removed from\n        the security group."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Refresh security group members from data store\n\n        Gets called when an instance gets added to or removed from\n        the security group."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Refresh common rules for all hosts/instances from data store.\n\n        Gets called when a rule has been added to or removed from\n        the list of rules (via admin api).\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_basic_filtering
dedent|''
name|'def'
name|'setup_basic_filtering'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create rules to block spoofing and allow dhcp.\n\n        This gets called when spawning an instance, before\n        :method:`prepare_instance_filter`.\n\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_filter_exists
dedent|''
name|'def'
name|'instance_filter_exists'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check nova-instance-instance-xxx exists"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IptablesFirewallDriver
dedent|''
dedent|''
name|'class'
name|'IptablesFirewallDriver'
op|'('
name|'FirewallDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver which enforces security groups through iptables rules."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'='
name|'linux_net'
op|'.'
name|'iptables_manager'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'network_infos'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'basicly_filtered'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'sg-fallback'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'sg-fallback'"
op|','
string|"'-j DROP'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'sg-fallback'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'sg-fallback'"
op|','
string|"'-j DROP'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_basic_filtering
dedent|''
name|'def'
name|'setup_basic_filtering'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|apply_instance_filter
dedent|''
name|'def'
name|'apply_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No-op. Everything is done in prepare_instance_filter."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'pop'
op|'('
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): use the passed info instead of the stored info'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_infos'
op|'.'
name|'pop'
op|'('
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'remove_filters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Attempted to unfilter instance %s which is not '"
nl|'\n'
string|"'filtered'"
op|')'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prepare_instance_filter
dedent|''
dedent|''
name|'def'
name|'prepare_instance_filter'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'network_infos'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'network_info'
newline|'\n'
name|'self'
op|'.'
name|'add_filters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Filters added to instance %s'"
op|')'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'refresh_provider_fw_rules'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Provider Firewall Rules refreshed'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_filter
dedent|''
name|'def'
name|'_create_filter'
op|'('
name|'self'
op|','
name|'ips'
op|','
name|'chain_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'-d %s -j $%s'"
op|'%'
op|'('
name|'ip'
op|','
name|'chain_name'
op|')'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_filters_for_instance
dedent|''
name|'def'
name|'_filters_for_instance'
op|'('
name|'self'
op|','
name|'chain_name'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a rule corresponding to each ip that defines a\n             jump to the corresponding instance - chain for all the traffic\n             destined to that ip."""'
newline|'\n'
name|'ips_v4'
op|'='
op|'['
name|'ip'
op|'['
string|"'ip'"
op|']'
name|'for'
op|'('
name|'_n'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'mapping'
op|'['
string|"'ips'"
op|']'
op|']'
newline|'\n'
name|'ipv4_rules'
op|'='
name|'self'
op|'.'
name|'_create_filter'
op|'('
name|'ips_v4'
op|','
name|'chain_name'
op|')'
newline|'\n'
nl|'\n'
name|'ipv6_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'ips_v6'
op|'='
op|'['
name|'ip'
op|'['
string|"'ip'"
op|']'
name|'for'
op|'('
name|'_n'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'mapping'
op|'['
string|"'ip6s'"
op|']'
op|']'
newline|'\n'
name|'ipv6_rules'
op|'='
name|'self'
op|'.'
name|'_create_filter'
op|'('
name|'ips_v6'
op|','
name|'chain_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
newline|'\n'
nl|'\n'
DECL|member|_add_filters
dedent|''
name|'def'
name|'_add_filters'
op|'('
name|'self'
op|','
name|'chain_name'
op|','
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'rule'
name|'in'
name|'ipv4_rules'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
name|'chain_name'
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'rule'
name|'in'
name|'ipv6_rules'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
name|'chain_name'
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_filters_for_instance
dedent|''
dedent|''
dedent|''
name|'def'
name|'add_filters_for_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_info'
op|'='
name|'self'
op|'.'
name|'network_infos'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
newline|'\n'
name|'chain_name'
op|'='
name|'self'
op|'.'
name|'_instance_chain_name'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
name|'chain_name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
name|'chain_name'
op|')'
newline|'\n'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|'='
name|'self'
op|'.'
name|'_filters_for_instance'
op|'('
name|'chain_name'
op|','
nl|'\n'
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_filters'
op|'('
string|"'local'"
op|','
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|')'
newline|'\n'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|'='
name|'self'
op|'.'
name|'instance_rules'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_filters'
op|'('
name|'chain_name'
op|','
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_filters_for_instance
dedent|''
name|'def'
name|'remove_filters_for_instance'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'chain_name'
op|'='
name|'self'
op|'.'
name|'_instance_chain_name'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'remove_chain'
op|'('
name|'chain_name'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'remove_chain'
op|'('
name|'chain_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_security_group_chain_name
name|'def'
name|'_security_group_chain_name'
op|'('
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'nova-sg-%s'"
op|'%'
op|'('
name|'security_group_id'
op|','
op|')'
newline|'\n'
nl|'\n'
DECL|member|_instance_chain_name
dedent|''
name|'def'
name|'_instance_chain_name'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'inst-%s'"
op|'%'
op|'('
name|'instance'
op|'['
string|"'id'"
op|']'
op|','
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_basic_rules
dedent|''
name|'def'
name|'_do_basic_rules'
op|'('
name|'self'
op|','
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
comment|'# Always drop invalid packets'
nl|'\n'
indent|'        '
name|'ipv4_rules'
op|'+='
op|'['
string|"'-m state --state '"
string|"'INVALID -j DROP'"
op|']'
newline|'\n'
name|'ipv6_rules'
op|'+='
op|'['
string|"'-m state --state '"
string|"'INVALID -j DROP'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Allow established connections'
nl|'\n'
name|'ipv4_rules'
op|'+='
op|'['
string|"'-m state --state ESTABLISHED,RELATED -j ACCEPT'"
op|']'
newline|'\n'
name|'ipv6_rules'
op|'+='
op|'['
string|"'-m state --state ESTABLISHED,RELATED -j ACCEPT'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Pass through provider-wide drops'
nl|'\n'
name|'ipv4_rules'
op|'+='
op|'['
string|"'-j $provider'"
op|']'
newline|'\n'
name|'ipv6_rules'
op|'+='
op|'['
string|"'-j $provider'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_do_dhcp_rules
dedent|''
name|'def'
name|'_do_dhcp_rules'
op|'('
name|'self'
op|','
name|'ipv4_rules'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dhcp_servers'
op|'='
op|'['
name|'info'
op|'['
string|"'dhcp_server'"
op|']'
name|'for'
op|'('
name|'_n'
op|','
name|'info'
op|')'
name|'in'
name|'network_info'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'dhcp_server'
name|'in'
name|'dhcp_servers'
op|':'
newline|'\n'
indent|'            '
name|'ipv4_rules'
op|'.'
name|'append'
op|'('
string|"'-s %s -p udp --sport 67 --dport 68 '"
nl|'\n'
string|"'-j ACCEPT'"
op|'%'
op|'('
name|'dhcp_server'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_project_network_rules
dedent|''
dedent|''
name|'def'
name|'_do_project_network_rules'
op|'('
name|'self'
op|','
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cidrs'
op|'='
op|'['
name|'network'
op|'['
string|"'cidr'"
op|']'
name|'for'
op|'('
name|'network'
op|','
name|'_i'
op|')'
name|'in'
name|'network_info'
op|']'
newline|'\n'
name|'for'
name|'cidr'
name|'in'
name|'cidrs'
op|':'
newline|'\n'
indent|'            '
name|'ipv4_rules'
op|'.'
name|'append'
op|'('
string|"'-s %s -j ACCEPT'"
op|'%'
op|'('
name|'cidr'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'cidrv6s'
op|'='
op|'['
name|'network'
op|'['
string|"'cidr_v6'"
op|']'
name|'for'
op|'('
name|'network'
op|','
name|'_i'
op|')'
name|'in'
nl|'\n'
name|'network_info'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'cidrv6'
name|'in'
name|'cidrv6s'
op|':'
newline|'\n'
indent|'                '
name|'ipv6_rules'
op|'.'
name|'append'
op|'('
string|"'-s %s -j ACCEPT'"
op|'%'
op|'('
name|'cidrv6'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_ra_rules
dedent|''
dedent|''
dedent|''
name|'def'
name|'_do_ra_rules'
op|'('
name|'self'
op|','
name|'ipv6_rules'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gateways_v6'
op|'='
op|'['
name|'mapping'
op|'['
string|"'gateway_v6'"
op|']'
name|'for'
op|'('
name|'_n'
op|','
name|'mapping'
op|')'
name|'in'
nl|'\n'
name|'network_info'
op|']'
newline|'\n'
name|'for'
name|'gateway_v6'
name|'in'
name|'gateways_v6'
op|':'
newline|'\n'
indent|'            '
name|'ipv6_rules'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'-s %s/128 -p icmpv6 -j ACCEPT'"
op|'%'
op|'('
name|'gateway_v6'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_icmp_rule
dedent|''
dedent|''
name|'def'
name|'_build_icmp_rule'
op|'('
name|'self'
op|','
name|'rule'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'icmp_type'
op|'='
name|'rule'
op|'.'
name|'from_port'
newline|'\n'
name|'icmp_code'
op|'='
name|'rule'
op|'.'
name|'to_port'
newline|'\n'
nl|'\n'
name|'if'
name|'icmp_type'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'icmp_type_arg'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'icmp_type_arg'
op|'='
string|"'%s'"
op|'%'
name|'icmp_type'
newline|'\n'
name|'if'
name|'not'
name|'icmp_code'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'icmp_type_arg'
op|'+='
string|"'/%s'"
op|'%'
name|'icmp_code'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'icmp_type_arg'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
string|"'-m'"
op|','
string|"'icmp'"
op|','
string|"'--icmp-type'"
op|','
name|'icmp_type_arg'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
string|"'-m'"
op|','
string|"'icmp6'"
op|','
string|"'--icmpv6-type'"
op|','
name|'icmp_type_arg'
op|']'
newline|'\n'
comment|'# return empty list if icmp_type == -1'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_build_tcp_udp_rule
dedent|''
name|'def'
name|'_build_tcp_udp_rule'
op|'('
name|'self'
op|','
name|'rule'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'rule'
op|'.'
name|'from_port'
op|'=='
name|'rule'
op|'.'
name|'to_port'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
string|"'--dport'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'rule'
op|'.'
name|'from_port'
op|','
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
string|"'-m'"
op|','
string|"'multiport'"
op|','
nl|'\n'
string|"'--dports'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'rule'
op|'.'
name|'from_port'
op|','
nl|'\n'
name|'rule'
op|'.'
name|'to_port'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|instance_rules
dedent|''
dedent|''
name|'def'
name|'instance_rules'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ipv4_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'ipv6_rules'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Initialize with basic rules'
nl|'\n'
name|'self'
op|'.'
name|'_do_basic_rules'
op|'('
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|','
name|'network_info'
op|')'
newline|'\n'
comment|'# Set up rules to allow traffic to/from DHCP server'
nl|'\n'
name|'self'
op|'.'
name|'_do_dhcp_rules'
op|'('
name|'ipv4_rules'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
comment|'#Allow project network traffic'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_do_project_network_rules'
op|'('
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|','
nl|'\n'
name|'network_info'
op|')'
newline|'\n'
comment|'# We wrap these in FLAGS.use_ipv6 because they might cause'
nl|'\n'
comment|'# a DB lookup. The other ones are just list operations, so'
nl|'\n'
comment|"# they're not worth the clutter."
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
comment|'# Allow RA responses'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_do_ra_rules'
op|'('
name|'ipv6_rules'
op|','
name|'network_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'security_groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# then, security group chains and rules'
nl|'\n'
name|'for'
name|'security_group'
name|'in'
name|'security_groups'
op|':'
newline|'\n'
indent|'            '
name|'rules'
op|'='
name|'db'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'security_group'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'rule'
name|'in'
name|'rules'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Adding security group rule: %r'"
op|')'
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'rule'
op|'.'
name|'cidr'
op|':'
newline|'\n'
indent|'                    '
name|'version'
op|'='
number|'4'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'version'
op|'='
name|'netutils'
op|'.'
name|'get_ip_version'
op|'('
name|'rule'
op|'.'
name|'cidr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                    '
name|'fw_rules'
op|'='
name|'ipv4_rules'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'fw_rules'
op|'='
name|'ipv6_rules'
newline|'\n'
nl|'\n'
dedent|''
name|'protocol'
op|'='
name|'rule'
op|'.'
name|'protocol'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'6'
name|'and'
name|'rule'
op|'.'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                    '
name|'protocol'
op|'='
string|"'icmpv6'"
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
op|'['
string|"'-j ACCEPT'"
op|']'
newline|'\n'
name|'if'
name|'protocol'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
op|'['
string|"'-p'"
op|','
name|'protocol'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'protocol'
name|'in'
op|'['
string|"'udp'"
op|','
string|"'tcp'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
name|'self'
op|'.'
name|'_build_tcp_udp_rule'
op|'('
name|'rule'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
name|'self'
op|'.'
name|'_build_icmp_rule'
op|'('
name|'rule'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'rule'
op|'.'
name|'cidr'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Using cidr %r'"
op|','
name|'rule'
op|'.'
name|'cidr'
op|')'
newline|'\n'
name|'args'
op|'+='
op|'['
string|"'-s'"
op|','
name|'rule'
op|'.'
name|'cidr'
op|']'
newline|'\n'
name|'fw_rules'
op|'+='
op|'['
string|"' '"
op|'.'
name|'join'
op|'('
name|'args'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'rule'
op|'['
string|"'grantee_group'"
op|']'
op|':'
newline|'\n'
comment|'# FIXME(jkoelker) This needs to be ported up into'
nl|'\n'
comment|'#                 the compute manager which already'
nl|'\n'
comment|'#                 has access to a nw_api handle,'
nl|'\n'
comment|'#                 and should be the only one making'
nl|'\n'
comment|'#                 making rpc calls.'
nl|'\n'
indent|'                        '
name|'import'
name|'nova'
op|'.'
name|'network'
newline|'\n'
name|'nw_api'
op|'='
name|'nova'
op|'.'
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'rule'
op|'['
string|"'grantee_group'"
op|']'
op|'['
string|"'instances'"
op|']'
op|':'
newline|'\n'
indent|'                            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'instance: %r'"
op|','
name|'instance'
op|')'
newline|'\n'
name|'ips'
op|'='
op|'['
op|']'
newline|'\n'
name|'nw_info'
op|'='
name|'nw_api'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
name|'for'
name|'net'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'                                '
name|'ips'
op|'.'
name|'extend'
op|'('
name|'net'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'ips: %r'"
op|','
name|'ips'
op|')'
newline|'\n'
name|'for'
name|'ip'
name|'in'
name|'ips'
op|':'
newline|'\n'
indent|'                                '
name|'subrule'
op|'='
name|'args'
op|'+'
op|'['
string|"'-s %s'"
op|'%'
name|'ip'
op|'['
string|"'ip'"
op|']'
op|']'
newline|'\n'
name|'fw_rules'
op|'+='
op|'['
string|"' '"
op|'.'
name|'join'
op|'('
name|'subrule'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Using fw_rules: %r'"
op|','
name|'fw_rules'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'ipv4_rules'
op|'+='
op|'['
string|"'-j $sg-fallback'"
op|']'
newline|'\n'
name|'ipv6_rules'
op|'+='
op|'['
string|"'-j $sg-fallback'"
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
newline|'\n'
nl|'\n'
DECL|member|instance_filter_exists
dedent|''
name|'def'
name|'instance_filter_exists'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'do_refresh_security_group_rules'
op|'('
name|'security_group'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'do_refresh_security_group_rules'
op|'('
name|'security_group'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'iptables'"
op|','
name|'external'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|do_refresh_security_group_rules
name|'def'
name|'do_refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'instance'
name|'in'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'remove_filters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'add_filters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|refresh_provider_fw_rules
dedent|''
dedent|''
name|'def'
name|'refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""See class:FirewallDriver: docs."""'
newline|'\n'
name|'self'
op|'.'
name|'_do_refresh_provider_fw_rules'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'apply'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'iptables'"
op|','
name|'external'
op|'='
name|'True'
op|')'
newline|'\n'
DECL|member|_do_refresh_provider_fw_rules
name|'def'
name|'_do_refresh_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Internal, synchronized version of refresh_provider_fw_rules."""'
newline|'\n'
name|'self'
op|'.'
name|'_purge_provider_fw_rules'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_build_provider_fw_rules'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_purge_provider_fw_rules
dedent|''
name|'def'
name|'_purge_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove all rules from the provider chains."""'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'empty_chain'
op|'('
string|"'provider'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'empty_chain'
op|'('
string|"'provider'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_provider_fw_rules
dedent|''
dedent|''
name|'def'
name|'_build_provider_fw_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create all rules for the provider IP DROPs."""'
newline|'\n'
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'provider'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_chain'
op|'('
string|"'provider'"
op|')'
newline|'\n'
dedent|''
name|'ipv4_rules'
op|','
name|'ipv6_rules'
op|'='
name|'self'
op|'.'
name|'_provider_rules'
op|'('
op|')'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'ipv4_rules'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'provider'"
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'rule'
name|'in'
name|'ipv6_rules'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'iptables'
op|'.'
name|'ipv6'
op|'['
string|"'filter'"
op|']'
op|'.'
name|'add_rule'
op|'('
string|"'provider'"
op|','
name|'rule'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_provider_rules
name|'def'
name|'_provider_rules'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generate a list of rules from provider for IP4 & IP6."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ipv4_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'ipv6_rules'
op|'='
op|'['
op|']'
newline|'\n'
name|'rules'
op|'='
name|'db'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'rules'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Adding provider rule: %s'"
op|')'
op|','
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'version'
op|'='
name|'netutils'
op|'.'
name|'get_ip_version'
op|'('
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                '
name|'fw_rules'
op|'='
name|'ipv4_rules'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'fw_rules'
op|'='
name|'ipv6_rules'
newline|'\n'
nl|'\n'
dedent|''
name|'protocol'
op|'='
name|'rule'
op|'['
string|"'protocol'"
op|']'
newline|'\n'
name|'if'
name|'version'
op|'=='
number|'6'
name|'and'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                '
name|'protocol'
op|'='
string|"'icmpv6'"
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
op|'['
string|"'-p'"
op|','
name|'protocol'
op|','
string|"'-s'"
op|','
name|'rule'
op|'['
string|"'cidr'"
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'protocol'
name|'in'
op|'['
string|"'udp'"
op|','
string|"'tcp'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|'=='
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
op|'['
string|"'--dport'"
op|','
string|"'%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'+='
op|'['
string|"'-m'"
op|','
string|"'multiport'"
op|','
nl|'\n'
string|"'--dports'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'rule'
op|'['
string|"'from_port'"
op|']'
op|','
nl|'\n'
name|'rule'
op|'['
string|"'to_port'"
op|']'
op|')'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'protocol'
op|'=='
string|"'icmp'"
op|':'
newline|'\n'
indent|'                '
name|'icmp_type'
op|'='
name|'rule'
op|'['
string|"'from_port'"
op|']'
newline|'\n'
name|'icmp_code'
op|'='
name|'rule'
op|'['
string|"'to_port'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'icmp_type'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'icmp_type_arg'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'icmp_type_arg'
op|'='
string|"'%s'"
op|'%'
name|'icmp_type'
newline|'\n'
name|'if'
name|'not'
name|'icmp_code'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'icmp_type_arg'
op|'+='
string|"'/%s'"
op|'%'
name|'icmp_code'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'icmp_type_arg'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'version'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'                        '
name|'args'
op|'+='
op|'['
string|"'-m'"
op|','
string|"'icmp'"
op|','
string|"'--icmp-type'"
op|','
nl|'\n'
name|'icmp_type_arg'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'version'
op|'=='
number|'6'
op|':'
newline|'\n'
indent|'                        '
name|'args'
op|'+='
op|'['
string|"'-m'"
op|','
string|"'icmp6'"
op|','
string|"'--icmpv6-type'"
op|','
nl|'\n'
name|'icmp_type_arg'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'args'
op|'+='
op|'['
string|"'-j DROP'"
op|']'
newline|'\n'
name|'fw_rules'
op|'+='
op|'['
string|"' '"
op|'.'
name|'join'
op|'('
name|'args'
op|')'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ipv4_rules'
op|','
name|'ipv6_rules'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
