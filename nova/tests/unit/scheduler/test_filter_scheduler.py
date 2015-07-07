begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nTests For Filter Scheduler.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filter_scheduler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'host_manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'weights'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
comment|'# noqa'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'scheduler'
name|'import'
name|'test_scheduler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_filtered_hosts
name|'def'
name|'fake_get_filtered_hosts'
op|'('
name|'hosts'
op|','
name|'filter_properties'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'list'
op|'('
name|'hosts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FilterSchedulerTestCase
dedent|''
name|'class'
name|'FilterSchedulerTestCase'
op|'('
name|'test_scheduler'
op|'.'
name|'SchedulerTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for Filter Scheduler."""'
newline|'\n'
nl|'\n'
DECL|variable|driver_cls
name|'driver_cls'
op|'='
name|'filter_scheduler'
op|'.'
name|'FilterScheduler'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
DECL|variable|return_value
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'SERVICES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
DECL|variable|return_value
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
DECL|variable|return_value
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_schedule_happy_day
name|'def'
name|'test_schedule_happy_day'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|','
name|'mock_get_all'
op|','
nl|'\n'
name|'mock_by_host'
op|','
name|'mock_get_by_binary'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure there\'s nothing glaringly wrong with _schedule()\n        by doing a happy day pass through.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'1.0'
newline|'\n'
nl|'\n'
DECL|function|_fake_weigh_objects
name|'def'
name|'_fake_weigh_objects'
op|'('
name|'_self'
op|','
name|'functions'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'next_weight'
op|'+='
number|'2.0'
newline|'\n'
name|'host_state'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
op|'['
name|'weights'
op|'.'
name|'WeighedHost'
op|'('
name|'host_state'
op|','
name|'self'
op|'.'
name|'next_weight'
op|')'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
string|"'get_filtered_hosts'"
op|','
nl|'\n'
name|'fake_get_filtered_hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'weights'
op|'.'
name|'HostWeightHandler'
op|','
nl|'\n'
string|"'get_weighed_objects'"
op|','
name|'_fake_weigh_objects'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'num_instances'
op|'='
number|'10'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'root_gb'
op|'='
number|'512'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'project_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'Linux'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
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
name|'weighed_hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'weighed_hosts'
op|')'
op|','
number|'10'
op|')'
newline|'\n'
name|'for'
name|'weighed_host'
name|'in'
name|'weighed_hosts'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'weighed_host'
op|'.'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_max_attempts
dedent|''
dedent|''
name|'def'
name|'test_max_attempts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'4'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'4'
op|','
name|'scheduler_utils'
op|'.'
name|'_max_attempts'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_max_attempts
dedent|''
name|'def'
name|'test_invalid_max_attempts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_max_attempts'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'_max_attempts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_add_retry_host
dedent|''
name|'def'
name|'test_add_retry_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'retry'
op|'='
name|'dict'
op|'('
name|'num_attempts'
op|'='
number|'1'
op|','
name|'hosts'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'retry'
op|'='
name|'retry'
op|')'
newline|'\n'
name|'host'
op|'='
string|'"fakehost"'
newline|'\n'
name|'node'
op|'='
string|'"fakenode"'
newline|'\n'
nl|'\n'
name|'scheduler_utils'
op|'.'
name|'_add_retry_host'
op|'('
name|'filter_properties'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
nl|'\n'
name|'hosts'
op|'='
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'hosts'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'host'
op|','
name|'node'
op|']'
op|','
name|'hosts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_select_populate
dedent|''
name|'def'
name|'test_post_select_populate'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test addition of certain filter props after a node is selected.'
nl|'\n'
indent|'        '
name|'retry'
op|'='
op|'{'
string|"'hosts'"
op|':'
op|'['
op|']'
op|','
string|"'num_attempts'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'filter_properties'
op|'='
op|'{'
string|"'retry'"
op|':'
name|'retry'
op|'}'
newline|'\n'
nl|'\n'
name|'host_state'
op|'='
name|'host_manager'
op|'.'
name|'HostState'
op|'('
string|"'host'"
op|','
string|"'node'"
op|')'
newline|'\n'
name|'host_state'
op|'.'
name|'limits'
op|'['
string|"'vcpu'"
op|']'
op|'='
number|'5'
newline|'\n'
name|'scheduler_utils'
op|'.'
name|'populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'host'"
op|','
string|"'node'"
op|']'
op|','
nl|'\n'
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'['
string|"'hosts'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'vcpu'"
op|':'
number|'5'
op|'}'
op|','
name|'host_state'
op|'.'
name|'limits'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'SERVICES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_schedule_host_pool
name|'def'
name|'test_schedule_host_pool'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|','
name|'mock_get_all'
op|','
nl|'\n'
name|'mock_by_host'
op|','
name|'mock_get_by_binary'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure the scheduler_host_subset_size property works properly."""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_host_subset_size'
op|'='
number|'2'
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
name|'driver'
op|'.'
name|'host_manager'
op|','
string|"'get_filtered_hosts'"
op|','
nl|'\n'
name|'fake_get_filtered_hosts'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'project_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'Linux'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
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
name|'hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
comment|'# one host should be chosen'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'hosts'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'SERVICES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_schedule_large_host_pool
name|'def'
name|'test_schedule_large_host_pool'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|','
name|'mock_get_all'
op|','
nl|'\n'
name|'mock_by_host'
op|','
name|'mock_get_by_binary'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Hosts should still be chosen if pool size\n        is larger than number of filtered hosts.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_host_subset_size'
op|'='
number|'20'
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
name|'driver'
op|'.'
name|'host_manager'
op|','
string|"'get_filtered_hosts'"
op|','
nl|'\n'
name|'fake_get_filtered_hosts'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'project_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'Linux'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
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
name|'hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
comment|'# one host should be chose'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'hosts'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.scheduler.host_manager.HostManager._add_instance_info'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'SERVICES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_schedule_chooses_best_host
name|'def'
name|'test_schedule_chooses_best_host'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|','
name|'mock_cn_get_all'
op|','
nl|'\n'
name|'mock_get_by_binary'
op|','
nl|'\n'
name|'mock_add_inst_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""If scheduler_host_subset_size is 1, the largest host with greatest\n        weight should be returned.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'scheduler_host_subset_size'
op|'='
number|'1'
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
name|'driver'
op|'.'
name|'host_manager'
op|','
string|"'get_filtered_hosts'"
op|','
nl|'\n'
name|'fake_get_filtered_hosts'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'50'
newline|'\n'
nl|'\n'
DECL|function|_fake_weigh_objects
name|'def'
name|'_fake_weigh_objects'
op|'('
name|'_self'
op|','
name|'functions'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'this_weight'
op|'='
name|'self'
op|'.'
name|'next_weight'
newline|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'0'
newline|'\n'
name|'host_state'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
op|'['
name|'weights'
op|'.'
name|'WeighedHost'
op|'('
name|'host_state'
op|','
name|'this_weight'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'project_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'Linux'"
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'root_gb'
op|'='
number|'512'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'weights'
op|'.'
name|'HostWeightHandler'
op|','
nl|'\n'
string|"'get_weighed_objects'"
op|','
name|'_fake_weigh_objects'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_schedule'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
comment|'# one host should be chosen'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'hosts'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'50'
op|','
name|'hosts'
op|'['
number|'0'
op|']'
op|'.'
name|'weight'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ServiceList.get_by_binary'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'SERVICES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.InstanceList.get_by_host'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'fakes'
op|'.'
name|'COMPUTE_NODES'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_extra_get_by_instance_uuid'"
op|','
nl|'\n'
name|'return_value'
op|'='
op|'{'
string|"'numa_topology'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'pci_requests'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
DECL|member|test_select_destinations
name|'def'
name|'test_select_destinations'
op|'('
name|'self'
op|','
name|'mock_get_extra'
op|','
name|'mock_get_all'
op|','
nl|'\n'
name|'mock_by_host'
op|','
name|'mock_get_by_binary'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""select_destinations is basically a wrapper around _schedule().\n\n        Similar to the _schedule tests, this just does a happy path test to\n        ensure there is nothing glaringly wrong.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'next_weight'
op|'='
number|'1.0'
newline|'\n'
nl|'\n'
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'selected_nodes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_fake_weigh_objects
name|'def'
name|'_fake_weigh_objects'
op|'('
name|'_self'
op|','
name|'functions'
op|','
name|'hosts'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'next_weight'
op|'+='
number|'2.0'
newline|'\n'
name|'host_state'
op|'='
name|'hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'selected_hosts'
op|'.'
name|'append'
op|'('
name|'host_state'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'selected_nodes'
op|'.'
name|'append'
op|'('
name|'host_state'
op|'.'
name|'nodename'
op|')'
newline|'\n'
name|'return'
op|'['
name|'weights'
op|'.'
name|'WeighedHost'
op|'('
name|'host_state'
op|','
name|'self'
op|'.'
name|'next_weight'
op|')'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'host_manager'
op|','
string|"'get_filtered_hosts'"
op|','
nl|'\n'
name|'fake_get_filtered_hosts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'weights'
op|'.'
name|'HostWeightHandler'
op|','
nl|'\n'
string|"'get_weighed_objects'"
op|','
name|'_fake_weigh_objects'
op|')'
newline|'\n'
nl|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'512'
op|','
nl|'\n'
name|'root_gb'
op|'='
number|'512'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
number|'0'
op|','
nl|'\n'
name|'vcpus'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'project_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'Linux'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'pci_requests'
op|'='
name|'None'
op|','
nl|'\n'
name|'numa_topology'
op|'='
name|'None'
op|','
nl|'\n'
name|'instance_group'
op|'='
name|'None'
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
name|'dests'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
op|'('
name|'host'
op|','
name|'node'
op|')'
op|'='
op|'('
name|'dests'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|','
name|'dests'
op|'['
number|'0'
op|']'
op|'['
string|"'nodename'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'host'
op|','
name|'selected_hosts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|','
name|'selected_nodes'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'filter_scheduler'
op|'.'
name|'FilterScheduler'
op|','
string|"'_schedule'"
op|')'
newline|'\n'
DECL|member|test_select_destinations_notifications
name|'def'
name|'test_select_destinations_notifications'
op|'('
name|'self'
op|','
name|'mock_schedule'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_schedule'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'driver'
op|'.'
name|'notifier'
op|','
string|"'info'"
op|')'
name|'as'
name|'mock_info'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
string|"'num_instances'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_properties'"
op|':'
op|'{'
string|"'uuid'"
op|':'
string|"'uuid1'"
op|'}'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'image'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'num_instances'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
string|"'uuid1'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'spec_obj'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'scheduler.select_destinations.start'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'expected'
op|')'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'scheduler.select_destinations.end'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'expected'
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'mock_info'
op|'.'
name|'call_args_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_select_destinations_no_valid_host
dedent|''
dedent|''
name|'def'
name|'test_select_destinations_no_valid_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|_return_no_host
indent|'        '
name|'def'
name|'_return_no_host'
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
name|'self'
op|'.'
name|'driver'
op|','
string|"'_schedule'"
op|','
name|'_return_no_host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoValidHost'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|','
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'num_instances'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_select_destinations_no_valid_host_not_enough
dedent|''
name|'def'
name|'test_select_destinations_no_valid_host_not_enough'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Tests that we have fewer hosts available than number of instances'
nl|'\n'
comment|'# requested to build.'
nl|'\n'
indent|'        '
name|'consumed_hosts'
op|'='
op|'['
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|','
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
op|']'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'driver'
op|','
string|"'_schedule'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'consumed_hosts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'select_destinations'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
name|'num_instances'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|"'Expected NoValidHost to be raised.'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoValidHost'
name|'as'
name|'e'
op|':'
newline|'\n'
comment|'# Make sure that we provided a reason why NoValidHost.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'reason'"
op|','
name|'e'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'e'
op|'.'
name|'kwargs'
op|'['
string|"'reason'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
comment|'# Make sure that the consumed hosts have chance to be reverted.'
nl|'\n'
name|'for'
name|'host'
name|'in'
name|'consumed_hosts'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'host'
op|'.'
name|'obj'
op|'.'
name|'updated'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
