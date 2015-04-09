begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'manager'
name|'as'
name|'compute_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'servicegroup'
name|'import'
name|'api'
name|'as'
name|'service_group_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'v3'
name|'import'
name|'test_servers'
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
string|"'nova.api.openstack.compute.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EvacuateJsonTest
name|'class'
name|'EvacuateJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
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
string|'"os-evacuate"'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-access-ips"'
op|']'
newline|'\n'
DECL|variable|_api_version
name|'_api_version'
op|'='
string|"'v2'"
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
name|'EvacuateJsonTest'
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
string|"'nova.api.openstack.compute.contrib.evacuate.Evacuate'"
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
string|"'nova.api.openstack.compute.contrib.extended_evacuate_find_host.'"
nl|'\n'
string|"'Extended_evacuate_find_host'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_test_evacuate
dedent|''
name|'def'
name|'_test_evacuate'
op|'('
name|'self'
op|','
name|'req_subs'
op|','
name|'server_req'
op|','
name|'server_resp'
op|','
nl|'\n'
name|'expected_resp_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_service_is_up
name|'def'
name|'fake_service_is_up'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Simulate validation of instance host is down."""'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|function|fake_service_get_by_compute_host
dedent|''
name|'def'
name|'fake_service_get_by_compute_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Simulate that given host is a valid host."""'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'host_name'"
op|':'
name|'host'
op|','
nl|'\n'
string|"'service'"
op|':'
string|"'compute'"
op|','
nl|'\n'
string|"'zone'"
op|':'
string|"'nova'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_check_instance_exists
dedent|''
name|'def'
name|'fake_check_instance_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Simulate validation of instance does not exist."""'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'service_group_api'
op|'.'
name|'API'
op|','
string|"'service_is_up'"
op|','
nl|'\n'
name|'fake_service_is_up'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'HostAPI'
op|','
string|"'service_get_by_compute_host'"
op|','
nl|'\n'
name|'fake_service_get_by_compute_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_manager'
op|'.'
name|'ComputeManager'
op|','
nl|'\n'
string|"'_check_instance_exists'"
op|','
nl|'\n'
name|'fake_check_instance_exists'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'server_req'
op|','
name|'req_subs'
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
name|'server_resp'
op|','
name|'subs'
op|','
name|'response'
op|','
name|'expected_resp_code'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.conductor.manager.ComputeTaskManager.rebuild_instance'"
op|')'
newline|'\n'
DECL|member|test_server_evacuate
name|'def'
name|'test_server_evacuate'
op|'('
name|'self'
op|','
name|'rebuild_mock'
op|')'
op|':'
newline|'\n'
comment|"# Note (wingwj): The host can't be the same one"
nl|'\n'
indent|'        '
name|'req_subs'
op|'='
op|'{'
nl|'\n'
string|"'host'"
op|':'
string|"'testHost'"
op|','
nl|'\n'
string|'"adminPass"'
op|':'
string|'"MySecretPass"'
op|','
nl|'\n'
string|'"onSharedStorage"'
op|':'
string|"'False'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_evacuate'
op|'('
name|'req_subs'
op|','
string|"'server-evacuate-req'"
op|','
nl|'\n'
string|"'server-evacuate-resp'"
op|','
number|'200'
op|')'
newline|'\n'
name|'rebuild_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'instance'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'image_ref'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'new_pass'
op|'='
string|'"MySecretPass"'
op|','
nl|'\n'
name|'orig_sys_metadata'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'bdms'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'recreate'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'on_shared_storage'
op|'='
name|'False'
op|','
name|'preserve_ephemeral'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'host'
op|'='
string|"'testHost'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.conductor.manager.ComputeTaskManager.rebuild_instance'"
op|')'
newline|'\n'
DECL|member|test_server_evacuate_find_host
name|'def'
name|'test_server_evacuate_find_host'
op|'('
name|'self'
op|','
name|'rebuild_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req_subs'
op|'='
op|'{'
nl|'\n'
string|'"adminPass"'
op|':'
string|'"MySecretPass"'
op|','
nl|'\n'
string|'"onSharedStorage"'
op|':'
string|"'False'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_test_evacuate'
op|'('
name|'req_subs'
op|','
string|"'server-evacuate-find-host-req'"
op|','
nl|'\n'
string|"'server-evacuate-find-host-resp'"
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'rebuild_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'instance'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'image_ref'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'new_pass'
op|'='
string|'"MySecretPass"'
op|','
nl|'\n'
name|'orig_sys_metadata'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'bdms'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'recreate'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'on_shared_storage'
op|'='
name|'False'
op|','
name|'preserve_ephemeral'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
