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
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
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
name|'excutils'
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
name|'loop'
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
name|'nbd'
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
nl|'\n'
DECL|class|VFSLocalFS
name|'class'
name|'VFSLocalFS'
op|'('
name|'vfs'
op|'.'
name|'VFS'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""\n    os.path.join() with safety check for injected file paths.\n\n    Join the supplied path components and make sure that the\n    resulting path we are injecting into is within the\n    mounted guest fs.  Trying to be clever and specifying a\n    path with \'..\' in it will hit this safeguard.\n    """'
newline|'\n'
DECL|member|_canonical_path
name|'def'
name|'_canonical_path'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'canonpath'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'imgdir'
op|','
name|'path'
op|'.'
name|'lstrip'
op|'('
string|'"/"'
op|')'
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'canonpath'
op|'.'
name|'startswith'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'realpath'
op|'('
name|'self'
op|'.'
name|'imgdir'
op|')'
op|'+'
string|"'/'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|"'File path %s not valid'"
op|')'
op|'%'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'canonpath'
newline|'\n'
nl|'\n'
dedent|''
string|'"""\n    This class implements a VFS module that is mapped to a virtual\n    root directory present on the host filesystem. This implementation\n    uses the nova.virt.disk.mount.Mount API to make virtual disk\n    images visible in the host filesystem. If the disk format is\n    raw, it will use the loopback mount impl, otherwise it will\n    use the qemu-nbd impl.\n    """'
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
string|'"raw"'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'imgdir'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VFSLocalFS'
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
name|'self'
op|'.'
name|'imgdir'
op|'='
name|'imgdir'
newline|'\n'
name|'self'
op|'.'
name|'mount'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|setup
dedent|''
name|'def'
name|'setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'imgdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|'"openstack-vfs-localfs"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'imgfmt'
op|'=='
string|'"raw"'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using LoopMount"'
op|')'
op|')'
newline|'\n'
name|'mount'
op|'='
name|'loop'
op|'.'
name|'LoopMount'
op|'('
name|'self'
op|'.'
name|'imgfile'
op|','
nl|'\n'
name|'self'
op|'.'
name|'imgdir'
op|','
nl|'\n'
name|'self'
op|'.'
name|'partition'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using NbdMount"'
op|')'
op|')'
newline|'\n'
name|'mount'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'self'
op|'.'
name|'imgfile'
op|','
nl|'\n'
name|'self'
op|'.'
name|'imgdir'
op|','
nl|'\n'
name|'self'
op|'.'
name|'partition'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'mount'
op|'.'
name|'do_mount'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'mount'
op|'.'
name|'error'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mount'
op|'='
name|'mount'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to mount image %(ex)s)"'
op|')'
op|','
op|'{'
string|"'ex'"
op|':'
name|'str'
op|'('
name|'e'
op|')'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'mount'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mount'
op|'.'
name|'do_teardown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to unmount %(imgdir)s: %(ex)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'imgdir'"
op|':'
name|'self'
op|'.'
name|'imgdir'
op|','
string|"'ex'"
op|':'
name|'str'
op|'('
name|'e'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'imgdir'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'self'
op|'.'
name|'imgdir'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to remove %(imgdir)s: %(ex)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'imgdir'"
op|':'
name|'self'
op|'.'
name|'imgdir'
op|','
string|"'ex'"
op|':'
name|'str'
op|'('
name|'e'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'imgdir'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mount'
op|'='
name|'None'
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
string|'"Make directory path=%s"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'canonpath'
op|','
name|'run_as_root'
op|'='
name|'True'
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
string|'"Append file path=%s"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'['
string|'"-a"'
op|','
name|'canonpath'
op|']'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'process_input'
op|'='
name|'content'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
string|'"Replace file path=%s"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
name|'args'
op|'='
op|'['
name|'canonpath'
op|']'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'process_input'
op|'='
name|'content'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
string|'"Read file path=%s"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'utils'
op|'.'
name|'read_file_as_root'
op|'('
name|'canonpath'
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
string|'"Has file path=%s"'
op|')'
op|','
name|'path'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'exists'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'readlink'"
op|','
string|"'-e'"
op|','
nl|'\n'
name|'canonpath'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'exists'
newline|'\n'
nl|'\n'
DECL|member|set_permissions
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
string|'"Set permissions path=%(path)s mode=%(mode)o"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'mode'"
op|':'
name|'mode'
op|'}'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chmod'"
op|','
string|'"%o"'
op|'%'
name|'mode'
op|','
name|'canonpath'
op|','
name|'run_as_root'
op|'='
name|'True'
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
string|'"Set permissions path=%(path)s "'
nl|'\n'
string|'"user=%(user)s group=%(group)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'user'"
op|':'
name|'user'
op|','
string|"'group'"
op|':'
name|'group'
op|'}'
op|')'
newline|'\n'
name|'canonpath'
op|'='
name|'self'
op|'.'
name|'_canonical_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'owner'
op|'='
name|'None'
newline|'\n'
name|'cmd'
op|'='
string|'"chown"'
newline|'\n'
name|'if'
name|'group'
name|'is'
name|'not'
name|'None'
name|'and'
name|'user'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'owner'
op|'='
name|'user'
op|'+'
string|'":"'
op|'+'
name|'group'
newline|'\n'
dedent|''
name|'elif'
name|'user'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'owner'
op|'='
name|'user'
newline|'\n'
dedent|''
name|'elif'
name|'group'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'owner'
op|'='
name|'group'
newline|'\n'
name|'cmd'
op|'='
string|'"chgrp"'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'owner'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd'
op|','
name|'owner'
op|','
name|'canonpath'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
