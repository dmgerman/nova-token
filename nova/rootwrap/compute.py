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
comment|"# nova/virt/disk/mount.py: 'kpartx', '-a', device"
nl|'\n'
comment|"# nova/virt/disk/mount.py: 'kpartx', '-d', device"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/kpartx"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/mount.py: 'tune2fs', '-c', 0, '-i', 0, mapped_device"
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: "tune2fs", "-O ^has_journal", part_path'
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: "tune2fs", "-j", partition_path'
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/tune2fs"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/mount.py: 'mount', mapped_device, mount_dir"
nl|'\n'
comment|"# nova/virt/xenapi/vm_utils.py: 'mount', '-t', 'ext2,ext3,ext4,reiserfs'.."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/mount"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/mount.py: 'umount', mapped_device"
nl|'\n'
comment|"# nova/virt/xenapi/vm_utils.py: 'umount', dev_path"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/umount"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/nbd.py: 'qemu-nbd', '-c', device, image"
nl|'\n'
comment|"# nova/virt/disk/nbd.py: 'qemu-nbd', '-d', device"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/qemu-nbd"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/loop.py: 'losetup', '--find', '--show', image"
nl|'\n'
comment|"# nova/virt/disk/loop.py: 'losetup', '--detach', device"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/losetup"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/guestfs.py: 'guestmount', '--rw', '-a', image, '-i'"
nl|'\n'
comment|"# nova/virt/disk/guestfs.py: 'guestmount', '--rw', '-a', image, '-m' dev"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/guestmount"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/guestfs.py: 'fusermount', 'u', mount_dir"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/fusermount"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/fusermount"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/api.py: 'tee', metadata_path"
nl|'\n'
comment|"# nova/virt/disk/api.py: 'tee', '-a', keyfile"
nl|'\n'
comment|"# nova/virt/disk/api.py: 'tee', netfile"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/bin/tee"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/api.py: 'mkdir', '-p', sshdir"
nl|'\n'
comment|"# nova/virt/disk/api.py: 'mkdir', '-p', netdir"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/mkdir"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/api.py: 'chown', 'root', sshdir"
nl|'\n'
comment|"# nova/virt/disk/api.py: 'chown', 'root:root', netdir"
nl|'\n'
comment|"# nova/virt/libvirt/connection.py: 'chown', os.getuid(), console_log"
nl|'\n'
comment|"# nova/virt/libvirt/connection.py: 'chown', os.getuid(), console_log"
nl|'\n'
comment|"# nova/virt/libvirt/connection.py: 'chown', 'root', basepath('disk')"
nl|'\n'
comment|"# nova/virt/xenapi/vm_utils.py: 'chown', os.getuid(), dev_path"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/chown"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/disk/api.py: 'chmod', '700', sshdir"
nl|'\n'
comment|"# nova/virt/disk/api.py: 'chmod', 755, netdir"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/chmod"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/libvirt/vif.py: 'ip', 'tuntap', 'add', dev, 'mode', 'tap'"
nl|'\n'
comment|"# nova/virt/libvirt/vif.py: 'ip', 'link', 'set', dev, 'up'"
nl|'\n'
comment|"# nova/virt/libvirt/vif.py: 'ip', 'link', 'delete', dev"
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
comment|"# nova/virt/libvirt/vif.py: 'tunctl', '-b', '-t', dev"
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/usr/sbin/tunctl"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/libvirt/vif.py: 'ovs-vsctl', ..."
nl|'\n'
comment|"# nova/virt/libvirt/vif.py: 'ovs-vsctl', 'del-port', ..."
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
nl|'\n'
comment|'# nova/virt/libvirt/connection.py: \'dd\', "if=%s" % virsh_output, ...'
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/bin/dd"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# nova/virt/xenapi/volume_utils.py: 'iscsiadm', '-m', ..."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/iscsiadm"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: "parted", "--script", ...'
nl|'\n'
comment|"# nova/virt/xenapi/vm_utils.py: 'parted', '--script', dev_path, ..*."
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/parted"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: fdisk %(dev_path)s'
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/fdisk"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: "e2fsck", "-f", "-p", partition_path'
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/e2fsck"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# nova/virt/xenapi/vm_utils.py: "resize2fs", partition_path'
nl|'\n'
name|'CommandFilter'
op|'('
string|'"/sbin/resize2fs"'
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
op|']'
newline|'\n'
endmarker|''
end_unit
