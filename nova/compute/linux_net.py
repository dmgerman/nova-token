begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'utils'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
comment|'# todo(ja): does the definition of network_path belong here?'
nl|'\n'
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
DECL|function|execute
name|'def'
name|'execute'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|'"FAKE NET: %s"'
op|'%'
name|'cmd'
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
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|function|runthis
dedent|''
dedent|''
name|'def'
name|'runthis'
op|'('
name|'desc'
op|','
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'nova'
op|'.'
name|'utils'
op|'.'
name|'runthis'
op|'('
name|'desc'
op|','
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
DECL|function|Popen
dedent|''
dedent|''
name|'def'
name|'Popen'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'fake_network'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|device_exists
dedent|''
dedent|''
name|'def'
name|'device_exists'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'execute'
op|'('
string|'"ifconfig %s"'
op|'%'
name|'device'
op|')'
newline|'\n'
name|'return'
name|'not'
name|'err'
newline|'\n'
nl|'\n'
DECL|function|confirm_rule
dedent|''
name|'def'
name|'confirm_rule'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'execute'
op|'('
string|'"sudo iptables --delete %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo iptables -I %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|remove_rule
dedent|''
name|'def'
name|'remove_rule'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'execute'
op|'('
string|'"sudo iptables --delete %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|bind_public_ip
dedent|''
name|'def'
name|'bind_public_ip'
op|'('
name|'ip'
op|','
name|'interface'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'runthis'
op|'('
string|'"Binding IP to interface: %s"'
op|','
string|'"sudo ip addr add %s dev %s"'
op|'%'
op|'('
name|'ip'
op|','
name|'interface'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|vlan_create
dedent|''
name|'def'
name|'vlan_create'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" create a vlan on on a bridge device unless vlan already exists """'
newline|'\n'
name|'if'
name|'not'
name|'device_exists'
op|'('
string|'"vlan%s"'
op|'%'
name|'net'
op|'.'
name|'vlan'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|'"sudo vconfig set_name_type VLAN_PLUS_VID_NO_PAD"'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo vconfig add %s %s"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_dev'
op|','
name|'net'
op|'.'
name|'vlan'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo ifconfig vlan%s up"'
op|'%'
op|'('
name|'net'
op|'.'
name|'vlan'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|bridge_create
dedent|''
dedent|''
name|'def'
name|'bridge_create'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" create a bridge on a vlan unless it already exists """'
newline|'\n'
name|'if'
name|'not'
name|'device_exists'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|'"sudo brctl addbr %s"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|')'
op|')'
newline|'\n'
comment|'# execute("sudo brctl setfd %s 0" % (net.bridge_name))'
nl|'\n'
comment|'# execute("sudo brctl setageing %s 10" % (net.bridge_name))'
nl|'\n'
name|'execute'
op|'('
string|'"sudo brctl stp %s off"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|')'
op|')'
newline|'\n'
name|'execute'
op|'('
string|'"sudo brctl addif %s vlan%s"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|','
name|'net'
op|'.'
name|'vlan'
op|')'
op|')'
newline|'\n'
name|'if'
name|'net'
op|'.'
name|'bridge_gets_ip'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|'"sudo ifconfig %s %s broadcast %s netmask %s up"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|','
name|'net'
op|'.'
name|'gateway'
op|','
name|'net'
op|'.'
name|'broadcast'
op|','
name|'net'
op|'.'
name|'netmask'
op|')'
op|')'
newline|'\n'
name|'confirm_rule'
op|'('
string|'"FORWARD --in-interface %s -j ACCEPT"'
op|'%'
op|'('
name|'net'
op|'.'
name|'bridge_name'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|'"sudo ifconfig %s up"'
op|'%'
name|'net'
op|'.'
name|'bridge_name'
op|')'
newline|'\n'
nl|'\n'
DECL|function|dnsmasq_cmd
dedent|''
dedent|''
dedent|''
name|'def'
name|'dnsmasq_cmd'
op|'('
name|'net'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cmd'
op|'='
op|'['
string|"'sudo dnsmasq'"
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
name|'dhcp_file'
op|'('
name|'net'
op|'.'
name|'vlan'
op|','
string|"'pid'"
op|')'
op|','
nl|'\n'
string|"' --listen-address=%s'"
op|'%'
name|'net'
op|'.'
name|'dhcp_listen_address'
op|','
nl|'\n'
string|"' --except-interface=lo'"
op|','
nl|'\n'
string|"' --dhcp-range=%s,%s,120s'"
op|'%'
op|'('
name|'net'
op|'.'
name|'dhcp_range_start'
op|','
name|'net'
op|'.'
name|'dhcp_range_end'
op|')'
op|','
nl|'\n'
string|"' --dhcp-lease-max=61'"
op|','
nl|'\n'
string|"' --dhcp-hostsfile=%s'"
op|'%'
name|'dhcp_file'
op|'('
name|'net'
op|'.'
name|'vlan'
op|','
string|"'conf'"
op|')'
op|','
nl|'\n'
string|"' --dhcp-leasefile=%s'"
op|'%'
name|'dhcp_file'
op|'('
name|'net'
op|'.'
name|'vlan'
op|','
string|"'leases'"
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
DECL|function|hostDHCP
dedent|''
name|'def'
name|'hostDHCP'
op|'('
name|'network'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'idx'
op|'='
name|'host'
op|'['
string|"'address'"
op|']'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|'['
op|'-'
number|'1'
op|']'
comment|"# Logically, the idx of instances they've launched in this net"
newline|'\n'
name|'return'
string|'"%s,%s-%s-%s.novalocal,%s"'
op|'%'
op|'('
name|'host'
op|'['
string|"'mac'"
op|']'
op|','
name|'host'
op|'['
string|"'user_id'"
op|']'
op|','
name|'network'
op|'.'
name|'vlan'
op|','
name|'idx'
op|','
name|'host'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# todo(ja): if the system has restarted or pid numbers have wrapped'
nl|'\n'
comment|'#           then you cannot be certain that the pid refers to the'
nl|'\n'
comment|'#           dnsmasq.  As well, sending a HUP only reloads the hostfile,'
nl|'\n'
comment|'#           so any configuration options (like dchp-range, vlan, ...)'
nl|'\n'
comment|"#           aren't reloaded"
nl|'\n'
DECL|function|start_dnsmasq
dedent|''
name|'def'
name|'start_dnsmasq'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" (re)starts a dnsmasq server for a given network\n\n    if a dnsmasq instance is already running then send a HUP\n    signal causing it to reload, otherwise spawn a new instance\n    """'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'dhcp_file'
op|'('
name|'network'
op|'.'
name|'vlan'
op|','
string|"'conf'"
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'host_name'
name|'in'
name|'network'
op|'.'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
string|'"%s\\n"'
op|'%'
name|'hostDHCP'
op|'('
name|'network'
op|','
name|'network'
op|'.'
name|'hosts'
op|'['
name|'host_name'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'pid'
op|'='
name|'dnsmasq_pid_for'
op|'('
name|'network'
op|')'
newline|'\n'
nl|'\n'
comment|'# if dnsmasq is already running, then tell it to reload'
nl|'\n'
name|'if'
name|'pid'
op|':'
newline|'\n'
comment|'# todo(ja): use "/proc/%d/cmdline" % (pid) to determine if pid refers'
nl|'\n'
comment|'#           correct dnsmasq process'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGHUP'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Killing dnsmasq threw %s"'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
comment|'# otherwise delete the existing leases file and start dnsmasq'
nl|'\n'
dedent|''
dedent|''
name|'lease_file'
op|'='
name|'dhcp_file'
op|'('
name|'network'
op|'.'
name|'vlan'
op|','
string|"'leases'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'lease_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'lease_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'Popen'
op|'('
name|'dnsmasq_cmd'
op|'('
name|'network'
op|')'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|stop_dnsmasq
dedent|''
name|'def'
name|'stop_dnsmasq'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" stops the dnsmasq instance for a given network """'
newline|'\n'
name|'pid'
op|'='
name|'dnsmasq_pid_for'
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
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGTERM'
op|')'
newline|'\n'
nl|'\n'
DECL|function|dhcp_file
dedent|''
dedent|''
name|'def'
name|'dhcp_file'
op|'('
name|'vlan'
op|','
name|'kind'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" return path to a pid, leases or conf file for a vlan """'
newline|'\n'
nl|'\n'
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
name|'vlan'
op|','
name|'kind'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|dnsmasq_pid_for
dedent|''
name|'def'
name|'dnsmasq_pid_for'
op|'('
name|'network'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" the pid for prior dnsmasq instance for a vlan,\n    returns None if no pid file exists\n\n    if machine has rebooted pid might be incorrect (caller should check)\n    """'
newline|'\n'
nl|'\n'
name|'pid_file'
op|'='
name|'dhcp_file'
op|'('
name|'network'
op|'.'
name|'vlan'
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
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
