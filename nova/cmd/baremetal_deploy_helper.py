begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Starter script for Bare-Metal Deployment Service."""'
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'threading'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'cgi'
newline|'\n'
name|'import'
name|'Queue'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'stat'
newline|'\n'
name|'from'
name|'wsgiref'
name|'import'
name|'simple_server'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'units'
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
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'api'
name|'as'
name|'disk'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|QUEUE
name|'QUEUE'
op|'='
name|'Queue'
op|'.'
name|'Queue'
op|'('
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
DECL|class|BareMetalDeployException
name|'class'
name|'BareMetalDeployException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# All functions are called from deploy() directly or indirectly.'
nl|'\n'
comment|'# They are split for stub-out.'
nl|'\n'
nl|'\n'
DECL|function|discovery
dedent|''
name|'def'
name|'discovery'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Do iSCSI discovery on portal."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'iscsiadm'"
op|','
nl|'\n'
string|"'-m'"
op|','
string|"'discovery'"
op|','
nl|'\n'
string|"'-t'"
op|','
string|"'st'"
op|','
nl|'\n'
string|"'-p'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|login_iscsi
dedent|''
name|'def'
name|'login_iscsi'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|','
name|'target_iqn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Login to an iSCSI target."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'iscsiadm'"
op|','
nl|'\n'
string|"'-m'"
op|','
string|"'node'"
op|','
nl|'\n'
string|"'-p'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|')'
op|','
nl|'\n'
string|"'-T'"
op|','
name|'target_iqn'
op|','
nl|'\n'
string|"'--login'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
comment|'# Ensure the login complete'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'3'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|logout_iscsi
dedent|''
name|'def'
name|'logout_iscsi'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|','
name|'target_iqn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Logout from an iSCSI target."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'iscsiadm'"
op|','
nl|'\n'
string|"'-m'"
op|','
string|"'node'"
op|','
nl|'\n'
string|"'-p'"
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'portal_address'
op|','
name|'portal_port'
op|')'
op|','
nl|'\n'
string|"'-T'"
op|','
name|'target_iqn'
op|','
nl|'\n'
string|"'--logout'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_partitions
dedent|''
name|'def'
name|'make_partitions'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create partitions for root, ephemeral and swap on a disk device."""'
newline|'\n'
comment|'# Lead in with 1MB to allow room for the partition table itself, otherwise'
nl|'\n'
comment|"# the way sfdisk adjusts doesn't shift the partition up to compensate, and"
nl|'\n'
comment|'# we lose the space.'
nl|'\n'
comment|'# http://bazaar.launchpad.net/~ubuntu-branches/ubuntu/raring/util-linux/'
nl|'\n'
comment|'# raring/view/head:/fdisk/sfdisk.c#L1940'
nl|'\n'
name|'if'
name|'ephemeral_mb'
op|':'
newline|'\n'
indent|'        '
name|'stdin_command'
op|'='
op|'('
string|"'1,%d,83;\\n,%d,82;\\n,%d,83;\\n0,0;\\n'"
op|'%'
nl|'\n'
op|'('
name|'ephemeral_mb'
op|','
name|'swap_mb'
op|','
name|'root_mb'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'stdin_command'
op|'='
op|'('
string|"'1,%d,83;\\n,%d,82;\\n0,0;\\n0,0;\\n'"
op|'%'
nl|'\n'
op|'('
name|'root_mb'
op|','
name|'swap_mb'
op|')'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sfdisk'"
op|','
string|"'-uM'"
op|','
name|'dev'
op|','
name|'process_input'
op|'='
name|'stdin_command'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'3'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
comment|'# avoid "device is busy"'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'3'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_block_device
dedent|''
name|'def'
name|'is_block_device'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check whether a device is block or not."""'
newline|'\n'
name|'s'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'return'
name|'stat'
op|'.'
name|'S_ISBLK'
op|'('
name|'s'
op|'.'
name|'st_mode'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dd
dedent|''
name|'def'
name|'dd'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Execute dd from src to dst."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd'"
op|','
nl|'\n'
string|"'if=%s'"
op|'%'
name|'src'
op|','
nl|'\n'
string|"'of=%s'"
op|'%'
name|'dst'
op|','
nl|'\n'
string|"'bs=1M'"
op|','
nl|'\n'
string|"'oflag=direct'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkswap
dedent|''
name|'def'
name|'mkswap'
op|'('
name|'dev'
op|','
name|'label'
op|'='
string|"'swap1'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Execute mkswap on a device."""'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkswap'"
op|','
nl|'\n'
string|"'-L'"
op|','
name|'label'
op|','
nl|'\n'
name|'dev'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkfs_ephemeral
dedent|''
name|'def'
name|'mkfs_ephemeral'
op|'('
name|'dev'
op|','
name|'label'
op|'='
string|'"ephemeral0"'
op|')'
op|':'
newline|'\n'
comment|'#TODO(jogo) support non-default mkfs options as well'
nl|'\n'
indent|'    '
name|'disk'
op|'.'
name|'mkfs'
op|'('
string|'"default"'
op|','
name|'label'
op|','
name|'dev'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|block_uuid
dedent|''
name|'def'
name|'block_uuid'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get UUID of a block device."""'
newline|'\n'
name|'out'
op|','
name|'_'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'blkid'"
op|','
string|"'-s'"
op|','
string|"'UUID'"
op|','
string|"'-o'"
op|','
string|"'value'"
op|','
name|'dev'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'return'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|switch_pxe_config
dedent|''
name|'def'
name|'switch_pxe_config'
op|'('
name|'path'
op|','
name|'root_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Switch a pxe config from deployment mode to service mode."""'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'lines'
op|'='
name|'f'
op|'.'
name|'readlines'
op|'('
op|')'
newline|'\n'
dedent|''
name|'root'
op|'='
string|"'UUID=%s'"
op|'%'
name|'root_uuid'
newline|'\n'
name|'rre'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r'\\$\\{ROOT\\}'"
op|')'
newline|'\n'
name|'dre'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^default .*$'"
op|')'
newline|'\n'
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
indent|'        '
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'rre'
op|'.'
name|'sub'
op|'('
name|'root'
op|','
name|'line'
op|')'
newline|'\n'
name|'line'
op|'='
name|'dre'
op|'.'
name|'sub'
op|'('
string|"'default boot'"
op|','
name|'line'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
dedent|''
dedent|''
name|'def'
name|'notify'
op|'('
name|'address'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Notify a node that it becomes ready to reboot."""'
newline|'\n'
name|'s'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_STREAM'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'.'
name|'connect'
op|'('
op|'('
name|'address'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
name|'s'
op|'.'
name|'send'
op|'('
string|"'done'"
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dev
dedent|''
dedent|''
name|'def'
name|'get_dev'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a device path for given parameters."""'
newline|'\n'
name|'dev'
op|'='
string|'"/dev/disk/by-path/ip-%s:%s-iscsi-%s-lun-%s"'
op|'%'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|')'
newline|'\n'
name|'return'
name|'dev'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_mb
dedent|''
name|'def'
name|'get_image_mb'
op|'('
name|'image_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get size of an image in Megabyte."""'
newline|'\n'
name|'mb'
op|'='
name|'units'
op|'.'
name|'Mi'
newline|'\n'
name|'image_byte'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getsize'
op|'('
name|'image_path'
op|')'
newline|'\n'
comment|'# round up size to MB'
nl|'\n'
name|'image_mb'
op|'='
name|'int'
op|'('
op|'('
name|'image_byte'
op|'+'
name|'mb'
op|'-'
number|'1'
op|')'
op|'/'
name|'mb'
op|')'
newline|'\n'
name|'return'
name|'image_mb'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|work_on_disk
dedent|''
name|'def'
name|'work_on_disk'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|','
name|'image_path'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates partitions and write an image to the root partition.\n\n    :param preserve_ephemeral: If True, no filesystem is written to the\n        ephemeral block device, preserving whatever content it had (if the\n        partition table has not changed).\n    """'
newline|'\n'
DECL|function|raise_exception
name|'def'
name|'raise_exception'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'BareMetalDeployException'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'ephemeral_mb'
op|':'
newline|'\n'
indent|'        '
name|'ephemeral_part'
op|'='
string|'"%s-part1"'
op|'%'
name|'dev'
newline|'\n'
name|'swap_part'
op|'='
string|'"%s-part2"'
op|'%'
name|'dev'
newline|'\n'
name|'root_part'
op|'='
string|'"%s-part3"'
op|'%'
name|'dev'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'root_part'
op|'='
string|'"%s-part1"'
op|'%'
name|'dev'
newline|'\n'
name|'swap_part'
op|'='
string|'"%s-part2"'
op|'%'
name|'dev'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'is_block_device'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise_exception'
op|'('
name|'_'
op|'('
string|'"parent device \'%s\' not found"'
op|')'
op|'%'
name|'dev'
op|')'
newline|'\n'
dedent|''
name|'make_partitions'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'is_block_device'
op|'('
name|'root_part'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise_exception'
op|'('
name|'_'
op|'('
string|'"root device \'%s\' not found"'
op|')'
op|'%'
name|'root_part'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'is_block_device'
op|'('
name|'swap_part'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise_exception'
op|'('
name|'_'
op|'('
string|'"swap device \'%s\' not found"'
op|')'
op|'%'
name|'swap_part'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'ephemeral_mb'
name|'and'
name|'not'
name|'is_block_device'
op|'('
name|'ephemeral_part'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise_exception'
op|'('
name|'_'
op|'('
string|'"ephemeral device \'%s\' not found"'
op|')'
op|'%'
name|'ephemeral_part'
op|')'
newline|'\n'
dedent|''
name|'dd'
op|'('
name|'image_path'
op|','
name|'root_part'
op|')'
newline|'\n'
name|'mkswap'
op|'('
name|'swap_part'
op|')'
newline|'\n'
name|'if'
name|'ephemeral_mb'
name|'and'
name|'not'
name|'preserve_ephemeral'
op|':'
newline|'\n'
indent|'        '
name|'mkfs_ephemeral'
op|'('
name|'ephemeral_part'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'root_uuid'
op|'='
name|'block_uuid'
op|'('
name|'root_part'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Failed to detect root device UUID."'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'root_uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|deploy
dedent|''
name|'def'
name|'deploy'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|','
name|'image_path'
op|','
name|'pxe_config_path'
op|','
nl|'\n'
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|','
name|'preserve_ephemeral'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""All-in-one function to deploy a node.\n\n    :param preserve_ephemeral: If True, no filesystem is written to the\n        ephemeral block device, preserving whatever content it had (if the\n        partition table has not changed).\n    """'
newline|'\n'
name|'dev'
op|'='
name|'get_dev'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|')'
newline|'\n'
name|'image_mb'
op|'='
name|'get_image_mb'
op|'('
name|'image_path'
op|')'
newline|'\n'
name|'if'
name|'image_mb'
op|'>'
name|'root_mb'
op|':'
newline|'\n'
indent|'        '
name|'root_mb'
op|'='
name|'image_mb'
newline|'\n'
dedent|''
name|'discovery'
op|'('
name|'address'
op|','
name|'port'
op|')'
newline|'\n'
name|'login_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'root_uuid'
op|'='
name|'work_on_disk'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'ephemeral_mb'
op|','
nl|'\n'
name|'image_path'
op|','
name|'preserve_ephemeral'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Log output if there was a error'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Cmd     : %s"'
op|')'
op|','
name|'err'
op|'.'
name|'cmd'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"StdOut  : %r"'
op|')'
op|','
name|'err'
op|'.'
name|'stdout'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"StdErr  : %r"'
op|')'
op|','
name|'err'
op|'.'
name|'stderr'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'logout_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
dedent|''
name|'switch_pxe_config'
op|'('
name|'pxe_config_path'
op|','
name|'root_uuid'
op|')'
newline|'\n'
comment|'# Ensure the node started netcat on the port after POST the request.'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'3'
op|')'
newline|'\n'
name|'notify'
op|'('
name|'address'
op|','
number|'10000'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Worker
dedent|''
name|'class'
name|'Worker'
op|'('
name|'threading'
op|'.'
name|'Thread'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Thread that handles requests in queue."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Worker'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'setDaemon'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stop'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'queue_timeout'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|run
dedent|''
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'not'
name|'self'
op|'.'
name|'stop'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# Set timeout to check self.stop periodically'
nl|'\n'
indent|'                '
op|'('
name|'node_id'
op|','
name|'params'
op|')'
op|'='
name|'QUEUE'
op|'.'
name|'get'
op|'('
name|'block'
op|'='
name|'True'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'self'
op|'.'
name|'queue_timeout'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Queue'
op|'.'
name|'Empty'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Requests comes here from BareMetalDeploy.post()'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'start deployment for node %(node_id)s, '"
nl|'\n'
string|"'params %(params)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'node_id'"
op|':'
name|'node_id'
op|','
string|"'params'"
op|':'
name|'params'
op|'}'
op|')'
newline|'\n'
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'node_id'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'DEPLOYING'
op|'}'
op|')'
newline|'\n'
name|'deploy'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'deployment to node %s failed'"
op|')'
op|','
name|'node_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'node_id'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'DEPLOYFAIL'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'deployment to node %s done'"
op|')'
op|','
name|'node_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'context'
op|','
name|'node_id'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'DEPLOYDONE'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalDeploy
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'BareMetalDeploy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI server for bare-metal deployment."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'worker'
op|'='
name|'Worker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'method'
op|'='
name|'environ'
op|'['
string|"'REQUEST_METHOD'"
op|']'
newline|'\n'
name|'if'
name|'method'
op|'=='
string|"'POST'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'post'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'501 Not Implemented'"
op|','
nl|'\n'
op|'['
op|'('
string|"'Content-type'"
op|','
string|"'text/plain'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|"'Not Implemented'"
newline|'\n'
nl|'\n'
DECL|member|post
dedent|''
dedent|''
name|'def'
name|'post'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"post: environ=%s"'
op|')'
op|','
name|'environ'
op|')'
newline|'\n'
name|'inpt'
op|'='
name|'environ'
op|'['
string|"'wsgi.input'"
op|']'
newline|'\n'
name|'length'
op|'='
name|'int'
op|'('
name|'environ'
op|'.'
name|'get'
op|'('
string|"'CONTENT_LENGTH'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'x'
op|'='
name|'inpt'
op|'.'
name|'read'
op|'('
name|'length'
op|')'
newline|'\n'
name|'q'
op|'='
name|'dict'
op|'('
name|'cgi'
op|'.'
name|'parse_qsl'
op|'('
name|'x'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'node_id'
op|'='
name|'q'
op|'['
string|"'i'"
op|']'
newline|'\n'
name|'deploy_key'
op|'='
name|'q'
op|'['
string|"'k'"
op|']'
newline|'\n'
name|'address'
op|'='
name|'q'
op|'['
string|"'a'"
op|']'
newline|'\n'
name|'port'
op|'='
name|'q'
op|'.'
name|'get'
op|'('
string|"'p'"
op|','
string|"'3260'"
op|')'
newline|'\n'
name|'iqn'
op|'='
name|'q'
op|'['
string|"'n'"
op|']'
newline|'\n'
name|'lun'
op|'='
name|'q'
op|'.'
name|'get'
op|'('
string|"'l'"
op|','
string|"'1'"
op|')'
newline|'\n'
name|'err_msg'
op|'='
name|'q'
op|'.'
name|'get'
op|'('
string|"'e'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'400 Bad Request'"
op|','
op|'['
op|'('
string|"'Content-type'"
op|','
string|"'text/plain'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|'"parameter \'%s\' is not defined"'
op|'%'
name|'e'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'err_msg'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Deploy agent error message: %s'"
op|')'
op|','
name|'err_msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'d'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'context'
op|','
name|'node_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'d'
op|'['
string|"'deploy_key'"
op|']'
op|'!='
name|'deploy_key'
op|':'
newline|'\n'
indent|'            '
name|'start_response'
op|'('
string|"'400 Bad Request'"
op|','
op|'['
op|'('
string|"'Content-type'"
op|','
string|"'text/plain'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|"'key is not match'"
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'port'
op|','
nl|'\n'
string|"'iqn'"
op|':'
name|'iqn'
op|','
nl|'\n'
string|"'lun'"
op|':'
name|'lun'
op|','
nl|'\n'
string|"'image_path'"
op|':'
name|'d'
op|'['
string|"'image_path'"
op|']'
op|','
nl|'\n'
string|"'pxe_config_path'"
op|':'
name|'d'
op|'['
string|"'pxe_config_path'"
op|']'
op|','
nl|'\n'
string|"'root_mb'"
op|':'
name|'int'
op|'('
name|'d'
op|'['
string|"'root_mb'"
op|']'
op|')'
op|','
nl|'\n'
string|"'swap_mb'"
op|':'
name|'int'
op|'('
name|'d'
op|'['
string|"'swap_mb'"
op|']'
op|')'
op|','
nl|'\n'
string|"'ephemeral_mb'"
op|':'
name|'int'
op|'('
name|'d'
op|'['
string|"'ephemeral_mb'"
op|']'
op|')'
op|','
nl|'\n'
string|"'preserve_ephemeral'"
op|':'
name|'d'
op|'['
string|"'preserve_ephemeral'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
comment|'# Restart worker, if needed'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'isAlive'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'worker'
op|'='
name|'Worker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"request is queued: node %(node_id)s, params %(params)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'node_id'"
op|':'
name|'node_id'
op|','
string|"'params'"
op|':'
name|'params'
op|'}'
op|')'
newline|'\n'
name|'QUEUE'
op|'.'
name|'put'
op|'('
op|'('
name|'node_id'
op|','
name|'params'
op|')'
op|')'
newline|'\n'
comment|'# Requests go to Worker.run()'
nl|'\n'
name|'start_response'
op|'('
string|"'200 OK'"
op|','
op|'['
op|'('
string|"'Content-type'"
op|','
string|"'text/plain'"
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
name|'global'
name|'LOG'
newline|'\n'
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.baremetal.deploy_helper'"
op|')'
newline|'\n'
name|'app'
op|'='
name|'BareMetalDeploy'
op|'('
op|')'
newline|'\n'
name|'srv'
op|'='
name|'simple_server'
op|'.'
name|'make_server'
op|'('
string|"''"
op|','
number|'10000'
op|','
name|'app'
op|')'
newline|'\n'
name|'srv'
op|'.'
name|'serve_forever'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
