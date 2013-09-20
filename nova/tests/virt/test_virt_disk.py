begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright (C) 2012 Red Hat, Inc.'
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
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fakeguestfs'
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
name|'diskapi'
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
name|'guestfs'
name|'as'
name|'vfsguestfs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtDiskTest
name|'class'
name|'VirtDiskTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VirtDiskTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'modules'
op|'['
string|"'guestfs'"
op|']'
op|'='
name|'fakeguestfs'
newline|'\n'
name|'vfsguestfs'
op|'.'
name|'guestfs'
op|'='
name|'fakeguestfs'
newline|'\n'
nl|'\n'
DECL|member|test_inject_data
dedent|''
name|'def'
name|'test_inject_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'diskapi'
op|'.'
name|'inject_data'
op|'('
string|'"/some/file"'
op|','
name|'use_cow'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'diskapi'
op|'.'
name|'inject_data'
op|'('
string|'"/some/file"'
op|','
nl|'\n'
name|'mandatory'
op|'='
op|'('
string|"'files'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'diskapi'
op|'.'
name|'inject_data'
op|'('
string|'"/some/file"'
op|','
name|'key'
op|'='
string|'"mysshkey"'
op|','
nl|'\n'
name|'mandatory'
op|'='
op|'('
string|"'key'"
op|','
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'os_name'
op|'='
name|'os'
op|'.'
name|'name'
newline|'\n'
name|'os'
op|'.'
name|'name'
op|'='
string|"'nt'"
comment|'# Cause password injection to fail'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'diskapi'
op|'.'
name|'inject_data'
op|','
nl|'\n'
string|'"/some/file"'
op|','
name|'admin_password'
op|'='
string|'"p"'
op|','
nl|'\n'
name|'mandatory'
op|'='
op|'('
string|"'admin_password'"
op|','
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'diskapi'
op|'.'
name|'inject_data'
op|'('
string|'"/some/file"'
op|','
name|'admin_password'
op|'='
string|'"p"'
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'name'
op|'='
name|'os_name'
newline|'\n'
nl|'\n'
DECL|member|test_inject_data_key
dedent|''
name|'def'
name|'test_inject_data_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'diskapi'
op|'.'
name|'_inject_key_into_fs'
op|'('
string|'"mysshkey"'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/root/.ssh"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/root/.ssh"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'True'
op|','
string|"'gid'"
op|':'
number|'0'
op|','
string|"'uid'"
op|':'
number|'0'
op|','
string|"'mode'"
op|':'
number|'0o700'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/root/.ssh/authorized_keys"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/root/.ssh/authorized_keys"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'content'"
op|':'
string|'"Hello World\\n# The following ssh "'
op|'+'
nl|'\n'
string|'"key was injected by Nova\\nmysshkey\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o600'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_data_key_with_selinux
dedent|''
name|'def'
name|'test_inject_data_key_with_selinux'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"etc/selinux"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"etc/rc.d"'
op|')'
newline|'\n'
name|'diskapi'
op|'.'
name|'_inject_key_into_fs'
op|'('
string|'"mysshkey"'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/etc/rc.d/rc.local"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/etc/rc.d/rc.local"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'content'"
op|':'
string|'"Hello World#!/bin/sh\\n# Added by "'
op|'+'
nl|'\n'
string|'"Nova to ensure injected ssh keys "'
op|'+'
nl|'\n'
string|'"have the right context\\nrestorecon "'
op|'+'
nl|'\n'
string|'"-RF root/.ssh 2>/dev/null || :\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/root/.ssh"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/root/.ssh"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'True'
op|','
string|"'gid'"
op|':'
number|'0'
op|','
string|"'uid'"
op|':'
number|'0'
op|','
string|"'mode'"
op|':'
number|'0o700'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/root/.ssh/authorized_keys"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/root/.ssh/authorized_keys"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'content'"
op|':'
string|'"Hello World\\n# The following ssh "'
op|'+'
nl|'\n'
string|'"key was injected by Nova\\nmysshkey\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o600'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_data_key_with_selinux_append_with_newline
dedent|''
name|'def'
name|'test_inject_data_key_with_selinux_append_with_newline'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'replace_file'
op|'('
string|'"/etc/rc.d/rc.local"'
op|','
string|'"#!/bin/sh\\necho done"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"etc/selinux"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"etc/rc.d"'
op|')'
newline|'\n'
name|'diskapi'
op|'.'
name|'_inject_key_into_fs'
op|'('
string|'"mysshkey"'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/etc/rc.d/rc.local"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/etc/rc.d/rc.local"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'content'"
op|':'
string|'"#!/bin/sh\\necho done\\n# Added "'
nl|'\n'
string|'"by Nova to ensure injected ssh keys have "'
nl|'\n'
string|'"the right context\\nrestorecon -RF "'
nl|'\n'
string|'"root/.ssh 2>/dev/null || :\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|'}'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_net
dedent|''
name|'def'
name|'test_inject_net'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'diskapi'
op|'.'
name|'_inject_net_into_fs'
op|'('
string|'"mynetconfig"'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/etc/network/interfaces"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/etc/network/interfaces"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'content'"
op|':'
string|"'mynetconfig'"
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_metadata
dedent|''
name|'def'
name|'test_inject_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'diskapi'
op|'.'
name|'_inject_metadata_into_fs'
op|'('
op|'['
op|'{'
string|'"key"'
op|':'
string|'"foo"'
op|','
nl|'\n'
string|'"value"'
op|':'
string|'"bar"'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"key"'
op|':'
string|'"eek"'
op|','
nl|'\n'
string|'"value"'
op|':'
string|'"wizz"'
op|'}'
op|']'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/meta.js"'
name|'in'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/meta.js"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'content'"
op|':'
string|'\'{"foo": "bar", \''
op|'+'
nl|'\n'
string|'\'"eek": "wizz"}\''
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_admin_password
dedent|''
name|'def'
name|'test_inject_admin_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vfs'
op|'='
name|'vfsguestfs'
op|'.'
name|'VFSGuestFS'
op|'('
string|'"/some/file"'
op|','
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_salt
name|'def'
name|'fake_salt'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|'"1234567890abcdef"'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'diskapi'
op|','
string|"'_generate_salt'"
op|','
name|'fake_salt'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'write'
op|'('
string|'"/etc/shadow"'
op|','
nl|'\n'
string|'"root:$1$12345678$xxxxx:14917:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"bin:*:14495:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"daemon:*:14495:0:99999:7:::\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'write'
op|'('
string|'"/etc/passwd"'
op|','
nl|'\n'
string|'"root:x:0:0:root:/root:/bin/bash\\n"'
op|'+'
nl|'\n'
string|'"bin:x:1:1:bin:/bin:/sbin/nologin\\n"'
op|'+'
nl|'\n'
string|'"daemon:x:2:2:daemon:/sbin:/sbin/nologin\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'diskapi'
op|'.'
name|'_inject_admin_password_into_fs'
op|'('
string|'"123456"'
op|','
name|'vfs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/etc/passwd"'
op|']'
op|','
nl|'\n'
op|'{'
string|"'content'"
op|':'
string|'"root:x:0:0:root:/root:/bin/bash\\n"'
op|'+'
nl|'\n'
string|'"bin:x:1:1:bin:/bin:/sbin/nologin\\n"'
op|'+'
nl|'\n'
string|'"daemon:x:2:2:daemon:/sbin:"'
op|'+'
nl|'\n'
string|'"/sbin/nologin\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
name|'shadow'
op|'='
name|'vfs'
op|'.'
name|'handle'
op|'.'
name|'files'
op|'['
string|'"/etc/shadow"'
op|']'
newline|'\n'
nl|'\n'
comment|'# if the encrypted password is only 13 characters long, then'
nl|'\n'
comment|'# nova.virt.disk.api:_set_password fell back to DES.'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'shadow'
op|'['
string|"'content'"
op|']'
op|')'
op|'=='
number|'91'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'shadow'
op|','
nl|'\n'
op|'{'
string|"'content'"
op|':'
string|'"root:12tir.zIbWQ3c"'
op|'+'
nl|'\n'
string|'":14917:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"bin:*:14495:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"daemon:*:14495:0:99999:7:::\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'shadow'
op|','
nl|'\n'
op|'{'
string|"'content'"
op|':'
string|'"root:$1$12345678$a4ge4d5iJ5vw"'
op|'+'
nl|'\n'
string|'"vbFS88TEN0:14917:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"bin:*:14495:0:99999:7:::\\n"'
op|'+'
nl|'\n'
string|'"daemon:*:14495:0:99999:7:::\\n"'
op|','
nl|'\n'
string|"'gid'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'isdir'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'mode'"
op|':'
number|'0o700'
op|','
nl|'\n'
string|"'uid'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'vfs'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
