begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'views'
name|'import'
name|'flavors'
name|'as'
name|'flavors_view'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
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
op|'.'
name|'compute'
name|'import'
name|'flavors'
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
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsController
name|'class'
name|'FlavorsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavor controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|variable|_view_builder_class
name|'_view_builder_class'
op|'='
name|'flavors_view'
op|'.'
name|'V3ViewBuilder'
newline|'\n'
nl|'\n'
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all flavors in brief."""'
newline|'\n'
name|'limited_flavors'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'index'
op|'('
name|'req'
op|','
name|'limited_flavors'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'400'
op|')'
newline|'\n'
DECL|member|detail
name|'def'
name|'detail'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return all flavors in detail."""'
newline|'\n'
name|'limited_flavors'
op|'='
name|'self'
op|'.'
name|'_get_flavors'
op|'('
name|'req'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_flavors'
op|'('
name|'limited_flavors'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'detail'
op|'('
name|'req'
op|','
name|'limited_flavors'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
number|'404'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about the given flavor id."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
name|'id'
op|','
name|'ctxt'
op|'='
name|'context'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'cache_db_flavor'
op|'('
name|'flavor'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_view_builder'
op|'.'
name|'show'
op|'('
name|'req'
op|','
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parse_is_public
dedent|''
name|'def'
name|'_parse_is_public'
op|'('
name|'self'
op|','
name|'is_public'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parse is_public into something usable."""'
newline|'\n'
nl|'\n'
name|'if'
name|'is_public'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# preserve default value of showing only public flavors'
nl|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'elif'
name|'utils'
op|'.'
name|'is_none_string'
op|'('
name|'is_public'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'strutils'
op|'.'
name|'bool_from_string'
op|'('
name|'is_public'
op|','
name|'strict'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid is_public filter [%s]'"
op|')'
op|'%'
name|'is_public'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flavors
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_flavors'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Helper function that returns a list of flavor dicts."""'
newline|'\n'
name|'filters'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'sort_key'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'sort_key'"
op|')'
name|'or'
string|"'flavorid'"
newline|'\n'
name|'sort_dir'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'sort_dir'"
op|')'
name|'or'
string|"'asc'"
newline|'\n'
name|'limit'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|')'
name|'or'
name|'None'
newline|'\n'
name|'marker'
op|'='
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'marker'"
op|')'
name|'or'
name|'None'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
comment|'# Only admin has query access to all flavor types'
nl|'\n'
indent|'            '
name|'filters'
op|'['
string|"'is_public'"
op|']'
op|'='
name|'self'
op|'.'
name|'_parse_is_public'
op|'('
nl|'\n'
name|'req'
op|'.'
name|'params'
op|'.'
name|'get'
op|'('
string|"'is_public'"
op|','
name|'None'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'filters'
op|'['
string|"'is_public'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'filters'
op|'['
string|"'disabled'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
string|"'min_ram'"
name|'in'
name|'req'
op|'.'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'filters'
op|'['
string|"'min_memory_mb'"
op|']'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'params'
op|'['
string|"'min_ram'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid min_ram filter [%s]'"
op|')'
op|'%'
name|'req'
op|'.'
name|'params'
op|'['
string|"'min_ram'"
op|']'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'min_disk'"
name|'in'
name|'req'
op|'.'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'filters'
op|'['
string|"'min_root_gb'"
op|']'
op|'='
name|'int'
op|'('
name|'req'
op|'.'
name|'params'
op|'['
string|"'min_disk'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|"'Invalid min_disk filter [%s]'"
op|')'
op|'%'
nl|'\n'
name|'req'
op|'.'
name|'params'
op|'['
string|"'min_disk'"
op|']'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'limited_flavors'
op|'='
name|'flavors'
op|'.'
name|'get_all_flavors_sorted_list'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|'='
name|'filters'
op|','
name|'sort_key'
op|'='
name|'sort_key'
op|','
name|'sort_dir'
op|'='
name|'sort_dir'
op|','
nl|'\n'
name|'limit'
op|'='
name|'limit'
op|','
name|'marker'
op|'='
name|'marker'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'MarkerNotFound'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'marker [%s] not found'"
op|')'
op|'%'
name|'marker'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'limited_flavors'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Flavors
dedent|''
dedent|''
name|'class'
name|'Flavors'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Flavors Extension."""'
newline|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"flavors"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"flavors"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/core/flavors/v3"'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_resources
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'collection_actions'
op|'='
op|'{'
string|"'detail'"
op|':'
string|"'GET'"
op|'}'
newline|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
newline|'\n'
nl|'\n'
name|'resources'
op|'='
op|'['
nl|'\n'
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'flavors'"
op|','
nl|'\n'
name|'FlavorsController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_name'
op|'='
string|"'flavor'"
op|','
nl|'\n'
name|'collection_actions'
op|'='
name|'collection_actions'
op|','
nl|'\n'
name|'member_actions'
op|'='
name|'member_actions'
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
dedent|''
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
