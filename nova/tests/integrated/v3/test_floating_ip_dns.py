begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'api_sample_base'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIpDNSTest
name|'class'
name|'FloatingIpDNSTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-floating-ip-dns"'
newline|'\n'
nl|'\n'
DECL|variable|domain
name|'domain'
op|'='
string|"'domain1.example.org'"
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'instance1'"
newline|'\n'
DECL|variable|scope
name|'scope'
op|'='
string|"'public'"
newline|'\n'
DECL|variable|project
name|'project'
op|'='
string|"'project1'"
newline|'\n'
DECL|variable|dns_type
name|'dns_type'
op|'='
string|"'A'"
newline|'\n'
DECL|variable|ip
name|'ip'
op|'='
string|"'192.168.1.1'"
newline|'\n'
nl|'\n'
DECL|member|_create_or_update
name|'def'
name|'_create_or_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'self'
op|'.'
name|'project'
op|','
nl|'\n'
string|"'scope'"
op|':'
name|'self'
op|'.'
name|'scope'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-floating-ip-dns/%s'"
op|'%'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'floating-ip-dns-create-or-update-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ip-dns-create-or-update-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_or_update_entry
dedent|''
name|'def'
name|'_create_or_update_entry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
string|"'ip'"
op|':'
name|'self'
op|'.'
name|'ip'
op|','
string|"'dns_type'"
op|':'
name|'self'
op|'.'
name|'dns_type'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'os-floating-ip-dns/%s/entries/%s'"
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'name'
op|')'
op|','
nl|'\n'
string|"'floating-ip-dns-create-or-update-entry-req'"
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
op|'{'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|','
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ip-dns-create-or-update-entry-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_list
dedent|''
name|'def'
name|'test_floating_ip_dns_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ip-dns'"
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'self'
op|'.'
name|'project'
op|','
nl|'\n'
string|"'scope'"
op|':'
name|'self'
op|'.'
name|'scope'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ip-dns-list-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_create_or_update
dedent|''
name|'def'
name|'test_floating_ip_dns_create_or_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_delete
dedent|''
name|'def'
name|'test_floating_ip_dns_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-floating-ip-dns/%s'"
op|'%'
name|'self'
op|'.'
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_create_or_update_entry
dedent|''
name|'def'
name|'test_floating_ip_dns_create_or_update_entry'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update_entry'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_entry_get
dedent|''
name|'def'
name|'test_floating_ip_dns_entry_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update_entry'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ip-dns/%s/entries/%s'"
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'name'
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'ip'"
op|':'
name|'self'
op|'.'
name|'ip'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ip-dns-entry-get-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_entry_delete
dedent|''
name|'def'
name|'test_floating_ip_dns_entry_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update_entry'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'os-floating-ip-dns/%s/entries/%s'"
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'name'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_floating_ip_dns_entry_list
dedent|''
name|'def'
name|'test_floating_ip_dns_entry_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_or_update_entry'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-floating-ip-dns/%s/entries/%s'"
nl|'\n'
op|'%'
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'ip'
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'domain'"
op|':'
name|'self'
op|'.'
name|'domain'
op|','
nl|'\n'
string|"'ip'"
op|':'
name|'self'
op|'.'
name|'ip'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'name'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'floating-ip-dns-entry-list-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
