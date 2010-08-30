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
string|'"""\nTest for the root WSGI middleware for all API controllers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Test
name|'class'
name|'Test'
op|'('
name|'unittest'
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
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
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
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable-msg=C0103'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rackspace
dedent|''
name|'def'
name|'test_rackspace'
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
name|'api'
op|'.'
name|'rackspace'
op|','
string|"'API'"
op|','
name|'APIStub'
op|')'
newline|'\n'
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.0/cloud'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|'.'
name|'API'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"/cloud"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ec2
dedent|''
name|'def'
name|'test_ec2'
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
name|'api'
op|'.'
name|'ec2'
op|','
string|"'API'"
op|','
name|'APIStub'
op|')'
newline|'\n'
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/ec2/cloud'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|'.'
name|'API'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"/cloud"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_found
dedent|''
name|'def'
name|'test_not_found'
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
name|'api'
op|'.'
name|'ec2'
op|','
string|"'API'"
op|','
name|'APIStub'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'api'
op|'.'
name|'rackspace'
op|','
string|"'API'"
op|','
name|'APIStub'
op|')'
newline|'\n'
name|'result'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/test/cloud'"
op|')'
op|'.'
name|'get_response'
op|'('
name|'api'
op|'.'
name|'API'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'result'
op|'.'
name|'body'
op|','
string|'"/cloud"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIStub
dedent|''
dedent|''
name|'class'
name|'APIStub'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class to verify request and mark it was called."""'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'req'
op|'.'
name|'path_info'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
