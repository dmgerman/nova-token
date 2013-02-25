begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'tpool'
newline|'\n'
name|'import'
name|'guestfs'
newline|'\n'
nl|'\n'
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
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
name|'import'
name|'api'
name|'as'
name|'vfs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'driver'
name|'as'
name|'libvirt_driver'
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
nl|'\n'
DECL|variable|guestfs
name|'guestfs'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VFSGuestFS
name|'class'
name|'VFSGuestFS'
op|'('
name|'vfs'
op|'.'
name|'VFS'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""\n    This class implements a VFS module that uses the libguestfs APIs\n    to access the disk image. The disk image is never mapped into\n    the host filesystem, thus avoiding any potential for symlink\n    attacks from the guest filesystem.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'imgfile'
op|','
name|'imgfmt'
op|'='
string|"'raw'"
op|','
name|'partition'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VFSGuestFS'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'imgfile'
op|','
name|'imgfmt'
op|','
name|'partition'
op|')'
newline|'\n'
nl|'\n'
name|'global'
name|'guestfs'
newline|'\n'
name|'if'
name|'guestfs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'guestfs'
op|'='
name|'__import__'
op|'('
string|"'guestfs'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|setup_os
dedent|''
name|'def'
name|'setup_os'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'partition'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setup_os_inspect'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setup_os_static'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_static
dedent|''
dedent|''
name|'def'
name|'setup_os_static'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mount guest OS image %(imgfile)s partition %(part)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'part'"
op|':'
name|'str'
op|'('
name|'self'
op|'.'
name|'partition'
op|')'
op|'}'
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
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
string|'"/dev/sda%d"'
op|'%'
name|'self'
op|'.'
name|'partition'
op|','
string|'"/"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
string|'"/dev/sda"'
op|','
string|'"/"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_inspect
dedent|''
dedent|''
name|'def'
name|'setup_os_inspect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Inspecting guest OS image %s"'
op|')'
op|','
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
name|'roots'
op|'='
name|'self'
op|'.'
name|'handle'
op|'.'
name|'inspect_os'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'roots'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"No operating system found in %s"'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'roots'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Multi-boot OS %(roots)s"'
op|')'
op|'%'
op|'{'
string|"'roots'"
op|':'
name|'str'
op|'('
name|'roots'
op|')'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Multi-boot operating system found in %s"'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'setup_os_root'
op|'('
name|'roots'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_root
dedent|''
name|'def'
name|'setup_os_root'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Inspecting guest OS root filesystem %s"'
op|')'
op|','
name|'root'
op|')'
newline|'\n'
name|'mounts'
op|'='
name|'self'
op|'.'
name|'handle'
op|'.'
name|'inspect_get_mountpoints'
op|'('
name|'root'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'mounts'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"No mount points found in %(root)s of %(imgfile)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'root'"
op|':'
name|'root'
op|','
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mounts'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'mount'
op|':'
name|'mount'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'for'
name|'mount'
name|'in'
name|'mounts'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mounting %(dev)s at %(dir)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'dev'"
op|':'
name|'mount'
op|'['
number|'1'
op|']'
op|','
string|"'dir'"
op|':'
name|'mount'
op|'['
number|'0'
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
name|'mount'
op|'['
number|'1'
op|']'
op|','
name|'mount'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Setting up appliance for %(imgfile)s %(imgfmt)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'imgfmt'"
op|':'
name|'self'
op|'.'
name|'imgfmt'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'='
name|'tpool'
op|'.'
name|'Proxy'
op|'('
name|'guestfs'
op|'.'
name|'GuestFS'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'add_drive_opts'
op|'('
name|'self'
op|'.'
name|'imgfile'
op|','
name|'format'
op|'='
name|'self'
op|'.'
name|'imgfmt'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'get_attach_method'
op|'('
op|')'
op|'=='
string|"'libvirt'"
op|':'
newline|'\n'
indent|'                '
name|'libvirt_url'
op|'='
string|"'libvirt:'"
op|'+'
name|'libvirt_driver'
op|'.'
name|'LibvirtDriver'
op|'.'
name|'uri'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'set_attach_method'
op|'('
name|'libvirt_url'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'handle'
op|'.'
name|'launch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'setup_os'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_init'
op|'('
string|'"/"'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|','
name|'e'
op|':'
newline|'\n'
comment|'# dereference object and implicitly close()'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Error mounting %(imgfile)s with libguestfs (%(e)s)"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Tearing down appliance"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to close augeas %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# Older libguestfs versions haven't an explicit shutdown"
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to shutdown appliance %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# Older libguestfs versions haven't an explicit close"
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to close guest handle %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# dereference object and implicitly close()'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_canonicalize_path
name|'def'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
op|'['
number|'0'
op|']'
op|'!='
string|"'/'"
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'/'"
op|'+'
name|'path'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|make_path
dedent|''
name|'def'
name|'make_path'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Make directory path=%(path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mkdir_p'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|append_file
dedent|''
name|'def'
name|'append_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Append file path=%(path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'write_append'
op|'('
name|'path'
op|','
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|replace_file
dedent|''
name|'def'
name|'replace_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Replace file path=%(path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'write'
op|'('
name|'path'
op|','
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|read_file
dedent|''
name|'def'
name|'read_file'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Read file path=%(path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'read_file'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|has_file
dedent|''
name|'def'
name|'has_file'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Has file path=%(path)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'stat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|set_permissions
dedent|''
dedent|''
name|'def'
name|'set_permissions'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Set permissions path=%(path)s mode=%(mode)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'chmod'
op|'('
name|'mode'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_ownership
dedent|''
name|'def'
name|'set_ownership'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'user'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Set ownership path=%(path)s "'
nl|'\n'
string|'"user=%(user)s group=%(group)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'uid'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'gid'
op|'='
op|'-'
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'user'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'uid'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_get'
op|'('
nl|'\n'
string|'"/files/etc/passwd/"'
op|'+'
name|'user'
op|'+'
string|'"/uid"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'group'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'gid'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_get'
op|'('
nl|'\n'
string|'"/files/etc/group/"'
op|'+'
name|'group'
op|'+'
string|'"/gid"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"chown uid=%(uid)d gid=%(gid)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'chown'
op|'('
name|'uid'
op|','
name|'gid'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
