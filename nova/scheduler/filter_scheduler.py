begin_unit
comment|'# Copyright (c) 2011 OpenStack, LLC.'
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
string|'"""\nThe FilterScheduler is for creating instances locally.\nYou can customize this scheduler by specifying your own Host Filters and\nWeighing Functions.\n"""'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'notifier'
name|'import'
name|'api'
name|'as'
name|'notifier'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'scheduler_options'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|class|FilterScheduler
name|'class'
name|'FilterScheduler'
op|'('
name|'driver'
op|'.'
name|'Scheduler'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Scheduler that can be used for filtering and weighing."""'
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
name|'super'
op|'('
name|'FilterScheduler'
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
name|'cost_function_cache'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'options'
op|'='
name|'scheduler_options'
op|'.'
name|'SchedulerOptions'
op|'('
op|')'
newline|'\n'
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
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called from nova.compute.api to provision\n        an instance.  We first create a build plan (a list of WeightedHosts)\n        and then provision.\n\n        Returns a list of the instances created.\n        """'
newline|'\n'
name|'instance_uuids'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'instance_uuids'"
op|')'
newline|'\n'
name|'num_instances'
op|'='
name|'len'
op|'('
name|'instance_uuids'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attempting to build %(num_instances)d instance(s)"'
op|')'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'payload'
op|'='
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'notifier'
op|'.'
name|'publisher_id'
op|'('
string|'"scheduler"'
op|')'
op|','
nl|'\n'
string|"'scheduler.run_instance.start'"
op|','
name|'notifier'
op|'.'
name|'INFO'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
name|'weighed_hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(comstud): Make sure we do not pass this through.  It'
nl|'\n'
comment|'# contains an instance of RpcContext that cannot be serialized.'
nl|'\n'
name|'filter_properties'
op|'.'
name|'pop'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'num'
op|','
name|'instance_uuid'
name|'in'
name|'enumerate'
op|'('
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'launch_index'"
op|']'
op|'='
name|'num'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'weighed_host'
op|'='
name|'weighed_hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|'""'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'context'
op|','
name|'weighed_host'
op|','
nl|'\n'
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
nl|'\n'
name|'requested_networks'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'is_first_time'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|"# NOTE(vish): we don't reraise the exception here to make sure"
nl|'\n'
comment|'#             that all instances in the request get set to'
nl|'\n'
comment|'#             error properly'
nl|'\n'
indent|'                '
name|'driver'
op|'.'
name|'handle_schedule_error'
op|'('
name|'context'
op|','
name|'ex'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'request_spec'
op|')'
newline|'\n'
comment|"# scrub retry host list in case we're scheduling multiple"
nl|'\n'
comment|'# instances:'
nl|'\n'
dedent|''
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'retry'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'retry'
op|'['
string|"'hosts'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'notifier'
op|'.'
name|'publisher_id'
op|'('
string|'"scheduler"'
op|')'
op|','
nl|'\n'
string|"'scheduler.run_instance.end'"
op|','
name|'notifier'
op|'.'
name|'INFO'
op|','
name|'payload'
op|')'
newline|'\n'
nl|'\n'
DECL|member|schedule_prep_resize
dedent|''
name|'def'
name|'schedule_prep_resize'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'instance'
op|','
name|'instance_type'
op|','
nl|'\n'
name|'reservations'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Select a target for resize.\n\n        Selects a target host for the instance, post-resize, and casts\n        the prep_resize operation to it.\n        """'
newline|'\n'
nl|'\n'
name|'weighed_hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
op|'['
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|']'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'weighed_hosts'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
string|'""'
op|')'
newline|'\n'
dedent|''
name|'weighed_host'
op|'='
name|'weighed_hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_post_select_populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'weighed_host'
op|'.'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
comment|'# context is not serializable'
nl|'\n'
name|'filter_properties'
op|'.'
name|'pop'
op|'('
string|"'context'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|'# Forward off to the host'
nl|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'prep_resize'
op|'('
name|'context'
op|','
name|'image'
op|','
name|'instance'
op|','
nl|'\n'
name|'instance_type'
op|','
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|','
name|'reservations'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provision_resource
dedent|''
name|'def'
name|'_provision_resource'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'weighed_host'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'requested_networks'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'is_first_time'
op|','
name|'instance_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone."""'
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
name|'weighted_host'
op|'='
name|'weighed_host'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
name|'context'
op|','
name|'notifier'
op|'.'
name|'publisher_id'
op|'('
string|'"scheduler"'
op|')'
op|','
nl|'\n'
string|"'scheduler.run_instance.scheduled'"
op|','
name|'notifier'
op|'.'
name|'INFO'
op|','
nl|'\n'
name|'payload'
op|')'
newline|'\n'
nl|'\n'
name|'updated_instance'
op|'='
name|'driver'
op|'.'
name|'instance_update_db'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_post_select_populate_filter_properties'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'weighed_host'
op|'.'
name|'obj'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_rpcapi'
op|'.'
name|'run_instance'
op|'('
name|'context'
op|','
name|'instance'
op|'='
name|'updated_instance'
op|','
nl|'\n'
name|'host'
op|'='
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
name|'is_first_time'
op|'='
name|'is_first_time'
op|','
nl|'\n'
name|'node'
op|'='
name|'weighed_host'
op|'.'
name|'obj'
op|'.'
name|'nodename'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_post_select_populate_filter_properties
dedent|''
name|'def'
name|'_post_select_populate_filter_properties'
op|'('
name|'self'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add additional information to the filter properties after a host has\n        been selected by the scheduling process.\n        """'
newline|'\n'
comment|'# Add a retry entry for the selected compute host:'
nl|'\n'
name|'self'
op|'.'
name|'_add_retry_host'
op|'('
name|'filter_properties'
op|','
name|'host_state'
op|'.'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_add_oversubscription_policy'
op|'('
name|'filter_properties'
op|','
name|'host_state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_retry_host
dedent|''
name|'def'
name|'_add_retry_host'
op|'('
name|'self'
op|','
name|'filter_properties'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add a retry entry for the selected compute host.  In the event that\n        the request gets re-scheduled, this entry will signal that the given\n        host has already been tried.\n        """'
newline|'\n'
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'retry'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'retry'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'hosts'
op|'='
name|'retry'
op|'['
string|"'hosts'"
op|']'
newline|'\n'
name|'hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_oversubscription_policy
dedent|''
name|'def'
name|'_add_oversubscription_policy'
op|'('
name|'self'
op|','
name|'filter_properties'
op|','
name|'host_state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filter_properties'
op|'['
string|"'limits'"
op|']'
op|'='
name|'host_state'
op|'.'
name|'limits'
newline|'\n'
nl|'\n'
DECL|member|_get_configuration_options
dedent|''
name|'def'
name|'_get_configuration_options'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Fetch options dictionary. Broken out for testing."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'options'
op|'.'
name|'get_configuration'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|populate_filter_properties
dedent|''
name|'def'
name|'populate_filter_properties'
op|'('
name|'self'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stuff things into filter_properties.  Can be overridden in a\n        subclass to add more data.\n        """'
newline|'\n'
comment|'# Save useful information from the request spec for filter processing:'
nl|'\n'
name|'project_id'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'project_id'"
op|']'
newline|'\n'
name|'os_type'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'os_type'"
op|']'
newline|'\n'
name|'filter_properties'
op|'['
string|"'project_id'"
op|']'
op|'='
name|'project_id'
newline|'\n'
name|'filter_properties'
op|'['
string|"'os_type'"
op|']'
op|'='
name|'os_type'
newline|'\n'
nl|'\n'
DECL|member|_max_attempts
dedent|''
name|'def'
name|'_max_attempts'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'max_attempts'
op|'='
name|'CONF'
op|'.'
name|'scheduler_max_attempts'
newline|'\n'
name|'if'
name|'max_attempts'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"Invalid value for "'
nl|'\n'
string|'"\'scheduler_max_attempts\', must be >= 1"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'max_attempts'
newline|'\n'
nl|'\n'
DECL|member|_populate_retry
dedent|''
name|'def'
name|'_populate_retry'
op|'('
name|'self'
op|','
name|'filter_properties'
op|','
name|'instance_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Populate filter properties with history of retries for this\n        request. If maximum retries is exceeded, raise NoValidHost.\n        """'
newline|'\n'
name|'max_attempts'
op|'='
name|'self'
op|'.'
name|'_max_attempts'
op|'('
op|')'
newline|'\n'
name|'retry'
op|'='
name|'filter_properties'
op|'.'
name|'pop'
op|'('
string|"'retry'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'max_attempts'
op|'=='
number|'1'
op|':'
newline|'\n'
comment|'# re-scheduling is disabled.'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
comment|'# retry is enabled, update attempt count:'
nl|'\n'
dedent|''
name|'if'
name|'retry'
op|':'
newline|'\n'
indent|'            '
name|'retry'
op|'['
string|"'num_attempts'"
op|']'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'retry'
op|'='
op|'{'
nl|'\n'
string|"'num_attempts'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'hosts'"
op|':'
op|'['
op|']'
comment|'# list of compute hosts tried'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'filter_properties'
op|'['
string|"'retry'"
op|']'
op|'='
name|'retry'
newline|'\n'
nl|'\n'
name|'if'
name|'retry'
op|'['
string|"'num_attempts'"
op|']'
op|'>'
name|'max_attempts'
op|':'
newline|'\n'
indent|'            '
name|'instance_uuid'
op|'='
name|'instance_properties'
op|'.'
name|'get'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Exceeded max scheduling attempts %(max_attempts)d for "'
nl|'\n'
string|'"instance %(instance_uuid)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'instance_uuids'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of hosts that meet the required specs,\n        ordered by their fitness.\n        """'
newline|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'instance_properties'
op|'='
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
newline|'\n'
name|'instance_type'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|'"instance_type"'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'config_options'
op|'='
name|'self'
op|'.'
name|'_get_configuration_options'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# check retry policy.  Rather ugly use of instance_uuids[0]...'
nl|'\n'
comment|"# but if we've exceeded max retries... then we really only"
nl|'\n'
comment|'# have a single instance.'
nl|'\n'
name|'properties'
op|'='
name|'instance_properties'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'            '
name|'properties'
op|'['
string|"'uuid'"
op|']'
op|'='
name|'instance_uuids'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_populate_retry'
op|'('
name|'filter_properties'
op|','
name|'properties'
op|')'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'.'
name|'update'
op|'('
op|'{'
string|"'context'"
op|':'
name|'context'
op|','
nl|'\n'
string|"'request_spec'"
op|':'
name|'request_spec'
op|','
nl|'\n'
string|"'config_options'"
op|':'
name|'config_options'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'instance_type'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'populate_filter_properties'
op|'('
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
nl|'\n'
comment|'# Find our local list of acceptable hosts by repeatedly'
nl|'\n'
comment|'# filtering and weighing our options. Each time we choose a'
nl|'\n'
comment|'# host, we virtually consume resources on it so subsequent'
nl|'\n'
comment|'# selections can adjust accordingly.'
nl|'\n'
nl|'\n'
comment|'# Note: remember, we are using an iterator here. So only'
nl|'\n'
comment|'# traverse this list once. This can bite you if the hosts'
nl|'\n'
comment|'# are being scanned in a filter or weighing function.'
nl|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'elevated'
op|')'
newline|'\n'
nl|'\n'
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'            '
name|'num_instances'
op|'='
name|'len'
op|'('
name|'instance_uuids'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'num_instances'
op|'='
name|'request_spec'
op|'.'
name|'get'
op|'('
string|"'num_instances'"
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
comment|'# Filter local hosts based on requirements ...'
nl|'\n'
indent|'            '
name|'hosts'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_filtered_hosts'
op|'('
name|'hosts'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
op|':'
newline|'\n'
comment|"# Can't get any more locally."
nl|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Filtered %(hosts)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'weighed_hosts'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_weighed_hosts'
op|'('
name|'hosts'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
name|'best_host'
op|'='
name|'weighed_hosts'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Choosing host %(best_host)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'selected_hosts'
op|'.'
name|'append'
op|'('
name|'best_host'
op|')'
newline|'\n'
comment|'# Now consume the resources so the filter/weights'
nl|'\n'
comment|'# will change for the next instance.'
nl|'\n'
name|'best_host'
op|'.'
name|'obj'
op|'.'
name|'consume_from_instance'
op|'('
name|'instance_properties'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'selected_hosts'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
