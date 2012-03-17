begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'tpool'
newline|'\n'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'firewall'
name|'as'
name|'base_firewall'
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
name|'__name__'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
comment|'# The default Firewall driver must be listed at position 0'
nl|'\n'
DECL|variable|drivers
name|'drivers'
op|'='
op|'['
string|"'nova.virt.libvirt.firewall.IptablesFirewallDriver'"
op|','
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'libvirt'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Libvirt module could not be loaded. NWFilterFirewall will "'
nl|'\n'
string|'"not work correctly."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NWFilterFirewall
dedent|''
name|'class'
name|'NWFilterFirewall'
op|'('
name|'base_firewall'
op|'.'
name|'FirewallDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This class implements a network filtering mechanism by using\n    libvirt\'s nwfilter.\n    all instances get a filter ("nova-base") applied. This filter\n    provides some basic security such as protection against MAC\n    spoofing, IP spoofing, and ARP spoofing.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'get_connection'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_libvirt_get_connection'
op|'='
name|'get_connection'
newline|'\n'
name|'self'
op|'.'
name|'static_filters_configured'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'handle_security_groups'
op|'='
name|'False'
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
string|'"""No-op. Everything is done in prepare_instance_filter"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_get_connection
dedent|''
name|'def'
name|'_get_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_libvirt_get_connection'
op|'('
op|')'
newline|'\n'
DECL|variable|_conn
dedent|''
name|'_conn'
op|'='
name|'property'
op|'('
name|'_get_connection'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|nova_dhcp_filter
name|'def'
name|'nova_dhcp_filter'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""The standard allow-dhcp-server filter is an <ip> one, so it uses\n           ebtables to allow traffic through. Without a corresponding rule in\n           iptables, it\'ll get blocked anyway."""'
newline|'\n'
nl|'\n'
name|'return'
string|"'''<filter name='nova-allow-dhcp-server' chain='ipv4'>\n                    <uuid>891e4787-e5c0-d59b-cbd6-41bc3c6b36fc</uuid>\n                    <rule action='accept' direction='out'\n                          priority='100'>\n                      <udp srcipaddr='0.0.0.0'\n                           dstipaddr='255.255.255.255'\n                           srcportstart='68'\n                           dstportstart='67'/>\n                    </rule>\n                    <rule action='accept' direction='in'\n                          priority='100'>\n                      <udp srcipaddr='$DHCPSERVER'\n                           srcportstart='67'\n                           dstportstart='68'/>\n                    </rule>\n                  </filter>'''"
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
string|'"""Set up basic filtering (MAC, IP, and ARP spoofing protection)"""'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Called setup_basic_filtering in nwfilter'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'handle_security_groups'
op|':'
newline|'\n'
comment|"# No point in setting up a filter set that we'll be overriding"
nl|'\n'
comment|'# anyway.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Ensuring static filters'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_static_filters'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|'=='
name|'str'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-vpn'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-base'"
newline|'\n'
nl|'\n'
dedent|''
name|'for'
op|'('
name|'network'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
name|'instance_filter_name'
op|','
nl|'\n'
op|'['
name|'base_filter'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ensure_static_filters
dedent|''
dedent|''
name|'def'
name|'_ensure_static_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Static filters are filters that have no need to be IP aware.\n\n        There is no configuration or tuneability of these filters, so they\n        can be set up once and forgotten about.\n\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'static_filters_configured'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
string|"'nova-base'"
op|','
nl|'\n'
op|'['
string|"'no-mac-spoofing'"
op|','
nl|'\n'
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|','
nl|'\n'
string|"'allow-dhcp-server'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
string|"'nova-vpn'"
op|','
nl|'\n'
op|'['
string|"'allow-dhcp-server'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'nova_dhcp_filter'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'static_filters_configured'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_filter_container
dedent|''
name|'def'
name|'_filter_container'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
string|"'''<filter name='%s' chain='root'>%s</filter>'''"
op|'%'
op|'('
nl|'\n'
name|'name'
op|','
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|'"<filterref filter=\'%s\'/>"'
op|'%'
op|'('
name|'f'
op|','
op|')'
name|'for'
name|'f'
name|'in'
name|'filters'
op|']'
op|')'
op|')'
newline|'\n'
name|'return'
name|'xml'
newline|'\n'
nl|'\n'
DECL|member|_define_filter
dedent|''
name|'def'
name|'_define_filter'
op|'('
name|'self'
op|','
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'callable'
op|'('
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'xml'
op|'='
name|'xml'
op|'('
op|')'
newline|'\n'
comment|'# execute in a native thread and block current greenthread until done'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'libvirt_nonblocking'
op|':'
newline|'\n'
comment|'# NOTE(maoy): the original implementation is to have the API called'
nl|'\n'
comment|'# in the thread pool no matter what.'
nl|'\n'
indent|'            '
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterDefineXML'
op|','
name|'xml'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(maoy): self._conn is a eventlet.tpool.Proxy object'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterDefineXML'
op|'('
name|'xml'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
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
string|'"""Clear out the nwfilter rules."""'
newline|'\n'
name|'instance_name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'for'
op|'('
name|'network'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_nw'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterLookupByName'
op|'('
name|'instance_filter_name'
op|')'
newline|'\n'
name|'_nw'
op|'.'
name|'undefine'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'libvirt'
op|'.'
name|'libvirtError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'errcode'
op|'='
name|'e'
op|'.'
name|'get_error_code'
op|'('
op|')'
newline|'\n'
name|'if'
name|'errcode'
op|'=='
name|'libvirt'
op|'.'
name|'VIR_ERR_OPERATION_INVALID'
op|':'
newline|'\n'
comment|'# This happens when the instance filter is still in'
nl|'\n'
comment|'# use (ie. when the instance has not terminated properly)'
nl|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'The nwfilter(%(instance_filter_name)s) '"
nl|'\n'
string|"'is not found.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_network_filters
dedent|''
dedent|''
dedent|''
name|'def'
name|'_create_network_filters'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'instance_secgroup_filter_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|'=='
name|'str'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-vpn'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'base_filter'
op|'='
string|"'nova-base'"
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
op|'('
name|'_n'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
name|'instance_filter_children'
op|'='
op|'['
name|'base_filter'
op|','
string|"'nova-provider-rules'"
op|','
nl|'\n'
name|'instance_secgroup_filter_name'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'allow_same_net_traffic'
op|':'
newline|'\n'
indent|'                '
name|'instance_filter_children'
op|'.'
name|'append'
op|'('
string|"'nova-project'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_ipv6'
op|':'
newline|'\n'
indent|'                    '
name|'instance_filter_children'
op|'.'
name|'append'
op|'('
string|"'nova-project-v6'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'result'
op|'.'
name|'append'
op|'('
op|'('
name|'instance_filter_name'
op|','
name|'instance_filter_children'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_define_filters
dedent|''
name|'def'
name|'_define_filters'
op|'('
name|'self'
op|','
name|'filter_name'
op|','
name|'filter_children'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_define_filter'
op|'('
name|'self'
op|'.'
name|'_filter_container'
op|'('
name|'filter_name'
op|','
nl|'\n'
name|'filter_children'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_instance_filter_name
name|'def'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'nic_id'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'nova-instance-%s'"
op|'%'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'nova-instance-%s-%s'"
op|'%'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'nic_id'
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
name|'for'
op|'('
name|'network'
op|','
name|'mapping'
op|')'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'nic_id'
op|'='
name|'mapping'
op|'['
string|"'mac'"
op|']'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_filter_name'
op|'='
name|'self'
op|'.'
name|'_instance_filter_name'
op|'('
name|'instance'
op|','
name|'nic_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_conn'
op|'.'
name|'nwfilterLookupByName'
op|'('
name|'instance_filter_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'libvirt'
op|'.'
name|'libvirtError'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'The nwfilter(%(instance_filter_name)s) for'"
nl|'\n'
string|"'%(name)s is not found.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IptablesFirewallDriver
dedent|''
dedent|''
name|'class'
name|'IptablesFirewallDriver'
op|'('
name|'base_firewall'
op|'.'
name|'IptablesFirewallDriver'
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
name|'execute'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IptablesFirewallDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nwfilter'
op|'='
name|'NWFilterFirewall'
op|'('
name|'kwargs'
op|'['
string|"'get_connection'"
op|']'
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
string|'"""Set up provider rules and basic NWFilter."""'
newline|'\n'
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'setup_basic_filtering'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'basicly_filtered'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'iptables firewall: Setup Basic Filtering'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'refresh_provider_fw_rules'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'basicly_filtered'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|apply_instance_filter
dedent|''
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
string|'"""No-op. Everything is done in prepare_instance_filter"""'
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
comment|'# NOTE(salvatore-orlando):'
nl|'\n'
comment|'# Overriding base class method for applying nwfilter operation'
nl|'\n'
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
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'unfilter_instance'
op|'('
name|'instance'
op|','
name|'network_info'
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
string|"'Attempted to unfilter instance which is not '"
nl|'\n'
string|"'filtered'"
op|')'
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_filter_exists
dedent|''
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
name|'return'
name|'self'
op|'.'
name|'nwfilter'
op|'.'
name|'instance_filter_exists'
op|'('
name|'instance'
op|','
name|'network_info'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
