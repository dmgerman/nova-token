begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'api_version_request'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'versions'
name|'as'
name|'views_versions'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'enabled'"
op|','
string|"'nova.api.openstack'"
op|','
name|'group'
op|'='
string|"'osapi_v21'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LINKS
name|'LINKS'
op|'='
op|'{'
nl|'\n'
string|"'v2.0'"
op|':'
op|'{'
nl|'\n'
string|"'html'"
op|':'
string|"'http://docs.openstack.org/'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'v2.1'"
op|':'
op|'{'
nl|'\n'
string|"'html'"
op|':'
string|"'http://docs.openstack.org/'"
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|VERSIONS
name|'VERSIONS'
op|'='
op|'{'
nl|'\n'
string|'"v2.0"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"SUPPORTED"'
op|','
nl|'\n'
string|'"version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"min_version"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"text/html"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'LINKS'
op|'['
string|"'v2.0'"
op|']'
op|'['
string|"'html'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json;version=2"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"v2.1"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v2.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"version"'
op|':'
name|'api_version_request'
op|'.'
name|'_MAX_API_VERSION'
op|','
nl|'\n'
string|'"min_version"'
op|':'
name|'api_version_request'
op|'.'
name|'_MIN_API_VERSION'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2013-07-23T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"text/html"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'LINKS'
op|'['
string|"'v2.1'"
op|']'
op|'['
string|"'html'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute+json;version=2.1"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Versions
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Versions'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'osapi_v21'
op|'.'
name|'enabled'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'VERSIONS'
op|'['
string|'"v2.1"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all versions."""'
newline|'\n'
name|'builder'
op|'='
name|'views_versions'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'builder'
op|'.'
name|'build_versions'
op|'('
name|'VERSIONS'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'300'
op|')'
newline|'\n'
DECL|member|multi
name|'def'
name|'multi'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return multiple choices."""'
newline|'\n'
name|'builder'
op|'='
name|'views_versions'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'builder'
op|'.'
name|'build_choices'
op|'('
name|'VERSIONS'
op|','
name|'req'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_action_args
dedent|''
name|'def'
name|'get_action_args'
op|'('
name|'self'
op|','
name|'request_environment'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parse dictionary created by routes library."""'
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'request_environment'
op|'['
string|"'PATH_INFO'"
op|']'
op|'=='
string|"'/'"
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'action'"
op|']'
op|'='
string|"'index'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'action'"
op|']'
op|'='
string|"'multi'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'args'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
