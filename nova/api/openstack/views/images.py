begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010-2011 OpenStack LLC.'
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
name|'os'
op|'.'
name|'path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilder
name|'class'
name|'ViewBuilder'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base class for generating responses to OpenStack API requests for\n    information about images.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'base_url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize new `ViewBuilder`.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_url'
op|'='
name|'base_url'
newline|'\n'
nl|'\n'
DECL|member|_format_dates
dedent|''
name|'def'
name|'_format_dates'
op|'('
name|'self'
op|','
name|'image'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr'
name|'in'
op|'['
string|"'created_at'"
op|','
string|"'updated_at'"
op|','
string|"'deleted_at'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'image'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'image'
op|'['
name|'attr'
op|']'
op|'='
name|'image'
op|'['
name|'attr'
op|']'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|generate_href
dedent|''
dedent|''
dedent|''
name|'def'
name|'generate_href'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return an href string pointing to this object.\n        """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_url'
op|','
string|'"images"'
op|','
name|'str'
op|'('
name|'image_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|build
dedent|''
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'image_obj'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a standardized image structure for display by the API.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_format_dates'
op|'('
name|'image_obj'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image_obj'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image_obj'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'detail'
op|':'
newline|'\n'
indent|'            '
name|'image'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|'"created"'
op|':'
name|'image_obj'
op|'['
string|'"created_at"'
op|']'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'image_obj'
op|'['
string|'"updated_at"'
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'image_obj'
op|'['
string|'"status"'
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'image'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV10
dedent|''
dedent|''
name|'class'
name|'ViewBuilderV10'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ViewBuilderV11
dedent|''
name|'class'
name|'ViewBuilderV11'
op|'('
name|'ViewBuilder'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    OpenStack API v1.1 Image Builder\n    """'
newline|'\n'
nl|'\n'
DECL|member|build
name|'def'
name|'build'
op|'('
name|'self'
op|','
name|'image_obj'
op|','
name|'detail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return a standardized image structure for display by the API.\n        """'
newline|'\n'
name|'image'
op|'='
name|'ViewBuilder'
op|'.'
name|'build'
op|'('
name|'self'
op|','
name|'image_obj'
op|','
name|'detail'
op|')'
newline|'\n'
name|'href'
op|'='
name|'self'
op|'.'
name|'generate_href'
op|'('
name|'image_obj'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'['
string|'"links"'
op|']'
op|'='
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/xml"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'image'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
