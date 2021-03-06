begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'block_device_mapping'
name|'as'
name|'block_device_mapping_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'multiple_create'
name|'as'
name|'multiple_create_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'servers'
name|'as'
name|'servers_v21'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
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
name|'network'
name|'import'
name|'manager'
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
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
name|'import'
name|'fake'
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
DECL|function|return_security_group
name|'def'
name|'return_security_group'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MultiCreateExtensionTestV21
dedent|''
name|'class'
name|'MultiCreateExtensionTestV21'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|validation_error
indent|'    '
name|'validation_error'
op|'='
name|'exception'
op|'.'
name|'ValidationError'
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
string|'"""Shared implementation for tests below that create instance."""'
newline|'\n'
name|'super'
op|'('
name|'MultiCreateExtensionTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'enable_instance_password'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
string|"'os-multiple-create'"
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_mult_create_controller'
op|'='
name|'servers_v21'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_create
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
number|'3'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'def_image_ref'
op|'='
string|"'http://localhost/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'+='
number|'1'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|'**'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'instance_cache_num'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
name|'or'
string|"'test'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'inst'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'inst_type'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fead::1234'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'def_image_ref'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"task_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"security_groups"'
op|':'
name|'inst'
op|'['
string|"'security_groups'"
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Stub for compute/api create() pulling in instance after\n            scheduling\n            """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'uuid'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|server_update
dedent|''
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'params'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance_uuid'
op|']'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_method
dedent|''
name|'def'
name|'fake_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|project_get_networks
dedent|''
name|'def'
name|'project_get_networks'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'1'"
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_add_security_group'"
op|','
nl|'\n'
name|'return_security_group'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.project_get_networks'"
op|','
name|'project_get_networks'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_create'"
op|','
name|'instance_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_system_metadata_update'"
op|','
name|'fake_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_get'"
op|','
name|'instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_update'"
op|','
name|'instance_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stub_out'
op|'('
string|"'nova.db.instance_update_and_get_original'"
op|','
nl|'\n'
name|'server_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'manager'
op|'.'
name|'VlanManager'
op|','
string|"'allocate_fixed_ip'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_extra
dedent|''
name|'def'
name|'_test_create_extra'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'False'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'imageRef'
op|'='
name|'image_uuid'
op|','
name|'flavorRef'
op|'='
number|'2'
op|')'
newline|'\n'
name|'if'
name|'no_image'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'pop'
op|'('
string|"'imageRef'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
newline|'\n'
name|'if'
name|'override_controller'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'override_controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_check_multiple_create_extension_disabled
dedent|''
dedent|''
name|'def'
name|'_check_multiple_create_extension_disabled'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# NOTE: on v2.1 API, "create a server" API doesn\'t add the following'
nl|'\n'
comment|'# attributes into kwargs when non-loading multiple_create extension.'
nl|'\n'
comment|'# However, v2.0 API adds them as values "1" instead. So we need to'
nl|'\n'
comment|'# define checking methods for each API here.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'min_count'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'max_count'"
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_multiple_create_disabled
dedent|''
name|'def'
name|'test_create_instance_with_multiple_create_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'min_count'
op|'='
number|'2'
newline|'\n'
name|'max_count'
op|'='
number|'3'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
name|'min_count'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
name|'max_count'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_check_multiple_create_extension_disabled'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
nl|'\n'
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_mult_create_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_create_with_string_type_min_and_max
dedent|''
name|'def'
name|'test_multiple_create_with_string_type_min_and_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'min_count'
op|'='
string|"'2'"
newline|'\n'
name|'max_count'
op|'='
string|"'3'"
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
name|'min_count'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
name|'max_count'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'kwargs'
op|'['
string|"'min_count'"
op|']'
op|','
name|'int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'kwargs'
op|'['
string|"'max_count'"
op|']'
op|','
name|'int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'min_count'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'max_count'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_multiple_create_enabled
dedent|''
name|'def'
name|'test_create_instance_with_multiple_create_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'min_count'
op|'='
number|'2'
newline|'\n'
name|'max_count'
op|'='
number|'3'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
name|'min_count'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
name|'max_count'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'min_count'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'max_count'"
op|']'
op|','
number|'3'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_negative_min
dedent|''
name|'def'
name|'test_create_instance_invalid_negative_min'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_negative_max
dedent|''
name|'def'
name|'test_create_instance_invalid_negative_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_blank_min
dedent|''
name|'def'
name|'test_create_instance_with_blank_min'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
string|"''"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavor_ref'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_blank_max
dedent|''
name|'def'
name|'test_create_instance_with_blank_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
string|"''"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavor_ref'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_min_greater_than_max
dedent|''
name|'def'
name|'test_create_instance_invalid_min_greater_than_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
number|'4'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
number|'2'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_alpha_min
dedent|''
name|'def'
name|'test_create_instance_invalid_alpha_min'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
string|"'abcd'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_alpha_max
dedent|''
name|'def'
name|'test_create_instance_invalid_alpha_max'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
string|"'abcd'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances
dedent|''
name|'def'
name|'test_create_multiple_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test creating multiple instances but not asking for\n        reservation_id\n        """'
newline|'\n'
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
number|'2'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|'}'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
nl|'\n'
name|'instance_uuids'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'res'
op|'['
string|'"server"'
op|']'
op|'['
string|'"id"'
op|']'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_admin_password_len'
op|'('
name|'res'
op|'['
string|'"server"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances_pass_disabled
dedent|''
name|'def'
name|'test_create_multiple_instances_pass_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test creating multiple instances but not asking for\n        reservation_id\n        """'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'enable_instance_password'
op|'='
name|'False'
op|')'
newline|'\n'
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
number|'2'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|'}'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
nl|'\n'
name|'instance_uuids'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'res'
op|'['
string|'"server"'
op|']'
op|'['
string|'"id"'
op|']'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_admin_password_missing'
op|'('
name|'res'
op|'['
string|'"server"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_admin_password_len
dedent|''
name|'def'
name|'_check_admin_password_len'
op|'('
name|'self'
op|','
name|'server_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""utility function - check server_dict for admin_password length."""'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'password_length'
op|','
nl|'\n'
name|'len'
op|'('
name|'server_dict'
op|'['
string|'"adminPass"'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_admin_password_missing
dedent|''
name|'def'
name|'_check_admin_password_missing'
op|'('
name|'self'
op|','
name|'server_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""utility function - check server_dict for admin_password absence."""'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|'"admin_password"'
op|','
name|'server_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_multiple_instances_resv_id_return
dedent|''
name|'def'
name|'_create_multiple_instances_resv_id_return'
op|'('
name|'self'
op|','
name|'resv_id_return'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test creating multiple instances with asking for\n        reservation_id\n        """'
newline|'\n'
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
number|'2'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|'}'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'RRID_ATTRIBUTE_NAME'
op|':'
name|'resv_id_return'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'reservation_id'
op|'='
name|'res'
op|'.'
name|'obj'
op|'['
string|"'reservation_id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'reservation_id'
op|','
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNotNone'
op|'('
name|'reservation_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'reservation_id'
op|')'
op|'>'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances_with_resv_id_return
dedent|''
name|'def'
name|'test_create_multiple_instances_with_resv_id_return'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_multiple_instances_resv_id_return'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances_with_string_resv_id_return
dedent|''
name|'def'
name|'test_create_multiple_instances_with_string_resv_id_return'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_create_multiple_instances_resv_id_return'
op|'('
string|'"True"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances_with_multiple_volume_bdm
dedent|''
name|'def'
name|'test_create_multiple_instances_with_multiple_volume_bdm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that a BadRequest is raised if multiple instances\n        are requested with a list of block device mappings for volumes.\n        """'
newline|'\n'
name|'min_count'
op|'='
number|'2'
newline|'\n'
name|'bdm'
op|'='
op|'['
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'uuid'"
op|':'
string|"'vol-xxxx'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'uuid'"
op|':'
string|"'vol-yyyy'"
op|'}'
nl|'\n'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
name|'block_device_mapping_v21'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'bdm'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
name|'min_count'
nl|'\n'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'min_count'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Cannot attach one or more volumes to multiple "'
nl|'\n'
string|'"instances"'
op|','
name|'exc'
op|'.'
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instances_with_single_volume_bdm
dedent|''
name|'def'
name|'test_create_multiple_instances_with_single_volume_bdm'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that a BadRequest is raised if multiple instances\n        are requested to boot from a single volume.\n        """'
newline|'\n'
name|'min_count'
op|'='
number|'2'
newline|'\n'
name|'bdm'
op|'='
op|'['
op|'{'
string|"'source_type'"
op|':'
string|"'volume'"
op|','
string|"'uuid'"
op|':'
string|"'vol-xxxx'"
op|'}'
op|']'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
name|'block_device_mapping_v21'
op|'.'
name|'ATTRIBUTE_NAME'
op|':'
name|'bdm'
op|','
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
name|'min_count'
nl|'\n'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'min_count'"
op|']'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
string|"'vol-xxxx'"
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Cannot attach one or more volumes to multiple "'
nl|'\n'
string|'"instances"'
op|','
name|'exc'
op|'.'
name|'explanation'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instance_with_non_integer_max_count
dedent|''
name|'def'
name|'test_create_multiple_instance_with_non_integer_max_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MAX_ATTRIBUTE_NAME'
op|':'
number|'2.5'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|'}'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_multiple_instance_with_non_integer_min_count
dedent|''
name|'def'
name|'test_create_multiple_instance_with_non_integer_min_count'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/123/flavors/3'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
name|'multiple_create_v21'
op|'.'
name|'MIN_ATTRIBUTE_NAME'
op|':'
number|'2.5'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|'}'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'validation_error'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
