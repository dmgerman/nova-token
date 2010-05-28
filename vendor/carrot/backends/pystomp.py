begin_unit
name|'from'
name|'stompy'
name|'import'
name|'Client'
newline|'\n'
name|'from'
name|'stompy'
name|'import'
name|'Empty'
name|'as'
name|'QueueEmpty'
newline|'\n'
name|'from'
name|'carrot'
op|'.'
name|'backends'
op|'.'
name|'base'
name|'import'
name|'BaseMessage'
op|','
name|'BaseBackend'
newline|'\n'
name|'from'
name|'itertools'
name|'import'
name|'count'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_PORT
name|'DEFAULT_PORT'
op|'='
number|'61613'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Message
name|'class'
name|'Message'
op|'('
name|'BaseMessage'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A message received by the STOMP broker.\n\n    Usually you don\'t insantiate message objects yourself, but receive\n    them using a :class:`carrot.messaging.Consumer`.\n\n    :param backend: see :attr:`backend`.\n    :param frame: see :attr:`_frame`.\n\n    .. attribute:: body\n\n        The message body.\n\n    .. attribute:: delivery_tag\n\n        The message delivery tag, uniquely identifying this message.\n\n    .. attribute:: backend\n\n        The message backend used.\n        A subclass of :class:`carrot.backends.base.BaseBackend`.\n\n    .. attribute:: _frame\n\n        The frame received by the STOMP client. This is considered a private\n        variable and should never be used in production code.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'backend'
op|','
name|'frame'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_frame'
op|'='
name|'frame'
newline|'\n'
name|'self'
op|'.'
name|'backend'
op|'='
name|'backend'
newline|'\n'
nl|'\n'
name|'kwargs'
op|'['
string|'"body"'
op|']'
op|'='
name|'frame'
op|'.'
name|'body'
newline|'\n'
name|'kwargs'
op|'['
string|'"delivery_tag"'
op|']'
op|'='
name|'frame'
op|'.'
name|'headers'
op|'['
string|'"message-id"'
op|']'
newline|'\n'
name|'kwargs'
op|'['
string|'"content_type"'
op|']'
op|'='
name|'frame'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"content-type"'
op|')'
newline|'\n'
name|'kwargs'
op|'['
string|'"content_encoding"'
op|']'
op|'='
name|'frame'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"content-encoding"'
op|')'
newline|'\n'
name|'kwargs'
op|'['
string|'"priority"'
op|']'
op|'='
name|'frame'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"priority"'
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'Message'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'backend'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ack
dedent|''
name|'def'
name|'ack'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Acknowledge this message as being processed.,\n        This will remove the message from the queue.\n\n        :raises MessageStateError: If the message has already been\n            acknowledged/requeued/rejected.\n\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'acknowledged'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'self'
op|'.'
name|'MessageStateError'
op|'('
nl|'\n'
string|'"Message already acknowledged with state: %s"'
op|'%'
name|'self'
op|'.'
name|'_state'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'backend'
op|'.'
name|'ack'
op|'('
name|'self'
op|'.'
name|'_frame'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_state'
op|'='
string|'"ACK"'
newline|'\n'
nl|'\n'
DECL|member|reject
dedent|''
name|'def'
name|'reject'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
string|'"The STOMP backend does not implement basic.reject"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|requeue
dedent|''
name|'def'
name|'requeue'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
nl|'\n'
string|'"The STOMP backend does not implement requeue"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Backend
dedent|''
dedent|''
name|'class'
name|'Backend'
op|'('
name|'BaseBackend'
op|')'
op|':'
newline|'\n'
DECL|variable|Stomp
indent|'    '
name|'Stomp'
op|'='
name|'Client'
newline|'\n'
DECL|variable|Message
name|'Message'
op|'='
name|'Message'
newline|'\n'
DECL|variable|default_port
name|'default_port'
op|'='
name|'DEFAULT_PORT'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'default_port'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"default_port"'
op|','
name|'self'
op|'.'
name|'default_port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_channel'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_consumers'
op|'='
op|'{'
op|'}'
comment|'# open consumers by consumer tag'
newline|'\n'
name|'self'
op|'.'
name|'_callbacks'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|establish_connection
dedent|''
name|'def'
name|'establish_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conninfo'
op|'='
name|'self'
op|'.'
name|'connection'
newline|'\n'
name|'if'
name|'not'
name|'conninfo'
op|'.'
name|'port'
op|':'
newline|'\n'
indent|'            '
name|'conninfo'
op|'.'
name|'port'
op|'='
name|'self'
op|'.'
name|'default_port'
newline|'\n'
dedent|''
name|'stomp'
op|'='
name|'self'
op|'.'
name|'Stomp'
op|'('
name|'conninfo'
op|'.'
name|'hostname'
op|','
name|'conninfo'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'stomp'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'return'
name|'stomp'
newline|'\n'
nl|'\n'
DECL|member|close_connection
dedent|''
name|'def'
name|'close_connection'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'connection'
op|'.'
name|'disconnect'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|queue_exists
dedent|''
dedent|''
name|'def'
name|'queue_exists'
op|'('
name|'self'
op|','
name|'queue'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|queue_purge
dedent|''
name|'def'
name|'queue_purge'
op|'('
name|'self'
op|','
name|'queue'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'purge_count'
name|'in'
name|'count'
op|'('
number|'0'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'frame'
op|'='
name|'self'
op|'.'
name|'channel'
op|'.'
name|'get_nowait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'QueueEmpty'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'purge_count'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'channel'
op|'.'
name|'ack'
op|'('
name|'frame'
op|')'
newline|'\n'
nl|'\n'
DECL|member|declare_consumer
dedent|''
dedent|''
dedent|''
name|'def'
name|'declare_consumer'
op|'('
name|'self'
op|','
name|'queue'
op|','
name|'no_ack'
op|','
name|'callback'
op|','
name|'consumer_tag'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ack'
op|'='
name|'no_ack'
name|'and'
string|'"auto"'
name|'or'
string|'"client"'
newline|'\n'
name|'self'
op|'.'
name|'channel'
op|'.'
name|'subscribe'
op|'('
name|'queue'
op|','
name|'ack'
op|'='
name|'ack'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_consumers'
op|'['
name|'consumer_tag'
op|']'
op|'='
name|'queue'
newline|'\n'
name|'self'
op|'.'
name|'_callbacks'
op|'['
name|'queue'
op|']'
op|'='
name|'callback'
newline|'\n'
nl|'\n'
DECL|member|consume
dedent|''
name|'def'
name|'consume'
op|'('
name|'self'
op|','
name|'limit'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an iterator that waits for one message at a time."""'
newline|'\n'
name|'for'
name|'total_message_count'
name|'in'
name|'count'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'limit'
name|'and'
name|'total_message_count'
op|'>='
name|'limit'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'StopIteration'
newline|'\n'
dedent|''
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'frame'
op|'='
name|'self'
op|'.'
name|'channel'
op|'.'
name|'get'
op|'('
op|')'
newline|'\n'
name|'if'
name|'frame'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'queue'
op|'='
name|'frame'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|'"destination"'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'queue'
name|'or'
name|'queue'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_callbacks'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_callbacks'
op|'['
name|'queue'
op|']'
op|'('
name|'frame'
op|')'
newline|'\n'
nl|'\n'
name|'yield'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|queue_declare
dedent|''
dedent|''
name|'def'
name|'queue_declare'
op|'('
name|'self'
op|','
name|'queue'
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
name|'channel'
op|'.'
name|'subscribe'
op|'('
name|'queue'
op|','
name|'ack'
op|'='
string|'"client"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'queue'
op|','
name|'no_ack'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'frame'
op|'='
name|'self'
op|'.'
name|'channel'
op|'.'
name|'get_nowait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'QueueEmpty'
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
name|'return'
name|'self'
op|'.'
name|'message_to_python'
op|'('
name|'frame'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ack
dedent|''
dedent|''
name|'def'
name|'ack'
op|'('
name|'self'
op|','
name|'frame'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'channel'
op|'.'
name|'ack'
op|'('
name|'frame'
op|')'
newline|'\n'
nl|'\n'
DECL|member|message_to_python
dedent|''
name|'def'
name|'message_to_python'
op|'('
name|'self'
op|','
name|'raw_message'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert encoded message body back to a Python value."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'Message'
op|'('
name|'backend'
op|'='
name|'self'
op|','
name|'frame'
op|'='
name|'raw_message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prepare_message
dedent|''
name|'def'
name|'prepare_message'
op|'('
name|'self'
op|','
name|'message_data'
op|','
name|'delivery_mode'
op|','
name|'priority'
op|'='
number|'0'
op|','
nl|'\n'
name|'content_type'
op|'='
name|'None'
op|','
name|'content_encoding'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'persistent'
op|'='
string|'"false"'
newline|'\n'
name|'if'
name|'delivery_mode'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'persistent'
op|'='
string|'"true"'
newline|'\n'
dedent|''
name|'priority'
op|'='
name|'priority'
name|'or'
number|'0'
newline|'\n'
name|'return'
op|'{'
string|'"body"'
op|':'
name|'message_data'
op|','
nl|'\n'
string|'"persistent"'
op|':'
name|'persistent'
op|','
nl|'\n'
string|'"priority"'
op|':'
name|'priority'
op|','
nl|'\n'
string|'"content-encoding"'
op|':'
name|'content_encoding'
op|','
nl|'\n'
string|'"content-type"'
op|':'
name|'content_type'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|publish
dedent|''
name|'def'
name|'publish'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'exchange'
op|','
name|'routing_key'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'['
string|'"destination"'
op|']'
op|'='
name|'exchange'
newline|'\n'
name|'self'
op|'.'
name|'channel'
op|'.'
name|'stomp'
op|'.'
name|'send'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cancel
dedent|''
name|'def'
name|'cancel'
op|'('
name|'self'
op|','
name|'consumer_tag'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_channel'
name|'or'
name|'consumer_tag'
name|'not'
name|'in'
name|'self'
op|'.'
name|'_consumers'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'queue'
op|'='
name|'self'
op|'.'
name|'_consumers'
op|'.'
name|'pop'
op|'('
name|'consumer_tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'channel'
op|'.'
name|'unsubscribe'
op|'('
name|'queue'
op|')'
newline|'\n'
nl|'\n'
DECL|member|close
dedent|''
name|'def'
name|'close'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'consumer_tag'
name|'in'
name|'self'
op|'.'
name|'_consumers'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cancel'
op|'('
name|'consumer_tag'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_channel'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_channel'
op|'.'
name|'disconnect'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|channel
name|'def'
name|'channel'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_channel'
op|':'
newline|'\n'
comment|'# Sorry, but the python-stomp library needs one connection'
nl|'\n'
comment|'# for each channel.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_channel'
op|'='
name|'self'
op|'.'
name|'establish_connection'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_channel'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
