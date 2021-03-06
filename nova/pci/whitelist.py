begin_unit
comment|'# Copyright (c) 2013 Intel, Inc.'
nl|'\n'
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'pci'
name|'import'
name|'devspec'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Whitelist
name|'class'
name|'Whitelist'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""White list class to decide assignable pci devices.\n\n    Not all devices on compute node can be assigned to guest, the\n    cloud administrator decides the devices that can be assigned\n    based on vendor_id or product_id etc. If no white list specified,\n    no device will be assignable.\n    """'
newline|'\n'
nl|'\n'
DECL|member|_parse_white_list_from_config
name|'def'
name|'_parse_white_list_from_config'
op|'('
name|'self'
op|','
name|'whitelists'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parse and validate the pci whitelist from the nova config."""'
newline|'\n'
name|'specs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'jsonspec'
name|'in'
name|'whitelists'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'dev_spec'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'jsonspec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Invalid entry: \'%s\'"'
op|')'
op|'%'
name|'jsonspec'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'dev_spec'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'dev_spec'
op|'='
op|'['
name|'dev_spec'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'isinstance'
op|'('
name|'dev_spec'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Invalid entry: \'%s\'; "'
nl|'\n'
string|'"Expecting list or dict"'
op|')'
op|'%'
name|'jsonspec'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'ds'
name|'in'
name|'dev_spec'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'ds'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'PciConfigInvalidWhitelist'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|'"Invalid entry: \'%s\'; "'
nl|'\n'
string|'"Expecting dict"'
op|')'
op|'%'
name|'ds'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'spec'
op|'='
name|'devspec'
op|'.'
name|'PciDeviceSpec'
op|'('
name|'ds'
op|')'
newline|'\n'
name|'specs'
op|'.'
name|'append'
op|'('
name|'spec'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'specs'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'whitelist_spec'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""White list constructor\n\n        For example, followed json string specifies that devices whose\n        vendor_id is \'8086\' and product_id is \'1520\' can be assigned\n        to guest.\n        \'[{"product_id":"1520", "vendor_id":"8086"}]\'\n\n        :param whitelist_spec: A json string for a list of dictionaries,\n                               each dictionary specifies the pci device\n                               properties requirement.\n        """'
newline|'\n'
name|'super'
op|'('
name|'Whitelist'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'if'
name|'whitelist_spec'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'specs'
op|'='
name|'self'
op|'.'
name|'_parse_white_list_from_config'
op|'('
name|'whitelist_spec'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'specs'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|device_assignable
dedent|''
dedent|''
name|'def'
name|'device_assignable'
op|'('
name|'self'
op|','
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check if a device can be assigned to a guest.\n\n        :param dev: A dictionary describing the device properties\n        """'
newline|'\n'
name|'for'
name|'spec'
name|'in'
name|'self'
op|'.'
name|'specs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'spec'
op|'.'
name|'match'
op|'('
name|'dev'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|get_devspec
dedent|''
name|'def'
name|'get_devspec'
op|'('
name|'self'
op|','
name|'pci_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'spec'
name|'in'
name|'self'
op|'.'
name|'specs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'spec'
op|'.'
name|'match_pci_obj'
op|'('
name|'pci_dev'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pci_device_devspec
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_pci_device_devspec'
op|'('
name|'pci_dev'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'dev_filter'
op|'='
name|'Whitelist'
op|'('
name|'CONF'
op|'.'
name|'pci_passthrough_whitelist'
op|')'
newline|'\n'
name|'return'
name|'dev_filter'
op|'.'
name|'get_devspec'
op|'('
name|'pci_dev'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
