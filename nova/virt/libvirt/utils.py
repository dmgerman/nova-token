begin_unit
comment|'#    Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'#    Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'#    All Rights Reserved.'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'#    Copyright (c) 2011 Piston Cloud Computing, Inc'
nl|'\n'
comment|'#    Copyright (c) 2011 OpenStack Foundation'
nl|'\n'
comment|'#    (c) Copyright 2013 Hewlett-Packard Development Company, L.P.'
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
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'arch'
newline|'\n'
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
name|'i18n'
name|'import'
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
name|'as'
name|'vconfig'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'volumeutils'
newline|'\n'
nl|'\n'
DECL|variable|libvirt_opts
name|'libvirt_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'snapshot_compression'"
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
string|"'Compress snapshot images when possible. This '"
nl|'\n'
string|"'currently applies exclusively to qcow2 images'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'libvirt_opts'
op|','
string|"'libvirt'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'instances_path'"
op|','
string|"'nova.compute.manager'"
op|')'
newline|'\n'
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
DECL|function|execute
name|'def'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_iscsi_initiator
dedent|''
name|'def'
name|'get_iscsi_initiator'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'volumeutils'
op|'.'
name|'get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_hbas
dedent|''
name|'def'
name|'get_fc_hbas'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the Fibre Channel HBA information."""'
newline|'\n'
name|'out'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
string|"'systool'"
op|','
string|"'-c'"
op|','
string|"'fc_host'"
op|','
string|"'-v'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# This handles the case where rootwrap is used'
nl|'\n'
comment|'# and systool is not installed'
nl|'\n'
comment|'# 96 = nova.cmd.rootwrap.RC_NOEXECFOUND:'
nl|'\n'
indent|'        '
name|'if'
name|'exc'
op|'.'
name|'exit_code'
op|'=='
number|'96'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"systool is not installed"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# This handles the case where rootwrap is NOT used'
nl|'\n'
comment|'# and systool is not installed'
nl|'\n'
indent|'        '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"systool is not installed"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'out'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"Cannot find any Fibre Channel HBAs"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'lines'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
comment|'# ignore the first 2 lines'
nl|'\n'
name|'lines'
op|'='
name|'lines'
op|'['
number|'2'
op|':'
op|']'
newline|'\n'
name|'hbas'
op|'='
op|'['
op|']'
newline|'\n'
name|'hba'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'lastline'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'        '
name|'line'
op|'='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
comment|'# 2 newlines denotes a new hba port'
nl|'\n'
name|'if'
name|'line'
op|'=='
string|"''"
name|'and'
name|'lastline'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'hba'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'hbas'
op|'.'
name|'append'
op|'('
name|'hba'
op|')'
newline|'\n'
name|'hba'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'val'
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'                '
name|'key'
op|'='
name|'val'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'replace'
op|'('
string|'" "'
op|','
string|'""'
op|')'
newline|'\n'
name|'value'
op|'='
name|'val'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'hba'
op|'['
name|'key'
op|']'
op|'='
name|'value'
op|'.'
name|'replace'
op|'('
string|'\'"\''
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'lastline'
op|'='
name|'line'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hbas'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_hbas_info
dedent|''
name|'def'
name|'get_fc_hbas_info'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get Fibre Channel WWNs and device paths from the system, if any."""'
newline|'\n'
comment|"# Note modern linux kernels contain the FC HBA's in /sys"
nl|'\n'
comment|'# and are obtainable via the systool app'
nl|'\n'
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
name|'hbas_info'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'wwpn'
op|'='
name|'hba'
op|'['
string|"'port_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
name|'wwnn'
op|'='
name|'hba'
op|'['
string|"'node_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
name|'device_path'
op|'='
name|'hba'
op|'['
string|"'ClassDevicepath'"
op|']'
newline|'\n'
name|'device'
op|'='
name|'hba'
op|'['
string|"'ClassDevice'"
op|']'
newline|'\n'
name|'hbas_info'
op|'.'
name|'append'
op|'('
op|'{'
string|"'port_name'"
op|':'
name|'wwpn'
op|','
nl|'\n'
string|"'node_name'"
op|':'
name|'wwnn'
op|','
nl|'\n'
string|"'host_device'"
op|':'
name|'device'
op|','
nl|'\n'
string|"'device_path'"
op|':'
name|'device_path'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hbas_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_wwpns
dedent|''
name|'def'
name|'get_fc_wwpns'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get Fibre Channel WWPNs from the system, if any."""'
newline|'\n'
comment|"# Note modern linux kernels contain the FC HBA's in /sys"
nl|'\n'
comment|'# and are obtainable via the systool app'
nl|'\n'
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'wwpns'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hba'
op|'['
string|"'port_state'"
op|']'
op|'=='
string|"'Online'"
op|':'
newline|'\n'
indent|'                '
name|'wwpn'
op|'='
name|'hba'
op|'['
string|"'port_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
name|'wwpns'
op|'.'
name|'append'
op|'('
name|'wwpn'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'wwpns'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fc_wwnns
dedent|''
name|'def'
name|'get_fc_wwnns'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get Fibre Channel WWNNs from the system, if any."""'
newline|'\n'
comment|"# Note modern linux kernels contain the FC HBA's in /sys"
nl|'\n'
comment|'# and are obtainable via the systool app'
nl|'\n'
name|'hbas'
op|'='
name|'get_fc_hbas'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'wwnns'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hba'
op|'['
string|"'port_state'"
op|']'
op|'=='
string|"'Online'"
op|':'
newline|'\n'
indent|'                '
name|'wwnn'
op|'='
name|'hba'
op|'['
string|"'node_name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
newline|'\n'
name|'wwnns'
op|'.'
name|'append'
op|'('
name|'wwnn'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'wwnns'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
dedent|''
name|'def'
name|'create_image'
op|'('
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a disk image\n\n    :param disk_format: Disk image format (as known by qemu-img)\n    :param path: Desired location of the disk image\n    :param size: Desired size of disk image. May be given as an int or\n                 a string. If given as an int, it will be interpreted\n                 as bytes. If it\'s a string, it should consist of a number\n                 with an optional suffix (\'K\' for Kibibytes,\n                 M for Mebibytes, \'G\' for Gibibytes, \'T\' for Tebibytes).\n                 If no suffix is given, it will be interpreted as bytes.\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_cow_image
dedent|''
name|'def'
name|'create_cow_image'
op|'('
name|'backing_file'
op|','
name|'path'
op|','
name|'size'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create COW image\n\n    Creates a COW image with the given backing file\n\n    :param backing_file: Existing image on which to base the COW image\n    :param path: Desired location of the COW image\n    """'
newline|'\n'
name|'base_cmd'
op|'='
op|'['
string|"'qemu-img'"
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
string|"'qcow2'"
op|']'
newline|'\n'
name|'cow_opts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'backing_file'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'backing_file=%s'"
op|'%'
name|'backing_file'
op|']'
newline|'\n'
name|'base_details'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'backing_file'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'base_details'
op|'='
name|'None'
newline|'\n'
comment|"# This doesn't seem to get inherited so force it to..."
nl|'\n'
comment|'# http://paste.ubuntu.com/1213295/'
nl|'\n'
comment|'# TODO(harlowja) probably file a bug against qemu-img/qemu'
nl|'\n'
dedent|''
name|'if'
name|'base_details'
name|'and'
name|'base_details'
op|'.'
name|'cluster_size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'cluster_size=%s'"
op|'%'
name|'base_details'
op|'.'
name|'cluster_size'
op|']'
newline|'\n'
comment|"# For now don't inherit this due the following discussion..."
nl|'\n'
comment|'# See: http://www.gossamer-threads.com/lists/openstack/dev/10592'
nl|'\n'
comment|"# if 'preallocation' in base_details:"
nl|'\n'
comment|"#     cow_opts += ['preallocation=%s' % base_details['preallocation']]"
nl|'\n'
dedent|''
name|'if'
name|'base_details'
name|'and'
name|'base_details'
op|'.'
name|'encrypted'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'encryption=%s'"
op|'%'
name|'base_details'
op|'.'
name|'encrypted'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'cow_opts'
op|'+='
op|'['
string|"'size=%s'"
op|'%'
name|'size'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'cow_opts'
op|':'
newline|'\n'
comment|'# Format as a comma separated list'
nl|'\n'
indent|'        '
name|'csv_opts'
op|'='
string|'","'
op|'.'
name|'join'
op|'('
name|'cow_opts'
op|')'
newline|'\n'
name|'cow_opts'
op|'='
op|'['
string|"'-o'"
op|','
name|'csv_opts'
op|']'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'base_cmd'
op|'+'
name|'cow_opts'
op|'+'
op|'['
name|'path'
op|']'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|pick_disk_driver_name
dedent|''
name|'def'
name|'pick_disk_driver_name'
op|'('
name|'hypervisor_version'
op|','
name|'is_block_dev'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pick the libvirt primary backend driver name\n\n    If the hypervisor supports multiple backend drivers we have to tell libvirt\n    which one should be used.\n\n    Xen supports the following drivers: "tap", "tap2", "phy", "file", or\n    "qemu", being "qemu" the preferred one. Qemu only supports "qemu".\n\n    :param is_block_dev:\n    :returns: driver_name or None\n    """'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'virt_type'
op|'=='
string|'"xen"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'is_block_dev'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"phy"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# 4002000 == 4.2.0'
nl|'\n'
indent|'            '
name|'if'
name|'hypervisor_version'
op|'>='
number|'4002000'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'qemu'"
newline|'\n'
comment|'# 4000000 == 4.0.0'
nl|'\n'
dedent|''
name|'elif'
name|'hypervisor_version'
op|'>'
number|'4000000'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|'"tap2"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|'"tap"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'virt_type'
name|'in'
op|'('
string|"'kvm'"
op|','
string|"'qemu'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"qemu"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"# UML doesn't want a driver_name set"
nl|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_size
dedent|''
dedent|''
name|'def'
name|'get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the (virtual) size of a disk image\n\n    :param path: Path to the disk image\n    :returns: Size (in bytes) of the given disk image as it would be seen\n              by a virtual machine.\n    """'
newline|'\n'
name|'size'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'virtual_size'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_backing_file
dedent|''
name|'def'
name|'get_disk_backing_file'
op|'('
name|'path'
op|','
name|'basename'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the backing file of a disk image\n\n    :param path: Path to the disk image\n    :returns: a path to the image\'s backing store\n    """'
newline|'\n'
name|'backing_file'
op|'='
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'backing_file'
newline|'\n'
name|'if'
name|'backing_file'
name|'and'
name|'basename'
op|':'
newline|'\n'
indent|'        '
name|'backing_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'backing_file'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'backing_file'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|copy_image
dedent|''
name|'def'
name|'copy_image'
op|'('
name|'src'
op|','
name|'dest'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Copy a disk image to an existing directory\n\n    :param src: Source image\n    :param dest: Destination path\n    :param host: Remote host\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
comment|'# We shell out to cp because that will intelligently copy'
nl|'\n'
comment|'# sparse files.  I.E. holes will not be written to DEST,'
nl|'\n'
comment|'# rather recreated efficiently.  In addition, since'
nl|'\n'
comment|'# coreutils 8.11, holes can be read efficiently too.'
nl|'\n'
indent|'        '
name|'execute'
op|'('
string|"'cp'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'dest'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'host'
op|','
name|'dest'
op|')'
newline|'\n'
comment|'# Try rsync first as that can compress and create sparse dest files.'
nl|'\n'
comment|"# Note however that rsync currently doesn't read sparse files"
nl|'\n'
comment|'# efficiently: https://bugzilla.samba.org/show_bug.cgi?id=8918'
nl|'\n'
comment|'# At least network traffic is mitigated with compression.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Do a relatively light weight test first, so that we'
nl|'\n'
comment|'# can fall back to scp, without having run out of space'
nl|'\n'
comment|'# on the destination for example.'
nl|'\n'
indent|'            '
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
string|"'--compress'"
op|','
string|"'--dry-run'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|"'scp'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
string|"'--compress'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
dedent|''
dedent|''
name|'def'
name|'write_to_file'
op|'('
name|'path'
op|','
name|'contents'
op|','
name|'umask'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Write the given contents to a file\n\n    :param path: Destination file\n    :param contents: Desired contents of the file\n    :param umask: Umask to set when creating this file (will be reset)\n    """'
newline|'\n'
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'        '
name|'saved_umask'
op|'='
name|'os'
op|'.'
name|'umask'
op|'('
name|'umask'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
name|'contents'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'umask'
op|'('
name|'saved_umask'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown
dedent|''
dedent|''
dedent|''
name|'def'
name|'chown'
op|'('
name|'path'
op|','
name|'owner'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Change ownership of file or directory\n\n    :param path: File or directory whose ownership to change\n    :param owner: Desired new owner (given as uid or username)\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'chown'"
op|','
name|'owner'
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_id_map_to_config
dedent|''
name|'def'
name|'_id_map_to_config'
op|'('
name|'id_map'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"%s:%s:%s"'
op|'%'
op|'('
name|'id_map'
op|'.'
name|'start'
op|','
name|'id_map'
op|'.'
name|'target'
op|','
name|'id_map'
op|'.'
name|'count'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown_for_id_maps
dedent|''
name|'def'
name|'chown_for_id_maps'
op|'('
name|'path'
op|','
name|'id_maps'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Change ownership of file or directory for an id mapped\n    environment\n\n    :param path: File or directory whose ownership to change\n    :param id_maps: List of type LibvirtConfigGuestIDMap\n    """'
newline|'\n'
name|'uid_maps_str'
op|'='
string|"','"
op|'.'
name|'join'
op|'('
op|'['
name|'_id_map_to_config'
op|'('
name|'id_map'
op|')'
name|'for'
name|'id_map'
name|'in'
name|'id_maps'
name|'if'
nl|'\n'
name|'isinstance'
op|'('
name|'id_map'
op|','
nl|'\n'
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestUIDMap'
op|')'
op|']'
op|')'
newline|'\n'
name|'gid_maps_str'
op|'='
string|"','"
op|'.'
name|'join'
op|'('
op|'['
name|'_id_map_to_config'
op|'('
name|'id_map'
op|')'
name|'for'
name|'id_map'
name|'in'
name|'id_maps'
name|'if'
nl|'\n'
name|'isinstance'
op|'('
name|'id_map'
op|','
nl|'\n'
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestGIDMap'
op|')'
op|']'
op|')'
newline|'\n'
name|'execute'
op|'('
string|"'nova-idmapshift'"
op|','
string|"'-i'"
op|','
string|"'-u'"
op|','
name|'uid_maps_str'
op|','
nl|'\n'
string|"'-g'"
op|','
name|'gid_maps_str'
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_snapshot
dedent|''
name|'def'
name|'extract_snapshot'
op|'('
name|'disk_path'
op|','
name|'source_fmt'
op|','
name|'out_path'
op|','
name|'dest_fmt'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract a snapshot from a disk image.\n    Note that nobody should write to the disk image during this operation.\n\n    :param disk_path: Path to disk image\n    :param out_path: Desired path of extracted snapshot\n    """'
newline|'\n'
comment|'# NOTE(markmc): ISO is just raw to qemu-img'
nl|'\n'
name|'if'
name|'dest_fmt'
op|'=='
string|"'iso'"
op|':'
newline|'\n'
indent|'        '
name|'dest_fmt'
op|'='
string|"'raw'"
newline|'\n'
nl|'\n'
dedent|''
name|'qemu_img_cmd'
op|'='
op|'('
string|"'qemu-img'"
op|','
string|"'convert'"
op|','
string|"'-f'"
op|','
name|'source_fmt'
op|','
string|"'-O'"
op|','
name|'dest_fmt'
op|')'
newline|'\n'
nl|'\n'
comment|'# Conditionally enable compression of snapshots.'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'snapshot_compression'
name|'and'
name|'dest_fmt'
op|'=='
string|'"qcow2"'
op|':'
newline|'\n'
indent|'        '
name|'qemu_img_cmd'
op|'+='
op|'('
string|"'-c'"
op|','
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'qemu_img_cmd'
op|'+='
op|'('
name|'disk_path'
op|','
name|'out_path'
op|')'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'qemu_img_cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_file
dedent|''
name|'def'
name|'load_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read contents of file\n\n    :param path: File to read\n    """'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'r'"
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fp'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_open
dedent|''
dedent|''
name|'def'
name|'file_open'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Open file\n\n    see built-in file() documentation for more details\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'file'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete (unlink) file\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|path_exists
dedent|''
name|'def'
name|'path_exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns if path exists\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_disk
dedent|''
name|'def'
name|'find_disk'
op|'('
name|'virt_dom'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find root device path for instance\n\n    May be file or device\n    """'
newline|'\n'
name|'xml_desc'
op|'='
name|'virt_dom'
op|'.'
name|'XMLDesc'
op|'('
number|'0'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'xml_desc'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'virt_type'
op|'=='
string|"'lxc'"
op|':'
newline|'\n'
indent|'        '
name|'source'
op|'='
name|'domain'
op|'.'
name|'find'
op|'('
string|"'devices/filesystem/source'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'source'
op|'.'
name|'get'
op|'('
string|"'dir'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'disk_path'
op|'['
number|'0'
op|':'
name|'disk_path'
op|'.'
name|'rfind'
op|'('
string|"'rootfs'"
op|')'
op|']'
newline|'\n'
name|'disk_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'disk_path'
op|','
string|"'disk'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'source'
op|'='
name|'domain'
op|'.'
name|'find'
op|'('
string|"'devices/disk/source'"
op|')'
newline|'\n'
name|'disk_path'
op|'='
name|'source'
op|'.'
name|'get'
op|'('
string|"'file'"
op|')'
name|'or'
name|'source'
op|'.'
name|'get'
op|'('
string|"'dev'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'disk_path'
name|'and'
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'images_type'
op|'=='
string|"'rbd'"
op|':'
newline|'\n'
indent|'            '
name|'disk_path'
op|'='
name|'source'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'if'
name|'disk_path'
op|':'
newline|'\n'
indent|'                '
name|'disk_path'
op|'='
string|"'rbd:'"
op|'+'
name|'disk_path'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'not'
name|'disk_path'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|'"Can\'t retrieve root device path "'
nl|'\n'
string|'"from instance libvirt configuration"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'disk_path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_type
dedent|''
name|'def'
name|'get_disk_type'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve disk type (raw, qcow2, lvm) for given file."""'
newline|'\n'
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/dev'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'lvm'"
newline|'\n'
dedent|''
name|'elif'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'rbd:'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'rbd'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'images'
op|'.'
name|'qemu_img_info'
op|'('
name|'path'
op|')'
op|'.'
name|'file_format'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fs_info
dedent|''
name|'def'
name|'get_fs_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get free/used/total space info for a filesystem\n\n    :param path: Any dirent on the filesystem\n    :returns: A dict containing:\n\n             :free: How much space is free (in bytes)\n             :used: How much space is used (in bytes)\n             :total: How big the filesystem is (in bytes)\n    """'
newline|'\n'
name|'hddinfo'
op|'='
name|'os'
op|'.'
name|'statvfs'
op|'('
name|'path'
op|')'
newline|'\n'
name|'total'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_blocks'
newline|'\n'
name|'free'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_bavail'
newline|'\n'
name|'used'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
op|'('
name|'hddinfo'
op|'.'
name|'f_blocks'
op|'-'
name|'hddinfo'
op|'.'
name|'f_bfree'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'total'"
op|':'
name|'total'
op|','
nl|'\n'
string|"'free'"
op|':'
name|'free'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'used'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image
dedent|''
name|'def'
name|'fetch_image'
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
name|'max_size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Grab image."""'
newline|'\n'
name|'images'
op|'.'
name|'fetch_to_raw'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'target'
op|','
name|'user_id'
op|','
name|'project_id'
op|','
nl|'\n'
name|'max_size'
op|'='
name|'max_size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_instance_path
dedent|''
name|'def'
name|'get_instance_path'
op|'('
name|'instance'
op|','
name|'forceold'
op|'='
name|'False'
op|','
name|'relative'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the correct path for instance storage.\n\n    This method determines the directory name for instance storage, while\n    handling the fact that we changed the naming style to something more\n    unique in the grizzly release.\n\n    :param instance: the instance we want a path for\n    :param forceold: force the use of the pre-grizzly format\n    :param relative: if True, just the relative path is returned\n\n    :returns: a path to store information about that instance\n    """'
newline|'\n'
name|'pre_grizzly_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'forceold'
name|'or'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pre_grizzly_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'relative'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'pre_grizzly_name'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'relative'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_arch
dedent|''
name|'def'
name|'get_arch'
op|'('
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the architecture of the guest (or host).\n\n    This method determines the CPU architecture that must be supported by\n    the hypervisor. It gets the (guest) arch info from image_meta properties,\n    and it will fallback to the nova-compute (host) arch if no architecture\n    info is provided in image_meta.\n\n    :param image_meta: the metadata associated with the instance image\n\n    :returns: guest (or host) architecture\n    """'
newline|'\n'
name|'if'
name|'image_meta'
op|':'
newline|'\n'
indent|'        '
name|'image_arch'
op|'='
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'properties'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
string|"'architecture'"
op|')'
newline|'\n'
name|'if'
name|'image_arch'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'image_arch'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'arch'
op|'.'
name|'from_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_mounted
dedent|''
name|'def'
name|'is_mounted'
op|'('
name|'mount_path'
op|','
name|'source'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the given source is mounted at given destination point."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'check_cmd'
op|'='
op|'['
string|"'findmnt'"
op|','
string|"'--target'"
op|','
name|'mount_path'
op|']'
newline|'\n'
name|'if'
name|'source'
op|':'
newline|'\n'
indent|'            '
name|'check_cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|"'--source'"
op|','
name|'source'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'check_cmd'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|"# info since it's not required to have this tool."
nl|'\n'
indent|'        '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"findmnt tool is not installed"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_valid_hostname
dedent|''
dedent|''
name|'def'
name|'is_valid_hostname'
op|'('
name|'hostname'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'re'
op|'.'
name|'match'
op|'('
string|'r"^[\\w\\-\\.:]+$"'
op|','
name|'hostname'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
