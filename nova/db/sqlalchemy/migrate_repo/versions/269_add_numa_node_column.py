begin_unit
comment|'# Copyright 2014 Intel Corporation'
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
comment|'#'
nl|'\n'
comment|'# See blueprint backportable-db-migrations-icehouse'
nl|'\n'
comment|'# http://lists.openstack.org/pipermail/openstack-dev/2013-March/006827.html'
nl|'\n'
nl|'\n'
name|'from'
name|'sqlalchemy'
name|'import'
name|'MetaData'
op|','
name|'Table'
op|','
name|'Column'
op|','
name|'Integer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|upgrade
name|'def'
name|'upgrade'
op|'('
name|'migrate_engine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'meta'
op|'='
name|'MetaData'
op|'('
name|'bind'
op|'='
name|'migrate_engine'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add a new column to store PCI device numa node'
nl|'\n'
name|'pci_devices'
op|'='
name|'Table'
op|'('
string|"'pci_devices'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
name|'shadow_pci_devices'
op|'='
name|'Table'
op|'('
string|"'shadow_pci_devices'"
op|','
name|'meta'
op|','
name|'autoload'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'numa_node'
op|'='
name|'Column'
op|'('
string|"'numa_node'"
op|','
name|'Integer'
op|','
name|'default'
op|'='
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'pci_devices'
op|'.'
name|'c'
op|','
string|"'numa_node'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_devices'
op|'.'
name|'create_column'
op|'('
name|'numa_node'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'shadow_pci_devices'
op|'.'
name|'c'
op|','
string|"'numa_node'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shadow_pci_devices'
op|'.'
name|'create_column'
op|'('
name|'numa_node'
op|'.'
name|'copy'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
