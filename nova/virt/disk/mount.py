begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Red Hat, Inc.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
string|'"""Support for mounting virtual image files"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.compute.disk'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Mount
name|'class'
name|'Mount'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Standard mounting operations, that can be overridden by subclasses.\n\n    The basic device operations provided are get, map and mount,\n    to be called in that order.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'mount_dir'
op|','
name|'partition'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Input'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'image'
op|'='
name|'image'
newline|'\n'
name|'self'
op|'.'
name|'partition'
op|'='
name|'partition'
newline|'\n'
name|'self'
op|'.'
name|'mount_dir'
op|'='
name|'mount_dir'
newline|'\n'
nl|'\n'
comment|'# Output'
nl|'\n'
name|'self'
op|'.'
name|'error'
op|'='
string|'""'
newline|'\n'
nl|'\n'
comment|'# Internal'
nl|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'self'
op|'.'
name|'mapped'
op|'='
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_dev
dedent|''
name|'def'
name|'get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make the image available as a block device in the file system."""'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|unget_dev
dedent|''
name|'def'
name|'unget_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Release the block device from the file system namespace."""'
newline|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|map_dev
dedent|''
name|'def'
name|'map_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Map partitions of the device to the file system namespace."""'
newline|'\n'
name|'assert'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'partition'
op|':'
newline|'\n'
indent|'            '
name|'map_path'
op|'='
string|"'/dev/mapper/%sp%s'"
op|'%'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'partition'
op|')'
newline|'\n'
name|'assert'
op|'('
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'map_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note kpartx can output warnings to stderr and succeed'
nl|'\n'
comment|'# Also it can output failures to stderr and "succeed"'
nl|'\n'
comment|'# So we just go on the existence of the mapped device'
nl|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'kpartx'"
op|','
string|"'-a'"
op|','
name|'self'
op|'.'
name|'device'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'discard_warnings'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note kpartx does nothing when presented with a raw image,'
nl|'\n'
comment|'# so given we only use it when we expect a partitioned image, fail'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'map_path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'err'
op|':'
newline|'\n'
indent|'                    '
name|'err'
op|'='
name|'_'
op|'('
string|"'no partitions found'"
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'Failed to map partitions: %s'"
op|')'
op|'%'
name|'err'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'map_path'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'self'
op|'.'
name|'device'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'mapped'
newline|'\n'
nl|'\n'
DECL|member|unmap_dev
dedent|''
name|'def'
name|'unmap_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove partitions of the device from the file system namespace."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'mapped'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'partition'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'kpartx'"
op|','
string|"'-d'"
op|','
name|'self'
op|'.'
name|'device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mapped'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|mnt_dev
dedent|''
name|'def'
name|'mnt_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mount the device into the file system."""'
newline|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'mount'"
op|','
name|'self'
op|'.'
name|'mapped_device'
op|','
name|'self'
op|'.'
name|'mount_dir'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
op|'%'
name|'err'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mounted'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|unmnt_dev
dedent|''
name|'def'
name|'unmnt_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unmount the device from the file system."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'mounted'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'self'
op|'.'
name|'mapped_device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|do_mount
dedent|''
name|'def'
name|'do_mount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the get, map and mnt operations."""'
newline|'\n'
name|'status'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
name|'self'
op|'.'
name|'get_dev'
op|'('
op|')'
name|'and'
name|'self'
op|'.'
name|'map_dev'
op|'('
op|')'
name|'and'
name|'self'
op|'.'
name|'mnt_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'status'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'do_umount'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|do_umount
dedent|''
name|'def'
name|'do_umount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the unmnt, unmap and unget operations."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'mounted'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unmnt_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'mapped'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unmap_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'linked'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
