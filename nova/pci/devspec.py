begin_unit
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
name|'import'
name|'ast'
newline|'\n'
name|'import'
name|'re'
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
name|'pci'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|MAX_VENDOR_ID
name|'MAX_VENDOR_ID'
op|'='
number|'0xFFFF'
newline|'\n'
DECL|variable|MAX_PRODUCT_ID
name|'MAX_PRODUCT_ID'
op|'='
number|'0xFFFF'
newline|'\n'
DECL|variable|MAX_FUNC
name|'MAX_FUNC'
op|'='
number|'0x7'
newline|'\n'
DECL|variable|MAX_DOMAIN
name|'MAX_DOMAIN'
op|'='
number|'0xFFFF'
newline|'\n'
DECL|variable|MAX_BUS
name|'MAX_BUS'
op|'='
number|'0xFF'
newline|'\n'
DECL|variable|MAX_SLOT
name|'MAX_SLOT'
op|'='
number|'0x1F'
newline|'\n'
DECL|variable|ANY
name|'ANY'
op|'='
string|"'*'"
newline|'\n'
DECL|variable|VIRTFN_RE
name|'VIRTFN_RE'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"virtfn\\d+"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_value
name|'def'
name|'get_value'
op|'('
name|'v'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'ast'
op|'.'
name|'literal_eval'
op|'('
string|'"0x"'
op|'+'
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pci_dev_info
dedent|''
name|'def'
name|'get_pci_dev_info'
op|'('
name|'pci_obj'
op|','
name|'property'
op|','
name|'max'
op|','
name|'hex_value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'a'
op|'='
name|'getattr'
op|'('
name|'pci_obj'
op|','
name|'property'
op|')'
newline|'\n'
name|'if'
name|'a'
op|'=='
name|'ANY'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'v'
op|'='
name|'get_value'
op|'('
name|'a'
op|')'
newline|'\n'
name|'if'
name|'v'
op|'>'
name|'max'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|'('
nl|'\n'
name|'reason'
op|'='
string|'"invalid %s %s"'
op|'%'
op|'('
name|'property'
op|','
name|'a'
op|')'
op|')'
newline|'\n'
dedent|''
name|'setattr'
op|'('
name|'pci_obj'
op|','
name|'property'
op|','
name|'hex_value'
op|'%'
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciAddress
dedent|''
name|'class'
name|'PciAddress'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages the address fields of the whitelist.\n\n    This class checks the address fields of the pci_passthrough_whitelist\n    configuration option, validating the address fields.\n    Example config are:\n\n        | pci_passthrough_whitelist = {"address":"*:0a:00.*",\n        |                         "physical_network":"physnet1"}\n        | pci_passthrough_whitelist = {"vendor_id":"1137","product_id":"0071"}\n\n    This function class will validate the address fields, check for wildcards,\n    and insert wildcards where the field is left blank.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'pci_addr'
op|','
name|'is_physical_function'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'domain'
op|'='
name|'ANY'
newline|'\n'
name|'self'
op|'.'
name|'bus'
op|'='
name|'ANY'
newline|'\n'
name|'self'
op|'.'
name|'slot'
op|'='
name|'ANY'
newline|'\n'
name|'self'
op|'.'
name|'func'
op|'='
name|'ANY'
newline|'\n'
name|'self'
op|'.'
name|'is_physical_function'
op|'='
name|'is_physical_function'
newline|'\n'
name|'self'
op|'.'
name|'_init_address_fields'
op|'('
name|'pci_addr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_physical_function
dedent|''
name|'def'
name|'_check_physical_function'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'ANY'
name|'in'
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'bus'
op|','
name|'self'
op|'.'
name|'slot'
op|','
name|'self'
op|'.'
name|'func'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'is_physical_function'
op|'='
name|'utils'
op|'.'
name|'is_physical_function'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_init_address_fields
dedent|''
name|'def'
name|'_init_address_fields'
op|'('
name|'self'
op|','
name|'pci_addr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'is_physical_function'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'bus'
op|','
name|'self'
op|'.'
name|'slot'
op|','
nl|'\n'
name|'self'
op|'.'
name|'func'
op|')'
op|'='
name|'utils'
op|'.'
name|'get_pci_address_fields'
op|'('
name|'pci_addr'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'dbs'
op|','
name|'sep'
op|','
name|'func'
op|'='
name|'pci_addr'
op|'.'
name|'partition'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'if'
name|'func'
op|':'
newline|'\n'
indent|'            '
name|'fstr'
op|'='
name|'func'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'fstr'
op|'!='
name|'ANY'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'f'
op|'='
name|'get_value'
op|'('
name|'fstr'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'SyntaxError'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceWrongAddressFormat'
op|'('
nl|'\n'
name|'address'
op|'='
name|'pci_addr'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'f'
op|'>'
name|'MAX_FUNC'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidAddressField'
op|'('
nl|'\n'
name|'address'
op|'='
name|'pci_addr'
op|','
name|'field'
op|'='
string|'"function"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'func'
op|'='
string|'"%1x"'
op|'%'
name|'f'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'dbs'
op|':'
newline|'\n'
indent|'            '
name|'dbs_fields'
op|'='
name|'dbs'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'dbs_fields'
op|')'
op|'>'
number|'3'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceWrongAddressFormat'
op|'('
name|'address'
op|'='
name|'pci_addr'
op|')'
newline|'\n'
comment|'# If we got a partial address like ":00.", we need to to turn this'
nl|'\n'
comment|'# into a domain of ANY, a bus of ANY, and a slot of 00. This code'
nl|'\n'
comment|'# allows the address bus and/or domain to be left off'
nl|'\n'
dedent|''
name|'dbs_all'
op|'='
op|'['
name|'ANY'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'3'
op|'-'
name|'len'
op|'('
name|'dbs_fields'
op|')'
op|')'
op|']'
newline|'\n'
name|'dbs_all'
op|'.'
name|'extend'
op|'('
name|'dbs_fields'
op|')'
newline|'\n'
name|'dbs_checked'
op|'='
op|'['
name|'s'
op|'.'
name|'strip'
op|'('
op|')'
name|'or'
name|'ANY'
name|'for'
name|'s'
name|'in'
name|'dbs_all'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'domain'
op|','
name|'self'
op|'.'
name|'bus'
op|','
name|'self'
op|'.'
name|'slot'
op|'='
name|'dbs_checked'
newline|'\n'
name|'get_pci_dev_info'
op|'('
name|'self'
op|','
string|"'domain'"
op|','
name|'MAX_DOMAIN'
op|','
string|"'%04x'"
op|')'
newline|'\n'
name|'get_pci_dev_info'
op|'('
name|'self'
op|','
string|"'bus'"
op|','
name|'MAX_BUS'
op|','
string|"'%02x'"
op|')'
newline|'\n'
name|'get_pci_dev_info'
op|'('
name|'self'
op|','
string|"'slot'"
op|','
name|'MAX_SLOT'
op|','
string|"'%02x'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_physical_function'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|match
dedent|''
dedent|''
name|'def'
name|'match'
op|'('
name|'self'
op|','
name|'pci_addr'
op|','
name|'pci_phys_addr'
op|')'
op|':'
newline|'\n'
comment|'# Assume this is called given pci_add and pci_phys_addr from libvirt,'
nl|'\n'
comment|'# no attempt is made to verify pci_addr is a VF of pci_phys_addr'
nl|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'is_physical_function'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'pci_phys_addr'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'func'
op|'='
op|'('
nl|'\n'
name|'utils'
op|'.'
name|'get_pci_address_fields'
op|'('
name|'pci_phys_addr'
op|')'
op|')'
newline|'\n'
name|'return'
op|'('
name|'self'
op|'.'
name|'domain'
op|'=='
name|'domain'
name|'and'
name|'self'
op|'.'
name|'bus'
op|'=='
name|'bus'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'slot'
op|'=='
name|'slot'
name|'and'
name|'self'
op|'.'
name|'func'
op|'=='
name|'func'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'domain'
op|','
name|'bus'
op|','
name|'slot'
op|','
name|'func'
op|'='
op|'('
nl|'\n'
name|'utils'
op|'.'
name|'get_pci_address_fields'
op|'('
name|'pci_addr'
op|')'
op|')'
newline|'\n'
name|'conditions'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'domain'
name|'in'
op|'('
name|'ANY'
op|','
name|'domain'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'bus'
name|'in'
op|'('
name|'ANY'
op|','
name|'bus'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'slot'
name|'in'
op|'('
name|'ANY'
op|','
name|'slot'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'func'
name|'in'
op|'('
name|'ANY'
op|','
name|'func'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'conditions'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDeviceSpec
dedent|''
dedent|''
dedent|''
name|'class'
name|'PciDeviceSpec'
op|'('
name|'object'
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
name|'dev_spec'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tags'
op|'='
name|'dev_spec'
newline|'\n'
name|'self'
op|'.'
name|'_init_dev_details'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dev_count'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|_init_dev_details
dedent|''
name|'def'
name|'_init_dev_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'vendor_id'
op|'='
name|'self'
op|'.'
name|'tags'
op|'.'
name|'pop'
op|'('
string|'"vendor_id"'
op|','
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'product_id'
op|'='
name|'self'
op|'.'
name|'tags'
op|'.'
name|'pop'
op|'('
string|'"product_id"'
op|','
name|'ANY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'address'
op|'='
name|'self'
op|'.'
name|'tags'
op|'.'
name|'pop'
op|'('
string|'"address"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dev_name'
op|'='
name|'self'
op|'.'
name|'tags'
op|'.'
name|'pop'
op|'('
string|'"devname"'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vendor_id'
op|'='
name|'self'
op|'.'
name|'vendor_id'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'get_pci_dev_info'
op|'('
name|'self'
op|','
string|"'vendor_id'"
op|','
name|'MAX_VENDOR_ID'
op|','
string|"'%04x'"
op|')'
newline|'\n'
name|'get_pci_dev_info'
op|'('
name|'self'
op|','
string|"'product_id'"
op|','
name|'MAX_PRODUCT_ID'
op|','
string|"'%04x'"
op|')'
newline|'\n'
nl|'\n'
name|'pf'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'address'
name|'and'
name|'self'
op|'.'
name|'dev_name'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceInvalidDeviceName'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'dev_name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'address'
op|','
name|'pf'
op|'='
name|'utils'
op|'.'
name|'get_function_by_ifname'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'dev_name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'address'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'PciDeviceNotFoundById'
op|'('
name|'id'
op|'='
name|'self'
op|'.'
name|'dev_name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'address'
op|'='
string|'"*:*:*.*"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'address'
op|'='
name|'PciAddress'
op|'('
name|'self'
op|'.'
name|'address'
op|','
name|'pf'
op|')'
newline|'\n'
nl|'\n'
DECL|member|match
dedent|''
name|'def'
name|'match'
op|'('
name|'self'
op|','
name|'dev_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conditions'
op|'='
op|'['
nl|'\n'
name|'self'
op|'.'
name|'vendor_id'
name|'in'
op|'('
name|'ANY'
op|','
name|'dev_dict'
op|'['
string|"'vendor_id'"
op|']'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'product_id'
name|'in'
op|'('
name|'ANY'
op|','
name|'dev_dict'
op|'['
string|"'product_id'"
op|']'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'address'
op|'.'
name|'match'
op|'('
name|'dev_dict'
op|'['
string|"'address'"
op|']'
op|','
nl|'\n'
name|'dev_dict'
op|'.'
name|'get'
op|'('
string|"'phys_function'"
op|')'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'return'
name|'all'
op|'('
name|'conditions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|match_pci_obj
dedent|''
name|'def'
name|'match_pci_obj'
op|'('
name|'self'
op|','
name|'pci_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'pci_obj'
op|'.'
name|'extra_info'
op|':'
newline|'\n'
indent|'            '
name|'phy_func'
op|'='
name|'pci_obj'
op|'.'
name|'extra_info'
op|'.'
name|'get'
op|'('
string|"'phys_function'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'phy_func'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'match'
op|'('
op|'{'
string|"'vendor_id'"
op|':'
name|'pci_obj'
op|'.'
name|'vendor_id'
op|','
nl|'\n'
string|"'product_id'"
op|':'
name|'pci_obj'
op|'.'
name|'product_id'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'pci_obj'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'phys_function'"
op|':'
name|'phy_func'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_tags
dedent|''
name|'def'
name|'get_tags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'tags'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
