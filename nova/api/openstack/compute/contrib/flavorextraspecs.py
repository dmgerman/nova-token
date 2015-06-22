begin_unit
comment|'# Copyright 2011 University of Southern California'
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
string|'"""The instance type extra specs extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
name|'from'
name|'webob'
name|'import'
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
name|'extensions'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'flavorextraspecs'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorExtraSpecsController
name|'class'
name|'FlavorExtraSpecsController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The flavor extra specs API controller for the OpenStack API."""'
newline|'\n'
nl|'\n'
DECL|member|_get_extra_specs
name|'def'
name|'_get_extra_specs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
name|'return'
name|'dict'
op|'('
name|'extra_specs'
op|'='
name|'flavor'
op|'.'
name|'extra_specs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_body
dedent|''
name|'def'
name|'_check_body'
op|'('
name|'self'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'body'
name|'is'
name|'None'
name|'or'
name|'body'
op|'=='
string|'""'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'No Request Body'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_extra_specs
dedent|''
dedent|''
name|'def'
name|'_check_extra_specs'
op|'('
name|'self'
op|','
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'type'
op|'('
name|'specs'
op|')'
name|'is'
name|'not'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Bad extra_specs provided'"
op|')'
newline|'\n'
name|'raise'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'.'
name|'validate_extra_spec_keys'
op|'('
name|'specs'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Fail to validate provided extra specs keys. "'
nl|'\n'
string|'"Expected string"'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'key'
op|','
string|"'extra_specs key'"
op|','
nl|'\n'
name|'min_length'
op|'='
number|'1'
op|','
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(dims): The following check was added for backwards'
nl|'\n'
comment|'# compatibility.'
nl|'\n'
name|'if'
op|'('
name|'isinstance'
op|'('
name|'value'
op|','
op|'('
name|'int'
op|','
name|'long'
op|','
name|'float'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'value'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'value'
op|','
string|"'extra_specs value'"
op|','
nl|'\n'
name|'max_length'
op|'='
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
dedent|''
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the list of extra specs for a given flavor."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'index'"
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_get_extra_specs'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'create'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_body'
op|'('
name|'body'
op|')'
newline|'\n'
name|'specs'
op|'='
name|'body'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_extra_specs'
op|'('
name|'specs'
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'extra_specs'
op|'='
name|'dict'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|','
op|'**'
name|'specs'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_check_extra_specs'
op|'('
name|'body'
op|')'
newline|'\n'
name|'if'
name|'id'
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body and URI mismatch'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'body'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'expl'
op|'='
name|'_'
op|'('
string|"'Request body contains too many items'"
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'expl'
op|')'
newline|'\n'
dedent|''
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavor'
op|'.'
name|'extra_specs'
op|'='
name|'dict'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|','
op|'**'
name|'body'
op|')'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorExtraSpecUpdateCreateFailed'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FlavorNotFound'
name|'as'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'error'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'body'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a single extra spec item."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'show'"
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
name|'id'
op|':'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
name|'id'
op|']'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Flavor %(flavor_id)s has no extra specs with "'
nl|'\n'
string|'"key %(key)s."'
op|')'
op|'%'
name|'dict'
op|'('
name|'flavor_id'
op|'='
name|'flavor_id'
op|','
nl|'\n'
name|'key'
op|'='
name|'id'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'flavor_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes an existing extra spec."""'
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
name|'authorize'
op|'('
name|'context'
op|','
name|'action'
op|'='
string|"'delete'"
op|')'
newline|'\n'
name|'flavor'
op|'='
name|'common'
op|'.'
name|'get_flavor'
op|'('
name|'context'
op|','
name|'flavor_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'flavor'
op|'.'
name|'extra_specs'
op|'['
name|'id'
op|']'
newline|'\n'
name|'flavor'
op|'.'
name|'save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'FlavorNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'FlavorExtraSpecsNotFound'
op|')'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
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
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Flavor %(flavor_id)s has no extra specs with "'
nl|'\n'
string|'"key %(key)s."'
op|')'
op|'%'
name|'dict'
op|'('
name|'flavor_id'
op|'='
name|'flavor_id'
op|','
nl|'\n'
name|'key'
op|'='
name|'id'
op|')'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Flavorextraspecs
dedent|''
dedent|''
dedent|''
name|'class'
name|'Flavorextraspecs'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Instance type (flavor) extra specs."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"FlavorExtraSpecs"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-flavor-extra-specs"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
op|'('
string|'"http://docs.openstack.org/compute/ext/"'
nl|'\n'
string|'"flavor_extra_specs/api/v1.1"'
op|')'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-06-23T00:00:00Z"'
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
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
string|"'os-extra_specs'"
op|','
nl|'\n'
name|'FlavorExtraSpecsController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
name|'dict'
op|'('
name|'member_name'
op|'='
string|"'flavor'"
op|','
name|'collection_name'
op|'='
string|"'flavors'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
