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
comment|'#    under the License.import datetime'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
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
DECL|function|notify
dedent|''
name|'def'
name|'notify'
op|'('
name|'event_name'
op|','
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
string|'"""\n    Sends a notification using the specified driver\n\n    Message format is as follows:\n\n    message_id - a UUID representing the id for this notification\n    publisher_id - the source worker_type.host of the message\n    timestamp - the GMT timestamp the notification was sent at\n    event_type - the literal type of event (ex. Instance Creation)\n    priority - patterned after the enumeration of Python logging levels in\n               the set (DEBUG, WARN, INFO, ERROR, CRITICAL)\n    payload - A python dictionary of attributes\n\n    The message body will be constructed as a dictionary of the above\n    attributes, and converted into a JSON dump, which will then be sent\n    via the transport mechanism defined by the driver.\n\n    Message example:\n\n    {\'message_id\': str(uuid.uuid4()),\n     \'publisher_id\': \'compute.host1\',\n     \'timestamp\': datetime.datetime.utcnow(),\n     \'priority\': \'WARN\',\n     \'event_type\': \'compute.create_instance\',\n     \'payload\': {\'instance_id\': 12, ... }}\n\n    """'
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
string|"'%s not in valid priorities'"
op|'%'
name|'priority'
op|')'
newline|'\n'
dedent|''
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_class'
op|'('
name|'FLAGS'
op|'.'
name|'notification_driver'
op|')'
op|'('
op|')'
newline|'\n'
name|'message'
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
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'notify'
op|'('
name|'message'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
