begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
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
string|'"""Tests for baremetal virtual power driver."""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
name|'processutils'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'base'
name|'as'
name|'bm_db_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'utils'
name|'as'
name|'bm_db_utils'
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
name|'virtual_power_driver'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'powervm'
op|'.'
name|'common'
name|'as'
name|'connection'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|COMMON_FLAGS
name|'COMMON_FLAGS'
op|'='
name|'dict'
op|'('
nl|'\n'
DECL|variable|firewall_driver
name|'firewall_driver'
op|'='
string|"'nova.virt.baremetal.fake.FakeFirewallDriver'"
op|','
nl|'\n'
DECL|variable|host
name|'host'
op|'='
string|"'test_host'"
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
string|"'nova.virt.baremetal.pxe.PXE'"
op|','
nl|'\n'
DECL|variable|instance_type_extra_specs
name|'instance_type_extra_specs'
op|'='
op|'['
string|"'cpu_arch:test'"
op|','
string|"'test_spec:test_value'"
op|']'
op|','
nl|'\n'
DECL|variable|power_manager
name|'power_manager'
op|'='
nl|'\n'
string|"'nova.virt.baremetal.virtual_power_driver.VirtualPowerManager'"
op|','
nl|'\n'
DECL|variable|vif_driver
name|'vif_driver'
op|'='
string|"'nova.virt.baremetal.fake.FakeVifDriver'"
op|','
nl|'\n'
DECL|variable|volume_driver
name|'volume_driver'
op|'='
string|"'nova.virt.baremetal.fake.FakeVolumeDriver'"
op|','
nl|'\n'
DECL|variable|virtual_power_ssh_host
name|'virtual_power_ssh_host'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|virtual_power_type
name|'virtual_power_type'
op|'='
string|"'vbox'"
op|','
nl|'\n'
DECL|variable|virtual_power_host_user
name|'virtual_power_host_user'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|virtual_power_host_pass
name|'virtual_power_host_pass'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|virtual_power_host_key
name|'virtual_power_host_key'
op|'='
name|'None'
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
DECL|class|BareMetalVPDTestCase
name|'class'
name|'BareMetalVPDTestCase'
op|'('
name|'bm_db_base'
op|'.'
name|'BMDBTestCase'
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
name|'BareMetalVPDTestCase'
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
nl|'\n'
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
name|'context'
op|'='
name|'utils'
op|'.'
name|'get_test_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_block_device_info'
op|'='
name|'None'
op|','
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_network_info'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
op|','
newline|'\n'
name|'self'
op|'.'
name|'node_info'
op|'='
name|'bm_db_utils'
op|'.'
name|'new_bm_node'
op|'('
nl|'\n'
name|'id'
op|'='
number|'123'
op|','
nl|'\n'
name|'service_host'
op|'='
string|"'test_host'"
op|','
nl|'\n'
name|'cpus'
op|'='
number|'2'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2048'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nic_info'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'11:11:11:11:11:11'"
op|','
string|"'datapath_id'"
op|':'
string|"'0x1'"
op|','
nl|'\n'
string|"'port_no'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
string|"'22:22:22:22:22:22'"
op|','
string|"'datapath_id'"
op|':'
string|"'0x2'"
op|','
nl|'\n'
string|"'port_no'"
op|':'
number|'2'
op|'}'
op|','
nl|'\n'
op|']'
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
DECL|member|_create_node
dedent|''
name|'def'
name|'_create_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'node'
op|'='
name|'db'
op|'.'
name|'bm_node_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node_info'
op|')'
newline|'\n'
name|'for'
name|'nic'
name|'in'
name|'self'
op|'.'
name|'nic_info'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
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
op|','
nl|'\n'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'instance'
op|'['
string|"'node'"
op|']'
op|'='
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_pm
dedent|''
name|'def'
name|'_create_pm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pm'
op|'='
name|'virtual_power_driver'
op|'.'
name|'VirtualPowerManager'
op|'('
nl|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'node'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'pm'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VPDMissingOptionsTestCase
dedent|''
dedent|''
name|'class'
name|'VPDMissingOptionsTestCase'
op|'('
name|'BareMetalVPDTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_get_conn_missing_options
indent|'    '
name|'def'
name|'test_get_conn_missing_options'
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
name|'virtual_power_ssh_host'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_user'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_pass'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'None'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_ssh_host'
op|'='
string|"'127.0.0.1'"
op|','
name|'group'
op|'='
string|'"baremetal"'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_conn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_user'
op|'='
string|"'user'"
op|','
name|'group'
op|'='
string|'"baremetal"'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_conn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VPDClassMethodsTestCase
dedent|''
dedent|''
name|'class'
name|'VPDClassMethodsTestCase'
op|'('
name|'BareMetalVPDTestCase'
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
name|'VPDClassMethodsTestCase'
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
name|'virtual_power_ssh_host'
op|'='
string|"'127.0.0.1'"
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_user'
op|'='
string|"'user'"
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_pass'
op|'='
string|"'password'"
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_conn_success_pass
dedent|''
name|'def'
name|'test_get_conn_success_pass'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_conn'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'connection'
op|','
string|"'ssh_connect'"
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'ssh_connect'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'self'
op|'.'
name|'_conn'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_set_connection'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'host'
op|','
string|"'127.0.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'username'
op|','
string|"'user'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'password'
op|','
string|"'password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'keyfile'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_conn_success_key
dedent|''
name|'def'
name|'test_get_conn_success_key'
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
name|'virtual_power_host_pass'
op|'='
string|"''"
op|','
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'virtual_power_host_key'
op|'='
string|"'/id_rsa_file.txt'"
op|','
nl|'\n'
name|'group'
op|'='
string|'"baremetal"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_conn'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'connection'
op|','
string|"'ssh_connect'"
op|')'
newline|'\n'
name|'connection'
op|'.'
name|'ssh_connect'
op|'('
name|'mox'
op|'.'
name|'IsA'
op|'('
name|'self'
op|'.'
name|'_conn'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_set_connection'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'host'
op|','
string|"'127.0.0.1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'username'
op|','
string|"'user'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'password'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'connection_data'
op|'.'
name|'keyfile'
op|','
string|"'/id_rsa_file.txt'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_full_node_list
dedent|''
name|'def'
name|'test_get_full_node_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'list_cmd'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"testNode"'
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
name|'name'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_full_node_list'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'name'
op|','
string|"'testNode'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_node
dedent|''
name|'def'
name|'test_check_for_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_get_full_node_list'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_full_node_list'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'"testNode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'get_node_macs'
op|'.'
name|'replace'
op|'('
string|"'{_NodeName_}'"
op|','
string|"'testNode'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'"111111111111"'
op|','
string|'"ffeeddccbbaa"'
op|']'
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
name|'name'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'name'
op|','
string|'\'"testNode"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_for_node_not_found
dedent|''
name|'def'
name|'test_check_for_node_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_get_full_node_list'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_get_full_node_list'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'"testNode"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'get_node_macs'
op|'.'
name|'replace'
op|'('
string|"'{_NodeName_}'"
op|','
string|"'testNode'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'"ffeeddccbbaa"'
op|']'
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
name|'name'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'name'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_activate_node
dedent|''
name|'def'
name|'test_activate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'\'"testNode"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'start_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Started"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'activate_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'active'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_activate_node_fail
dedent|''
name|'def'
name|'test_activate_node_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'\'"testNode"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'start_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Started"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'activate_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deactivate_node
dedent|''
name|'def'
name|'test_deactivate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'\'"testNode"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'stop_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Stopped"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'deactivate_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'deleted'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deactivate_node_fail
dedent|''
name|'def'
name|'test_deactivate_node_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'\'"testNode"\''
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'stop_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Stopped"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'deactivate_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot_node
dedent|''
name|'def'
name|'test_reboot_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'reboot_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Restarted"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'reboot_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'active'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_reboot_node_fail
dedent|''
name|'def'
name|'test_reboot_node_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'is_power_on'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'reboot_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|'"Restarted"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
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
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'reboot_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_power_on
dedent|''
name|'def'
name|'test_is_power_on'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'list_running_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_matched_name'
op|'='
string|"'testNode'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_power_on_fail
dedent|''
name|'def'
name|'test_is_power_on_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NodeNotFound'
op|','
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_power_on_match_subname
dedent|''
name|'def'
name|'test_is_power_on_match_subname'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_run_command'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_vp_cmd'
op|'.'
name|'list_running_cmd'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode01"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_matched_name'
op|'='
string|'\'"testNode"\''
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'is_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_command
dedent|''
name|'def'
name|'test_run_command'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_set_connection'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'processutils'
op|','
string|"'ssh_execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_set_connection'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'processutils'
op|'.'
name|'ssh_execute'
op|'('
name|'None'
op|','
string|"'/usr/bin/VBoxManage test return'"
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
string|'"test\\nreturn"'
op|','
string|'""'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_matched_name'
op|'='
string|"'testNode'"
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
string|'"test return"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
op|'['
string|"'test'"
op|','
string|"'return'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_command_raises_exception
dedent|''
name|'def'
name|'test_run_command_raises_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_set_connection'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'processutils'
op|','
string|"'ssh_execute'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_set_connection'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'processutils'
op|'.'
name|'ssh_execute'
op|'('
name|'None'
op|','
string|"'/usr/bin/VBoxManage test return'"
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
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
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_run_command'
op|'('
string|'"test return"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_activate_node_with_exception
dedent|''
name|'def'
name|'test_activate_node_with_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_pm'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'pm'
op|','
string|"'_check_for_node'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'processutils'
op|','
string|"'ssh_execute'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
string|'\'"testNode"\''
op|']'
op|')'
newline|'\n'
name|'processutils'
op|'.'
name|'ssh_execute'
op|'('
string|"'test'"
op|','
string|"'/usr/bin/VBoxManage startvm '"
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|')'
newline|'\n'
name|'processutils'
op|'.'
name|'ssh_execute'
op|'('
string|"'test'"
op|','
string|"'/usr/bin/VBoxManage list runningvms'"
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
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
name|'self'
op|'.'
name|'pm'
op|'.'
name|'_connection'
op|'='
string|"'test'"
newline|'\n'
name|'state'
op|'='
name|'self'
op|'.'
name|'pm'
op|'.'
name|'activate_node'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'state'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
