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
string|'"""Unit tests for the API endpoint"""'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
name|'import'
name|'regioninfo'
newline|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'webob'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'api'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'apirequest'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
name|'FLAGS'
op|'.'
name|'FAKE_subdomain'
op|'='
string|"'ec2'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHttplibSocket
name|'class'
name|'FakeHttplibSocket'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""a fake socket implementation for httplib.HTTPResponse, trivial"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'response_string'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_buffer'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
name|'response_string'
op|')'
newline|'\n'
nl|'\n'
DECL|member|makefile
dedent|''
name|'def'
name|'makefile'
op|'('
name|'self'
op|','
name|'_mode'
op|','
name|'_other'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the socket\'s internal buffer"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_buffer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHttplibConnection
dedent|''
dedent|''
name|'class'
name|'FakeHttplibConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A fake httplib.HTTPConnection for boto to use\n\n    requests made via this connection actually get translated and routed into\n    our WSGI app, we then wait for the response and turn it back into\n    the httplib.HTTPResponse that boto expects.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'app'
op|','
name|'host'
op|','
name|'is_secure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'app'
op|'='
name|'app'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'host'
newline|'\n'
nl|'\n'
DECL|member|request
dedent|''
name|'def'
name|'request'
op|'('
name|'self'
op|','
name|'method'
op|','
name|'path'
op|','
name|'data'
op|','
name|'headers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'path'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
name|'method'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'data'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'='
name|'headers'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'text/html'"
newline|'\n'
name|'req'
op|'.'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
comment|'# Call the WSGI app, get the HTTP response'
nl|'\n'
name|'resp'
op|'='
name|'str'
op|'('
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
op|')'
newline|'\n'
comment|'# For some reason, the response doesn\'t have "HTTP/1.0 " prepended; I'
nl|'\n'
comment|"# guess that's a function the web server usually provides."
nl|'\n'
name|'resp'
op|'='
string|'"HTTP/1.0 %s"'
op|'%'
name|'resp'
newline|'\n'
name|'sock'
op|'='
name|'FakeHttplibSocket'
op|'('
name|'resp'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'http_response'
op|'='
name|'httplib'
op|'.'
name|'HTTPResponse'
op|'('
name|'sock'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'http_response'
op|'.'
name|'begin'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|getresponse
dedent|''
name|'def'
name|'getresponse'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'http_response'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Required for compatibility with boto/tornado"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XmlConversionTestCase
dedent|''
dedent|''
name|'class'
name|'XmlConversionTestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit test api xml conversion"""'
newline|'\n'
DECL|member|test_number_conversion
name|'def'
name|'test_number_conversion'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conv'
op|'='
name|'apirequest'
op|'.'
name|'_try_convert'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'None'"
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'True'"
op|')'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'False'"
op|')'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'0'"
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'42'"
op|')'
op|','
number|'42'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'3.14'"
op|')'
op|','
number|'3.14'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'-57.12'"
op|')'
op|','
op|'-'
number|'57.12'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'0x57'"
op|')'
op|','
number|'0x57'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'-0x57'"
op|')'
op|','
op|'-'
number|'0x57'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'-'"
op|')'
op|','
string|"'-'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'conv'
op|'('
string|"'-0'"
op|')'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ApiEc2TestCase
dedent|''
dedent|''
name|'class'
name|'ApiEc2TestCase'
op|'('
name|'test'
op|'.'
name|'BaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit test for the cloud controller on an EC2 API"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=C0103,C0111'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ApiEc2TestCase'
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
name|'manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'host'
op|'='
string|"'127.0.0.1'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'api'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|expect_http
dedent|''
name|'def'
name|'expect_http'
op|'('
name|'self'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'is_secure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a new EC2 connection"""'
newline|'\n'
name|'self'
op|'.'
name|'ec2'
op|'='
name|'boto'
op|'.'
name|'connect_ec2'
op|'('
nl|'\n'
name|'aws_access_key_id'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'region'
op|'='
name|'regioninfo'
op|'.'
name|'RegionInfo'
op|'('
name|'None'
op|','
string|"'test'"
op|','
name|'self'
op|'.'
name|'host'
op|')'
op|','
nl|'\n'
name|'port'
op|'='
number|'8773'
op|','
nl|'\n'
name|'path'
op|'='
string|"'/services/Cloud'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ec2'
op|','
string|"'new_http_connection'"
op|')'
newline|'\n'
name|'http'
op|'='
name|'FakeHttplibConnection'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'app'
op|','
string|"'%s:8773'"
op|'%'
op|'('
name|'self'
op|'.'
name|'host'
op|')'
op|','
name|'False'
op|')'
newline|'\n'
comment|'# pylint: disable-msg=E1103'
nl|'\n'
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'new_http_connection'
op|'('
name|'host'
op|','
name|'is_secure'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'http'
op|')'
newline|'\n'
name|'return'
name|'http'
newline|'\n'
nl|'\n'
DECL|member|test_describe_instances
dedent|''
name|'def'
name|'test_describe_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that, after creating a user and a project, the describe\n        instances call to the API works properly"""'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_instances'
op|'('
op|')'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_get_all_key_pairs
dedent|''
name|'def'
name|'test_get_all_key_pairs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that, after creating a user and project and generating\n         a key pair, that the API call to list key pairs works properly"""'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'keyname'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
comment|'# NOTE(vish): create depends on pool, so call helper directly'
nl|'\n'
name|'cloud'
op|'.'
name|'_gen_key'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'user'
op|'.'
name|'id'
op|','
name|'keyname'
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_key_pairs'
op|'('
op|')'
newline|'\n'
name|'results'
op|'='
op|'['
name|'k'
name|'for'
name|'k'
name|'in'
name|'rv'
name|'if'
name|'k'
op|'.'
name|'name'
op|'=='
name|'keyname'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'results'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_all_security_groups
dedent|''
name|'def'
name|'test_get_all_security_groups'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that we can retrieve security groups"""'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'rv'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|'.'
name|'name'
op|','
string|"'default'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_delete_security_group
dedent|''
name|'def'
name|'test_create_delete_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that we can create a security group"""'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
comment|'# At the moment, you need both of these to actually be netadmin'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
name|'project'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
nl|'\n'
name|'security_group_name'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'create_security_group'
op|'('
name|'security_group_name'
op|','
string|"'test group'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'rv'
op|')'
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'security_group_name'
name|'in'
op|'['
name|'group'
op|'.'
name|'name'
name|'for'
name|'group'
name|'in'
name|'rv'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'delete_security_group'
op|'('
name|'security_group_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_revoke_security_group_cidr
dedent|''
name|'def'
name|'test_authorize_revoke_security_group_cidr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Test that we can add and remove CIDR based rules\n        to a security group\n        """'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
comment|'# At the moment, you need both of these to actually be netadmin'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
name|'project'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
nl|'\n'
name|'security_group_name'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'create_security_group'
op|'('
name|'security_group_name'
op|','
string|"'test group'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'ec2'
newline|'\n'
nl|'\n'
name|'group'
op|'.'
name|'authorize'
op|'('
string|"'tcp'"
op|','
number|'80'
op|','
number|'81'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
comment|"# I don't bother checkng that we actually find it here,"
nl|'\n'
comment|'# because the create/delete unit test further up should'
nl|'\n'
comment|'# be good enough for that.'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'rv'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'group'
op|'.'
name|'name'
op|'=='
name|'security_group_name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'group'
op|'.'
name|'rules'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'int'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'from_port'
op|')'
op|','
number|'80'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'int'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'to_port'
op|')'
op|','
number|'81'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'grants'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'grants'
op|'['
number|'0'
op|']'
op|')'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'ec2'
newline|'\n'
nl|'\n'
name|'group'
op|'.'
name|'revoke'
op|'('
string|"'tcp'"
op|','
number|'80'
op|','
number|'81'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'delete_security_group'
op|'('
name|'security_group_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'ec2'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rv'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
number|'0'
op|']'
op|'.'
name|'name'
op|','
string|"'default'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|test_authorize_revoke_security_group_foreign_group
dedent|''
name|'def'
name|'test_authorize_revoke_security_group_foreign_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Test that we can grant and revoke another security group access\n        to a security group\n        """'
newline|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'user'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_user'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'project'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'create_project'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
comment|'# At the moment, you need both of these to actually be netadmin'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
name|'project'
op|'.'
name|'add_role'
op|'('
string|"'fake'"
op|','
string|"'netadmin'"
op|')'
newline|'\n'
nl|'\n'
name|'security_group_name'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
name|'other_security_group_name'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
string|'"sdiuisudfsdcnpaqwertasd"'
op|')'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'4'
op|','
number|'8'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'group'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'create_security_group'
op|'('
name|'security_group_name'
op|','
string|"'test group'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'other_group'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'create_security_group'
op|'('
name|'other_security_group_name'
op|','
nl|'\n'
string|"'some other group'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'ec2'
newline|'\n'
nl|'\n'
name|'group'
op|'.'
name|'authorize'
op|'('
name|'src_group'
op|'='
name|'other_group'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# I don't bother checkng that we actually find it here,"
nl|'\n'
comment|'# because the create/delete unit test further up should'
nl|'\n'
comment|'# be good enough for that.'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'rv'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'group'
op|'.'
name|'name'
op|'=='
name|'security_group_name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'group'
op|'.'
name|'rules'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'grants'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'str'
op|'('
name|'group'
op|'.'
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'grants'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
string|"'%s-%s'"
op|'%'
op|'('
name|'other_security_group_name'
op|','
string|"'fake'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'rv'
op|'='
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'get_all_security_groups'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'group'
name|'in'
name|'rv'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'group'
op|'.'
name|'name'
op|'=='
name|'security_group_name'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'connection'
op|'='
name|'self'
op|'.'
name|'ec2'
newline|'\n'
name|'group'
op|'.'
name|'revoke'
op|'('
name|'src_group'
op|'='
name|'other_group'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'expect_http'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ec2'
op|'.'
name|'delete_security_group'
op|'('
name|'security_group_name'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'delete_user'
op|'('
name|'user'
op|')'
newline|'\n'
nl|'\n'
name|'return'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
