begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 X.commerce, a business unit of eBay Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'iso8601'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'openstack'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|NS
name|'NS'
op|'='
string|'"{http://docs.openstack.org/common/api/v1.0}"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionTestCase
name|'class'
name|'ExtensionTestCase'
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
name|'ExtensionTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext_list'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_volume_extension'
op|'['
op|':'
op|']'
newline|'\n'
name|'fox'
op|'='
op|'('
string|"'nova.tests.api.openstack.volume.extensions.'"
nl|'\n'
string|"'foxinsocks.Foxinsocks'"
op|')'
newline|'\n'
name|'if'
name|'fox'
name|'not'
name|'in'
name|'ext_list'
op|':'
newline|'\n'
indent|'            '
name|'ext_list'
op|'.'
name|'append'
op|'('
name|'fox'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_volume_extension'
op|'='
name|'ext_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionControllerTest
dedent|''
dedent|''
dedent|''
name|'class'
name|'ExtensionControllerTest'
op|'('
name|'ExtensionTestCase'
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
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ExtensionControllerTest'
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
name|'ext_list'
op|'='
op|'['
nl|'\n'
string|'"TypesManage"'
op|','
nl|'\n'
string|'"TypesExtraSpecs"'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'ext_list'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_extensions_json
dedent|''
name|'def'
name|'test_list_extensions_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'volume'
op|'.'
name|'APIRouter'
op|'('
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
string|'"/fake/extensions"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure we have all the extensions, extra extensions being OK.'
nl|'\n'
name|'data'
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
name|'names'
op|'='
op|'['
name|'str'
op|'('
name|'x'
op|'['
string|"'name'"
op|']'
op|')'
name|'for'
name|'x'
name|'in'
name|'data'
op|'['
string|"'extensions'"
op|']'
nl|'\n'
name|'if'
name|'str'
op|'('
name|'x'
op|'['
string|"'name'"
op|']'
op|')'
name|'in'
name|'self'
op|'.'
name|'ext_list'
op|']'
newline|'\n'
name|'names'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'names'
op|','
name|'self'
op|'.'
name|'ext_list'
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure all the timestamps are valid according to iso8601'
nl|'\n'
name|'for'
name|'ext'
name|'in'
name|'data'
op|'['
string|"'extensions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'iso8601'
op|'.'
name|'parse_date'
op|'('
name|'ext'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure that at least Fox in Sox is correct.'
nl|'\n'
dedent|''
op|'('
name|'fox_ext'
op|','
op|')'
op|'='
op|'['
nl|'\n'
name|'x'
name|'for'
name|'x'
name|'in'
name|'data'
op|'['
string|"'extensions'"
op|']'
name|'if'
name|'x'
op|'['
string|"'alias'"
op|']'
op|'=='
string|"'FOXNSOX'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fox_ext'
op|','
op|'{'
nl|'\n'
string|"'namespace'"
op|':'
string|"'http://www.fox.in.socks/api/ext/pie/v1.0'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'Fox In Socks'"
op|','
nl|'\n'
string|"'updated'"
op|':'
string|"'2011-01-22T13:25:27-06:00'"
op|','
nl|'\n'
string|"'description'"
op|':'
string|"'The Fox In Socks Extension'"
op|','
nl|'\n'
string|"'alias'"
op|':'
string|"'FOXNSOX'"
op|','
nl|'\n'
string|"'links'"
op|':'
op|'['
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'ext'
name|'in'
name|'data'
op|'['
string|"'extensions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'url'
op|'='
string|"'/fake/extensions/%s'"
op|'%'
name|'ext'
op|'['
string|"'alias'"
op|']'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|'['
string|"'extension'"
op|']'
op|'['
string|"'alias'"
op|']'
op|','
name|'ext'
op|'['
string|"'alias'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_extension_json
dedent|''
dedent|''
name|'def'
name|'test_get_extension_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'volume'
op|'.'
name|'APIRouter'
op|'('
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
string|'"/fake/extensions/FOXNSOX"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
name|'data'
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'extension'"
op|']'
op|','
op|'{'
nl|'\n'
string|'"namespace"'
op|':'
string|'"http://www.fox.in.socks/api/ext/pie/v1.0"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"Fox In Socks"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-22T13:25:27-06:00"'
op|','
nl|'\n'
string|'"description"'
op|':'
string|'"The Fox In Socks Extension"'
op|','
nl|'\n'
string|'"alias"'
op|':'
string|'"FOXNSOX"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_non_existing_extension_json
dedent|''
name|'def'
name|'test_get_non_existing_extension_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'volume'
op|'.'
name|'APIRouter'
op|'('
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
string|'"/fake/extensions/4"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_extensions_xml
dedent|''
name|'def'
name|'test_list_extensions_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'volume'
op|'.'
name|'APIRouter'
op|'('
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
string|'"/fake/extensions"'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'accept'
op|'='
string|'"application/xml"'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
name|'root'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'tag'
op|'.'
name|'split'
op|'('
string|"'extensions'"
op|')'
op|'['
number|'0'
op|']'
op|','
name|'NS'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure we have all the extensions, extras extensions being OK.'
nl|'\n'
name|'exts'
op|'='
name|'root'
op|'.'
name|'findall'
op|'('
string|"'{0}extension'"
op|'.'
name|'format'
op|'('
name|'NS'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'len'
op|'('
name|'exts'
op|')'
op|'>='
name|'len'
op|'('
name|'self'
op|'.'
name|'ext_list'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Make sure that at least Fox in Sox is correct.'
nl|'\n'
op|'('
name|'fox_ext'
op|','
op|')'
op|'='
op|'['
name|'x'
name|'for'
name|'x'
name|'in'
name|'exts'
name|'if'
name|'x'
op|'.'
name|'get'
op|'('
string|"'alias'"
op|')'
op|'=='
string|"'FOXNSOX'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fox_ext'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
string|"'Fox In Socks'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fox_ext'
op|'.'
name|'get'
op|'('
string|"'namespace'"
op|')'
op|','
nl|'\n'
string|"'http://www.fox.in.socks/api/ext/pie/v1.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fox_ext'
op|'.'
name|'get'
op|'('
string|"'updated'"
op|')'
op|','
string|"'2011-01-22T13:25:27-06:00'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fox_ext'
op|'.'
name|'findtext'
op|'('
string|"'{0}description'"
op|'.'
name|'format'
op|'('
name|'NS'
op|')'
op|')'
op|','
nl|'\n'
string|"'The Fox In Socks Extension'"
op|')'
newline|'\n'
nl|'\n'
name|'xmlutil'
op|'.'
name|'validate_schema'
op|'('
name|'root'
op|','
string|"'extensions'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_extension_xml
dedent|''
name|'def'
name|'test_get_extension_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'volume'
op|'.'
name|'APIRouter'
op|'('
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
string|'"/fake/extensions/FOXNSOX"'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'accept'
op|'='
string|'"application/xml"'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'xml'
op|'='
name|'response'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
name|'root'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'tag'
op|'.'
name|'split'
op|'('
string|"'extension'"
op|')'
op|'['
number|'0'
op|']'
op|','
name|'NS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'get'
op|'('
string|"'alias'"
op|')'
op|','
string|"'FOXNSOX'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|','
string|"'Fox In Socks'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'get'
op|'('
string|"'namespace'"
op|')'
op|','
nl|'\n'
string|"'http://www.fox.in.socks/api/ext/pie/v1.0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'get'
op|'('
string|"'updated'"
op|')'
op|','
string|"'2011-01-22T13:25:27-06:00'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'root'
op|'.'
name|'findtext'
op|'('
string|"'{0}description'"
op|'.'
name|'format'
op|'('
name|'NS'
op|')'
op|')'
op|','
nl|'\n'
string|"'The Fox In Socks Extension'"
op|')'
newline|'\n'
nl|'\n'
name|'xmlutil'
op|'.'
name|'validate_schema'
op|'('
name|'root'
op|','
string|"'extension'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
