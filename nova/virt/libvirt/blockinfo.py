begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (C) 2012-2013 Red Hat, Inc.'
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
string|'"""\nHandling of block device information and mapping.\n\nThis module contains helper methods for interpreting the block\ndevice information and determining the suitable mapping to\nguest devices and libvirt XML.\n\nThroughout these methods there are a number of standard\nvariables / types used\n\n * \'mapping\': a dict contains the storage device mapping.\n\n   For the default disk types it will contain the following\n   keys & values:\n\n      \'disk\' -> disk_info\n      \'disk.rescue\' -> disk_info\n      \'disk.local\' -> disk_info\n      \'disk.swap\' -> disk_info\n      \'disk.config\' -> disk_info\n\n   If any of the default disks are overridden by the block\n   device info mappings, the hash value will be None\n\n   For any ephemeral device there will also be a dict entry\n\n      \'disk.eph$NUM\' -> disk_info\n\n   For any volume device there will also be a dict entry:\n\n       $path -> disk_info\n\n   Finally a special key will refer to the root device:\n\n      \'root\' -> disk_info\n\n\n * \'disk_info\': a tuple specifying disk configuration\n\n   It contains the following 3 fields\n\n      (disk bus, disk dev, device type)\n\n   and possibly these optional fields: (\'format\',)\n\n * \'disk_bus\': the guest bus type (\'ide\', \'virtio\', \'scsi\', etc)\n\n * \'disk_dev\': the device name \'vda\', \'hdc\', \'sdf\', \'xvde\' etc\n\n * \'device_type\': type of device eg \'disk\', \'cdrom\', \'floppy\'\n\n * \'format\': Which format to apply to the device if applicable\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'block_device'
name|'as'
name|'driver_block_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'configdrive'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SUPPORTED_DEVICE_TYPES
name|'SUPPORTED_DEVICE_TYPES'
op|'='
op|'('
string|"'disk'"
op|','
string|"'cdrom'"
op|','
string|"'floppy'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|has_disk_dev
name|'def'
name|'has_disk_dev'
op|'('
name|'mapping'
op|','
name|'disk_dev'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine if a disk device name has already been used.\n\n       Looks at all the keys in mapping to see if any\n       corresponding disk_info tuple has a device name\n       matching disk_dev\n\n       Returns True if the disk_dev is in use.\n    """'
newline|'\n'
nl|'\n'
name|'for'
name|'disk'
name|'in'
name|'mapping'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'mapping'
op|'['
name|'disk'
op|']'
newline|'\n'
name|'if'
name|'info'
op|'['
string|"'dev'"
op|']'
op|'=='
name|'disk_dev'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dev_prefix_for_disk_bus
dedent|''
name|'def'
name|'get_dev_prefix_for_disk_bus'
op|'('
name|'disk_bus'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the dev prefix for a disk bus.\n\n       Determine the dev prefix to be combined\n       with a disk number to fix a disk_dev.\n       eg \'hd\' for \'ide\' bus can be used to\n       form a disk dev \'hda\'\n\n       Returns the dev prefix or raises an\n       exception if the disk bus is unknown.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'libvirt_disk_prefix'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'CONF'
op|'.'
name|'libvirt_disk_prefix'
newline|'\n'
dedent|''
name|'if'
name|'disk_bus'
op|'=='
string|'"ide"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"hd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"virtio"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"vd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"xen"'
op|':'
newline|'\n'
comment|'# Two possible mappings for Xen, xvda or sda'
nl|'\n'
comment|'# which are interchangable, so we pick sda'
nl|'\n'
indent|'        '
name|'return'
string|'"sd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"scsi"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"sd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"usb"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"sd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"uml"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"ubd"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_bus'
op|'=='
string|'"lxc"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unable to determine disk prefix for %s"'
op|')'
op|'%'
nl|'\n'
name|'disk_bus'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dev_count_for_disk_bus
dedent|''
dedent|''
name|'def'
name|'get_dev_count_for_disk_bus'
op|'('
name|'disk_bus'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the number disks supported.\n\n       Determine how many disks can be supported in\n       a single VM for a particular disk bus.\n\n       Returns the number of disks supported.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'disk_bus'
op|'=='
string|'"ide"'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'4'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'26'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_disk_dev_for_disk_bus
dedent|''
dedent|''
name|'def'
name|'find_disk_dev_for_disk_bus'
op|'('
name|'mapping'
op|','
name|'bus'
op|','
name|'last_device'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Identify a free disk dev name for a bus.\n\n       Determines the possible disk dev names for\n       the bus, and then checks them in order until\n       it identifies one that is not yet used in the\n       disk mapping. If \'last_device\' is set, it will\n       only consider the last available disk dev name.\n\n       Returns the chosen disk_dev name, or raises an\n       exception if none is available.\n    """'
newline|'\n'
nl|'\n'
name|'dev_prefix'
op|'='
name|'get_dev_prefix_for_disk_bus'
op|'('
name|'bus'
op|')'
newline|'\n'
name|'if'
name|'dev_prefix'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'max_dev'
op|'='
name|'get_dev_count_for_disk_bus'
op|'('
name|'bus'
op|')'
newline|'\n'
name|'if'
name|'last_device'
op|':'
newline|'\n'
indent|'        '
name|'devs'
op|'='
op|'['
name|'max_dev'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'devs'
op|'='
name|'range'
op|'('
name|'max_dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'idx'
name|'in'
name|'devs'
op|':'
newline|'\n'
indent|'        '
name|'disk_dev'
op|'='
name|'dev_prefix'
op|'+'
name|'chr'
op|'('
name|'ord'
op|'('
string|"'a'"
op|')'
op|'+'
name|'idx'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'has_disk_dev'
op|'('
name|'mapping'
op|','
name|'disk_dev'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'disk_dev'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"No free disk device names for prefix \'%s\'"'
op|')'
op|','
nl|'\n'
name|'dev_prefix'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_disk_bus_valid_for_virt
dedent|''
name|'def'
name|'is_disk_bus_valid_for_virt'
op|'('
name|'virt_type'
op|','
name|'disk_bus'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'valid_bus'
op|'='
op|'{'
nl|'\n'
string|"'qemu'"
op|':'
op|'['
string|"'virtio'"
op|','
string|"'scsi'"
op|','
string|"'ide'"
op|','
string|"'usb'"
op|']'
op|','
nl|'\n'
string|"'kvm'"
op|':'
op|'['
string|"'virtio'"
op|','
string|"'scsi'"
op|','
string|"'ide'"
op|','
string|"'usb'"
op|']'
op|','
nl|'\n'
string|"'xen'"
op|':'
op|'['
string|"'xen'"
op|','
string|"'ide'"
op|']'
op|','
nl|'\n'
string|"'uml'"
op|':'
op|'['
string|"'uml'"
op|']'
op|','
nl|'\n'
string|"'lxc'"
op|':'
op|'['
string|"'lxc'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'virt_type'
name|'not'
name|'in'
name|'valid_bus'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedVirtType'
op|'('
name|'virt'
op|'='
name|'virt_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'disk_bus'
name|'in'
name|'valid_bus'
op|'['
name|'virt_type'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_bus_for_device_type
dedent|''
name|'def'
name|'get_disk_bus_for_device_type'
op|'('
name|'virt_type'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'None'
op|','
nl|'\n'
name|'device_type'
op|'='
string|'"disk"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the best disk bus to use for a device type.\n\n       Considering the currently configured virtualization\n       type, return the optimal disk_bus to use for a given\n       device type. For example, for a disk on KVM it will\n       return \'virtio\', while for a CDROM it will return \'ide\'\n\n       Returns the disk_bus, or returns None if the device\n       type is not supported for this virtualization\n    """'
newline|'\n'
nl|'\n'
comment|'# Prefer a disk bus set against the image first of all'
nl|'\n'
name|'if'
name|'image_meta'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
string|'"hw_"'
op|'+'
name|'device_type'
op|'+'
string|'"_bus"'
newline|'\n'
name|'disk_bus'
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
name|'key'
op|')'
newline|'\n'
name|'if'
name|'disk_bus'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'is_disk_bus_valid_for_virt'
op|'('
name|'virt_type'
op|','
name|'disk_bus'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'UnsupportedHardware'
op|'('
name|'model'
op|'='
name|'disk_bus'
op|','
nl|'\n'
name|'virt'
op|'='
name|'virt_type'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'disk_bus'
newline|'\n'
nl|'\n'
comment|'# Otherwise pick a hypervisor default disk bus'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'virt_type'
op|'=='
string|'"uml"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device_type'
op|'=='
string|'"disk"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"uml"'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'virt_type'
op|'=='
string|'"lxc"'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"lxc"'
newline|'\n'
dedent|''
name|'elif'
name|'virt_type'
op|'=='
string|'"xen"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device_type'
op|'=='
string|'"cdrom"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"ide"'
newline|'\n'
dedent|''
name|'elif'
name|'device_type'
op|'=='
string|'"disk"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"xen"'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'virt_type'
name|'in'
op|'('
string|'"qemu"'
op|','
string|'"kvm"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device_type'
op|'=='
string|'"cdrom"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"ide"'
newline|'\n'
dedent|''
name|'elif'
name|'device_type'
op|'=='
string|'"disk"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"virtio"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_bus_for_disk_dev
dedent|''
name|'def'
name|'get_disk_bus_for_disk_dev'
op|'('
name|'virt_type'
op|','
name|'disk_dev'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the disk bus for a disk device.\n\n       Given a disk device like \'hda\', \'sdf\', \'xvdb\', etc\n       guess what the most appropriate disk bus is for\n       the currently configured virtualization technology\n\n       Returns the disk bus, or raises an Exception if\n       the disk device prefix is unknown.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'disk_dev'
op|'['
op|':'
number|'2'
op|']'
op|'=='
string|"'hd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"ide"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_dev'
op|'['
op|':'
number|'2'
op|']'
op|'=='
string|"'sd'"
op|':'
newline|'\n'
comment|"# Reverse mapping 'sd' is not reliable"
nl|'\n'
comment|'# there are many possible mappings. So'
nl|'\n'
comment|'# this picks the most likely mappings'
nl|'\n'
indent|'        '
name|'if'
name|'virt_type'
op|'=='
string|'"xen"'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"xen"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"scsi"'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'disk_dev'
op|'['
op|':'
number|'2'
op|']'
op|'=='
string|"'vd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"virtio"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_dev'
op|'['
op|':'
number|'3'
op|']'
op|'=='
string|"'xvd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"xen"'
newline|'\n'
dedent|''
name|'elif'
name|'disk_dev'
op|'['
op|':'
number|'3'
op|']'
op|'=='
string|"'ubd'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"uml"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Unable to determine disk bus for \'%s\'"'
op|')'
op|'%'
nl|'\n'
name|'disk_dev'
op|'['
op|':'
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_next_disk_info
dedent|''
dedent|''
name|'def'
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
name|'disk_bus'
op|','
nl|'\n'
name|'device_type'
op|'='
string|"'disk'"
op|','
nl|'\n'
name|'last_device'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the disk info for the next device on disk_bus.\n\n       Considering the disks already listed in the disk mapping,\n       determine the next available disk dev that can be assigned\n       for the disk bus.\n\n       Returns the disk_info for the next available disk.\n    """'
newline|'\n'
nl|'\n'
name|'disk_dev'
op|'='
name|'find_disk_dev_for_disk_bus'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'disk_bus'
op|','
nl|'\n'
name|'last_device'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'bus'"
op|':'
name|'disk_bus'
op|','
nl|'\n'
string|"'dev'"
op|':'
name|'disk_dev'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'device_type'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_eph_disk
dedent|''
name|'def'
name|'get_eph_disk'
op|'('
name|'index'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'disk.eph'"
op|'+'
name|'str'
op|'('
name|'index'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_config_drive_type
dedent|''
name|'def'
name|'get_config_drive_type'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine the type of config drive.\n\n       If config_drive_format is set to iso9660 then the config drive will\n       be \'cdrom\', otherwise \'disk\'.\n\n       Returns a string indicating the config drive type.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'config_drive_format'
op|'=='
string|"'iso9660'"
op|':'
newline|'\n'
indent|'        '
name|'config_drive_type'
op|'='
string|"'cdrom'"
newline|'\n'
dedent|''
name|'elif'
name|'CONF'
op|'.'
name|'config_drive_format'
op|'=='
string|"'vfat'"
op|':'
newline|'\n'
indent|'        '
name|'config_drive_type'
op|'='
string|"'disk'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ConfigDriveUnknownFormat'
op|'('
nl|'\n'
name|'format'
op|'='
name|'CONF'
op|'.'
name|'config_drive_format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'config_drive_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_info_from_bdm
dedent|''
name|'def'
name|'get_info_from_bdm'
op|'('
name|'virt_type'
op|','
name|'bdm'
op|','
name|'mapping'
op|'='
op|'{'
op|'}'
op|','
name|'disk_bus'
op|'='
name|'None'
op|','
nl|'\n'
name|'dev_type'
op|'='
name|'None'
op|','
name|'allowed_types'
op|'='
name|'None'
op|','
nl|'\n'
name|'assigned_devices'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'allowed_types'
op|'='
name|'allowed_types'
name|'or'
name|'SUPPORTED_DEVICE_TYPES'
newline|'\n'
name|'device_name'
op|'='
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
name|'get_device_name'
op|'('
name|'bdm'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'bdm_type'
op|'='
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'device_type'"
op|')'
name|'or'
name|'dev_type'
newline|'\n'
name|'if'
name|'bdm_type'
name|'not'
name|'in'
name|'allowed_types'
op|':'
newline|'\n'
indent|'        '
name|'bdm_type'
op|'='
string|"'disk'"
newline|'\n'
nl|'\n'
dedent|''
name|'bdm_bus'
op|'='
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'disk_bus'"
op|')'
name|'or'
name|'disk_bus'
newline|'\n'
name|'if'
name|'not'
name|'is_disk_bus_valid_for_virt'
op|'('
name|'virt_type'
op|','
name|'bdm_bus'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device_name'
op|':'
newline|'\n'
indent|'            '
name|'bdm_bus'
op|'='
name|'get_disk_bus_for_disk_dev'
op|'('
name|'virt_type'
op|','
name|'device_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'bdm_bus'
op|'='
name|'get_disk_bus_for_device_type'
op|'('
name|'virt_type'
op|','
name|'None'
op|','
name|'bdm_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'device_name'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'assigned_devices'
op|':'
newline|'\n'
indent|'            '
name|'padded_mapping'
op|'='
name|'dict'
op|'('
op|'('
name|'dev'
op|','
op|'{'
string|"'dev'"
op|':'
name|'dev'
op|'}'
op|')'
nl|'\n'
name|'for'
name|'dev'
name|'in'
name|'assigned_devices'
op|')'
newline|'\n'
name|'padded_mapping'
op|'.'
name|'update'
op|'('
name|'mapping'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'padded_mapping'
op|'='
name|'mapping'
newline|'\n'
nl|'\n'
dedent|''
name|'device_name'
op|'='
name|'find_disk_dev_for_disk_bus'
op|'('
name|'padded_mapping'
op|','
name|'bdm_bus'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'bdm_info'
op|'='
op|'{'
string|"'bus'"
op|':'
name|'bdm_bus'
op|','
nl|'\n'
string|"'dev'"
op|':'
name|'device_name'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'bdm_type'
op|'}'
newline|'\n'
nl|'\n'
name|'bdm_format'
op|'='
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'guest_format'"
op|')'
newline|'\n'
name|'if'
name|'bdm_format'
op|':'
newline|'\n'
indent|'        '
name|'bdm_info'
op|'.'
name|'update'
op|'('
op|'{'
string|"'format'"
op|':'
name|'bdm_format'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'bdm_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_device_name
dedent|''
name|'def'
name|'get_device_name'
op|'('
name|'bdm'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the device name if present regardless of the bdm format."""'
newline|'\n'
name|'return'
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'device_name'"
op|')'
name|'or'
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'mount_device'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_root_info
dedent|''
name|'def'
name|'get_root_info'
op|'('
name|'virt_type'
op|','
name|'image_meta'
op|','
name|'root_bdm'
op|','
name|'disk_bus'
op|','
name|'cdrom_bus'
op|','
nl|'\n'
name|'root_device_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# NOTE (ndipanov): This is a hack to avoid considering an image'
nl|'\n'
comment|"#                  BDM with local target, as we don't support them"
nl|'\n'
comment|'#                  yet. Only aplies when passed non-driver format'
nl|'\n'
indent|'    '
name|'no_root_bdm'
op|'='
op|'('
name|'not'
name|'root_bdm'
name|'or'
op|'('
nl|'\n'
name|'root_bdm'
op|'.'
name|'get'
op|'('
string|"'source_type'"
op|')'
op|'=='
string|"'image'"
name|'and'
nl|'\n'
name|'root_bdm'
op|'.'
name|'get'
op|'('
string|"'destination_type'"
op|')'
op|'=='
string|"'local'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'no_root_bdm'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'image_meta'
name|'and'
name|'image_meta'
op|'.'
name|'get'
op|'('
string|"'disk_format'"
op|')'
op|'=='
string|"'iso'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'root_device_bus'
op|'='
name|'cdrom_bus'
newline|'\n'
name|'root_device_type'
op|'='
string|"'cdrom'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_device_bus'
op|'='
name|'disk_bus'
newline|'\n'
name|'root_device_type'
op|'='
string|"'disk'"
newline|'\n'
dedent|''
name|'if'
name|'root_device_name'
op|':'
newline|'\n'
indent|'            '
name|'root_device_bus'
op|'='
name|'get_disk_bus_for_disk_dev'
op|'('
name|'virt_type'
op|','
nl|'\n'
name|'root_device_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'root_device_name'
op|'='
name|'find_disk_dev_for_disk_bus'
op|'('
op|'{'
op|'}'
op|','
name|'root_device_bus'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
string|"'bus'"
op|':'
name|'root_device_bus'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'root_device_type'
op|','
nl|'\n'
string|"'dev'"
op|':'
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
name|'root_device_name'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'get_device_name'
op|'('
name|'root_bdm'
op|')'
name|'and'
name|'root_device_name'
op|':'
newline|'\n'
indent|'            '
name|'root_bdm'
op|'='
name|'root_bdm'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'root_bdm'
op|'['
string|"'device_name'"
op|']'
op|'='
name|'root_device_name'
newline|'\n'
dedent|''
name|'return'
name|'get_info_from_bdm'
op|'('
name|'virt_type'
op|','
name|'root_bdm'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|default_device_names
dedent|''
dedent|''
name|'def'
name|'default_device_names'
op|'('
name|'virt_type'
op|','
name|'instance'
op|','
name|'root_device_name'
op|','
nl|'\n'
name|'update_func'
op|','
name|'ephemerals'
op|','
name|'swap'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
name|'root_device_name'
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'driver_block_device'
op|'.'
name|'get_swap'
op|'('
nl|'\n'
name|'driver_block_device'
op|'.'
name|'convert_swap'
op|'('
name|'swap'
op|')'
op|')'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
name|'driver_block_device'
op|'.'
name|'convert_ephemerals'
op|'('
name|'ephemerals'
op|')'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'('
nl|'\n'
name|'driver_block_device'
op|'.'
name|'convert_volumes'
op|'('
nl|'\n'
name|'block_device_mapping'
op|')'
op|'+'
nl|'\n'
name|'driver_block_device'
op|'.'
name|'convert_snapshots'
op|'('
nl|'\n'
name|'block_device_mapping'
op|')'
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'devices'
op|'='
name|'dict'
op|'('
op|'('
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|','
name|'bdm'
op|')'
name|'for'
name|'bdm'
name|'in'
nl|'\n'
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'ephemerals'
op|','
name|'swap'
op|','
name|'block_device_mapping'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'get_disk_info'
op|'('
name|'virt_type'
op|','
name|'instance'
op|','
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'driver_bdm'
name|'in'
name|'itertools'
op|'.'
name|'chain'
op|'('
name|'block_device_info'
op|'['
string|"'ephemerals'"
op|']'
op|','
nl|'\n'
op|'['
name|'block_device_info'
op|'['
string|"'swap'"
op|']'
op|']'
name|'if'
nl|'\n'
name|'block_device_info'
op|'['
string|"'swap'"
op|']'
name|'else'
op|'['
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|'['
string|"'block_device_mapping'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'driver_bdm'
op|'.'
name|'id'
name|'in'
name|'devices'
op|':'
newline|'\n'
indent|'            '
name|'bdm'
op|'='
name|'devices'
op|'['
name|'driver_bdm'
op|'.'
name|'id'
op|']'
newline|'\n'
comment|'# NOTE (ndipanov): We may have chosen different values'
nl|'\n'
comment|'# for bus and type so update those along with device name'
nl|'\n'
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|'='
name|'get_device_name'
op|'('
name|'driver_bdm'
op|')'
newline|'\n'
name|'bdm'
op|'['
string|"'disk_bus'"
op|']'
op|'='
name|'driver_bdm'
op|'['
string|"'disk_bus'"
op|']'
newline|'\n'
comment|'# Swap does not have device type in driver format'
nl|'\n'
name|'bdm'
op|'['
string|"'device_type'"
op|']'
op|'='
name|'driver_bdm'
op|'.'
name|'get'
op|'('
string|"'device_type'"
op|','
string|"'disk'"
op|')'
newline|'\n'
name|'if'
name|'update_func'
op|':'
newline|'\n'
indent|'                '
name|'update_func'
op|'('
name|'bdm'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|has_default_ephemeral
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'has_default_ephemeral'
op|'('
name|'instance'
op|','
name|'disk_bus'
op|','
name|'block_device_info'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ephemerals'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'instance'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'<='
number|'0'
name|'or'
name|'ephemerals'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
name|'disk_bus'
op|')'
newline|'\n'
name|'if'
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
name|'info'
op|'['
string|"'dev'"
op|']'
op|','
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_bdm
dedent|''
dedent|''
name|'def'
name|'update_bdm'
op|'('
name|'bdm'
op|','
name|'info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'device_name_field'
op|'='
op|'('
string|"'device_name'"
nl|'\n'
name|'if'
string|"'device_name'"
name|'in'
name|'bdm'
nl|'\n'
name|'else'
string|"'mount_device'"
op|')'
newline|'\n'
comment|'# Do not update the device name if it was already present'
nl|'\n'
name|'bdm'
op|'.'
name|'update'
op|'('
name|'dict'
op|'('
name|'zip'
op|'('
op|'('
name|'device_name_field'
op|','
nl|'\n'
string|"'disk_bus'"
op|','
string|"'device_type'"
op|')'
op|','
nl|'\n'
op|'('
op|'('
name|'bdm'
op|'.'
name|'get'
op|'('
name|'device_name_field'
op|')'
name|'or'
nl|'\n'
name|'block_device'
op|'.'
name|'prepend_dev'
op|'('
name|'info'
op|'['
string|"'dev'"
op|']'
op|')'
op|')'
op|','
nl|'\n'
name|'info'
op|'['
string|"'bus'"
op|']'
op|','
name|'info'
op|'['
string|"'type'"
op|']'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_mapping
dedent|''
name|'def'
name|'get_disk_mapping'
op|'('
name|'virt_type'
op|','
name|'instance'
op|','
nl|'\n'
name|'disk_bus'
op|','
name|'cdrom_bus'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'None'
op|','
name|'rescue'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine how to map default disks to the virtual machine.\n\n       This is about figuring out whether the default \'disk\',\n       \'disk.local\', \'disk.swap\' and \'disk.config\' images have\n       been overridden by the block device mapping.\n\n       Returns the guest disk mapping for the devices.\n    """'
newline|'\n'
nl|'\n'
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'extract_flavor'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'pre_assigned_device_names'
op|'='
op|'['
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
name|'get_device_name'
op|'('
name|'bdm'
op|')'
op|')'
name|'for'
name|'bdm'
name|'in'
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'block_device_info'
op|')'
op|','
nl|'\n'
op|'['
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
op|']'
op|','
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
op|')'
nl|'\n'
name|'if'
name|'get_device_name'
op|'('
name|'bdm'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'virt_type'
op|'=='
string|'"lxc"'
op|':'
newline|'\n'
comment|'# NOTE(zul): This information is not used by the libvirt driver'
nl|'\n'
comment|'# however we need to populate mapping so the image can be'
nl|'\n'
comment|'# created when the instance is started. This can'
nl|'\n'
comment|'# be removed when we convert LXC to use block devices.'
nl|'\n'
indent|'        '
name|'root_disk_bus'
op|'='
name|'disk_bus'
newline|'\n'
name|'root_device_type'
op|'='
string|"'disk'"
newline|'\n'
nl|'\n'
name|'root_info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'root_disk_bus'
op|','
nl|'\n'
name|'root_device_type'
op|')'
newline|'\n'
name|'mapping'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_info'
newline|'\n'
name|'mapping'
op|'['
string|"'disk'"
op|']'
op|'='
name|'root_info'
newline|'\n'
nl|'\n'
name|'return'
name|'mapping'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'rescue'
op|':'
newline|'\n'
indent|'        '
name|'rescue_info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'disk_bus'
op|')'
newline|'\n'
name|'mapping'
op|'['
string|"'disk.rescue'"
op|']'
op|'='
name|'rescue_info'
newline|'\n'
name|'mapping'
op|'['
string|"'root'"
op|']'
op|'='
name|'rescue_info'
newline|'\n'
nl|'\n'
name|'os_info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'disk_bus'
op|')'
newline|'\n'
name|'mapping'
op|'['
string|"'disk'"
op|']'
op|'='
name|'os_info'
newline|'\n'
nl|'\n'
name|'return'
name|'mapping'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'root_bdm'
op|'='
op|'('
name|'bdm'
name|'for'
name|'bdm'
name|'in'
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
name|'block_device_info'
op|')'
nl|'\n'
name|'if'
name|'bdm'
op|'.'
name|'get'
op|'('
string|"'boot_index'"
op|')'
op|'=='
number|'0'
op|')'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
comment|'# NOTE (ndipanov): This happens when we boot from image as'
nl|'\n'
comment|'# there is no driver represenation of local targeted images'
nl|'\n'
comment|'# and they will not be in block_device_info list.'
nl|'\n'
indent|'        '
name|'root_bdm'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'root_device_name'
op|'='
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'block_device_info'
op|')'
op|')'
newline|'\n'
name|'root_info'
op|'='
name|'get_root_info'
op|'('
name|'virt_type'
op|','
name|'image_meta'
op|','
name|'root_bdm'
op|','
nl|'\n'
name|'disk_bus'
op|','
name|'cdrom_bus'
op|','
name|'root_device_name'
op|')'
newline|'\n'
nl|'\n'
name|'mapping'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_info'
newline|'\n'
comment|'# NOTE (ndipanov): This implicitely relies on image->local BDMs not'
nl|'\n'
comment|'#                  being considered in the driver layer - so missing'
nl|'\n'
comment|'#                  bdm with boot_index 0 means - use image, unless it was'
nl|'\n'
comment|'#                  overriden. This can happen when using legacy syntax and'
nl|'\n'
comment|'#                  no root_device_name is set on the instance.'
nl|'\n'
name|'if'
name|'not'
name|'root_bdm'
name|'and'
name|'not'
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
name|'root_info'
op|'['
string|"'dev'"
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'['
string|"'disk'"
op|']'
op|'='
name|'root_info'
newline|'\n'
nl|'\n'
dedent|''
name|'default_eph'
op|'='
name|'has_default_ephemeral'
op|'('
name|'instance'
op|','
name|'disk_bus'
op|','
name|'block_device_info'
op|','
nl|'\n'
name|'mapping'
op|')'
newline|'\n'
name|'if'
name|'default_eph'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'['
string|"'disk.local'"
op|']'
op|'='
name|'default_eph'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'idx'
op|','
name|'eph'
name|'in'
name|'enumerate'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'eph_info'
op|'='
name|'get_info_from_bdm'
op|'('
nl|'\n'
name|'virt_type'
op|','
name|'eph'
op|','
name|'mapping'
op|','
name|'disk_bus'
op|','
nl|'\n'
name|'assigned_devices'
op|'='
name|'pre_assigned_device_names'
op|')'
newline|'\n'
name|'mapping'
op|'['
name|'get_eph_disk'
op|'('
name|'idx'
op|')'
op|']'
op|'='
name|'eph_info'
newline|'\n'
name|'update_bdm'
op|'('
name|'eph'
op|','
name|'eph_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'swap'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
newline|'\n'
name|'if'
name|'swap'
name|'and'
name|'swap'
op|'.'
name|'get'
op|'('
string|"'swap_size'"
op|','
number|'0'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'swap_info'
op|'='
name|'get_info_from_bdm'
op|'('
name|'virt_type'
op|','
name|'swap'
op|','
name|'mapping'
op|','
name|'disk_bus'
op|')'
newline|'\n'
name|'mapping'
op|'['
string|"'disk.swap'"
op|']'
op|'='
name|'swap_info'
newline|'\n'
name|'update_bdm'
op|'('
name|'swap'
op|','
name|'swap_info'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'inst_type'
op|'['
string|"'swap'"
op|']'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'swap_info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'disk_bus'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
name|'swap_info'
op|'['
string|"'dev'"
op|']'
op|','
nl|'\n'
name|'block_device_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mapping'
op|'['
string|"'disk.swap'"
op|']'
op|'='
name|'swap_info'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'block_device_mapping'
op|'='
name|'driver'
op|'.'
name|'block_device_info_get_mapping'
op|'('
nl|'\n'
name|'block_device_info'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vol'
name|'in'
name|'block_device_mapping'
op|':'
newline|'\n'
indent|'        '
name|'vol_info'
op|'='
name|'get_info_from_bdm'
op|'('
nl|'\n'
name|'virt_type'
op|','
name|'vol'
op|','
name|'mapping'
op|','
nl|'\n'
name|'assigned_devices'
op|'='
name|'pre_assigned_device_names'
op|')'
newline|'\n'
name|'mapping'
op|'['
name|'block_device'
op|'.'
name|'prepend_dev'
op|'('
name|'vol_info'
op|'['
string|"'dev'"
op|']'
op|')'
op|']'
op|'='
name|'vol_info'
newline|'\n'
name|'update_bdm'
op|'('
name|'vol'
op|','
name|'vol_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'configdrive'
op|'.'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'device_type'
op|'='
name|'get_config_drive_type'
op|'('
op|')'
newline|'\n'
name|'disk_bus'
op|'='
name|'get_disk_bus_for_device_type'
op|'('
name|'virt_type'
op|','
nl|'\n'
name|'image_meta'
op|','
nl|'\n'
name|'device_type'
op|')'
newline|'\n'
name|'config_info'
op|'='
name|'get_next_disk_info'
op|'('
name|'mapping'
op|','
nl|'\n'
name|'disk_bus'
op|','
nl|'\n'
name|'device_type'
op|','
nl|'\n'
name|'last_device'
op|'='
name|'True'
op|')'
newline|'\n'
name|'mapping'
op|'['
string|"'disk.config'"
op|']'
op|'='
name|'config_info'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_info
dedent|''
name|'def'
name|'get_disk_info'
op|'('
name|'virt_type'
op|','
name|'instance'
op|','
name|'block_device_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'None'
op|','
name|'rescue'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Determine guest disk mapping info.\n\n       This is a wrapper around get_disk_mapping, which\n       also returns the chosen disk_bus and cdrom_bus.\n       The returned data is in a dict\n\n            - disk_bus: the bus for harddisks\n            - cdrom_bus: the bus for CDROMs\n            - mapping: the disk mapping\n\n       Returns the disk mapping disk.\n    """'
newline|'\n'
nl|'\n'
name|'disk_bus'
op|'='
name|'get_disk_bus_for_device_type'
op|'('
name|'virt_type'
op|','
name|'image_meta'
op|','
string|'"disk"'
op|')'
newline|'\n'
name|'cdrom_bus'
op|'='
name|'get_disk_bus_for_device_type'
op|'('
name|'virt_type'
op|','
name|'image_meta'
op|','
string|'"cdrom"'
op|')'
newline|'\n'
name|'mapping'
op|'='
name|'get_disk_mapping'
op|'('
name|'virt_type'
op|','
name|'instance'
op|','
nl|'\n'
name|'disk_bus'
op|','
name|'cdrom_bus'
op|','
nl|'\n'
name|'block_device_info'
op|','
nl|'\n'
name|'image_meta'
op|','
name|'rescue'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'{'
string|"'disk_bus'"
op|':'
name|'disk_bus'
op|','
nl|'\n'
string|"'cdrom_bus'"
op|':'
name|'cdrom_bus'
op|','
nl|'\n'
string|"'mapping'"
op|':'
name|'mapping'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
