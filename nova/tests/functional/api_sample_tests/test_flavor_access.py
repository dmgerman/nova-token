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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
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
name|'import_opt'
op|'('
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorAccessSampleJsonTests
name|'class'
name|'FlavorAccessSampleJsonTests'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV21'
op|')'
op|':'
newline|'\n'
DECL|variable|ADMIN_API
indent|'    '
name|'ADMIN_API'
op|'='
name|'True'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
string|"'flavor-access'"
newline|'\n'
nl|'\n'
DECL|member|_get_flags
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'super'
op|'('
name|'FlavorAccessSampleJsonTests'
op|','
name|'self'
op|')'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'osapi_compute_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'flavor_access.Flavor_access'"
op|')'
newline|'\n'
comment|'# FlavorAccess extension also needs Flavormanage to be loaded.'
nl|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'flavormanage.Flavormanage'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'flavor_disabled.Flavor_disabled'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'flavorextradata.Flavorextradata'"
op|')'
newline|'\n'
name|'f'
op|'['
string|"'osapi_compute_extension'"
op|']'
op|'.'
name|'append'
op|'('
nl|'\n'
string|"'nova.api.openstack.compute.contrib.'"
nl|'\n'
string|"'flavor_swap.Flavor_swap'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_add_tenant
dedent|''
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
string|"'10'"
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
string|"'10'"
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
comment|'# TODO(sdague): remove tests that are duplicative'
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
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-access-detail-resp'"
op|','
op|'{'
op|'}'
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
string|"'10'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors/%s/os-flavor-access'"
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
string|"'1'"
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
dedent|''
dedent|''
endmarker|''
end_unit
