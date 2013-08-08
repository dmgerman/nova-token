begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2012 Red Hat, Inc'
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
DECL|class|GuestFS
name|'class'
name|'GuestFS'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
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
name|'drives'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'running'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'closed'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'mounts'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'auginit'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'attach_method'
op|'='
string|"'libvirt'"
newline|'\n'
name|'self'
op|'.'
name|'root_mounted'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|launch
dedent|''
name|'def'
name|'launch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'running'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|shutdown
dedent|''
name|'def'
name|'shutdown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'running'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'mounts'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'drives'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'closed'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|add_drive_opts
dedent|''
name|'def'
name|'add_drive_opts'
op|'('
name|'self'
op|','
name|'file'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'drives'
op|'.'
name|'append'
op|'('
op|'('
name|'file'
op|','
name|'kwargs'
op|'['
string|"'format'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_attach_method
dedent|''
name|'def'
name|'get_attach_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'attach_method'
newline|'\n'
nl|'\n'
DECL|member|set_attach_method
dedent|''
name|'def'
name|'set_attach_method'
op|'('
name|'self'
op|','
name|'attach_method'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'attach_method'
op|'='
name|'attach_method'
newline|'\n'
nl|'\n'
DECL|member|inspect_os
dedent|''
name|'def'
name|'inspect_os'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|'"/dev/guestvgf/lv_root"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|inspect_get_mountpoints
dedent|''
name|'def'
name|'inspect_get_mountpoints'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|'['
string|'"/home"'
op|','
string|'"/dev/mapper/guestvgf-lv_home"'
op|']'
op|','
nl|'\n'
op|'['
string|'"/"'
op|','
string|'"/dev/mapper/guestvgf-lv_root"'
op|']'
op|','
nl|'\n'
op|'['
string|'"/boot"'
op|','
string|'"/dev/vda1"'
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|member|mount_options
dedent|''
name|'def'
name|'mount_options'
op|'('
name|'self'
op|','
name|'options'
op|','
name|'device'
op|','
name|'mntpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'mntpoint'
op|'=='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'root_mounted'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'root_mounted'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'RuntimeError'
op|'('
nl|'\n'
string|'"mount: %s: No such file or directory"'
op|'%'
name|'mntpoint'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'mounts'
op|'.'
name|'append'
op|'('
op|'('
name|'options'
op|','
name|'device'
op|','
name|'mntpoint'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|mkdir_p
dedent|''
name|'def'
name|'mkdir_p'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"isdir"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"gid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"uid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"mode"'
op|':'
number|'0o700'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|read_file
dedent|''
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
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"isdir"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"content"'
op|':'
string|'"Hello World"'
op|','
nl|'\n'
string|'"gid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"uid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"mode"'
op|':'
number|'0o700'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
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
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"isdir"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"content"'
op|':'
string|'"Hello World"'
op|','
nl|'\n'
string|'"gid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"uid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"mode"'
op|':'
number|'0o700'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|'='
name|'content'
newline|'\n'
nl|'\n'
DECL|member|write_append
dedent|''
name|'def'
name|'write_append'
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
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
nl|'\n'
string|'"isdir"'
op|':'
name|'False'
op|','
nl|'\n'
string|'"content"'
op|':'
string|'"Hello World"'
op|','
nl|'\n'
string|'"gid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"uid"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"mode"'
op|':'
number|'0o700'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|'='
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|'+'
name|'content'
newline|'\n'
nl|'\n'
DECL|member|stat
dedent|''
name|'def'
name|'stat'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"mode"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|chown
dedent|''
name|'def'
name|'chown'
op|'('
name|'self'
op|','
name|'uid'
op|','
name|'gid'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'uid'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"uid"'
op|']'
op|'='
name|'uid'
newline|'\n'
dedent|''
name|'if'
name|'gid'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"gid"'
op|']'
op|'='
name|'gid'
newline|'\n'
nl|'\n'
DECL|member|chmod
dedent|''
dedent|''
name|'def'
name|'chmod'
op|'('
name|'self'
op|','
name|'mode'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
name|'not'
name|'in'
name|'self'
op|'.'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"mode"'
op|']'
op|'='
name|'mode'
newline|'\n'
nl|'\n'
DECL|member|aug_init
dedent|''
name|'def'
name|'aug_init'
op|'('
name|'self'
op|','
name|'root'
op|','
name|'flags'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auginit'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|aug_close
dedent|''
name|'def'
name|'aug_close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auginit'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|aug_get
dedent|''
name|'def'
name|'aug_get'
op|'('
name|'self'
op|','
name|'cfgpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'auginit'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
string|'"Augeus not initialized"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'cfgpath'
op|'=='
string|'"/files/etc/passwd/root/uid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'elif'
name|'cfgpath'
op|'=='
string|'"/files/etc/passwd/fred/uid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'105'
newline|'\n'
dedent|''
name|'elif'
name|'cfgpath'
op|'=='
string|'"/files/etc/passwd/joe/uid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'110'
newline|'\n'
dedent|''
name|'elif'
name|'cfgpath'
op|'=='
string|'"/files/etc/group/root/gid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'elif'
name|'cfgpath'
op|'=='
string|'"/files/etc/group/users/gid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'500'
newline|'\n'
dedent|''
name|'elif'
name|'cfgpath'
op|'=='
string|'"/files/etc/group/admins/gid"'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'600'
newline|'\n'
dedent|''
name|'raise'
name|'RuntimeError'
op|'('
string|'"Unknown path %s"'
op|','
name|'cfgpath'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
