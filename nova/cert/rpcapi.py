begin_unit
comment|'# Copyright 2013, Red Hat, Inc.'
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
string|'"""\nClient side of the cert manager RPC API.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
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
name|'rpc'
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
DECL|class|CertAPI
name|'class'
name|'CertAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the cert rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Added get_backdoor_port()\n\n        ... Grizzly and Havana support message version 1.1.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.1.\n\n        2.0 - Major API rev for Icehouse\n\n        ... Icehouse, Juno, Kilo, and Liberty support message version\n        2.0.  So, any changes to existing methods in 2.x after that\n        point should be done such that they can handle the version_cap\n        being set to 2.0.\n\n    '''"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'havana'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'icehouse'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
string|"'juno'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
string|"'kilo'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
string|"'liberty'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CertAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'cert_topic'
op|','
name|'version'
op|'='
string|"'2.0'"
op|')'
newline|'\n'
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'cert'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'cert'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|'='
name|'version_cap'
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
name|'ctxt'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'revoke_certs_by_user'"
op|','
name|'user_id'
op|'='
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
name|'ctxt'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'revoke_certs_by_project'"
op|','
nl|'\n'
name|'project_id'
op|'='
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
name|'ctxt'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'revoke_certs_by_user_and_project'"
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|','
name|'project_id'
op|'='
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
name|'ctxt'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'generate_x509_cert'"
op|','
nl|'\n'
name|'user_id'
op|'='
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|'='
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
name|'ctxt'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'fetch_ca'"
op|','
name|'project_id'
op|'='
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
name|'ctxt'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'fetch_crl'"
op|','
name|'project_id'
op|'='
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
name|'ctxt'
op|','
name|'project_id'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
string|"'decrypt_text'"
op|','
nl|'\n'
name|'project_id'
op|'='
name|'project_id'
op|','
nl|'\n'
name|'text'
op|'='
name|'text'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
