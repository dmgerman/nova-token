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
nl|'\n'
DECL|member|_generate_name
dedent|''
name|'def'
name|'_generate_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return a name not in the DB"""'
newline|'\n'
name|'nonexistent_flavor'
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
DECL|member|_generate_flavorid
dedent|''
dedent|''
name|'def'
name|'_generate_flavorid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return a flavorid not in the DB"""'
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
name|'name'
op|'='
string|"'Small Flavor'"
newline|'\n'
name|'flavorid'
op|'='
string|"'flavor1'"
newline|'\n'
nl|'\n'
name|'original_list'
op|'='
name|'instance_types'
op|'.'
name|'get_all_types'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# create new type and make sure values stick'
nl|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'create'
op|'('
name|'name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
name|'flavorid'
op|')'
newline|'\n'
name|'inst_type_id'
op|'='
name|'inst_type'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'flavorid'"
op|']'
op|','
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'name'"
op|']'
op|','
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'memory_mb'"
op|']'
op|','
number|'256'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'vcpus'"
op|']'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'local_gb'"
op|']'
op|','
number|'120'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'swap'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'rxtx_quota'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_type'
op|'['
string|"'rxtx_cap'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure new type shows up in list'
nl|'\n'
name|'new_list'
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
name|'original_list'
op|')'
op|','
name|'len'
op|'('
name|'new_list'
op|')'
op|','
nl|'\n'
string|"'instance type was not created'"
op|')'
newline|'\n'
nl|'\n'
comment|'# destroy instance and make sure deleted flag is set to True'
nl|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|'('
name|'name'
op|')'
newline|'\n'
name|'inst_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type'
op|'('
name|'inst_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'inst_type'
op|'['
string|'"deleted"'
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# deleted instance should not be in list anymoer'
nl|'\n'
name|'new_list'
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
name|'original_list'
op|','
name|'new_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# ensure instances are gone after purge'
nl|'\n'
name|'instance_types'
op|'.'
name|'purge'
op|'('
name|'name'
op|')'
newline|'\n'
name|'new_list'
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
name|'original_list'
op|','
name|'new_list'
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
name|'invalid_sigs'
op|'='
op|'['
nl|'\n'
op|'('
op|'('
string|"'Zero memory'"
op|','
number|'0'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Negative memory'"
op|','
op|'-'
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer memory'"
op|','
string|"'asdf'"
op|','
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
op|'('
string|"'Zero vcpus'"
op|','
number|'256'
op|','
number|'0'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Negative vcpus'"
op|','
number|'256'
op|','
op|'-'
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer vcpus'"
op|','
number|'256'
op|','
string|"'a'"
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
op|'('
string|"'Negative storage'"
op|','
number|'256'
op|','
number|'1'
op|','
op|'-'
number|'1'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer storage'"
op|','
number|'256'
op|','
number|'1'
op|','
string|"'a'"
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
op|'('
string|"'Negative swap'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
string|"'swap'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer swap'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'flavor1'"
op|')'
op|','
op|'{'
string|"'swap'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
op|'('
string|"'Negative rxtx_quota'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'f1'"
op|')'
op|','
op|'{'
string|"'rxtx_quota'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer rxtx_quota'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'f1'"
op|')'
op|','
op|'{'
string|"'rxtx_quota'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
nl|'\n'
op|'('
op|'('
string|"'Negative rxtx_cap'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'f1'"
op|')'
op|','
op|'{'
string|"'rxtx_cap'"
op|':'
op|'-'
number|'1'
op|'}'
op|')'
op|','
nl|'\n'
op|'('
op|'('
string|"'Non-integer rxtx_cap'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'10'
op|','
string|"'f1'"
op|')'
op|','
op|'{'
string|"'rxtx_cap'"
op|':'
string|"'a'"
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'args'
op|','
name|'kwargs'
op|')'
name|'in'
name|'invalid_sigs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'create'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_existent_inst_type_shouldnt_delete
dedent|''
dedent|''
name|'def'
name|'test_non_existent_inst_type_shouldnt_delete'
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
name|'InstanceTypeNotFoundByName'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|','
nl|'\n'
string|"'unknown_flavor'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_duplicate_names_fail
dedent|''
name|'def'
name|'test_duplicate_names_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that name duplicates raise ApiError"""'
newline|'\n'
name|'name'
op|'='
string|"'some_name'"
newline|'\n'
name|'instance_types'
op|'.'
name|'create'
op|'('
name|'name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
string|"'flavor1'"
op|')'
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
name|'create'
op|','
nl|'\n'
name|'name'
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
string|"'flavor2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_duplicate_flavorids_fail
dedent|''
name|'def'
name|'test_duplicate_flavorids_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensures that flavorid duplicates raise ApiError"""'
newline|'\n'
name|'flavorid'
op|'='
string|"'flavor1'"
newline|'\n'
name|'instance_types'
op|'.'
name|'create'
op|'('
string|"'name one'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
name|'flavorid'
op|')'
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
name|'create'
op|','
nl|'\n'
string|"'name two'"
op|','
number|'256'
op|','
number|'1'
op|','
number|'120'
op|','
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
name|'InstanceTypeNotFoundByName'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'destroy'
op|','
name|'None'
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
name|'InstanceTypeNotFoundByName'
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
name|'InstanceTypeNotFound'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'purge'
op|','
nl|'\n'
string|"'unknown_flavor'"
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
string|"'unknown_flavor'"
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
DECL|member|test_will_get_instance_type_by_id
dedent|''
name|'def'
name|'test_will_get_instance_type_by_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'default_instance_type'
op|'='
name|'instance_types'
op|'.'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
name|'instance_type_id'
op|'='
name|'default_instance_type'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'fetched'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type'
op|'('
name|'instance_type_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'default_instance_type'
op|','
name|'fetched'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_instance_type_by_unknown_id
dedent|''
name|'def'
name|'test_will_not_get_instance_type_by_unknown_id'
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
number|'10000'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_instance_type_with_bad_id
dedent|''
name|'def'
name|'test_will_not_get_instance_type_with_bad_id'
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
string|"'asdf'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_instance_type_get_by_None_name_returns_default
dedent|''
name|'def'
name|'test_instance_type_get_by_None_name_returns_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure get by name returns default flavor with no name"""'
newline|'\n'
name|'default'
op|'='
name|'instance_types'
op|'.'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
name|'actual'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'default'
op|','
name|'actual'
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
name|'InstanceTypeNotFoundByName'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|','
number|'10000'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_get_instance_by_unknown_flavor_id
dedent|''
name|'def'
name|'test_will_not_get_instance_by_unknown_flavor_id'
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
name|'FlavorNotFound'
op|','
nl|'\n'
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|','
nl|'\n'
string|"'unknown_flavor'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_get_instance_by_flavor_id
dedent|''
name|'def'
name|'test_will_get_instance_by_flavor_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'default_instance_type'
op|'='
name|'instance_types'
op|'.'
name|'get_default_instance_type'
op|'('
op|')'
newline|'\n'
name|'flavorid'
op|'='
name|'default_instance_type'
op|'['
string|"'flavorid'"
op|']'
newline|'\n'
name|'fetched'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type_by_flavor_id'
op|'('
name|'flavorid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'default_instance_type'
op|','
name|'fetched'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InstanceTypeFilteringTest
dedent|''
dedent|''
name|'class'
name|'InstanceTypeFilteringTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test cases for the filter option available for instance_type_get_all"""'
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
name|'InstanceTypeFilteringTest'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFilterResults
dedent|''
name|'def'
name|'assertFilterResults'
op|'('
name|'self'
op|','
name|'filters'
op|','
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst_types'
op|'='
name|'db'
op|'.'
name|'instance_type_get_all'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'filters'
op|'='
name|'filters'
op|')'
newline|'\n'
name|'inst_names'
op|'='
op|'['
name|'i'
op|'['
string|"'name'"
op|']'
name|'for'
name|'i'
name|'in'
name|'inst_types'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'inst_names'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_filters
dedent|''
name|'def'
name|'test_no_filters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filters'
op|'='
name|'None'
newline|'\n'
name|'expected'
op|'='
op|'['
string|"'m1.large'"
op|','
string|"'m1.medium'"
op|','
string|"'m1.small'"
op|','
string|"'m1.tiny'"
op|','
nl|'\n'
string|"'m1.xlarge'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFilterResults'
op|'('
name|'filters'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_min_memory_mb_filter
dedent|''
name|'def'
name|'test_min_memory_mb_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Exclude tiny instance which is 512 MB"""'
newline|'\n'
name|'filters'
op|'='
name|'dict'
op|'('
name|'min_memory_mb'
op|'='
number|'513'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
string|"'m1.large'"
op|','
string|"'m1.medium'"
op|','
string|"'m1.small'"
op|','
string|"'m1.xlarge'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFilterResults'
op|'('
name|'filters'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_min_local_gb_filter
dedent|''
name|'def'
name|'test_min_local_gb_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Exclude everything but large and xlarge which have >= 80 GB"""'
newline|'\n'
name|'filters'
op|'='
name|'dict'
op|'('
name|'min_local_gb'
op|'='
number|'80'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
string|"'m1.large'"
op|','
string|"'m1.xlarge'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFilterResults'
op|'('
name|'filters'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_min_memory_mb_AND_local_gb_filter
dedent|''
name|'def'
name|'test_min_memory_mb_AND_local_gb_filter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Exclude everything but large and xlarge which have >= 80 GB"""'
newline|'\n'
name|'filters'
op|'='
name|'dict'
op|'('
name|'min_memory_mb'
op|'='
number|'16384'
op|','
name|'min_local_gb'
op|'='
number|'80'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
string|"'m1.xlarge'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFilterResults'
op|'('
name|'filters'
op|','
name|'expected'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
