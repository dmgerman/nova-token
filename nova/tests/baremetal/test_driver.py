begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California / ISI'
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
string|'"""\nTests for baremetal driver.\n"""'
newline|'\n'
nl|'\n'
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
name|'tests'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
name|'as'
name|'fake_image'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'test_virt_drivers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'utils'
name|'as'
name|'test_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'driver'
name|'as'
name|'bm_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'volume_driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'firewall'
name|'import'
name|'NoopFirewallDriver'
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
nl|'\n'
nl|'\n'
DECL|class|FakeVifDriver
name|'class'
name|'FakeVifDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|plug
indent|'    '
name|'def'
name|'plug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unplug
dedent|''
name|'def'
name|'unplug'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'vif'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|variable|FakeFirewallDriver
dedent|''
dedent|''
name|'FakeFirewallDriver'
op|'='
name|'NoopFirewallDriver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeVolumeDriver
name|'class'
name|'FakeVolumeDriver'
op|'('
name|'volume_driver'
op|'.'
name|'VolumeDriver'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeVolumeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_initiator'
op|'='
string|'"testtesttest"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|NODE
dedent|''
dedent|''
name|'NODE'
op|'='
name|'utils'
op|'.'
name|'new_bm_node'
op|'('
name|'cpus'
op|'='
number|'2'
op|','
name|'memory_mb'
op|'='
number|'4096'
op|','
name|'service_host'
op|'='
string|'"host1"'
op|')'
newline|'\n'
DECL|variable|NICS
name|'NICS'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'01:23:45:67:89:01'"
op|','
string|"'datapath_id'"
op|':'
string|"'0x1'"
op|','
string|"'port_no'"
op|':'
number|'1'
op|','
op|'}'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'01:23:45:67:89:02'"
op|','
string|"'datapath_id'"
op|':'
string|"'0x2'"
op|','
string|"'port_no'"
op|':'
number|'2'
op|','
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|class_path
name|'def'
name|'class_path'
op|'('
name|'class_'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'class_'
op|'.'
name|'__module__'
op|'+'
string|"'.'"
op|'+'
name|'class_'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|COMMON_FLAGS
dedent|''
name|'COMMON_FLAGS'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'firewall_driver'
op|'='
name|'class_path'
op|'('
name|'FakeFirewallDriver'
op|')'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|BAREMETAL_FLAGS
name|'BAREMETAL_FLAGS'
op|'='
name|'dict'
op|'('
nl|'\n'
DECL|variable|driver
name|'driver'
op|'='
string|"'nova.virt.baremetal.fake.Fake'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
name|'NODE'
op|'['
string|"'service_host'"
op|']'
op|','
nl|'\n'
DECL|variable|instance_type_extra_specs
name|'instance_type_extra_specs'
op|'='
op|'['
string|"'cpu_arch:test'"
op|']'
op|','
nl|'\n'
DECL|variable|power_manager
name|'power_manager'
op|'='
string|"'nova.virt.baremetal.fake.FakePowerManager'"
op|','
nl|'\n'
DECL|variable|sql_connection
name|'sql_connection'
op|'='
string|"'sqlite:///:memory:'"
op|','
nl|'\n'
DECL|variable|vif_driver
name|'vif_driver'
op|'='
name|'class_path'
op|'('
name|'FakeVifDriver'
op|')'
op|','
nl|'\n'
DECL|variable|volume_driver
name|'volume_driver'
op|'='
name|'class_path'
op|'('
name|'FakeVolumeDriver'
op|')'
op|','
nl|'\n'
DECL|variable|group
name|'group'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_baremetal_stuff
name|'def'
name|'_create_baremetal_stuff'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'context'
op|'='
name|'test_utils'
op|'.'
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_create'
op|'('
name|'context'
op|','
name|'NODE'
op|')'
newline|'\n'
name|'for'
name|'nic'
name|'in'
name|'NICS'
op|':'
newline|'\n'
indent|'        '
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'node'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'nic'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'nic'
op|'['
string|"'datapath_id'"
op|']'
op|','
nl|'\n'
name|'nic'
op|'['
string|"'port_no'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'node'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BaremetalDriverSpawnTestCase
dedent|''
name|'class'
name|'BaremetalDriverSpawnTestCase'
op|'('
name|'base'
op|'.'
name|'Database'
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
name|'BaremetalDriverSpawnTestCase'
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
op|'**'
name|'COMMON_FLAGS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
op|'**'
name|'BAREMETAL_FLAGS'
op|')'
newline|'\n'
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'node'
op|'='
name|'_create_baremetal_stuff'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node_id'
op|'='
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'test_utils'
op|'.'
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'test_utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network_info'
op|'='
name|'test_utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'block_device_info'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'image_meta'
op|'='
name|'test_utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'bm_driver'
op|'.'
name|'BareMetalDriver'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'kwargs'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'image_meta'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|'('
string|"'/foo'"
op|','
string|"'bar'"
op|')'
op|','
op|'('
string|"'/abc'"
op|','
string|"'xyz'"
op|')'
op|']'
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"'testpass'"
op|','
nl|'\n'
name|'network_info'
op|'='
name|'self'
op|'.'
name|'network_info'
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'self'
op|'.'
name|'block_device_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'fake_image'
op|'.'
name|'FakeImageService_reset'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ok
dedent|''
name|'def'
name|'test_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'node'"
op|']'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|'('
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'['
string|"'instance_uuid'"
op|']'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'node'
op|'['
string|"'task_state'"
op|']'
op|','
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_without_node
dedent|''
name|'def'
name|'test_without_node'
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
nl|'\n'
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|','
nl|'\n'
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_node_not_found
dedent|''
name|'def'
name|'test_node_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'node'"
op|']'
op|'='
string|'"123456789"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|','
nl|'\n'
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_node_in_use
dedent|''
name|'def'
name|'test_node_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'node'"
op|']'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node_id'
op|','
nl|'\n'
op|'{'
string|"'instance_uuid'"
op|':'
string|"'something'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'spawn'
op|','
nl|'\n'
op|'**'
name|'self'
op|'.'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'BaremetalDriverTestCase'
op|'('
name|'test_virt_drivers'
op|'.'
name|'_VirtDriverTestCase'
op|','
nl|'\n'
DECL|class|BaremetalDriverTestCase
name|'base'
op|'.'
name|'Database'
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
name|'BaremetalDriverTestCase'
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
name|'driver_module'
op|'='
string|"'nova.virt.baremetal.BareMetalDriver'"
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
op|'**'
name|'COMMON_FLAGS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node'
op|'='
name|'_create_baremetal_stuff'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node_id'
op|'='
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'fake_image'
op|'.'
name|'FakeImageService_reset'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_running_instance
dedent|''
name|'def'
name|'_get_running_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ref'
op|'='
name|'test_utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'instance_ref'
op|'['
string|"'node'"
op|']'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'network_info'
op|'='
name|'test_utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'image_info'
op|'='
name|'test_utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'spawn'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'instance_ref'
op|','
name|'image_info'
op|','
nl|'\n'
op|'['
op|']'
op|','
string|"'herp'"
op|','
name|'network_info'
op|'='
name|'network_info'
op|')'
newline|'\n'
name|'return'
name|'instance_ref'
op|','
name|'network_info'
newline|'\n'
nl|'\n'
DECL|member|test_loading_baremetal_drivers
dedent|''
name|'def'
name|'test_loading_baremetal_drivers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'fake'
newline|'\n'
name|'drv'
op|'='
name|'bm_driver'
op|'.'
name|'BareMetalDriver'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'drv'
op|'.'
name|'baremetal_nodes'
op|','
name|'fake'
op|'.'
name|'Fake'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'drv'
op|'.'
name|'_vif_driver'
op|','
name|'FakeVifDriver'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'drv'
op|'.'
name|'_firewall_driver'
op|','
name|'FakeFirewallDriver'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'drv'
op|'.'
name|'_volume_driver'
op|','
name|'FakeVolumeDriver'
op|')'
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
name|'self'
op|'.'
name|'flags'
op|'('
name|'instance_type_extra_specs'
op|'='
op|'['
string|"'cpu_arch:x86_64'"
op|','
nl|'\n'
string|"'x:123'"
op|','
nl|'\n'
string|"'y:456'"
op|','
op|']'
op|')'
newline|'\n'
name|'drv'
op|'='
name|'bm_driver'
op|'.'
name|'BareMetalDriver'
op|'('
name|'None'
op|')'
newline|'\n'
name|'cap_list'
op|'='
name|'drv'
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
name|'cap_list'
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
name|'cap_list'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'cap'
op|'='
name|'cap_list'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cap'
op|'['
string|"'cpu_arch'"
op|']'
op|','
string|"'x86_64'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cap'
op|'['
string|"'x'"
op|']'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cap'
op|'['
string|"'y'"
op|']'
op|','
string|"'456'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cap'
op|'['
string|"'hypervisor_type'"
op|']'
op|','
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'cap'
op|'['
string|"'driver'"
op|']'
op|','
nl|'\n'
string|"'nova.virt.baremetal.fake.Fake'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
