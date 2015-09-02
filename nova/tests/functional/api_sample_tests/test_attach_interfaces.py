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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'api'
name|'as'
name|'network_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_network_cache_model'
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
DECL|class|AttachInterfacesSampleJsonTest
name|'class'
name|'AttachInterfacesSampleJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|"'os-attach-interfaces'"
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
name|'AttachInterfacesSampleJsonTest'
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
string|"'attach_interfaces.Attach_interfaces'"
op|')'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'AttachInterfacesSampleJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_list_ports
name|'def'
name|'fake_list_ports'
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
indent|'            '
name|'uuid'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'device_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'uuid'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'port_data'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"ce531f90-199f-48c0-816c-13e38010b442"'
op|','
nl|'\n'
string|'"network_id"'
op|':'
string|'"3cb9bc59-5699-4588-a4b1-b87f96708bc6"'
op|','
nl|'\n'
string|'"admin_state_up"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'"fa:16:3e:4c:2c:30"'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"ip_address"'
op|':'
string|'"192.168.1.3"'
op|','
nl|'\n'
string|'"subnet_id"'
op|':'
string|'"f8a6e8f8-c2ec-497c-9f23-da9616de54ef"'
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"device_id"'
op|':'
name|'uuid'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'ports'
op|'='
op|'{'
string|"'ports'"
op|':'
op|'['
name|'port_data'
op|']'
op|'}'
newline|'\n'
name|'return'
name|'ports'
newline|'\n'
nl|'\n'
DECL|function|fake_show_port
dedent|''
name|'def'
name|'fake_show_port'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'port_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'port_id'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PortNotFound'
op|'('
name|'port_id'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'port_data'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'port_id'
op|','
nl|'\n'
string|'"network_id"'
op|':'
string|'"3cb9bc59-5699-4588-a4b1-b87f96708bc6"'
op|','
nl|'\n'
string|'"admin_state_up"'
op|':'
name|'True'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"ACTIVE"'
op|','
nl|'\n'
string|'"mac_address"'
op|':'
string|'"fa:16:3e:4c:2c:30"'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"ip_address"'
op|':'
string|'"192.168.1.3"'
op|','
nl|'\n'
string|'"subnet_id"'
op|':'
string|'"f8a6e8f8-c2ec-497c-9f23-da9616de54ef"'
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"device_id"'
op|':'
string|"'bece68a3-2f8b-4e66-9092-244493d6aba7'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'port'
op|'='
op|'{'
string|"'port'"
op|':'
name|'port_data'
op|'}'
newline|'\n'
name|'return'
name|'port'
newline|'\n'
nl|'\n'
DECL|function|fake_attach_interface
dedent|''
name|'def'
name|'fake_attach_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'network_id'
op|','
name|'port_id'
op|','
nl|'\n'
name|'requested_ip'
op|'='
string|"'192.168.1.3'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'network_id'
op|':'
newline|'\n'
indent|'                '
name|'network_id'
op|'='
string|'"fake_net_uuid"'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'port_id'
op|':'
newline|'\n'
indent|'                '
name|'port_id'
op|'='
string|'"fake_port_uuid"'
newline|'\n'
dedent|''
name|'vif'
op|'='
name|'fake_network_cache_model'
op|'.'
name|'new_vif'
op|'('
op|')'
newline|'\n'
name|'vif'
op|'['
string|"'id'"
op|']'
op|'='
name|'port_id'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'id'"
op|']'
op|'='
name|'network_id'
newline|'\n'
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'subnets'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'='
name|'requested_ip'
newline|'\n'
name|'return'
name|'vif'
newline|'\n'
nl|'\n'
DECL|function|fake_detach_interface
dedent|''
name|'def'
name|'fake_detach_interface'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'port_id'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'list_ports'"
op|','
name|'fake_list_ports'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'show_port'"
op|','
name|'fake_show_port'
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
name|'API'
op|','
string|"'attach_interface'"
op|','
nl|'\n'
name|'fake_attach_interface'
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
name|'API'
op|','
string|"'detach_interface'"
op|','
nl|'\n'
name|'fake_detach_interface'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'auth_strategy'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'url'
op|'='
string|"'http://anyhost/'"
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'timeout'
op|'='
number|'30'
op|','
name|'group'
op|'='
string|"'neutron'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|generalize_subs
dedent|''
name|'def'
name|'generalize_subs'
op|'('
name|'self'
op|','
name|'subs'
op|','
name|'vanilla_regexes'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'['
string|"'subnet_id'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'net_id'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'port_id'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'mac_addr'"
op|']'
op|'='
string|"'(?:[a-f0-9]{2}:){5}[a-f0-9]{2}'"
newline|'\n'
name|'subs'
op|'['
string|"'ip_address'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'ip'"
op|']'
newline|'\n'
name|'return'
name|'subs'
newline|'\n'
nl|'\n'
DECL|member|test_list_interfaces
dedent|''
name|'def'
name|'test_list_interfaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-interface'"
nl|'\n'
op|'%'
name|'instance_uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'ip_address'"
op|':'
string|"'192.168.1.3'"
op|','
nl|'\n'
string|"'subnet_id'"
op|':'
string|"'f8a6e8f8-c2ec-497c-9f23-da9616de54ef'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'fa:16:3e:4c:2c:30'"
op|','
nl|'\n'
string|"'net_id'"
op|':'
string|"'3cb9bc59-5699-4588-a4b1-b87f96708bc6'"
op|','
nl|'\n'
string|"'port_id'"
op|':'
string|"'ce531f90-199f-48c0-816c-13e38010b442'"
op|','
nl|'\n'
string|"'port_state'"
op|':'
string|"'ACTIVE'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'attach-interfaces-list-resp'"
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
DECL|member|_stub_show_for_instance
dedent|''
name|'def'
name|'_stub_show_for_instance'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|','
name|'port_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'show_port'
op|'='
name|'network_api'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'show_port'
op|'('
name|'None'
op|','
name|'port_id'
op|')'
newline|'\n'
name|'show_port'
op|'['
string|"'port'"
op|']'
op|'['
string|"'device_id'"
op|']'
op|'='
name|'instance_uuid'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'show_port'"
op|','
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'k'
op|':'
name|'show_port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_interfaces
dedent|''
name|'def'
name|'test_show_interfaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'port_id'
op|'='
string|"'ce531f90-199f-48c0-816c-13e38010b442'"
newline|'\n'
name|'self'
op|'.'
name|'_stub_show_for_instance'
op|'('
name|'instance_uuid'
op|','
name|'port_id'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/os-interface/%s'"
op|'%'
nl|'\n'
op|'('
name|'instance_uuid'
op|','
name|'port_id'
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'ip_address'"
op|':'
string|"'192.168.1.3'"
op|','
nl|'\n'
string|"'subnet_id'"
op|':'
string|"'f8a6e8f8-c2ec-497c-9f23-da9616de54ef'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'fa:16:3e:4c:2c:30'"
op|','
nl|'\n'
string|"'net_id'"
op|':'
string|"'3cb9bc59-5699-4588-a4b1-b87f96708bc6'"
op|','
nl|'\n'
string|"'port_id'"
op|':'
name|'port_id'
op|','
nl|'\n'
string|"'port_state'"
op|':'
string|"'ACTIVE'"
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'attach-interfaces-show-resp'"
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
DECL|member|test_create_interfaces
dedent|''
name|'def'
name|'test_create_interfaces'
op|'('
name|'self'
op|','
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance_uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
dedent|''
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'net_id'"
op|':'
string|"'3cb9bc59-5699-4588-a4b1-b87f96708bc6'"
op|','
nl|'\n'
string|"'port_id'"
op|':'
string|"'ce531f90-199f-48c0-816c-13e38010b442'"
op|','
nl|'\n'
string|"'subnet_id'"
op|':'
string|"'f8a6e8f8-c2ec-497c-9f23-da9616de54ef'"
op|','
nl|'\n'
string|"'ip_address'"
op|':'
string|"'192.168.1.3'"
op|','
nl|'\n'
string|"'port_state'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
string|"'mac_addr'"
op|':'
string|"'fa:16:3e:4c:2c:30'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_stub_show_for_instance'
op|'('
name|'instance_uuid'
op|','
name|'subs'
op|'['
string|"'port_id'"
op|']'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/os-interface'"
nl|'\n'
op|'%'
name|'instance_uuid'
op|','
nl|'\n'
string|"'attach-interfaces-create-req'"
op|','
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
string|"'attach-interfaces-create-resp'"
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
DECL|member|test_delete_interfaces
dedent|''
name|'def'
name|'test_delete_interfaces'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'port_id'
op|'='
string|"'ce531f90-199f-48c0-816c-13e38010b442'"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'servers/%s/os-interface/%s'"
op|'%'
nl|'\n'
op|'('
name|'instance_uuid'
op|','
name|'port_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
