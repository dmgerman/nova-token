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
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
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
name|'volume'
op|'.'
name|'encryptors'
name|'import'
name|'nop'
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
DECL|function|get_volume_encryptor
name|'def'
name|'get_volume_encryptor'
op|'('
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a VolumeEncryptor used to encrypt the specified volume.\n\n    :param: the connection information used to attach the volume\n    :returns VolumeEncryptor: the VolumeEncryptor for the volume\n    """'
newline|'\n'
name|'encryptor'
op|'='
name|'nop'
op|'.'
name|'NoOpEncryptor'
op|'('
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'location'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'control_location'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'location'
name|'and'
name|'location'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|"'front-end'"
op|':'
comment|'# case insensitive'
newline|'\n'
indent|'        '
name|'provider'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'provider'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'encryptor'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'provider'
op|','
name|'connection_info'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
newline|'\n'
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
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Error instantiating %(provider)s: %(exception)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'provider'"
op|':'
name|'provider'
op|','
string|"'exception'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'encryptor'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_encryption_metadata
dedent|''
name|'def'
name|'get_encryption_metadata'
op|'('
name|'context'
op|','
name|'volume_api'
op|','
name|'volume_id'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
op|'('
string|"'data'"
name|'in'
name|'connection_info'
name|'and'
nl|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'.'
name|'get'
op|'('
string|"'encrypted'"
op|','
name|'False'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'volume_api'
op|'.'
name|'get_volume_encryption_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
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
name|'error'
op|'('
name|'_LE'
op|'('
string|'"Failed to retrieve encryption metadata for "'
nl|'\n'
string|'"volume %(volume_id)s: %(exception)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'volume_id'
op|','
string|"'exception'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'metadata'
newline|'\n'
dedent|''
endmarker|''
end_unit
