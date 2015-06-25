begin_unit
comment|'# Copyright 2015 Cloudbase Solutions Srl'
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
name|'eventlet'
newline|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'eventhandler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'utilsfactory'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|EventHandlerTestCase
name|'class'
name|'EventHandlerTestCase'
op|'('
name|'test_base'
op|'.'
name|'HyperVBaseTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|_FAKE_POLLING_INTERVAL
indent|'    '
name|'_FAKE_POLLING_INTERVAL'
op|'='
number|'3'
newline|'\n'
DECL|variable|_FAKE_EVENT_CHECK_TIMEFRAME
name|'_FAKE_EVENT_CHECK_TIMEFRAME'
op|'='
number|'15'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utilsfactory'
op|','
string|"'get_vmutils'"
op|')'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|','
name|'mock_get_vmutils'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'EventHandlerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_state_change_callback'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_running_state_callback'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'power_state_check_timeframe'
op|'='
name|'self'
op|'.'
name|'_FAKE_EVENT_CHECK_TIMEFRAME'
op|','
nl|'\n'
name|'group'
op|'='
string|"'hyperv'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'power_state_event_polling_interval'
op|'='
name|'self'
op|'.'
name|'_FAKE_POLLING_INTERVAL'
op|','
nl|'\n'
name|'group'
op|'='
string|"'hyperv'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_event_handler'
op|'='
name|'eventhandler'
op|'.'
name|'InstanceEventHandler'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_state_change_callback'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_running_state_callback'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventhandler'
op|','
string|"'wmi'"
op|','
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventhandler'
op|'.'
name|'InstanceEventHandler'
op|','
string|"'_dispatch_event'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventlet'
op|','
string|"'sleep'"
op|')'
newline|'\n'
DECL|member|_test_poll_events
name|'def'
name|'_test_poll_events'
op|'('
name|'self'
op|','
name|'mock_sleep'
op|','
name|'mock_dispatch'
op|','
nl|'\n'
name|'mock_wmi'
op|','
name|'event_found'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_listener'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_wmi'
op|'.'
name|'x_wmi_timed_out'
op|'='
name|'Exception'
newline|'\n'
name|'fake_listener'
op|'.'
name|'side_effect'
op|'='
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'event'
name|'if'
name|'event_found'
nl|'\n'
name|'else'
name|'mock_wmi'
op|'.'
name|'x_wmi_timed_out'
op|','
nl|'\n'
name|'KeyboardInterrupt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_listener'
op|'='
name|'fake_listener'
newline|'\n'
nl|'\n'
comment|"# This is supposed to run as a daemon, so we'll just cause an exception"
nl|'\n'
comment|'# in order to be able to test the method.'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'KeyboardInterrupt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_poll_events'
op|')'
newline|'\n'
name|'if'
name|'event_found'
op|':'
newline|'\n'
indent|'            '
name|'mock_dispatch'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'event'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mock_sleep'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'_FAKE_POLLING_INTERVAL'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_poll_having_events
dedent|''
dedent|''
name|'def'
name|'test_poll_having_events'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test case in which events were found in the checked interval'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_poll_events'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_poll_no_event_found
dedent|''
name|'def'
name|'test_poll_no_event_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_poll_events'
op|'('
name|'event_found'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventhandler'
op|'.'
name|'InstanceEventHandler'
op|','
nl|'\n'
string|"'_get_instance_uuid'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventhandler'
op|'.'
name|'InstanceEventHandler'
op|','
string|"'_emit_event'"
op|')'
newline|'\n'
DECL|member|_test_dispatch_event
name|'def'
name|'_test_dispatch_event'
op|'('
name|'self'
op|','
name|'mock_emit_event'
op|','
name|'mock_get_uuid'
op|','
nl|'\n'
name|'missing_uuid'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_get_uuid'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
name|'if'
name|'not'
name|'missing_uuid'
name|'else'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_vmutils'
op|'.'
name|'get_vm_power_state'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'power_state'
op|')'
newline|'\n'
nl|'\n'
name|'event'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'event'
op|'.'
name|'ElementName'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_name'
newline|'\n'
name|'event'
op|'.'
name|'EnabledState'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'enabled_state'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_dispatch_event'
op|'('
name|'event'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'missing_uuid'
op|':'
newline|'\n'
indent|'            '
name|'mock_emit_event'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'power_state'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_emit_event'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dispatch_event_new_final_state
dedent|''
dedent|''
name|'def'
name|'test_dispatch_event_new_final_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_dispatch_event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dispatch_event_missing_uuid
dedent|''
name|'def'
name|'test_dispatch_event_missing_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_dispatch_event'
op|'('
name|'missing_uuid'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'eventhandler'
op|'.'
name|'InstanceEventHandler'
op|','
string|"'_get_virt_event'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'spawn_n'"
op|')'
newline|'\n'
DECL|member|test_emit_event
name|'def'
name|'test_emit_event'
op|'('
name|'self'
op|','
name|'mock_spawn'
op|','
name|'mock_get_event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_emit_event'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
op|')'
newline|'\n'
nl|'\n'
name|'virt_event'
op|'='
name|'mock_get_event'
op|'.'
name|'return_value'
newline|'\n'
name|'mock_spawn'
op|'.'
name|'assert_has_calls'
op|'('
nl|'\n'
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'_state_change_callback'
op|','
name|'virt_event'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'self'
op|'.'
name|'_running_state_callback'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_name'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_get_instance_uuid
dedent|''
name|'def'
name|'_test_get_instance_uuid'
op|'('
name|'self'
op|','
name|'instance_found'
op|'='
name|'True'
op|','
nl|'\n'
name|'missing_uuid'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'instance_found'
op|':'
newline|'\n'
indent|'            '
name|'side_effect'
op|'='
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
nl|'\n'
name|'if'
name|'not'
name|'missing_uuid'
name|'else'
name|'None'
op|','
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
name|'mock_get_uuid'
op|'='
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_vmutils'
op|'.'
name|'get_instance_uuid'
newline|'\n'
name|'mock_get_uuid'
op|'.'
name|'side_effect'
op|'='
name|'side_effect'
newline|'\n'
nl|'\n'
name|'instance_uuid'
op|'='
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_get_instance_uuid'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'expected_uuid'
op|'='
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
nl|'\n'
name|'if'
name|'instance_found'
name|'and'
name|'not'
name|'missing_uuid'
name|'else'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_uuid'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_nova_created_instance_uuid
dedent|''
name|'def'
name|'test_get_nova_created_instance_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_get_instance_uuid'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_deleted_instance_uuid
dedent|''
name|'def'
name|'test_get_deleted_instance_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_get_instance_uuid'
op|'('
name|'instance_found'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_uuid_missing_notes
dedent|''
name|'def'
name|'test_get_instance_uuid_missing_notes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_get_instance_uuid'
op|'('
name|'missing_uuid'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.event.LifecycleEvent'"
op|')'
newline|'\n'
DECL|member|test_get_virt_event
name|'def'
name|'test_get_virt_event'
op|'('
name|'self'
op|','
name|'mock_lifecycle_event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_state'
op|'='
name|'constants'
op|'.'
name|'HYPERV_VM_STATE_ENABLED'
newline|'\n'
name|'expected_transition'
op|'='
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_TRANSITION_MAP'
op|'['
nl|'\n'
name|'instance_state'
op|']'
newline|'\n'
nl|'\n'
name|'virt_event'
op|'='
name|'self'
op|'.'
name|'_event_handler'
op|'.'
name|'_get_virt_event'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|','
name|'instance_state'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'mock_lifecycle_event'
op|'.'
name|'return_value'
op|','
nl|'\n'
name|'virt_event'
op|')'
newline|'\n'
name|'mock_lifecycle_event'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'uuid'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'instance_uuid'
op|','
nl|'\n'
name|'transition'
op|'='
name|'expected_transition'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
