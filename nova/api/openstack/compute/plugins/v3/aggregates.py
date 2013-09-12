begin_unit
comment|'# Copyright (c) 2012 Citrix Systems, Inc.'
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
string|'"""The Aggregate admin API extension."""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
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
name|'api'
name|'as'
name|'compute_api'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-aggregates"'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|'"v3:"'
op|'+'
name|'ALIAS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_context
name|'def'
name|'_get_context'
op|'('
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_host_from_body
dedent|''
name|'def'
name|'get_host_from_body'
op|'('
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Makes sure that the host exists."""'
newline|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'fn'
op|')'
newline|'\n'
DECL|function|wrapped
name|'def'
name|'wrapped'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
name|'fn'
op|'.'
name|'wsgi_action'
op|')'
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
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'host'
op|'='
name|'body'
op|'['
name|'fn'
op|'.'
name|'wsgi_action'
op|']'
op|'.'
name|'get'
op|'('
string|"'host'"
op|')'
newline|'\n'
name|'if'
name|'host'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Could not find host to be set in "'
nl|'\n'
string|'"request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'host'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"The value of host must be a string"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'fn'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'host'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AggregateController
dedent|''
name|'class'
name|'AggregateController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The Host Aggregates API controller for the OpenStack API."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'api'
op|'='
name|'compute_api'
op|'.'
name|'AggregateAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
op|')'
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
string|'"""Returns a list a host aggregate\'s id, name, availability_zone."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'aggregates'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_aggregate_list'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'aggregates'"
op|':'
op|'['
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'a'
op|')'
op|'['
string|"'aggregate'"
op|']'
nl|'\n'
name|'for'
name|'a'
name|'in'
name|'aggregates'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'201'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates an aggregate, given its name and availability_zone."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'aggregate'"
op|')'
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
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host_aggregate'
op|'='
name|'body'
op|'['
string|'"aggregate"'
op|']'
newline|'\n'
name|'name'
op|'='
name|'host_aggregate'
op|'['
string|'"name"'
op|']'
newline|'\n'
name|'avail_zone'
op|'='
name|'host_aggregate'
op|'['
string|'"availability_zone"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Could not find %s parameter in the request"'
op|')'
op|'%'
name|'e'
op|'.'
name|'args'
op|'['
number|'0'
op|']'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'name'
op|','
string|'"Aggregate name"'
op|','
number|'1'
op|','
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'create_aggregate'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'avail_zone'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateNameExists'
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
name|'InvalidAggregateAction'
name|'as'
name|'e'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
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
string|'"""Shows the details of an aggregate, hosts and metadata included."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_aggregate'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateNotFound'
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
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates the name and/or availability_zone of given aggregate."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'aggregate'"
op|')'
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
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'updates'
op|'='
name|'body'
op|'['
string|'"aggregate"'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'updates'
op|')'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Request body is empty"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'updates'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
name|'not'
name|'in'
op|'['
string|'"name"'
op|','
string|'"availability_zone"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Invalid key %s in request body."'
op|')'
op|'%'
name|'key'
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
dedent|''
name|'if'
string|"'name'"
name|'in'
name|'updates'
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
name|'updates'
op|'['
string|"'name'"
op|']'
op|','
string|'"Aggregate name"'
op|','
number|'1'
op|','
nl|'\n'
number|'255'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
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
name|'e'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'update_aggregate'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'updates'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateNotFound'
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
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
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
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'204'
op|')'
newline|'\n'
DECL|member|delete
name|'def'
name|'delete'
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
string|'"""Removes an aggregate by id."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_aggregate'
op|'('
name|'context'
op|','
name|'id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateNotFound'
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
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'get_host_from_body'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'add_host'"
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
DECL|member|_add_host
name|'def'
name|'_add_host'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adds a host to the specified aggregate."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'add_host_to_aggregate'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'AggregateNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
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
op|'('
name|'exception'
op|'.'
name|'AggregateHostExists'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidAggregateAction'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|','
number|'409'
op|')'
op|')'
newline|'\n'
op|'@'
name|'get_host_from_body'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'remove_host'"
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'response'
op|'('
number|'202'
op|')'
newline|'\n'
DECL|member|_remove_host
name|'def'
name|'_remove_host'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a host from the specified aggregate."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'remove_host_from_aggregate'
op|'('
name|'context'
op|','
name|'id'
op|','
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'exception'
op|'.'
name|'AggregateNotFound'
op|','
name|'exception'
op|'.'
name|'AggregateHostNotFound'
op|','
nl|'\n'
name|'exception'
op|'.'
name|'ComputeHostNotFound'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot remove host %(host)s in aggregate %(id)s'"
op|')'
op|'%'
op|'{'
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
string|"'id'"
op|':'
name|'id'
op|'}'
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
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidAggregateAction'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot remove host %(host)s in aggregate %(id)s'"
op|')'
op|'%'
op|'{'
nl|'\n'
string|"'host'"
op|':'
name|'host'
op|','
string|"'id'"
op|':'
name|'id'
op|'}'
newline|'\n'
name|'raise'
name|'exc'
op|'.'
name|'HTTPConflict'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'extensions'
op|'.'
name|'expected_errors'
op|'('
op|'('
number|'400'
op|','
number|'404'
op|')'
op|')'
newline|'\n'
op|'@'
name|'wsgi'
op|'.'
name|'action'
op|'('
string|"'set_metadata'"
op|')'
newline|'\n'
DECL|member|_set_metadata
name|'def'
name|'_set_metadata'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Replaces the aggregate\'s existing metadata with new metadata."""'
newline|'\n'
name|'context'
op|'='
name|'_get_context'
op|'('
name|'req'
op|')'
newline|'\n'
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|','
string|"'set_metadata'"
op|')'
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
name|'_'
op|'('
string|'"Invalid request body"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'is_valid_body'
op|'('
name|'body'
op|'['
string|'"set_metadata"'
op|']'
op|','
string|'"metadata"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
nl|'\n'
name|'explanation'
op|'='
name|'_'
op|'('
string|'"Invalid request format for metadata"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'metadata'
op|'='
name|'body'
op|'['
string|'"set_metadata"'
op|']'
op|'['
string|'"metadata"'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'aggregate'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'update_aggregate_metadata'
op|'('
name|'context'
op|','
nl|'\n'
name|'id'
op|','
name|'metadata'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'AggregateNotFound'
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
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_marshall_aggregate
dedent|''
name|'def'
name|'_marshall_aggregate'
op|'('
name|'self'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_aggregate'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'aggregate'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): The original API specified non-TZ-aware timestamps'
nl|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'value'
op|'.'
name|'replace'
op|'('
name|'tzinfo'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'_aggregate'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|'"aggregate"'
op|':'
name|'_aggregate'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Aggregates
dedent|''
dedent|''
name|'class'
name|'Aggregates'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Admin-only aggregate administration."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Aggregates"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/aggregates/api/v3"'
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
name|'resources'
op|'='
op|'['
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'alias'
op|','
nl|'\n'
name|'AggregateController'
op|'('
op|')'
op|','
nl|'\n'
name|'member_actions'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'POST'"
op|'}'
op|')'
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
