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
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
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
op|'.'
name|'contrib'
name|'import'
name|'quota_classes'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
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
DECL|class|QuotaClassSetsTest
dedent|''
name|'class'
name|'QuotaClassSetsTest'
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
name|'QuotaClassSetsTest'
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
name|'controller'
op|'='
name|'quota_classes'
op|'.'
name|'QuotaClassSetsController'
op|'('
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
DECL|member|test_quotas_show_as_admin
dedent|''
name|'def'
name|'test_quotas_show_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
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
DECL|member|test_quotas_show_as_unauthorized_user
dedent|''
name|'def'
name|'test_quotas_show_as_unauthorized_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
string|"'test_class'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_as_admin
dedent|''
name|'def'
name|'test_quotas_update_as_admin'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|"'test_class'"
op|','
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
DECL|member|test_quotas_update_as_user
dedent|''
name|'def'
name|'test_quotas_update_as_user'
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
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
string|"'test_class'"
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
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
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_with_a_non_integer_value
dedent|''
name|'def'
name|'test_quotas_update_with_a_non_integer_value'
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
string|'"not integer"'
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
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/v2/fake4/os-quota-class-sets/test_class'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
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
name|'req'
op|','
string|"'test_class'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaTemplateXMLSerializerTest
dedent|''
dedent|''
name|'class'
name|'QuotaTemplateXMLSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
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
name|'QuotaTemplateXMLSerializerTest'
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
name|'serializer'
op|'='
name|'quota_classes'
op|'.'
name|'QuotaClassTemplate'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serializer
dedent|''
name|'def'
name|'test_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'quota_class_set'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'test_class'"
op|','
nl|'\n'
name|'metadata_items'
op|'='
number|'10'
op|','
nl|'\n'
name|'injected_file_path_bytes'
op|'='
number|'255'
op|','
nl|'\n'
name|'injected_file_content_bytes'
op|'='
number|'20'
op|','
nl|'\n'
name|'ram'
op|'='
number|'50'
op|','
nl|'\n'
name|'floating_ips'
op|'='
number|'60'
op|','
nl|'\n'
name|'fixed_ips'
op|'='
op|'-'
number|'1'
op|','
nl|'\n'
name|'instances'
op|'='
number|'70'
op|','
nl|'\n'
name|'injected_files'
op|'='
number|'80'
op|','
nl|'\n'
name|'security_groups'
op|'='
number|'10'
op|','
nl|'\n'
name|'security_group_rules'
op|'='
number|'20'
op|','
nl|'\n'
name|'key_pairs'
op|'='
number|'100'
op|','
nl|'\n'
name|'cores'
op|'='
number|'90'
op|')'
op|')'
newline|'\n'
name|'text'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'quota_class_set'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test_class'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'exemplar'
op|'['
string|"'quota_class_set'"
op|']'
op|')'
op|'-'
number|'1'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'child'
op|'.'
name|'tag'
op|','
name|'exemplar'
op|'['
string|"'quota_class_set'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'child'
op|'.'
name|'text'
op|')'
op|','
nl|'\n'
name|'exemplar'
op|'['
string|"'quota_class_set'"
op|']'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserializer
dedent|''
dedent|''
name|'def'
name|'test_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'quota_class_set'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'metadata_items'
op|'='
string|"'10'"
op|','
nl|'\n'
name|'injected_file_content_bytes'
op|'='
string|"'20'"
op|','
nl|'\n'
name|'ram'
op|'='
string|"'50'"
op|','
nl|'\n'
name|'floating_ips'
op|'='
string|"'60'"
op|','
nl|'\n'
name|'fixed_ips'
op|'='
string|"'-1'"
op|','
nl|'\n'
name|'instances'
op|'='
string|"'70'"
op|','
nl|'\n'
name|'injected_files'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'security_groups'
op|'='
string|"'10'"
op|','
nl|'\n'
name|'security_group_rules'
op|'='
string|"'20'"
op|','
nl|'\n'
name|'key_pairs'
op|'='
string|"'100'"
op|','
nl|'\n'
name|'cores'
op|'='
string|"'90'"
op|')'
op|')'
newline|'\n'
name|'intext'
op|'='
op|'('
string|'"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\\n"'
nl|'\n'
string|"'<quota_class_set>'"
nl|'\n'
string|"'<metadata_items>10</metadata_items>'"
nl|'\n'
string|"'<injected_file_content_bytes>20'"
nl|'\n'
string|"'</injected_file_content_bytes>'"
nl|'\n'
string|"'<ram>50</ram>'"
nl|'\n'
string|"'<floating_ips>60</floating_ips>'"
nl|'\n'
string|"'<fixed_ips>-1</fixed_ips>'"
nl|'\n'
string|"'<instances>70</instances>'"
nl|'\n'
string|"'<injected_files>80</injected_files>'"
nl|'\n'
string|"'<cores>90</cores>'"
nl|'\n'
string|"'<security_groups>10</security_groups>'"
nl|'\n'
string|"'<security_group_rules>20</security_group_rules>'"
nl|'\n'
string|"'<key_pairs>100</key_pairs>'"
nl|'\n'
string|"'</quota_class_set>'"
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
op|'['
string|"'body'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'exemplar'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
