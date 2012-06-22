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
string|'"""Tests for metadata service."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'from'
name|'copy'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
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
name|'metadata'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'handler'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
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
name|'network'
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
name|'fake_network'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|USER_DATA_STRING
name|'USER_DATA_STRING'
op|'='
op|'('
string|'"This is an encoded string"'
op|')'
newline|'\n'
DECL|variable|ENCODE_USER_DATA_STRING
name|'ENCODE_USER_DATA_STRING'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'USER_DATA_STRING'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|INSTANCES
name|'INSTANCES'
op|'='
op|'('
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'b65cee2f-8c69-4aeb-be2f-f79742548fc2'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'key_name'"
op|':'
string|'"mykey"'
op|','
nl|'\n'
string|"'key_data'"
op|':'
string|'"ssh-rsa AAAAB3Nzai....N3NtHw== someuser@somehost"'
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'test'"
op|','
nl|'\n'
string|"'launch_index'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'m1.tiny'"
op|'}'
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
string|"'r-xxxxxxxx'"
op|','
nl|'\n'
string|"'user_data'"
op|':'
name|'ENCODE_USER_DATA_STRING'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
number|'7'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'fixed_ips'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'info_cache'"
op|':'
op|'{'
string|"'network_info'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\n'
string|"'hostname'"
op|':'
string|"'test'"
op|'}'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_non_existing_address
name|'def'
name|'return_non_existing_address'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_InstanceMetadata
dedent|''
name|'def'
name|'fake_InstanceMetadata'
op|'('
name|'stubs'
op|','
name|'inst_data'
op|','
name|'address'
op|'='
name|'None'
op|','
name|'sgroups'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'if'
name|'sgroups'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'sgroups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'default'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
DECL|function|sg_get
dedent|''
name|'def'
name|'sg_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'sgroups'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'security_group_get_by_instance'"
op|','
name|'sg_get'
op|')'
newline|'\n'
name|'return'
name|'base'
op|'.'
name|'InstanceMetadata'
op|'('
name|'inst_data'
op|','
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_request
dedent|''
name|'def'
name|'fake_request'
op|'('
name|'stubs'
op|','
name|'mdinst'
op|','
name|'relpath'
op|','
name|'address'
op|'='
string|'"127.0.0.1"'
op|','
nl|'\n'
name|'fake_get_metadata'
op|'='
name|'None'
op|','
name|'headers'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|get_metadata
indent|'    '
name|'def'
name|'get_metadata'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'mdinst'
newline|'\n'
nl|'\n'
dedent|''
name|'app'
op|'='
name|'handler'
op|'.'
name|'MetadataRequestHandler'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'fake_get_metadata'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'fake_get_metadata'
op|'='
name|'get_metadata'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'stubs'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'app'
op|','
string|"'get_metadata'"
op|','
name|'fake_get_metadata'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'relpath'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
name|'address'
newline|'\n'
nl|'\n'
name|'if'
name|'headers'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'headers'
op|'.'
name|'update'
op|'('
name|'headers'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataTestCase
dedent|''
name|'class'
name|'MetadataTestCase'
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
name|'MetadataTestCase'
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
name|'instance'
op|'='
name|'INSTANCES'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_user_data
dedent|''
name|'def'
name|'test_user_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'inst'
op|'['
string|"'user_data'"
op|']'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|'"happy"'
op|')'
newline|'\n'
name|'md'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'inst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|'='
string|"'2009-04-04'"
op|')'
op|'['
string|"'user-data'"
op|']'
op|','
string|'"happy"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_user_data
dedent|''
name|'def'
name|'test_no_user_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'del'
name|'inst'
op|'['
string|"'user_data'"
op|']'
newline|'\n'
name|'md'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'inst'
op|')'
newline|'\n'
name|'obj'
op|'='
name|'object'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|'='
string|"'2009-04-04'"
op|')'
op|'.'
name|'get'
op|'('
string|"'user-data'"
op|','
name|'obj'
op|')'
op|','
nl|'\n'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_security_groups
dedent|''
name|'def'
name|'test_security_groups'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'='
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
newline|'\n'
name|'sgroups'
op|'='
op|'['
op|'{'
string|"'name'"
op|':'
string|"'default'"
op|'}'
op|','
op|'{'
string|"'name'"
op|':'
string|"'other'"
op|'}'
op|']'
newline|'\n'
name|'expected'
op|'='
op|'['
string|"'default'"
op|','
string|"'other'"
op|']'
newline|'\n'
nl|'\n'
name|'md'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'inst'
op|','
name|'sgroups'
op|'='
name|'sgroups'
op|')'
newline|'\n'
name|'data'
op|'='
name|'md'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|'='
string|"'2009-04-04'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'security-groups'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_local_hostname_fqdn
dedent|''
name|'def'
name|'test_local_hostname_fqdn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'md'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'md'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|'='
string|"'2009-04-04'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'local-hostname'"
op|']'
op|','
nl|'\n'
string|'"%s.%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'instance'
op|'['
string|"'hostname'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'dhcp_domain'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_instance_mapping
dedent|''
name|'def'
name|'test_format_instance_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure that _format_instance_mappings works"""'
newline|'\n'
name|'ctxt'
op|'='
name|'None'
newline|'\n'
name|'instance_ref0'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'e5fe5518-0288-4fa3-b0c4-c79764101b85'"
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'instance_ref1'
op|'='
op|'{'
string|"'id'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'b65cee2f-8c69-4aeb-be2f-f79742548fc2'"
op|','
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda1'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_bdm_get
name|'def'
name|'fake_bdm_get'
op|'('
name|'ctxt'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
op|'{'
string|"'volume_id'"
op|':'
number|'87654321'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdh'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'swap'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'volume_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'no_device'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'delete_on_termination'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|','
nl|'\n'
name|'fake_bdm_get'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'ami'"
op|':'
string|"'sda1'"
op|','
nl|'\n'
string|"'root'"
op|':'
string|"'/dev/sda1'"
op|','
nl|'\n'
string|"'ephemeral0'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'/dev/sdc'"
op|','
nl|'\n'
string|"'ebs0'"
op|':'
string|"'/dev/sdh'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base'
op|'.'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
name|'instance_ref0'
op|')'
op|','
nl|'\n'
name|'base'
op|'.'
name|'_DEFAULT_MAPPINGS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base'
op|'.'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
name|'instance_ref1'
op|')'
op|','
nl|'\n'
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_pubkey
dedent|''
name|'def'
name|'test_pubkey'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'md'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'copy'
op|'('
name|'self'
op|'.'
name|'instance'
op|')'
op|')'
newline|'\n'
name|'data'
op|'='
name|'md'
op|'.'
name|'get_ec2_metadata'
op|'('
name|'version'
op|'='
string|"'2009-04-04'"
op|')'
newline|'\n'
name|'pubkey_ent'
op|'='
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'public-keys'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'pubkey_ent'
op|')'
op|','
nl|'\n'
string|'"0=%s"'
op|'%'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'pubkey_ent'
op|'['
string|"'0'"
op|']'
op|'['
string|"'openssh-key'"
op|']'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'key_data'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataHandlerTestCase
dedent|''
dedent|''
name|'class'
name|'MetadataHandlerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test that metadata is returning proper values."""'
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
name|'MetadataHandlerTestCase'
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
name|'instance'
op|'='
name|'INSTANCES'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'mdinst'
op|'='
name|'fake_InstanceMetadata'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'address'
op|'='
name|'None'
op|','
name|'sgroups'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_root
dedent|''
name|'def'
name|'test_root'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'base'
op|'.'
name|'VERSIONS'
op|')'
op|'+'
string|'"\\nlatest"'
newline|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
string|'"/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'body'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
string|'"/foo/../"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'body'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_version_root
dedent|''
name|'def'
name|'test_version_root'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
string|'"/2009-04-04"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'body'
op|','
string|"'meta-data/\\nuser-data'"
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
string|'"/9999-99-99"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_data_non_existing_fixed_address
dedent|''
name|'def'
name|'test_user_data_non_existing_fixed_address'
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
name|'network'
op|'.'
name|'API'
op|','
string|"'get_fixed_ip_by_address'"
op|','
nl|'\n'
name|'return_non_existing_address'
op|')'
newline|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
string|'"/2009-04-04/user-data"'
op|','
nl|'\n'
string|'"127.1.1.1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fixed_address_none
dedent|''
name|'def'
name|'test_fixed_address_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'fake_request'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
nl|'\n'
name|'relpath'
op|'='
string|'"/2009-04-04/user-data"'
op|','
name|'address'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'500'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_path_is_404
dedent|''
name|'def'
name|'test_invalid_path_is_404'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
nl|'\n'
name|'relpath'
op|'='
string|'"/2009-04-04/user-data-invalid"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_user_data_with_use_forwarded_header
dedent|''
name|'def'
name|'test_user_data_with_use_forwarded_header'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_addr'
op|'='
string|'"192.192.192.2"'
newline|'\n'
nl|'\n'
DECL|function|fake_get_metadata
name|'def'
name|'fake_get_metadata'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'address'
op|'=='
name|'expected_addr'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'mdinst'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|'"Expected addr of %s, got %s"'
op|'%'
nl|'\n'
op|'('
name|'expected_addr'
op|','
name|'address'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_forwarded_for'
op|'='
name|'True'
op|')'
newline|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
nl|'\n'
name|'relpath'
op|'='
string|'"/2009-04-04/user-data"'
op|','
nl|'\n'
name|'address'
op|'='
string|'"168.168.168.1"'
op|','
nl|'\n'
name|'fake_get_metadata'
op|'='
name|'fake_get_metadata'
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'X-Forwarded-For'"
op|':'
name|'expected_addr'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'body'
op|','
nl|'\n'
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'self'
op|'.'
name|'instance'
op|'['
string|"'user_data'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'fake_request'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'mdinst'
op|','
nl|'\n'
name|'relpath'
op|'='
string|'"/2009-04-04/user-data"'
op|','
nl|'\n'
name|'address'
op|'='
string|'"168.168.168.1"'
op|','
nl|'\n'
name|'fake_get_metadata'
op|'='
name|'fake_get_metadata'
op|','
nl|'\n'
name|'headers'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'500'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
