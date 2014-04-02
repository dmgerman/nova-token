begin_unit
comment|'# Copyright 2012 Red Hat, Inc.'
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
nl|'\n'
string|'"""Tests for network API."""'
newline|'\n'
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
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
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'base_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'floating_ips'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'rpcapi'
name|'as'
name|'network_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'a47ae74e-ab08-547f-9eee-ffd23fc46c16'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkPolicyTestCase
name|'class'
name|'NetworkPolicyTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'NetworkPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'init'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NetworkPolicyTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'policy'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_policy
dedent|''
name|'def'
name|'test_check_policy'
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
name|'policy'
op|','
string|"'enforce'"
op|')'
newline|'\n'
name|'target'
op|'='
op|'{'
nl|'\n'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'policy'
op|'.'
name|'enforce'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'network:get_all'"
op|','
name|'target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'api'
op|'.'
name|'check_policy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'get_all'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiTestCase
dedent|''
dedent|''
name|'class'
name|'ApiTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'ApiTestCase'
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
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
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
string|"'fake-user'"
op|','
nl|'\n'
string|"'fake-project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_allocate_for_instance_handles_macs_passed
dedent|''
name|'def'
name|'test_allocate_for_instance_handles_macs_passed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# If a macs argument is supplied to the 'nova-network' API, it is just"
nl|'\n'
comment|'# ignored. This test checks that the call down to the rpcapi layer'
nl|'\n'
comment|"# doesn't pass macs down: nova-network doesn't support hypervisor"
nl|'\n'
comment|'# mac address limits (today anyhow).'
nl|'\n'
indent|'        '
name|'macs'
op|'='
name|'set'
op|'('
op|'['
string|"'ab:cd:ef:01:23:34'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'network_rpcapi'
op|','
string|'"allocate_for_instance"'
op|')'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'zip'
op|'('
op|'['
string|"'host'"
op|','
string|"'instance_id'"
op|','
string|"'project_id'"
op|','
nl|'\n'
string|"'requested_networks'"
op|','
string|"'rxtx_factor'"
op|','
string|"'vpn'"
op|','
string|"'macs'"
op|','
nl|'\n'
string|"'dhcp_options'"
op|']'
op|','
nl|'\n'
name|'itertools'
op|'.'
name|'repeat'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'network_rpcapi'
op|'.'
name|'allocate_for_instance'
op|'('
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
op|'**'
name|'kwargs'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
name|'flavor'
op|'['
string|"'rxtx_factor'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'sys_meta'
op|'='
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'flavor'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
string|"'id'"
op|','
name|'uuid'
op|'='
string|"'uuid'"
op|','
name|'project_id'
op|'='
string|"'project_id'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'host'"
op|','
name|'system_metadata'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
name|'sys_meta'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'allocate_for_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
string|"'vpn'"
op|','
string|"'requested_networks'"
op|','
name|'macs'
op|'='
name|'macs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_test_associate_floating_ip
dedent|''
name|'def'
name|'_do_test_associate_floating_ip'
op|'('
name|'self'
op|','
name|'orig_instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test post-association logic."""'
newline|'\n'
nl|'\n'
name|'new_instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'new-uuid'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_associate
name|'def'
name|'fake_associate'
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
name|'return'
name|'orig_instance_uuid'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'floating_ips'
op|'.'
name|'FloatingIP'
op|','
string|"'associate_floating_ip'"
op|','
nl|'\n'
name|'fake_associate'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_nw_info
name|'def'
name|'fake_get_nw_info'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
DECL|class|FakeNWInfo
indent|'            '
name|'class'
name|'FakeNWInfo'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|json
indent|'                '
name|'def'
name|'json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'FakeNWInfo'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|','
string|"'_get_instance_nw_info'"
op|','
nl|'\n'
name|'fake_get_nw_info'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'orig_instance_uuid'
op|':'
newline|'\n'
indent|'            '
name|'expected_updated_instances'
op|'='
op|'['
name|'new_instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'orig_instance_uuid'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'expected_updated_instances'
op|'='
op|'['
name|'new_instance'
op|'['
string|"'uuid'"
op|']'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_info_cache_update
dedent|''
name|'def'
name|'fake_instance_info_cache_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'cache'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_uuid'
op|','
nl|'\n'
name|'expected_updated_instances'
op|'.'
name|'pop'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'instance_info_cache_update'"
op|','
nl|'\n'
name|'fake_instance_info_cache_update'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_update_instance_cache_with_nw_info
name|'def'
name|'fake_update_instance_cache_with_nw_info'
op|'('
name|'api'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'nw_info'
op|'='
name|'None'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'base_api'
op|','
string|'"update_instance_cache_with_nw_info"'
op|','
nl|'\n'
name|'fake_update_instance_cache_with_nw_info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'new_instance'
op|','
nl|'\n'
string|"'172.24.4.225'"
op|','
nl|'\n'
string|"'10.0.0.2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_preassociated_floating_ip
dedent|''
name|'def'
name|'test_associate_preassociated_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_associate_floating_ip'
op|'('
string|"'orig-uuid'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_associate_unassociated_floating_ip
dedent|''
name|'def'
name|'test_associate_unassociated_floating_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_test_associate_floating_ip'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_floating_ip_invalid_id
dedent|''
name|'def'
name|'test_get_floating_ip_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidID'
op|','
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_floating_ip'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'123zzz'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_migrate_instance_calls
dedent|''
name|'def'
name|'_stub_migrate_instance_calls'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'multi_host'
op|','
name|'info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_flavor'
op|'='
name|'flavors'
op|'.'
name|'get_default_flavor'
op|'('
op|')'
newline|'\n'
name|'fake_flavor'
op|'['
string|"'rxtx_factor'"
op|']'
op|'='
number|'1.21'
newline|'\n'
name|'sys_meta'
op|'='
name|'utils'
op|'.'
name|'dict_to_metadata'
op|'('
nl|'\n'
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
op|'{'
op|'}'
op|','
name|'fake_flavor'
op|')'
op|')'
newline|'\n'
name|'fake_instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'fake_uuid'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
name|'fake_flavor'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project_id'"
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
newline|'\n'
name|'fake_migration'
op|'='
op|'{'
string|"'source_compute'"
op|':'
string|"'fake_compute_source'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'fake_compute_dest'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_mig_inst_method
name|'def'
name|'fake_mig_inst_method'
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
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|'='
name|'kwargs'
newline|'\n'
nl|'\n'
DECL|function|fake_is_multi_host
dedent|''
name|'def'
name|'fake_is_multi_host'
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
name|'return'
name|'multi_host'
newline|'\n'
nl|'\n'
DECL|function|fake_get_floaters
dedent|''
name|'def'
name|'fake_get_floaters'
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
name|'return'
op|'['
string|"'fake_float1'"
op|','
string|"'fake_float2'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_rpcapi'
op|'.'
name|'NetworkAPI'
op|','
name|'method'
op|','
nl|'\n'
name|'fake_mig_inst_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|','
string|"'_is_multi_host'"
op|','
nl|'\n'
name|'fake_is_multi_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|','
string|"'_get_floating_ip_addresses'"
op|','
nl|'\n'
name|'fake_get_floaters'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'instance_uuid'"
op|':'
string|"'fake_uuid'"
op|','
nl|'\n'
string|"'source_compute'"
op|':'
string|"'fake_compute_source'"
op|','
nl|'\n'
string|"'dest_compute'"
op|':'
string|"'fake_compute_dest'"
op|','
nl|'\n'
string|"'rxtx_factor'"
op|':'
number|'1.21'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake_project_id'"
op|','
nl|'\n'
string|"'floating_addresses'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'if'
name|'multi_host'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'['
string|"'floating_addresses'"
op|']'
op|'='
op|'['
string|"'fake_float1'"
op|','
string|"'fake_float2'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'fake_instance'
op|','
name|'fake_migration'
op|','
name|'expected'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start_with_multhost
dedent|''
name|'def'
name|'test_migrate_instance_start_with_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_start'"
op|','
name|'True'
op|','
name|'info'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'host'"
op|']'
op|'='
string|"'fake_compute_source'"
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_start'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_start_without_multhost
dedent|''
name|'def'
name|'test_migrate_instance_start_without_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_start'"
op|','
name|'False'
op|','
name|'info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_start'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish_with_multhost
dedent|''
name|'def'
name|'test_migrate_instance_finish_with_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_finish'"
op|','
name|'True'
op|','
name|'info'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'host'"
op|']'
op|'='
string|"'fake_compute_dest'"
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_finish'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_migrate_instance_finish_without_multhost
dedent|''
name|'def'
name|'test_migrate_instance_finish_without_multhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|"'kwargs'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'arg1'
op|','
name|'arg2'
op|','
name|'expected'
op|'='
name|'self'
op|'.'
name|'_stub_migrate_instance_calls'
op|'('
nl|'\n'
string|"'migrate_instance_finish'"
op|','
name|'False'
op|','
name|'info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'migrate_instance_finish'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'info'
op|'['
string|"'kwargs'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_instance_has_no_fixed_ip
dedent|''
name|'def'
name|'test_is_multi_host_instance_has_no_fixed_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_fixed_ip_get_by_instance
indent|'        '
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FixedIpNotFoundForInstance'
op|'('
name|'instance_uuid'
op|'='
name|'uuid'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_network_has_no_project_id
dedent|''
name|'def'
name|'test_is_multi_host_network_has_no_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_multi_host'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
op|'['
name|'True'
op|','
name|'False'
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'is_multi_host'
op|','
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_instance
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
op|'['
op|'{'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'FAKE_UUID'
op|','
op|'}'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'is_multi_host'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_multi_host_network_has_project_id
dedent|''
name|'def'
name|'test_is_multi_host_network_has_project_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_multi_host'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
op|'['
name|'True'
op|','
name|'False'
op|']'
op|')'
newline|'\n'
name|'network'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'multi_host'"
op|':'
name|'is_multi_host'
op|','
op|'}'
newline|'\n'
name|'network_ref'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|'.'
name|'network_create_safe'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
nl|'\n'
name|'network'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fixed_ip_get_by_instance
name|'def'
name|'fake_fixed_ip_get_by_instance'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixed_ip'
op|'='
op|'['
op|'{'
string|"'network_id'"
op|':'
name|'network_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
name|'FAKE_UUID'
op|','
op|'}'
op|']'
newline|'\n'
name|'return'
name|'fixed_ip'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'fixed_ip_get_by_instance'"
op|','
nl|'\n'
name|'fake_fixed_ip_get_by_instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'_is_multi_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'is_multi_host'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_network_disassociate_project
dedent|''
name|'def'
name|'test_network_disassociate_project'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_network_disassociate
indent|'        '
name|'def'
name|'fake_network_disassociate'
op|'('
name|'ctx'
op|','
name|'network_id'
op|','
name|'disassociate_host'
op|','
nl|'\n'
name|'disassociate_project'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'network_id'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'disassociate_host'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'disassociate_project'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get
dedent|''
name|'def'
name|'fake_get'
op|'('
name|'context'
op|','
name|'network_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'db'
op|','
string|"'network_disassociate'"
op|','
nl|'\n'
name|'fake_network_disassociate'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'network_api'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'associate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'FAKE_UUID'
op|','
name|'project'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.network.api.API'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_info_cache_update'"
op|')'
newline|'\n'
DECL|class|TestUpdateInstanceCache
name|'class'
name|'TestUpdateInstanceCache'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestUpdateInstanceCache'
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
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|'}'
newline|'\n'
name|'vifs'
op|'='
op|'['
name|'network_model'
op|'.'
name|'VIF'
op|'('
name|'id'
op|'='
string|"'super_vif'"
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
name|'vifs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nw_json'
op|'='
name|'fields'
op|'.'
name|'NetworkModel'
op|'.'
name|'to_primitive'
op|'('
name|'self'
op|','
string|"'network_info'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_nw_info_none
dedent|''
name|'def'
name|'test_update_nw_info_none'
op|'('
name|'self'
op|','
name|'db_mock'
op|','
name|'api_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'nw_info'
newline|'\n'
nl|'\n'
name|'base_api'
op|'.'
name|'update_instance_cache_with_nw_info'
op|'('
name|'api_mock'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'None'
op|')'
newline|'\n'
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'db_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
name|'self'
op|'.'
name|'nw_json'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_nw_info_one_network
dedent|''
name|'def'
name|'test_update_nw_info_one_network'
op|'('
name|'self'
op|','
name|'db_mock'
op|','
name|'api_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'nw_info'
newline|'\n'
name|'base_api'
op|'.'
name|'update_instance_cache_with_nw_info'
op|'('
name|'api_mock'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
name|'self'
op|'.'
name|'nw_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'db_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
name|'self'
op|'.'
name|'nw_json'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_nw_info_empty_list
dedent|''
name|'def'
name|'test_update_nw_info_empty_list'
op|'('
name|'self'
op|','
name|'db_mock'
op|','
name|'api_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'nw_info'
newline|'\n'
name|'base_api'
op|'.'
name|'update_instance_cache_with_nw_info'
op|'('
name|'api_mock'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'db_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
string|"'[]'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_decorator_return_object
dedent|''
name|'def'
name|'test_decorator_return_object'
op|'('
name|'self'
op|','
name|'db_mock'
op|','
name|'api_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'base_api'
op|'.'
name|'refresh_cache'
newline|'\n'
DECL|function|func
name|'def'
name|'func'
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
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'func'
op|'('
name|'api_mock'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'db_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
string|"'[]'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_decorator_return_none
dedent|''
name|'def'
name|'test_decorator_return_none'
op|'('
name|'self'
op|','
name|'db_mock'
op|','
name|'api_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'base_api'
op|'.'
name|'refresh_cache'
newline|'\n'
DECL|function|func
name|'def'
name|'func'
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
name|'pass'
newline|'\n'
dedent|''
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'nw_info'
newline|'\n'
name|'func'
op|'('
name|'api_mock'
op|','
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'api_mock'
op|'.'
name|'_get_instance_nw_info'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'db_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'network_info'"
op|':'
name|'self'
op|'.'
name|'nw_json'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
