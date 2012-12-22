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
name|'utils'
name|'as'
name|'tests_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
name|'import'
name|'localfs'
name|'as'
name|'vfsimpl'
newline|'\n'
nl|'\n'
DECL|variable|dirs
name|'dirs'
op|'='
op|'['
op|']'
newline|'\n'
DECL|variable|files
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|commands
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
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
name|'commands'
op|'.'
name|'append'
op|'('
op|'{'
string|'"args"'
op|':'
name|'args'
op|','
string|'"kwargs"'
op|':'
name|'kwargs'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"readlink"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'['
number|'1'
op|']'
op|'=='
string|'"-nm"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'args'
op|'['
number|'2'
op|']'
name|'in'
op|'['
string|'"/scratch/dir/some/file"'
op|','
nl|'\n'
string|'"/scratch/dir/some/dir"'
op|','
nl|'\n'
string|'"/scratch/dir/other/dir"'
op|','
nl|'\n'
string|'"/scratch/dir/other/file"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'args'
op|'['
number|'2'
op|']'
op|','
string|'""'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'args'
op|'['
number|'1'
op|']'
op|'=='
string|'"-e"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'args'
op|'['
number|'2'
op|']'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'args'
op|'['
number|'2'
op|']'
op|','
string|'""'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
string|'""'
op|','
string|'"No such file"'
newline|'\n'
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"mkdir"'
op|':'
newline|'\n'
indent|'        '
name|'dirs'
op|'.'
name|'append'
op|'('
name|'args'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"chown"'
op|':'
newline|'\n'
indent|'        '
name|'owner'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'path'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'sep'
op|'='
name|'owner'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'if'
name|'sep'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'='
name|'owner'
op|'['
number|'0'
op|':'
name|'sep'
op|']'
newline|'\n'
name|'group'
op|'='
name|'owner'
op|'['
name|'sep'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'user'
op|'='
name|'owner'
newline|'\n'
name|'group'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'user'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'user'
op|'=='
string|'"fred"'
op|':'
newline|'\n'
indent|'                '
name|'uid'
op|'='
number|'105'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'uid'
op|'='
number|'110'
newline|'\n'
dedent|''
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
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'group'
op|'=='
string|'"users"'
op|':'
newline|'\n'
indent|'                '
name|'gid'
op|'='
number|'500'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'gid'
op|'='
number|'600'
newline|'\n'
dedent|''
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
dedent|''
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"chgrp"'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'path'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'group'
op|'=='
string|'"users"'
op|':'
newline|'\n'
indent|'            '
name|'gid'
op|'='
number|'500'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'gid'
op|'='
number|'600'
newline|'\n'
dedent|''
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
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"chmod"'
op|':'
newline|'\n'
indent|'        '
name|'mode'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'path'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"No such file: "'
op|'+'
name|'path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"mode"'
op|']'
op|'='
name|'int'
op|'('
name|'mode'
op|','
number|'8'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"cat"'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
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
number|'0700'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|','
string|'""'
newline|'\n'
dedent|''
name|'elif'
name|'args'
op|'['
number|'0'
op|']'
op|'=='
string|'"tee"'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'args'
op|'['
number|'1'
op|']'
op|'=='
string|'"-a"'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
name|'append'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'append'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'print'
name|'str'
op|'('
name|'files'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'path'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'['
name|'path'
op|']'
op|'='
op|'{'
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
number|'0700'
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'if'
name|'append'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|'+='
name|'kwargs'
op|'['
string|'"process_input"'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'['
name|'path'
op|']'
op|'['
string|'"content"'
op|']'
op|'='
name|'kwargs'
op|'['
string|'"process_input"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtDiskVFSLocalFSTestPaths
dedent|''
dedent|''
dedent|''
name|'class'
name|'VirtDiskVFSLocalFSTestPaths'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'VirtDiskVFSLocalFSTestPaths'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'real_execute'
op|'='
name|'utils'
op|'.'
name|'execute'
newline|'\n'
nl|'\n'
DECL|function|nonroot_execute
name|'def'
name|'nonroot_execute'
op|'('
op|'*'
name|'cmd_parts'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'run_as_root'"
op|','
name|'None'
op|')'
newline|'\n'
name|'return'
name|'real_execute'
op|'('
op|'*'
name|'cmd_parts'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'nonroot_execute'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_safe_path
dedent|''
name|'def'
name|'test_check_safe_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'tests_utils'
op|'.'
name|'is_osx'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Unable to test on OSX"'
op|')'
newline|'\n'
dedent|''
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
string|'"dummy.img"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/foo"'
newline|'\n'
name|'ret'
op|'='
name|'vfs'
op|'.'
name|'_canonical_path'
op|'('
string|"'etc/something.conf'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'ret'
op|','
string|"'/foo/etc/something.conf'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_unsafe_path
dedent|''
name|'def'
name|'test_check_unsafe_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'tests_utils'
op|'.'
name|'is_osx'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Unable to test on OSX"'
op|')'
newline|'\n'
dedent|''
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
string|'"dummy.img"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/foo"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Invalid'
op|','
nl|'\n'
name|'vfs'
op|'.'
name|'_canonical_path'
op|','
nl|'\n'
string|"'etc/../../../something.conf'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtDiskVFSLocalFSTest
dedent|''
dedent|''
name|'class'
name|'VirtDiskVFSLocalFSTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'VirtDiskVFSLocalFSTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_makepath
dedent|''
name|'def'
name|'test_makepath'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'dirs'
op|','
name|'commands'
newline|'\n'
name|'dirs'
op|'='
op|'['
op|']'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"/some/dir"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'make_path'
op|'('
string|'"/other/dir"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dirs'
op|','
nl|'\n'
op|'['
string|'"/scratch/dir/some/dir"'
op|','
string|'"/scratch/dir/other/dir"'
op|']'
op|')'
op|','
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/dir'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
nl|'\n'
string|"'/scratch/dir/some/dir'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/other/dir'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
nl|'\n'
string|"'/scratch/dir/other/dir'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_append_file
dedent|''
name|'def'
name|'test_append_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'files'
op|','
name|'commands'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'append_file'
op|'('
string|'"/some/file"'
op|','
string|'" Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/scratch/dir/some/file"'
name|'in'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"content"'
op|']'
op|','
nl|'\n'
string|'"Hello World Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'tee'"
op|','
string|"'-a'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'process_input'"
op|':'
string|"' Goodbye'"
op|','
nl|'\n'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_replace_file
dedent|''
name|'def'
name|'test_replace_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'files'
op|','
name|'commands'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'replace_file'
op|'('
string|'"/some/file"'
op|','
string|'"Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|'"/scratch/dir/some/file"'
name|'in'
name|'files'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"content"'
op|']'
op|','
nl|'\n'
string|'"Goodbye"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'tee'"
op|','
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'process_input'"
op|':'
string|"'Goodbye'"
op|','
nl|'\n'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_file
dedent|''
name|'def'
name|'test_read_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'commands'
op|','
name|'files'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
op|','
string|'"Hello World"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'cat'"
op|','
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_has_file
dedent|''
name|'def'
name|'test_has_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'commands'
op|','
name|'files'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vfs'
op|'.'
name|'has_file'
op|'('
string|'"/some/file"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'vfs'
op|'.'
name|'has_file'
op|'('
string|'"/other/file"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'cat'"
op|','
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-e'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/other/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-e'"
op|','
nl|'\n'
string|"'/scratch/dir/other/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_permissions
dedent|''
name|'def'
name|'test_set_permissions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'commands'
op|','
name|'files'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_permissions'
op|'('
string|'"/some/file"'
op|','
number|'0777'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"mode"'
op|']'
op|','
number|'0777'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'cat'"
op|','
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'chmod'"
op|','
string|"'777'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_ownership
dedent|''
name|'def'
name|'test_set_ownership'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'commands'
op|','
name|'files'
newline|'\n'
name|'commands'
op|'='
op|'['
op|']'
newline|'\n'
name|'files'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'='
name|'vfsimpl'
op|'.'
name|'VFSLocalFS'
op|'('
name|'imgfile'
op|'='
string|'"/dummy.qcow2"'
op|','
name|'imgfmt'
op|'='
string|'"qcow2"'
op|')'
newline|'\n'
name|'vfs'
op|'.'
name|'imgdir'
op|'='
string|'"/scratch/dir"'
newline|'\n'
name|'vfs'
op|'.'
name|'read_file'
op|'('
string|'"/some/file"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|','
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
string|'"fred"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|','
number|'105'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
name|'None'
op|','
string|'"users"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|','
number|'105'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|','
number|'500'
op|')'
newline|'\n'
nl|'\n'
name|'vfs'
op|'.'
name|'set_ownership'
op|'('
string|'"/some/file"'
op|','
string|'"joe"'
op|','
string|'"admins"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"uid"'
op|']'
op|','
number|'110'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'files'
op|'['
string|'"/scratch/dir/some/file"'
op|']'
op|'['
string|'"gid"'
op|']'
op|','
number|'600'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'commands'
op|','
nl|'\n'
op|'['
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'cat'"
op|','
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'chown'"
op|','
string|"'fred'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'chgrp'"
op|','
string|"'users'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'readlink'"
op|','
string|"'-nm'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'args'"
op|':'
op|'('
string|"'chown'"
op|','
string|"'joe:admins'"
op|','
nl|'\n'
string|"'/scratch/dir/some/file'"
op|')'
op|','
nl|'\n'
string|"'kwargs'"
op|':'
op|'{'
string|"'run_as_root'"
op|':'
name|'True'
op|'}'
op|'}'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
