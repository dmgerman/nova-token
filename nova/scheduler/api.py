begin_unit
comment|'# Copyright (c) 2011 Openstack, LLC.'
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
string|'"""\nHandles all requests relating to schedulers.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'novaclient'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'enable_zone_routing'"
op|','
nl|'\n'
name|'False'
op|','
nl|'\n'
string|"'When True, routing to child zones will occur.'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.scheduler.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_call_scheduler
name|'def'
name|'_call_scheduler'
op|'('
name|'method'
op|','
name|'context'
op|','
name|'params'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generic handler for RPC calls to the scheduler.\n\n    :param params: Optional dictionary of arguments to be passed to the\n                   scheduler worker\n\n    :retval: Result returned by scheduler worker\n    """'
newline|'\n'
name|'if'
name|'not'
name|'params'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'queue'
op|'='
name|'FLAGS'
op|'.'
name|'scheduler_topic'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
string|"'method'"
op|':'
name|'method'
op|','
string|"'args'"
op|':'
name|'params'
op|'}'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'call'
op|'('
name|'context'
op|','
name|'queue'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
name|'class'
name|'API'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the scheduler."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_zone_list
name|'def'
name|'get_zone_list'
op|'('
name|'cls'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of zones assoicated with this zone."""'
newline|'\n'
name|'items'
op|'='
name|'_call_scheduler'
op|'('
string|"'get_zone_list'"
op|','
name|'context'
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'['
string|"'api_url'"
op|']'
op|'='
name|'item'
op|'['
string|"'api_url'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'\\\\/'"
op|','
string|"'/'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'items'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_zone_capabilities
name|'def'
name|'get_zone_capabilities'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a dict of key, value capabilities for this zone,\n           or for a particular class of services running in this zone."""'
newline|'\n'
name|'return'
name|'_call_scheduler'
op|'('
string|"'get_zone_capabilities'"
op|','
name|'context'
op|'='
name|'context'
op|','
nl|'\n'
name|'params'
op|'='
name|'dict'
op|'('
name|'service'
op|'='
name|'service'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|update_service_capabilities
name|'def'
name|'update_service_capabilities'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'service_name'
op|','
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Send an update to all the scheduler services informing them\n           of the capabilities of this service."""'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'method'
op|'='
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'args'
op|'='
name|'dict'
op|'('
name|'service_name'
op|'='
name|'service_name'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|')'
op|')'
newline|'\n'
name|'return'
name|'rpc'
op|'.'
name|'fanout_cast'
op|'('
name|'context'
op|','
string|"'scheduler'"
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_wrap_method
dedent|''
dedent|''
name|'def'
name|'_wrap_method'
op|'('
name|'function'
op|','
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrap method to supply self."""'
newline|'\n'
DECL|function|_wrap
name|'def'
name|'_wrap'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'function'
op|'('
name|'self'
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
name|'_wrap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_process
dedent|''
name|'def'
name|'_process'
op|'('
name|'func'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Worker stub for green thread pool. Give the worker\n    an authenticated nova client and zone info."""'
newline|'\n'
name|'nova'
op|'='
name|'novaclient'
op|'.'
name|'OpenStack'
op|'('
name|'zone'
op|'.'
name|'username'
op|','
name|'zone'
op|'.'
name|'password'
op|','
name|'zone'
op|'.'
name|'api_url'
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'authenticate'
op|'('
op|')'
newline|'\n'
name|'return'
name|'func'
op|'('
name|'nova'
op|','
name|'zone'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|child_zone_helper
dedent|''
name|'def'
name|'child_zone_helper'
op|'('
name|'zone_list'
op|','
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fire off a command to each zone in the list."""'
newline|'\n'
name|'green_pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
op|')'
newline|'\n'
name|'return'
op|'['
name|'result'
name|'for'
name|'result'
name|'in'
name|'green_pool'
op|'.'
name|'imap'
op|'('
nl|'\n'
name|'_wrap_method'
op|'('
name|'_process'
op|','
name|'func'
op|')'
op|','
name|'zone_list'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'def'
name|'_issue_novaclient_command'
op|'('
name|'nova'
op|','
name|'zone'
op|','
name|'collection'
op|','
name|'method_name'
op|','
DECL|function|_issue_novaclient_command
name|'item_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use novaclient to issue command to a single child zone.\n       One of these will be run in parallel for each child zone."""'
newline|'\n'
name|'item'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'getattr'
op|'('
name|'nova'
op|','
name|'collection'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'item_id'
op|','
name|'int'
op|')'
name|'or'
name|'item_id'
op|'.'
name|'isdigit'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'manager'
op|'.'
name|'get'
op|'('
name|'int'
op|'('
name|'item_id'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'manager'
op|'.'
name|'find'
op|'('
name|'name'
op|'='
name|'item_id'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'novaclient'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
name|'zone'
op|'.'
name|'api_url'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(collection)s \'%(item_id)s\' not found on \'%(url)s\'"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'getattr'
op|'('
name|'item'
op|','
name|'method_name'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|wrap_novaclient_function
dedent|''
name|'def'
name|'wrap_novaclient_function'
op|'('
name|'f'
op|','
name|'collection'
op|','
name|'method_name'
op|','
name|'item_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Appends collection, method_name and item_id to the incoming\n    (nova, zone) call from child_zone_helper."""'
newline|'\n'
DECL|function|inner
name|'def'
name|'inner'
op|'('
name|'nova'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'f'
op|'('
name|'nova'
op|','
name|'zone'
op|','
name|'collection'
op|','
name|'method_name'
op|','
name|'item_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'inner'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|reroute_compute
dedent|''
name|'class'
name|'reroute_compute'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator used to indicate that the method should\n       delegate the call the child zones if the db query\n       can\'t find anything."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'method_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'method_name'
op|'='
name|'method_name'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped_f
indent|'        '
name|'def'
name|'wrapped_f'
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
name|'collection'
op|','
name|'context'
op|','
name|'item_id'
op|'='
name|'self'
op|'.'
name|'get_collection_context_and_id'
op|'('
name|'args'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance %(item_id)s not found "'
nl|'\n'
string|'"locally: \'%(e)s\'"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'enable_zone_routing'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'zones'
op|'='
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'zones'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'result'
op|'='
name|'child_zone_helper'
op|'('
name|'zones'
op|','
nl|'\n'
name|'wrap_novaclient_function'
op|'('
name|'_issue_novaclient_command'
op|','
nl|'\n'
name|'collection'
op|','
name|'self'
op|'.'
name|'method_name'
op|','
name|'item_id'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"***REROUTE: %s"'
op|'%'
name|'result'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'unmarshall_result'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapped_f'
newline|'\n'
nl|'\n'
DECL|member|get_collection_context_and_id
dedent|''
name|'def'
name|'get_collection_context_and_id'
op|'('
name|'self'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a tuple of (novaclient collection name, security\n           context and resource id. Derived class should override this."""'
newline|'\n'
name|'return'
op|'('
string|'"servers"'
op|','
name|'args'
op|'['
number|'1'
op|']'
op|','
name|'args'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unmarshall_result
dedent|''
name|'def'
name|'unmarshall_result'
op|'('
name|'self'
op|','
name|'result'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'result'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
