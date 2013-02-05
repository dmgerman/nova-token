begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""Tests For miscellaneous util methods used with compute."""'
newline|'\n'
nl|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'api'
name|'as'
name|'network_api'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'notifier'
name|'import'
name|'test_notifier'
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
name|'fake_instance_actions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
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
DECL|class|ComputeValidateDeviceTestCase
name|'class'
name|'ComputeValidateDeviceTestCase'
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
name|'ComputeValidateDeviceTestCase'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
comment|'# check if test name includes "xen"'
nl|'\n'
name|'if'
string|"'xen'"
name|'in'
name|'self'
op|'.'
name|'id'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'compute_driver'
op|'='
string|"'xenapi.XenAPIDriver'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance'
op|'='
op|'{'
nl|'\n'
string|"'uuid'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/vda'"
op|','
nl|'\n'
string|"'default_ephemeral_device'"
op|':'
string|"'/dev/vdb'"
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_get
name|'def'
name|'fake_get'
op|'('
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'instance_type'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|','
nl|'\n'
name|'lambda'
name|'context'
op|','
name|'instance'
op|':'
name|'self'
op|'.'
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_device
dedent|''
name|'def'
name|'_validate_device'
op|'('
name|'self'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bdms'
op|'='
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'compute_utils'
op|'.'
name|'get_device_name_for_instance'
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
name|'bdms'
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_fake_bdm
name|'def'
name|'_fake_bdm'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'device_name'"
op|':'
name|'device'
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|test_wrap
dedent|''
name|'def'
name|'test_wrap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'letter'
name|'in'
name|'string'
op|'.'
name|'ascii_lowercase'
op|'['
number|'2'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vd'"
op|'+'
name|'letter'
op|')'
op|')'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdaa'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_wrap_plus_one
dedent|''
name|'def'
name|'test_wrap_plus_one'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'letter'
name|'in'
name|'string'
op|'.'
name|'ascii_lowercase'
op|'['
number|'2'
op|':'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'data'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vd'"
op|'+'
name|'letter'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'data'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vdaa'"
op|')'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdab'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_later
dedent|''
name|'def'
name|'test_later'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vdc'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vdd'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vde'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdf'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_gap
dedent|''
name|'def'
name|'test_gap'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vdc'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
string|"'/dev/vde'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdd'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_bdms
dedent|''
name|'def'
name|'test_no_bdms'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lxc_names_work
dedent|''
name|'def'
name|'test_lxc_names_work'
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
string|"'root_device_name'"
op|']'
op|'='
string|"'/dev/a'"
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'ephemeral_device_name'"
op|']'
op|'='
string|"'/dev/b'"
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/c'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_name_conversion
dedent|''
name|'def'
name|'test_name_conversion'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'data'
op|'='
op|'['
op|']'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
string|"'/dev/c'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdc'"
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
string|"'/dev/sdc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdc'"
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
string|"'/dev/xvdc'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_bdms
dedent|''
name|'def'
name|'test_invalid_bdms'
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
string|"'root_device_name'"
op|']'
op|'='
string|'"baddata"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidDevicePath'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_validate_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_device_prefix
dedent|''
name|'def'
name|'test_invalid_device_prefix'
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
name|'InvalidDevicePath'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_validate_device'
op|','
string|"'/baddata/vdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_device_in_use
dedent|''
name|'def'
name|'test_device_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'DevicePathInUse'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_validate_device'
op|','
string|"'/dev/vda'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'/dev/vda'"
op|','
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap
dedent|''
name|'def'
name|'test_swap'
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
string|"'default_swap_device'"
op|']'
op|'='
string|'"/dev/vdc"'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdd'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_no_ephemeral
dedent|''
name|'def'
name|'test_swap_no_ephemeral'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'default_ephemeral_device'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'default_swap_device'"
op|']'
op|'='
string|'"/dev/vdb"'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/vdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ephemeral_xenapi
dedent|''
name|'def'
name|'test_ephemeral_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_type'
op|'='
op|'{'
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|"'get_instance_type'"
op|','
nl|'\n'
name|'lambda'
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|':'
name|'self'
op|'.'
name|'instance_type'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/xvdc'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_xenapi
dedent|''
name|'def'
name|'test_swap_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_type'
op|'='
op|'{'
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'10'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|"'get_instance_type'"
op|','
nl|'\n'
name|'lambda'
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|':'
name|'self'
op|'.'
name|'instance_type'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/xvdb'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_and_ephemeral_xenapi
dedent|''
name|'def'
name|'test_swap_and_ephemeral_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_type'
op|'='
op|'{'
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'10'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|"'get_instance_type'"
op|','
nl|'\n'
name|'lambda'
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|':'
name|'self'
op|'.'
name|'instance_type'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/xvdd'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_and_one_attachment_xenapi
dedent|''
name|'def'
name|'test_swap_and_one_attachment_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance_type'
op|'='
op|'{'
nl|'\n'
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'10'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'instance_types'
op|','
string|"'get_instance_type'"
op|','
nl|'\n'
name|'lambda'
name|'instance_type_id'
op|','
name|'ctxt'
op|'='
name|'None'
op|':'
name|'self'
op|'.'
name|'instance_type'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/xvdb'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'data'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_fake_bdm'
op|'('
name|'device'
op|')'
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_validate_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'device'
op|','
string|"'/dev/xvdd'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UsageInfoTestCase
dedent|''
dedent|''
name|'class'
name|'UsageInfoTestCase'
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
DECL|function|fake_get_nw_info
indent|'        '
name|'def'
name|'fake_get_nw_info'
op|'('
name|'cls'
op|','
name|'ctxt'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ctxt'
op|'.'
name|'is_admin'
op|')'
newline|'\n'
name|'return'
name|'fake_network'
op|'.'
name|'fake_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'UsageInfoTestCase'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_api'
op|'.'
name|'API'
op|','
string|"'get_instance_nw_info'"
op|','
nl|'\n'
name|'fake_get_nw_info'
op|')'
newline|'\n'
nl|'\n'
name|'notifier_api'
op|'.'
name|'_reset_drivers'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'notifier_api'
op|'.'
name|'_reset_drivers'
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
name|'flags'
op|'('
name|'compute_driver'
op|'='
string|"'nova.virt.fake.FakeDriver'"
op|','
nl|'\n'
name|'notification_driver'
op|'='
op|'['
name|'test_notifier'
op|'.'
name|'__name__'
op|']'
op|','
nl|'\n'
name|'network_manager'
op|'='
string|"'nova.network.manager.FlatManager'"
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
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_show
name|'def'
name|'fake_show'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
number|'1'
op|','
string|"'ramdisk_id'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
nl|'\n'
string|"'show'"
op|','
name|'fake_show'
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'set_stub_network_methods'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake_instance_actions'
op|'.'
name|'stub_out_action_events'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'params'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance."""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_ref'"
op|']'
op|'='
number|'1'
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'launch_time'"
op|']'
op|'='
string|"'10'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user_id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project_id'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type_id'"
op|']'
op|'='
name|'type_id'
newline|'\n'
name|'inst'
op|'['
string|"'ami_launch_index'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'root_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'['
string|"'ephemeral_gb'"
op|']'
op|'='
number|'0'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_notify_usage_exists
dedent|''
name|'def'
name|'test_notify_usage_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Ensure 'exists' notification generates appropriate usage data."
nl|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
comment|'# Set some system metadata'
nl|'\n'
name|'sys_metadata'
op|'='
op|'{'
string|"'image_md_key1'"
op|':'
string|"'val1'"
op|','
nl|'\n'
string|"'image_md_key2'"
op|':'
string|"'val2'"
op|','
nl|'\n'
string|"'other_data'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_system_metadata_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'sys_metadata'
op|','
name|'False'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_usage_exists'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'compute.instance.exists'"
op|')'
newline|'\n'
name|'payload'
op|'='
name|'msg'
op|'['
string|"'payload'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_type'"
op|']'
op|','
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'payload'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'type_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'display_name'"
op|','
string|"'created_at'"
op|','
string|"'launched_at'"
op|','
nl|'\n'
string|"'state'"
op|','
string|"'state_description'"
op|','
nl|'\n'
string|"'bandwidth'"
op|','
string|"'audit_period_beginning'"
op|','
nl|'\n'
string|"'audit_period_ending'"
op|','
string|"'image_meta'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'attr'
name|'in'
name|'payload'
op|','
nl|'\n'
name|'msg'
op|'='
string|'"Key %s not in payload"'
op|'%'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_meta'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'md_key1'"
op|':'
string|"'val1'"
op|','
string|"'md_key2'"
op|':'
string|"'val2'"
op|'}'
op|')'
newline|'\n'
name|'image_ref_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_ref_url'"
op|']'
op|','
name|'image_ref_url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_notify_usage_exists_deleted_instance
dedent|''
name|'def'
name|'test_notify_usage_exists_deleted_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Ensure 'exists' notification generates appropriate usage data."
nl|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
comment|'# Set some system metadata'
nl|'\n'
name|'sys_metadata'
op|'='
op|'{'
string|"'image_md_key1'"
op|':'
string|"'val1'"
op|','
nl|'\n'
string|"'image_md_key2'"
op|':'
string|"'val2'"
op|','
nl|'\n'
string|"'other_data'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_system_metadata_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'sys_metadata'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|'.'
name|'elevated'
op|'('
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_usage_exists'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'compute.instance.exists'"
op|')'
newline|'\n'
name|'payload'
op|'='
name|'msg'
op|'['
string|"'payload'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_type'"
op|']'
op|','
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'payload'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'type_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'display_name'"
op|','
string|"'created_at'"
op|','
string|"'launched_at'"
op|','
nl|'\n'
string|"'state'"
op|','
string|"'state_description'"
op|','
nl|'\n'
string|"'bandwidth'"
op|','
string|"'audit_period_beginning'"
op|','
nl|'\n'
string|"'audit_period_ending'"
op|','
string|"'image_meta'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'attr'
name|'in'
name|'payload'
op|','
nl|'\n'
name|'msg'
op|'='
string|'"Key %s not in payload"'
op|'%'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_meta'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'md_key1'"
op|':'
string|"'val1'"
op|','
string|"'md_key2'"
op|':'
string|"'val2'"
op|'}'
op|')'
newline|'\n'
name|'image_ref_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_ref_url'"
op|']'
op|','
name|'image_ref_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_notify_usage_exists_instance_not_found
dedent|''
name|'def'
name|'test_notify_usage_exists_instance_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# Ensure 'exists' notification generates appropriate usage data."
nl|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_usage_exists'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'compute.instance.exists'"
op|')'
newline|'\n'
name|'payload'
op|'='
name|'msg'
op|'['
string|"'payload'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_type'"
op|']'
op|','
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'payload'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'type_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'display_name'"
op|','
string|"'created_at'"
op|','
string|"'launched_at'"
op|','
nl|'\n'
string|"'state'"
op|','
string|"'state_description'"
op|','
nl|'\n'
string|"'bandwidth'"
op|','
string|"'audit_period_beginning'"
op|','
nl|'\n'
string|"'audit_period_ending'"
op|','
string|"'image_meta'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'attr'
name|'in'
name|'payload'
op|','
nl|'\n'
name|'msg'
op|'='
string|'"Key %s not in payload"'
op|'%'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_meta'"
op|']'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'image_ref_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_ref_url'"
op|']'
op|','
name|'image_ref_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_notify_about_instance_usage
dedent|''
name|'def'
name|'test_notify_about_instance_usage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
comment|'# Set some system metadata'
nl|'\n'
name|'sys_metadata'
op|'='
op|'{'
string|"'image_md_key1'"
op|':'
string|"'val1'"
op|','
nl|'\n'
string|"'image_md_key2'"
op|':'
string|"'val2'"
op|','
nl|'\n'
string|"'other_data'"
op|':'
string|"'meow'"
op|'}'
newline|'\n'
name|'extra_usage_info'
op|'='
op|'{'
string|"'image_name'"
op|':'
string|"'fake_name'"
op|'}'
newline|'\n'
name|'db'
op|'.'
name|'instance_system_metadata_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'sys_metadata'
op|','
name|'False'
op|')'
newline|'\n'
comment|'# NOTE(russellb) Make sure our instance has the latest system_metadata'
nl|'\n'
comment|'# in it.'
nl|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'notify_about_instance_usage'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
string|"'create.start'"
op|','
name|'extra_usage_info'
op|'='
name|'extra_usage_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'test_notifier'
op|'.'
name|'NOTIFICATIONS'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'compute.instance.create.start'"
op|')'
newline|'\n'
name|'payload'
op|'='
name|'msg'
op|'['
string|"'payload'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'tenant_id'"
op|']'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'user_id'"
op|']'
op|','
name|'self'
op|'.'
name|'user_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_id'"
op|']'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'instance_type'"
op|']'
op|','
string|"'m1.tiny'"
op|')'
newline|'\n'
name|'type_id'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
string|"'m1.tiny'"
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'payload'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
op|','
name|'str'
op|'('
name|'type_id'
op|')'
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'display_name'"
op|','
string|"'created_at'"
op|','
string|"'launched_at'"
op|','
nl|'\n'
string|"'state'"
op|','
string|"'state_description'"
op|','
string|"'image_meta'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'attr'
name|'in'
name|'payload'
op|','
nl|'\n'
name|'msg'
op|'='
string|'"Key %s not in payload"'
op|'%'
name|'attr'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_meta'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'md_key1'"
op|':'
string|"'val1'"
op|','
string|"'md_key2'"
op|':'
string|"'val2'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_name'"
op|']'
op|','
string|"'fake_name'"
op|')'
newline|'\n'
name|'image_ref_url'
op|'='
string|'"%s/images/1"'
op|'%'
name|'glance'
op|'.'
name|'generate_glance_url'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'payload'
op|'['
string|"'image_ref_url'"
op|']'
op|','
name|'image_ref_url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'terminate_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
