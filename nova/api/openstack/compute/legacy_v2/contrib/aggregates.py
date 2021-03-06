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
name|'extensions'
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
name|'context'
name|'as'
name|'nova_context'
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
string|"'aggregates'"
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
name|'len'
op|'('
name|'body'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Only host parameter can be specified'"
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
name|'elif'
string|"'host'"
name|'not'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Host parameter must be specified'"
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'body'
op|'['
string|"'host'"
op|']'
op|','
string|"'host'"
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
name|'host'
op|'='
name|'body'
op|'['
string|"'host'"
op|']'
newline|'\n'
nl|'\n'
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
name|'object'
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
DECL|member|index
dedent|''
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
DECL|member|create
dedent|''
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
string|'"""Creates an aggregate, given its name and\n        optional availability zone.\n        """'
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
nl|'\n'
name|'if'
name|'len'
op|'('
name|'body'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
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
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
name|'avail_zone'
op|'='
name|'host_aggregate'
op|'.'
name|'get'
op|'('
string|'"availability_zone"'
op|')'
newline|'\n'
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
name|'if'
name|'avail_zone'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'avail_zone'
op|','
string|'"Availability_zone"'
op|','
number|'1'
op|','
nl|'\n'
number|'255'
op|')'
newline|'\n'
dedent|''
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
nl|'\n'
dedent|''
name|'agg'
op|'='
name|'self'
op|'.'
name|'_marshall_aggregate'
op|'('
name|'aggregate'
op|')'
newline|'\n'
nl|'\n'
comment|'# To maintain the same API result as before the changes for returning'
nl|'\n'
comment|'# nova objects were made.'
nl|'\n'
name|'del'
name|'agg'
op|'['
string|"'aggregate'"
op|']'
op|'['
string|"'hosts'"
op|']'
newline|'\n'
name|'del'
name|'agg'
op|'['
string|"'aggregate'"
op|']'
op|'['
string|"'metadata'"
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'agg'
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
DECL|member|update
dedent|''
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
nl|'\n'
name|'if'
name|'len'
op|'('
name|'body'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'='
name|'body'
op|'['
string|'"aggregate"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
op|')'
newline|'\n'
nl|'\n'
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
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'name'"
name|'in'
name|'updates'
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
name|'if'
name|'updates'
op|'.'
name|'get'
op|'('
string|'"availability_zone"'
op|')'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'updates'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
string|'"Availability_zone"'
op|','
number|'1'
op|','
number|'255'
op|')'
newline|'\n'
dedent|''
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
DECL|member|delete
dedent|''
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
nl|'\n'
DECL|member|action
dedent|''
dedent|''
name|'def'
name|'action'
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
name|'_actions'
op|'='
op|'{'
nl|'\n'
string|"'add_host'"
op|':'
name|'self'
op|'.'
name|'_add_host'
op|','
nl|'\n'
string|"'remove_host'"
op|':'
name|'self'
op|'.'
name|'_remove_host'
op|','
nl|'\n'
string|"'set_metadata'"
op|':'
name|'self'
op|'.'
name|'_set_metadata'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'for'
name|'action'
op|','
name|'data'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'action'
name|'not'
name|'in'
name|'_actions'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Aggregates does not have %s action'"
op|')'
op|'%'
name|'action'
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
name|'return'
name|'_actions'
op|'['
name|'action'
op|']'
op|'('
name|'req'
op|','
name|'id'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
nl|'\n'
dedent|''
op|'@'
name|'get_host_from_body'
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
nl|'\n'
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
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
string|"'Cannot add host %(host)s in aggregate'"
nl|'\n'
string|"' %(id)s: not found'"
op|')'
op|'%'
op|'{'
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
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot add host %(host)s in aggregate'"
nl|'\n'
string|"' %(id)s: host exists'"
op|')'
op|'%'
op|'{'
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
name|'get_host_from_body'
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
nl|'\n'
comment|'# NOTE(alex_xu): back-compatible with db layer hard-code admin'
nl|'\n'
comment|'# permission checks. This has to be left only for API v2.0 because'
nl|'\n'
comment|'# this version has to be stable even if it means that only admins'
nl|'\n'
comment|'# can call this method while the policy could be changed.'
nl|'\n'
name|'nova_context'
op|'.'
name|'require_admin_context'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
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
string|"'Cannot remove host %(host)s in aggregate'"
nl|'\n'
string|"' %(id)s: not found'"
op|')'
op|'%'
op|'{'
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
string|"'Cannot remove host %(host)s in aggregate'"
nl|'\n'
string|"' %(id)s: invalid'"
op|')'
op|'%'
op|'{'
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
DECL|member|_set_metadata
dedent|''
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
nl|'\n'
name|'if'
name|'len'
op|'('
name|'body'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'='
name|'body'
op|'['
string|'"metadata"'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# The metadata should be a dict'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'metadata'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'The value of metadata must be a dict'"
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
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'metadata'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'key'
op|','
string|'"metadata.key"'
op|','
number|'1'
op|','
number|'255'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'utils'
op|'.'
name|'check_string_length'
op|'('
name|'value'
op|','
string|'"metadata.value"'
op|','
number|'0'
op|','
number|'255'
op|')'
newline|'\n'
dedent|''
dedent|''
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
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Cannot set metadata %(metadata)s in aggregate'"
nl|'\n'
string|"' %(id)s'"
op|')'
op|'%'
op|'{'
string|"'metadata'"
op|':'
name|'metadata'
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
name|'self'
op|'.'
name|'_build_aggregate_items'
op|'('
name|'aggregate'
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
DECL|member|_build_aggregate_items
dedent|''
name|'def'
name|'_build_aggregate_items'
op|'('
name|'self'
op|','
name|'aggregate'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(rlrossit): Within the compute API, metadata will always be'
nl|'\n'
comment|'# set on the aggregate object (at a minimum to {}). Because of this,'
nl|'\n'
comment|'# we can freely use getattr() on keys in obj_extra_fields (in this'
nl|'\n'
comment|"# case it is only ['availability_zone']) without worrying about"
nl|'\n'
comment|'# lazy-loading an unset variable'
nl|'\n'
indent|'        '
name|'keys'
op|'='
name|'aggregate'
op|'.'
name|'obj_fields'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
comment|'# NOTE(danms): Skip the uuid field because we have no microversion'
nl|'\n'
comment|'# to expose it'
nl|'\n'
indent|'            '
name|'if'
op|'('
op|'('
name|'aggregate'
op|'.'
name|'obj_attr_is_set'
op|'('
name|'key'
op|')'
nl|'\n'
name|'or'
name|'key'
name|'in'
name|'aggregate'
op|'.'
name|'obj_extra_fields'
op|')'
name|'and'
nl|'\n'
name|'key'
op|'!='
string|"'uuid'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'key'
op|','
name|'getattr'
op|'('
name|'aggregate'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Aggregates
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Aggregates'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
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
string|'"os-aggregates"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/compute/ext/aggregates/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2012-01-12T00:00:00Z"'
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
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-aggregates'"
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
string|'"action"'
op|':'
string|'"POST"'
op|','
op|'}'
op|')'
newline|'\n'
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
