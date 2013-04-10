begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011-2013 University of Southern California / ISI'
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
string|'"""Tests for baremetal tilera driver."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
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
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
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
name|'as'
name|'bm_db_base'
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
name|'as'
name|'bm_db_utils'
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
name|'tilera'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'utils'
name|'as'
name|'bm_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'api'
name|'as'
name|'disk_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'fake'
name|'as'
name|'fake_virt'
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
string|"'nova.virt.baremetal.tilera.Tilera'"
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
string|"'nova.virt.baremetal.fake.FakePowerManager'"
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
DECL|class|BareMetalTileraTestCase
name|'class'
name|'BareMetalTileraTestCase'
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
name|'BareMetalTileraTestCase'
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
name|'self'
op|'.'
name|'driver'
op|'='
name|'tilera'
op|'.'
name|'Tilera'
op|'('
name|'fake_virt'
op|'.'
name|'FakeVirtAPI'
op|'('
op|')'
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
name|'addCleanup'
op|'('
name|'fake_image'
op|'.'
name|'FakeImageService_reset'
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
name|'service_host'
op|'='
string|"'test_host'"
op|','
nl|'\n'
name|'cpus'
op|'='
number|'4'
op|','
nl|'\n'
name|'memory_mb'
op|'='
number|'2048'
op|','
nl|'\n'
name|'prov_mac_address'
op|'='
string|"'11:11:11:11:11:11'"
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
string|"'22:22:22:22:22:22'"
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
string|"'33:33:33:33:33:33'"
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
name|'self'
op|'.'
name|'spawn_params'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'admin_password'
op|'='
string|"'test_pass'"
op|','
nl|'\n'
name|'block_device_info'
op|'='
name|'self'
op|'.'
name|'test_block_device_info'
op|','
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'image_meta'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
name|'None'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|','
nl|'\n'
name|'injected_files'
op|'='
op|'['
op|'('
string|"'/fake/path'"
op|','
string|"'hello world'"
op|')'
op|']'
op|','
nl|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'self'
op|'.'
name|'test_network_info'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TileraClassMethodsTestCase
dedent|''
dedent|''
name|'class'
name|'TileraClassMethodsTestCase'
op|'('
name|'BareMetalTileraTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_build_network_config
indent|'    '
name|'def'
name|'test_build_network_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'net'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
number|'1'
op|')'
newline|'\n'
name|'config'
op|'='
name|'tilera'
op|'.'
name|'build_network_config'
op|'('
name|'net'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'eth0'"
op|','
name|'config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'eth1'"
op|','
name|'config'
op|')'
newline|'\n'
nl|'\n'
name|'net'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
number|'2'
op|')'
newline|'\n'
name|'config'
op|'='
name|'tilera'
op|'.'
name|'build_network_config'
op|'('
name|'net'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'eth0'"
op|','
name|'config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'eth1'"
op|','
name|'config'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_build_network_config_dhcp
dedent|''
name|'def'
name|'test_build_network_config_dhcp'
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
nl|'\n'
name|'net_config_template'
op|'='
string|"'$pybasedir/nova/virt/baremetal/'"
nl|'\n'
string|"'net-dhcp.ubuntu.template'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'net'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'net'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'config'
op|'='
name|'tilera'
op|'.'
name|'build_network_config'
op|'('
name|'net'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'iface eth0 inet dhcp'"
op|','
name|'config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'address 1.2.3.4'"
op|','
name|'config'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_build_network_config_static
dedent|''
name|'def'
name|'test_build_network_config_static'
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
nl|'\n'
name|'net_config_template'
op|'='
string|"'$pybasedir/nova/virt/baremetal/'"
nl|'\n'
string|"'net-static.ubuntu.template'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'net'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
op|')'
newline|'\n'
name|'net'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'ips'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'ip'"
op|']'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'config'
op|'='
name|'tilera'
op|'.'
name|'build_network_config'
op|'('
name|'net'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'iface eth0 inet static'"
op|','
name|'config'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'address 1.2.3.4'"
op|','
name|'config'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_dir_path
dedent|''
name|'def'
name|'test_image_dir_path'
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
nl|'\n'
name|'tilera'
op|'.'
name|'get_image_dir_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
string|"'instance-00000001'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_file_path
dedent|''
name|'def'
name|'test_image_file_path'
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
nl|'\n'
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'instances_path'
op|','
string|"'instance-00000001'"
op|','
string|"'disk'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_tilera_nfs_path
dedent|''
name|'def'
name|'test_tilera_nfs_path'
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
name|'node'
op|'['
string|"'id'"
op|']'
op|'='
string|"'123'"
newline|'\n'
name|'tilera_nfs_dir'
op|'='
string|'"fs_"'
op|'+'
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'tilera'
op|'.'
name|'get_tilera_nfs_path'
op|'('
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
nl|'\n'
name|'tilera_nfs_dir'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_partition_sizes
dedent|''
name|'def'
name|'test_get_partition_sizes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# default "kinda.big" instance'
nl|'\n'
indent|'        '
name|'sizes'
op|'='
name|'tilera'
op|'.'
name|'get_partition_sizes'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sizes'
op|'['
number|'0'
op|']'
op|','
number|'40960'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sizes'
op|'['
number|'1'
op|']'
op|','
number|'1024'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_not_zero
dedent|''
name|'def'
name|'test_swap_not_zero'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# override swap to 0'
nl|'\n'
indent|'        '
name|'instance_type'
op|'='
name|'utils'
op|'.'
name|'get_test_instance_type'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'instance_type'
op|'['
string|"'swap'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
name|'utils'
op|'.'
name|'get_test_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_type'
op|')'
newline|'\n'
nl|'\n'
name|'sizes'
op|'='
name|'tilera'
op|'.'
name|'get_partition_sizes'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sizes'
op|'['
number|'0'
op|']'
op|','
number|'40960'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'sizes'
op|'['
number|'1'
op|']'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_tftp_image_info
dedent|''
name|'def'
name|'test_get_tftp_image_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Tilera case needs only kernel_id.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'kernel_id'"
op|']'
op|'='
string|"'aaaa'"
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid'"
newline|'\n'
nl|'\n'
comment|'# Here, we confirm both that kernel_id was set'
nl|'\n'
comment|'# and that the proper paths are getting set for all of them'
nl|'\n'
name|'base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'res'
op|'='
name|'tilera'
op|'.'
name|'get_tftp_image_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'kernel'"
op|':'
op|'['
string|"'aaaa'"
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base'
op|','
string|"'kernel'"
op|')'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TileraPrivateMethodsTestCase
dedent|''
dedent|''
name|'class'
name|'TileraPrivateMethodsTestCase'
op|'('
name|'BareMetalTileraTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_collect_mac_addresses
indent|'    '
name|'def'
name|'test_collect_mac_addresses'
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
name|'address_list'
op|'='
op|'['
name|'nic'
op|'['
string|"'address'"
op|']'
name|'for'
name|'nic'
name|'in'
name|'self'
op|'.'
name|'nic_info'
op|']'
newline|'\n'
name|'address_list'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'macs'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_collect_mac_addresses'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'macs'
op|','
name|'address_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cache_tftp_images
dedent|''
name|'def'
name|'test_cache_tftp_images'
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
string|"'kernel_id'"
op|']'
op|'='
string|"'aaaa'"
newline|'\n'
name|'image_info'
op|'='
name|'tilera'
op|'.'
name|'get_tftp_image_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|','
string|"'makedirs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tftp_root'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'for'
name|'uuid'
op|','
name|'path'
name|'in'
op|'['
name|'image_info'
op|'['
name|'label'
op|']'
name|'for'
name|'label'
name|'in'
name|'image_info'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_cache_tftp_images'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'image_info'
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
DECL|member|test_cache_image
dedent|''
name|'def'
name|'test_cache_image'
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
name|'os'
op|','
string|"'makedirs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'tilera'
op|'.'
name|'get_image_dir_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
name|'self'
op|'.'
name|'instance'
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
nl|'\n'
name|'image_meta'
op|'='
name|'utils'
op|'.'
name|'get_test_image_info'
op|'('
nl|'\n'
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
name|'driver'
op|'.'
name|'_cache_image'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
name|'image_meta'
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
DECL|member|test_inject_into_image
dedent|''
name|'def'
name|'test_inject_into_image'
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
name|'files'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|'='
string|"'fake hostname'"
newline|'\n'
name|'files'
op|'.'
name|'append'
op|'('
op|'('
string|"'/etc/hostname'"
op|','
string|"'fake hostname'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|'='
string|"'fake ssh key'"
newline|'\n'
name|'net_info'
op|'='
name|'utils'
op|'.'
name|'get_test_network_info'
op|'('
number|'1'
op|')'
newline|'\n'
name|'net'
op|'='
name|'tilera'
op|'.'
name|'build_network_config'
op|'('
name|'net_info'
op|')'
newline|'\n'
name|'admin_password'
op|'='
string|"'fake password'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'disk_api'
op|','
string|"'inject_data'"
op|')'
newline|'\n'
name|'disk_api'
op|'.'
name|'inject_data'
op|'('
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'image'
op|'='
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|','
nl|'\n'
name|'key'
op|'='
string|"'fake ssh key'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'None'
op|','
nl|'\n'
name|'partition'
op|'='
name|'None'
op|','
nl|'\n'
name|'net'
op|'='
name|'net'
op|','
nl|'\n'
name|'files'
op|'='
name|'files'
op|','
nl|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_inject_into_image'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'net_info'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
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
nl|'\n'
DECL|class|TileraPublicMethodsTestCase
dedent|''
dedent|''
name|'class'
name|'TileraPublicMethodsTestCase'
op|'('
name|'BareMetalTileraTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_cache_images
indent|'    '
name|'def'
name|'test_cache_images'
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
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'tilera'
op|','
string|'"get_tftp_image_info"'
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
name|'driver'
op|','
string|'"_cache_tftp_images"'
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
name|'driver'
op|','
string|'"_cache_image"'
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
name|'driver'
op|','
string|'"_inject_into_image"'
op|')'
newline|'\n'
nl|'\n'
name|'tilera'
op|'.'
name|'get_tftp_image_info'
op|'('
name|'self'
op|'.'
name|'instance'
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
name|'driver'
op|'.'
name|'_cache_tftp_images'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_cache_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_inject_into_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'self'
op|'.'
name|'test_network_info'
op|','
name|'None'
op|','
string|"''"
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'cache_images'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'admin_password'
op|'='
string|"''"
op|','
nl|'\n'
name|'image_meta'
op|'='
op|'['
op|']'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'None'
op|','
nl|'\n'
name|'network_info'
op|'='
name|'self'
op|'.'
name|'test_network_info'
op|','
nl|'\n'
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
DECL|member|test_destroy_images
dedent|''
name|'def'
name|'test_destroy_images'
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
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'unlink_without_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'rmtree_without_raise'"
op|')'
newline|'\n'
nl|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'rmtree_without_raise'
op|'('
name|'tilera'
op|'.'
name|'get_image_dir_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'destroy_images'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
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
DECL|member|test_activate_bootloader_passes_details
dedent|''
name|'def'
name|'test_activate_bootloader_passes_details'
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
name|'image_info'
op|'='
op|'{'
nl|'\n'
string|"'kernel'"
op|':'
op|'['
name|'None'
op|','
string|"'cccc'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'iqn'
op|'='
string|'"iqn-%s"'
op|'%'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'tilera_config'
op|'='
string|"'this is a fake tilera config'"
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'tilera_path'
op|'='
name|'tilera'
op|'.'
name|'get_tilera_nfs_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'image_path'
op|'='
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'tilera'
op|','
string|"'get_tftp_image_info'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'tilera'
op|','
string|"'get_partition_sizes'"
op|')'
newline|'\n'
nl|'\n'
name|'tilera'
op|'.'
name|'get_tftp_image_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'image_info'
op|')'
newline|'\n'
name|'tilera'
op|'.'
name|'get_partition_sizes'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
number|'0'
op|','
number|'0'
op|')'
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
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_bootloader'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_activate_and_deactivate_bootloader
dedent|''
name|'def'
name|'test_activate_and_deactivate_bootloader'
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid'"
newline|'\n'
name|'tilera_path'
op|'='
name|'tilera'
op|'.'
name|'get_tilera_nfs_path'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'image_path'
op|'='
name|'tilera'
op|'.'
name|'get_image_file_path'
op|'('
name|'self'
op|'.'
name|'instance'
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
nl|'\n'
comment|'# activate and deactivate the bootloader'
nl|'\n'
comment|'# and check the deployment task_state in the database'
nl|'\n'
name|'row'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'row'
op|'['
string|"'deploy_key'"
op|']'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_bootloader'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'row'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'row'
op|'['
string|"'deploy_key'"
op|']'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'deactivate_bootloader'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'row'
op|'='
name|'db'
op|'.'
name|'bm_node_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'row'
op|'['
string|"'deploy_key'"
op|']'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deactivate_bootloader_for_nonexistent_instance
dedent|''
name|'def'
name|'test_deactivate_bootloader_for_nonexistent_instance'
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
name|'node'
op|'['
string|"'id'"
op|']'
op|'='
string|"'fake-node-id'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'unlink_without_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'rmtree_without_raise'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'tilera'
op|','
string|"'get_tftp_image_info'"
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
name|'driver'
op|','
string|"'_collect_mac_addresses'"
op|')'
newline|'\n'
nl|'\n'
name|'tilera_path'
op|'='
name|'tilera'
op|'.'
name|'get_tilera_nfs_path'
op|'('
name|'self'
op|'.'
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'tilera'
op|'.'
name|'get_tftp_image_info'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_collect_mac_addresses'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'db_exc'
op|'.'
name|'DBError'
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'deactivate_bootloader'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
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
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|'='
string|"'fake-uuid'"
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'DEPLOYING'
op|','
nl|'\n'
string|"'instance_uuid'"
op|':'
string|"'fake-uuid'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# test DEPLOYDONE'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'DEPLOYDONE'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_node'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# test no deploy -- state is just ACTIVE'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
nl|'\n'
op|'{'
string|"'task_state'"
op|':'
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_node'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# test node gone'
nl|'\n'
name|'db'
op|'.'
name|'bm_node_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceDeployFailure'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'activate_node'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'node'
op|','
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
