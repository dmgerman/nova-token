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
name|'httplib'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
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
name|'from'
name|'tornado'
name|'import'
name|'httpserver'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
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
op|'.'
name|'auth'
name|'import'
name|'users'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
name|'import'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'endpoint'
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
comment|'# NOTE(termie): These are a bunch of helper methods and classes to short'
nl|'\n'
comment|'#               circuit boto calls and feed them into our tornado handlers,'
nl|'\n'
comment|"#               it's pretty damn circuitous so apologies if you have to fix"
nl|'\n'
comment|'#               a bug in it'
nl|'\n'
DECL|function|boto_to_tornado
name|'def'
name|'boto_to_tornado'
op|'('
name|'method'
op|','
name|'path'
op|','
name|'headers'
op|','
name|'data'
op|','
name|'host'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" translate boto requests into tornado requests\n\n    connection should be a FakeTornadoHttpConnection instance\n    """'
newline|'\n'
name|'headers'
op|'='
name|'httpserver'
op|'.'
name|'HTTPHeaders'
op|'('
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'httpserver'
op|'.'
name|'HTTPRequest'
op|'('
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'uri'
op|'='
name|'path'
op|','
nl|'\n'
name|'headers'
op|'='
name|'headers'
op|','
nl|'\n'
name|'body'
op|'='
name|'data'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'remote_ip'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
name|'return'
name|'req'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|raw_to_httpresponse
dedent|''
name|'def'
name|'raw_to_httpresponse'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" translate a raw tornado http response into an httplib.HTTPResponse """'
newline|'\n'
name|'sock'
op|'='
name|'FakeHttplibSocket'
op|'('
name|'s'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'httplib'
op|'.'
name|'HTTPResponse'
op|'('
name|'sock'
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'begin'
op|'('
op|')'
newline|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHttplibSocket
dedent|''
name|'class'
name|'FakeHttplibSocket'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" a fake socket implementation for httplib.HTTPResponse, trivial """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fp'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
name|'s'
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
name|'mode'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'fp'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeTornadoStream
dedent|''
dedent|''
name|'class'
name|'FakeTornadoStream'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" a fake stream to satisfy tornado\'s assumptions, trivial """'
newline|'\n'
DECL|member|set_close_callback
name|'def'
name|'set_close_callback'
op|'('
name|'self'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeTornadoConnection
dedent|''
dedent|''
name|'class'
name|'FakeTornadoConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" a fake connection object for tornado to pass to its handlers\n\n    web requests are expected to write to this as they get data and call\n    finish when they are done with the request, we buffer the writes and\n    kick off a callback when it is done so that we can feed the result back\n    into boto.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'d'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'d'
op|'='
name|'d'
newline|'\n'
name|'self'
op|'.'
name|'_buffer'
op|'='
name|'StringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'chunk'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_buffer'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
DECL|member|finish
dedent|''
name|'def'
name|'finish'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'self'
op|'.'
name|'_buffer'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'d'
op|'.'
name|'callback'
op|'('
name|'s'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|xheaders
dedent|''
name|'xheaders'
op|'='
name|'None'
newline|'\n'
nl|'\n'
op|'@'
name|'property'
newline|'\n'
DECL|member|stream
name|'def'
name|'stream'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeTornadoStream'
op|'('
op|')'
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
string|'""" a fake httplib.HTTPConnection for boto to use\n\n    requests made via this connection actually get translated and routed into\n    our tornado app, we then wait for the response and turn it back into\n    the httplib.HTTPResponse that boto expects.\n    """'
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
name|'self'
op|'.'
name|'deferred'
op|'='
name|'defer'
op|'.'
name|'Deferred'
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
name|'boto_to_tornado'
newline|'\n'
name|'conn'
op|'='
name|'FakeTornadoConnection'
op|'('
name|'self'
op|'.'
name|'deferred'
op|')'
newline|'\n'
name|'request'
op|'='
name|'boto_to_tornado'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
nl|'\n'
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'path'
op|'='
name|'path'
op|','
nl|'\n'
name|'headers'
op|'='
name|'headers'
op|','
nl|'\n'
name|'data'
op|'='
name|'data'
op|','
nl|'\n'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'handler'
op|'='
name|'self'
op|'.'
name|'app'
op|'('
name|'request'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deferred'
op|'.'
name|'addCallback'
op|'('
name|'raw_to_httpresponse'
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
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|function|_waiter
name|'def'
name|'_waiter'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'yield'
name|'self'
op|'.'
name|'deferred'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'='
name|'_waiter'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(termie): defer.returnValue above should ensure that'
nl|'\n'
comment|'#               this deferred has already been called by the time'
nl|'\n'
comment|'#               we get here, we are going to cheat and return'
nl|'\n'
comment|'#               the result of the callback'
nl|'\n'
name|'return'
name|'d'
op|'.'
name|'result'
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
name|'pass'
newline|'\n'
nl|'\n'
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
name|'users'
op|'='
name|'users'
op|'.'
name|'UserManager'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
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
name|'APIServerApplication'
op|'('
op|'{'
string|"'Cloud'"
op|':'
name|'self'
op|'.'
name|'cloud'
op|'}'
op|')'
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
name|'FLAGS'
op|'.'
name|'cc_port'
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
name|'http'
op|'='
name|'FakeHttplibConnection'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'app'
op|','
string|"'%s:%d'"
op|'%'
op|'('
name|'self'
op|'.'
name|'host'
op|','
name|'FLAGS'
op|'.'
name|'cc_port'
op|')'
op|','
name|'False'
op|')'
newline|'\n'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'users'
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
dedent|''
name|'except'
name|'Exception'
op|','
name|'_err'
op|':'
newline|'\n'
indent|'            '
name|'pass'
comment|'# User may already exist'
newline|'\n'
dedent|''
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
name|'users'
op|'.'
name|'delete_user'
op|'('
string|"'fake'"
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'users'
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
dedent|''
name|'except'
name|'Exception'
op|','
name|'_err'
op|':'
newline|'\n'
indent|'            '
name|'pass'
comment|'# User may already exist'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'users'
op|'.'
name|'generate_key_pair'
op|'('
string|"'fake'"
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
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'k'
op|':'
name|'k'
op|'.'
name|'name'
op|'=='
name|'keyname'
op|','
name|'rv'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'users'
op|'.'
name|'delete_user'
op|'('
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
