begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2011 Red Hat, Inc.'
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
string|'"""\nA remote procedure call (rpc) abstraction.\n\nFor some wrappers that add message versioning to rpc, see:\n    rpc.dispatcher\n    rpc.proxy\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'local'
newline|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|rpc_opts
name|'rpc_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rpc_backend'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'%s.impl_kombu'"
op|'%'
name|'__package__'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"The messaging module to use, defaults to kombu."'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'rpc_thread_pool_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'64'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Size of RPC thread pool'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'rpc_conn_pool_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'30'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Size of RPC connection pool'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'rpc_response_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds to wait for a response from call or multicall'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'rpc_cast_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'30'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds to wait before a cast expires (TTL). '"
nl|'\n'
string|"'Only supported by impl_zmq.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'allowed_rpc_exception_modules'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.openstack.common.exception'"
op|','
nl|'\n'
string|"'nova.exception'"
op|','
nl|'\n'
string|"'cinder.exception'"
op|','
nl|'\n'
string|"'exceptions'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Modules of exceptions that are permitted to be recreated'"
nl|'\n'
string|"'upon receiving exception data from an rpc call.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'fake_rabbit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If passed, use a fake RabbitMQ provider'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'control_exchange'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'openstack'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'AMQP exchange to connect to if using RabbitMQ or Qpid'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
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
name|'register_opts'
op|'('
name|'rpc_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_defaults
name|'def'
name|'set_defaults'
op|'('
name|'control_exchange'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'cfg'
op|'.'
name|'set_defaults'
op|'('
name|'rpc_opts'
op|','
nl|'\n'
name|'control_exchange'
op|'='
name|'control_exchange'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_connection
dedent|''
name|'def'
name|'create_connection'
op|'('
name|'new'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a connection to the message bus used for rpc.\n\n    For some example usage of creating a connection and some consumers on that\n    connection, see nova.service.\n\n    :param new: Whether or not to create a new connection.  A new connection\n                will be created by default.  If new is False, the\n                implementation is free to return an existing connection from a\n                pool.\n\n    :returns: An instance of openstack.common.rpc.common.Connection\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'create_connection'
op|'('
name|'CONF'
op|','
name|'new'
op|'='
name|'new'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_check_for_lock
dedent|''
name|'def'
name|'_check_for_lock'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'debug'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
op|'('
name|'hasattr'
op|'('
name|'local'
op|'.'
name|'strong_store'
op|','
string|"'locks_held'"
op|')'
nl|'\n'
name|'and'
name|'local'
op|'.'
name|'strong_store'
op|'.'
name|'locks_held'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stack'
op|'='
string|"' :: '"
op|'.'
name|'join'
op|'('
op|'['
name|'frame'
op|'['
number|'3'
op|']'
name|'for'
name|'frame'
name|'in'
name|'inspect'
op|'.'
name|'stack'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'A RPC is being made while holding a lock. The locks '"
nl|'\n'
string|"'currently held are %(locks)s. This is probably a bug. '"
nl|'\n'
string|"'Please report it. Include the following: [%(stack)s].'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'locks'"
op|':'
name|'local'
op|'.'
name|'strong_store'
op|'.'
name|'locks_held'
op|','
nl|'\n'
string|"'stack'"
op|':'
name|'stack'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|call
dedent|''
name|'def'
name|'call'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|','
name|'check_for_lock'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Invoke a remote method that returns something.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  openstack.common.rpc.common.Connection.create_consumer()\n                  and only applies when the consumer was created with\n                  fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n    :param timeout: int, number of seconds to use for a response timeout.\n                    If set, this overrides the rpc_response_timeout option.\n    :param check_for_lock: if True, a warning is emitted if a RPC call is made\n                    with a lock held.\n\n    :returns: A dict from the remote method.\n\n    :raises: openstack.common.rpc.common.Timeout if a complete response\n             is not received before the timeout is reached.\n    """'
newline|'\n'
name|'if'
name|'check_for_lock'
op|':'
newline|'\n'
indent|'        '
name|'_check_for_lock'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'call'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast
dedent|''
name|'def'
name|'cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Invoke a remote method that does not return anything.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  openstack.common.rpc.common.Connection.create_consumer()\n                  and only applies when the consumer was created with\n                  fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'cast'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast
dedent|''
name|'def'
name|'fanout_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Broadcast a remote method invocation with no return.\n\n    This method will get invoked on all consumers that were set up with this\n    topic name and fanout=True.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  openstack.common.rpc.common.Connection.create_consumer()\n                  and only applies when the consumer was created with\n                  fanout=True.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'fanout_cast'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|multicall
dedent|''
name|'def'
name|'multicall'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|'='
name|'None'
op|','
name|'check_for_lock'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Invoke a remote method and get back an iterator.\n\n    In this case, the remote method will be returning multiple values in\n    separate messages, so the return values can be processed as the come in via\n    an iterator.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the rpc message to.  This correlates to the\n                  topic argument of\n                  openstack.common.rpc.common.Connection.create_consumer()\n                  and only applies when the consumer was created with\n                  fanout=False.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n    :param timeout: int, number of seconds to use for a response timeout.\n                    If set, this overrides the rpc_response_timeout option.\n    :param check_for_lock: if True, a warning is emitted if a RPC call is made\n                    with a lock held.\n\n    :returns: An iterator.  The iterator will yield a tuple (N, X) where N is\n              an index that starts at 0 and increases by one for each value\n              returned and X is the Nth value that was returned by the remote\n              method.\n\n    :raises: openstack.common.rpc.common.Timeout if a complete response\n             is not received before the timeout is reached.\n    """'
newline|'\n'
name|'if'
name|'check_for_lock'
op|':'
newline|'\n'
indent|'        '
name|'_check_for_lock'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'multicall'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'envelope'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send notification event.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param topic: The topic to send the notification to.\n    :param msg: This is a dict of content of event.\n    :param envelope: Set to True to enable message envelope for notifications.\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'notify'
op|'('
name|'cfg'
op|'.'
name|'CONF'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|','
name|'envelope'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Clean up resoruces in use by implementation.\n\n    Clean up any resources that have been allocated by the RPC implementation.\n    This is typically open connections to a messaging service.  This function\n    would get called before an application using this API exits to allow\n    connections to get torn down cleanly.\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cast_to_server
dedent|''
name|'def'
name|'cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Invoke a remote method that does not return anything.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param server_params: Connection information\n    :param topic: The topic to send the notification to.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'cast_to_server'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'server_params'
op|','
name|'topic'
op|','
nl|'\n'
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fanout_cast_to_server
dedent|''
name|'def'
name|'fanout_cast_to_server'
op|'('
name|'context'
op|','
name|'server_params'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Broadcast to a remote method invocation with no return.\n\n    :param context: Information that identifies the user that has made this\n                    request.\n    :param server_params: Connection information\n    :param topic: The topic to send the notification to.\n    :param msg: This is a dict in the form { "method" : "method_to_invoke",\n                                             "args" : dict_of_kwargs }\n\n    :returns: None\n    """'
newline|'\n'
name|'return'
name|'_get_impl'
op|'('
op|')'
op|'.'
name|'fanout_cast_to_server'
op|'('
name|'CONF'
op|','
name|'context'
op|','
name|'server_params'
op|','
nl|'\n'
name|'topic'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a queue name for a given topic + host.\n\n    This function only works if this naming convention is followed on the\n    consumer side, as well.  For example, in nova, every instance of the\n    nova-foo service calls create_consumer() for two topics:\n\n        foo\n        foo.<host>\n\n    Messages sent to the \'foo\' topic are distributed to exactly one instance of\n    the nova-foo service.  The services are chosen in a round-robin fashion.\n    Messages sent to the \'foo.<host>\' topic are sent to the nova-foo service on\n    <host>.\n    """'
newline|'\n'
name|'return'
string|"'%s.%s'"
op|'%'
op|'('
name|'topic'
op|','
name|'host'
op|')'
name|'if'
name|'host'
name|'else'
name|'topic'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_RPCIMPL
dedent|''
name|'_RPCIMPL'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_impl
name|'def'
name|'_get_impl'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delay import of rpc_backend until configuration is loaded."""'
newline|'\n'
name|'global'
name|'_RPCIMPL'
newline|'\n'
name|'if'
name|'_RPCIMPL'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'_RPCIMPL'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'CONF'
op|'.'
name|'rpc_backend'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
comment|'# For backwards compatibility with older nova config.'
nl|'\n'
indent|'            '
name|'impl'
op|'='
name|'CONF'
op|'.'
name|'rpc_backend'
op|'.'
name|'replace'
op|'('
string|"'nova.rpc'"
op|','
nl|'\n'
string|"'nova.openstack.common.rpc'"
op|')'
newline|'\n'
name|'_RPCIMPL'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'impl'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'_RPCIMPL'
newline|'\n'
dedent|''
endmarker|''
end_unit
