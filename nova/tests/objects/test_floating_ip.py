begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
nl|'\n'
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
name|'floating_ip'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_fixed_ip'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'objects'
name|'import'
name|'test_objects'
newline|'\n'
nl|'\n'
DECL|variable|fake_floating_ip
name|'fake_floating_ip'
op|'='
op|'{'
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'address'"
op|':'
string|"'172.17.0.1'"
op|','
nl|'\n'
string|"'fixed_ip_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'auto_assigned'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'pool'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'fixed_ip'"
op|':'
name|'None'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_TestFloatingIPObject
name|'class'
name|'_TestFloatingIPObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|_compare
indent|'    '
name|'def'
name|'_compare'
op|'('
name|'self'
op|','
name|'obj'
op|','
name|'db_obj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'field'
name|'in'
name|'obj'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'in'
name|'floating_ip'
op|'.'
name|'FLOATING_IP_OPTIONAL_ATTRS'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'obj'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'field'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'obj_val'
op|'='
name|'obj'
op|'['
name|'field'
op|']'
op|'.'
name|'id'
newline|'\n'
name|'db_val'
op|'='
name|'db_obj'
op|'['
name|'field'
op|']'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'obj_val'
op|'='
name|'obj'
op|'['
name|'field'
op|']'
newline|'\n'
name|'db_val'
op|'='
name|'db_obj'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'obj_val'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'obj_val'
op|'='
name|'str'
op|'('
name|'obj_val'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_val'
op|','
name|'obj_val'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get'"
op|')'
newline|'\n'
DECL|member|test_get_by_id
name|'def'
name|'test_get_by_id'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_floatingip'
op|'='
name|'dict'
op|'('
name|'fake_floating_ip'
op|','
nl|'\n'
name|'fixed_ip'
op|'='
name|'test_fixed_ip'
op|'.'
name|'fake_fixed_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'return_value'
op|'='
name|'db_floatingip'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'get_by_id'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingip'
op|','
name|'db_floatingip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_by_address'"
op|')'
newline|'\n'
DECL|member|test_get_by_address
name|'def'
name|'test_get_by_address'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
name|'fake_floating_ip'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'get_by_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingip'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_pools'"
op|')'
newline|'\n'
DECL|member|test_get_pool_names
name|'def'
name|'test_get_pool_names'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'a'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'b'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'a'"
op|','
string|"'b'"
op|']'
op|','
nl|'\n'
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'get_pool_names'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_allocate_address'"
op|')'
newline|'\n'
DECL|member|test_allocate_address
name|'def'
name|'test_allocate_address'
op|'('
name|'self'
op|','
name|'allocate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'allocate'
op|'.'
name|'return_value'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'allocate_address'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'project'"
op|','
nl|'\n'
string|"'pool'"
op|')'
op|')'
newline|'\n'
name|'allocate'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'project'"
op|','
string|"'pool'"
op|','
nl|'\n'
name|'auto_assigned'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_fixed_ip_associate'"
op|')'
newline|'\n'
DECL|member|test_associate
name|'def'
name|'test_associate'
op|'('
name|'self'
op|','
name|'associate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixed'
op|'='
name|'dict'
op|'('
name|'test_fixed_ip'
op|'.'
name|'fake_fixed_ip'
op|','
nl|'\n'
name|'network'
op|'='
name|'test_network'
op|'.'
name|'fake_network'
op|')'
newline|'\n'
name|'associate'
op|'.'
name|'return_value'
op|'='
name|'db_fixed'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'associate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'172.17.0.1'"
op|','
nl|'\n'
string|"'192.168.1.1'"
op|','
nl|'\n'
string|"'host'"
op|')'
newline|'\n'
name|'associate'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'172.17.0.1'"
op|','
nl|'\n'
string|"'192.168.1.1'"
op|','
string|"'host'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_fixed'
op|'['
string|"'id'"
op|']'
op|','
name|'floatingip'
op|'.'
name|'fixed_ip'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'172.17.0.1'"
op|','
name|'str'
op|'('
name|'floatingip'
op|'.'
name|'address'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'host'"
op|','
name|'floatingip'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_deallocate'"
op|')'
newline|'\n'
DECL|member|test_deallocate
name|'def'
name|'test_deallocate'
op|'('
name|'self'
op|','
name|'deallocate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'deallocate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'deallocate'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_destroy'"
op|')'
newline|'\n'
DECL|member|test_destroy
name|'def'
name|'test_destroy'
op|'('
name|'self'
op|','
name|'destroy'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'destroy'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_disassociate'"
op|')'
newline|'\n'
DECL|member|test_disassociate
name|'def'
name|'test_disassociate'
op|'('
name|'self'
op|','
name|'disassociate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'db_fixed'
op|'='
name|'dict'
op|'('
name|'test_fixed_ip'
op|'.'
name|'fake_fixed_ip'
op|','
nl|'\n'
name|'network'
op|'='
name|'test_network'
op|'.'
name|'fake_network'
op|')'
newline|'\n'
name|'disassociate'
op|'.'
name|'return_value'
op|'='
name|'db_fixed'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'disassociate'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'disassociate'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'db_fixed'
op|'['
string|"'id'"
op|']'
op|','
name|'floatingip'
op|'.'
name|'fixed_ip'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1.2.3.4'"
op|','
name|'str'
op|'('
name|'floatingip'
op|'.'
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_update'"
op|')'
newline|'\n'
DECL|member|test_save
name|'def'
name|'test_save'
op|'('
name|'self'
op|','
name|'update'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'update'
op|'.'
name|'return_value'
op|'='
name|'fake_floating_ip'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
number|'123'
op|','
name|'address'
op|'='
string|"'1.2.3.4'"
op|','
nl|'\n'
name|'host'
op|'='
string|"'foo'"
op|')'
newline|'\n'
name|'floatingip'
op|'.'
name|'obj_reset_changes'
op|'('
op|'['
string|"'address'"
op|','
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'floatingip'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
op|')'
op|','
name|'floatingip'
op|'.'
name|'obj_what_changed'
op|'('
op|')'
op|')'
newline|'\n'
name|'update'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_save_errors
dedent|''
name|'def'
name|'test_save_errors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
number|'123'
op|','
name|'host'
op|'='
string|"'foo'"
op|')'
newline|'\n'
name|'floatingip'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'floating_ip'
op|'.'
name|'address'
op|'='
string|"'1.2.3.4'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'floatingip'
op|'.'
name|'save'
op|')'
newline|'\n'
nl|'\n'
name|'floatingip'
op|'.'
name|'obj_reset_changes'
op|'('
op|')'
newline|'\n'
name|'floatingip'
op|'.'
name|'fixed_ip_id'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ObjectActionError'
op|','
name|'floatingip'
op|'.'
name|'save'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_update'"
op|')'
newline|'\n'
DECL|member|test_save_no_fixedip
name|'def'
name|'test_save_no_fixedip'
op|'('
name|'self'
op|','
name|'update'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'update'
op|'.'
name|'return_value'
op|'='
name|'fake_floating_ip'
newline|'\n'
name|'floatingip'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
number|'123'
op|')'
newline|'\n'
name|'floatingip'
op|'.'
name|'fixed_ip'
op|'='
name|'objects'
op|'.'
name|'FixedIP'
op|'('
name|'context'
op|'='
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'id'
op|'='
number|'456'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'fixed_ip'"
op|','
name|'update'
op|'.'
name|'calls'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_all'"
op|')'
newline|'\n'
DECL|member|test_get_all
name|'def'
name|'test_get_all'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_floating_ip'
op|']'
newline|'\n'
name|'floatingips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_all'
op|'('
name|'self'
op|'.'
name|'context'
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
name|'floatingips'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingips'
op|'['
number|'0'
op|']'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_all_by_host'"
op|')'
newline|'\n'
DECL|member|test_get_by_host
name|'def'
name|'test_get_by_host'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_floating_ip'
op|']'
newline|'\n'
name|'floatingips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_host'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'host'"
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
name|'floatingips'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingips'
op|'['
number|'0'
op|']'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_all_by_project'"
op|')'
newline|'\n'
DECL|member|test_get_by_project
name|'def'
name|'test_get_by_project'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_floating_ip'
op|']'
newline|'\n'
name|'floatingips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_project'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'project'"
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
name|'floatingips'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingips'
op|'['
number|'0'
op|']'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'project'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_by_fixed_address'"
op|')'
newline|'\n'
DECL|member|test_get_by_fixed_address
name|'def'
name|'test_get_by_fixed_address'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_floating_ip'
op|']'
newline|'\n'
name|'floatingips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_fixed_address'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
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
name|'floatingips'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingips'
op|'['
number|'0'
op|']'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_get_by_fixed_ip_id'"
op|')'
newline|'\n'
DECL|member|test_get_by_fixed_ip_id
name|'def'
name|'test_get_by_fixed_ip_id'
op|'('
name|'self'
op|','
name|'get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_floating_ip'
op|']'
newline|'\n'
name|'floatingips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIPList'
op|'.'
name|'get_by_fixed_ip_id'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'123'
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
name|'floatingips'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare'
op|'('
name|'floatingips'
op|'['
number|'0'
op|']'
op|','
name|'fake_floating_ip'
op|')'
newline|'\n'
name|'get'
op|'.'
name|'assert_called_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'123'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.instance_floating_address_get_all'"
op|')'
newline|'\n'
DECL|member|test_get_addresses_by_instance
name|'def'
name|'test_get_addresses_by_instance'
op|'('
name|'self'
op|','
name|'get_all'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'['
string|"'1.2.3.4'"
op|','
string|"'4.5.6.7'"
op|']'
newline|'\n'
name|'get_all'
op|'.'
name|'return_value'
op|'='
name|'list'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'ips'
op|'='
name|'floating_ip'
op|'.'
name|'FloatingIP'
op|'.'
name|'get_addresses_by_instance'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'uuid'"
op|':'
string|"'1234'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'ips'
op|')'
newline|'\n'
name|'get_all'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'1234'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_make_ip_info
dedent|''
name|'def'
name|'test_make_ip_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'make_ip_info'
op|'('
string|"'1.2.3.4'"
op|','
string|"'pool'"
op|','
string|"'eth0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'address'"
op|':'
string|"'1.2.3.4'"
op|','
string|"'pool'"
op|':'
string|"'pool'"
op|','
nl|'\n'
string|"'interface'"
op|':'
string|"'eth0'"
op|'}'
op|','
nl|'\n'
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_bulk_create'"
op|')'
newline|'\n'
DECL|member|test_bulk_create
name|'def'
name|'test_bulk_create'
op|'('
name|'self'
op|','
name|'create_mock'
op|')'
op|':'
newline|'\n'
DECL|function|fake_create
indent|'        '
name|'def'
name|'fake_create'
op|'('
name|'ctxt'
op|','
name|'ip_info'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'address'"
op|':'
name|'ip'
op|'['
string|"'address'"
op|']'
op|','
string|"'fixed_ip_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'foo'"
op|','
string|"'host'"
op|':'
string|"'host'"
op|','
nl|'\n'
string|"'auto_assigned'"
op|':'
name|'False'
op|','
string|"'pool'"
op|':'
name|'ip'
op|'['
string|"'pool'"
op|']'
op|','
nl|'\n'
string|"'interface'"
op|':'
name|'ip'
op|'['
string|"'interface'"
op|']'
op|','
string|"'fixed_ip'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'None'
op|','
string|"'updated_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'ip_info'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'create_mock'
op|'.'
name|'side_effect'
op|'='
name|'fake_create'
newline|'\n'
name|'ips'
op|'='
op|'['
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'make_ip_info'
op|'('
string|"'1.1.1.1'"
op|','
string|"'pool'"
op|','
string|"'eth0'"
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'make_ip_info'
op|'('
string|"'1.1.1.2'"
op|','
string|"'loop'"
op|','
string|"'eth1'"
op|')'
op|']'
newline|'\n'
name|'result'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'ips'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIs'
op|'('
name|'result'
op|','
name|'None'
op|')'
newline|'\n'
name|'result'
op|'='
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'ips'
op|','
name|'want_result'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'1.1.1.2'"
op|','
name|'str'
op|'('
name|'result'
op|'['
number|'1'
op|']'
op|'.'
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.db.floating_ip_bulk_destroy'"
op|')'
newline|'\n'
DECL|member|test_bulk_destroy
name|'def'
name|'test_bulk_destroy'
op|'('
name|'self'
op|','
name|'destroy_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ips'
op|'='
op|'['
op|'{'
string|"'address'"
op|':'
string|"'1.2.3.4'"
op|'}'
op|','
op|'{'
string|"'address'"
op|':'
string|"'4.5.6.7'"
op|'}'
op|']'
newline|'\n'
name|'objects'
op|'.'
name|'FloatingIPList'
op|'.'
name|'destroy'
op|'('
name|'None'
op|','
name|'ips'
op|')'
newline|'\n'
name|'destroy_mock'
op|'.'
name|'assert_called_once_with'
op|'('
name|'None'
op|','
name|'ips'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'TestFloatingIPObject'
op|'('
name|'test_objects'
op|'.'
name|'_LocalTest'
op|','
nl|'\n'
DECL|class|TestFloatingIPObject
name|'_TestFloatingIPObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'class'
name|'TestRemoteFloatingIPObject'
op|'('
name|'test_objects'
op|'.'
name|'_RemoteTest'
op|','
nl|'\n'
DECL|class|TestRemoteFloatingIPObject
name|'_TestFloatingIPObject'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
endmarker|''
end_unit
