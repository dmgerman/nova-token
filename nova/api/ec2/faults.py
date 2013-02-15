begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
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
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Fault
name|'class'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPException'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Captures exception and return REST Response."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a response for the given webob.exc.exception."""'
newline|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'='
name|'exception'
newline|'\n'
nl|'\n'
dedent|''
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
string|'"""Generate a WSGI response based on the exception passed to ctor."""'
newline|'\n'
name|'code'
op|'='
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'status_int'
newline|'\n'
name|'message'
op|'='
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'explanation'
newline|'\n'
nl|'\n'
name|'if'
name|'code'
op|'=='
number|'501'
op|':'
newline|'\n'
indent|'            '
name|'message'
op|'='
string|'"The requested function is not supported"'
newline|'\n'
dedent|''
name|'code'
op|'='
name|'str'
op|'('
name|'code'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'AWSAccessKeyId'"
name|'not'
name|'in'
name|'req'
op|'.'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
name|'user_id'
op|','
name|'_sep'
op|','
name|'project_id'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'AWSAccessKeyId'"
op|']'
op|'.'
name|'partition'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'project_id'
op|'='
name|'project_id'
name|'or'
name|'user_id'
newline|'\n'
name|'remote_address'
op|'='
name|'getattr'
op|'('
name|'req'
op|','
string|"'remote_address'"
op|','
string|"'127.0.0.1'"
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user_id'
op|','
nl|'\n'
name|'project_id'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'status'
op|'='
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'status_int'
newline|'\n'
name|'resp'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'resp'
op|'.'
name|'body'
op|'='
name|'str'
op|'('
string|'\'<?xml version="1.0"?>\\n\''
nl|'\n'
string|"'<Response><Errors><Error><Code>%s</Code>'"
nl|'\n'
string|"'<Message>%s</Message></Error></Errors>'"
nl|'\n'
string|"'<RequestID>%s</RequestID></Response>'"
op|'%'
nl|'\n'
op|'('
name|'utils'
op|'.'
name|'xhtml_escape'
op|'('
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'code'
op|')'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'xhtml_escape'
op|'('
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'message'
op|')'
op|')'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'xhtml_escape'
op|'('
name|'utils'
op|'.'
name|'utf8'
op|'('
name|'ctxt'
op|'.'
name|'request_id'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resp'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
