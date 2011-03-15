begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nTests dealing with HTTP rate-limiting.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'limits'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'limits'
name|'import'
name|'Limit'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|TEST_LIMITS
name|'TEST_LIMITS'
op|'='
op|'['
nl|'\n'
name|'Limit'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|','
string|'"^/delayed"'
op|','
number|'1'
op|','
name|'limits'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"POST"'
op|','
string|'"*"'
op|','
string|'".*"'
op|','
number|'7'
op|','
name|'limits'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"POST"'
op|','
string|'"/servers"'
op|','
string|'"^/servers"'
op|','
number|'3'
op|','
name|'limits'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"PUT"'
op|','
string|'"*"'
op|','
string|'""'
op|','
number|'10'
op|','
name|'limits'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
name|'Limit'
op|'('
string|'"PUT"'
op|','
string|'"/servers"'
op|','
string|'"^/servers"'
op|','
number|'5'
op|','
name|'limits'
op|'.'
name|'PER_MINUTE'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|class|LimiterTest
name|'class'
name|'LimiterTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for the in-memory `limits.Limiter` class.\n    """'
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
string|'"""Run before each test."""'
newline|'\n'
name|'test'
op|'.'
name|'TestCase'
op|'.'
name|'setUp'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'time'
op|'='
number|'0.0'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'limits'
op|'.'
name|'Limit'
op|','
string|'"_get_time"'
op|','
name|'self'
op|'.'
name|'_get_time'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'limiter'
op|'='
name|'limits'
op|'.'
name|'Limiter'
op|'('
name|'TEST_LIMITS'
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
string|'"""Run after each test."""'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_time
dedent|''
name|'def'
name|'_get_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the "time" according to this test suite."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'time'
newline|'\n'
nl|'\n'
DECL|member|_check
dedent|''
name|'def'
name|'_check'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check and yield results from checks."""'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'num'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'check_for_delay'
op|'('
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_sum
dedent|''
dedent|''
name|'def'
name|'_check_sum'
op|'('
name|'self'
op|','
name|'num'
op|','
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check and sum results from checks."""'
newline|'\n'
name|'results'
op|'='
name|'self'
op|'.'
name|'_check'
op|'('
name|'num'
op|','
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|')'
newline|'\n'
name|'return'
name|'sum'
op|'('
name|'filter'
op|'('
name|'lambda'
name|'x'
op|':'
name|'x'
op|'!='
name|'None'
op|','
name|'results'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_delay_GET
dedent|''
name|'def'
name|'test_no_delay_GET'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Simple test to ensure no delay on a single call for a limit verb we\n        didn"t set.\n        """'
newline|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'check_for_delay'
op|'('
string|'"GET"'
op|','
string|'"/anything"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_delay_PUT
dedent|''
name|'def'
name|'test_no_delay_PUT'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Simple test to ensure no delay on a single call for a known limit.\n        """'
newline|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'limiter'
op|'.'
name|'check_for_delay'
op|'('
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delay_PUT
dedent|''
name|'def'
name|'test_delay_PUT'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure the 11th PUT will result in a delay of 6.0 seconds until\n        the next request will be granced.\n        """'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'10'
op|'+'
op|'['
number|'6.0'
op|']'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'11'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delay_POST
dedent|''
name|'def'
name|'test_delay_POST'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure the 8th POST will result in a delay of 6.0 seconds until\n        the next request will be granced.\n        """'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'7'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'7'
op|','
string|'"POST"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
number|'60.0'
op|'/'
number|'7.0'
newline|'\n'
name|'results'
op|'='
name|'self'
op|'.'
name|'_check_sum'
op|'('
number|'1'
op|','
string|'"POST"'
op|','
string|'"/anything"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failUnlessAlmostEqual'
op|'('
name|'expected'
op|','
name|'results'
op|','
number|'8'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delay_GET
dedent|''
name|'def'
name|'test_delay_GET'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure the 11th GET will result in NO delay.\n        """'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'11'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'11'
op|','
string|'"GET"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delay_PUT_servers
dedent|''
name|'def'
name|'test_delay_PUT_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure PUT on /servers limits at 5 requests, and PUT elsewhere is still\n        OK after 5 requests...but then after 11 total requests, PUT limiting\n        kicks in.\n        """'
newline|'\n'
comment|'# First 6 requests on PUT /servers'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'5'
op|'+'
op|'['
number|'12.0'
op|']'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'6'
op|','
string|'"PUT"'
op|','
string|'"/servers"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
comment|'# Next 5 request on PUT /anything'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'4'
op|'+'
op|'['
number|'6.0'
op|']'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'5'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delay_PUT_wait
dedent|''
name|'def'
name|'test_delay_PUT_wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure after hitting the limit and then waiting for the correct\n        amount of time, the limit will be lifted.\n        """'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'10'
op|'+'
op|'['
number|'6.0'
op|']'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'11'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
comment|'# Advance time'
nl|'\n'
name|'self'
op|'.'
name|'time'
op|'+='
number|'6.0'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|','
number|'6.0'
op|']'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'2'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_delays
dedent|''
name|'def'
name|'test_multiple_delays'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure multiple requests still get a delay.\n        """'
newline|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'10'
op|'+'
op|'['
number|'6.0'
op|']'
op|'*'
number|'10'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'20'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'time'
op|'+='
number|'1.0'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'['
number|'5.0'
op|']'
op|'*'
number|'10'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'10'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_multiple_users
dedent|''
name|'def'
name|'test_multiple_users'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Tests involving multiple users.\n        """'
newline|'\n'
comment|'# User1'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'10'
op|'+'
op|'['
number|'6.0'
op|']'
op|'*'
number|'10'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'20'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|','
string|'"user1"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
comment|'# User2'
nl|'\n'
name|'expected'
op|'='
op|'['
name|'None'
op|']'
op|'*'
number|'10'
op|'+'
op|'['
number|'6.0'
op|']'
op|'*'
number|'5'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'15'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|','
string|'"user2"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'time'
op|'+='
number|'1.0'
newline|'\n'
nl|'\n'
comment|'# User1 again'
nl|'\n'
name|'expected'
op|'='
op|'['
number|'5.0'
op|']'
op|'*'
number|'10'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'10'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|','
string|'"user1"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'time'
op|'+='
number|'1.0'
newline|'\n'
nl|'\n'
comment|'# User1 again'
nl|'\n'
name|'expected'
op|'='
op|'['
number|'4.0'
op|']'
op|'*'
number|'5'
newline|'\n'
name|'results'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'_check'
op|'('
number|'5'
op|','
string|'"PUT"'
op|','
string|'"/anything"'
op|','
string|'"user2"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'results'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WsgiLimiterTest
dedent|''
dedent|''
name|'class'
name|'WsgiLimiterTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for `limits.WsgiLimiter` class.\n    """'
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
string|'"""Run before each test."""'
newline|'\n'
name|'test'
op|'.'
name|'TestCase'
op|'.'
name|'setUp'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'time'
op|'='
number|'0.0'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'limits'
op|'.'
name|'WsgiLimiter'
op|'('
name|'TEST_LIMITS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'.'
name|'_limiter'
op|'.'
name|'_get_time'
op|'='
name|'self'
op|'.'
name|'_get_time'
newline|'\n'
nl|'\n'
DECL|member|_get_time
dedent|''
name|'def'
name|'_get_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the "time" according to this test suite."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'time'
newline|'\n'
nl|'\n'
DECL|member|_request_data
dedent|''
name|'def'
name|'_request_data'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get data decribing a limit request verb/path."""'
newline|'\n'
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|'"verb"'
op|':'
name|'verb'
op|','
string|'"path"'
op|':'
name|'path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_request
dedent|''
name|'def'
name|'_request'
op|'('
name|'self'
op|','
name|'verb'
op|','
name|'url'
op|','
name|'username'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure that POSTing to the given url causes the given username\n        to perform the given action.  Make the internal rate limiter return\n        delay and make sure that the WSGI app returns the correct response.\n        """'
newline|'\n'
name|'if'
name|'username'
op|':'
newline|'\n'
indent|'            '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/%s"'
op|'%'
name|'username'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'request'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'self'
op|'.'
name|'_request_data'
op|'('
name|'verb'
op|','
name|'url'
op|')'
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
nl|'\n'
name|'if'
string|'"X-Wait-Seconds"'
name|'in'
name|'response'
op|'.'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
name|'return'
name|'response'
op|'.'
name|'headers'
op|'['
string|'"X-Wait-Seconds"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_int'
op|','
number|'204'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_methods
dedent|''
name|'def'
name|'test_invalid_methods'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Only POSTs should work."""'
newline|'\n'
name|'requests'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'method'
name|'in'
op|'['
string|'"GET"'
op|','
string|'"PUT"'
op|','
string|'"DELETE"'
op|','
string|'"HEAD"'
op|','
string|'"OPTIONS"'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/"'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'self'
op|'.'
name|'_request_data'
op|'('
string|'"GET"'
op|','
string|'"/something"'
op|')'
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
number|'405'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_good_url
dedent|''
dedent|''
name|'def'
name|'test_good_url'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/something"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_escaping
dedent|''
name|'def'
name|'test_escaping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/something/jump%20up"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_response_to_delays
dedent|''
name|'def'
name|'test_response_to_delays'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
string|"'60.00'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_response_to_delays_usernames
dedent|''
name|'def'
name|'test_response_to_delays_usernames'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|','
string|'"user1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|','
string|'"user2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|','
string|'"user1"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
string|"'60.00'"
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'_request'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|','
string|'"user2"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
string|"'60.00'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeHttplibSocket
dedent|''
dedent|''
name|'class'
name|'FakeHttplibSocket'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Fake `httplib.HTTPResponse` replacement.\n    """'
newline|'\n'
nl|'\n'
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
string|'"""Initialize new `FakeHttplibSocket`."""'
newline|'\n'
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
string|'"""Returns the socket\'s internal buffer."""'
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
string|'"""\n    Fake `httplib.HTTPConnection`.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'app'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize `FakeHttplibConnection`.\n        """'
newline|'\n'
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
name|'body'
op|'='
string|'""'
op|','
name|'headers'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Requests made via this connection actually get translated and routed into\n        our WSGI app, we then wait for the response and turn it back into\n        an `httplib.HTTPResponse`.\n        """'
newline|'\n'
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
name|'headers'
op|'='
name|'headers'
newline|'\n'
name|'req'
op|'.'
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'body'
newline|'\n'
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
string|'"""Return our generated response from the request."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'http_response'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wire_HTTPConnection_to_WSGI
dedent|''
dedent|''
name|'def'
name|'wire_HTTPConnection_to_WSGI'
op|'('
name|'host'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Monkeypatches HTTPConnection so that if you try to connect to host, you\n    are instead routed straight to the given WSGI app.\n\n    After calling this method, when any code calls\n\n    httplib.HTTPConnection(host)\n\n    the connection object will be a fake.  Its requests will be sent directly\n    to the given WSGI app rather than through a socket.\n\n    Code connecting to hosts other than host will not be affected.\n\n    This method may be called multiple times to map different hosts to\n    different apps.\n    """'
newline|'\n'
DECL|class|HTTPConnectionDecorator
name|'class'
name|'HTTPConnectionDecorator'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wraps the real HTTPConnection class so that when you instantiate\n        the class you might instead get a fake instance."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'wrapped'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'wrapped'
op|'='
name|'wrapped'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'connection_host'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'connection_host'
op|'=='
name|'host'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'FakeHttplibConnection'
op|'('
name|'app'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'wrapped'
op|'('
name|'connection_host'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'httplib'
op|'.'
name|'HTTPConnection'
op|'='
name|'HTTPConnectionDecorator'
op|'('
name|'httplib'
op|'.'
name|'HTTPConnection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WsgiLimiterProxyTest
dedent|''
name|'class'
name|'WsgiLimiterProxyTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for the `limits.WsgiLimiterProxy` class.\n    """'
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
string|'"""\n        Do some nifty HTTP/WSGI magic which allows for WSGI to be called\n        directly by something like the `httplib` library.\n        """'
newline|'\n'
name|'test'
op|'.'
name|'TestCase'
op|'.'
name|'setUp'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'time'
op|'='
number|'0.0'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'limits'
op|'.'
name|'WsgiLimiter'
op|'('
name|'TEST_LIMITS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'.'
name|'_limiter'
op|'.'
name|'_get_time'
op|'='
name|'self'
op|'.'
name|'_get_time'
newline|'\n'
name|'wire_HTTPConnection_to_WSGI'
op|'('
string|'"169.254.0.1:80"'
op|','
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'proxy'
op|'='
name|'limits'
op|'.'
name|'WsgiLimiterProxy'
op|'('
string|'"169.254.0.1:80"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_time
dedent|''
name|'def'
name|'_get_time'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the "time" according to this test suite."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'time'
newline|'\n'
nl|'\n'
DECL|member|test_200
dedent|''
name|'def'
name|'test_200'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Successful request test."""'
newline|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'.'
name|'check_for_delay'
op|'('
string|'"GET"'
op|','
string|'"/anything"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_403
dedent|''
name|'def'
name|'test_403'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Forbidden request test."""'
newline|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'.'
name|'check_for_delay'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'delay'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'.'
name|'check_for_delay'
op|'('
string|'"GET"'
op|','
string|'"/delayed"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'delay'
op|','
string|"'60.00'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
