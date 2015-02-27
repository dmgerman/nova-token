begin_unit
comment|'# Copyright (c) 2011 OpenStack Foundation'
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
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
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
DECL|variable|filter_scheduler_opts
name|'filter_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_host_subset_size'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'New instances will be scheduled on a host chosen '"
nl|'\n'
string|"'randomly from a subset of the N best hosts. This '"
nl|'\n'
string|"'property defines the subset size that a host is '"
nl|'\n'
string|"'chosen from. A value of 1 chooses the '"
nl|'\n'
string|"'first host returned by the weighing functions. '"
nl|'\n'
string|"'This value must be at least 1. Any value less than 1 '"
nl|'\n'
string|"'will be ignored, and 1 will be used instead'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'filter_scheduler_opts'
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
name|'options'
op|'='
name|'scheduler_options'
op|'.'
name|'SchedulerOptions'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'notifier'
op|'='
name|'rpc'
op|'.'
name|'get_notifier'
op|'('
string|"'scheduler'"
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
string|'"""Selects a filtered set of hosts and nodes."""'
newline|'\n'
name|'self'
op|'.'
name|'notifier'
op|'.'
name|'info'
op|'('
name|'context'
op|','
string|"'scheduler.select_destinations.start'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'num_instances'
op|'='
name|'request_spec'
op|'['
string|"'num_instances'"
op|']'
newline|'\n'
name|'selected_hosts'
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
op|')'
newline|'\n'
nl|'\n'
comment|"# Couldn't fulfill the request_spec"
nl|'\n'
name|'if'
name|'len'
op|'('
name|'selected_hosts'
op|')'
op|'<'
name|'num_instances'
op|':'
newline|'\n'
comment|"# Log the details but don't put those into the reason since"
nl|'\n'
comment|"# we don't want to give away too much information about our"
nl|'\n'
comment|'# actual environment.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'There are %(hosts)d hosts available but '"
nl|'\n'
string|"'%(num_instances)d instances requested to build.'"
op|','
nl|'\n'
op|'{'
string|"'hosts'"
op|':'
name|'len'
op|'('
name|'selected_hosts'
op|')'
op|','
nl|'\n'
string|"'num_instances'"
op|':'
name|'num_instances'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'There are not enough hosts available.'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoValidHost'
op|'('
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dests'
op|'='
op|'['
name|'dict'
op|'('
name|'host'
op|'='
name|'host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|','
name|'nodename'
op|'='
name|'host'
op|'.'
name|'obj'
op|'.'
name|'nodename'
op|','
nl|'\n'
name|'limits'
op|'='
name|'host'
op|'.'
name|'obj'
op|'.'
name|'limits'
op|')'
name|'for'
name|'host'
name|'in'
name|'selected_hosts'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'notifier'
op|'.'
name|'info'
op|'('
name|'context'
op|','
string|"'scheduler.select_destinations.end'"
op|','
nl|'\n'
name|'dict'
op|'('
name|'request_spec'
op|'='
name|'request_spec'
op|')'
op|')'
newline|'\n'
name|'return'
name|'dests'
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
DECL|member|_schedule
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
name|'update_group_hosts'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'group_updated'"
op|','
name|'False'
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
name|'_get_all_host_states'
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
op|','
name|'index'
op|'='
name|'num'
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
string|'"Filtered %(hosts)s"'
op|','
op|'{'
string|"'hosts'"
op|':'
name|'hosts'
op|'}'
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
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Weighed %(hosts)s"'
op|','
op|'{'
string|"'hosts'"
op|':'
name|'weighed_hosts'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'scheduler_host_subset_size'
op|'='
name|'CONF'
op|'.'
name|'scheduler_host_subset_size'
newline|'\n'
name|'if'
name|'scheduler_host_subset_size'
op|'>'
name|'len'
op|'('
name|'weighed_hosts'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'scheduler_host_subset_size'
op|'='
name|'len'
op|'('
name|'weighed_hosts'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'scheduler_host_subset_size'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'scheduler_host_subset_size'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'chosen_host'
op|'='
name|'random'
op|'.'
name|'choice'
op|'('
nl|'\n'
name|'weighed_hosts'
op|'['
number|'0'
op|':'
name|'scheduler_host_subset_size'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Selected host: %(host)s"'
op|','
op|'{'
string|"'host'"
op|':'
name|'chosen_host'
op|'}'
op|')'
newline|'\n'
name|'selected_hosts'
op|'.'
name|'append'
op|'('
name|'chosen_host'
op|')'
newline|'\n'
nl|'\n'
comment|'# Now consume the resources so the filter/weights'
nl|'\n'
comment|'# will change for the next instance.'
nl|'\n'
name|'chosen_host'
op|'.'
name|'obj'
op|'.'
name|'consume_from_instance'
op|'('
name|'instance_properties'
op|')'
newline|'\n'
name|'if'
name|'update_group_hosts'
name|'is'
name|'True'
op|':'
newline|'\n'
comment|'# NOTE(sbauza): Group details are serialized into a list now'
nl|'\n'
comment|'# that they are populated by the conductor, we need to'
nl|'\n'
comment|'# deserialize them'
nl|'\n'
indent|'                '
name|'if'
name|'isinstance'
op|'('
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'='
name|'set'
op|'('
nl|'\n'
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'filter_properties'
op|'['
string|"'group_hosts'"
op|']'
op|'.'
name|'add'
op|'('
name|'chosen_host'
op|'.'
name|'obj'
op|'.'
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'selected_hosts'
newline|'\n'
nl|'\n'
DECL|member|_get_all_host_states
dedent|''
name|'def'
name|'_get_all_host_states'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Template method, so a subclass can implement caching."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'host_manager'
op|'.'
name|'get_all_host_states'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
