begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack, LLC'
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
string|'"""Stubouts, mocks and fixtures for the test suite"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
nl|'\n'
DECL|class|FakeModel
name|'class'
name|'FakeModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out for model """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'values'
op|'='
name|'values'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'in'
name|'self'
op|'.'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'values'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|stub_out_db_instance_api
dedent|''
dedent|''
dedent|''
name|'def'
name|'stub_out_db_instance_api'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out the db API for creating Instances """'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_create
name|'def'
name|'fake_instance_create'
op|'('
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Stubs out the db.instance_create method """'
newline|'\n'
nl|'\n'
name|'type_data'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'base_options'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'values'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'values'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'r'"
op|')'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'values'
op|'['
string|"'image_id'"
op|']'
op|','
nl|'\n'
string|"'kernel_id'"
op|':'
name|'values'
op|'['
string|"'kernel_id'"
op|']'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'values'
op|'['
string|"'ramdisk_id'"
op|']'
op|','
nl|'\n'
string|"'state_description'"
op|':'
string|"'scheduling'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
name|'values'
op|'['
string|"'user_id'"
op|']'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'values'
op|'['
string|"'project_id'"
op|']'
op|','
nl|'\n'
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
nl|'\n'
string|"'instance_type'"
op|':'
name|'values'
op|'['
string|"'instance_type'"
op|']'
op|','
nl|'\n'
string|"'key_data'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'type_data'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'mac_address'"
op|':'
name|'values'
op|'['
string|"'mac_address'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'type_data'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'type_data'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'FakeModel'
op|'('
name|'base_options'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
nl|'\n'
DECL|function|stub_out_db_network_api
dedent|''
name|'def'
name|'stub_out_db_network_api'
op|'('
name|'stubs'
op|','
name|'injected'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out the db API for retrieving networks"""'
newline|'\n'
name|'network_fields'
op|'='
op|'{'
nl|'\n'
string|"'bridge'"
op|':'
string|"'xenbr0'"
op|','
nl|'\n'
string|"'injected'"
op|':'
name|'injected'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'injected'
op|':'
newline|'\n'
indent|'        '
name|'network_fields'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|"'netmask'"
op|':'
string|"'255.255.255.0'"
op|','
nl|'\n'
string|"'gateway'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'broadcast'"
op|':'
string|"'10.0.0.255'"
op|','
nl|'\n'
string|"'dns'"
op|':'
string|"'10.0.0.2'"
op|','
nl|'\n'
string|"'ra_server'"
op|':'
name|'None'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
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
newline|'\n'
indent|'        '
name|'return'
name|'FakeModel'
op|'('
name|'network_fields'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_fixed_address
dedent|''
name|'def'
name|'fake_instance_get_fixed_address'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'10.0.0.3'"
newline|'\n'
nl|'\n'
dedent|''
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
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_fixed_address'"
op|','
name|'fake_instance_get_fixed_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
