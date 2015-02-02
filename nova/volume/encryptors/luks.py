begin_unit
comment|'# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory'
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
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
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
name|'volume'
op|'.'
name|'encryptors'
name|'import'
name|'cryptsetup'
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
nl|'\n'
DECL|function|is_luks
name|'def'
name|'is_luks'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks if the specified device uses LUKS for encryption.\n\n    :param device: the device to check\n    :returns: true if the specified device uses LUKS; false otherwise\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# check to see if the device uses LUKS: exit status is 0'
nl|'\n'
comment|'# if the device is a LUKS partition and non-zero if not'
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cryptsetup'"
op|','
string|"'isLuks'"
op|','
string|"'--verbose'"
op|','
name|'device'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"isLuks exited abnormally (status %(exit_code)s): "'
nl|'\n'
string|'"%(stderr)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|'"exit_code"'
op|':'
name|'e'
op|'.'
name|'exit_code'
op|','
string|'"stderr"'
op|':'
name|'e'
op|'.'
name|'stderr'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LuksEncryptor
dedent|''
dedent|''
name|'class'
name|'LuksEncryptor'
op|'('
name|'cryptsetup'
op|'.'
name|'CryptsetupEncryptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A VolumeEncryptor based on LUKS.\n\n    This VolumeEncryptor uses dm-crypt to encrypt the specified volume.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LuksEncryptor'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_format_volume
dedent|''
name|'def'
name|'_format_volume'
op|'('
name|'self'
op|','
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a LUKS header on the volume.\n\n        :param passphrase: the passphrase used to access the volume\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"formatting encrypted volume %s"'
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(joel-coffman): cryptsetup will strip trailing newlines from'
nl|'\n'
comment|'# input specified on stdin unless --key-file=- is specified.'
nl|'\n'
name|'cmd'
op|'='
op|'['
string|'"cryptsetup"'
op|','
string|'"--batch-mode"'
op|','
string|'"luksFormat"'
op|','
string|'"--key-file=-"'
op|']'
newline|'\n'
nl|'\n'
name|'cipher'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cipher"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'cipher'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|'"--cipher"'
op|','
name|'cipher'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'key_size'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"key_size"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'key_size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|'"--key-size"'
op|','
name|'key_size'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
name|'self'
op|'.'
name|'dev_path'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'process_input'
op|'='
name|'passphrase'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_open_volume
dedent|''
name|'def'
name|'_open_volume'
op|'('
name|'self'
op|','
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Opens the LUKS partition on the volume using the specified\n        passphrase.\n\n        :param passphrase: the passphrase used to access the volume\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"opening encrypted volume %s"'
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cryptsetup'"
op|','
string|"'luksOpen'"
op|','
string|"'--key-file=-'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'dev_path'
op|','
name|'self'
op|'.'
name|'dev_name'
op|','
name|'process_input'
op|'='
name|'passphrase'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shadows the device and passes an unencrypted version to the\n        instance.\n\n        Transparent disk encryption is achieved by mounting the volume via\n        dm-crypt and passing the resulting device to the instance. The\n        instance is unaware of the underlying encryption due to modifying the\n        original symbolic link to refer to the device mounted by dm-crypt.\n        """'
newline|'\n'
nl|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'_get_key'
op|'('
name|'context'
op|')'
op|'.'
name|'get_encoded'
op|'('
op|')'
newline|'\n'
comment|'# LUKS uses a passphrase rather than a raw key -- convert to string'
nl|'\n'
name|'passphrase'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'hex'
op|'('
name|'x'
op|')'
op|'.'
name|'replace'
op|'('
string|"'0x'"
op|','
string|"''"
op|')'
name|'for'
name|'x'
name|'in'
name|'key'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_open_volume'
op|'('
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'exit_code'
op|'=='
number|'1'
name|'and'
name|'not'
name|'is_luks'
op|'('
name|'self'
op|'.'
name|'dev_path'
op|')'
op|':'
newline|'\n'
comment|'# the device has never been formatted; format it and try again'
nl|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"%s is not a valid LUKS device;"'
nl|'\n'
string|'" formatting device for first use"'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_format_volume'
op|'('
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_open_volume'
op|'('
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
comment|'# modify the original symbolic link to refer to the decrypted device'
nl|'\n'
dedent|''
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ln'"
op|','
string|"'--symbolic'"
op|','
string|"'--force'"
op|','
nl|'\n'
string|"'/dev/mapper/%s'"
op|'%'
name|'self'
op|'.'
name|'dev_name'
op|','
name|'self'
op|'.'
name|'symlink_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_close_volume
dedent|''
name|'def'
name|'_close_volume'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Closes the device (effectively removes the dm-crypt mapping)."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"closing encrypted volume %s"'
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cryptsetup'"
op|','
string|"'luksClose'"
op|','
name|'self'
op|'.'
name|'dev_name'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'3'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
