begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
DECL|variable|hyperv_opts
name|'hyperv_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'instances_path_share'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|'""'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The name of a Windows share name mapped to the '"
nl|'\n'
string|'\'"instances_path" dir and used by the resize feature \''
nl|'\n'
string|"'to copy files to the target host. If left blank, an '"
nl|'\n'
string|"'administrative share will be used, looking for the same '"
nl|'\n'
string|'\'"instances_path" used locally\''
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
name|'hyperv_opts'
op|','
string|"'hyperv'"
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
nl|'\n'
nl|'\n'
DECL|class|PathUtils
name|'class'
name|'PathUtils'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|open
indent|'    '
name|'def'
name|'open'
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
string|'"""Wrapper on __builin__.open used to simplify unit testing."""'
newline|'\n'
name|'import'
name|'__builtin__'
newline|'\n'
name|'return'
name|'__builtin__'
op|'.'
name|'open'
op|'('
name|'path'
op|','
name|'mode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|exists
dedent|''
name|'def'
name|'exists'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
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
DECL|member|makedirs
dedent|''
name|'def'
name|'makedirs'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove
dedent|''
name|'def'
name|'remove'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'remove'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rename
dedent|''
name|'def'
name|'rename'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'rename'
op|'('
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copyfile
dedent|''
name|'def'
name|'copyfile'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'copy'
op|'('
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy
dedent|''
name|'def'
name|'copy'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
comment|'# With large files this is 2x-3x faster than shutil.copy(src, dest),'
nl|'\n'
comment|'# especially when copying to a UNC target.'
nl|'\n'
comment|'# shutil.copyfileobj(...) with a proper buffer is better than'
nl|'\n'
comment|'# shutil.copy(...) but still 20% slower than a shell copy.'
nl|'\n'
comment|'# It can be replaced with Win32 API calls to avoid the process'
nl|'\n'
comment|'# spawning overhead.'
nl|'\n'
indent|'        '
name|'output'
op|','
name|'ret'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cmd.exe'"
op|','
string|"'/C'"
op|','
string|"'copy'"
op|','
string|"'/Y'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
name|'if'
name|'ret'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'IOError'
op|'('
name|'_'
op|'('
string|"'The file copy from %(src)s to %(dest)s failed'"
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'src'"
op|':'
name|'src'
op|','
string|"'dest'"
op|':'
name|'dest'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rmtree
dedent|''
dedent|''
name|'def'
name|'rmtree'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instances_dir
dedent|''
name|'def'
name|'get_instances_dir'
op|'('
name|'self'
op|','
name|'remote_server'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'local_instance_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'remote_server'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'instances_path_share'
op|':'
newline|'\n'
indent|'                '
name|'path'
op|'='
name|'CONF'
op|'.'
name|'hyperv'
op|'.'
name|'instances_path_share'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Use an administrative share'
nl|'\n'
indent|'                '
name|'path'
op|'='
name|'local_instance_path'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"'$'"
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
string|"'\\\\\\\\%(remote_server)s\\\\%(path)s'"
op|'%'
nl|'\n'
op|'{'
string|"'remote_server'"
op|':'
name|'remote_server'
op|','
string|"'path'"
op|':'
name|'path'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'local_instance_path'
newline|'\n'
nl|'\n'
DECL|member|_check_create_dir
dedent|''
dedent|''
name|'def'
name|'_check_create_dir'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating directory: %s'"
op|')'
op|'%'
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'makedirs'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_remove_dir
dedent|''
dedent|''
name|'def'
name|'_check_remove_dir'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Removing directory: %s'"
op|')'
op|'%'
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rmtree'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instances_sub_dir
dedent|''
dedent|''
name|'def'
name|'_get_instances_sub_dir'
op|'('
name|'self'
op|','
name|'dir_name'
op|','
name|'remote_server'
op|'='
name|'None'
op|','
nl|'\n'
name|'create_dir'
op|'='
name|'True'
op|','
name|'remove_dir'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instances_path'
op|'='
name|'self'
op|'.'
name|'get_instances_dir'
op|'('
name|'remote_server'
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instances_path'
op|','
name|'dir_name'
op|')'
newline|'\n'
name|'if'
name|'remove_dir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_remove_dir'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'create_dir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_create_dir'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|get_instance_migr_revert_dir
dedent|''
name|'def'
name|'get_instance_migr_revert_dir'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'create_dir'
op|'='
name|'False'
op|','
nl|'\n'
name|'remove_dir'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dir_name'
op|'='
string|"'%s_revert'"
op|'%'
name|'instance_name'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_instances_sub_dir'
op|'('
name|'dir_name'
op|','
name|'None'
op|','
name|'create_dir'
op|','
nl|'\n'
name|'remove_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_instance_dir
dedent|''
name|'def'
name|'get_instance_dir'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'remote_server'
op|'='
name|'None'
op|','
nl|'\n'
name|'create_dir'
op|'='
name|'True'
op|','
name|'remove_dir'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_instances_sub_dir'
op|'('
name|'instance_name'
op|','
name|'remote_server'
op|','
nl|'\n'
name|'create_dir'
op|','
name|'remove_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vhd_path
dedent|''
name|'def'
name|'get_vhd_path'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_path'
op|'='
name|'self'
op|'.'
name|'get_instance_dir'
op|'('
name|'instance_name'
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'instance_path'
op|','
string|"'root.vhd'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_base_vhd_dir
dedent|''
name|'def'
name|'get_base_vhd_dir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_instances_sub_dir'
op|'('
string|"'_base'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_export_dir
dedent|''
name|'def'
name|'get_export_dir'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dir_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'export'"
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_instances_sub_dir'
op|'('
name|'dir_name'
op|','
name|'create_dir'
op|'='
name|'True'
op|','
nl|'\n'
name|'remove_dir'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
