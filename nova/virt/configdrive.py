begin_unit
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
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
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
name|'i18n'
name|'import'
name|'_LW'
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
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'always'"
op|','
string|"'True'"
op|','
string|"'False'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'\'Set to "always" to force injection to take place on a \''
nl|'\n'
string|'\'config drive. NOTE: The "always" will be deprecated in \''
nl|'\n'
string|"'the Liberty release cycle.'"
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
comment|"# Config drives are 64mb, if we can't size to the exact size of the data"
nl|'\n'
DECL|variable|CONFIGDRIVESIZE_BYTES
name|'CONFIGDRIVESIZE_BYTES'
op|'='
number|'64'
op|'*'
name|'units'
op|'.'
name|'Mi'
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
indent|'    '
string|'"""Build config drives, optionally as a context manager."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'if'
name|'CONF'
op|'.'
name|'force_config_drive'
op|'=='
string|"'always'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'\'The setting "always" will be deprecated in the \''
nl|'\n'
string|'\'Liberty version. Please use "True" instead\''
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'imagefile'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'mdfiles'
op|'='
op|'['
op|']'
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
DECL|member|__enter__
dedent|''
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'exctype'
op|','
name|'excval'
op|','
name|'exctb'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'exctype'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
comment|"# NOTE(mikal): this means we're being cleaned up because an"
nl|'\n'
comment|'# exception was thrown. All bets are off now, and we should not'
nl|'\n'
comment|'# swallow the exception'
nl|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_file
dedent|''
name|'def'
name|'_add_file'
op|'('
name|'self'
op|','
name|'basedir'
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
name|'basedir'
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
string|"'wb'"
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
name|'data'
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
name|'mdfiles'
op|'.'
name|'append'
op|'('
op|'('
name|'path'
op|','
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_write_md_files
dedent|''
dedent|''
name|'def'
name|'_write_md_files'
op|'('
name|'self'
op|','
name|'basedir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'data'
name|'in'
name|'self'
op|'.'
name|'mdfiles'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_add_file'
op|'('
name|'basedir'
op|','
name|'data'
op|'['
number|'0'
op|']'
op|','
name|'data'
op|'['
number|'1'
op|']'
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
op|','
name|'tmpdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'publisher'
op|'='
string|'"%(product)s %(version)s"'
op|'%'
op|'{'
nl|'\n'
string|"'product'"
op|':'
name|'version'
op|'.'
name|'product_string'
op|'('
op|')'
op|','
nl|'\n'
string|"'version'"
op|':'
name|'version'
op|'.'
name|'version_string_with_package'
op|'('
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'publisher'
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
name|'tmpdir'
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
op|','
name|'tmpdir'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(mikal): This is a little horrible, but I couldn't find an"
nl|'\n'
comment|'# equivalent to genisoimage for vfat filesystems.'
nl|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'wb'"
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
name|'CONFIGDRIVESIZE_BYTES'
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
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'mountdir'
op|':'
newline|'\n'
indent|'            '
name|'mounted'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'_'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
nl|'\n'
string|"'mount'"
op|','
string|"'-o'"
op|','
string|"'loop,uid=%d,gid=%d'"
op|'%'
op|'('
name|'os'
op|'.'
name|'getuid'
op|'('
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'getgid'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'path'
op|','
nl|'\n'
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
indent|'                    '
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
comment|"# NOTE(mikal): I can't just use shutils.copytree here,"
nl|'\n'
comment|'# because the destination directory already'
nl|'\n'
comment|'# exists. This is annoying.'
nl|'\n'
name|'for'
name|'ent'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'tmpdir'
op|')'
op|':'
newline|'\n'
indent|'                    '
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
name|'tmpdir'
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
indent|'                '
name|'if'
name|'mounted'
op|':'
newline|'\n'
indent|'                    '
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
nl|'\n'
DECL|member|make_drive
dedent|''
dedent|''
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
string|'"""Make the config drive.\n\n        :param path: the path to place the config drive image at\n\n        :raises ProcessExecuteError if a helper process has failed.\n        """'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_write_md_files'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'config_drive_format'
op|'=='
string|"'iso9660'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_make_iso9660'
op|'('
name|'path'
op|','
name|'tmpdir'
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
indent|'                '
name|'self'
op|'.'
name|'_make_vfat'
op|'('
name|'path'
op|','
name|'tmpdir'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
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
name|'fileutils'
op|'.'
name|'delete_if_exists'
op|'('
name|'self'
op|'.'
name|'imagefile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"<ConfigDriveBuilder: "'
op|'+'
name|'str'
op|'('
name|'self'
op|'.'
name|'mdfiles'
op|')'
op|'+'
string|'">"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|required_by
dedent|''
dedent|''
name|'def'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'image_prop'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance'
op|')'
op|'.'
name|'get'
op|'('
nl|'\n'
name|'utils'
op|'.'
name|'SM_IMAGE_PROP_PREFIX'
op|'+'
string|"'img_config_drive'"
op|','
string|"'optional'"
op|')'
newline|'\n'
name|'if'
name|'image_prop'
name|'not'
name|'in'
op|'['
string|"'optional'"
op|','
string|"'mandatory'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'Image config drive option %(image_prop)s is invalid '"
nl|'\n'
string|"'and will be ignored'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'image_prop'"
op|':'
name|'image_prop'
op|'}'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'config_drive'"
op|')'
name|'or'
nl|'\n'
string|"'always'"
op|'=='
name|'CONF'
op|'.'
name|'force_config_drive'
name|'or'
nl|'\n'
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'CONF'
op|'.'
name|'force_config_drive'
op|')'
name|'or'
nl|'\n'
name|'image_prop'
op|'=='
string|"'mandatory'"
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_instance
dedent|''
name|'def'
name|'update_instance'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Update the instance config_drive setting if necessary\n\n    The image or configuration file settings may override the default instance\n    setting. In this case the instance needs to mirror the actual\n    virtual machine configuration.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|'.'
name|'config_drive'
name|'and'
name|'required_by'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'.'
name|'config_drive'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
