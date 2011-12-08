begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'rootwrap'
op|'.'
name|'filters'
name|'import'
name|'CommandFilter'
op|','
name|'DnsmasqFilter'
newline|'\n'
nl|'\n'
DECL|variable|filters
name|'filters'
op|'='
op|'['
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'add', str(floating_ip)+'/32'i.."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'del', str(floating_ip)+'/32'.."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'add', '169.254.169.254/32',.."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'show', 'dev', dev, 'scope',.."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'del/add', ip_params, dev)"
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'del', params, fields[-1]"
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'add', params, bridge"
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', '-f', 'inet6', 'addr', 'change', .."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'link', 'set', 'dev', dev, 'promisc',.."
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'link', 'add', 'link', bridge_if ..."
nl|'\n'
comment|'# nova/network/linux_net.py: \'ip\', \'link\', \'set\', interface, "address",..'
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'link', 'set', interface, 'up'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'link', 'set', bridge, 'up'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'addr', 'show', 'dev', interface, .."
nl|'\n'
comment|'# nova/network/linux_net.py: \'ip\', \'link\', \'set\', dev, "address", ..'
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip', 'link', 'set', dev, 'up'"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/ip"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip[6]tables-save' % (cmd,), '-t', ..."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/iptables-save"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/ip6tables-save"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'ip[6]tables-restore' % (cmd,)"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/iptables-restore"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/ip6tables-restore"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'arping', '-U', floating_ip, '-A', '-I', ..."
nl|'\n'
comment|"# nova/network/linux_net.py: 'arping', '-U', network_ref['dhcp_server'],.."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/arping"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', '-n'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', 'del', 'default', 'gw'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', 'add', 'default', 'gw'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', '-n'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', 'del', 'default', 'gw', old_gw, .."
nl|'\n'
comment|"# nova/network/linux_net.py: 'route', 'add', 'default', 'gw', old_gateway"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/route"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'dhcp_release', dev, address, mac_address"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/dhcp_release"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'kill', '-9', pid"
nl|'\n'
comment|"# nova/network/linux_net.py: 'kill', '-HUP', pid"
nl|'\n'
comment|"# nova/network/linux_net.py: 'kill', pid"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/kill"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# nova/network/linux_net.py: dnsmasq call'
nl|'\n'
name|'DnsmasqFilter'
op|'('
string|'"/usr/sbin/dnsmasq"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'radvd', '-C', '%s' % _ra_file(dev, 'conf'),.."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/sbin/radvd"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'brctl', 'addbr', bridge"
nl|'\n'
comment|"# nova/network/linux_net.py: 'brctl', 'setfd', bridge, 0"
nl|'\n'
comment|"# nova/network/linux_net.py: 'brctl', 'stp', bridge, 'off'"
nl|'\n'
comment|"# nova/network/linux_net.py: 'brctl', 'addif', bridge, interface"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/brctl"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/sbin/brctl"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/network/linux_net.py: 'ovs-vsctl', ...."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/ovs-vsctl"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
endmarker|''
end_unit
