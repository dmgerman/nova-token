begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Michael Still and Canonical Inc'
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
string|'"""Config Drive v2 helper."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
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
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
name|'import'
name|'version'
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
DECL|variable|configdrive_opts
name|'configdrive_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'config_drive_format'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'iso9660'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Config drive format. One of iso9660 (default) or vfat'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'config_drive_tempdir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'tempfile'
op|'.'
name|'tempdir'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
op|'('
string|"'Where to put temporary files associated with '"
nl|'\n'
string|"'config drive creation'"
op|')'
op|')'
op|','
nl|'\n'
comment|'# force_config_drive is a string option, to allow for future behaviors'
nl|'\n'
comment|'#  (e.g. use config_drive based on image properties)'
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'force_config_drive'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set to force injection to take place on a config drive '"
nl|'\n'
string|"'(if set, valid options are: always)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'mkisofs_cmd'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'genisoimage'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name and optionally path of the tool used for '"
nl|'\n'
string|"'ISO image creation'"
op|')'
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
name|'configdrive_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDriveBuilder
name|'class'
name|'ConfigDriveBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'instance_md'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'imagefile'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|"# TODO(mikal): I don't think I can use utils.tempdir here, because"
nl|'\n'
comment|'# I need to have the directory last longer than the scope of this'
nl|'\n'
comment|'# method call'
nl|'\n'
name|'self'
op|'.'
name|'tempdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'dir'
op|'='
name|'CONF'
op|'.'
name|'config_drive_tempdir'
op|','
nl|'\n'
name|'prefix'
op|'='
string|"'cd_gen_'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance_md'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'add_instance_metadata'
op|'('
name|'instance_md'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_file
dedent|''
dedent|''
name|'def'
name|'_add_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filepath'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|','
name|'path'
op|')'
newline|'\n'
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'filepath'
op|')'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'dirname'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'filepath'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|add_instance_metadata
dedent|''
dedent|''
name|'def'
name|'add_instance_metadata'
op|'('
name|'self'
op|','
name|'instance_md'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
op|'('
name|'path'
op|','
name|'value'
op|')'
name|'in'
name|'instance_md'
op|'.'
name|'metadata_for_config_drive'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_file'
op|'('
name|'path'
op|','
name|'value'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Added %(filepath)s to config drive'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'filepath'"
op|':'
name|'path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_iso9660
dedent|''
dedent|''
name|'def'
name|'_make_iso9660'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
name|'CONF'
op|'.'
name|'mkisofs_cmd'
op|','
nl|'\n'
string|"'-o'"
op|','
name|'path'
op|','
nl|'\n'
string|"'-ldots'"
op|','
nl|'\n'
string|"'-allow-lowercase'"
op|','
nl|'\n'
string|"'-allow-multidot'"
op|','
nl|'\n'
string|"'-l'"
op|','
nl|'\n'
string|"'-publisher'"
op|','
op|'('
string|'\'"OpenStack nova %s"\''
nl|'\n'
op|'%'
name|'version'
op|'.'
name|'version_string'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'-quiet'"
op|','
nl|'\n'
string|"'-J'"
op|','
nl|'\n'
string|"'-r'"
op|','
nl|'\n'
string|"'-V'"
op|','
string|"'config-2'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'tempdir'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'1'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_make_vfat
dedent|''
name|'def'
name|'_make_vfat'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(mikal): This is a little horrible, but I couldn't find an"
nl|'\n'
comment|'# equivalent to genisoimage for vfat filesystems. vfat images are'
nl|'\n'
comment|'# always 64mb.'
nl|'\n'
indent|'        '
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
indent|'            '
name|'f'
op|'.'
name|'truncate'
op|'('
number|'64'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'utils'
op|'.'
name|'mkfs'
op|'('
string|"'vfat'"
op|','
name|'path'
op|','
name|'label'
op|'='
string|"'config-2'"
op|')'
newline|'\n'
nl|'\n'
name|'mounted'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'mountdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'dir'
op|'='
name|'CONF'
op|'.'
name|'config_drive_tempdir'
op|','
nl|'\n'
name|'prefix'
op|'='
string|"'cd_mnt_'"
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
string|"'mount'"
op|','
string|"'-o'"
op|','
string|"'loop'"
op|','
name|'path'
op|','
name|'mountdir'
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
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'ConfigDriveMountFailed'
op|'('
name|'operation'
op|'='
string|"'mount'"
op|','
nl|'\n'
name|'error'
op|'='
name|'err'
op|')'
newline|'\n'
dedent|''
name|'mounted'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'chown'"
op|','
nl|'\n'
string|"'%s.%s'"
op|'%'
op|'('
name|'os'
op|'.'
name|'getuid'
op|'('
op|')'
op|','
name|'os'
op|'.'
name|'getgid'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'mountdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'ConfigDriveMountFailed'
op|'('
name|'operation'
op|'='
string|"'chown'"
op|','
nl|'\n'
name|'error'
op|'='
name|'err'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(mikal): I can't just use shutils.copytree here, because the"
nl|'\n'
comment|'# destination directory already exists. This is annoying.'
nl|'\n'
dedent|''
name|'for'
name|'ent'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'shutil'
op|'.'
name|'copytree'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|','
name|'ent'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mountdir'
op|','
name|'ent'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'mounted'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'mountdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'mountdir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|make_drive
dedent|''
dedent|''
name|'def'
name|'make_drive'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'config_drive_format'
op|'=='
string|"'iso9660'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_make_iso9660'
op|'('
name|'path'
op|')'
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
indent|'            '
name|'self'
op|'.'
name|'_make_vfat'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
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
DECL|member|cleanup
dedent|''
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'imagefile'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'delete_if_exists'
op|'('
name|'self'
op|'.'
name|'imagefile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Could not remove tmpdir: %s'"
op|')'
op|','
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|required_by
dedent|''
dedent|''
dedent|''
name|'def'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'config_drive'"
op|')'
name|'or'
name|'CONF'
op|'.'
name|'force_config_drive'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|enabled_for
dedent|''
name|'def'
name|'enabled_for'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'required_by'
op|'('
name|'instance'
op|')'
name|'or'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'config_drive_id'"
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
