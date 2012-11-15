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
string|'"""Support for mounting images with qemu-nbd"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
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
op|'.'
name|'disk'
op|'.'
name|'mount'
name|'import'
name|'api'
newline|'\n'
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
nl|'\n'
DECL|variable|nbd_opts
name|'nbd_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'timeout_nbd'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'time to wait for a NBD device coming up'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_nbd_devices'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'16'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'maximum number of possible nbd devices'"
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
name|'nbd_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NbdMount
name|'class'
name|'NbdMount'
op|'('
name|'api'
op|'.'
name|'Mount'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""qemu-nbd support disk images."""'
newline|'\n'
DECL|variable|mode
name|'mode'
op|'='
string|"'nbd'"
newline|'\n'
nl|'\n'
comment|'# NOTE(padraig): There are three issues with this nbd device handling'
nl|'\n'
comment|'#  1. max_nbd_devices should be inferred (#861504)'
nl|'\n'
comment|'#  2. We assume nothing else on the system uses nbd devices'
nl|'\n'
comment|'#  3. Multiple workers on a system can race against each other'
nl|'\n'
comment|'# A patch has been proposed in Nov 2011, to add add a -f option to'
nl|'\n'
comment|'# qemu-nbd, akin to losetup -f. One could test for this by running qemu-nbd'
nl|'\n'
comment|'# with just the -f option, where it will fail if not supported, or if there'
nl|'\n'
comment|'# are no free devices. Note that patch currently hardcodes 16 devices.'
nl|'\n'
comment|'# We might be able to alleviate problem 2. by scanning /proc/partitions'
nl|'\n'
comment|'# like the aformentioned patch does.'
nl|'\n'
DECL|variable|_DEVICES
name|'_DEVICES'
op|'='
op|'['
string|"'/dev/nbd%s'"
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'CONF'
op|'.'
name|'max_nbd_devices'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_allocate_nbd
name|'def'
name|'_allocate_nbd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|'"/sys/block/nbd0"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'nbd unavailable: module not loaded'"
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_DEVICES'
op|':'
newline|'\n'
comment|'# really want to log this info, not raise'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'No free nbd devices'"
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'self'
op|'.'
name|'_DEVICES'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|'"/sys/block/%s/pid"'
op|'%'
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'device'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'device'
newline|'\n'
nl|'\n'
DECL|member|_free_nbd
dedent|''
name|'def'
name|'_free_nbd'
op|'('
name|'self'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
comment|'# The device could already be present if unget_dev'
nl|'\n'
comment|'# is called right after a nova restart'
nl|'\n'
comment|'# (when destroying an LXC container for example).'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'device'
name|'in'
name|'self'
op|'.'
name|'_DEVICES'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_DEVICES'
op|'.'
name|'append'
op|'('
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dev
dedent|''
dedent|''
name|'def'
name|'get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'device'
op|'='
name|'self'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Get nbd device %(dev)s for %(imgfile)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'dev'"
op|':'
name|'device'
op|','
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'image'
op|'}'
op|')'
newline|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'qemu-nbd'"
op|','
string|"'-c'"
op|','
name|'device'
op|','
name|'self'
op|'.'
name|'image'
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
string|"'qemu-nbd error: %s'"
op|')'
op|'%'
name|'err'
newline|'\n'
name|'self'
op|'.'
name|'_free_nbd'
op|'('
name|'device'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): this forks into another process, so give it a chance'
nl|'\n'
comment|'#             to set up before continuing'
nl|'\n'
dedent|''
name|'for'
name|'_i'
name|'in'
name|'range'
op|'('
name|'CONF'
op|'.'
name|'timeout_nbd'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|'"/sys/block/%s/pid"'
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'device'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'device'
op|'='
name|'device'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'nbd device %s did not show up'"
op|')'
op|'%'
name|'device'
newline|'\n'
name|'self'
op|'.'
name|'_free_nbd'
op|'('
name|'device'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
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
name|'if'
name|'not'
name|'self'
op|'.'
name|'linked'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Release nbd device %s"'
op|')'
op|','
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'qemu-nbd'"
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
name|'self'
op|'.'
name|'_free_nbd'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
