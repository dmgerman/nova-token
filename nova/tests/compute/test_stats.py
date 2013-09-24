begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 OpenStack Foundation'
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
string|'"""Tests for compute node stats."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'stats'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'task_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StatsTestCase
name|'class'
name|'StatsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'StatsTestCase'
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
name|'stats'
op|'='
name|'stats'
op|'.'
name|'Stats'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|','
name|'values'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
nl|'\n'
string|'"os_type"'
op|':'
string|'"Linux"'
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|'"1234"'
op|','
nl|'\n'
string|'"task_state"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"12-34-56-78-90"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'values'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|test_os_type_count
dedent|''
name|'def'
name|'test_os_type_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'os_type'
op|'='
string|'"Linux"'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
name|'os_type'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_os_type_"'
op|'+'
name|'os_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_os_type_"'
op|'+'
name|'os_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_os_type_Vax"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
name|'os_type'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_os_type_"'
op|'+'
name|'os_type'
op|']'
op|'-='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
name|'os_type'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_project_count
dedent|''
name|'def'
name|'test_update_project_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proj_id'
op|'='
string|'"1234"'
newline|'\n'
nl|'\n'
DECL|function|_get
name|'def'
name|'_get'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
name|'proj_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'_get'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_proj_"'
op|'+'
name|'proj_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'_get'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_proj_"'
op|'+'
name|'proj_id'
op|']'
op|'-='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'_get'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_count
dedent|''
name|'def'
name|'test_instance_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_instances"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_instances"'
op|']'
op|'-='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_stats_for_instance
dedent|''
name|'def'
name|'test_add_stats_for_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
op|'{'
nl|'\n'
string|'"os_type"'
op|':'
string|'"Linux"'
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|'"1234"'
op|','
nl|'\n'
string|'"task_state"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'3'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"12-34-56-78-90"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
nl|'\n'
string|'"os_type"'
op|':'
string|'"FreeBSD"'
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|'"1234"'
op|','
nl|'\n'
string|'"task_state"'
op|':'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"23-45-67-89-01"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
op|'{'
nl|'\n'
string|'"os_type"'
op|':'
string|'"Linux"'
op|','
nl|'\n'
string|'"project_id"'
op|':'
string|'"2345"'
op|','
nl|'\n'
string|'"task_state"'
op|':'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
nl|'\n'
string|'"vcpus"'
op|':'
number|'2'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"34-56-78-90-12"'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
string|'"Linux"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
string|'"FreeBSD"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
string|'"1234"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
string|'"2345"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_task_None"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_task_"'
op|'+'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_None"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_"'
op|'+'
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'6'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_vcpus_used'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_calculate_workload
dedent|''
name|'def'
name|'test_calculate_workload'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_task_None"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_task_"'
op|'+'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_task_"'
op|'+'
name|'task_states'
op|'.'
name|'SCHEDULING'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'calculate_workload'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_stats_for_instance_no_change
dedent|''
name|'def'
name|'test_update_stats_for_instance_no_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
comment|'# no change'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
string|'"1234"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_os_type_Linux"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_task_None"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_"'
op|'+'
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_stats_for_instance_vm_change
dedent|''
name|'def'
name|'test_update_stats_for_instance_vm_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'['
string|'"vm_state"'
op|']'
op|'='
name|'vm_states'
op|'.'
name|'PAUSED'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
number|'1234'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_os_type_Linux"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_%s"'
op|'%'
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_%s"'
op|'%'
name|'vm_states'
op|'.'
name|'PAUSED'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_stats_for_instance_task_change
dedent|''
name|'def'
name|'test_update_stats_for_instance_task_change'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'['
string|'"task_state"'
op|']'
op|'='
name|'task_states'
op|'.'
name|'REBUILDING'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
string|'"1234"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_os_type_Linux"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_task_None"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_task_%s"'
op|'%'
name|'task_states'
op|'.'
name|'REBUILDING'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_stats_for_instance_deleted
dedent|''
name|'def'
name|'test_update_stats_for_instance_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_proj_1234"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'['
string|'"vm_state"'
op|']'
op|'='
name|'vm_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_instances_for_project'
op|'('
string|'"1234"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_os_type'
op|'('
string|'"Linux"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"num_vm_"'
op|'+'
name|'vm_states'
op|'.'
name|'BUILDING'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'num_vcpus_used'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_io_workload
dedent|''
name|'def'
name|'test_io_workload'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vms'
op|'='
op|'['
name|'vm_states'
op|'.'
name|'ACTIVE'
op|','
name|'vm_states'
op|'.'
name|'BUILDING'
op|','
name|'vm_states'
op|'.'
name|'PAUSED'
op|']'
newline|'\n'
name|'tasks'
op|'='
op|'['
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|','
name|'task_states'
op|'.'
name|'REBUILDING'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESIZE_PREP'
op|','
name|'task_states'
op|'.'
name|'IMAGE_SNAPSHOT'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'IMAGE_LIVE_SNAPSHOT'
op|','
name|'task_states'
op|'.'
name|'IMAGE_BACKUP'
op|','
nl|'\n'
name|'task_states'
op|'.'
name|'RESCUING'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'state'
name|'in'
name|'vms'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_vm_"'
op|'+'
name|'state'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'state'
name|'in'
name|'tasks'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stats'
op|'.'
name|'_increment'
op|'('
string|'"num_task_"'
op|'+'
name|'state'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'6'
op|','
name|'self'
op|'.'
name|'stats'
op|'.'
name|'io_workload'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_io_workload_saved_to_stats
dedent|''
name|'def'
name|'test_io_workload_saved_to_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'{'
string|"'task_state'"
op|':'
name|'task_states'
op|'.'
name|'RESIZE_MIGRATING'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'values'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'self'
op|'.'
name|'stats'
op|'['
string|'"io_workload"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_clear
dedent|''
name|'def'
name|'test_clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'update_stats_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'stats'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'stats'
op|'.'
name|'states'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stats'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'stats'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'stats'
op|'.'
name|'states'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
