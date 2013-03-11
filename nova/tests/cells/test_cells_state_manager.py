begin_unit
comment|'# Copyright (c) 2013 Rackspace Hosting'
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
string|'"""\nTests For CellsStateManager\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'state'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FAKE_COMPUTES
name|'FAKE_COMPUTES'
op|'='
op|'['
nl|'\n'
op|'('
string|"'host1'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
string|"'host2'"
op|','
number|'1024'
op|','
number|'100'
op|','
op|'-'
number|'1'
op|','
op|'-'
number|'1'
op|')'
op|','
nl|'\n'
op|'('
string|"'host3'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'1024'
op|','
number|'100'
op|')'
op|','
nl|'\n'
op|'('
string|"'host4'"
op|','
number|'1024'
op|','
number|'100'
op|','
number|'300'
op|','
number|'30'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_ITYPES
name|'FAKE_ITYPES'
op|'='
op|'['
nl|'\n'
op|'('
number|'0'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
op|'('
number|'50'
op|','
number|'12'
op|','
number|'13'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_compute_node_get_all
name|'def'
name|'_fake_compute_node_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
DECL|function|_node
indent|'    '
name|'def'
name|'_node'
op|'('
name|'host'
op|','
name|'total_mem'
op|','
name|'total_disk'
op|','
name|'free_mem'
op|','
name|'free_disk'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'service'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'disabled'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'return'
op|'{'
string|"'service'"
op|':'
name|'service'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'total_mem'
op|','
nl|'\n'
string|"'local_gb'"
op|':'
name|'total_disk'
op|','
nl|'\n'
string|"'free_ram_mb'"
op|':'
name|'free_mem'
op|','
nl|'\n'
string|"'free_disk_gb'"
op|':'
name|'free_disk'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'_node'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_COMPUTES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_instance_type_all
dedent|''
name|'def'
name|'_fake_instance_type_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
DECL|function|_type
indent|'    '
name|'def'
name|'_type'
op|'('
name|'mem'
op|','
name|'root'
op|','
name|'eph'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'root_gb'"
op|':'
name|'root'
op|','
nl|'\n'
string|"'ephemeral_gb'"
op|':'
name|'eph'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'mem'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'['
name|'_type'
op|'('
op|'*'
name|'fake'
op|')'
name|'for'
name|'fake'
name|'in'
name|'FAKE_ITYPES'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestCellsStateManager
dedent|''
name|'class'
name|'TestCellsStateManager'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'TestCellsStateManager'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'compute_node_get_all'"
op|','
name|'_fake_compute_node_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_type_get_all'"
op|','
name|'_fake_instance_type_all'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_no_reserve
dedent|''
name|'def'
name|'test_capacity_no_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# utilize entire cell'
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'0.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'compute'
op|'['
number|'3'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'compute'
op|'['
number|'4'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'units'
op|'='
name|'cell_free_ram'
op|'/'
number|'50'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'units'
op|'='
number|'5'
comment|'# 4 on host 3, 1 on host4'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_full_reserve
dedent|''
name|'def'
name|'test_capacity_full_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# reserve the entire cell. (utilize zero percent)'
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'100.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'compute'
op|'['
number|'3'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'compute'
op|'['
number|'4'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_capacity_part_reserve
dedent|''
name|'def'
name|'test_capacity_part_reserve'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# utilize half the cell's free capacity"
nl|'\n'
indent|'        '
name|'cap'
op|'='
name|'self'
op|'.'
name|'_capacity'
op|'('
number|'50.0'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_ram'
op|'='
name|'sum'
op|'('
name|'compute'
op|'['
number|'3'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_ram'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'cell_free_disk'
op|'='
number|'1024'
op|'*'
name|'sum'
op|'('
name|'compute'
op|'['
number|'4'
op|']'
name|'for'
name|'compute'
name|'in'
name|'FAKE_COMPUTES'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cell_free_disk'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'total_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'units'
op|'='
number|'10'
comment|'# 10 from host 3'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'ram_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
string|"'50'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'sz'
op|'='
number|'25'
op|'*'
number|'1024'
newline|'\n'
name|'units'
op|'='
number|'2'
comment|'# 2 on host 3'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'units'
op|','
name|'cap'
op|'['
string|"'disk_free'"
op|']'
op|'['
string|"'units_by_mb'"
op|']'
op|'['
name|'str'
op|'('
name|'sz'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_capacity
dedent|''
name|'def'
name|'_capacity'
op|'('
name|'self'
op|','
name|'reserve_percent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'reserve_percent'
op|'='
name|'reserve_percent'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
name|'mgr'
op|'='
name|'state'
op|'.'
name|'CellStateManager'
op|'('
op|')'
newline|'\n'
name|'my_state'
op|'='
name|'mgr'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
name|'return'
name|'my_state'
op|'.'
name|'capacities'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
