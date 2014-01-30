begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Intel Corp.'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'pci'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
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
op|'.'
name|'objects'
name|'import'
name|'instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'pci_device'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_pci_device'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_compute_node
name|'fake_compute_node'
op|'='
op|'{'
nl|'\n'
string|"'pci_stats'"
op|':'
op|'['
op|'{'
string|'"count"'
op|':'
number|'3'
op|','
nl|'\n'
string|'"vendor_id"'
op|':'
string|'"8086"'
op|','
nl|'\n'
string|'"product_id"'
op|':'
string|'"1520"'
op|','
nl|'\n'
string|'"extra_info"'
op|':'
op|'{'
string|'"phys_function"'
op|':'
string|'\'[["0x0000", "0x04", \''
nl|'\n'
string|'\'"0x00", "0x1"]]\''
op|'}'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeResponse
name|'class'
name|'FakeResponse'
op|'('
name|'wsgi'
op|'.'
name|'ResponseObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciServerControllerTest
dedent|''
name|'class'
name|'PciServerControllerTest'
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
name|'PciServerControllerTest'
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
name|'controller'
op|'='
name|'pci'
op|'.'
name|'PciServerController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_obj'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
string|"'addresses'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'fb08'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'a3'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'9a3af784c'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'e992080ac0'"
op|','
nl|'\n'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'fake_list'
op|'='
op|'{'
string|"'servers'"
op|':'
op|'['
op|'{'
string|"'addresses'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'fb08'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'a3'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'ACTIVE'"
op|','
nl|'\n'
string|"'tenant_id'"
op|':'
string|"'9a3af784c'"
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'e992080ac'"
op|','
nl|'\n'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_create_fake_instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_fake_pci_device'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'claim'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'.'
name|'allocate'
op|'('
name|'self'
op|'.'
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_instance
dedent|''
name|'def'
name|'_create_fake_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inst'
op|'='
name|'instance'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'uuid'
op|'='
string|"'fake-inst-uuid'"
newline|'\n'
name|'self'
op|'.'
name|'inst'
op|'.'
name|'pci_devices'
op|'='
name|'pci_device'
op|'.'
name|'PciDeviceList'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_fake_pci_device
dedent|''
name|'def'
name|'_create_fake_pci_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_pci_device_get_by_addr
indent|'        '
name|'def'
name|'fake_pci_device_get_by_addr'
op|'('
name|'ctxt'
op|','
name|'id'
op|','
name|'addr'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'test_pci_device'
op|'.'
name|'fake_db_dev'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
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
string|"'pci_device_get_by_addr'"
op|','
nl|'\n'
name|'fake_pci_device_get_by_addr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pci_device'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'get_by_dev_addr'
op|'('
name|'ctxt'
op|','
number|'1'
op|','
string|"'a'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_db_instance
indent|'        '
name|'def'
name|'fake_get_db_instance'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'inst'
newline|'\n'
nl|'\n'
dedent|''
name|'resp'
op|'='
name|'FakeResponse'
op|'('
name|'self'
op|'.'
name|'fake_obj'
op|','
string|"''"
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-pci/1'"
op|','
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'req'
op|','
string|"'get_db_instance'"
op|','
name|'fake_get_db_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'resp'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|'}'
op|']'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
op|'['
string|"'os-pci:pci_devices'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_db_instance
indent|'        '
name|'def'
name|'fake_get_db_instance'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'inst'
newline|'\n'
nl|'\n'
dedent|''
name|'resp'
op|'='
name|'FakeResponse'
op|'('
name|'self'
op|'.'
name|'fake_list'
op|','
string|"''"
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-pci/detail'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'req'
op|','
string|"'get_db_instance'"
op|','
name|'fake_get_db_instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'resp'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|'}'
op|']'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'servers'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'os-pci:pci_devices'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciHypervisorControllerTest
dedent|''
dedent|''
name|'class'
name|'PciHypervisorControllerTest'
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
name|'PciHypervisorControllerTest'
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
name|'controller'
op|'='
name|'pci'
op|'.'
name|'PciHypervisorController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_objs'
op|'='
name|'dict'
op|'('
name|'hypervisors'
op|'='
op|'['
nl|'\n'
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_obj'
op|'='
name|'dict'
op|'('
name|'hypervisor'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'service'
op|'='
name|'dict'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'host'
op|'='
string|'"compute1"'
op|')'
op|','
nl|'\n'
name|'hypervisor_type'
op|'='
string|'"xen"'
op|','
nl|'\n'
name|'hypervisor_version'
op|'='
number|'3'
op|','
nl|'\n'
name|'hypervisor_hostname'
op|'='
string|'"hyper1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
name|'def'
name|'test_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_db_compute_node
indent|'        '
name|'def'
name|'fake_get_db_compute_node'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
nl|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'fake_compute_node'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/1'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'FakeResponse'
op|'('
name|'self'
op|'.'
name|'fake_obj'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'req'
op|','
string|"'get_db_compute_node'"
op|','
name|'fake_get_db_compute_node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'resp'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-pci:pci_stats'"
op|','
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'hypervisor'"
op|']'
op|')'
newline|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
nl|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'hypervisor'"
op|']'
op|'['
string|"'os-pci:pci_stats'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail
dedent|''
name|'def'
name|'test_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_db_compute_node
indent|'        '
name|'def'
name|'fake_get_db_compute_node'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
nl|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'fake_compute_node'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/os-hypervisors/detail'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'FakeResponse'
op|'('
name|'self'
op|'.'
name|'fake_objs'
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'req'
op|','
string|"'get_db_compute_node'"
op|','
name|'fake_get_db_compute_node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'resp'
op|')'
newline|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
nl|'\n'
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-pci:pci_stats'"
op|','
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'hypervisors'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_compute_node'
op|'['
string|"'pci_stats'"
op|']'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'resp'
op|'.'
name|'obj'
op|'['
string|"'hypervisors'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'os-pci:pci_stats'"
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
