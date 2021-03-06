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
op|'.'
name|'pci'
name|'import'
name|'whitelist'
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
string|"'0000:00:0a.1'"
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
string|"'phys_function'"
op|':'
string|"'0000:00:0a.0'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WhitelistTestCase
name|'class'
name|'WhitelistTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_whitelist
indent|'    '
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
string|'\'{"product_id":"0001", "vendor_id":"8086"}\''
newline|'\n'
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
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
number|'1'
op|','
name|'len'
op|'('
name|'parsed'
op|'.'
name|'specs'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_whitelist_list_format
dedent|''
name|'def'
name|'test_whitelist_list_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'white_list'
op|'='
string|'\'[{"product_id":"0001", "vendor_id":"8086"},\''
string|'\'{"product_id":"0002", "vendor_id":"8086"}]\''
newline|'\n'
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
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
number|'2'
op|','
name|'len'
op|'('
name|'parsed'
op|'.'
name|'specs'
op|')'
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
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev_dict'
op|')'
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
name|'wl1'
op|'='
string|'\'{"product_id":"0001", "vendor_id":"8086"}\''
newline|'\n'
name|'wl2'
op|'='
string|'\'{"product_id":"0002", "vendor_id":"8087"}\''
newline|'\n'
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
op|'('
op|'['
name|'wl1'
op|','
name|'wl2'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'parsed'
op|'.'
name|'specs'
op|')'
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
name|'white_list'
op|'='
string|'\'{"product_id":"0001", "vendor_id":"8086"}\''
newline|'\n'
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
op|'('
op|'['
name|'white_list'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev_dict'
op|')'
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
name|'white_list_1'
op|'='
string|'\'{"product_id":"0001", "vendor_id":"8086"}\''
newline|'\n'
name|'white_list_2'
op|'='
string|'\'{"product_id":"0002", "vendor_id":"8087"}\''
newline|'\n'
name|'parsed'
op|'='
name|'whitelist'
op|'.'
name|'Whitelist'
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
name|'assertTrue'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev_dict'
op|')'
op|')'
newline|'\n'
name|'dev_dict1'
op|'='
name|'dev_dict'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'dev_dict1'
op|'['
string|"'vendor_id'"
op|']'
op|'='
string|"'8087'"
newline|'\n'
name|'dev_dict1'
op|'['
string|"'product_id'"
op|']'
op|'='
string|"'0002'"
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'parsed'
op|'.'
name|'device_assignable'
op|'('
name|'dev_dict1'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
