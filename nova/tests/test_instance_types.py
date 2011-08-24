begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Ken Pepple'
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
string|'"""\nUnit Tests for instance types code\n"""'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
op|'.'
name|'session'
name|'import'
name|'get_session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'models'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.compute'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeTestCase
name|'class'
name|'InstanceTypeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for instance type code"""'
newline|'\n'
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
name|'InstanceTypeTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'max_flavorid'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'InstanceTypes'
op|')'
op|'.'
name|'order_by'
op|'('
string|'"flavorid desc"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'max_id'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'InstanceTypes'
op|')'
op|'.'
name|'order_by'
op|'('
string|'"id desc"'
op|')'
op|'.'
name|'first'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flavorid'
op|'='
name|'max_flavorid'
op|'['
string|'"flavorid"'
op|']'
op|'+'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'max_id'
op|'['
string|'"id"'
op|']'
op|'+'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'name'
op|'='
name|'str'
op|'('
name|'int'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_nonexistent_flavor_name
dedent|''
name|'def'
name|'_nonexistent_flavor_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return an instance type name not in the DB"""'
newline|'\n'
name|'nonexistent_flavor'
op|'='
string|'"sdfsfsdf"'
newline|'\n'
name|'flavors'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
newline|'\n'
name|'while'
name|'nonexistent_flavor'
name|'in'
name|'flavors'
op|':'
newline|'\n'
indent|'            '
name|'nonexistent_flavor'
op|'+='
string|'"z"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'nonexistent_flavor'
newline|'\n'
nl|'\n'
DECL|member|_nonexistent_flavor_id
dedent|''
dedent|''
name|'def'
name|'_nonexistent_flavor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return an instance type ID not in the DB"""'
newline|'\n'
name|'nonexistent_flavor'
op|'='
number|'2700'
newline|'\n'
name|'flavor_ids'
op|'='
op|'['
name|'value'
op|'['
string|'"id"'
op|']'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
newline|'\n'
name|'while'
name|'nonexistent_flavor'
name|'in'
name|'flavor_ids'
op|':'
newline|'\n'
indent|'            '
name|'nonexistent_flavor'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'nonexistent_flavor'
newline|'\n'
nl|'\n'
DECL|member|_existing_flavor
dedent|''
dedent|''
name|'def'
name|'_existing_flavor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return first instance type name"""'
newline|'\n'
name|'return'
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_create_then_delete
dedent|''
name|'def'
name|'test_instance_type_create_then_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance types can be created"""'
newline|'\n'
name|'starting_inst_list'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
newline|'\n'
name|'instance_types'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
name|'self'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'new'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'len'
op|'('
name|'starting_inst_list'
op|')'
op|','
nl|'\n'
name|'len'
op|'('
name|'new'
op|')'
op|','
nl|'\n'
string|"'instance type was not created'"
op|')'
newline|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type'
op|'('
name|'self'
op|'.'
name|'id'
op|')'
op|'['
string|'"deleted"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'starting_inst_list'
op|','
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
op|')'
newline|'\n'
name|'instance_types'
op|'.'
name|'purge'
op|'('
name|'self'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'starting_inst_list'
op|')'
op|','
nl|'\n'
name|'len'
op|'('
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'instance type not purged'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_instance_types
dedent|''
name|'def'
name|'test_get_all_instance_types'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that all instance types can be retrieved"""'
newline|'\n'
name|'session'
op|'='
name|'get_session'
op|'('
op|')'
newline|'\n'
name|'total_instance_types'
op|'='
name|'session'
op|'.'
name|'query'
op|'('
name|'models'
op|'.'
name|'InstanceTypes'
op|')'
op|'.'
name|'count'
op|'('
op|')'
newline|'\n'
name|'inst_types'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'total_instance_types'
op|','
name|'len'
op|'('
name|'inst_types'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_create_args_should_fail
dedent|''
name|'def'
name|'test_invalid_create_args_should_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that instance type creation fails with invalid args"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'name'
op|','
number|'0'
op|','
number|'1'
op|','
number|'120'
op|','
name|'self'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'name'
op|','
number|'256'
op|','
op|'-'
number|'1'
op|','
number|'120'
op|','
name|'self'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'name'
op|','
number|'256'
op|','
number|'1'
op|','
string|'"aa"'
op|','
name|'self'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_existant_inst_type_shouldnt_delete
dedent|''
name|'def'
name|'test_non_existant_inst_type_shouldnt_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that instance type creation fails with invalid args"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ApiError'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_nonexistent_flavor_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_repeated_inst_types_should_raise_api_error
dedent|''
name|'def'
name|'test_repeated_inst_types_should_raise_api_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that instance duplicates raises ApiError"""'
newline|'\n'
name|'new_name'
op|'='
name|'self'
op|'.'
name|'name'
op|'+'
string|'"dup"'
newline|'\n'
name|'instance_types'
op|'.'
name|'create'
op|'('
name|'new_name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
name|'self'
op|'.'
name|'flavorid'
op|'+'
number|'1'
op|')'
newline|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|'('
name|'new_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'ApiError'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'create'
op|','
name|'new_name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
name|'self'
op|'.'
name|'flavorid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_destroy_with_no_name
dedent|''
name|'def'
name|'test_will_not_destroy_with_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure destroy sad path of no name raises error"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ApiError'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_nonexistent_flavor_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_purge_without_name
dedent|''
name|'def'
name|'test_will_not_purge_without_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure purge without a name raises error"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInstanceType'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'purge'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_purge_with_wrong_name
dedent|''
name|'def'
name|'test_will_not_purge_with_wrong_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure purge without correct name raises error"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ApiError'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'purge'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_nonexistent_flavor_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_bad_default_instance_type
dedent|''
name|'def'
name|'test_will_not_get_bad_default_instance_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""ensures error raised on bad default instance type"""'
newline|'\n'
name|'FLAGS'
op|'.'
name|'default_instance_type'
op|'='
name|'self'
op|'.'
name|'_nonexistent_flavor_name'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceTypeNotFoundByName'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_default_instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_instance_type_by_name_with_no_name
dedent|''
name|'def'
name|'test_will_not_get_instance_type_by_name_with_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure get by name returns default flavor with no name"""'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'instance_types'
op|'.'
name|'get_default_instance_type'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_instance_type_with_bad_name
dedent|''
name|'def'
name|'test_will_not_get_instance_type_with_bad_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure get by name returns default flavor with bad name"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_nonexistent_flavor_name'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_flavor_by_bad_flavor_id
dedent|''
name|'def'
name|'test_will_not_get_flavor_by_bad_flavor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure get by flavor raises error with wrong flavorid"""'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InstanceTypeNotFound'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_nonexistent_flavor_id'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
