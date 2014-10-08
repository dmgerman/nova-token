begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""Wrappers around standard crypto data elements.\n\nIncludes root and intermediate CAs, SSH key_pairs and x509 certificates.\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'absolute_import'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'struct'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'pyasn1'
op|'.'
name|'codec'
op|'.'
name|'der'
name|'import'
name|'encoder'
name|'as'
name|'der_encoder'
newline|'\n'
name|'from'
name|'pyasn1'
op|'.'
name|'type'
name|'import'
name|'univ'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'_'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|crypto_opts
name|'crypto_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ca_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cacert.pem'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of root CA'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'key_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'private'"
op|','
string|"'cakey.pem'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of private key'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'crl_file'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'crl.pem'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Filename of root Certificate Revocation List'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'keys_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'keys'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Where we keep our keys'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ca_path'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'CA'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Where we keep our root CA'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_project_ca'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Should we use a CA for each project?'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'user_cert_subject'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'/C=US/ST=California/O=OpenStack/'"
nl|'\n'
string|"'OU=NovaDev/CN=%.16s-%.16s-%s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Subject for certificate for users, %s for '"
nl|'\n'
string|"'project, user, timestamp'"
op|')'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'project_cert_subject'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'/C=US/ST=California/O=OpenStack/'"
nl|'\n'
string|"'OU=NovaDev/CN=project-ca-%.16s-%s'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
name|'_'
op|'('
string|"'Subject for certificate for projects, %s for '"
nl|'\n'
string|"'project, timestamp'"
op|')'
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
name|'crypto_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ca_folder
name|'def'
name|'ca_folder'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'CONF'
op|'.'
name|'use_project_ca'
name|'and'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'ca_path'
op|','
string|"'projects'"
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'CONF'
op|'.'
name|'ca_path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ca_path
dedent|''
name|'def'
name|'ca_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'CONF'
op|'.'
name|'ca_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|key_path
dedent|''
name|'def'
name|'key_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'CONF'
op|'.'
name|'key_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|crl_path
dedent|''
name|'def'
name|'crl_path'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
name|'CONF'
op|'.'
name|'crl_file'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_ca
dedent|''
name|'def'
name|'fetch_ca'
op|'('
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'ca_file_path'
op|'='
name|'ca_path'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_file_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'CryptoCAFileNotFound'
op|'('
name|'project'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'ca_file_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_ca_filesystem
dedent|''
dedent|''
name|'def'
name|'ensure_ca_filesystem'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure the CA filesystem exists."""'
newline|'\n'
name|'ca_dir'
op|'='
name|'ca_folder'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_path'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'genrootca_sh_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'CA'"
op|','
string|"'genrootca.sh'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'ca_dir'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_dir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|'"sh"'
op|','
name|'genrootca_sh_path'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_generate_fingerprint
dedent|''
dedent|''
name|'def'
name|'_generate_fingerprint'
op|'('
name|'public_key_file'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ssh-keygen'"
op|','
string|"'-q'"
op|','
string|"'-l'"
op|','
string|"'-f'"
op|','
name|'public_key_file'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'return'
name|'fingerprint'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_fingerprint
dedent|''
name|'def'
name|'generate_fingerprint'
op|'('
name|'public_key'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pubfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.pub'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'pubfile'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'f'
op|'.'
name|'write'
op|'('
name|'public_key'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_generate_fingerprint'
op|'('
name|'pubfile'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidKeypair'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'failed to generate fingerprint'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_key_pair
dedent|''
dedent|''
dedent|''
name|'def'
name|'generate_key_pair'
op|'('
name|'bits'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp'"
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
string|"'ssh-keygen'"
op|','
string|"'-q'"
op|','
string|"'-N'"
op|','
string|"''"
op|','
string|"'-t'"
op|','
string|"'rsa'"
op|','
nl|'\n'
string|"'-f'"
op|','
name|'keyfile'
op|','
string|"'-C'"
op|','
string|"'Generated-by-Nova'"
op|']'
newline|'\n'
name|'if'
name|'bits'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'-b'"
op|','
name|'bits'
op|']'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'_generate_fingerprint'
op|'('
string|"'%s.pub'"
op|'%'
op|'('
name|'keyfile'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'keyfile'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FileNotFound'
op|'('
name|'keyfile'
op|')'
newline|'\n'
dedent|''
name|'private_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'public_key_path'
op|'='
name|'keyfile'
op|'+'
string|"'.pub'"
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'public_key_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FileNotFound'
op|'('
name|'public_key_path'
op|')'
newline|'\n'
dedent|''
name|'public_key'
op|'='
name|'open'
op|'('
name|'public_key_path'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'private_key'
op|','
name|'public_key'
op|','
name|'fingerprint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_crl
dedent|''
name|'def'
name|'fetch_crl'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get crl file for project."""'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'crl_file_path'
op|'='
name|'crl_path'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'crl_file_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'CryptoCRLFileNotFound'
op|'('
name|'project'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'crl_file_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'crlfile'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'crlfile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|decrypt_text
dedent|''
dedent|''
name|'def'
name|'decrypt_text'
op|'('
name|'project_id'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'private_key'
op|'='
name|'key_path'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'private_key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ProjectNotFound'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'dec'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
nl|'\n'
string|"'rsautl'"
op|','
nl|'\n'
string|"'-decrypt'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
string|"'%s'"
op|'%'
name|'private_key'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'return'
name|'dec'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DecryptionFailure'
op|'('
name|'reason'
op|'='
name|'exc'
op|'.'
name|'stderr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_RSA_OID
dedent|''
dedent|''
name|'_RSA_OID'
op|'='
name|'univ'
op|'.'
name|'ObjectIdentifier'
op|'('
string|"'1.2.840.113549.1.1.1'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_to_sequence
name|'def'
name|'_to_sequence'
op|'('
op|'*'
name|'vals'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'seq'
op|'='
name|'univ'
op|'.'
name|'Sequence'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'vals'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'seq'
op|'.'
name|'setComponentByPosition'
op|'('
name|'i'
op|','
name|'vals'
op|'['
name|'i'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'seq'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|convert_from_sshrsa_to_pkcs8
dedent|''
name|'def'
name|'convert_from_sshrsa_to_pkcs8'
op|'('
name|'pubkey'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a ssh public key to openssl format\n       Equivalent to the ssh-keygen\'s -m option\n    """'
newline|'\n'
comment|'# get the second field from the public key file.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'keydata'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'pubkey'
op|'.'
name|'split'
op|'('
name|'None'
op|')'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unable to find the key"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'EncryptionFailure'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
comment|'# decode the parts of the key'
nl|'\n'
dedent|''
name|'parts'
op|'='
op|'['
op|']'
newline|'\n'
name|'while'
name|'keydata'
op|':'
newline|'\n'
indent|'        '
name|'dlen'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'>I'"
op|','
name|'keydata'
op|'['
op|':'
number|'4'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'data'
op|'='
name|'keydata'
op|'['
number|'4'
op|':'
name|'dlen'
op|'+'
number|'4'
op|']'
newline|'\n'
name|'keydata'
op|'='
name|'keydata'
op|'['
number|'4'
op|'+'
name|'dlen'
op|':'
op|']'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
comment|'# Use asn to build the openssl key structure'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#  SEQUENCE(2 elem)'
nl|'\n'
comment|'#    +- SEQUENCE(2 elem)'
nl|'\n'
comment|'#    |    +- OBJECT IDENTIFIER (1.2.840.113549.1.1.1)'
nl|'\n'
comment|'#    |    +- NULL'
nl|'\n'
comment|'#    +- BIT STRING(1 elem)'
nl|'\n'
comment|'#         +- SEQUENCE(2 elem)'
nl|'\n'
comment|'#              +- INTEGER(2048 bit)'
nl|'\n'
comment|'#              +- INTEGER 65537'
nl|'\n'
nl|'\n'
comment|'# Build the sequence for the bit string'
nl|'\n'
dedent|''
name|'n_val'
op|'='
name|'int'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'%02X'"
op|'%'
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'B'"
op|','
name|'x'
op|')'
op|'['
number|'0'
op|']'
name|'for'
name|'x'
name|'in'
name|'parts'
op|'['
number|'2'
op|']'
op|']'
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'e_val'
op|'='
name|'int'
op|'('
nl|'\n'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'%02X'"
op|'%'
name|'struct'
op|'.'
name|'unpack'
op|'('
string|"'B'"
op|','
name|'x'
op|')'
op|'['
number|'0'
op|']'
name|'for'
name|'x'
name|'in'
name|'parts'
op|'['
number|'1'
op|']'
op|']'
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'pkinfo'
op|'='
name|'_to_sequence'
op|'('
name|'univ'
op|'.'
name|'Integer'
op|'('
name|'n_val'
op|')'
op|','
name|'univ'
op|'.'
name|'Integer'
op|'('
name|'e_val'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Convert the sequence into a bit string'
nl|'\n'
name|'pklong'
op|'='
name|'long'
op|'('
name|'der_encoder'
op|'.'
name|'encode'
op|'('
name|'pkinfo'
op|')'
op|'.'
name|'encode'
op|'('
string|"'hex'"
op|')'
op|','
number|'16'
op|')'
newline|'\n'
name|'pkbitstring'
op|'='
name|'univ'
op|'.'
name|'BitString'
op|'('
string|'"\'00%s\'B"'
op|'%'
name|'bin'
op|'('
name|'pklong'
op|')'
op|'['
number|'2'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Build the key data structure'
nl|'\n'
name|'oid'
op|'='
name|'_to_sequence'
op|'('
name|'_RSA_OID'
op|','
name|'univ'
op|'.'
name|'Null'
op|'('
op|')'
op|')'
newline|'\n'
name|'pkcs1_seq'
op|'='
name|'_to_sequence'
op|'('
name|'oid'
op|','
name|'pkbitstring'
op|')'
newline|'\n'
name|'pkcs8'
op|'='
name|'base64'
op|'.'
name|'encodestring'
op|'('
name|'der_encoder'
op|'.'
name|'encode'
op|'('
name|'pkcs1_seq'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Remove the embedded new line and format the key, each line'
nl|'\n'
comment|'# should be 64 characters long'
nl|'\n'
name|'return'
op|'('
string|"'-----BEGIN PUBLIC KEY-----\\n%s\\n-----END PUBLIC KEY-----\\n'"
op|'%'
nl|'\n'
name|'re'
op|'.'
name|'sub'
op|'('
string|'"(.{64})"'
op|','
string|'"\\\\1\\n"'
op|','
name|'pkcs8'
op|'.'
name|'replace'
op|'('
string|"'\\n'"
op|','
string|"''"
op|')'
op|','
name|'re'
op|'.'
name|'DOTALL'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ssh_encrypt_text
dedent|''
name|'def'
name|'ssh_encrypt_text'
op|'('
name|'ssh_public_key'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Encrypt text with an ssh public key.\n    """'
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
indent|'        '
name|'sslkey'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'ssl.key'"
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
name|'convert_from_sshrsa_to_pkcs8'
op|'('
name|'ssh_public_key'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'sslkey'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'f'
op|'.'
name|'write'
op|'('
name|'out'
op|')'
newline|'\n'
dedent|''
name|'enc'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
nl|'\n'
string|"'rsautl'"
op|','
nl|'\n'
string|"'-encrypt'"
op|','
nl|'\n'
string|"'-pubin'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
name|'sslkey'
op|','
nl|'\n'
string|"'-keyform'"
op|','
string|"'PEM'"
op|','
nl|'\n'
name|'process_input'
op|'='
name|'text'
op|')'
newline|'\n'
name|'return'
name|'enc'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'EncryptionFailure'
op|'('
name|'reason'
op|'='
name|'exc'
op|'.'
name|'stderr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_cert
dedent|''
dedent|''
dedent|''
name|'def'
name|'revoke_cert'
op|'('
name|'project_id'
op|','
name|'file_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke a cert by file name."""'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'ProjectNotFound'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(vish): potential race condition here'
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-config'"
op|','
string|"'./openssl.cnf'"
op|','
string|"'-revoke'"
op|','
nl|'\n'
name|'file_name'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-gencrl'"
op|','
string|"'-config'"
op|','
string|"'./openssl.cnf'"
op|','
nl|'\n'
string|"'-out'"
op|','
name|'CONF'
op|'.'
name|'crl_file'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'RevokeCertFailure'
op|'('
name|'project_id'
op|'='
name|'project_id'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_user
dedent|''
dedent|''
name|'def'
name|'revoke_certs_by_user'
op|'('
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke all user certs."""'
newline|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_user'
op|'('
name|'admin'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_project
dedent|''
dedent|''
name|'def'
name|'revoke_certs_by_project'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke all project certs."""'
newline|'\n'
comment|'# NOTE(vish): This is somewhat useless because we can just shut down'
nl|'\n'
comment|'#             the vpn.'
nl|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_project'
op|'('
name|'admin'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_certs_by_user_and_project
dedent|''
dedent|''
name|'def'
name|'revoke_certs_by_user_and_project'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke certs for user in project."""'
newline|'\n'
name|'admin'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'for'
name|'cert'
name|'in'
name|'db'
op|'.'
name|'certificate_get_all_by_user_and_project'
op|'('
name|'admin'
op|','
nl|'\n'
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'revoke_cert'
op|'('
name|'cert'
op|'['
string|"'project_id'"
op|']'
op|','
name|'cert'
op|'['
string|"'file_name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_project_cert_subject
dedent|''
dedent|''
name|'def'
name|'_project_cert_subject'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper to generate user cert subject."""'
newline|'\n'
name|'return'
name|'CONF'
op|'.'
name|'project_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_user_cert_subject
dedent|''
name|'def'
name|'_user_cert_subject'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper to generate user cert subject."""'
newline|'\n'
name|'return'
name|'CONF'
op|'.'
name|'user_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'user_id'
op|','
name|'timeutils'
op|'.'
name|'isotime'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_x509_cert
dedent|''
name|'def'
name|'generate_x509_cert'
op|'('
name|'user_id'
op|','
name|'project_id'
op|','
name|'bits'
op|'='
number|'2048'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate and sign a cert for user in project."""'
newline|'\n'
name|'subject'
op|'='
name|'_user_cert_subject'
op|'('
name|'user_id'
op|','
name|'project_id'
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
name|'tmpdir'
op|':'
newline|'\n'
indent|'        '
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.key'"
op|')'
op|')'
newline|'\n'
name|'csrfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.csr'"
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'genrsa'"
op|','
string|"'-out'"
op|','
name|'keyfile'
op|','
name|'str'
op|'('
name|'bits'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'req'"
op|','
string|"'-new'"
op|','
string|"'-key'"
op|','
name|'keyfile'
op|','
string|"'-out'"
op|','
nl|'\n'
name|'csrfile'
op|','
string|"'-batch'"
op|','
string|"'-subj'"
op|','
name|'subject'
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'csr'
op|'='
name|'open'
op|'('
name|'csrfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'serial'
op|','
name|'signed_csr'
op|')'
op|'='
name|'sign_csr'
op|'('
name|'csr'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|','
string|"'newcerts/%s.pem'"
op|'%'
name|'serial'
op|')'
newline|'\n'
name|'cert'
op|'='
op|'{'
string|"'user_id'"
op|':'
name|'user_id'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'project_id'
op|','
nl|'\n'
string|"'file_name'"
op|':'
name|'fname'
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'certificate_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'cert'
op|')'
newline|'\n'
name|'return'
op|'('
name|'private_key'
op|','
name|'signed_csr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ensure_project_folder
dedent|''
name|'def'
name|'_ensure_project_folder'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'geninter_sh_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'CA'"
op|','
string|"'geninter.sh'"
op|')'
op|')'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|'('
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sh'"
op|','
name|'geninter_sh_path'
op|','
name|'project_id'
op|','
nl|'\n'
name|'_project_cert_subject'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_vpn_files
dedent|''
dedent|''
name|'def'
name|'generate_vpn_files'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'project_folder'
op|'='
name|'ca_folder'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'key_fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'project_folder'
op|','
string|"'server.key'"
op|')'
newline|'\n'
name|'crt_fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'project_folder'
op|','
string|"'server.crt'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'crt_fn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
comment|'# NOTE(vish): The 2048 is to maintain compatibility with the old script.'
nl|'\n'
comment|'#             We are using "project-vpn" as the user_id for the cert'
nl|'\n'
comment|'#             even though that user may not really exist. Ultimately'
nl|'\n'
comment|'#             this will be changed to be launched by a real user.  At'
nl|'\n'
comment|'#             that point we will can delete this helper method.'
nl|'\n'
dedent|''
name|'key'
op|','
name|'csr'
op|'='
name|'generate_x509_cert'
op|'('
string|"'project-vpn'"
op|','
name|'project_id'
op|','
number|'2048'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'key_fn'
op|','
string|"'w'"
op|')'
name|'as'
name|'keyfile'
op|':'
newline|'\n'
indent|'        '
name|'keyfile'
op|'.'
name|'write'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'crt_fn'
op|','
string|"'w'"
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'        '
name|'crtfile'
op|'.'
name|'write'
op|'('
name|'csr'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|sign_csr
dedent|''
dedent|''
name|'def'
name|'sign_csr'
op|'('
name|'csr_text'
op|','
name|'project_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'use_project_ca'
op|':'
newline|'\n'
indent|'        '
name|'project_id'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'_ensure_project_folder'
op|'('
name|'project_id'
op|')'
newline|'\n'
name|'return'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_sign_csr
dedent|''
name|'def'
name|'_sign_csr'
op|'('
name|'csr_text'
op|','
name|'ca_folder'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
name|'inbound'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'inbound.csr'"
op|')'
newline|'\n'
name|'outbound'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'outbound.csr'"
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'inbound'
op|','
string|"'w'"
op|')'
name|'as'
name|'csrfile'
op|':'
newline|'\n'
indent|'                '
name|'csrfile'
op|'.'
name|'write'
op|'('
name|'csr_text'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
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
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to write inbound.csr'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Flags path: %s'"
op|','
name|'ca_folder'
op|')'
newline|'\n'
name|'start'
op|'='
name|'os'
op|'.'
name|'getcwd'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Change working dir to CA'
nl|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'ca_folder'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'ca_folder'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'ca'"
op|','
string|"'-batch'"
op|','
string|"'-out'"
op|','
name|'outbound'
op|','
string|"'-config'"
op|','
nl|'\n'
string|"'./openssl.cnf'"
op|','
string|"'-infiles'"
op|','
name|'inbound'
op|')'
newline|'\n'
name|'out'
op|','
name|'_err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'x509'"
op|','
string|"'-in'"
op|','
name|'outbound'
op|','
nl|'\n'
string|"'-serial'"
op|','
string|"'-noout'"
op|')'
newline|'\n'
name|'serial'
op|'='
name|'string'
op|'.'
name|'strip'
op|'('
name|'out'
op|'.'
name|'rpartition'
op|'('
string|"'='"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'outbound'
op|','
string|"'r'"
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'serial'
op|','
name|'crtfile'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
