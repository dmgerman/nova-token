begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""Functionality related to notifications common to multiple layers of\nthe system.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_context'
name|'import'
name|'context'
name|'as'
name|'common_context'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
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
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|notify_opts
name|'notify_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'notify_on_state_change'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If set, send compute.instance.update notifications on instance '"
nl|'\n'
string|"'state changes.  Valid values are None for no notifications, '"
nl|'\n'
string|'\'"vm_state" for notifications on VM state changes, or \''
nl|'\n'
string|'\'"vm_and_task_state" for notifications on VM and task state \''
nl|'\n'
string|"'changes.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'notify_api_faults'"
op|','
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'If set, send api.fault notifications on caught exceptions '"
nl|'\n'
string|"'in the API service.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_notification_level'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'INFO'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'DEBUG'"
op|','
string|"'INFO'"
op|','
string|"'WARN'"
op|','
string|"'ERROR'"
op|','
string|"'CRITICAL'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default notification level for outgoing notifications'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'default_publisher_id'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Default publisher_id for outgoing notifications'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
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
name|'notify_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|notify_decorator
name|'def'
name|'notify_decorator'
op|'('
name|'name'
op|','
name|'fn'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator for notify which is used from utils.monkey_patch().\n\n        :param name: name of the function\n        :param fn: - object of the function\n        :returns: fn -- decorated function\n\n    """'
newline|'\n'
DECL|function|wrapped_func
name|'def'
name|'wrapped_func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwarg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'body'
op|'['
string|"'args'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'body'
op|'['
string|"'kwarg'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'arg'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'args'"
op|']'
op|'.'
name|'append'
op|'('
name|'arg'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'kwarg'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'kwarg'"
op|']'
op|'['
name|'key'
op|']'
op|'='
name|'kwarg'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'common_context'
op|'.'
name|'get_context_from_function_and_args'
op|'('
nl|'\n'
name|'fn'
op|','
name|'args'
op|','
name|'kwarg'
op|')'
newline|'\n'
nl|'\n'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'api'"
op|','
nl|'\n'
name|'publisher_id'
op|'='
op|'('
name|'CONF'
op|'.'
name|'default_publisher_id'
nl|'\n'
name|'or'
name|'CONF'
op|'.'
name|'host'
op|')'
op|')'
newline|'\n'
name|'method'
op|'='
name|'notifier'
op|'.'
name|'getattr'
op|'('
name|'CONF'
op|'.'
name|'default_notification_level'
op|'.'
name|'lower'
op|'('
op|')'
op|','
nl|'\n'
string|"'info'"
op|')'
newline|'\n'
name|'method'
op|'('
name|'ctxt'
op|','
name|'name'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'fn'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwarg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped_func'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_api_fault
dedent|''
name|'def'
name|'send_api_fault'
op|'('
name|'url'
op|','
name|'status'
op|','
name|'exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send an api.fault notification."""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'notify_api_faults'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'payload'
op|'='
op|'{'
string|"'url'"
op|':'
name|'url'
op|','
string|"'exception'"
op|':'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exception'
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'status'
op|'}'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'api'"
op|')'
op|'.'
name|'error'
op|'('
name|'common_context'
op|'.'
name|'get_current'
op|'('
op|')'
name|'or'
nl|'\n'
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
string|"'api.fault'"
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_update
dedent|''
name|'def'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_instance'
op|','
name|'new_instance'
op|','
name|'service'
op|'='
string|'"compute"'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send compute.instance.update notification to report any changes occurred\n    in that instance\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'notify_on_state_change'
op|':'
newline|'\n'
comment|'# skip all this if updates are disabled'
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'update_with_state_change'
op|'='
name|'False'
newline|'\n'
nl|'\n'
name|'old_vm_state'
op|'='
name|'old_instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
name|'new_vm_state'
op|'='
name|'new_instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
name|'old_task_state'
op|'='
name|'old_instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
name|'new_task_state'
op|'='
name|'new_instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
nl|'\n'
comment|'# we should check if we need to send a state change or a regular'
nl|'\n'
comment|'# notification'
nl|'\n'
name|'if'
name|'old_vm_state'
op|'!='
name|'new_vm_state'
op|':'
newline|'\n'
comment|'# yes, the vm state is changing:'
nl|'\n'
indent|'        '
name|'update_with_state_change'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'CONF'
op|'.'
name|'notify_on_state_change'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|'"vm_and_task_state"'
name|'and'
nl|'\n'
name|'old_task_state'
op|'!='
name|'new_task_state'
op|')'
op|':'
newline|'\n'
comment|'# yes, the task state is changing:'
nl|'\n'
indent|'        '
name|'update_with_state_change'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'update_with_state_change'
op|':'
newline|'\n'
comment|'# send a notification with state changes'
nl|'\n'
comment|'# value of verify_states need not be True as the check for states is'
nl|'\n'
comment|'# already done here'
nl|'\n'
indent|'        '
name|'send_update_with_states'
op|'('
name|'context'
op|','
name|'new_instance'
op|','
name|'old_vm_state'
op|','
nl|'\n'
name|'new_vm_state'
op|','
name|'old_task_state'
op|','
name|'new_task_state'
op|','
name|'service'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'old_display_name'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'new_instance'
op|'['
string|'"display_name"'
op|']'
op|'!='
name|'old_instance'
op|'['
string|'"display_name"'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'old_display_name'
op|'='
name|'old_instance'
op|'['
string|'"display_name"'
op|']'
newline|'\n'
dedent|''
name|'_send_instance_update_notification'
op|'('
name|'context'
op|','
name|'new_instance'
op|','
nl|'\n'
name|'service'
op|'='
name|'service'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'old_display_name'
op|'='
name|'old_display_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Failed to send instance update notification. The '"
nl|'\n'
string|"'instance could not be found and was most likely '"
nl|'\n'
string|"'deleted.'"
op|','
name|'instance'
op|'='
name|'new_instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to send state update notification"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'new_instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|send_update_with_states
dedent|''
dedent|''
dedent|''
name|'def'
name|'send_update_with_states'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'old_vm_state'
op|','
name|'new_vm_state'
op|','
nl|'\n'
name|'old_task_state'
op|','
name|'new_task_state'
op|','
name|'service'
op|'='
string|'"compute"'
op|','
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'verify_states'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send compute.instance.update notification to report changes if there\n    are any, in the instance\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'notify_on_state_change'
op|':'
newline|'\n'
comment|'# skip all this if updates are disabled'
nl|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'fire_update'
op|'='
name|'True'
newline|'\n'
comment|'# send update notification by default'
nl|'\n'
nl|'\n'
name|'if'
name|'verify_states'
op|':'
newline|'\n'
comment|'# check whether we need to send notification related to state changes'
nl|'\n'
indent|'        '
name|'fire_update'
op|'='
name|'False'
newline|'\n'
comment|'# do not send notification if the conditions for vm and(or) task state'
nl|'\n'
comment|'# are not satisfied'
nl|'\n'
name|'if'
name|'old_vm_state'
op|'!='
name|'new_vm_state'
op|':'
newline|'\n'
comment|'# yes, the vm state is changing:'
nl|'\n'
indent|'            '
name|'fire_update'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'CONF'
op|'.'
name|'notify_on_state_change'
op|'.'
name|'lower'
op|'('
op|')'
op|'=='
string|'"vm_and_task_state"'
name|'and'
nl|'\n'
name|'old_task_state'
op|'!='
name|'new_task_state'
op|')'
op|':'
newline|'\n'
comment|'# yes, the task state is changing:'
nl|'\n'
indent|'            '
name|'fire_update'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'fire_update'
op|':'
newline|'\n'
comment|'# send either a state change or a regular notification'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'_send_instance_update_notification'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'old_vm_state'
op|'='
name|'old_vm_state'
op|','
name|'old_task_state'
op|'='
name|'old_task_state'
op|','
nl|'\n'
name|'new_vm_state'
op|'='
name|'new_vm_state'
op|','
name|'new_task_state'
op|'='
name|'new_task_state'
op|','
nl|'\n'
name|'service'
op|'='
name|'service'
op|','
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Failed to send instance update notification. The '"
nl|'\n'
string|"'instance could not be found and was most likely '"
nl|'\n'
string|"'deleted.'"
op|','
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to send state update notification"'
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_compute_states_payload
dedent|''
dedent|''
dedent|''
name|'def'
name|'_compute_states_payload'
op|'('
name|'instance'
op|','
name|'old_vm_state'
op|'='
name|'None'
op|','
nl|'\n'
name|'old_task_state'
op|'='
name|'None'
op|','
name|'new_vm_state'
op|'='
name|'None'
op|','
name|'new_task_state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# If the states were not specified we assume the current instance'
nl|'\n'
comment|'# states are the correct information. This is important to do for'
nl|'\n'
comment|'# both old and new states because otherwise we create some really'
nl|'\n'
comment|'# confusing nofications like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   None(None) => Building(none)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# When we really were just continuing to build'
nl|'\n'
indent|'    '
name|'if'
name|'new_vm_state'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'new_vm_state'
op|'='
name|'instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'new_task_state'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'new_task_state'
op|'='
name|'instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'old_vm_state'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'old_vm_state'
op|'='
name|'instance'
op|'['
string|'"vm_state"'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'old_task_state'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'old_task_state'
op|'='
name|'instance'
op|'['
string|'"task_state"'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'states_payload'
op|'='
op|'{'
nl|'\n'
string|'"old_state"'
op|':'
name|'old_vm_state'
op|','
nl|'\n'
string|'"state"'
op|':'
name|'new_vm_state'
op|','
nl|'\n'
string|'"old_task_state"'
op|':'
name|'old_task_state'
op|','
nl|'\n'
string|'"new_task_state"'
op|':'
name|'new_task_state'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'return'
name|'states_payload'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_send_instance_update_notification
dedent|''
name|'def'
name|'_send_instance_update_notification'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'old_vm_state'
op|'='
name|'None'
op|','
nl|'\n'
name|'old_task_state'
op|'='
name|'None'
op|','
name|'new_vm_state'
op|'='
name|'None'
op|','
name|'new_task_state'
op|'='
name|'None'
op|','
nl|'\n'
name|'service'
op|'='
string|'"compute"'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'old_display_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Send \'compute.instance.update\' notification to inform observers\n    about instance state changes.\n    """'
newline|'\n'
nl|'\n'
name|'payload'
op|'='
name|'info_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|"# determine how we'll report states"
nl|'\n'
name|'payload'
op|'.'
name|'update'
op|'('
nl|'\n'
name|'_compute_states_payload'
op|'('
nl|'\n'
name|'instance'
op|','
name|'old_vm_state'
op|','
name|'old_task_state'
op|','
nl|'\n'
name|'new_vm_state'
op|','
name|'new_task_state'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# add audit fields:'
nl|'\n'
op|'('
name|'audit_start'
op|','
name|'audit_end'
op|')'
op|'='
name|'audit_period_bounds'
op|'('
name|'current_period'
op|'='
name|'True'
op|')'
newline|'\n'
name|'payload'
op|'['
string|'"audit_period_beginning"'
op|']'
op|'='
name|'audit_start'
newline|'\n'
name|'payload'
op|'['
string|'"audit_period_ending"'
op|']'
op|'='
name|'audit_end'
newline|'\n'
nl|'\n'
comment|'# add bw usage info:'
nl|'\n'
name|'bw'
op|'='
name|'bandwidth_usage'
op|'('
name|'instance'
op|','
name|'audit_start'
op|')'
newline|'\n'
name|'payload'
op|'['
string|'"bandwidth"'
op|']'
op|'='
name|'bw'
newline|'\n'
nl|'\n'
comment|'# add old display name if it is changed'
nl|'\n'
name|'if'
name|'old_display_name'
op|':'
newline|'\n'
indent|'        '
name|'payload'
op|'['
string|'"old_display_name"'
op|']'
op|'='
name|'old_display_name'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
name|'service'
op|','
name|'host'
op|')'
op|'.'
name|'info'
op|'('
name|'context'
op|','
nl|'\n'
string|"'compute.instance.update'"
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|audit_period_bounds
dedent|''
name|'def'
name|'audit_period_bounds'
op|'('
name|'current_period'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the start and end of the relevant audit usage period\n\n    :param current_period: if True, this will generate a usage for the\n        current usage period; if False, this will generate a usage for the\n        previous audit period.\n    """'
newline|'\n'
nl|'\n'
name|'begin'
op|','
name|'end'
op|'='
name|'utils'
op|'.'
name|'last_completed_audit_period'
op|'('
op|')'
newline|'\n'
name|'if'
name|'current_period'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'end'
newline|'\n'
name|'audit_end'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'audit_start'
op|'='
name|'begin'
newline|'\n'
name|'audit_end'
op|'='
name|'end'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'audit_start'
op|','
name|'audit_end'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bandwidth_usage
dedent|''
name|'def'
name|'bandwidth_usage'
op|'('
name|'instance_ref'
op|','
name|'audit_start'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get bandwidth usage information for the instance for the\n    specified audit period.\n    """'
newline|'\n'
name|'admin_context'
op|'='
name|'nova'
op|'.'
name|'context'
op|'.'
name|'get_admin_context'
op|'('
name|'read_deleted'
op|'='
string|"'yes'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|_get_nwinfo_old_skool
name|'def'
name|'_get_nwinfo_old_skool'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Support for getting network info without objects."""'
newline|'\n'
name|'if'
op|'('
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'info_cache'"
op|')'
name|'and'
nl|'\n'
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
name|'is'
name|'not'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cached_info'
op|'='
name|'instance_ref'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'network_info'"
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'cached_info'
op|','
name|'network_model'
op|'.'
name|'NetworkInfo'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'cached_info'
newline|'\n'
dedent|''
name|'return'
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'cached_info'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'admin_context'
op|','
nl|'\n'
name|'instance_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Failed to get nw_info'"
op|')'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_ref'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'ignore_missing_network_data'
op|':'
newline|'\n'
indent|'                    '
name|'return'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
comment|'# FIXME(comstud): Temporary as we transition to objects.'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'instance_ref'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'instance_ref'
op|'.'
name|'info_cache'
op|'.'
name|'network_info'
newline|'\n'
name|'if'
name|'nw_info'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'_get_nwinfo_old_skool'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'macs'
op|'='
op|'['
name|'vif'
op|'['
string|"'address'"
op|']'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|']'
newline|'\n'
name|'uuids'
op|'='
op|'['
name|'instance_ref'
op|'['
string|'"uuid"'
op|']'
op|']'
newline|'\n'
nl|'\n'
name|'bw_usages'
op|'='
name|'objects'
op|'.'
name|'BandwidthUsageList'
op|'.'
name|'get_by_uuids'
op|'('
name|'admin_context'
op|','
name|'uuids'
op|','
nl|'\n'
name|'audit_start'
op|')'
newline|'\n'
name|'bw'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'b'
name|'in'
name|'bw_usages'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'b'
op|'.'
name|'mac'
name|'in'
name|'macs'
op|':'
newline|'\n'
indent|'            '
name|'label'
op|'='
string|"'net-name-not-found-%s'"
op|'%'
name|'b'
op|'.'
name|'mac'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'vif'
op|'['
string|"'address'"
op|']'
op|'=='
name|'b'
op|'.'
name|'mac'
op|':'
newline|'\n'
indent|'                    '
name|'label'
op|'='
name|'vif'
op|'['
string|"'network'"
op|']'
op|'['
string|"'label'"
op|']'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bw'
op|'['
name|'label'
op|']'
op|'='
name|'dict'
op|'('
name|'bw_in'
op|'='
name|'b'
op|'.'
name|'bw_in'
op|','
name|'bw_out'
op|'='
name|'b'
op|'.'
name|'bw_out'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'bw'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_meta
dedent|''
name|'def'
name|'image_meta'
op|'('
name|'system_metadata'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Format image metadata for use in notifications from the instance\n    system metadata.\n    """'
newline|'\n'
name|'image_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'md_key'
op|','
name|'md_value'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'system_metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'md_key'
op|'.'
name|'startswith'
op|'('
string|"'image_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_meta'
op|'['
name|'md_key'
op|'['
number|'6'
op|':'
op|']'
op|']'
op|'='
name|'md_value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'image_meta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|info_from_instance
dedent|''
name|'def'
name|'info_from_instance'
op|'('
name|'context'
op|','
name|'instance'
op|','
name|'network_info'
op|','
nl|'\n'
name|'system_metadata'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get detailed instance information for an instance which is common to all\n    notifications.\n\n    :param:instance: nova.objects.Instance\n    :param:network_info: network_info provided if not None\n    :param:system_metadata: system_metadata DB entries for the instance,\n    if not None\n\n    .. note::\n\n        Currently unused here in trunk, but needed for potential custom\n        modifications.\n\n    """'
newline|'\n'
nl|'\n'
DECL|function|null_safe_str
name|'def'
name|'null_safe_str'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'s'
op|')'
name|'if'
name|'s'
name|'else'
string|"''"
newline|'\n'
nl|'\n'
DECL|function|null_safe_int
dedent|''
name|'def'
name|'null_safe_int'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'s'
op|')'
name|'if'
name|'s'
name|'else'
string|"''"
newline|'\n'
nl|'\n'
DECL|function|null_safe_isotime
dedent|''
name|'def'
name|'null_safe_isotime'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'s'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'s'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'s'
op|')'
name|'if'
name|'s'
name|'else'
string|"''"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'image_ref_url'
op|'='
name|'glance'
op|'.'
name|'generate_image_url'
op|'('
name|'instance'
op|'.'
name|'image_ref'
op|')'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'instance'
op|'.'
name|'get_flavor'
op|'('
op|')'
newline|'\n'
name|'instance_type_name'
op|'='
name|'instance_type'
op|'.'
name|'get'
op|'('
string|"'name'"
op|','
string|"''"
op|')'
newline|'\n'
name|'instance_flavorid'
op|'='
name|'instance_type'
op|'.'
name|'get'
op|'('
string|"'flavorid'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
name|'instance_info'
op|'='
name|'dict'
op|'('
nl|'\n'
comment|'# Owner properties'
nl|'\n'
name|'tenant_id'
op|'='
name|'instance'
op|'.'
name|'project_id'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'instance'
op|'.'
name|'user_id'
op|','
nl|'\n'
nl|'\n'
comment|'# Identity properties'
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'.'
name|'uuid'
op|','
nl|'\n'
name|'display_name'
op|'='
name|'instance'
op|'.'
name|'display_name'
op|','
nl|'\n'
name|'reservation_id'
op|'='
name|'instance'
op|'.'
name|'reservation_id'
op|','
nl|'\n'
name|'hostname'
op|'='
name|'instance'
op|'.'
name|'hostname'
op|','
nl|'\n'
nl|'\n'
comment|'# Type properties'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_type_name'
op|','
nl|'\n'
name|'instance_type_id'
op|'='
name|'instance'
op|'.'
name|'instance_type_id'
op|','
nl|'\n'
name|'instance_flavor_id'
op|'='
name|'instance_flavorid'
op|','
nl|'\n'
name|'architecture'
op|'='
name|'instance'
op|'.'
name|'architecture'
op|','
nl|'\n'
nl|'\n'
comment|'# Capacity properties'
nl|'\n'
name|'memory_mb'
op|'='
name|'instance'
op|'.'
name|'memory_mb'
op|','
nl|'\n'
name|'disk_gb'
op|'='
name|'instance'
op|'.'
name|'root_gb'
op|'+'
name|'instance'
op|'.'
name|'ephemeral_gb'
op|','
nl|'\n'
name|'vcpus'
op|'='
name|'instance'
op|'.'
name|'vcpus'
op|','
nl|'\n'
comment|'# Note(dhellmann): This makes the disk_gb value redundant, but'
nl|'\n'
comment|'# we are keeping it for backwards-compatibility with existing'
nl|'\n'
comment|'# users of notifications.'
nl|'\n'
name|'root_gb'
op|'='
name|'instance'
op|'.'
name|'root_gb'
op|','
nl|'\n'
name|'ephemeral_gb'
op|'='
name|'instance'
op|'.'
name|'ephemeral_gb'
op|','
nl|'\n'
nl|'\n'
comment|'# Location properties'
nl|'\n'
name|'host'
op|'='
name|'instance'
op|'.'
name|'host'
op|','
nl|'\n'
name|'node'
op|'='
name|'instance'
op|'.'
name|'node'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'instance'
op|'.'
name|'availability_zone'
op|','
nl|'\n'
name|'cell_name'
op|'='
name|'null_safe_str'
op|'('
name|'instance'
op|'.'
name|'cell_name'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Date properties'
nl|'\n'
name|'created_at'
op|'='
name|'str'
op|'('
name|'instance'
op|'.'
name|'created_at'
op|')'
op|','
nl|'\n'
comment|'# Terminated and Deleted are slightly different (although being'
nl|'\n'
comment|'# terminated and not deleted is a transient state), so include'
nl|'\n'
comment|'# both and let the recipient decide which they want to use.'
nl|'\n'
name|'terminated_at'
op|'='
name|'null_safe_isotime'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'terminated_at'"
op|','
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'deleted_at'
op|'='
name|'null_safe_isotime'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'deleted_at'"
op|','
name|'None'
op|')'
op|')'
op|','
nl|'\n'
name|'launched_at'
op|'='
name|'null_safe_isotime'
op|'('
name|'instance'
op|'.'
name|'get'
op|'('
string|"'launched_at'"
op|','
name|'None'
op|')'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# Image properties'
nl|'\n'
name|'image_ref_url'
op|'='
name|'image_ref_url'
op|','
nl|'\n'
name|'os_type'
op|'='
name|'instance'
op|'.'
name|'os_type'
op|','
nl|'\n'
name|'kernel_id'
op|'='
name|'instance'
op|'.'
name|'kernel_id'
op|','
nl|'\n'
name|'ramdisk_id'
op|'='
name|'instance'
op|'.'
name|'ramdisk_id'
op|','
nl|'\n'
nl|'\n'
comment|'# Status properties'
nl|'\n'
name|'state'
op|'='
name|'instance'
op|'.'
name|'vm_state'
op|','
nl|'\n'
name|'state_description'
op|'='
name|'null_safe_str'
op|'('
name|'instance'
op|'.'
name|'task_state'
op|')'
op|','
nl|'\n'
name|'progress'
op|'='
name|'null_safe_int'
op|'('
name|'instance'
op|'.'
name|'progress'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|'# accessIPs'
nl|'\n'
name|'access_ip_v4'
op|'='
name|'instance'
op|'.'
name|'access_ip_v4'
op|','
nl|'\n'
name|'access_ip_v6'
op|'='
name|'instance'
op|'.'
name|'access_ip_v6'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'network_info'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ips'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'network_info'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ip'
op|'['
string|'"label"'
op|']'
op|'='
name|'vif'
op|'['
string|'"network"'
op|']'
op|'['
string|'"label"'
op|']'
newline|'\n'
name|'ip'
op|'['
string|'"vif_mac"'
op|']'
op|'='
name|'vif'
op|'['
string|'"address"'
op|']'
newline|'\n'
name|'fixed_ips'
op|'.'
name|'append'
op|'('
name|'ip'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'instance_info'
op|'['
string|"'fixed_ips'"
op|']'
op|'='
name|'fixed_ips'
newline|'\n'
nl|'\n'
comment|'# add image metadata'
nl|'\n'
dedent|''
name|'image_meta_props'
op|'='
name|'image_meta'
op|'('
name|'instance'
op|'.'
name|'system_metadata'
op|')'
newline|'\n'
name|'instance_info'
op|'['
string|'"image_meta"'
op|']'
op|'='
name|'image_meta_props'
newline|'\n'
nl|'\n'
comment|'# add instance metadata'
nl|'\n'
name|'instance_info'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'instance'
op|'.'
name|'metadata'
newline|'\n'
nl|'\n'
name|'instance_info'
op|'.'
name|'update'
op|'('
name|'kw'
op|')'
newline|'\n'
name|'return'
name|'instance_info'
newline|'\n'
dedent|''
endmarker|''
end_unit
