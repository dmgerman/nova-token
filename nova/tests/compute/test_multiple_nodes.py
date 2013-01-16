begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Tests for compute service with multiple compute nodes."""'
newline|'\n'
nl|'\n'
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
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
newline|'\n'
nl|'\n'
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
string|"'compute_manager'"
op|','
string|"'nova.service'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'compute_driver'"
op|','
string|"'nova.virt.driver'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaseTestCase
name|'class'
name|'BaseTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|tearDown
indent|'    '
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake'
op|'.'
name|'restore_nodes'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'BaseTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDriverSingleNodeTestCase
dedent|''
dedent|''
name|'class'
name|'FakeDriverSingleNodeTestCase'
op|'('
name|'BaseTestCase'
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
name|'FakeDriverSingleNodeTestCase'
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
name|'driver'
op|'='
name|'fake'
op|'.'
name|'FakeDriver'
op|'('
name|'virtapi'
op|'='
name|'None'
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'set_nodes'
op|'('
op|'['
string|"'xyz'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_stats
dedent|''
name|'def'
name|'test_get_host_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_host_stats'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'stats'
op|','
name|'dict'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'stats'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'xyz'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_available_resource
dedent|''
name|'def'
name|'test_get_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_available_resource'
op|'('
string|"'xyz'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'xyz'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeDriverMultiNodeTestCase
dedent|''
dedent|''
name|'class'
name|'FakeDriverMultiNodeTestCase'
op|'('
name|'BaseTestCase'
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
name|'FakeDriverMultiNodeTestCase'
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
name|'driver'
op|'='
name|'fake'
op|'.'
name|'FakeDriver'
op|'('
name|'virtapi'
op|'='
name|'None'
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'set_nodes'
op|'('
op|'['
string|"'aaa'"
op|','
string|"'bbb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_host_stats
dedent|''
name|'def'
name|'test_get_host_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stats'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_host_stats'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'stats'
op|','
name|'list'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'stats'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'stats'
op|'['
number|'0'
op|']'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'aaa'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'stats'
op|'['
number|'1'
op|']'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'bbb'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_available_resource
dedent|''
name|'def'
name|'test_get_available_resource'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res_a'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_available_resource'
op|'('
string|"'aaa'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_a'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'aaa'"
op|')'
newline|'\n'
nl|'\n'
name|'res_b'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_available_resource'
op|'('
string|"'bbb'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_b'
op|'['
string|"'hypervisor_hostname'"
op|']'
op|','
string|"'bbb'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_available_resource'
op|','
string|"'xxx'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultiNodeComputeTestCase
dedent|''
dedent|''
name|'class'
name|'MultiNodeComputeTestCase'
op|'('
name|'BaseTestCase'
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
name|'MultiNodeComputeTestCase'
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
name|'flags'
op|'('
name|'compute_driver'
op|'='
string|"'nova.virt.fake.FakeDriver'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'CONF'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_local'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'conductor'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conductor'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'conductor'"
op|','
nl|'\n'
name|'manager'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'manager'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_available_resource_add_remove_node
dedent|''
name|'def'
name|'test_update_available_resource_add_remove_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'set_nodes'
op|'('
op|'['
string|"'A'"
op|','
string|"'B'"
op|','
string|"'C'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'update_available_resource'
op|'('
name|'ctx'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sorted'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_resource_tracker_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
op|'['
string|"'A'"
op|','
string|"'B'"
op|','
string|"'C'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'.'
name|'set_nodes'
op|'('
op|'['
string|"'A'"
op|','
string|"'B'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'update_available_resource'
op|'('
name|'ctx'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sorted'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_resource_tracker_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
op|'['
string|"'A'"
op|','
string|"'B'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'.'
name|'set_nodes'
op|'('
op|'['
string|"'A'"
op|','
string|"'B'"
op|','
string|"'C'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'update_available_resource'
op|'('
name|'ctx'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sorted'
op|'('
name|'self'
op|'.'
name|'compute'
op|'.'
name|'_resource_tracker_dict'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|','
nl|'\n'
op|'['
string|"'A'"
op|','
string|"'B'"
op|','
string|"'C'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
