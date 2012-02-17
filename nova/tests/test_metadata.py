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
string|'"""Tests for the testing the metadata code."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
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
name|'handler'
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
op|'('
op|'{'
string|"'id'"
op|':'
number|'1'
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
name|'None'
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
string|"''"
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
string|"'hostname'"
op|':'
string|"'test'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_get_floating_ips_by_fixed_address
name|'def'
name|'fake_get_floating_ips_by_fixed_address'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'fixed_ip'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
string|"'1.2.3.4'"
op|','
string|"'5.6.7.8'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
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
name|'return'
name|'self'
op|'.'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|instance_get_list
dedent|''
name|'def'
name|'instance_get_list'
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
name|'return'
op|'['
name|'self'
op|'.'
name|'instance'
op|']'
newline|'\n'
nl|'\n'
DECL|function|get_fixed_ip_by_address
dedent|''
name|'def'
name|'get_fixed_ip_by_address'
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
name|'return'
op|'{'
string|"'instance_id'"
op|':'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'id'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'fake_network'
op|'.'
name|'stub_out_nw_api_get_instance_nw_info'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
nl|'\n'
name|'spectacular'
op|'='
name|'True'
op|')'
newline|'\n'
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
string|"'get_floating_ips_by_fixed_address'"
op|','
nl|'\n'
name|'fake_get_floating_ips_by_fixed_address'
op|')'
newline|'\n'
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
name|'get_fixed_ip_by_address'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'instance_get'"
op|','
name|'instance_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'instance_get_all_by_filters'"
op|','
name|'instance_get_list'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'handler'
op|'.'
name|'MetadataRequestHandler'
op|'('
op|')'
newline|'\n'
name|'network_manager'
op|'='
name|'fake_network'
op|'.'
name|'FakeNetworkManager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'self'
op|'.'
name|'app'
op|'.'
name|'compute_api'
op|'.'
name|'network_api'
op|','
nl|'\n'
string|"'get_instance_uuids_by_ip_filter'"
op|','
nl|'\n'
name|'network_manager'
op|'.'
name|'get_instance_uuids_by_ip_filter'
op|')'
newline|'\n'
nl|'\n'
DECL|member|request
dedent|''
name|'def'
name|'request'
op|'('
name|'self'
op|','
name|'relative_url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'relative_url'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
string|'"127.0.0.1"'
newline|'\n'
name|'return'
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|test_base
dedent|''
name|'def'
name|'test_base'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'request'
op|'('
string|"'/'"
op|')'
op|','
string|"'meta-data/\\nuser-data'"
op|')'
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
name|'self'
op|'.'
name|'instance'
op|'['
string|"'user_data'"
op|']'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|"'happy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'request'
op|'('
string|"'/user-data'"
op|')'
op|','
string|"'happy'"
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
DECL|function|sg_get
indent|'        '
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
indent|'            '
name|'return'
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
dedent|''
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'request'
op|'('
string|"'/meta-data/security-groups'"
op|')'
op|','
nl|'\n'
string|"'default\\nother'"
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
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/user-data'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
string|'"127.1.1.1"'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_user_data_none_fixed_address
dedent|''
name|'def'
name|'test_user_data_none_fixed_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/user-data'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
name|'None'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_user_data_invalid_url
dedent|''
name|'def'
name|'test_user_data_invalid_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/user-data-invalid'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
string|'"127.0.0.1"'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
name|'self'
op|'.'
name|'instance'
op|'['
string|"'user_data'"
op|']'
op|'='
name|'ENCODE_USER_DATA_STRING'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_forwarded_for'
op|'='
name|'True'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/user-data'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'remote_addr'
op|'='
string|'"127.0.0.1"'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
name|'USER_DATA_STRING'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'request'
op|'('
string|"'/meta-data/local-hostname'"
op|')'
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
DECL|member|test_get_instance_mapping
dedent|''
name|'def'
name|'test_get_instance_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure that _get_instance_mapping works"""'
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
name|'id'
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
name|'self'
op|'.'
name|'app'
op|'.'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_ref0'
op|')'
op|','
nl|'\n'
name|'handler'
op|'.'
name|'_DEFAULT_MAPPINGS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'app'
op|'.'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_ref1'
op|')'
op|','
nl|'\n'
name|'expected'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
