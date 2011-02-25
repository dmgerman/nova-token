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
string|'"""\nAMQP-based RPC. Queues have consumers and publishers.\nNo fan-out support yet.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'traceback'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'carrot'
name|'import'
name|'connection'
name|'as'
name|'carrot_connection'
newline|'\n'
name|'from'
name|'carrot'
name|'import'
name|'messaging'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenpool'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'fakerabbit'
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
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.rpc'"
op|')'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'rpc_thread_pool_size'"
op|','
number|'1024'
op|','
string|"'Size of RPC thread pool'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Connection
name|'class'
name|'Connection'
op|'('
name|'carrot_connection'
op|'.'
name|'BrokerConnection'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Connection instance object"""'
newline|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|','
name|'new'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the instance"""'
newline|'\n'
name|'if'
name|'new'
name|'or'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'='
name|'dict'
op|'('
name|'hostname'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_host'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_port'
op|','
nl|'\n'
name|'userid'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_userid'
op|','
nl|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_password'
op|','
nl|'\n'
name|'virtual_host'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_virtual_host'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'fake_rabbit'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'['
string|"'backend_cls'"
op|']'
op|'='
name|'fakerabbit'
op|'.'
name|'Backend'
newline|'\n'
nl|'\n'
comment|'# NOTE(vish): magic is fun!'
nl|'\n'
comment|'# pylint: disable-msg=W0142'
nl|'\n'
dedent|''
name|'if'
name|'new'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'cls'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|recreate
name|'def'
name|'recreate'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recreates the connection instance\n\n        This is necessary to recover from some network errors/disconnects"""'
newline|'\n'
name|'del'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Consumer
dedent|''
dedent|''
name|'class'
name|'Consumer'
op|'('
name|'messaging'
op|'.'
name|'Consumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumer base class\n\n    Contains methods for connecting the fetch method to async loops\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'rabbit_max_retries'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'i'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
name|'FLAGS'
op|'.'
name|'rabbit_retry_interval'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'super'
op|'('
name|'Consumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failed_connection'
op|'='
name|'False'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
comment|'# Catching all because carrot sucks'
newline|'\n'
indent|'                '
name|'fl_host'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_host'
newline|'\n'
name|'fl_port'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_port'
newline|'\n'
name|'fl_intv'
op|'='
name|'FLAGS'
op|'.'
name|'rabbit_retry_interval'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"AMQP server on %(fl_host)s:%(fl_port)d is"'
nl|'\n'
string|'" unreachable: %(e)s. Trying again in %(fl_intv)d"'
nl|'\n'
string|'" seconds."'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failed_connection'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'failed_connection'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Unable to connect to AMQP server "'
nl|'\n'
string|'"after %d tries. Shutting down."'
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'rabbit_max_retries'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch
dedent|''
dedent|''
name|'def'
name|'fetch'
op|'('
name|'self'
op|','
name|'no_ack'
op|'='
name|'None'
op|','
name|'auto_ack'
op|'='
name|'None'
op|','
name|'enable_callbacks'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Wraps the parent fetch with some logic for failed connections"""'
newline|'\n'
comment|'# TODO(vish): the logic for failed connections and logging should be'
nl|'\n'
comment|'#             refactored into some sort of connection manager object'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'failed_connection'
op|':'
newline|'\n'
comment|'# NOTE(vish): connection is defined in the parent class, we can'
nl|'\n'
comment|'#             recreate it as long as we create the backend too'
nl|'\n'
comment|'# pylint: disable-msg=W0201'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'connection'
op|'='
name|'Connection'
op|'.'
name|'recreate'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backend'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'create_backend'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'declare'
op|'('
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'Consumer'
op|','
name|'self'
op|')'
op|'.'
name|'fetch'
op|'('
name|'no_ack'
op|','
name|'auto_ack'
op|','
name|'enable_callbacks'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'failed_connection'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Reconnected to queue"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failed_connection'
op|'='
name|'False'
newline|'\n'
comment|"# NOTE(vish): This is catching all errors because we really don't"
nl|'\n'
comment|'#             want exceptions to be logged 10 times a second if some'
nl|'\n'
comment|'#             persistent failure occurs.'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
comment|'# pylint: disable-msg=W0703'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'failed_connection'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Failed to fetch message from queue"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'failed_connection'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|attach_to_eventlet
dedent|''
dedent|''
dedent|''
name|'def'
name|'attach_to_eventlet'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Only needed for unit tests!"""'
newline|'\n'
name|'timer'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'fetch'
op|','
name|'enable_callbacks'
op|'='
name|'True'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
number|'0.1'
op|')'
newline|'\n'
name|'return'
name|'timer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdapterConsumer
dedent|''
dedent|''
name|'class'
name|'AdapterConsumer'
op|'('
name|'Consumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Calls methods on a proxy object based on method and args"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|','
name|'proxy'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Initing the Adapter Consumer for %s'"
op|')'
op|'%'
name|'topic'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'proxy'
op|'='
name|'proxy'
newline|'\n'
name|'self'
op|'.'
name|'pool'
op|'='
name|'greenpool'
op|'.'
name|'GreenPool'
op|'('
name|'FLAGS'
op|'.'
name|'rpc_thread_pool_size'
op|')'
newline|'\n'
name|'super'
op|'('
name|'AdapterConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
nl|'\n'
DECL|member|receive
dedent|''
name|'def'
name|'receive'
op|'('
name|'self'
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
name|'self'
op|'.'
name|'pool'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_receive'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
newline|'\n'
DECL|member|_receive
name|'def'
name|'_receive'
op|'('
name|'self'
op|','
name|'message_data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Magically looks for a method on the proxy object and calls it\n\n        Message data should be a dictionary with two keys:\n            method: string representing the method to call\n            args: dictionary of arg: value\n\n        Example: {\'method\': \'echo\', \'args\': {\'value\': 42}}\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'received %s'"
op|')'
op|'%'
name|'message_data'
op|')'
newline|'\n'
name|'msg_id'
op|'='
name|'message_data'
op|'.'
name|'pop'
op|'('
string|"'_msg_id'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'_unpack_context'
op|'('
name|'message_data'
op|')'
newline|'\n'
nl|'\n'
name|'method'
op|'='
name|'message_data'
op|'.'
name|'get'
op|'('
string|"'method'"
op|')'
newline|'\n'
name|'args'
op|'='
name|'message_data'
op|'.'
name|'get'
op|'('
string|"'args'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'message'
op|'.'
name|'ack'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'method'
op|':'
newline|'\n'
comment|'# NOTE(vish): we may not want to ack here, but that means that bad'
nl|'\n'
comment|'#             messages stay in the queue indefinitely, so for now'
nl|'\n'
comment|'#             we just log the message and send an error string'
nl|'\n'
comment|'#             back to the caller'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'no method for message: %s'"
op|')'
op|'%'
name|'message_data'
op|')'
newline|'\n'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'_'
op|'('
string|"'No method for message: %s'"
op|')'
op|'%'
name|'message_data'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'node_func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'proxy'
op|','
name|'str'
op|'('
name|'method'
op|')'
op|')'
newline|'\n'
name|'node_args'
op|'='
name|'dict'
op|'('
op|'('
name|'str'
op|'('
name|'k'
op|')'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'args'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# NOTE(vish): magic is fun!'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'rval'
op|'='
name|'node_func'
op|'('
name|'context'
op|'='
name|'ctxt'
op|','
op|'**'
name|'node_args'
op|')'
newline|'\n'
name|'if'
name|'msg_id'
op|':'
newline|'\n'
indent|'                '
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'rval'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"Exception during message handling"'
op|')'
newline|'\n'
name|'if'
name|'msg_id'
op|':'
newline|'\n'
indent|'                '
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'None'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Publisher
dedent|''
dedent|''
name|'class'
name|'Publisher'
op|'('
name|'messaging'
op|'.'
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publisher base class"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicAdapterConsumer
dedent|''
name|'class'
name|'TopicAdapterConsumer'
op|'('
name|'AdapterConsumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumes messages on a specific topic"""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"topic"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|','
name|'proxy'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'queue'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'FLAGS'
op|'.'
name|'control_exchange'
newline|'\n'
name|'self'
op|'.'
name|'durable'
op|'='
name|'False'
newline|'\n'
name|'super'
op|'('
name|'TopicAdapterConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
name|'proxy'
op|'='
name|'proxy'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutAdapterConsumer
dedent|''
dedent|''
name|'class'
name|'FanoutAdapterConsumer'
op|'('
name|'AdapterConsumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumes messages from a fanout exchange"""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"fanout"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|','
name|'proxy'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exchange'
op|'='
string|'"%s_fanout"'
op|'%'
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'topic'
newline|'\n'
name|'unique'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'self'
op|'.'
name|'queue'
op|'='
string|'"%s_fanout_%s"'
op|'%'
op|'('
name|'topic'
op|','
name|'unique'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'durable'
op|'='
name|'False'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Created \'%(exchange)s\' fanout exchange "'
nl|'\n'
string|'"with \'%(key)s\' routing key"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'exchange'
op|'='
name|'self'
op|'.'
name|'exchange'
op|','
name|'key'
op|'='
name|'self'
op|'.'
name|'routing_key'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'FanoutAdapterConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
name|'proxy'
op|'='
name|'proxy'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TopicPublisher
dedent|''
dedent|''
name|'class'
name|'TopicPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publishes messages on a specific topic"""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"topic"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'topic'
op|'='
string|'"broadcast"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'FLAGS'
op|'.'
name|'control_exchange'
newline|'\n'
name|'self'
op|'.'
name|'durable'
op|'='
name|'False'
newline|'\n'
name|'super'
op|'('
name|'TopicPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FanoutPublisher
dedent|''
dedent|''
name|'class'
name|'FanoutPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publishes messages to a fanout exchange."""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"fanout"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|','
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exchange'
op|'='
string|'"%s_fanout"'
op|'%'
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'queue'
op|'='
string|'"%s_fanout"'
op|'%'
name|'topic'
newline|'\n'
name|'self'
op|'.'
name|'durable'
op|'='
name|'False'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Writing to \'%(exchange)s\' fanout exchange"'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'exchange'
op|'='
name|'self'
op|'.'
name|'exchange'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'FanoutPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectConsumer
dedent|''
dedent|''
name|'class'
name|'DirectConsumer'
op|'('
name|'Consumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Consumes messages directly on a channel specified by msg_id"""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"direct"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'msg_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'queue'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'auto_delete'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'exclusive'
op|'='
name|'True'
newline|'\n'
name|'super'
op|'('
name|'DirectConsumer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectPublisher
dedent|''
dedent|''
name|'class'
name|'DirectPublisher'
op|'('
name|'Publisher'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Publishes messages directly on a channel specified by msg_id"""'
newline|'\n'
DECL|variable|exchange_type
name|'exchange_type'
op|'='
string|'"direct"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'msg_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'routing_key'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'exchange'
op|'='
name|'msg_id'
newline|'\n'
name|'self'
op|'.'
name|'auto_delete'
op|'='
name|'True'
newline|'\n'
name|'super'
op|'('
name|'DirectPublisher'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|'='
name|'connection'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|msg_reply
dedent|''
dedent|''
name|'def'
name|'msg_reply'
op|'('
name|'msg_id'
op|','
name|'reply'
op|'='
name|'None'
op|','
name|'failure'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a reply or an error on the channel signified by msg_id\n\n    failure should be a sys.exc_info() tuple.\n\n    """'
newline|'\n'
name|'if'
name|'failure'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'='
name|'str'
op|'('
name|'failure'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'tb'
op|'='
name|'traceback'
op|'.'
name|'format_exception'
op|'('
op|'*'
name|'failure'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Returning exception %s to caller"'
op|')'
op|','
name|'message'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'tb'
op|')'
newline|'\n'
name|'failure'
op|'='
op|'('
name|'failure'
op|'['
number|'0'
op|']'
op|'.'
name|'__name__'
op|','
name|'str'
op|'('
name|'failure'
op|'['
number|'1'
op|']'
op|')'
op|','
name|'tb'
op|')'
newline|'\n'
dedent|''
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'DirectPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'msg_id'
op|'='
name|'msg_id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'publisher'
op|'.'
name|'send'
op|'('
op|'{'
string|"'result'"
op|':'
name|'reply'
op|','
string|"'failure'"
op|':'
name|'failure'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'publisher'
op|'.'
name|'send'
op|'('
nl|'\n'
op|'{'
string|"'result'"
op|':'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'repr'
op|'('
name|'v'
op|')'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'reply'
op|'.'
name|'__dict__'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'failure'"
op|':'
name|'failure'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteError
dedent|''
name|'class'
name|'RemoteError'
op|'('
name|'exception'
op|'.'
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Signifies that a remote class has raised an exception\n\n    Containes a string representation of the type of the original exception,\n    the value of the original exception, and the traceback.  These are\n    sent to the parent as a joined string so printing the exception\n    contains all of the relevent info."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'exc_type'
op|','
name|'value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exc_type'
op|'='
name|'exc_type'
newline|'\n'
name|'self'
op|'.'
name|'value'
op|'='
name|'value'
newline|'\n'
name|'self'
op|'.'
name|'traceback'
op|'='
name|'traceback'
newline|'\n'
name|'super'
op|'('
name|'RemoteError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
string|'"%s %s\\n%s"'
op|'%'
op|'('
name|'exc_type'
op|','
nl|'\n'
name|'value'
op|','
nl|'\n'
name|'traceback'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unpack_context
dedent|''
dedent|''
name|'def'
name|'_unpack_context'
op|'('
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unpack context from msg."""'
newline|'\n'
name|'context_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'list'
op|'('
name|'msg'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(vish): Some versions of python don't like unicode keys"
nl|'\n'
comment|'#             in kwargs.'
nl|'\n'
indent|'        '
name|'key'
op|'='
name|'str'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'key'
op|'.'
name|'startswith'
op|'('
string|"'_context_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'msg'
op|'.'
name|'pop'
op|'('
name|'key'
op|')'
newline|'\n'
name|'context_dict'
op|'['
name|'key'
op|'['
number|'9'
op|':'
op|']'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'unpacked context: %s'"
op|')'
op|','
name|'context_dict'
op|')'
newline|'\n'
name|'return'
name|'context'
op|'.'
name|'RequestContext'
op|'.'
name|'from_dict'
op|'('
name|'context_dict'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_pack_context
dedent|''
name|'def'
name|'_pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pack context into msg.\n\n    Values for message keys need to be less than 255 chars, so we pull\n    context out into a bunch of separate keys. If we want to support\n    more arguments in rabbit messages, we may want to do the same\n    for args at some point.\n    """'
newline|'\n'
name|'context'
op|'='
name|'dict'
op|'('
op|'['
op|'('
string|"'_context_%s'"
op|'%'
name|'key'
op|','
name|'value'
op|')'
nl|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'context'
op|'.'
name|'to_dict'
op|'('
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'msg'
op|'.'
name|'update'
op|'('
name|'context'
op|')'
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
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message on a topic and wait for a response"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Making asynchronous call..."'
op|')'
op|')'
newline|'\n'
name|'msg_id'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'msg'
op|'.'
name|'update'
op|'('
op|'{'
string|"'_msg_id'"
op|':'
name|'msg_id'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"MSG_ID is %s"'
op|')'
op|'%'
op|'('
name|'msg_id'
op|')'
op|')'
newline|'\n'
name|'_pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|class|WaitMessage
name|'class'
name|'WaitMessage'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__call__
indent|'        '
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Acks message and sets result."""'
newline|'\n'
name|'message'
op|'.'
name|'ack'
op|'('
op|')'
newline|'\n'
name|'if'
name|'data'
op|'['
string|"'failure'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'result'
op|'='
name|'RemoteError'
op|'('
op|'*'
name|'data'
op|'['
string|"'failure'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'result'
op|'='
name|'data'
op|'['
string|"'result'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'wait_msg'
op|'='
name|'WaitMessage'
op|'('
op|')'
newline|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'consumer'
op|'='
name|'DirectConsumer'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'msg_id'
op|'='
name|'msg_id'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
name|'wait_msg'
op|')'
newline|'\n'
nl|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'TopicPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'.'
name|'wait'
op|'('
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'consumer'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
comment|'# NOTE(termie): this is a little bit of a change from the original'
nl|'\n'
comment|'#               non-eventlet code where returning a Failure'
nl|'\n'
comment|'#               instance from a deferred call is very similar to'
nl|'\n'
comment|'#               raising an exception'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'wait_msg'
op|'.'
name|'result'
op|','
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'wait_msg'
op|'.'
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'wait_msg'
op|'.'
name|'result'
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
string|'"""Sends a message on a topic without waiting for a response"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Making asynchronous cast..."'
op|')'
op|')'
newline|'\n'
name|'_pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'TopicPublisher'
op|'('
name|'connection'
op|'='
name|'conn'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
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
string|'"""Sends a message on a fanout exchange without waiting for a response"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Making asynchronous fanout cast..."'
op|')'
op|')'
newline|'\n'
name|'_pack_context'
op|'('
name|'msg'
op|','
name|'context'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'publisher'
op|'='
name|'FanoutPublisher'
op|'('
name|'topic'
op|','
name|'connection'
op|'='
name|'conn'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generic_response
dedent|''
name|'def'
name|'generic_response'
op|'('
name|'message_data'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Logs a result and exits"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'response %s'"
op|')'
op|','
name|'message_data'
op|')'
newline|'\n'
name|'message'
op|'.'
name|'ack'
op|'('
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_message
dedent|''
name|'def'
name|'send_message'
op|'('
name|'topic'
op|','
name|'message'
op|','
name|'wait'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a message for testing"""'
newline|'\n'
name|'msg_id'
op|'='
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|'.'
name|'hex'
newline|'\n'
name|'message'
op|'.'
name|'update'
op|'('
op|'{'
string|"'_msg_id'"
op|':'
name|'msg_id'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'topic is %s'"
op|')'
op|','
name|'topic'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'message %s'"
op|')'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'wait'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'='
name|'messaging'
op|'.'
name|'Consumer'
op|'('
name|'connection'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
op|','
nl|'\n'
name|'queue'
op|'='
name|'msg_id'
op|','
nl|'\n'
name|'exchange'
op|'='
name|'msg_id'
op|','
nl|'\n'
name|'auto_delete'
op|'='
name|'True'
op|','
nl|'\n'
name|'exchange_type'
op|'='
string|'"direct"'
op|','
nl|'\n'
name|'routing_key'
op|'='
name|'msg_id'
op|')'
newline|'\n'
name|'consumer'
op|'.'
name|'register_callback'
op|'('
name|'generic_response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'publisher'
op|'='
name|'messaging'
op|'.'
name|'Publisher'
op|'('
name|'connection'
op|'='
name|'Connection'
op|'.'
name|'instance'
op|'('
op|')'
op|','
nl|'\n'
name|'exchange'
op|'='
name|'FLAGS'
op|'.'
name|'control_exchange'
op|','
nl|'\n'
name|'durable'
op|'='
name|'False'
op|','
nl|'\n'
name|'exchange_type'
op|'='
string|'"topic"'
op|','
nl|'\n'
name|'routing_key'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'send'
op|'('
name|'message'
op|')'
newline|'\n'
name|'publisher'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'wait'
op|':'
newline|'\n'
indent|'        '
name|'consumer'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
comment|'# NOTE(vish): you can send messages from the command line using'
nl|'\n'
comment|'#             topic and a json sting representing a dictionary'
nl|'\n'
comment|'#             for the method'
nl|'\n'
indent|'    '
name|'send_message'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|']'
op|','
name|'json'
op|'.'
name|'loads'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'2'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
