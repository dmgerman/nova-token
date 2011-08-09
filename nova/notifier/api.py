begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.exception'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'default_notification_level'"
op|','
string|"'INFO'"
op|','
nl|'\n'
string|"'Default notification level for outgoing notifications'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|WARN
name|'WARN'
op|'='
string|"'WARN'"
newline|'\n'
DECL|variable|INFO
name|'INFO'
op|'='
string|"'INFO'"
newline|'\n'
DECL|variable|ERROR
name|'ERROR'
op|'='
string|"'ERROR'"
newline|'\n'
DECL|variable|CRITICAL
name|'CRITICAL'
op|'='
string|"'CRITICAL'"
newline|'\n'
DECL|variable|DEBUG
name|'DEBUG'
op|'='
string|"'DEBUG'"
newline|'\n'
nl|'\n'
DECL|variable|log_levels
name|'log_levels'
op|'='
op|'('
name|'DEBUG'
op|','
name|'WARN'
op|','
name|'INFO'
op|','
name|'ERROR'
op|','
name|'CRITICAL'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BadPriorityException
name|'class'
name|'BadPriorityException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|publisher_id
dedent|''
name|'def'
name|'publisher_id'
op|'('
name|'service'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'host'
newline|'\n'
dedent|''
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'service'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'publisher_id'
op|','
name|'event_type'
op|','
name|'priority'
op|','
name|'payload'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Sends a notification using the specified driver\n\n    Notify parameters:\n\n    publisher_id - the source worker_type.host of the message\n    event_type - the literal type of event (ex. Instance Creation)\n    priority - patterned after the enumeration of Python logging levels in\n               the set (DEBUG, WARN, INFO, ERROR, CRITICAL)\n    payload - A python dictionary of attributes\n\n    Outgoing message format includes the above parameters, and appends the\n    following:\n\n    message_id - a UUID representing the id for this notification\n    timestamp - the GMT timestamp the notification was sent at\n\n    The composite message will be constructed as a dictionary of the above\n    attributes, which will then be sent via the transport mechanism defined\n    by the driver.\n\n    Message example:\n\n    {\'message_id\': str(uuid.uuid4()),\n     \'publisher_id\': \'compute.host1\',\n     \'timestamp\': utils.utcnow(),\n     \'priority\': \'WARN\',\n     \'event_type\': \'compute.create_instance\',\n     \'payload\': {\'instance_id\': 12, ... }}\n\n    """'
newline|'\n'
name|'if'
name|'priority'
name|'not'
name|'in'
name|'log_levels'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'BadPriorityException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'%s not in valid priorities'"
op|'%'
name|'priority'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Ensure everything is JSON serializable.'
nl|'\n'
dedent|''
name|'payload'
op|'='
name|'utils'
op|'.'
name|'to_primitive'
op|'('
name|'payload'
op|','
name|'convert_instances'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'notification_driver'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'dict'
op|'('
name|'message_id'
op|'='
name|'str'
op|'('
name|'uuid'
op|'.'
name|'uuid4'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'publisher_id'
op|'='
name|'publisher_id'
op|','
nl|'\n'
name|'event_type'
op|'='
name|'event_type'
op|','
nl|'\n'
name|'priority'
op|'='
name|'priority'
op|','
nl|'\n'
name|'payload'
op|'='
name|'payload'
op|','
nl|'\n'
name|'timestamp'
op|'='
name|'str'
op|'('
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'driver'
op|'.'
name|'notify'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Problem \'%(e)s\' attempting to "'
nl|'\n'
string|'"send to notification system."'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
