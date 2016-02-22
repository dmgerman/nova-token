begin_unit
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
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
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
name|'fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'uuidsentinel'
newline|'\n'
nl|'\n'
DECL|variable|DISK_INVENTORY
name|'DISK_INVENTORY'
op|'='
name|'dict'
op|'('
nl|'\n'
DECL|variable|total
name|'total'
op|'='
number|'200'
op|','
nl|'\n'
DECL|variable|reserved
name|'reserved'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|min_unit
name|'min_unit'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|max_unit
name|'max_unit'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|step_size
name|'step_size'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|allocation_ratio
name|'allocation_ratio'
op|'='
number|'1.0'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceProviderTestCase
name|'class'
name|'ResourceProviderTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test resource-provider objects\' lifecycles."""'
newline|'\n'
nl|'\n'
DECL|member|setUp
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
name|'ResourceProviderTestCase'
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
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'Database'
op|'('
op|')'
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
string|"'fake-user'"
op|','
string|"'fake-project'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_resource_provider_requires_uuid
dedent|''
name|'def'
name|'test_create_resource_provider_requires_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource_provider'
op|'='
name|'objects'
op|'.'
name|'ResourceProvider'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'resource_provider'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_resource_provider
dedent|''
name|'def'
name|'test_create_resource_provider'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'created_resource_provider'
op|'='
name|'objects'
op|'.'
name|'ResourceProvider'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuidsentinel'
op|'.'
name|'fake_resource_provider'
nl|'\n'
op|')'
newline|'\n'
name|'created_resource_provider'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'created_resource_provider'
op|'.'
name|'id'
op|','
name|'int'
op|')'
newline|'\n'
nl|'\n'
name|'retrieved_resource_provider'
op|'='
name|'objects'
op|'.'
name|'ResourceProvider'
op|'.'
name|'get_by_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuidsentinel'
op|'.'
name|'fake_resource_provider'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'retrieved_resource_provider'
op|'.'
name|'id'
op|','
nl|'\n'
name|'created_resource_provider'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_inventory_with_uncreated_provider
dedent|''
name|'def'
name|'test_create_inventory_with_uncreated_provider'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource_provider'
op|'='
name|'objects'
op|'.'
name|'ResourceProvider'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuidsentinel'
op|'.'
name|'inventory_resource_provider'
nl|'\n'
op|')'
newline|'\n'
name|'resource_class'
op|'='
name|'fields'
op|'.'
name|'ResourceClass'
op|'.'
name|'DISK_GB'
newline|'\n'
name|'disk_inventory'
op|'='
name|'objects'
op|'.'
name|'Inventory'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'resource_provider'
op|'='
name|'resource_provider'
op|','
nl|'\n'
name|'resource_class'
op|'='
name|'resource_class'
op|','
nl|'\n'
op|'**'
name|'DISK_INVENTORY'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
nl|'\n'
name|'disk_inventory'
op|'.'
name|'create'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_update_inventory
dedent|''
name|'def'
name|'test_create_and_update_inventory'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource_provider'
op|'='
name|'objects'
op|'.'
name|'ResourceProvider'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'uuidsentinel'
op|'.'
name|'inventory_resource_provider'
nl|'\n'
op|')'
newline|'\n'
name|'resource_provider'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'resource_class'
op|'='
name|'fields'
op|'.'
name|'ResourceClass'
op|'.'
name|'DISK_GB'
newline|'\n'
name|'disk_inventory'
op|'='
name|'objects'
op|'.'
name|'Inventory'
op|'('
nl|'\n'
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'resource_provider'
op|'='
name|'resource_provider'
op|','
nl|'\n'
name|'resource_class'
op|'='
name|'resource_class'
op|','
nl|'\n'
op|'**'
name|'DISK_INVENTORY'
nl|'\n'
op|')'
newline|'\n'
name|'disk_inventory'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resource_class'
op|','
name|'disk_inventory'
op|'.'
name|'resource_class'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resource_provider'
op|','
nl|'\n'
name|'disk_inventory'
op|'.'
name|'resource_provider'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'DISK_INVENTORY'
op|'['
string|"'allocation_ratio'"
op|']'
op|','
nl|'\n'
name|'disk_inventory'
op|'.'
name|'allocation_ratio'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'DISK_INVENTORY'
op|'['
string|"'total'"
op|']'
op|','
nl|'\n'
name|'disk_inventory'
op|'.'
name|'total'
op|')'
newline|'\n'
nl|'\n'
name|'disk_inventory'
op|'.'
name|'total'
op|'='
number|'32'
newline|'\n'
name|'disk_inventory'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'inventories'
op|'='
name|'objects'
op|'.'
name|'InventoryList'
op|'.'
name|'get_all_by_resource_provider_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'resource_provider'
op|'.'
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'inventories'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'32'
op|','
name|'inventories'
op|'['
number|'0'
op|']'
op|'.'
name|'total'
op|')'
newline|'\n'
nl|'\n'
name|'inventories'
op|'['
number|'0'
op|']'
op|'.'
name|'total'
op|'='
number|'33'
newline|'\n'
name|'inventories'
op|'['
number|'0'
op|']'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'reloaded_inventories'
op|'='
op|'('
nl|'\n'
name|'objects'
op|'.'
name|'InventoryList'
op|'.'
name|'get_all_by_resource_provider_uuid'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'resource_provider'
op|'.'
name|'uuid'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'33'
op|','
name|'reloaded_inventories'
op|'['
number|'0'
op|']'
op|'.'
name|'total'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit