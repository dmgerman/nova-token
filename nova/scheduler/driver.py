begin_unit
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
string|'"""\nScheduler base class that all Schedulers should inherit from\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'utils'
name|'as'
name|'compute_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'vm_states'
newline|'\n'
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
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'notifications'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
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
name|'from'
name|'nova'
name|'import'
name|'servicegroup'
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
DECL|variable|scheduler_driver_opts
name|'scheduler_driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler_host_manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.scheduler.host_manager.HostManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The scheduler host manager class to use'"
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
name|'scheduler_driver_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|handle_schedule_error
name|'def'
name|'handle_schedule_error'
op|'('
name|'context'
op|','
name|'ex'
op|','
name|'instance_uuid'
op|','
name|'request_spec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""On run_instance failure, update instance state and\n    send notifications.\n    """'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'ex'
op|','
name|'exception'
op|'.'
name|'NoValidHost'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"NoValidHost exception with message: \\\'%s\\\'"'
op|')'
op|','
nl|'\n'
name|'ex'
op|'.'
name|'format_message'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Exception during scheduler.run_instance"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|'.'
name|'upper'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'Setting instance to %s state.'"
op|')'
op|','
name|'state'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'old_ref'
op|','
name|'new_ref'
op|')'
op|'='
name|'db'
op|'.'
name|'instance_update_and_get_original'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|','
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
string|"'task_state'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'notifications'
op|'.'
name|'send_update'
op|'('
name|'context'
op|','
name|'old_ref'
op|','
name|'new_ref'
op|','
nl|'\n'
name|'service'
op|'='
string|'"scheduler"'
op|')'
newline|'\n'
name|'compute_utils'
op|'.'
name|'add_instance_fault_from_exc'
op|'('
name|'context'
op|','
nl|'\n'
name|'new_ref'
op|','
name|'ex'
op|','
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'properties'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'instance_properties'
op|'='
name|'properties'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'state'
op|'='
name|'vm_states'
op|'.'
name|'ERROR'
op|','
nl|'\n'
name|'method'
op|'='
string|"'run_instance'"
op|','
nl|'\n'
name|'reason'
op|'='
name|'ex'
op|')'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'scheduler'"
op|')'
op|'.'
name|'error'
op|'('
name|'context'
op|','
nl|'\n'
string|"'scheduler.run_instance'"
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_update_db
dedent|''
name|'def'
name|'instance_update_db'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'extra_values'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Clear the host and node - set the scheduled_at field of an Instance.\n\n    :returns: An Instance with the updated fields set properly.\n    """'
newline|'\n'
name|'now'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'values'
op|'='
op|'{'
string|"'host'"
op|':'
name|'None'
op|','
string|"'node'"
op|':'
name|'None'
op|','
string|"'scheduled_at'"
op|':'
name|'now'
op|'}'
newline|'\n'
name|'if'
name|'extra_values'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'.'
name|'update'
op|'('
name|'extra_values'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Scheduler
dedent|''
name|'class'
name|'Scheduler'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The base class that all Scheduler classes should inherit from."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'host_manager'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'scheduler_host_manager'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'servicegroup_api'
op|'='
name|'servicegroup'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_periodic_tasks
dedent|''
name|'def'
name|'run_periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Manager calls this so drivers can perform periodic tasks."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|hosts_up
dedent|''
name|'def'
name|'hosts_up'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the list of hosts that have a running service for topic."""'
newline|'\n'
nl|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_topic'
op|'('
name|'context'
op|','
name|'topic'
op|')'
newline|'\n'
name|'return'
op|'['
name|'service'
op|'['
string|"'host'"
op|']'
nl|'\n'
name|'for'
name|'service'
name|'in'
name|'services'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'servicegroup_api'
op|'.'
name|'service_is_up'
op|'('
name|'service'
op|')'
op|']'
newline|'\n'
nl|'\n'
comment|'# NOTE(alaski): Remove this method when the scheduler rpc interface is'
nl|'\n'
comment|'# bumped to 4.x as it is no longer used.'
nl|'\n'
DECL|member|schedule_run_instance
dedent|''
name|'def'
name|'schedule_run_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'legacy_bdm_in_spec'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override schedule_run_instance method for scheduler to work."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Driver must implement schedule_run_instance"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select_destinations
dedent|''
name|'def'
name|'select_destinations'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Must override select_destinations method.\n\n        :return: A list of dicts with \'host\', \'nodename\' and \'limits\' as keys\n            that satisfies the request_spec and filter_properties.\n        """'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Driver must implement select_destinations"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
