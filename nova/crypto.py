begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
string|'"""\nWrappers around standard crypto data elements.\n\nIncludes root and intermediate CAs, SSH key_pairs and x509 certificates.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'struct'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
name|'import'
name|'M2Crypto'
newline|'\n'
nl|'\n'
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|','
name|'unicode'
op|'='
number|'1'
op|')'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
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
string|'"nova.crypto"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ca_file'"
op|','
string|"'cacert.pem'"
op|','
name|'_'
op|'('
string|"'Filename of root CA'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'key_file'"
op|','
nl|'\n'
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
name|'_'
op|'('
string|"'Filename of private key'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'crl_file'"
op|','
string|"'crl.pem'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Filename of root Certificate Revokation List'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'keys_path'"
op|','
string|"'$state_path/keys'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Where we keep our keys'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ca_path'"
op|','
string|"'$state_path/CA'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Where we keep our root CA'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'use_project_ca'"
op|','
name|'False'
op|','
nl|'\n'
name|'_'
op|'('
string|"'Should we use a CA for each project?'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'user_cert_subject'"
op|','
nl|'\n'
string|"'/C=US/ST=California/L=MountainView/O=AnsoLabs/'"
nl|'\n'
string|"'OU=NovaDev/CN=%s-%s-%s'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Subject for certificate for users, '"
nl|'\n'
string|"'%s for project, user, timestamp'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'project_cert_subject'"
op|','
nl|'\n'
string|"'/C=US/ST=California/L=MountainView/O=AnsoLabs/'"
nl|'\n'
string|"'OU=NovaDev/CN=project-ca-%s-%s'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Subject for certificate for projects, '"
nl|'\n'
string|"'%s for project, timestamp'"
op|')'
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vpn_cert_subject'"
op|','
nl|'\n'
string|"'/C=US/ST=California/L=MountainView/O=AnsoLabs/'"
nl|'\n'
string|"'OU=NovaDev/CN=project-vpn-%s-%s'"
op|','
nl|'\n'
name|'_'
op|'('
string|"'Subject for certificate for vpns, '"
nl|'\n'
string|"'%s for project, timestamp'"
op|')'
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
name|'FLAGS'
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
name|'FLAGS'
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
name|'FLAGS'
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
name|'FLAGS'
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
name|'FLAGS'
op|'.'
name|'key_file'
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
op|','
name|'chain'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'FLAGS'
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
name|'buffer'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'project_id'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'ca_path'
op|'('
name|'project_id'
op|')'
op|','
string|'"r"'
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'            '
name|'buffer'
op|'+='
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'chain'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'buffer'
newline|'\n'
dedent|''
dedent|''
name|'with'
name|'open'
op|'('
name|'ca_path'
op|'('
name|'None'
op|')'
op|','
string|'"r"'
op|')'
name|'as'
name|'cafile'
op|':'
newline|'\n'
indent|'        '
name|'buffer'
op|'+='
name|'cafile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'buffer'
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
number|'1024'
op|')'
op|':'
newline|'\n'
comment|'# what is the magic 65537?'
nl|'\n'
nl|'\n'
indent|'    '
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
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
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ssh-keygen'"
op|','
string|"'-q'"
op|','
string|"'-b'"
op|','
string|'"%d"'
op|'%'
name|'bits'
op|','
string|"'-N'"
op|','
string|'\'""\''
op|','
string|"'-f'"
op|','
name|'keyfile'
op|')'
newline|'\n'
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
string|'"%s.pub"'
op|'%'
op|'('
name|'keyfile'
op|')'
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
name|'public_key'
op|'='
name|'open'
op|'('
name|'keyfile'
op|'+'
string|"'.pub'"
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
comment|'# code below returns public key in pem format'
nl|'\n'
comment|'# key = M2Crypto.RSA.gen_key(bits, 65537, callback=lambda: None)'
nl|'\n'
comment|'# private_key = key.as_pem(cipher=None)'
nl|'\n'
comment|'# bio = M2Crypto.BIO.MemoryBuffer()'
nl|'\n'
comment|'# key.save_pub_key_bio(bio)'
nl|'\n'
comment|'# public_key = bio.read()'
nl|'\n'
comment|"# public_key, err = execute('ssh-keygen','-y','-f','/dev/stdin', private_key)"
nl|'\n'
nl|'\n'
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
DECL|function|ssl_pub_to_ssh_pub
dedent|''
name|'def'
name|'ssl_pub_to_ssh_pub'
op|'('
name|'ssl_public_key'
op|','
name|'name'
op|'='
string|"'root'"
op|','
name|'suffix'
op|'='
string|"'nova'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'buf'
op|'='
name|'M2Crypto'
op|'.'
name|'BIO'
op|'.'
name|'MemoryBuffer'
op|'('
name|'ssl_public_key'
op|')'
newline|'\n'
name|'rsa_key'
op|'='
name|'M2Crypto'
op|'.'
name|'RSA'
op|'.'
name|'load_pub_key_bio'
op|'('
name|'buf'
op|')'
newline|'\n'
name|'e'
op|','
name|'n'
op|'='
name|'rsa_key'
op|'.'
name|'pub'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'key_type'
op|'='
string|"'ssh-rsa'"
newline|'\n'
nl|'\n'
name|'key_data'
op|'='
name|'struct'
op|'.'
name|'pack'
op|'('
string|"'>I'"
op|','
name|'len'
op|'('
name|'key_type'
op|')'
op|')'
newline|'\n'
name|'key_data'
op|'+='
name|'key_type'
newline|'\n'
name|'key_data'
op|'+='
string|"'%s%s'"
op|'%'
op|'('
name|'e'
op|','
name|'n'
op|')'
newline|'\n'
nl|'\n'
name|'b64_blob'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'key_data'
op|')'
newline|'\n'
name|'return'
string|"'%s %s %s@%s\\n'"
op|'%'
op|'('
name|'key_type'
op|','
name|'b64_blob'
op|','
name|'name'
op|','
name|'suffix'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|revoke_cert
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
string|'"""Revoke a cert by file name"""'
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
name|'project_id'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(vish): potential race condition here'
nl|'\n'
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
string|'"\'%s\'"'
op|'%'
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
string|"'-out'"
op|','
string|'"\'%s\'"'
op|'%'
nl|'\n'
name|'FLAGS'
op|'.'
name|'crl_file'
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
DECL|function|revoke_certs_by_user
dedent|''
name|'def'
name|'revoke_certs_by_user'
op|'('
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Revoke all user certs"""'
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
string|'"""Revoke all project certs"""'
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
string|'"""Revoke certs for user in project"""'
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
string|'"""Helper to generate user cert subject"""'
newline|'\n'
name|'return'
name|'FLAGS'
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
DECL|function|_vpn_cert_subject
dedent|''
name|'def'
name|'_vpn_cert_subject'
op|'('
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Helper to generate user cert subject"""'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'vpn_cert_subject'
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
string|'"""Helper to generate user cert subject"""'
newline|'\n'
name|'return'
name|'FLAGS'
op|'.'
name|'user_cert_subject'
op|'%'
op|'('
name|'project_id'
op|','
name|'user_id'
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
number|'1024'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate and sign a cert for user in project"""'
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
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
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
name|'join'
op|'('
name|'tmpdir'
op|','
string|"'temp.csr'"
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
name|'bits'
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
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'tmpdir'
op|')'
newline|'\n'
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
string|'"newcerts/%s.pem"'
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
string|"'geninter.sh'"
op|','
name|'project_id'
op|','
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
name|'csr_fn'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'project_folder'
op|','
string|'"server.csr"'
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
string|'"server.crt"'
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
dedent|''
name|'_ensure_project_folder'
op|'('
name|'project_id'
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
comment|'# TODO(vish): the shell scripts could all be done in python'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sh'"
op|','
string|"'genvpn.sh'"
op|','
nl|'\n'
name|'project_id'
op|','
name|'_vpn_cert_subject'
op|'('
name|'project_id'
op|')'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'csr_fn'
op|','
string|'"r"'
op|')'
name|'as'
name|'csrfile'
op|':'
newline|'\n'
indent|'        '
name|'csr_text'
op|'='
name|'csrfile'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
op|'('
name|'serial'
op|','
name|'signed_csr'
op|')'
op|'='
name|'sign_csr'
op|'('
name|'csr_text'
op|','
name|'project_id'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'crt_fn'
op|','
string|'"w"'
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
name|'signed_csr'
op|')'
newline|'\n'
dedent|''
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|sign_csr
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
name|'FLAGS'
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
name|'project_folder'
op|'='
name|'ca_folder'
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
name|'tmpfolder'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'inbound'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'tmpfolder'
op|','
string|'"inbound.csr"'
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
name|'tmpfolder'
op|','
string|'"outbound.csr"'
op|')'
newline|'\n'
name|'csrfile'
op|'='
name|'open'
op|'('
name|'inbound'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'csrfile'
op|'.'
name|'write'
op|'('
name|'csr_text'
op|')'
newline|'\n'
name|'csrfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Flags path: %s"'
op|')'
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
comment|'# Change working dir to CA'
nl|'\n'
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
string|"','"
op|'-'
name|'serial'
string|"','"
op|'-'
name|'noout'
errortoken|"'"
op|')'
newline|'\n'
name|'serial'
op|'='
name|'out'
op|'.'
name|'rpartition'
op|'('
string|'"="'
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
name|'os'
op|'.'
name|'chdir'
op|'('
name|'start'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'outbound'
op|','
string|'"r"'
op|')'
name|'as'
name|'crtfile'
op|':'
newline|'\n'
indent|'        '
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
nl|'\n'
nl|'\n'
DECL|function|mkreq
dedent|''
dedent|''
name|'def'
name|'mkreq'
op|'('
name|'bits'
op|','
name|'subject'
op|'='
string|'"foo"'
op|','
name|'ca'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pk'
op|'='
name|'M2Crypto'
op|'.'
name|'EVP'
op|'.'
name|'PKey'
op|'('
op|')'
newline|'\n'
name|'req'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'Request'
op|'('
op|')'
newline|'\n'
name|'rsa'
op|'='
name|'M2Crypto'
op|'.'
name|'RSA'
op|'.'
name|'gen_key'
op|'('
name|'bits'
op|','
number|'65537'
op|','
name|'callback'
op|'='
name|'lambda'
op|':'
name|'None'
op|')'
newline|'\n'
name|'pk'
op|'.'
name|'assign_rsa'
op|'('
name|'rsa'
op|')'
newline|'\n'
name|'rsa'
op|'='
name|'None'
comment|'# should not be freed here'
newline|'\n'
name|'req'
op|'.'
name|'set_pubkey'
op|'('
name|'pk'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'set_subject'
op|'('
name|'subject'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'sign'
op|'('
name|'pk'
op|','
string|"'sha512'"
op|')'
newline|'\n'
name|'assert'
name|'req'
op|'.'
name|'verify'
op|'('
name|'pk'
op|')'
newline|'\n'
name|'pk2'
op|'='
name|'req'
op|'.'
name|'get_pubkey'
op|'('
op|')'
newline|'\n'
name|'assert'
name|'req'
op|'.'
name|'verify'
op|'('
name|'pk2'
op|')'
newline|'\n'
name|'return'
name|'req'
op|','
name|'pk'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkcacert
dedent|''
name|'def'
name|'mkcacert'
op|'('
name|'subject'
op|'='
string|"'nova'"
op|','
name|'years'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'req'
op|','
name|'pk'
op|'='
name|'mkreq'
op|'('
number|'2048'
op|','
name|'subject'
op|','
name|'ca'
op|'='
number|'1'
op|')'
newline|'\n'
name|'pkey'
op|'='
name|'req'
op|'.'
name|'get_pubkey'
op|'('
op|')'
newline|'\n'
name|'sub'
op|'='
name|'req'
op|'.'
name|'get_subject'
op|'('
op|')'
newline|'\n'
name|'cert'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'X509'
op|'('
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_serial_number'
op|'('
number|'1'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_version'
op|'('
number|'2'
op|')'
newline|'\n'
comment|'# FIXME subject is not set in mkreq yet'
nl|'\n'
name|'cert'
op|'.'
name|'set_subject'
op|'('
name|'sub'
op|')'
newline|'\n'
name|'t'
op|'='
name|'long'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|'+'
name|'time'
op|'.'
name|'timezone'
newline|'\n'
name|'now'
op|'='
name|'M2Crypto'
op|'.'
name|'ASN1'
op|'.'
name|'ASN1_UTCTIME'
op|'('
op|')'
newline|'\n'
name|'now'
op|'.'
name|'set_time'
op|'('
name|'t'
op|')'
newline|'\n'
name|'nowPlusYear'
op|'='
name|'M2Crypto'
op|'.'
name|'ASN1'
op|'.'
name|'ASN1_UTCTIME'
op|'('
op|')'
newline|'\n'
name|'nowPlusYear'
op|'.'
name|'set_time'
op|'('
name|'t'
op|'+'
op|'('
name|'years'
op|'*'
number|'60'
op|'*'
number|'60'
op|'*'
number|'24'
op|'*'
number|'365'
op|')'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_not_before'
op|'('
name|'now'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_not_after'
op|'('
name|'nowPlusYear'
op|')'
newline|'\n'
name|'issuer'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'X509_Name'
op|'('
op|')'
newline|'\n'
name|'issuer'
op|'.'
name|'C'
op|'='
string|'"US"'
newline|'\n'
name|'issuer'
op|'.'
name|'CN'
op|'='
name|'subject'
newline|'\n'
name|'cert'
op|'.'
name|'set_issuer'
op|'('
name|'issuer'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'set_pubkey'
op|'('
name|'pkey'
op|')'
newline|'\n'
name|'ext'
op|'='
name|'M2Crypto'
op|'.'
name|'X509'
op|'.'
name|'new_extension'
op|'('
string|"'basicConstraints'"
op|','
string|"'CA:TRUE'"
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'add_ext'
op|'('
name|'ext'
op|')'
newline|'\n'
name|'cert'
op|'.'
name|'sign'
op|'('
name|'pk'
op|','
string|"'sha512'"
op|')'
newline|'\n'
nl|'\n'
comment|"# print 'cert', dir(cert)"
nl|'\n'
name|'print'
name|'cert'
op|'.'
name|'as_pem'
op|'('
op|')'
newline|'\n'
name|'print'
name|'pk'
op|'.'
name|'get_rsa'
op|'('
op|')'
op|'.'
name|'as_pem'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'cert'
op|','
name|'pk'
op|','
name|'pkey'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
comment|'# http://code.google.com/p/boto'
nl|'\n'
nl|'\n'
DECL|function|compute_md5
dedent|''
name|'def'
name|'compute_md5'
op|'('
name|'fp'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    :type fp: file\n    :param fp: File pointer to the file to MD5 hash.  The file pointer will be\n               reset to the beginning of the file before the method returns.\n\n    :rtype: tuple\n    :return: the hex digest version of the MD5 hash\n    """'
newline|'\n'
name|'m'
op|'='
name|'hashlib'
op|'.'
name|'md5'
op|'('
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'s'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
name|'while'
name|'s'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'.'
name|'update'
op|'('
name|'s'
op|')'
newline|'\n'
name|'s'
op|'='
name|'fp'
op|'.'
name|'read'
op|'('
number|'8192'
op|')'
newline|'\n'
dedent|''
name|'hex_md5'
op|'='
name|'m'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
comment|'# size = fp.tell()'
nl|'\n'
name|'fp'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'return'
name|'hex_md5'
newline|'\n'
dedent|''
endmarker|''
end_unit
