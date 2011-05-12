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
DECL|function|get_zone_list
dedent|''
name|'def'
name|'get_zone_list'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
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
indent|'        '
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
name|'if'
name|'not'
name|'items'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'db'
op|'.'
name|'zone_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'items'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_get
dedent|''
name|'def'
name|'zone_get'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'zone_get'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_delete
dedent|''
name|'def'
name|'zone_delete'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'zone_delete'
op|'('
name|'context'
op|','
name|'zone_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_create
dedent|''
name|'def'
name|'zone_create'
op|'('
name|'context'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'zone_create'
op|'('
name|'context'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|zone_update
dedent|''
name|'def'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'db'
op|'.'
name|'zone_update'
op|'('
name|'context'
op|','
name|'zone_id'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_zone_capabilities
dedent|''
name|'def'
name|'get_zone_capabilities'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a dict of key, value capabilities for this zone."""'
newline|'\n'
name|'return'
name|'_call_scheduler'
op|'('
string|"'get_zone_capabilities'"
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'context'
op|','
name|'service_name'
op|','
name|'host'
op|','
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send an update to all the scheduler services informing them\n       of the capabilities of this service."""'
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
string|'"""Fire off a command to each zone in the list.\n    The return is [novaclient return objects] from each child zone.\n    For example, if you are calling server.pause(), the list will\n    be whatever the response from server.pause() is. One entry\n    per child zone called."""'
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
DECL|function|_issue_novaclient_command
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
name|'item_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Use novaclient to issue command to a single child zone.\n       One of these will be run in parallel for each child zone."""'
newline|'\n'
name|'manager'
op|'='
name|'getattr'
op|'('
name|'nova'
op|','
name|'collection'
op|')'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
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
name|'except'
name|'ValueError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'result'
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
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'method_name'
op|'.'
name|'lower'
op|'('
op|')'
name|'not'
name|'in'
op|'['
string|"'get'"
op|','
string|"'find'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'getattr'
op|'('
name|'result'
op|','
name|'method_name'
op|')'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
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
DECL|class|RedirectResult
dedent|''
name|'class'
name|'RedirectResult'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to the HTTP API know that these results are pre-cooked\n    and they can be returned to the caller directly."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'results'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'results'
op|'='
name|'results'
newline|'\n'
name|'super'
op|'('
name|'RedirectResult'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
nl|'\n'
name|'message'
op|'='
name|'_'
op|'('
string|'"Uncaught Zone redirection exception"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|reroute_compute
dedent|''
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
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Call the original function ...'
nl|'\n'
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
comment|'# Ask the children to provide an answer ...'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Asking child zones ..."'
op|')'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_call_child_zones'
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
comment|'# Scrub the results and raise another exception'
nl|'\n'
comment|'# so the API layers can bail out gracefully ...'
nl|'\n'
name|'raise'
name|'RedirectResult'
op|'('
name|'self'
op|'.'
name|'unmarshall_result'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapped_f'
newline|'\n'
nl|'\n'
DECL|member|_call_child_zones
dedent|''
name|'def'
name|'_call_child_zones'
op|'('
name|'self'
op|','
name|'zones'
op|','
name|'function'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ask the child zones to perform this operation.\n        Broken out for testing."""'
newline|'\n'
name|'return'
name|'child_zone_helper'
op|'('
name|'zones'
op|','
name|'function'
op|')'
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
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a tuple of (novaclient collection name, security\n           context and resource id. Derived class should override this."""'
newline|'\n'
name|'context'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
name|'instance_id'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'instance_id'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'>'
number|'0'
name|'and'
name|'not'
name|'context'
op|':'
newline|'\n'
indent|'            '
name|'context'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'>'
number|'1'
name|'and'
name|'not'
name|'instance_id'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'args'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'('
string|'"servers"'
op|','
name|'context'
op|','
name|'instance_id'
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
name|'zone_responses'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Result is a list of responses from each child zone.\n        Each decorator derivation is responsible to turning this\n        into a format expected by the calling method. For\n        example, this one is expected to return a single Server\n        dict {\'server\':{k:v}}. Others may return a list of them, like\n        {\'servers\':[{k,v}]}"""'
newline|'\n'
name|'reduced_response'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'zone_response'
name|'in'
name|'zone_responses'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'zone_response'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'server'
op|'='
name|'zone_response'
op|'.'
name|'__dict__'
newline|'\n'
nl|'\n'
name|'for'
name|'k'
name|'in'
name|'server'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'k'
op|'['
number|'0'
op|']'
op|'=='
string|"'_'"
name|'or'
name|'k'
op|'=='
string|"'manager'"
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'server'
op|'['
name|'k'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'reduced_response'
op|'.'
name|'append'
op|'('
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'reduced_response'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'reduced_response'
op|'['
number|'0'
op|']'
comment|'# first for now.'
newline|'\n'
dedent|''
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|redirect_handler
dedent|''
dedent|''
name|'def'
name|'redirect_handler'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|new_f
indent|'    '
name|'def'
name|'new_f'
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
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'RedirectResult'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'e'
op|'.'
name|'results'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'new_f'
newline|'\n'
dedent|''
endmarker|''
end_unit
