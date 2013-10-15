begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpcclient'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_opts
name|'rpcapi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cert'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'the topic cert nodes listen on'"
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
name|'rpcapi_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cert'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to cert services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CertAPI
name|'class'
name|'CertAPI'
op|'('
name|'rpcclient'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the cert rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Added get_backdoor_port()\n\n        ... Grizzly and Havana support message version 1.1.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.1.\n\n        2.0 - Major API rev for Icehouse\n    '''"
newline|'\n'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# NOTE(russellb): This is the default minimum version that the server'
nl|'\n'
comment|'# (manager) side must implement unless otherwise specified using a version'
nl|'\n'
comment|'# argument to self.call()/cast()/etc. here.  It should be left as X.0 where'
nl|'\n'
comment|'# X is the current major API version (1.0, 2.0, ...).  For more information'
nl|'\n'
comment|'# about rpc API versioning, see the docs in'
nl|'\n'
comment|'# openstack/common/rpc/dispatcher.py.'
nl|'\n'
comment|'#'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'2.0'"
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
name|'super'
op|'('
name|'CertAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'cert_topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'self'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_compat_version
dedent|''
name|'def'
name|'_get_compat_version'
op|'('
name|'self'
op|','
name|'current'
op|','
name|'havana_compat'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'can_send_version'
op|'('
name|'current'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'havana_compat'
newline|'\n'
dedent|''
name|'return'
name|'current'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
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
