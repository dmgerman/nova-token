begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata'
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
string|'"""\nTests for Block Device utility functions.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'matchers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BlockDeviceTestCase
name|'class'
name|'BlockDeviceTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_properties
indent|'    '
name|'def'
name|'test_properties'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root_device0'
op|'='
string|"'/dev/sda'"
newline|'\n'
name|'root_device1'
op|'='
string|"'/dev/sdb'"
newline|'\n'
name|'mappings'
op|'='
op|'['
op|'{'
string|"'virtual'"
op|':'
string|"'root'"
op|','
nl|'\n'
string|"'device'"
op|':'
name|'root_device0'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'properties0'
op|'='
op|'{'
string|"'mappings'"
op|':'
name|'mappings'
op|'}'
newline|'\n'
name|'properties1'
op|'='
op|'{'
string|"'mappings'"
op|':'
name|'mappings'
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
name|'root_device1'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'properties_root_device_name'
op|'('
op|'{'
op|'}'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'properties_root_device_name'
op|'('
name|'properties0'
op|')'
op|','
nl|'\n'
name|'root_device0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'properties_root_device_name'
op|'('
name|'properties1'
op|')'
op|','
nl|'\n'
name|'root_device1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ephemeral
dedent|''
name|'def'
name|'test_ephemeral'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'ephemeral'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'ephemeral0'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'ephemeral1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'ephemeral11'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'root'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'swap'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_ephemeral'
op|'('
string|"'/dev/sda1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'ephemeral_num'
op|'('
string|"'ephemeral0'"
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'ephemeral_num'
op|'('
string|"'ephemeral1'"
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'ephemeral_num'
op|'('
string|"'ephemeral11'"
op|')'
op|','
number|'11'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'ephemeral'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'ephemeral0'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'ephemeral1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'swap'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'root'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
string|"'/dev/sda1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mappings_prepend_dev
dedent|''
name|'def'
name|'test_mappings_prepend_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mapping'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ami'"
op|','
string|"'device'"
op|':'
string|"'/dev/sda'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'root'"
op|','
string|"'device'"
op|':'
string|"'sda'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral0'"
op|','
string|"'device'"
op|':'
string|"'sdb'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'swap'"
op|','
string|"'device'"
op|':'
string|"'sdc'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral1'"
op|','
string|"'device'"
op|':'
string|"'sdd'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral2'"
op|','
string|"'device'"
op|':'
string|"'sde'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ami'"
op|','
string|"'device'"
op|':'
string|"'/dev/sda'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'root'"
op|','
string|"'device'"
op|':'
string|"'sda'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral0'"
op|','
string|"'device'"
op|':'
string|"'/dev/sdb'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'swap'"
op|','
string|"'device'"
op|':'
string|"'/dev/sdc'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral1'"
op|','
string|"'device'"
op|':'
string|"'/dev/sdd'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'ephemeral2'"
op|','
string|"'device'"
op|':'
string|"'/dev/sde'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'prepended'
op|'='
name|'block_device'
op|'.'
name|'mappings_prepend_dev'
op|'('
name|'mapping'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'prepended'
op|'.'
name|'sort'
op|'('
op|')'
op|','
name|'expected'
op|'.'
name|'sort'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_strip_dev
dedent|''
name|'def'
name|'test_strip_dev'
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
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
string|"'/dev/sda'"
op|')'
op|','
string|"'sda'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
string|"'sda'"
op|')'
op|','
string|"'sda'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_strip_prefix
dedent|''
name|'def'
name|'test_strip_prefix'
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
name|'block_device'
op|'.'
name|'strip_prefix'
op|'('
string|"'/dev/sda'"
op|')'
op|','
string|"'a'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'strip_prefix'
op|'('
string|"'a'"
op|')'
op|','
string|"'a'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'strip_prefix'
op|'('
string|"'xvda'"
op|')'
op|','
string|"'a'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'block_device'
op|'.'
name|'strip_prefix'
op|'('
string|"'vda'"
op|')'
op|','
string|"'a'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_in_mapping
dedent|''
name|'def'
name|'test_volume_in_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'swap'
op|'='
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'ephemerals'
op|'='
op|'['
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'num'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral2'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdd'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
op|'['
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sde'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sdf'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|']'
newline|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda'"
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'swap'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
name|'ephemerals'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
name|'block_device_mapping'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|_assert_volume_in_mapping
name|'def'
name|'_assert_volume_in_mapping'
op|'('
name|'device_name'
op|','
name|'true_or_false'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'in_mapping'
op|'='
name|'block_device'
op|'.'
name|'volume_in_mapping'
op|'('
nl|'\n'
name|'device_name'
op|','
name|'block_device_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'in_mapping'
op|','
name|'true_or_false'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_assert_volume_in_mapping'
op|'('
string|"'sda'"
op|','
name|'False'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdb'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdc1'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdd'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sde'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdf'"
op|','
name|'True'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdg'"
op|','
name|'False'
op|')'
newline|'\n'
name|'_assert_volume_in_mapping'
op|'('
string|"'sdh1'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestBlockDeviceDict
dedent|''
dedent|''
name|'class'
name|'TestBlockDeviceDict'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestBlockDeviceDict'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'BDM'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api_mapping'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdb1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'blank'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'guest_format'"
op|':'
string|"'swap'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'blank'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake-volume-id-1'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'4'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake-snapshot-id-1'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'5'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdc'"
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'new_mapping'
op|'='
op|'['
nl|'\n'
name|'BDM'
op|'('
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdb1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'blank'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'guest_format'"
op|':'
string|"'swap'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
name|'BDM'
op|'('
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'blank'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'local'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
name|'BDM'
op|'('
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake-volume-id-1'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
name|'BDM'
op|'('
op|'{'
string|"'id'"
op|':'
number|'4'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'source_type'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'destination_type'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'fake-snapshot-id-1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake-volume-id-2'"
op|','
nl|'\n'
string|"'boot_index'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
name|'BDM'
op|'('
op|'{'
string|"'id'"
op|':'
number|'5'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdc'"
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'legacy_mapping'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdb1'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'swap'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'2'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'3'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake-volume-id-1'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'4'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sda2'"
op|','
nl|'\n'
string|"'connection_info'"
op|':'
string|'"{\'fake\': \'connection_info\'}"'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
string|"'fake-snapshot-id-1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake-volume-id-2'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'5'
op|','
string|"'instance_uuid'"
op|':'
string|"'fake-instance'"
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/vdc'"
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_init
dedent|''
name|'def'
name|'test_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_validate
indent|'        '
name|'def'
name|'fake_validate'
op|'('
name|'obj'
op|','
name|'dct'
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
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
string|"'_fields'"
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'field1'"
op|','
string|"'field2'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
string|"'_db_only_fields'"
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"'db_field1'"
op|','
string|"'db_field2'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
string|"'_validate'"
op|','
nl|'\n'
name|'fake_validate'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure db fields are not picked up if they are not'
nl|'\n'
comment|'# in the original dict'
nl|'\n'
name|'dev_dict'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
op|'{'
string|"'field1'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'field2'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'db_field1'"
op|':'
string|"'baz'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'db_field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'db_field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure all expected fields are defaulted'
nl|'\n'
name|'dev_dict'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
op|'{'
string|"'field1'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'dev_dict'
op|'['
string|"'field2'"
op|']'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'db_field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'db_field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
nl|'\n'
comment|'# Unless they are not meant to be'
nl|'\n'
name|'dev_dict'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
op|'{'
string|"'field1'"
op|':'
string|"'foo'"
op|'}'
op|','
nl|'\n'
name|'do_not_default'
op|'='
name|'set'
op|'('
op|'['
string|"'field2'"
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'db_field1'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
string|"'db_field2'"
name|'in'
name|'dev_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_validate
dedent|''
name|'def'
name|'test_validate'
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
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
op|'{'
string|"'bogus_field'"
op|':'
string|"'lame_val'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'lame_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'del'
name|'lame_bdm'
op|'['
string|"'source_type'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
name|'lame_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'lame_bdm'
op|'['
string|"'no_device'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'lame_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'lame_dev_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'lame_dev_bdm'
op|'['
string|"'device_name'"
op|']'
op|'='
string|'"not a valid name"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
name|'lame_dev_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'lame_dev_bdm'
op|'['
string|"'device_name'"
op|']'
op|'='
string|'""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
name|'lame_dev_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'cool_volume_size_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'cool_volume_size_bdm'
op|'['
string|"'volume_size'"
op|']'
op|'='
string|"'42'"
newline|'\n'
name|'cool_volume_size_bdm'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
nl|'\n'
name|'cool_volume_size_bdm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'cool_volume_size_bdm'
op|'['
string|"'volume_size'"
op|']'
op|','
number|'42'
op|')'
newline|'\n'
nl|'\n'
name|'lame_volume_size_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'lame_volume_size_bdm'
op|'['
string|"'volume_size'"
op|']'
op|'='
string|"'some_non_int_string'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
name|'lame_volume_size_bdm'
op|')'
newline|'\n'
nl|'\n'
name|'truthy_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'truthy_bdm'
op|'['
string|"'delete_on_termination'"
op|']'
op|'='
string|"'1'"
newline|'\n'
name|'truthy_bdm'
op|'='
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'('
name|'truthy_bdm'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'truthy_bdm'
op|'['
string|"'delete_on_termination'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'verbose_bdm'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'verbose_bdm'
op|'['
string|"'boot_index'"
op|']'
op|'='
string|"'first'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidBDMFormat'
op|','
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|','
nl|'\n'
name|'verbose_bdm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_legacy
dedent|''
name|'def'
name|'test_from_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'legacy'
op|','
name|'new'
name|'in'
name|'zip'
op|'('
name|'self'
op|'.'
name|'legacy_mapping'
op|','
name|'self'
op|'.'
name|'new_mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertThat'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'.'
name|'from_legacy'
op|'('
name|'legacy'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'IsSubDictOf'
op|'('
name|'new'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_api
dedent|''
dedent|''
name|'def'
name|'test_from_api'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'api'
op|','
name|'new'
name|'in'
name|'zip'
op|'('
name|'self'
op|'.'
name|'api_mapping'
op|','
name|'self'
op|'.'
name|'new_mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'new'
op|'['
string|"'connection_info'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'new'
op|'['
string|"'snapshot_id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'new'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertThat'
op|'('
nl|'\n'
name|'block_device'
op|'.'
name|'BlockDeviceDict'
op|'.'
name|'from_api'
op|'('
name|'api'
op|')'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'IsSubDictOf'
op|'('
name|'new'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_legacy
dedent|''
dedent|''
name|'def'
name|'test_legacy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'legacy'
op|','
name|'new'
name|'in'
name|'zip'
op|'('
name|'self'
op|'.'
name|'legacy_mapping'
op|','
name|'self'
op|'.'
name|'new_mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertThat'
op|'('
nl|'\n'
name|'legacy'
op|','
nl|'\n'
name|'matchers'
op|'.'
name|'IsSubDictOf'
op|'('
name|'new'
op|'.'
name|'legacy'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_legacy_mapping
dedent|''
dedent|''
name|'def'
name|'test_legacy_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'got_legacy'
op|'='
name|'block_device'
op|'.'
name|'legacy_mapping'
op|'('
name|'self'
op|'.'
name|'new_mapping'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'legacy'
op|','
name|'expected'
name|'in'
name|'zip'
op|'('
name|'got_legacy'
op|','
name|'self'
op|'.'
name|'legacy_mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'expected'
op|','
name|'matchers'
op|'.'
name|'IsSubDictOf'
op|'('
name|'legacy'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
