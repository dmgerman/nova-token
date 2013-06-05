begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'plugins'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'plugins'
op|'.'
name|'v3'
name|'import'
name|'extension_info'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'policy'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|fake_extension
name|'class'
name|'fake_extension'
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
name|'name'
op|','
name|'alias'
op|','
name|'description'
op|','
name|'namespace'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'alias'
op|'='
name|'alias'
newline|'\n'
name|'self'
op|'.'
name|'__doc__'
op|'='
name|'description'
newline|'\n'
name|'self'
op|'.'
name|'namespace'
op|'='
name|'namespace'
newline|'\n'
name|'self'
op|'.'
name|'version'
op|'='
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|fake_extensions
dedent|''
dedent|''
name|'fake_extensions'
op|'='
op|'{'
nl|'\n'
string|"'ext1-alias'"
op|':'
name|'fake_extension'
op|'('
string|"'ext1'"
op|','
string|"'ext1-alias'"
op|','
string|"'ext1 description'"
op|','
nl|'\n'
string|"'ext1 namespace'"
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'ext2-alias'"
op|':'
name|'fake_extension'
op|'('
string|"'ext2'"
op|','
string|"'ext2-alias'"
op|','
string|"'ext2 description'"
op|','
nl|'\n'
string|"'ext2 namespace'"
op|','
number|'2'
op|')'
op|','
nl|'\n'
string|"'ext3-alias'"
op|':'
name|'fake_extension'
op|'('
string|"'ext3'"
op|','
string|"'ext3-alias'"
op|','
string|"'ext3 description'"
op|','
nl|'\n'
string|"'ext3 namespace'"
op|','
number|'1'
op|')'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_policy_enforce
name|'def'
name|'fake_policy_enforce'
op|'('
name|'context'
op|','
name|'action'
op|','
name|'target'
op|','
name|'do_raise'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|function|fake_policy_enforce_selective
dedent|''
name|'def'
name|'fake_policy_enforce_selective'
op|'('
name|'context'
op|','
name|'action'
op|','
name|'target'
op|','
name|'do_raise'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'action'
op|'=='
string|"'compute_extension:v3:ext1-alias:discoverable'"
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotAuthorized'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionInfoTest
dedent|''
dedent|''
name|'class'
name|'ExtensionInfoTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'ExtensionInfoTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'ext_info'
op|'.'
name|'extensions'
op|'='
name|'fake_extensions'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'extension_info'
op|'.'
name|'ExtensionInfoController'
op|'('
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extension_info_list
dedent|''
name|'def'
name|'test_extension_info_list'
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
name|'policy'
op|','
string|"'enforce'"
op|','
name|'fake_policy_enforce'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/extensions'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'extensions'"
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'e'
name|'in'
name|'res_dict'
op|'['
string|"'extensions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'e'
op|'['
string|"'alias'"
op|']'
op|','
name|'fake_extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'name'"
op|']'
op|','
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'alias'"
op|']'
op|','
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'__doc__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'namespace'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'namespace'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'version'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extension_info_show
dedent|''
dedent|''
name|'def'
name|'test_extension_info_show'
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
name|'policy'
op|','
string|"'enforce'"
op|','
name|'fake_policy_enforce'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/extensions/ext1-alias'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'ext1-alias'"
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
name|'res_dict'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
string|"'ext1-alias'"
op|']'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'alias'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
string|"'ext1-alias'"
op|']'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
string|"'ext1-alias'"
op|']'
op|'.'
name|'__doc__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'namespace'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
string|"'ext1-alias'"
op|']'
op|'.'
name|'namespace'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'version'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
string|"'ext1-alias'"
op|']'
op|'.'
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extension_info_list_not_all_discoverable
dedent|''
name|'def'
name|'test_extension_info_list_not_all_discoverable'
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
name|'policy'
op|','
string|"'enforce'"
op|','
name|'fake_policy_enforce_selective'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/extensions'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'req'
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
name|'res_dict'
op|'['
string|"'extensions'"
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
name|'e'
name|'in'
name|'res_dict'
op|'['
string|"'extensions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
string|"'ext1-alias'"
op|','
name|'e'
op|'['
string|"'alias'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'e'
op|'['
string|"'alias'"
op|']'
op|','
name|'fake_extensions'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'name'"
op|']'
op|','
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'alias'"
op|']'
op|','
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'alias'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'__doc__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'namespace'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'namespace'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'e'
op|'['
string|"'version'"
op|']'
op|','
nl|'\n'
name|'fake_extensions'
op|'['
name|'e'
op|'['
string|"'alias'"
op|']'
op|']'
op|'.'
name|'version'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
