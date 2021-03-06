begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'access_ips'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
name|'as'
name|'servers_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPsExtTestV21
name|'class'
name|'AccessIPsExtTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'AccessIPsExtTestV21'
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
name|'access_ips_ext'
op|'='
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test
dedent|''
name|'def'
name|'_test'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'fe80::'"
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v4'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fe80::'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv4_only
dedent|''
name|'def'
name|'_test_with_ipv4_only'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'1.1.1.1'"
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v4'"
op|':'
string|"'1.1.1.1'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv6_only
dedent|''
name|'def'
name|'_test_with_ipv6_only'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'fe80::'"
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v6'"
op|':'
string|"'fe80::'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_without_ipv4_and_ipv6
dedent|''
name|'def'
name|'_test_without_ipv4_and_ipv6'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv4_null
dedent|''
name|'def'
name|'_test_with_ipv4_null'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
name|'None'
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v4'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv6_null
dedent|''
name|'def'
name|'_test_with_ipv6_null'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
name|'None'
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v6'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv4_blank
dedent|''
name|'def'
name|'_test_with_ipv4_blank'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"''"
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v4'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_ipv6_blank
dedent|''
name|'def'
name|'_test_with_ipv6_blank'
op|'('
name|'self'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server_dict'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"''"
op|'}'
newline|'\n'
name|'create_kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'func'
op|'('
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'create_kwargs'
op|','
op|'{'
string|"'access_ip_v6'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create
dedent|''
name|'def'
name|'test_server_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv4_only
dedent|''
name|'def'
name|'test_server_create_with_ipv4_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv6_only
dedent|''
name|'def'
name|'test_server_create_with_ipv6_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_without_ipv4_and_ipv6
dedent|''
name|'def'
name|'test_server_create_without_ipv4_and_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_ipv4_and_ipv6'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv4_null
dedent|''
name|'def'
name|'test_server_create_with_ipv4_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv6_null
dedent|''
name|'def'
name|'test_server_create_with_ipv6_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv4_blank
dedent|''
name|'def'
name|'test_server_create_with_ipv4_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_create_with_ipv6_blank
dedent|''
name|'def'
name|'test_server_create_with_ipv6_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update
dedent|''
name|'def'
name|'test_server_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv4_only
dedent|''
name|'def'
name|'test_server_update_with_ipv4_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv6_only
dedent|''
name|'def'
name|'test_server_update_with_ipv6_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_without_ipv4_and_ipv6
dedent|''
name|'def'
name|'test_server_update_without_ipv4_and_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_ipv4_and_ipv6'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv4_null
dedent|''
name|'def'
name|'test_server_update_with_ipv4_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv6_null
dedent|''
name|'def'
name|'test_server_update_with_ipv6_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv4_blank
dedent|''
name|'def'
name|'test_server_update_with_ipv4_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_update_with_ipv6_blank
dedent|''
name|'def'
name|'test_server_update_with_ipv6_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild
dedent|''
name|'def'
name|'test_server_rebuild'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv4_only
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv4_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv6_only
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv6_only'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_only'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_without_ipv4_and_ipv6
dedent|''
name|'def'
name|'test_server_rebuild_without_ipv4_and_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_ipv4_and_ipv6'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv4_null
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv4_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv6_null
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv6_null'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_null'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv4_blank
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv4_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv4_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_server_rebuild_with_ipv6_blank
dedent|''
name|'def'
name|'test_server_rebuild_with_ipv6_blank'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_ipv6_blank'
op|'('
name|'self'
op|'.'
name|'access_ips_ext'
op|'.'
name|'server_rebuild'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPsExtAPIValidationTestV21
dedent|''
dedent|''
name|'class'
name|'AccessIPsExtAPIValidationTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
name|'AccessIPsExtAPIValidationTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_save
name|'def'
name|'fake_save'
op|'('
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_rebuild
dedent|''
name|'def'
name|'fake_rebuild'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_set_up_controller'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_get_by_uuid'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_instance_get'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.objects.instance.Instance.save'"
op|','
name|'fake_save'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.compute.api.API.rebuild'"
op|','
name|'fake_rebuild'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_up_controller
dedent|''
name|'def'
name|'_set_up_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note(gmann): V2.1 has Access IP as separate extension. This class tests'
nl|'\n'
comment|'# calls controller directly so Access IPs will not be present in server'
nl|'\n'
comment|'# response. Those are being tested in AccessIPsExtTest class.'
nl|'\n'
DECL|member|_verify_update_access_ip
dedent|''
name|'def'
name|'_verify_update_access_ip'
op|'('
name|'self'
op|','
name|'res_dict'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_test_create
dedent|''
name|'def'
name|'_test_create'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'http://localhost/123/flavors/3'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'update'
op|'('
name|'params'
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
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'return'
name|'res_dict'
newline|'\n'
nl|'\n'
DECL|member|_test_update
dedent|''
name|'def'
name|'_test_update'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'server'"
op|']'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_update_access_ip'
op|'('
name|'res_dict'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_rebuild
dedent|''
name|'def'
name|'_test_rebuild'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'rebuild'"
op|':'
op|'{'
nl|'\n'
string|"'imageRef'"
op|':'
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'rebuild'"
op|']'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_action_rebuild'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_access_ipv4
dedent|''
name|'def'
name|'test_create_server_with_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'192.168.0.10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_access_ip_pass_disabled
dedent|''
name|'def'
name|'test_create_server_with_access_ip_pass_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# test with admin passwords disabled See lp bug 921814'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_instance_password'
op|'='
name|'False'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'192.168.0.10'"
op|','
nl|'\n'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'2001:db8::9abc'"
op|'}'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'res'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"admin_password"'
op|','
name|'server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_invalid_access_ipv4
dedent|''
name|'def'
name|'test_create_server_with_invalid_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'1.1.1.1.1.1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_access_ipv6
dedent|''
name|'def'
name|'test_create_server_with_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'2001:db8::9abc'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_create'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_invalid_access_ipv6
dedent|''
name|'def'
name|'test_create_server_with_invalid_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'fe80:::::::'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_create'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server_with_access_ipv4
dedent|''
name|'def'
name|'test_update_server_with_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'192.168.0.10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_update'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server_with_invalid_access_ipv4
dedent|''
name|'def'
name|'test_update_server_with_invalid_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'1.1.1.1.1.1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_update'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server_with_access_ipv6
dedent|''
name|'def'
name|'test_update_server_with_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'2001:db8::9abc'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_update'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server_with_invalid_access_ipv6
dedent|''
name|'def'
name|'test_update_server_with_invalid_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'fe80:::::::'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_update'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_server_with_access_ipv4
dedent|''
name|'def'
name|'test_rebuild_server_with_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'192.168.0.10'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_rebuild'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_server_with_invalid_access_ipv4
dedent|''
name|'def'
name|'test_rebuild_server_with_invalid_access_ipv4'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|':'
string|"'1.1.1.1.1.1'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_rebuild'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_server_with_access_ipv6
dedent|''
name|'def'
name|'test_rebuild_server_with_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'2001:db8::9abc'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_rebuild'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_server_with_invalid_access_ipv6
dedent|''
name|'def'
name|'test_rebuild_server_with_invalid_access_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|':'
string|"'fe80:::::::'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
name|'self'
op|'.'
name|'_test_rebuild'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AccessIPsControllerTestV21
dedent|''
dedent|''
name|'class'
name|'AccessIPsControllerTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'AccessIPsControllerTestV21'
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
name|'controller'
op|'='
name|'access_ips'
op|'.'
name|'AccessIPsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_with_access_ips
dedent|''
name|'def'
name|'_test_with_access_ips'
op|'('
name|'self'
op|','
name|'func'
op|','
name|'kwargs'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'('
op|'{'
string|"'nova.context'"
op|':'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fe80::'"
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
nl|'\n'
op|'{'
string|'"server"'
op|':'
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|'}'
op|')'
newline|'\n'
name|'func'
op|'('
name|'req'
op|','
name|'resp_obj'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
nl|'\n'
string|"'1.1.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
nl|'\n'
string|"'fe80::'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_without_access_ips
dedent|''
name|'def'
name|'_test_without_access_ips'
op|'('
name|'self'
op|','
name|'func'
op|','
name|'kwargs'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'('
op|'{'
string|"'nova.context'"
op|':'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
nl|'\n'
op|'{'
string|'"server"'
op|':'
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|'}'
op|'}'
op|')'
newline|'\n'
name|'func'
op|'('
name|'req'
op|','
name|'resp_obj'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
nl|'\n'
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
nl|'\n'
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_without_access_ips
dedent|''
name|'def'
name|'test_show_without_access_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'('
op|'{'
string|"'nova.context'"
op|':'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
op|'}'
op|')'
newline|'\n'
name|'instance1'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake1'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fe80::'"
op|'}'
newline|'\n'
name|'instance2'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake2'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.1.1.2'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fe81::'"
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance1'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance2'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
nl|'\n'
op|'{'
string|'"servers"'
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'fake1'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake2'"
op|'}'
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'resp_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
nl|'\n'
string|"'1.1.1.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
nl|'\n'
string|"'fe80::'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'1'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
nl|'\n'
string|"'1.1.1.2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'1'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
nl|'\n'
string|"'fe81::'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_without_access_ips
dedent|''
name|'def'
name|'test_detail_without_access_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'('
op|'{'
string|"'nova.context'"
op|':'
nl|'\n'
name|'fakes'
op|'.'
name|'FakeRequestContext'
op|'('
string|"'fake_user'"
op|','
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
op|'}'
op|')'
newline|'\n'
name|'instance1'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake1'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'instance2'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake2'"
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance1'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_instance'
op|'('
name|'instance2'
op|')'
newline|'\n'
name|'resp_obj'
op|'='
name|'wsgi'
op|'.'
name|'ResponseObject'
op|'('
nl|'\n'
op|'{'
string|'"servers"'
op|':'
op|'['
op|'{'
string|"'id'"
op|':'
string|"'fake1'"
op|'}'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake2'"
op|'}'
op|']'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'resp_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'0'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'1'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v4_key'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'resp_obj'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'1'
op|']'
op|'['
name|'access_ips'
op|'.'
name|'AccessIPs'
op|'.'
name|'v6_key'
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'body'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_without_access_ips
dedent|''
name|'def'
name|'test_update_without_access_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'body'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild
dedent|''
name|'def'
name|'test_rebuild'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_with_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'rebuild'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'body'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_without_access_ips
dedent|''
name|'def'
name|'test_rebuild_without_access_ips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_without_access_ips'
op|'('
name|'self'
op|'.'
name|'controller'
op|'.'
name|'rebuild'
op|','
op|'{'
string|"'id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'body'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
