begin_unit
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2014 NEC Corporation.  All rights reserved.'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'stevedore'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'compute'
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
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_bad_extension
name|'class'
name|'fake_bad_extension'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|name
indent|'    '
name|'name'
op|'='
string|'"fake_bad_extension"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"fake-bad"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_stevedore_enabled_extensions
dedent|''
name|'class'
name|'fake_stevedore_enabled_extensions'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'namespace'
op|','
name|'check_func'
op|','
name|'invoke_on_load'
op|'='
name|'False'
op|','
nl|'\n'
name|'invoke_args'
op|'='
op|'('
op|')'
op|','
name|'invoke_kwds'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extensions'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|map
dedent|''
name|'def'
name|'map'
op|'('
name|'self'
op|','
name|'func'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|__iter__
dedent|''
name|'def'
name|'__iter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iter'
op|'('
name|'self'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_loaded_extension_info
dedent|''
dedent|''
name|'class'
name|'fake_loaded_extension_info'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|register_extension
dedent|''
name|'def'
name|'register_extension'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'extensions'
op|'['
name|'ext'
op|']'
op|'='
name|'ext'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_extensions
dedent|''
name|'def'
name|'get_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'core1'"
op|':'
name|'None'
op|','
string|"'core2'"
op|':'
name|'None'
op|','
string|"'noncore1'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionLoadingTestCase
dedent|''
dedent|''
name|'class'
name|'ExtensionLoadingTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_set_v21_core
indent|'    '
name|'def'
name|'_set_v21_core'
op|'('
name|'self'
op|','
name|'core_extensions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'core_extensions'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_loaded
dedent|''
name|'def'
name|'test_extensions_loaded'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'servers'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_bad_extension
dedent|''
name|'def'
name|'test_check_bad_extension'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'loaded_ext_info'
op|'='
name|'extension_info'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'loaded_ext_info'
op|'.'
name|'_check_extension'
op|'('
name|'fake_bad_extension'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_blacklist
dedent|''
name|'def'
name|'test_extensions_blacklist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
op|'['
string|"'os-hosts'"
op|']'
op|','
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.api.openstack.APIRouterV21._register_resources_list'"
op|')'
newline|'\n'
DECL|member|test_extensions_inherit
name|'def'
name|'test_extensions_inherit'
op|'('
name|'self'
op|','
name|'mock_register'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'servers'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-volumes'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
name|'mock_register'
op|'.'
name|'assert_called_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
name|'ext_no_inherits'
op|'='
name|'mock_register'
op|'.'
name|'call_args_list'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'ext_has_inherits'
op|'='
name|'mock_register'
op|'.'
name|'call_args_list'
op|'['
number|'1'
op|']'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
comment|'# os-volumes inherits from servers'
nl|'\n'
name|'name_list'
op|'='
op|'['
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
name|'for'
name|'ext'
name|'in'
name|'ext_has_inherits'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-volumes'"
op|','
name|'name_list'
op|')'
newline|'\n'
name|'name_list'
op|'='
op|'['
name|'ext'
op|'.'
name|'obj'
op|'.'
name|'alias'
name|'for'
name|'ext'
name|'in'
name|'ext_no_inherits'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'servers'"
op|','
name|'name_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_whitelist_accept
dedent|''
name|'def'
name|'test_extensions_whitelist_accept'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(maurosr): just to avoid to get an exception raised for not'
nl|'\n'
comment|'# loading all core api.'
nl|'\n'
indent|'        '
name|'v21_core'
op|'='
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
newline|'\n'
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_set_v21_core'
op|','
name|'v21_core'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_whitelist'"
op|','
op|'['
string|"'servers'"
op|','
string|"'os-hosts'"
op|']'
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_whitelist_block
dedent|''
name|'def'
name|'test_extensions_whitelist_block'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(maurosr): just to avoid to get an exception raised for not'
nl|'\n'
comment|'# loading all core api.'
nl|'\n'
indent|'        '
name|'v21_core'
op|'='
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
newline|'\n'
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_set_v21_core'
op|','
name|'v21_core'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_whitelist'"
op|','
op|'['
string|"'servers'"
op|']'
op|','
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_blacklist_overrides_whitelist
dedent|''
name|'def'
name|'test_blacklist_overrides_whitelist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(maurosr): just to avoid to get an exception raised for not'
nl|'\n'
comment|'# loading all core api.'
nl|'\n'
indent|'        '
name|'v21_core'
op|'='
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
newline|'\n'
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'servers'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_set_v21_core'
op|','
name|'v21_core'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_whitelist'"
op|','
op|'['
string|"'servers'"
op|','
string|"'os-hosts'"
op|']'
op|','
nl|'\n'
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
op|'['
string|"'os-hosts'"
op|']'
op|','
string|"'osapi_v21'"
op|')'
newline|'\n'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'os-hosts'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'servers'"
op|','
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
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
name|'app'
op|'.'
name|'_loaded_extension_info'
op|'.'
name|'extensions'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_missing_core_extensions
dedent|''
name|'def'
name|'test_get_missing_core_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'v21_core'
op|'='
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
newline|'\n'
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'core1'"
op|','
string|"'core2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_set_v21_core'
op|','
name|'v21_core'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
nl|'\n'
name|'compute'
op|'.'
name|'APIRouterV21'
op|'.'
name|'get_missing_core_extensions'
op|'('
nl|'\n'
op|'['
string|"'core1'"
op|','
string|"'core2'"
op|','
string|"'noncore1'"
op|']'
op|')'
op|')'
op|')'
newline|'\n'
name|'missing_core'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'.'
name|'get_missing_core_extensions'
op|'('
nl|'\n'
op|'['
string|"'core1'"
op|']'
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
name|'missing_core'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'core2'"
op|','
name|'missing_core'
op|')'
newline|'\n'
name|'missing_core'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'.'
name|'get_missing_core_extensions'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'missing_core'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'core1'"
op|','
name|'missing_core'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'core2'"
op|','
name|'missing_core'
op|')'
newline|'\n'
name|'missing_core'
op|'='
name|'compute'
op|'.'
name|'APIRouterV21'
op|'.'
name|'get_missing_core_extensions'
op|'('
nl|'\n'
op|'['
string|"'noncore1'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'missing_core'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'core1'"
op|','
name|'missing_core'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'core2'"
op|','
name|'missing_core'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_core_extensions_present
dedent|''
name|'def'
name|'test_core_extensions_present'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'stevedore'
op|'.'
name|'enabled'
op|','
string|"'EnabledExtensionManager'"
op|','
nl|'\n'
name|'fake_stevedore_enabled_extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'extension_info'
op|','
string|"'LoadedExtensionInfo'"
op|','
nl|'\n'
name|'fake_loaded_extension_info'
op|')'
newline|'\n'
name|'v21_core'
op|'='
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
newline|'\n'
name|'openstack'
op|'.'
name|'API_V21_CORE_EXTENSIONS'
op|'='
name|'set'
op|'('
op|'['
string|"'core1'"
op|','
string|"'core2'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'self'
op|'.'
name|'_set_v21_core'
op|','
name|'v21_core'
op|')'
newline|'\n'
comment|'# if no core API extensions are missing then an exception will'
nl|'\n'
comment|'# not be raised when creating an instance of compute.APIRouterV21'
nl|'\n'
name|'compute'
op|'.'
name|'APIRouterV21'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_core_extensions_missing
dedent|''
name|'def'
name|'test_core_extensions_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'stevedore'
op|'.'
name|'enabled'
op|','
string|"'EnabledExtensionManager'"
op|','
nl|'\n'
name|'fake_stevedore_enabled_extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'extension_info'
op|','
string|"'LoadedExtensionInfo'"
op|','
nl|'\n'
name|'fake_loaded_extension_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CoreAPIMissing'
op|','
name|'compute'
op|'.'
name|'APIRouterV21'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_expected_error
dedent|''
name|'def'
name|'test_extensions_expected_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|function|fake_func
name|'def'
name|'fake_func'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'fake_func'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_expected_error_from_list
dedent|''
name|'def'
name|'test_extensions_expected_error_from_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'403'
op|')'
op|')'
newline|'\n'
DECL|function|fake_func
name|'def'
name|'fake_func'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|','
name|'fake_func'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_unexpected_error
dedent|''
name|'def'
name|'test_extensions_unexpected_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|function|fake_func
name|'def'
name|'fake_func'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|','
name|'fake_func'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_unexpected_error_from_list
dedent|''
name|'def'
name|'test_extensions_unexpected_error_from_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'404'
op|','
number|'413'
op|')'
op|')'
newline|'\n'
DECL|function|fake_func
name|'def'
name|'fake_func'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|','
name|'fake_func'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_unexpected_policy_not_authorized_error
dedent|''
name|'def'
name|'test_extensions_unexpected_policy_not_authorized_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|function|fake_func
name|'def'
name|'fake_func'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|'('
name|'action'
op|'='
string|'"foo"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
name|'fake_func'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
