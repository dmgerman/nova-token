begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'webob'
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
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
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
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'gettextutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFaultWrapper
name|'class'
name|'TestFaultWrapper'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests covering `nova.api.openstack:FaultWrapper` class."""'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.openstack.common.gettextutils.get_localized_message'"
op|')'
newline|'\n'
DECL|member|test_safe_exception_translated
name|'def'
name|'test_safe_exception_translated'
op|'('
name|'self'
op|','
name|'mock_get_localized'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'gettextutils'
op|'.'
name|'Message'
op|'('
string|"'Should be translated.'"
op|','
string|"'nova'"
op|')'
newline|'\n'
name|'safe_exception'
op|'='
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
name|'safe_exception'
op|'.'
name|'msg_fmt'
op|'='
name|'msg'
newline|'\n'
name|'safe_exception'
op|'.'
name|'safe'
op|'='
name|'True'
newline|'\n'
name|'safe_exception'
op|'.'
name|'code'
op|'='
number|'404'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_translate
name|'def'
name|'fake_translate'
op|'('
name|'mesg'
op|','
name|'locale'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'str'
op|'('
name|'mesg'
op|')'
op|'=='
string|'"Should be translated."'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|'"I\'ve been translated!"'
newline|'\n'
dedent|''
name|'return'
name|'mesg'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_get_localized'
op|'.'
name|'side_effect'
op|'='
name|'fake_translate'
newline|'\n'
nl|'\n'
DECL|function|raiser
name|'def'
name|'raiser'
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
name|'raise'
name|'safe_exception'
newline|'\n'
nl|'\n'
dedent|''
name|'wrapper'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'FaultWrapper'
op|'('
name|'raiser'
op|')'
newline|'\n'
name|'response'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'wrapper'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"I\'ve been translated!"'
op|','
name|'unicode'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
op|')'
newline|'\n'
name|'mock_get_localized'
op|'.'
name|'assert_any_call'
op|'('
nl|'\n'
string|"u'Should be translated.'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestFaults
dedent|''
dedent|''
name|'class'
name|'TestFaults'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests covering `nova.api.openstack.faults:Fault` class."""'
newline|'\n'
nl|'\n'
DECL|member|_prepare_xml
name|'def'
name|'_prepare_xml'
op|'('
name|'self'
op|','
name|'xml_string'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove characters from string which hinder XML equality testing."""'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\n"'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\t"'
op|','
string|'""'
op|')'
newline|'\n'
name|'return'
name|'xml_string'
newline|'\n'
nl|'\n'
DECL|member|test_400_fault_json
dedent|''
name|'def'
name|'test_400_fault_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test fault serialized to JSON via file-extension and/or header.'
nl|'\n'
indent|'        '
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.json'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/json"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'fault'
op|'='
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'scram'"
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"badRequest"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"scram"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'400'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_413_fault_json
dedent|''
dedent|''
name|'def'
name|'test_413_fault_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test fault serialized to JSON via file-extension and/or header.'
nl|'\n'
indent|'        '
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.json'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/json"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPRequestEntityTooLarge'
newline|'\n'
comment|'# NOTE(aloga): we intentionally pass an integer for the'
nl|'\n'
comment|"# 'Retry-After' header. It should be then converted to a str"
nl|'\n'
name|'fault'
op|'='
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'('
name|'explanation'
op|'='
string|"'sorry'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'4'
op|'}'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"overLimit"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'413'
op|','
nl|'\n'
string|'"retryAfter"'
op|':'
string|'"4"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_429_fault_json
dedent|''
dedent|''
name|'def'
name|'test_429_fault_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test fault serialized to JSON via file-extension and/or header.'
nl|'\n'
indent|'        '
name|'requests'
op|'='
op|'['
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.json'"
op|')'
op|','
nl|'\n'
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|','
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/json"'
op|'}'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'request'
name|'in'
name|'requests'
op|':'
newline|'\n'
indent|'            '
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPTooManyRequests'
newline|'\n'
comment|'# NOTE(aloga): we intentionally pass an integer for the'
nl|'\n'
comment|"# 'Retry-After' header. It should be then converted to a str"
nl|'\n'
name|'fault'
op|'='
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'exc'
op|'('
name|'explanation'
op|'='
string|"'sorry'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|"'Retry-After'"
op|':'
number|'4'
op|'}'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"overLimit"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'429'
op|','
nl|'\n'
string|'"retryAfter"'
op|':'
string|'"4"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_raise
dedent|''
dedent|''
name|'def'
name|'test_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure the ability to raise :class:`Fault` in WSGI-ified methods.'
nl|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raiser
name|'def'
name|'raiser'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
string|"'whut?'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'raiser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'whut?'"
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_raise_403
dedent|''
name|'def'
name|'test_raise_403'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure the ability to raise :class:`Fault` in WSGI-ified methods.'
nl|'\n'
indent|'        '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raiser
name|'def'
name|'raiser'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
string|"'whut?'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'raiser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'resizeNotAllowed'"
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'forbidden'"
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_raise_localize_explanation
dedent|''
name|'def'
name|'test_raise_localize_explanation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msgid'
op|'='
string|'"String with params: %s"'
newline|'\n'
name|'params'
op|'='
op|'('
string|"'blah'"
op|','
op|')'
newline|'\n'
name|'lazy_gettext'
op|'='
name|'gettextutils'
op|'.'
name|'_'
newline|'\n'
name|'expl'
op|'='
name|'lazy_gettext'
op|'('
name|'msgid'
op|')'
op|'%'
name|'params'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|raiser
name|'def'
name|'raiser'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/.xml'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'raiser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
op|'('
name|'msgid'
op|'%'
name|'params'
op|')'
op|','
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_fault_has_status_int
dedent|''
name|'def'
name|'test_fault_has_status_int'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure the status_int is set correctly on faults.'
nl|'\n'
indent|'        '
name|'fault'
op|'='
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'what?'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fault'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_xml_serializer
dedent|''
name|'def'
name|'test_xml_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Ensure that a v1.1 request responds with a v1.1 xmlns.'
nl|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1'"
op|','
nl|'\n'
name|'headers'
op|'='
op|'{'
string|'"Accept"'
op|':'
string|'"application/xml"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'fault'
op|'='
name|'wsgi'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
string|"'scram'"
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'fault'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'common'
op|'.'
name|'XML_NS_V11'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'content_type'
op|','
string|'"application/xml"'
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
number|'400'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FaultsXMLSerializationTestV11
dedent|''
dedent|''
name|'class'
name|'FaultsXMLSerializationTestV11'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Tests covering `nova.api.openstack.faults:Fault` class."""'
newline|'\n'
nl|'\n'
DECL|member|_prepare_xml
name|'def'
name|'_prepare_xml'
op|'('
name|'self'
op|','
name|'xml_string'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"  "'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\n"'
op|','
string|'""'
op|')'
newline|'\n'
name|'xml_string'
op|'='
name|'xml_string'
op|'.'
name|'replace'
op|'('
string|'"\\t"'
op|','
string|'""'
op|')'
newline|'\n'
name|'return'
name|'xml_string'
newline|'\n'
nl|'\n'
DECL|member|test_400_fault
dedent|''
name|'def'
name|'test_400_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'attributes'"
op|':'
op|'{'
string|'"badRequest"'
op|':'
string|"'code'"
op|'}'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'xmlns'
op|'='
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|'"badRequest"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"scram"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'400'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <badRequest code="400" xmlns="%s">\n                    <message>scram</message>\n                </badRequest>\n            """'
op|')'
op|'%'
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_413_fault
dedent|''
name|'def'
name|'test_413_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'attributes'"
op|':'
op|'{'
string|'"overLimit"'
op|':'
string|"'code'"
op|'}'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'xmlns'
op|'='
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|'"overLimit"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'413'
op|','
nl|'\n'
string|'"retryAfter"'
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <overLimit code="413" xmlns="%s">\n                    <message>sorry</message>\n                    <retryAfter>4</retryAfter>\n                </overLimit>\n            """'
op|')'
op|'%'
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_429_fault
dedent|''
name|'def'
name|'test_429_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'attributes'"
op|':'
op|'{'
string|'"overLimit"'
op|':'
string|"'code'"
op|'}'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'xmlns'
op|'='
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|'"overLimit"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'429'
op|','
nl|'\n'
string|'"retryAfter"'
op|':'
number|'4'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <overLimit code="429" xmlns="%s">\n                    <message>sorry</message>\n                    <retryAfter>4</retryAfter>\n                </overLimit>\n            """'
op|')'
op|'%'
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_404_fault
dedent|''
name|'def'
name|'test_404_fault'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'attributes'"
op|':'
op|'{'
string|'"itemNotFound"'
op|':'
string|"'code'"
op|'}'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|','
nl|'\n'
name|'xmlns'
op|'='
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'fixture'
op|'='
op|'{'
nl|'\n'
string|'"itemNotFound"'
op|':'
op|'{'
nl|'\n'
string|'"message"'
op|':'
string|'"sorry"'
op|','
nl|'\n'
string|'"code"'
op|':'
number|'404'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'output'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
name|'output'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'self'
op|'.'
name|'_prepare_xml'
op|'('
string|'"""\n                <itemNotFound code="404" xmlns="%s">\n                    <message>sorry</message>\n                </itemNotFound>\n            """'
op|')'
op|'%'
name|'common'
op|'.'
name|'XML_NS_V11'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|'.'
name|'toxml'
op|'('
op|')'
op|','
name|'actual'
op|'.'
name|'toxml'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
