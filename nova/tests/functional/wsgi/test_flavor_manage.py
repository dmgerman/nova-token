begin_unit
comment|'# Copyright 2015 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'import'
name|'testscenarios'
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
name|'as'
name|'ex'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'as'
name|'nova_fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
name|'import'
name|'integrated_helpers'
name|'as'
name|'helper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'policy_fixture'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rand_flavor
name|'def'
name|'rand_flavor'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'flav'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'name-%s'"
op|'%'
name|'helper'
op|'.'
name|'generate_random_alphanumeric'
op|'('
number|'10'
op|')'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'helper'
op|'.'
name|'generate_random_alphanumeric'
op|'('
number|'10'
op|')'
op|','
nl|'\n'
string|"'ram'"
op|':'
name|'int'
op|'('
name|'helper'
op|'.'
name|'generate_random_numeric'
op|'('
number|'2'
op|')'
op|')'
op|'+'
number|'1'
op|','
nl|'\n'
string|"'disk'"
op|':'
name|'int'
op|'('
name|'helper'
op|'.'
name|'generate_random_numeric'
op|'('
number|'3'
op|')'
op|')'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'int'
op|'('
name|'helper'
op|'.'
name|'generate_random_numeric'
op|'('
number|'1'
op|')'
op|')'
op|'+'
number|'1'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'flav'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'flav'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorManageFullstack
dedent|''
name|'class'
name|'FlavorManageFullstack'
op|'('
name|'testscenarios'
op|'.'
name|'WithScenarios'
op|','
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests for flavors manage administrative command.\n\n    Extension: os-flavors-manage\n\n    os-flavors-manage adds a set of admin functions to the flavors\n    resource for the creation and deletion of flavors.\n\n    POST /v2/flavors:\n\n    ::\n\n        {\n            \'name\': NAME, # string, required unique\n            \'id\': ID, # string, required unique\n            \'ram\': RAM, # in MB, required\n            \'vcpus\': VCPUS, # int value, required\n            \'disk\': DISK, # in GB, required\n            \'OS-FLV-EXT-DATA:ephemeral\', # in GB, ephemeral disk size\n            \'is_public\': IS_PUBLIC, # boolean\n            \'swap\': SWAP, # in GB?\n            \'rxtx_factor\': RXTX, # ???\n        }\n\n    Returns Flavor\n\n    DELETE /v2/flavors/ID\n\n\n    Functional Test Scope:\n\n    This test starts the wsgi stack for the nova api services, uses an\n    in memory database to ensure the path through the wsgi layer to\n    the database.\n\n    """'
newline|'\n'
nl|'\n'
DECL|variable|_additional_fixtures
name|'_additional_fixtures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|variable|scenarios
name|'scenarios'
op|'='
op|'['
nl|'\n'
comment|'# test v2.1 base microversion'
nl|'\n'
op|'('
string|"'v2_1'"
op|','
op|'{'
nl|'\n'
string|"'api_major_version'"
op|':'
string|"'v2.1'"
op|'}'
op|')'
op|','
nl|'\n'
op|']'
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
name|'FlavorManageFullstack'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# load any additional fixtures specified by the scenario'
nl|'\n'
name|'for'
name|'fix'
name|'in'
name|'self'
op|'.'
name|'_additional_fixtures'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fix'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'RealPolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'api_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
nl|'\n'
name|'nova_fixtures'
op|'.'
name|'OSAPIFixture'
op|'('
nl|'\n'
name|'api_version'
op|'='
name|'self'
op|'.'
name|'api_major_version'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sdague): because this test is primarily an admin API'
nl|'\n'
comment|'# test default self.api to the admin api.'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'api_fixture'
op|'.'
name|'admin_api'
newline|'\n'
name|'self'
op|'.'
name|'user_api'
op|'='
name|'api_fixture'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorDbEqual
dedent|''
name|'def'
name|'assertFlavorDbEqual'
op|'('
name|'self'
op|','
name|'flav'
op|','
name|'flavdb'
op|')'
op|':'
newline|'\n'
comment|'# a mapping of the REST params to the db fields'
nl|'\n'
indent|'        '
name|'mapping'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'name'"
op|','
nl|'\n'
string|"'disk'"
op|':'
string|"'root_gb'"
op|','
nl|'\n'
string|"'ram'"
op|':'
string|"'memory_mb'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
string|"'vcpus'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'flavorid'"
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'swap'"
nl|'\n'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'flav'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flav'
op|'['
name|'k'
op|']'
op|','
name|'flavdb'
op|'['
name|'v'
op|']'
op|','
nl|'\n'
string|'"%s != %s"'
op|'%'
op|'('
name|'flav'
op|','
name|'flavdb'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorAPIEqual
dedent|''
dedent|''
dedent|''
name|'def'
name|'assertFlavorAPIEqual'
op|'('
name|'self'
op|','
name|'flav'
op|','
name|'flavapi'
op|')'
op|':'
newline|'\n'
comment|'# for all keys in the flavor, ensure they are correctly set in'
nl|'\n'
comment|'# flavapi response.'
nl|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'flav'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'flavapi'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flav'
op|'['
name|'k'
op|']'
op|','
name|'flavapi'
op|'['
name|'k'
op|']'
op|','
nl|'\n'
string|'"%s != %s"'
op|'%'
op|'('
name|'flav'
op|','
name|'flavapi'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Missing key: %s in flavor: %s"'
op|'%'
op|'('
name|'k'
op|','
name|'flavapi'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorInList
dedent|''
dedent|''
dedent|''
name|'def'
name|'assertFlavorInList'
op|'('
name|'self'
op|','
name|'flav'
op|','
name|'flavlist'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'item'
name|'in'
name|'flavlist'
op|'['
string|"'flavors'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'flav'
op|'['
string|"'id'"
op|']'
op|'=='
name|'item'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'flav'
op|'['
string|"'name'"
op|']'
op|','
name|'item'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'fail'
op|'('
string|'"%s not found in %s"'
op|'%'
op|'('
name|'flav'
op|','
name|'flavlist'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertFlavorNotInList
dedent|''
name|'def'
name|'assertFlavorNotInList'
op|'('
name|'self'
op|','
name|'flav'
op|','
name|'flavlist'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'item'
name|'in'
name|'flavlist'
op|'['
string|"'flavors'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'flav'
op|'['
string|"'id'"
op|']'
op|'=='
name|'item'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'fail'
op|'('
string|'"%s found in %s"'
op|'%'
op|'('
name|'flav'
op|','
name|'flavlist'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_manage_func_negative
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_flavor_manage_func_negative'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test flavor manage edge conditions.\n\n        - Bogus body is a 400\n        - Unknown flavor is a 404\n        - Deleting unknown flavor is a 404\n        """'
newline|'\n'
comment|'# Test for various API failure conditions'
nl|'\n'
comment|'# bad body is 400'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
string|"''"
op|','
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
comment|'# get unknown flavor is 404'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/foo'"
op|','
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
comment|'# delete unknown flavor is 404'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/foo'"
op|','
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
comment|'# bounds conditions - invalid vcpus'
nl|'\n'
name|'flav'
op|'='
op|'{'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
name|'vcpus'
op|'='
number|'0'
op|')'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'flav'
op|','
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status'
op|','
name|'resp'
op|')'
newline|'\n'
comment|"# ... and ensure that we didn't leak it into the db"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ex'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|','
nl|'\n'
name|'ctx'
op|','
name|'flav'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# bounds conditions - invalid ram'
nl|'\n'
name|'flav'
op|'='
op|'{'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
name|'ram'
op|'='
number|'0'
op|')'
op|'}'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'flav'
op|','
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
comment|"# ... and ensure that we didn't leak it into the db"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ex'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|','
nl|'\n'
name|'ctx'
op|','
name|'flav'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sdague): if there are other bounds conditions that'
nl|'\n'
comment|'# should be checked, stack them up here.'
nl|'\n'
nl|'\n'
DECL|member|test_flavor_manage_deleted
dedent|''
name|'def'
name|'test_flavor_manage_deleted'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure the behavior around a deleted flavor is stable.\n\n        - Fetching a deleted flavor works, and returns the flavor info.\n        - Listings should not contain deleted flavors\n\n        """'
newline|'\n'
comment|'# create a deleted flavor'
nl|'\n'
name|'new_flav'
op|'='
op|'{'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'new_flav'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/%s'"
op|'%'
name|'new_flav'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# deleted flavor should not show up in a list'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_get'
op|'('
string|"'flavors'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorNotInList'
op|'('
name|'new_flav'
op|'['
string|"'flavor'"
op|']'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_create_frozen
dedent|''
name|'def'
name|'test_flavor_create_frozen'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'db'
op|'.'
name|'flavor_create'
op|'('
name|'ctx'
op|','
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'foo'"
op|','
string|"'memory_mb'"
op|':'
number|'512'
op|','
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'root_gb'"
op|':'
number|'1'
op|','
string|"'ephemeral_gb'"
op|':'
number|'0'
op|','
string|"'flavorid'"
op|':'
string|"'foo'"
op|','
nl|'\n'
string|"'swap'"
op|':'
number|'0'
op|','
string|"'rxtx_factor'"
op|':'
number|'1.0'
op|','
string|"'vcpu_weight'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'disabled'"
op|':'
name|'False'
op|','
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'new_flav'
op|'='
op|'{'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
op|')'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'new_flav'
op|','
nl|'\n'
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'409'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_manage_func
dedent|''
name|'def'
name|'test_flavor_manage_func'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Basic flavor creation lifecycle testing.\n\n        - Creating a flavor\n        - Ensure it\'s in the database\n        - Ensure it\'s in the listing\n        - Delete it\n        - Ensure it\'s hidden in the database\n        """'
newline|'\n'
nl|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'flav1'
op|'='
op|'{'
nl|'\n'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Create flavor and ensure it made it to the database'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'flav1'
op|')'
newline|'\n'
nl|'\n'
name|'flav1db'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'ctx'
op|','
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorDbEqual'
op|'('
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|','
name|'flav1db'
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure new flavor is seen in the listing'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_get'
op|'('
string|"'flavors'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFlavorInList'
op|'('
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete flavor and ensure it was removed from the database'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/%s'"
op|'%'
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ex'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|','
nl|'\n'
name|'ctx'
op|','
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/%s'"
op|'%'
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_manage_permissions
dedent|''
name|'def'
name|'test_flavor_manage_permissions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that regular users can\'t create or delete flavors.\n\n        """'
newline|'\n'
name|'ctx'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'flav1'
op|'='
op|'{'
string|"'flavor'"
op|':'
name|'rand_flavor'
op|'('
op|')'
op|'}'
newline|'\n'
nl|'\n'
comment|"# Ensure user can't create flavor"
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'user_api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'flav1'
op|','
nl|'\n'
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'403'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
comment|"# ... and that it didn't leak through"
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ex'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|','
nl|'\n'
name|'ctx'
op|','
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create the flavor as the admin user'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_post'
op|'('
string|"'flavors'"
op|','
name|'flav1'
op|')'
newline|'\n'
nl|'\n'
comment|"# Ensure user can't delete flavors from our cloud"
nl|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'user_api'
op|'.'
name|'api_delete'
op|'('
string|"'flavors/%s'"
op|'%'
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'check_response_status'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'403'
op|','
name|'resp'
op|'.'
name|'status'
op|')'
newline|'\n'
comment|"# ... and ensure that we didn't actually delete the flavor,"
nl|'\n'
comment|'# this will throw an exception if we did.'
nl|'\n'
name|'objects'
op|'.'
name|'Flavor'
op|'.'
name|'get_by_flavor_id'
op|'('
name|'ctx'
op|','
name|'flav1'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
