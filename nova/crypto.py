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
name|'binascii'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'cryptography'
name|'import'
name|'exceptions'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
name|'import'
name|'backends'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
op|'.'
name|'asymmetric'
name|'import'
name|'padding'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
name|'import'
name|'hashes'
newline|'\n'
name|'from'
name|'cryptography'
op|'.'
name|'hazmat'
op|'.'
name|'primitives'
name|'import'
name|'serialization'
newline|'\n'
name|'from'
name|'cryptography'
name|'import'
name|'x509'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
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
name|'excutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'fileutils'
newline|'\n'
name|'import'
name|'paramiko'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
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
op|','
name|'_LE'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
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
name|'crypto'
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
name|'crypto'
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
name|'crypto'
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
name|'crypto'
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
name|'crypto'
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
name|'crypto'
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
name|'crypto'
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
name|'fileutils'
op|'.'
name|'ensure_tree'
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
op|','
name|'cwd'
op|'='
name|'ca_dir'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_fingerprint
dedent|''
dedent|''
name|'def'
name|'generate_fingerprint'
op|'('
name|'public_key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pub_bytes'
op|'='
name|'public_key'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
comment|'# Test that the given public_key string is a proper ssh key. The'
nl|'\n'
comment|'# returned object is unused since pyca/cryptography does not have a'
nl|'\n'
comment|'# fingerprint method.'
nl|'\n'
name|'serialization'
op|'.'
name|'load_ssh_public_key'
op|'('
nl|'\n'
name|'pub_bytes'
op|','
name|'backends'
op|'.'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'pub_data'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'public_key'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'digest'
op|'='
name|'hashes'
op|'.'
name|'Hash'
op|'('
name|'hashes'
op|'.'
name|'MD5'
op|'('
op|')'
op|','
name|'backends'
op|'.'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'digest'
op|'.'
name|'update'
op|'('
name|'pub_data'
op|')'
newline|'\n'
name|'md5hash'
op|'='
name|'digest'
op|'.'
name|'finalize'
op|'('
op|')'
newline|'\n'
name|'raw_fp'
op|'='
name|'binascii'
op|'.'
name|'hexlify'
op|'('
name|'md5hash'
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'raw_fp'
op|'='
name|'raw_fp'
op|'.'
name|'decode'
op|'('
string|"'ascii'"
op|')'
newline|'\n'
dedent|''
name|'return'
string|"':'"
op|'.'
name|'join'
op|'('
name|'a'
op|'+'
name|'b'
name|'for'
name|'a'
op|','
name|'b'
name|'in'
name|'zip'
op|'('
name|'raw_fp'
op|'['
op|':'
op|':'
number|'2'
op|']'
op|','
name|'raw_fp'
op|'['
number|'1'
op|':'
op|':'
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'        '
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
DECL|function|generate_x509_fingerprint
dedent|''
dedent|''
name|'def'
name|'generate_x509_fingerprint'
op|'('
name|'pem_key'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'pem_key'
op|','
name|'six'
op|'.'
name|'text_type'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pem_key'
op|'='
name|'pem_key'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
dedent|''
name|'cert'
op|'='
name|'x509'
op|'.'
name|'load_pem_x509_certificate'
op|'('
nl|'\n'
name|'pem_key'
op|','
name|'backends'
op|'.'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'raw_fp'
op|'='
name|'binascii'
op|'.'
name|'hexlify'
op|'('
name|'cert'
op|'.'
name|'fingerprint'
op|'('
name|'hashes'
op|'.'
name|'SHA1'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'raw_fp'
op|'='
name|'raw_fp'
op|'.'
name|'decode'
op|'('
string|"'ascii'"
op|')'
newline|'\n'
dedent|''
name|'return'
string|"':'"
op|'.'
name|'join'
op|'('
name|'a'
op|'+'
name|'b'
name|'for'
name|'a'
op|','
name|'b'
name|'in'
name|'zip'
op|'('
name|'raw_fp'
op|'['
op|':'
op|':'
number|'2'
op|']'
op|','
name|'raw_fp'
op|'['
number|'1'
op|':'
op|':'
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|','
name|'binascii'
op|'.'
name|'Error'
op|')'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
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
string|"'failed to generate X509 fingerprint. '"
nl|'\n'
string|"'Error message: %s'"
op|')'
op|'%'
name|'ex'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_key
dedent|''
dedent|''
name|'def'
name|'generate_key'
op|'('
name|'bits'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate a paramiko RSAKey"""'
newline|'\n'
comment|'# NOTE(dims): pycryptodome has changed the signature of the RSA.generate'
nl|'\n'
comment|'# call. specifically progress_func has been dropped. paramiko still uses'
nl|'\n'
comment|'# pycrypto. However some projects like latest pysaml2 have switched from'
nl|'\n'
comment|'# pycrypto to pycryptodome as pycrypto seems to have been abandoned.'
nl|'\n'
comment|'# paramiko project has started transition to pycryptodome as well but'
nl|'\n'
comment|'# there is no release yet with that support. So at the moment depending on'
nl|'\n'
comment|'# which version of pysaml2 is installed, Nova is likely to break. So we'
nl|'\n'
comment|'# call "RSA.generate(bits)" which works on both pycrypto and pycryptodome'
nl|'\n'
comment|'# and then wrap it into a paramiko.RSAKey'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(coreywright): Paramiko 2 avoids this conundrum by migrating from'
nl|'\n'
comment|'# PyCrypto/PyCryptodome to cryptography.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# TODO(coreywright): When Paramiko constraint is upgraded to 2.x, then'
nl|'\n'
comment|'# remove this abstraction and replace the call to this function with a call'
nl|'\n'
comment|'# to `paramiko.RSAKey.generate(bits)`.'
nl|'\n'
nl|'\n'
name|'if'
name|'paramiko'
op|'.'
name|'__version_info__'
op|'['
number|'0'
op|']'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'        '
name|'key'
op|'='
name|'paramiko'
op|'.'
name|'RSAKey'
op|'.'
name|'generate'
op|'('
name|'bits'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
comment|'# paramiko 1.x'
newline|'\n'
indent|'        '
name|'from'
name|'Crypto'
op|'.'
name|'PublicKey'
name|'import'
name|'RSA'
newline|'\n'
name|'rsa'
op|'='
name|'RSA'
op|'.'
name|'generate'
op|'('
name|'bits'
op|')'
newline|'\n'
name|'key'
op|'='
name|'paramiko'
op|'.'
name|'RSAKey'
op|'('
name|'vals'
op|'='
op|'('
name|'rsa'
op|'.'
name|'e'
op|','
name|'rsa'
op|'.'
name|'n'
op|')'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'d'
op|'='
name|'rsa'
op|'.'
name|'d'
newline|'\n'
name|'key'
op|'.'
name|'p'
op|'='
name|'rsa'
op|'.'
name|'p'
newline|'\n'
name|'key'
op|'.'
name|'q'
op|'='
name|'rsa'
op|'.'
name|'q'
newline|'\n'
dedent|''
name|'return'
name|'key'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_key_pair
dedent|''
name|'def'
name|'generate_key_pair'
op|'('
name|'bits'
op|'='
number|'2048'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'key'
op|'='
name|'generate_key'
op|'('
name|'bits'
op|')'
newline|'\n'
name|'keyout'
op|'='
name|'six'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'key'
op|'.'
name|'write_private_key'
op|'('
name|'keyout'
op|')'
newline|'\n'
name|'private_key'
op|'='
name|'keyout'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'public_key'
op|'='
string|"'%s %s Generated-by-Nova'"
op|'%'
op|'('
name|'key'
op|'.'
name|'get_name'
op|'('
op|')'
op|','
name|'key'
op|'.'
name|'get_base64'
op|'('
op|')'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'generate_fingerprint'
op|'('
name|'public_key'
op|')'
newline|'\n'
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
name|'crypto'
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
name|'private_key_file'
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
name|'private_key_file'
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
name|'with'
name|'open'
op|'('
name|'private_key_file'
op|','
string|"'rb'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'priv_key'
op|'='
name|'serialization'
op|'.'
name|'load_pem_private_key'
op|'('
nl|'\n'
name|'data'
op|','
name|'None'
op|','
name|'backends'
op|'.'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'priv_key'
op|'.'
name|'decrypt'
op|'('
name|'text'
op|','
name|'padding'
op|'.'
name|'PKCS1v15'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|','
name|'exceptions'
op|'.'
name|'UnsupportedAlgorithm'
op|')'
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
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ssh_encrypt_text
dedent|''
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
string|'"""Encrypt text with an ssh public key.\n\n    If text is a Unicode string, encode it to UTF-8.\n    """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'text'
op|','
name|'six'
op|'.'
name|'text_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'text'
op|'='
name|'text'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pub_bytes'
op|'='
name|'ssh_public_key'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
name|'pub_key'
op|'='
name|'serialization'
op|'.'
name|'load_ssh_public_key'
op|'('
nl|'\n'
name|'pub_bytes'
op|','
name|'backends'
op|'.'
name|'default_backend'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'pub_key'
op|'.'
name|'encrypt'
op|'('
name|'text'
op|','
name|'padding'
op|'.'
name|'PKCS1v15'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'EncryptionFailure'
op|'('
name|'reason'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_cert
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
op|','
name|'cwd'
op|'='
name|'ca_folder'
op|'('
name|'project_id'
op|')'
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
name|'crypto'
op|'.'
name|'crl_file'
op|','
name|'cwd'
op|'='
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
name|'crypto'
op|'.'
name|'project_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'utils'
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
name|'crypto'
op|'.'
name|'user_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'user_id'
op|','
nl|'\n'
name|'utils'
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
name|'with'
name|'open'
op|'('
name|'keyfile'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'private_key'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'with'
name|'open'
op|'('
name|'csrfile'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'csr'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
DECL|function|generate_winrm_x509_cert
dedent|''
name|'def'
name|'generate_winrm_x509_cert'
op|'('
name|'user_id'
op|','
name|'bits'
op|'='
number|'2048'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate a cert for passwordless auth for user in project."""'
newline|'\n'
name|'subject'
op|'='
string|"'/CN=%s'"
op|'%'
name|'user_id'
newline|'\n'
name|'upn'
op|'='
string|"'%s@localhost'"
op|'%'
name|'user_id'
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
name|'conffile'
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
string|"'temp.conf'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'_create_x509_openssl_config'
op|'('
name|'conffile'
op|','
name|'upn'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'certificate'
op|','
name|'_err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'openssl'"
op|','
string|"'req'"
op|','
string|"'-x509'"
op|','
string|"'-nodes'"
op|','
string|"'-days'"
op|','
string|"'3650'"
op|','
nl|'\n'
string|"'-config'"
op|','
name|'conffile'
op|','
string|"'-newkey'"
op|','
string|"'rsa:%s'"
op|'%'
name|'bits'
op|','
nl|'\n'
string|"'-outform'"
op|','
string|"'PEM'"
op|','
string|"'-keyout'"
op|','
name|'keyfile'
op|','
string|"'-subj'"
op|','
name|'subject'
op|','
nl|'\n'
string|"'-extensions'"
op|','
string|"'v3_req_client'"
op|','
nl|'\n'
name|'binary'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'out'
op|','
name|'_err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'openssl'"
op|','
string|"'pkcs12'"
op|','
string|"'-export'"
op|','
nl|'\n'
string|"'-inkey'"
op|','
name|'keyfile'
op|','
string|"'-password'"
op|','
string|"'pass:'"
op|','
nl|'\n'
name|'process_input'
op|'='
name|'certificate'
op|','
nl|'\n'
name|'binary'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'private_key'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'out'
op|')'
newline|'\n'
name|'fingerprint'
op|'='
name|'generate_x509_fingerprint'
op|'('
name|'certificate'
op|')'
newline|'\n'
name|'if'
name|'six'
op|'.'
name|'PY3'
op|':'
newline|'\n'
indent|'            '
name|'private_key'
op|'='
name|'private_key'
op|'.'
name|'decode'
op|'('
string|"'ascii'"
op|')'
newline|'\n'
name|'certificate'
op|'='
name|'certificate'
op|'.'
name|'decode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'('
name|'private_key'
op|','
name|'certificate'
op|','
name|'fingerprint'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_x509_openssl_config
dedent|''
name|'def'
name|'_create_x509_openssl_config'
op|'('
name|'conffile'
op|','
name|'upn'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'content'
op|'='
op|'('
string|'"distinguished_name  = req_distinguished_name\\n"'
nl|'\n'
string|'"[req_distinguished_name]\\n"'
nl|'\n'
string|'"[v3_req_client]\\n"'
nl|'\n'
string|'"extendedKeyUsage = clientAuth\\n"'
nl|'\n'
string|'"subjectAltName = otherName:"'
string|'"1.3.6.1.4.1.311.20.2.3;UTF8:%s\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'conffile'
op|','
string|"'w'"
op|')'
name|'as'
name|'file'
op|':'
newline|'\n'
indent|'        '
name|'file'
op|'.'
name|'write'
op|'('
name|'content'
op|'%'
name|'upn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_ensure_project_folder
dedent|''
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
op|','
name|'cwd'
op|'='
name|'ca_folder'
op|'('
op|')'
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
name|'crypto'
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
name|'_LE'
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
op|','
name|'cwd'
op|'='
name|'ca_folder'
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
op|','
name|'cwd'
op|'='
name|'ca_folder'
op|')'
newline|'\n'
name|'serial'
op|'='
name|'out'
op|'.'
name|'rpartition'
op|'('
string|"'='"
op|')'
op|'['
number|'2'
op|']'
op|'.'
name|'strip'
op|'('
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
