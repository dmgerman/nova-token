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
name|'import'
name|'operator'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
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
name|'least_cost'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'scheduler_options'
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
op|'{'
op|'}'
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
DECL|member|schedule
dedent|''
name|'def'
name|'schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'method'
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
string|'"""The schedule() contract requires we return the one\n        best-suited host for this request.\n\n        NOTE: We\'re only focused on compute instances right now,\n        so this method will always raise NoValidHost()."""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"No host selection for %s defined."'
op|')'
op|'%'
name|'topic'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called from nova.compute.api to provision\n        an instance.  We first create a build plan (a list of WeightedHosts)\n        and then provision.\n\n        Returns a list of the instances created.\n        """'
newline|'\n'
nl|'\n'
name|'elevated'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
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
name|'weighted_hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|'"compute"'
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'weighted_hosts'
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
nl|'\n'
comment|'# NOTE(comstud): Make sure we do not pass this through.  It'
nl|'\n'
comment|'# contains an instance of RpcContext that cannot be serialized.'
nl|'\n'
dedent|''
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'filter_properties'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'instances'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'xrange'
op|'('
name|'num_instances'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'weighted_hosts'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'weighted_host'
op|'='
name|'weighted_hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
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
name|'instance'
op|'='
name|'self'
op|'.'
name|'_provision_resource'
op|'('
name|'elevated'
op|','
name|'weighted_host'
op|','
nl|'\n'
name|'request_spec'
op|','
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'instance'
op|':'
newline|'\n'
indent|'                '
name|'instances'
op|'.'
name|'append'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'notifier'
op|'.'
name|'notify'
op|'('
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
name|'return'
name|'instances'
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
name|'request_spec'
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
string|'"""Select a target for resize.\n\n        Selects a target host for the instance, post-resize, and casts\n        the prep_resize operation to it.\n        """'
newline|'\n'
nl|'\n'
name|'hosts'
op|'='
name|'self'
op|'.'
name|'_schedule'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'request_spec'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hosts'
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
name|'host'
op|'='
name|'hosts'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(comstud): Make sure we do not pass this through.  It'
nl|'\n'
comment|'# contains an instance of RpcContext that cannot be serialized.'
nl|'\n'
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'filter_properties'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
comment|'# Forward off to the host'
nl|'\n'
name|'driver'
op|'.'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'host'
op|'.'
name|'host_state'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'prep_resize'"
op|','
op|'**'
name|'kwargs'
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
name|'weighted_host'
op|','
name|'request_spec'
op|','
nl|'\n'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create the requested resource in this Zone."""'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'create_instance_db_entry'
op|'('
name|'context'
op|','
name|'request_spec'
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
op|','
nl|'\n'
name|'weighted_host'
op|'='
name|'weighted_host'
op|'.'
name|'to_dict'
op|'('
op|')'
op|','
nl|'\n'
name|'instance_id'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'notifier'
op|'.'
name|'notify'
op|'('
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
name|'driver'
op|'.'
name|'cast_to_compute_host'
op|'('
name|'context'
op|','
name|'weighted_host'
op|'.'
name|'host_state'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'run_instance'"
op|','
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'inst'
op|'='
name|'driver'
op|'.'
name|'encode_instance'
op|'('
name|'instance'
op|','
name|'local'
op|'='
name|'True'
op|')'
newline|'\n'
comment|'# So if another instance is created, create_instance_db_entry will'
nl|'\n'
comment|"# actually create a new entry, instead of assume it's been created"
nl|'\n'
comment|'# already'
nl|'\n'
name|'del'
name|'request_spec'
op|'['
string|"'instance_properties'"
op|']'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'return'
name|'inst'
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
string|'"""Stuff things into filter_properties.  Can be overriden in a\n        subclass to add more data.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_schedule
dedent|''
name|'def'
name|'_schedule'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|','
name|'request_spec'
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
name|'if'
name|'topic'
op|'!='
string|'"compute"'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Scheduler only understands Compute nodes (for now)"'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'cost_functions'
op|'='
name|'self'
op|'.'
name|'get_cost_functions'
op|'('
op|')'
newline|'\n'
name|'config_options'
op|'='
name|'self'
op|'.'
name|'_get_configuration_options'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'filter_properties'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'filter_properties'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
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
comment|'# unfiltered_hosts_dict is {host : ZoneManager.HostInfo()}'
nl|'\n'
name|'unfiltered_hosts_dict'
op|'='
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
nl|'\n'
name|'elevated'
op|','
name|'topic'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note: remember, we are using an iterator here. So only'
nl|'\n'
comment|'# traverse this list once. This can bite you if the hosts'
nl|'\n'
comment|'# are being scanned in a filter or weighing function.'
nl|'\n'
name|'hosts'
op|'='
name|'unfiltered_hosts_dict'
op|'.'
name|'itervalues'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'selected_hosts'
op|'='
op|'['
op|']'
newline|'\n'
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
name|'filter_hosts'
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
comment|'# weighted_host = WeightedHost() ... the best'
nl|'\n'
comment|'# host for the job.'
nl|'\n'
comment|'# TODO(comstud): filter_properties will also be used for'
nl|'\n'
comment|'# weighing and I plan fold weighing into the host manager'
nl|'\n'
comment|"# in a future patch.  I'll address the naming of this"
nl|'\n'
comment|'# variable at that time.'
nl|'\n'
name|'weighted_host'
op|'='
name|'least_cost'
op|'.'
name|'weighted_sum'
op|'('
name|'cost_functions'
op|','
nl|'\n'
name|'hosts'
op|','
name|'filter_properties'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Weighted %(weighted_host)s"'
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
name|'weighted_host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now consume the resources so the filter/weights'
nl|'\n'
comment|'# will change for the next instance.'
nl|'\n'
name|'weighted_host'
op|'.'
name|'host_state'
op|'.'
name|'consume_from_instance'
op|'('
nl|'\n'
name|'instance_properties'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'selected_hosts'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'operator'
op|'.'
name|'attrgetter'
op|'('
string|"'weight'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'selected_hosts'
op|'['
op|':'
name|'num_instances'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_cost_functions
dedent|''
name|'def'
name|'get_cost_functions'
op|'('
name|'self'
op|','
name|'topic'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of tuples containing weights and cost functions to\n        use for weighing hosts\n        """'
newline|'\n'
name|'if'
name|'topic'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# Schedulers only support compute right now.'
nl|'\n'
indent|'            '
name|'topic'
op|'='
string|'"compute"'
newline|'\n'
dedent|''
name|'if'
name|'topic'
name|'in'
name|'self'
op|'.'
name|'cost_function_cache'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'cost_function_cache'
op|'['
name|'topic'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'cost_fns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'cost_fn_str'
name|'in'
name|'FLAGS'
op|'.'
name|'least_cost_functions'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'.'"
name|'in'
name|'cost_fn_str'
op|':'
newline|'\n'
indent|'                '
name|'short_name'
op|'='
name|'cost_fn_str'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'short_name'
op|'='
name|'cost_fn_str'
newline|'\n'
name|'cost_fn_str'
op|'='
string|'"%s.%s.%s"'
op|'%'
op|'('
nl|'\n'
name|'__name__'
op|','
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'short_name'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
op|'('
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'%s_'"
op|'%'
name|'topic'
op|')'
name|'or'
nl|'\n'
name|'short_name'
op|'.'
name|'startswith'
op|'('
string|"'noop'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
comment|'# NOTE: import_class is somewhat misnamed since'
nl|'\n'
comment|'# the weighing function can be any non-class callable'
nl|'\n'
comment|"# (i.e., no 'self')"
nl|'\n'
indent|'                '
name|'cost_fn'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'cost_fn_str'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerCostFunctionNotFound'
op|'('
nl|'\n'
name|'cost_fn_str'
op|'='
name|'cost_fn_str'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'flag_name'
op|'='
string|'"%s_weight"'
op|'%'
name|'cost_fn'
op|'.'
name|'__name__'
newline|'\n'
name|'weight'
op|'='
name|'getattr'
op|'('
name|'FLAGS'
op|','
name|'flag_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SchedulerWeightFlagNotFound'
op|'('
nl|'\n'
name|'flag_name'
op|'='
name|'flag_name'
op|')'
newline|'\n'
dedent|''
name|'cost_fns'
op|'.'
name|'append'
op|'('
op|'('
name|'weight'
op|','
name|'cost_fn'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'cost_function_cache'
op|'['
name|'topic'
op|']'
op|'='
name|'cost_fns'
newline|'\n'
name|'return'
name|'cost_fns'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
