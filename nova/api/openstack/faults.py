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
nl|'\n'
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
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
string|'"""Wrap webob.exc.HTTPException to provide API friendly response."""'
newline|'\n'
nl|'\n'
DECL|variable|_fault_names
name|'_fault_names'
op|'='
op|'{'
nl|'\n'
number|'400'
op|':'
string|'"badRequest"'
op|','
nl|'\n'
number|'401'
op|':'
string|'"unauthorized"'
op|','
nl|'\n'
number|'403'
op|':'
string|'"resizeNotAllowed"'
op|','
nl|'\n'
number|'404'
op|':'
string|'"itemNotFound"'
op|','
nl|'\n'
number|'405'
op|':'
string|'"badMethod"'
op|','
nl|'\n'
number|'409'
op|':'
string|'"inProgress"'
op|','
nl|'\n'
number|'413'
op|':'
string|'"overLimit"'
op|','
nl|'\n'
number|'415'
op|':'
string|'"badMediaType"'
op|','
nl|'\n'
number|'501'
op|':'
string|'"notImplemented"'
op|','
nl|'\n'
number|'503'
op|':'
string|'"serviceUnavailable"'
op|'}'
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
string|'"""Create a Fault for the given webob.exc.exception."""'
newline|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'='
name|'exception'
newline|'\n'
name|'self'
op|'.'
name|'status_int'
op|'='
name|'exception'
op|'.'
name|'status_int'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
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
comment|'# Replace the body with fault details.'
nl|'\n'
name|'code'
op|'='
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'status_int'
newline|'\n'
name|'fault_name'
op|'='
name|'self'
op|'.'
name|'_fault_names'
op|'.'
name|'get'
op|'('
name|'code'
op|','
string|'"cloudServersFault"'
op|')'
newline|'\n'
name|'fault_data'
op|'='
op|'{'
nl|'\n'
name|'fault_name'
op|':'
op|'{'
nl|'\n'
string|"'code'"
op|':'
name|'code'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'explanation'
op|'}'
op|'}'
newline|'\n'
name|'if'
name|'code'
op|'=='
number|'413'
op|':'
newline|'\n'
indent|'            '
name|'retry'
op|'='
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'headers'
op|'['
string|"'Retry-After'"
op|']'
newline|'\n'
name|'fault_data'
op|'['
name|'fault_name'
op|']'
op|'['
string|"'retryAfter'"
op|']'
op|'='
name|'retry'
newline|'\n'
nl|'\n'
comment|"# 'code' is an attribute on the fault tag itself"
nl|'\n'
dedent|''
name|'metadata'
op|'='
op|'{'
string|"'attributes'"
op|':'
op|'{'
name|'fault_name'
op|':'
string|"'code'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'xml_serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|','
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'content_type'
op|'='
name|'req'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'serializer'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'xml_serializer'
op|','
nl|'\n'
string|"'application/json'"
op|':'
name|'wsgi'
op|'.'
name|'JSONDictSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
op|'['
name|'content_type'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'body'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fault_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'content_type'
op|'='
name|'content_type'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'wrapped_exc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OverLimitFault
dedent|''
dedent|''
name|'class'
name|'OverLimitFault'
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
string|'"""\n    Rate-limited request response.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'details'
op|','
name|'retry_time'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize new `OverLimitFault` with relevant information.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'content'
op|'='
op|'{'
nl|'\n'
string|'"overLimitFault"'
op|':'
op|'{'
nl|'\n'
string|'"code"'
op|':'
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'status_int'
op|','
nl|'\n'
string|'"message"'
op|':'
name|'message'
op|','
nl|'\n'
string|'"details"'
op|':'
name|'details'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the wrapped exception with a serialized body conforming to our\n        error format.\n        """'
newline|'\n'
name|'content_type'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|'"attributes"'
op|':'
op|'{'
string|'"overLimitFault"'
op|':'
string|'"code"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'xml_serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|','
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
newline|'\n'
name|'serializer'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'xml_serializer'
op|','
nl|'\n'
string|"'application/json'"
op|':'
name|'wsgi'
op|'.'
name|'JSONDictSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
op|'['
name|'content_type'
op|']'
newline|'\n'
nl|'\n'
name|'content'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'wrapped_exc'
op|'.'
name|'body'
op|'='
name|'content'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'wrapped_exc'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
