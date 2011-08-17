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
name|'httplib'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'metadatarequesthandler'
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
nl|'\n'
nl|'\n'
DECL|class|MetadataTestCase
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
DECL|function|instance_get
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
DECL|function|floating_get
dedent|''
name|'def'
name|'floating_get'
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
string|"'99.99.99.99'"
newline|'\n'
nl|'\n'
dedent|''
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|','
string|"'instance_get_floating_address'"
op|','
name|'floating_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'metadatarequesthandler'
op|'.'
name|'MetadataRequestHandler'
op|'('
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
dedent|''
dedent|''
endmarker|''
end_unit
