begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'quota_classes'
name|'as'
name|'quota_classes_v21'
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
nl|'\n'
nl|'\n'
DECL|function|quota_set
name|'def'
name|'quota_set'
op|'('
name|'class_name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'class_name'
op|','
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'-'
number|'1'
op|','
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'security_group_rules'"
op|':'
number|'20'
op|','
string|"'key_pairs'"
op|':'
number|'100'
op|','
nl|'\n'
string|"'injected_file_path_bytes'"
op|':'
number|'255'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClassSetsTestV21
dedent|''
name|'class'
name|'QuotaClassSetsTestV21'
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
name|'super'
op|'('
name|'QuotaClassSetsTestV21'
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
name|'self'
op|'.'
name|'_setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup
dedent|''
name|'def'
name|'_setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'quota_classes_v21'
op|'.'
name|'QuotaClassSetsController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_quota_set
dedent|''
name|'def'
name|'test_format_quota_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw_quota_set'
op|'='
op|'{'
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_path_bytes'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'security_group_rules'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'key_pairs'"
op|':'
number|'100'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'quota_set'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_format_quota_set'
op|'('
string|"'test_class'"
op|','
nl|'\n'
name|'raw_quota_set'
op|')'
newline|'\n'
name|'qs'
op|'='
name|'quota_set'
op|'['
string|"'quota_class_set'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'id'"
op|']'
op|','
string|"'test_class'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'instances'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'cores'"
op|']'
op|','
number|'20'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'ram'"
op|']'
op|','
number|'51200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'floating_ips'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'fixed_ips'"
op|']'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'metadata_items'"
op|']'
op|','
number|'128'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'injected_files'"
op|']'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'injected_file_path_bytes'"
op|']'
op|','
number|'255'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'injected_file_content_bytes'"
op|']'
op|','
number|'10240'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'security_groups'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'security_group_rules'"
op|']'
op|','
number|'20'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'key_pairs'"
op|']'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_show
dedent|''
name|'def'
name|'test_quotas_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'quota_set'
op|'('
string|"'test_class'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update
dedent|''
name|'def'
name|'test_quotas_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50'
op|','
string|"'cores'"
op|':'
number|'50'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'-'
number|'1'
op|','
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|','
nl|'\n'
string|"'injected_file_path_bytes'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'security_group_rules'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'key_pairs'"
op|':'
number|'100'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_empty_body
dedent|''
name|'def'
name|'test_quotas_update_with_empty_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_invalid_integer
dedent|''
name|'def'
name|'test_quotas_update_with_invalid_integer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'2'
op|'**'
number|'31'
op|'+'
number|'1'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_long_quota_class_name
dedent|''
name|'def'
name|'test_quotas_update_with_long_quota_class_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
string|"'a'"
op|'*'
number|'256'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'10'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'name'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_non_integer
dedent|''
name|'def'
name|'test_quotas_update_with_non_integer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
string|'"abc"'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50.5'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
nl|'\n'
string|"'instances'"
op|':'
string|"u'\\u30aa\\u30fc\\u30d7\\u30f3'"
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_unsupported_quota_class
dedent|''
name|'def'
name|'test_quotas_update_with_unsupported_quota_class'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50'
op|','
string|"'cores'"
op|':'
number|'50'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'unsupported'"
op|':'
number|'12'
op|'}'
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
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaClassesPolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'QuotaClassesPolicyEnforcementV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'QuotaClassesPolicyEnforcementV21'
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
name|'quota_classes_v21'
op|'.'
name|'QuotaClassSetsController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
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
DECL|member|test_show_policy_failed
dedent|''
name|'def'
name|'test_show_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-quota-class-sets:show"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"quota_class:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_policy_failed
dedent|''
name|'def'
name|'test_update_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-quota-class-sets:update"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"quota_class:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'quota_class_set'"
op|':'
op|'{'
op|'}'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
