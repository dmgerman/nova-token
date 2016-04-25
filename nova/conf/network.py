begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'paths'
newline|'\n'
nl|'\n'
DECL|variable|NOVA_NET_API
name|'NOVA_NET_API'
op|'='
string|"'nova.network.api.API'"
newline|'\n'
nl|'\n'
DECL|variable|network_opts
name|'network_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"flat_network_bridge"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis option determines the bridge used for simple network interfaces when no\nbridge is specified in the VM creation request.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment.\n\nPossible values:\n\n    Any string representing a valid network bridge, such as \'br100\'\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"flat_network_dns"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"8.8.4.4"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is the address of the DNS server for a simple network. If this option is\nnot specified, the default of \'8.8.4.4\' is used.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment.\n\nPossible values:\n\n    Any valid IP address.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"flat_injected"'
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
string|'"""\nThis option determines whether the network setup information is injected into\nthe VM before it is booted.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment.\n\nPossible values:\n\n    True, False (default)\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"flat_interface"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis option is the name of the virtual interface of the VM on which the bridge\nwill be built.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment.\n\nPossible values:\n\n    Any valid virtual interface name, such as \'eth0\'\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"vlan_start"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|min
name|'min'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|max
name|'max'
op|'='
number|'4094'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is the VLAN number used for private networks. Note that the when creating\nthe networks, if the specified number has already been assigned, nova-network\nwill increment this number until it finds an available VLAN.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment. It also will be ignored if the configuration option\nfor `network_manager` is not set to the default of\n\'nova.network.manager.VlanManager\'.\n\nPossible values:\n\n    Any integer between 1 and 4094. Values outside of that range will raise a\n    ValueError exception. Default = 100.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``network_manager``, ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"vlan_interface"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis option is the name of the virtual interface of the VM on which the VLAN\nbridge will be built.\n\nPlease note that this option is only used when using nova-network instead of\nNeutron in your deployment. It also will be ignored if the configuration option\nfor `network_manager` is not set to the default of\n\'nova.network.manager.VlanManager\'.\n\nPossible values:\n\n    Any valid virtual interface name, such as \'eth0\'\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    ``use_neutron``\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"num_networks"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of networks to support"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"vpn_ip"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"$my_ip"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Public IP for the cloudpipe VPN servers"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"vpn_start"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"First Vpn port for private networks"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"network_size"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'256'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of addresses in each private subnet"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"fixed_range_v6"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"fd00::/48"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Fixed IPv6 address block"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"gateway"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Default IPv4 gateway"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"gateway_v6"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Default IPv6 gateway"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"cnt_vpn_clients"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of addresses reserved for vpn clients"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"fixed_ip_disassociate_timeout"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Seconds after which a deallocated IP is disassociated"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"create_unique_mac_address_attempts"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of attempts to create unique mac address"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"fake_call"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"If True, skip using the queue and make local calls"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"teardown_unused_network_gateway"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"If True, unused gateway devices (VLAN and bridge) are "'
nl|'\n'
string|'"deleted in VLAN network mode with multi hosted "'
nl|'\n'
string|'"networks"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"force_dhcp_release"'
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
string|'"If True, send a dhcp release on instance termination"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"update_dns_entries"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"If True, when a DNS entry must be updated, it sends a "'
nl|'\n'
string|'"fanout cast to all network hosts to update their DNS "'
nl|'\n'
string|'"entries in multi host mode"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"dns_update_periodic_interval"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of seconds to wait between runs of updates to DNS "'
nl|'\n'
string|'"entries."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"dhcp_domain"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"novalocal"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Domain to use for building the hostnames"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"l3_lib"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.network.l3.LinuxNetL3"'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Indicates underlying L3 management library"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"share_dhcp_address"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nDEPRECATED: THIS VALUE SHOULD BE SET WHEN CREATING THE NETWORK.\n\nIf True in multi_host mode, all compute hosts share the same dhcp address. The\nsame IP address used for DHCP will be added on each nova-network node which is\nonly visible to the VMs on the same host.\n\nThe use of this configuration has been deprecated and may be removed in any\nrelease after Mitaka. It is recommended that instead of relying on this option,\nan explicit value should be passed to \'create_networks()\' as a keyword argument\nwith the name \'share_address\'.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# NOTE(mriedem): Remove network_device_mtu in Newton.'
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"network_device_mtu"'
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nDEPRECATED: THIS VALUE SHOULD BE SET WHEN CREATING THE NETWORK.\n\nMTU (Maximum Transmission Unit) setting for a network interface.\n\nThe use of this configuration has been deprecated and may be removed in any\nrelease after Mitaka. It is recommended that instead of relying on this option,\nan explicit value should be passed to \'create_networks()\' as a keyword argument\nwith the name \'mtu\'.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
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
DECL|variable|help
name|'help'
op|'='
string|'"Whether to use Neutron or Nova Network as the back end "'
nl|'\n'
string|'"for networking. Defaults to False (indicating Nova "'
nl|'\n'
string|'"network).Set to True to use neutron."'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|linux_net_opts
name|'linux_net_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'dhcpbridge_flagfile'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'/etc/nova/nova-dhcpbridge.conf'"
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis option is a list of full paths to one or more configuration files for\ndhcpbridge. In most cases the default path of \'/etc/nova/nova-dhcpbridge.conf\'\nshould be sufficient, but if you have special needs for configuring dhcpbridge,\nyou can change or add to this list.\n\n* Possible values\n\n    A list of strings, where each string is the full path to a dhcpbridge\n    configuration file.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'networks_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'networks'"
op|')'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThe location where the network configuration files will be kept. The default is\nthe \'networks\' directory off of the location where nova\'s Python module is\ninstalled.\n\n* Possible values\n\n    A string containing the full path to the desired configuration directory\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'public_interface'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'eth0'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is the name of the network interface for public IP addresses. The default\nis \'eth0\'.\n\n* Possible values:\n\n    Any string representing a network interface name\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'dhcpbridge'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'bindir_def'
op|'('
string|"'nova-dhcpbridge'"
op|')'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThe location of the binary nova-dhcpbridge. By default it is the binary named\n\'nova-dhcpbridge\' that is installed with all the other nova binaries.\n\n* Possible values:\n\n    Any string representing the full path to the binary for dhcpbridge\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'routing_source_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is the public IP address of the network host. It is used when creating a\nSNAT rule.\n\n* Possible values:\n\n    Any valid IP address\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    force_snat_range\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'dhcp_lease_time'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'86400'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThe lifetime of a DHCP lease, in seconds. The default is 86400 (one day).\n\nPossible values:\n\n    Any positive integer value.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|'"dns_server"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nDespite the singular form of the name of this option, it is actually a list of\nzero or more server addresses that dnsmasq will use for DNS nameservers. If\nthis is not empty, dnsmasq will not read /etc/resolv.conf, but will only use\nthe servers specified in this option. If the option use_network_dns_servers is\nTrue, the dns1 and dns2 servers from the network will be appended to this list,\nand will be used as DNS servers, too.\n\nPossible values:\n\n    A list of strings, where each string is etiher an IP address or a FQDN.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    use_network_dns_servers\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"use_network_dns_servers"'
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
string|'"""\nWhen this option is set to True, the dns1 and dns2 servers for the network\nspecified by the user on boot will be used for DNS, as well as any specified in\nthe `dns_server` option.\n\nPossible values:\n\n    True, False (default)\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    dns_server\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|'"dmz_cidr"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis option is a list of zero or more IP address ranges in your network\'s DMZ\nthat should be accepted.\n\nPossible values:\n\n    A list of strings, each of which should be a valid CIDR.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|'"force_snat_range"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is a list of zero or more IP ranges that traffic from the\n`routing_source_ip` will be SNATted to. If the list is empty, then no SNAT\nrules are created.\n\nPossible values:\n\n    A list of strings, each of which should be a valid CIDR.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    routing_source_ip\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"dnsmasq_config_file"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'""'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThe path to the custom dnsmasq configuration file, if any.\n\nPossible values:\n\n    The full path to the configuration file, or an empty string if there is no\n    custom dnsmasq configuration file.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"linuxnet_interface_driver"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"nova.network.linux_net.LinuxBridgeInterfaceDriver"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThis is the class used as the ethernet device driver for linuxnet bridge\noperations. The default value should be all you need for most cases, but if you\nwish to use a customized class, set this option to the full dot-separated\nimport path for that class.\n\nPossible values:\n\n    Any string representing a dot-separated class path that Nova can import.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|'"linuxnet_ovs_integration_bridge"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'"br-int"'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nThe name of the Open vSwitch bridge that is used with linuxnet when connecting\nwith Open vSwitch."\n\nPossible values:\n\n    Any string representing a valid bridge name.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"send_arp_for_ha"'
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
string|'"""\nWhen True, when a device starts up, and upon binding floating IP addresses, arp\nmessages will be sent to ensure that the arp caches on the compute hosts are\nup-to-date.\n\nPossible values:\n\n    True, False (default)\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    send_arp_for_ha_count\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"send_arp_for_ha_count"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nWhen arp messages are configured to be sent, they will be sent with the count\nset to the value of this option. Of course, if this is set to zero, no arp\nmessages will be sent.\n\nPossible values:\n\n    Any integer greater than or equal to 0\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    send_arp_for_ha\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|'"use_single_default_gateway"'
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
string|'"""\nWhen set to True, only the firt nic of a VM will get its default gateway from\nthe DHCP server.\n\nPossible values:\n\n    True, False (default)\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|'"forward_bridge_interface"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|'"all"'
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nOne or more interfaces that bridges can forward traffic to. If any of the items\nin this list is the special keyword \'all\', then all traffic will be forwarded.\n\nPossible values:\n\n    A list of zero or more interface names, or the word \'all\'.\n\n* Services that use this:\n\n    ``nova-network``\n\n* Related options:\n\n    None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'metadata_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$my_ip'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The IP address for the metadata API server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'metadata_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'8775'
op|','
nl|'\n'
DECL|variable|min
name|'min'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|max
name|'max'
op|'='
number|'65535'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The port for the metadata API port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iptables_top_regex'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Regular expression to match the iptables rule that '"
nl|'\n'
string|"'should always be on the top.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iptables_bottom_regex'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Regular expression to match the iptables rule that '"
nl|'\n'
string|"'should always be on the bottom.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iptables_drop_action'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'DROP'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The table that iptables to jump to when a packet is '"
nl|'\n'
string|"'to be dropped.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ovs_vsctl_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'120'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Amount of time, in seconds, that ovs_vsctl should wait '"
nl|'\n'
string|"'for a response from the database. 0 is to wait forever.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'fake_network'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If passed, use fake network devices and addresses'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ebtables_exec_attempts'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of times to retry ebtables commands on failure.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'ebtables_retry_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds to wait between ebtables retries.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ldap_dns_opts
name|'ldap_dns_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ldap://ldap.example.com:389'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'URL for LDAP server which will store DNS entries'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_user'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'uid=admin,ou=people,dc=example,dc=org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'User for LDAP DNS'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'password'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for LDAP DNS'"
op|','
nl|'\n'
DECL|variable|secret
name|'secret'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_hostmaster'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'hostmaster@example.org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Hostmaster for LDAP DNS driver Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'ldap_dns_servers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'dns.example.org'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DNS Servers for LDAP DNS driver'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_base_dn'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'ou=hosts,dc=example,dc=org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base DN for DNS entries in LDAP'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_refresh'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'1800'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Refresh interval (in seconds) for LDAP DNS driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_retry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'3600'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Retry interval (in seconds) for LDAP DNS driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_expiry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'86400'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Expiry interval (in seconds) for LDAP DNS driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_minimum'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'7200'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Minimum interval (in seconds) for LDAP DNS driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|security_group_opts
name|'security_group_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'security_group_api'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DEPRECATED: Full class name of the security API class'"
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ALL_DEFAULT_OPTS
name|'ALL_DEFAULT_OPTS'
op|'='
op|'('
name|'linux_net_opts'
op|'+'
name|'network_opts'
op|'+'
name|'ldap_dns_opts'
nl|'\n'
op|'+'
name|'security_group_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'linux_net_opts'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'network_opts'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ldap_dns_opts'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'security_group_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|'"DEFAULT"'
op|':'
name|'ALL_DEFAULT_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
