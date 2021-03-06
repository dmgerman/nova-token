begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
string|'"""\nCert manager manages x509 certificates.\n\n**Related Flags**\n\n:cert_topic:  What :mod:`rpc` topic to listen to (default: `cert`).\n:cert_manager:  The module name of a class derived from\n                :class:`manager.Manager` (default:\n                :class:`nova.cert.manager.Manager`).\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
nl|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CertManager
name|'class'
name|'CertManager'
op|'('
name|'manager'
op|'.'
name|'Manager'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|target
indent|'    '
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'version'
op|'='
string|"'2.0'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CertManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'cert'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'crypto'
op|'.'
name|'ensure_ca_filesystem'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|revoke_certs_by_user
dedent|''
name|'def'
name|'revoke_certs_by_user'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Revoke all user certs."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'revoke_certs_by_user'
op|'('
name|'user_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|revoke_certs_by_project
dedent|''
name|'def'
name|'revoke_certs_by_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Revoke all project certs."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'revoke_certs_by_project'
op|'('
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|revoke_certs_by_user_and_project
dedent|''
name|'def'
name|'revoke_certs_by_user_and_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Revoke certs for user in project."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'revoke_certs_by_user_and_project'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|generate_x509_cert
dedent|''
name|'def'
name|'generate_x509_cert'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generate and sign a cert for user in project."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'generate_x509_cert'
op|'('
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_ca
dedent|''
name|'def'
name|'fetch_ca'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get root ca for a project."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'fetch_ca'
op|'('
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_crl
dedent|''
name|'def'
name|'fetch_crl'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get crl for a project."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'fetch_crl'
op|'('
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|decrypt_text
dedent|''
name|'def'
name|'decrypt_text'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Decrypt base64 encoded text using the projects private key."""'
newline|'\n'
name|'return'
name|'crypto'
op|'.'
name|'decrypt_text'
op|'('
name|'project_id'
op|','
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'text'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
