begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'logging'
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
name|'quota'
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
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaTestCase
name|'class'
name|'QuotaTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
name|'super'
op|'('
name|'QuotaTestCase'
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
name|'flags'
op|'('
name|'connection_type'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'quota_instances'
op|'='
number|'2'
op|','
nl|'\n'
name|'quota_cores'
op|'='
number|'4'
op|','
nl|'\n'
name|'quota_volumes'
op|'='
number|'2'
op|','
nl|'\n'
name|'quota_gigabytes'
op|'='
number|'20'
op|','
nl|'\n'
name|'quota_floating_ips'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'admin'"
op|','
string|"'admin'"
op|','
string|"'admin'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'network'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'network_manager'
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
name|'project'
op|'='
name|'self'
op|'.'
name|'project'
op|','
nl|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_project'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_user'
op|'('
name|'self'
op|'.'
name|'user'
op|')'
newline|'\n'
name|'super'
op|'('
name|'QuotaTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instance
dedent|''
name|'def'
name|'_create_instance'
op|'('
name|'self'
op|','
name|'cores'
op|'='
number|'2'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test instance"""'
newline|'\n'
name|'inst'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'inst'
op|'['
string|"'image_id'"
op|']'
op|'='
string|"'ami-test'"
newline|'\n'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|'='
string|"'r-fakeres'"
newline|'\n'
name|'inst'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'inst'
op|'['
string|"'instance_type'"
op|']'
op|'='
string|"'m1.large'"
newline|'\n'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|'='
name|'cores'
newline|'\n'
name|'inst'
op|'['
string|"'mac_address'"
op|']'
op|'='
name|'utils'
op|'.'
name|'generate_mac'
op|'('
op|')'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'inst'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|','
name|'size'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a test volume"""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'id'
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_quota_overrides
dedent|''
name|'def'
name|'test_quota_overrides'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure overriding a projects quotas works"""'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
op|'{'
string|"'project_id'"
op|':'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|'}'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'4'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|','
op|'{'
string|"'cores'"
op|':'
number|'100'
op|'}'
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'quota'
op|'.'
name|'allowed_instances'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'100'
op|','
string|"'m1.small'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'num_instances'
op|','
number|'10'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'quota_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_instances
dedent|''
name|'def'
name|'test_too_many_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cloud'
op|'.'
name|'QuotaError'
op|','
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.small'"
op|')'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_cores
dedent|''
dedent|''
name|'def'
name|'test_too_many_cores'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'_create_instance'
op|'('
name|'cores'
op|'='
number|'4'
op|')'
newline|'\n'
name|'instance_ids'
op|'.'
name|'append'
op|'('
name|'instance_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cloud'
op|'.'
name|'QuotaError'
op|','
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'run_instances'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'instance_type'
op|'='
string|"'m1.small'"
op|')'
newline|'\n'
name|'for'
name|'instance_id'
name|'in'
name|'instance_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'instance_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_volumes
dedent|''
dedent|''
name|'def'
name|'test_too_many_volumes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_volumes'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cloud'
op|'.'
name|'QuotaError'
op|','
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'create_volume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'size'
op|'='
number|'10'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_gigabytes
dedent|''
dedent|''
name|'def'
name|'test_too_many_gigabytes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'volume_id'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
name|'size'
op|'='
number|'20'
op|')'
newline|'\n'
name|'volume_ids'
op|'.'
name|'append'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cloud'
op|'.'
name|'QuotaError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'create_volume'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'size'
op|'='
number|'10'
op|')'
newline|'\n'
name|'for'
name|'volume_id'
name|'in'
name|'volume_ids'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_addresses
dedent|''
dedent|''
name|'def'
name|'test_too_many_addresses'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address'
op|'='
string|"'192.168.0.100'"
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
op|'{'
string|"'address'"
op|':'
name|'address'
op|','
string|"'host'"
op|':'
name|'FLAGS'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
name|'float_addr'
op|'='
name|'self'
op|'.'
name|'network'
op|'.'
name|'allocate_floating_ip'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'self'
op|'.'
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
comment|'# NOTE(vish): This assert never fails. When cloud attempts to'
nl|'\n'
comment|'#             make an rpc.call, the test just finishes with OK. It'
nl|'\n'
comment|'#             appears to be something in the magic inline callbacks'
nl|'\n'
comment|'#             that is breaking.'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'cloud'
op|'.'
name|'QuotaError'
op|','
name|'self'
op|'.'
name|'cloud'
op|'.'
name|'allocate_address'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'floating_ip_destroy'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
