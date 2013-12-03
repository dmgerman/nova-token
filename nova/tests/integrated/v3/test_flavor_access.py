begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
DECL|class|FlavorAccessSampleJsonTests
name|'class'
name|'FlavorAccessSampleJsonTests'
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
string|"'flavor-access'"
newline|'\n'
nl|'\n'
DECL|member|_add_tenant
name|'def'
name|'_add_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'fake_tenant'"
op|','
nl|'\n'
string|"'flavor_id'"
op|':'
number|'10'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'flavors/10/action'"
op|','
nl|'\n'
string|"'flavor-access-add-tenant-req'"
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-add-tenant-resp'"
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
DECL|member|_create_flavor
dedent|''
name|'def'
name|'_create_flavor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'flavor_id'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'flavor_name'"
op|':'
string|"'test_flavor'"
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|'"flavors"'
op|','
nl|'\n'
string|'"flavor-access-create-req"'
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|'"flavor-access-create-resp"'
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_create
dedent|''
name|'def'
name|'test_flavor_access_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_flavor'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_detail
dedent|''
name|'def'
name|'test_flavor_access_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-detail-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_list
dedent|''
name|'def'
name|'test_flavor_access_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_flavor'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_tenant'
op|'('
op|')'
newline|'\n'
name|'flavor_id'
op|'='
number|'10'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors/%s/flavor-access'"
op|'%'
name|'flavor_id'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'flavor_id'"
op|':'
name|'flavor_id'
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'fake_tenant'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_show
dedent|''
name|'def'
name|'test_flavor_access_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor_id'
op|'='
number|'1'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors/%s'"
op|'%'
name|'flavor_id'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'flavor_id'"
op|':'
name|'flavor_id'
nl|'\n'
op|'}'
newline|'\n'
name|'subs'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-show-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_add_tenant
dedent|''
name|'def'
name|'test_flavor_access_add_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_flavor'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_tenant'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_access_remove_tenant
dedent|''
name|'def'
name|'test_flavor_access_remove_tenant'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_flavor'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_tenant'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'fake_tenant'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'flavors/10/action'"
op|','
nl|'\n'
string|'"flavor-access-remove-tenant-req"'
op|','
nl|'\n'
name|'subs'
op|')'
newline|'\n'
name|'exp_subs'
op|'='
op|'{'
nl|'\n'
string|'"tenant_id"'
op|':'
name|'self'
op|'.'
name|'api'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|'"flavor_id"'
op|':'
string|'"10"'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-remove-tenant-resp'"
op|','
nl|'\n'
name|'exp_subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccessSampleXmlTests
dedent|''
dedent|''
name|'class'
name|'FlavorAccessSampleXmlTests'
op|'('
name|'FlavorAccessSampleJsonTests'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
dedent|''
endmarker|''
end_unit
