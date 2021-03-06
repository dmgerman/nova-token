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
name|'help'
op|'='
string|'"""\nAn alias for a PCI passthrough device requirement.\n\nThis allows users to specify the alias in the extra_spec for a flavor, without\nneeding to repeat all the PCI property requirements.\n\nPossible Values:\n\n* A list of JSON values which describe the aliases. For example:\n\n    pci_alias = {\n      "name": "QuickAssist",\n      "product_id": "0443",\n      "vendor_id": "8086",\n      "device_type": "type-PCI"\n    }\n\n  defines an alias for the Intel QuickAssist card. (multi valued). Valid key\n  values are :\n\n  * "name"\n  * "product_id"\n  * "vendor_id"\n  * "device_type"\n\nServices which consume this:\n\n* nova-compute\n\nRelated options:\n\n* None"""'
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
name|'help'
op|'='
string|'"""\nWhite list of PCI devices available to VMs.\n\nPossible values:\n\n* A JSON dictionary which describe a whitelisted PCI device. It should take\n  the following format:\n\n    ["device_id": "<id>",] ["product_id": "<id>",]\n    ["address": "[[[[<domain>]:]<bus>]:][<slot>][.[<function>]]" |\n     "devname": "PCI Device Name",]\n    {"tag": "<tag_value>",}\n\n  where \'[\' indicates zero or one occurrences, \'{\' indicates zero or multiple\n  occurrences, and \'|\' mutually exclusive options. Note that any missing\n  fields are automatically wildcarded. Valid examples are:\n\n    pci_passthrough_whitelist = {"devname":"eth0",\n                                 "physical_network":"physnet"}\n    pci_passthrough_whitelist = {"address":"*:0a:00.*"}\n    pci_passthrough_whitelist = {"address":":0a:00.",\n                                 "physical_network":"physnet1"}\n    pci_passthrough_whitelist = {"vendor_id":"1137",\n                                 "product_id":"0071"}\n    pci_passthrough_whitelist = {"vendor_id":"1137",\n                                 "product_id":"0071",\n                                 "address": "0000:0a:00.1",\n                                 "physical_network":"physnet1"}\n\n  The following are invalid, as they specify mutually exclusive options:\n\n    pci_passthrough_whitelist = {"devname":"eth0",\n                                 "physical_network":"physnet",\n                                 "address":"*:0a:00.*"}\n\n* A JSON list of JSON dictionaries corresponding to the above format. For\n  example:\n\n    pci_passthrough_whitelist = [{"product_id":"0001", "vendor_id":"8086"},\n                                 {"product_id":"0002", "vendor_id":"8086"}]\n\nServices which consume this:\n\n* nova-compute\n\nRelated options:\n\n* None"""'
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
