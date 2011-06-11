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
name|'stubout'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
name|'import'
name|'notify'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
name|'import'
name|'no_op_notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'notifier'
name|'import'
name|'rabbit_notifier'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NotifierTestCase
name|'class'
name|'NotifierTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test case for notifications"""'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NotifierTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'NotifierTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_notification
dedent|''
name|'def'
name|'test_send_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'notify_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|mock_notify
name|'def'
name|'mock_notify'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'notify_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'no_op_notifier'
op|','
string|"'notify'"
op|','
nl|'\n'
name|'mock_notify'
op|')'
newline|'\n'
nl|'\n'
DECL|class|Mock
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
name|'notify'
op|'('
string|"'publisher_id'"
op|','
string|"'event_type'"
op|','
nl|'\n'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'WARN'
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'notify_called'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_verify_message_format
dedent|''
name|'def'
name|'test_verify_message_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""A test to ensure changing the message format is prohibitively\n        annoying"""'
newline|'\n'
nl|'\n'
DECL|function|message_assert
name|'def'
name|'message_assert'
op|'('
name|'message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fields'
op|'='
op|'['
op|'('
string|"'publisher_id'"
op|','
string|"'publisher_id'"
op|')'
op|','
nl|'\n'
op|'('
string|"'event_type'"
op|','
string|"'event_type'"
op|')'
op|','
nl|'\n'
op|'('
string|"'priority'"
op|','
string|"'WARN'"
op|')'
op|','
nl|'\n'
op|'('
string|"'payload'"
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'fields'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'message'
op|'['
name|'k'
op|']'
op|','
name|'v'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'message'
op|'['
string|"'message_id'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'len'
op|'('
name|'message'
op|'['
string|"'timestamp'"
op|']'
op|')'
op|'>'
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'no_op_notifier'
op|','
string|"'notify'"
op|','
nl|'\n'
name|'message_assert'
op|')'
newline|'\n'
name|'notify'
op|'('
string|"'publisher_id'"
op|','
string|"'event_type'"
op|','
nl|'\n'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'WARN'
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_send_rabbit_notification
dedent|''
name|'def'
name|'test_send_rabbit_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.rabbit_notifier'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mock_cast'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|mock_cast
name|'def'
name|'mock_cast'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mock_cast'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|class|Mock
dedent|''
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'notify'
op|'('
string|"'publisher_id'"
op|','
string|"'event_type'"
op|','
nl|'\n'
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'WARN'
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'mock_cast'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_priority
dedent|''
name|'def'
name|'test_invalid_priority'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|mock_cast
indent|'        '
name|'def'
name|'mock_cast'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|Mock
dedent|''
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'nova'
op|'.'
name|'notifier'
op|'.'
name|'api'
op|'.'
name|'BadPriorityException'
op|','
nl|'\n'
name|'notify'
op|','
string|"'publisher_id'"
op|','
nl|'\n'
string|"'event_type'"
op|','
string|"'not a priority'"
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rabbit_priority_queue
dedent|''
name|'def'
name|'test_rabbit_priority_queue'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.rabbit_notifier'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_topic'"
op|','
nl|'\n'
string|"'testnotify'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'test_topic'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|mock_cast
name|'def'
name|'mock_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'msg'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'test_topic'
op|'='
name|'topic'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'notify'
op|'('
string|"'publisher_id'"
op|','
nl|'\n'
string|"'event_type'"
op|','
string|"'DEBUG'"
op|','
name|'dict'
op|'('
name|'a'
op|'='
number|'3'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'test_topic'
op|','
string|"'testnotify.debug'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_error_notification
dedent|''
name|'def'
name|'test_error_notification'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'notification_driver'"
op|','
nl|'\n'
string|"'nova.notifier.rabbit_notifier'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
op|','
string|"'publish_errors'"
op|','
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'setup_from_flags'
op|'('
op|')'
newline|'\n'
name|'msgs'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|mock_cast
name|'def'
name|'mock_cast'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msgs'
op|'.'
name|'append'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'rpc'
op|','
string|"'cast'"
op|','
name|'mock_cast'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|"'foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'msgs'
op|')'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'msgs'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|'['
string|"'event_type'"
op|']'
op|','
string|"'error_notification'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|'['
string|"'priority'"
op|']'
op|','
string|"'ERROR'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'msg'
op|'['
string|"'payload'"
op|']'
op|'['
string|"'error'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
