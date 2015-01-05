begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'mox3'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'webob'
name|'import'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'certificates'
name|'as'
name|'certificates_v2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'certificates'
name|'as'
name|'certificates_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cert'
name|'import'
name|'rpcapi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'policy'
name|'as'
name|'common_policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CertificatesTestV21
name|'class'
name|'CertificatesTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|certificates
indent|'    '
name|'certificates'
op|'='
name|'certificates_v21'
newline|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'/v3/os-certificates'"
newline|'\n'
DECL|variable|certificate_show_extension
name|'certificate_show_extension'
op|'='
string|"'compute_extension:v3:os-certificates:show'"
newline|'\n'
name|'certificate_create_extension'
op|'='
DECL|variable|certificate_create_extension
string|"'compute_extension:v3:os-certificates:create'"
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CertificatesTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'certificates'
op|'.'
name|'CertificatesController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_translate_certificate_view
dedent|''
name|'def'
name|'test_translate_certificate_view'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pk'
op|','
name|'cert'
op|'='
string|"'fakepk'"
op|','
string|"'fakecert'"
newline|'\n'
name|'view'
op|'='
name|'self'
op|'.'
name|'certificates'
op|'.'
name|'_translate_certificate_view'
op|'('
name|'cert'
op|','
name|'pk'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'data'"
op|']'
op|','
name|'cert'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'view'
op|'['
string|"'private_key'"
op|']'
op|','
name|'pk'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_certificates_show_root
dedent|''
name|'def'
name|'test_certificates_show_root'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cert_rpcapi'
op|','
string|"'fetch_ca'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cert_rpcapi'
op|'.'
name|'fetch_ca'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'project_id'
op|'='
string|"'fake'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'fakeroot'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/root'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'root'"
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
string|"'certificate'"
op|':'
op|'{'
string|"'data'"
op|':'
string|"'fakeroot'"
op|','
string|"'private_key'"
op|':'
name|'None'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_certificates_show_policy_failed
dedent|''
name|'def'
name|'test_certificates_show_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
nl|'\n'
name|'self'
op|'.'
name|'certificate_show_extension'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|'"!"'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/root'"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'req'
op|','
string|"'root'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'self'
op|'.'
name|'certificate_show_extension'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_certificates_create_certificate
dedent|''
name|'def'
name|'test_certificates_create_certificate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cert_rpcapi'
op|','
nl|'\n'
string|"'generate_x509_cert'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'cert_rpcapi'
op|'.'
name|'generate_x509_cert'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'user_id'
op|'='
string|"'fake_user'"
op|','
nl|'\n'
name|'project_id'
op|'='
string|"'fake'"
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
string|"'fakepk'"
op|','
string|"'fakecert'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
op|'{'
nl|'\n'
string|"'certificate'"
op|':'
op|'{'
string|"'data'"
op|':'
string|"'fakecert'"
op|','
nl|'\n'
string|"'private_key'"
op|':'
string|"'fakepk'"
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_certificates_create_policy_failed
dedent|''
name|'def'
name|'test_certificates_create_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rules'
op|'='
op|'{'
nl|'\n'
name|'self'
op|'.'
name|'certificate_create_extension'
op|':'
nl|'\n'
name|'common_policy'
op|'.'
name|'parse_rule'
op|'('
string|'"!"'
op|')'
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'set_rules'
op|'('
name|'rules'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'self'
op|'.'
name|'certificate_create_extension'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rpcapi'
op|'.'
name|'CertAPI'
op|','
string|"'fetch_ca'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'CryptoCAFileNotFound'
op|'('
name|'project'
op|'='
string|"'fake'"
op|')'
op|')'
newline|'\n'
DECL|member|test_non_exist_certificates_show
name|'def'
name|'test_non_exist_certificates_show'
op|'('
name|'self'
op|','
name|'mock_fetch_ca'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'self'
op|'.'
name|'url'
op|'+'
string|"'/root'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
string|"'root'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CertificatesTestV2
dedent|''
dedent|''
name|'class'
name|'CertificatesTestV2'
op|'('
name|'CertificatesTestV21'
op|')'
op|':'
newline|'\n'
DECL|variable|certificates
indent|'    '
name|'certificates'
op|'='
name|'certificates_v2'
newline|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'/v2/fake/os-certificates'"
newline|'\n'
DECL|variable|certificate_show_extension
name|'certificate_show_extension'
op|'='
string|"'compute_extension:certificates'"
newline|'\n'
DECL|variable|certificate_create_extension
name|'certificate_create_extension'
op|'='
string|"'compute_extension:certificates'"
dedent|''
endmarker|''
end_unit
