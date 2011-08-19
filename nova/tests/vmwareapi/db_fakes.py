begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nStubouts, mocks and fixtures for the test suite\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'import'
name|'time'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_state'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|stub_out_db_instance_api
name|'def'
name|'stub_out_db_instance_api'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Stubs out the db API for creating Instances."""'
newline|'\r\n'
nl|'\r\n'
name|'INSTANCE_TYPES'
op|'='
op|'{'
nl|'\r\n'
string|"'m1.tiny'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'0'
op|','
name|'flavorid'
op|'='
number|'1'
op|')'
op|','
nl|'\r\n'
string|"'m1.small'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'2048'
op|','
name|'vcpus'
op|'='
number|'1'
op|','
name|'local_gb'
op|'='
number|'20'
op|','
name|'flavorid'
op|'='
number|'2'
op|')'
op|','
nl|'\r\n'
string|"'m1.medium'"
op|':'
nl|'\r\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'vcpus'
op|'='
number|'2'
op|','
name|'local_gb'
op|'='
number|'40'
op|','
name|'flavorid'
op|'='
number|'3'
op|')'
op|','
nl|'\r\n'
string|"'m1.large'"
op|':'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'8192'
op|','
name|'vcpus'
op|'='
number|'4'
op|','
name|'local_gb'
op|'='
number|'80'
op|','
name|'flavorid'
op|'='
number|'4'
op|')'
op|','
nl|'\r\n'
string|"'m1.xlarge'"
op|':'
nl|'\r\n'
name|'dict'
op|'('
name|'memory_mb'
op|'='
number|'16384'
op|','
name|'vcpus'
op|'='
number|'8'
op|','
name|'local_gb'
op|'='
number|'160'
op|','
name|'flavorid'
op|'='
number|'5'
op|')'
op|'}'
newline|'\r\n'
nl|'\r\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Stubs out for model."""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\r\n'
nl|'\r\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\r\n'
nl|'\r\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\r\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_instance_create
dedent|''
dedent|''
dedent|''
name|'def'
name|'fake_instance_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Stubs out the db.instance_create method."""'
newline|'\r\n'
nl|'\r\n'
name|'type_data'
op|'='
name|'INSTANCE_TYPES'
op|'['
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|']'
newline|'\r\n'
nl|'\r\n'
name|'base_options'
op|'='
op|'{'
nl|'\r\n'
string|"'name'"
op|':'
name|'values'
op|'['
string|"'name'"
op|']'
op|','
nl|'\r\n'
string|"'id'"
op|':'
name|'values'
op|'['
string|"'id'"
op|']'
op|','
nl|'\r\n'
string|"'reservation_id'"
op|':'
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
op|','
nl|'\r\n'
string|"'image_ref'"
op|':'
name|'values'
op|'['
string|"'image_ref'"
op|']'
op|','
nl|'\r\n'
string|"'kernel_id'"
op|':'
name|'values'
op|'['
string|"'kernel_id'"
op|']'
op|','
nl|'\r\n'
string|"'ramdisk_id'"
op|':'
name|'values'
op|'['
string|"'ramdisk_id'"
op|']'
op|','
nl|'\r\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'BUILD'
op|','
nl|'\r\n'
string|"'task_state'"
op|':'
name|'task_state'
op|'.'
name|'SCHEDULE'
op|','
nl|'\r\n'
string|"'user_id'"
op|':'
name|'values'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\r\n'
string|"'project_id'"
op|':'
name|'values'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\r\n'
string|"'launch_time'"
op|':'
name|'time'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
op|','
nl|'\r\n'
string|"'instance_type'"
op|':'
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|','
nl|'\r\n'
string|"'memory_mb'"
op|':'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\r\n'
string|"'vcpus'"
op|':'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\r\n'
string|"'mac_addresses'"
op|':'
op|'['
op|'{'
string|"'address'"
op|':'
name|'values'
op|'['
string|"'mac_address'"
op|']'
op|'}'
op|']'
op|','
nl|'\r\n'
string|"'local_gb'"
op|':'
name|'type_data'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\r\n'
op|'}'
newline|'\r\n'
name|'return'
name|'FakeModel'
op|'('
name|'base_options'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_network_get_by_instance
dedent|''
name|'def'
name|'fake_network_get_by_instance'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Stubs out the db.network_get_by_instance method."""'
newline|'\r\n'
nl|'\r\n'
name|'fields'
op|'='
op|'{'
nl|'\r\n'
string|"'bridge'"
op|':'
string|"'vmnet0'"
op|','
nl|'\r\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\r\n'
string|"'gateway'"
op|':'
string|"'10.10.10.1'"
op|','
nl|'\r\n'
string|"'broadcast'"
op|':'
string|"'10.10.10.255'"
op|','
nl|'\r\n'
string|"'dns1'"
op|':'
string|"'fake'"
op|','
nl|'\r\n'
string|"'vlan'"
op|':'
number|'100'
op|'}'
newline|'\r\n'
name|'return'
name|'FakeModel'
op|'('
name|'fields'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_instance_action_create
dedent|''
name|'def'
name|'fake_instance_action_create'
op|'('
name|'context'
op|','
name|'action'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Stubs out the db.instance_action_create method."""'
newline|'\r\n'
name|'pass'
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_instance_get_fixed_addresses
dedent|''
name|'def'
name|'fake_instance_get_fixed_addresses'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Stubs out the db.instance_get_fixed_address method."""'
newline|'\r\n'
name|'return'
string|"'10.10.10.10'"
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_instance_type_get_all
dedent|''
name|'def'
name|'fake_instance_type_get_all'
op|'('
name|'context'
op|','
name|'inactive'
op|'='
number|'0'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
newline|'\r\n'
nl|'\r\n'
DECL|function|fake_instance_type_get_by_name
dedent|''
name|'def'
name|'fake_instance_type_get_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
name|'INSTANCE_TYPES'
op|'['
name|'name'
op|']'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_create'"
op|','
name|'fake_instance_create'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'network_get_by_instance'"
op|','
name|'fake_network_get_by_instance'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_action_create'"
op|','
name|'fake_instance_action_create'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_fixed_addresses'"
op|','
nl|'\r\n'
name|'fake_instance_get_fixed_addresses'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_all'"
op|','
name|'fake_instance_type_get_all'
op|')'
newline|'\r\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_by_name'"
op|','
name|'fake_instance_type_get_by_name'
op|')'
newline|'\r\n'
dedent|''
endmarker|''
end_unit
