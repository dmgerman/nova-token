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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|pci_alias_opt
name|'pci_alias_opt'
op|'='
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
nl|'\n'
string|"'pci_alias'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'An alias for a PCI passthrough device requirement. This allows '"
nl|'\n'
string|"'users to specify the alias in the extra_spec for a flavor, '"
nl|'\n'
string|"'without needing to repeat all the PCI property requirements. For '"
nl|'\n'
string|"'example: pci_alias = { '"
nl|'\n'
string|'\'"name": "QuickAssist", \''
nl|'\n'
string|'\'"product_id": "0443", \''
nl|'\n'
string|'\'"vendor_id": "8086", \''
nl|'\n'
string|'\'"device_type": "type-PCI" \''
nl|'\n'
string|"'} defines an alias for the Intel QuickAssist card. (multi '"
nl|'\n'
string|"'valued).'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|pci_passthrough_whitelist_opt
name|'pci_passthrough_whitelist_opt'
op|'='
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
nl|'\n'
string|"'pci_passthrough_whitelist'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'White list of PCI devices available to VMs. For example: '"
nl|'\n'
string|"'pci_passthrough_whitelist = '"
nl|'\n'
string|'\'[{"vendor_id": "8086", "product_id": "0443"}]\''
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALL_OPTS
name|'ALL_OPTS'
op|'='
op|'['
name|'pci_alias_opt'
op|','
nl|'\n'
name|'pci_passthrough_whitelist_opt'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_OPTS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# TODO(sfinucan): This should be moved into the PCI group and'
nl|'\n'
comment|'# oslo_config.cfg.OptGroup used'
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|"'DEFAULT'"
op|':'
name|'ALL_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit