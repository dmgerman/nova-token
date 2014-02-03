begin_unit
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
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'pci'
name|'import'
name|'pci_whitelist'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|dev_dict
name|'dev_dict'
op|'='
op|'{'
nl|'\n'
string|"'compute_node_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'a'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0001'"
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciHostDevicesWhiteListTestCase
name|'class'
name|'PciHostDevicesWhiteListTestCase'
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
name|'PciHostDevicesWhiteListTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist_wrong_format
dedent|''
name|'def'
name|'test_whitelist_wrong_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list'
op|'='
string|'\'[{"vendor_x_id":"8086", "product_id":"0001"}]\''
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|','
name|'white_list'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'white_list'
op|'='
string|'\'[{"vendor_id":"80863", "product_id":"0001"}]\''
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|','
name|'white_list'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist_missed_fields
dedent|''
name|'def'
name|'test_whitelist_missed_fields'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list'
op|'='
string|'\'[{"vendor_id":"80863"}]\''
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|','
nl|'\n'
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|','
name|'white_list'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist
dedent|''
name|'def'
name|'test_whitelist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"}]\''
newline|'\n'
name|'parsed'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
op|'['
name|'white_list'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'spec'
op|','
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
nl|'\n'
string|"'product_id'"
op|':'
string|"'0001'"
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist_empty
dedent|''
name|'def'
name|'test_whitelist_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'parsed'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev'
op|')'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist_multiple
dedent|''
name|'def'
name|'test_whitelist_multiple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list_1'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"}]\''
newline|'\n'
name|'white_list_2'
op|'='
string|'\'[{"product_id":"0002", "vendor_id":"8087"}]\''
newline|'\n'
name|'parsed'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
nl|'\n'
op|'['
name|'white_list_1'
op|','
name|'white_list_2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'spec'
op|','
nl|'\n'
op|'['
op|'{'
string|"'vendor_id'"
op|':'
string|"'8086'"
op|','
string|"'product_id'"
op|':'
string|"'0001'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'vendor_id'"
op|':'
string|"'8087'"
op|','
string|"'product_id'"
op|':'
string|"'0002'"
op|'}'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_device_assignable
dedent|''
name|'def'
name|'test_device_assignable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'white_list'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"}]\''
newline|'\n'
name|'parsed'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
op|'['
name|'white_list'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_device_assignable_multiple
dedent|''
name|'def'
name|'test_device_assignable_multiple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'white_list_1'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"}]\''
newline|'\n'
name|'white_list_2'
op|'='
string|'\'[{"product_id":"0002", "vendor_id":"8087"}]\''
newline|'\n'
name|'parsed'
op|'='
name|'pci_whitelist'
op|'.'
name|'PciHostDevicesWhiteList'
op|'('
nl|'\n'
op|'['
name|'white_list_1'
op|','
name|'white_list_2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
name|'dev'
op|'.'
name|'vendor_id'
op|'='
string|"'8087'"
newline|'\n'
name|'dev'
op|'.'
name|'product_id'
op|'='
string|"'0002'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_pci_devices_filter
dedent|''
name|'def'
name|'test_get_pci_devices_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list_1'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"}]\''
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'pci_passthrough_whitelist'
op|'='
op|'['
name|'white_list_1'
op|']'
op|')'
newline|'\n'
name|'pci_filter'
op|'='
name|'pci_whitelist'
op|'.'
name|'get_pci_devices_filter'
op|'('
op|')'
newline|'\n'
name|'dev'
op|'='
name|'pci_device'
op|'.'
name|'PciDevice'
op|'.'
name|'create'
op|'('
name|'dev_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pci_filter'
op|'.'
name|'device_assignable'
op|'('
name|'dev'
op|')'
op|','
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
