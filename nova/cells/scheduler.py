begin_unit
comment|'# Copyright (c) 2012 Rackspace Hosting'
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
string|'"""\nCells Scheduler\n"""'
newline|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'cells'
name|'import'
name|'weights'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_actions'
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
name|'conductor'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
op|'.'
name|'objects'
name|'import'
name|'instance'
name|'as'
name|'instance_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'instance_action'
name|'as'
name|'instance_action_obj'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
name|'scheduler'
name|'import'
name|'rpcapi'
name|'as'
name|'scheduler_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'utils'
name|'as'
name|'scheduler_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|cell_scheduler_opts
name|'cell_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_filter_classes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.cells.filters.all_filters'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Filter classes the cells scheduler should use.  '"
nl|'\n'
string|'\'An entry of "nova.cells.filters.all_filters" \''
nl|'\n'
string|"'maps to all cells filters included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_weight_classes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.cells.weights.all_weighers'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Weigher classes the cells scheduler should use.  '"
nl|'\n'
string|'\'An entry of "nova.cells.weights.all_weighers" \''
nl|'\n'
string|"'maps to all cell weighers included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How many retries when no cells are available.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_retry_delay'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How often to retry in seconds when no cells are '"
nl|'\n'
string|"'available.'"
op|')'
nl|'\n'
op|']'
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
name|'cell_scheduler_opts'
op|','
name|'group'
op|'='
string|"'cells'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CellsScheduler
name|'class'
name|'CellsScheduler'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The cells scheduler."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'msg_runner'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CellsScheduler'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'='
name|'msg_runner'
newline|'\n'
name|'self'
op|'.'
name|'state_manager'
op|'='
name|'msg_runner'
op|'.'
name|'state_manager'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler_rpcapi'
op|'='
name|'scheduler_rpcapi'
op|'.'
name|'SchedulerAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_task_api'
op|'='
name|'conductor'
op|'.'
name|'ComputeTaskAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filter_handler'
op|'='
name|'filters'
op|'.'
name|'CellFilterHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filter_classes'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'scheduler_filter_classes'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weight_handler'
op|'='
name|'weights'
op|'.'
name|'CellWeightHandler'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'weigher_classes'
op|'='
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_matching_classes'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'scheduler_weight_classes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_instances_here
dedent|''
name|'def'
name|'_create_instances_here'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuids'
op|','
name|'instance_properties'
op|','
nl|'\n'
name|'instance_type'
op|','
name|'image'
op|','
name|'security_groups'
op|','
name|'block_device_mapping'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_values'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'instance_properties'
op|')'
newline|'\n'
comment|'# The parent may pass these metadata values as lists, and the'
nl|'\n'
comment|'# create call expects it to be a dict.'
nl|'\n'
name|'instance_values'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'utils'
op|'.'
name|'instance_meta'
op|'('
name|'instance_values'
op|')'
newline|'\n'
name|'sys_metadata'
op|'='
name|'utils'
op|'.'
name|'instance_sys_meta'
op|'('
name|'instance_values'
op|')'
newline|'\n'
comment|'# Make sure the flavor info is set.  It may not have been passed'
nl|'\n'
comment|'# down.'
nl|'\n'
name|'sys_metadata'
op|'='
name|'flavors'
op|'.'
name|'save_flavor_info'
op|'('
name|'sys_metadata'
op|','
name|'instance_type'
op|')'
newline|'\n'
name|'instance_values'
op|'['
string|"'system_metadata'"
op|']'
op|'='
name|'sys_metadata'
newline|'\n'
comment|'# Pop out things that will get set properly when re-creating the'
nl|'\n'
comment|'# instance record.'
nl|'\n'
name|'instance_values'
op|'.'
name|'pop'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'instance_values'
op|'.'
name|'pop'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'instance_values'
op|'.'
name|'pop'
op|'('
string|"'info_cache'"
op|')'
newline|'\n'
name|'instance_values'
op|'.'
name|'pop'
op|'('
string|"'security_groups'"
op|')'
newline|'\n'
nl|'\n'
name|'num_instances'
op|'='
name|'len'
op|'('
name|'instance_uuids'
op|')'
newline|'\n'
name|'for'
name|'i'
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
name|'instance'
op|'='
name|'instance_obj'
op|'.'
name|'Instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
name|'instance_values'
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'uuid'
op|'='
name|'instance_uuid'
newline|'\n'
name|'instance'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create_db_entry_for_new_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
nl|'\n'
name|'instance_type'
op|','
nl|'\n'
name|'image'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'security_groups'
op|','
nl|'\n'
name|'block_device_mapping'
op|','
nl|'\n'
name|'num_instances'
op|','
name|'i'
op|')'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'obj_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_update_at_top'
op|'('
name|'ctxt'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_action_here
dedent|''
dedent|''
name|'def'
name|'_create_action_here'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_uuids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'instance_uuid'
name|'in'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'            '
name|'instance_action_obj'
op|'.'
name|'InstanceAction'
op|'.'
name|'action_start'
op|'('
nl|'\n'
name|'ctxt'
op|','
nl|'\n'
name|'instance_uuid'
op|','
nl|'\n'
name|'instance_actions'
op|'.'
name|'CREATE'
op|','
nl|'\n'
name|'want_result'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_possible_cells
dedent|''
dedent|''
name|'def'
name|'_get_possible_cells'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_child_cells'
op|'('
op|')'
newline|'\n'
name|'our_cell'
op|'='
name|'self'
op|'.'
name|'state_manager'
op|'.'
name|'get_my_state'
op|'('
op|')'
newline|'\n'
comment|'# Include our cell in the list, if we have any capacity info'
nl|'\n'
name|'if'
name|'not'
name|'cells'
name|'or'
name|'our_cell'
op|'.'
name|'capacities'
op|':'
newline|'\n'
indent|'            '
name|'cells'
op|'.'
name|'append'
op|'('
name|'our_cell'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cells'
newline|'\n'
nl|'\n'
DECL|member|_grab_target_cells
dedent|''
name|'def'
name|'_grab_target_cells'
op|'('
name|'self'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cells'
op|'='
name|'self'
op|'.'
name|'_get_possible_cells'
op|'('
op|')'
newline|'\n'
name|'cells'
op|'='
name|'self'
op|'.'
name|'filter_handler'
op|'.'
name|'get_filtered_objects'
op|'('
name|'self'
op|'.'
name|'filter_classes'
op|','
nl|'\n'
name|'cells'
op|','
nl|'\n'
name|'filter_properties'
op|')'
newline|'\n'
comment|"# NOTE(comstud): I know this reads weird, but the 'if's are nested"
nl|'\n'
comment|"# this way to optimize for the common case where 'cells' is a list"
nl|'\n'
comment|'# containing at least 1 entry.'
nl|'\n'
name|'if'
name|'not'
name|'cells'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'cells'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# None means to bypass further scheduling as a filter'
nl|'\n'
comment|'# took care of everything.'
nl|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NoCellsAvailable'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'weighted_cells'
op|'='
name|'self'
op|'.'
name|'weight_handler'
op|'.'
name|'get_weighed_objects'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'weigher_classes'
op|','
name|'cells'
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
string|'"Weighted cells: %(weighted_cells)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'weighted_cells'"
op|':'
name|'weighted_cells'
op|'}'
op|')'
newline|'\n'
name|'target_cells'
op|'='
op|'['
name|'cell'
op|'.'
name|'obj'
name|'for'
name|'cell'
name|'in'
name|'weighted_cells'
op|']'
newline|'\n'
name|'return'
name|'target_cells'
newline|'\n'
nl|'\n'
DECL|member|_run_instance
dedent|''
name|'def'
name|'_run_instance'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'target_cells'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'host_sched_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attempt to schedule instance(s)."""'
newline|'\n'
name|'ctxt'
op|'='
name|'message'
op|'.'
name|'ctxt'
newline|'\n'
name|'request_spec'
op|'='
name|'host_sched_kwargs'
op|'['
string|"'request_spec'"
op|']'
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
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'request_spec'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'security_groups'
op|'='
name|'request_spec'
op|'['
string|"'security_group'"
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
name|'request_spec'
op|'['
string|"'block_device_mapping'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Scheduling with routing_path=%(routing_path)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'routing_path'"
op|':'
name|'message'
op|'.'
name|'routing_path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'target_cell'
name|'in'
name|'target_cells'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'target_cell'
op|'.'
name|'is_me'
op|':'
newline|'\n'
comment|'# Need to create instance DB entries as the host scheduler'
nl|'\n'
comment|'# expects that the instance(s) already exists.'
nl|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_create_instances_here'
op|'('
name|'ctxt'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'instance_properties'
op|','
name|'instance_type'
op|','
name|'image'
op|','
nl|'\n'
name|'security_groups'
op|','
name|'block_device_mapping'
op|')'
newline|'\n'
comment|'# Need to record the create action in the db as the'
nl|'\n'
comment|'# scheduler expects it to already exist.'
nl|'\n'
name|'self'
op|'.'
name|'_create_action_here'
op|'('
name|'ctxt'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'scheduler_rpcapi'
op|'.'
name|'run_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
op|'**'
name|'host_sched_kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'schedule_run_instance'
op|'('
name|'ctxt'
op|','
name|'target_cell'
op|','
nl|'\n'
name|'host_sched_kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Couldn\'t communicate with cell \'%s\'"'
op|')'
op|'%'
nl|'\n'
name|'target_cell'
op|'.'
name|'name'
op|')'
newline|'\n'
comment|'# FIXME(comstud): Would be nice to kick this back up so that'
nl|'\n'
comment|'# the parent cell could retry, if we had a parent.'
nl|'\n'
dedent|''
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"Couldn\'t communicate with any cells"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoCellsAvailable'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_build_instances
dedent|''
name|'def'
name|'_build_instances'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'target_cells'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'build_inst_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attempt to build instance(s) or send msg to child cell."""'
newline|'\n'
name|'ctxt'
op|'='
name|'message'
op|'.'
name|'ctxt'
newline|'\n'
name|'instance_properties'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'instances'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'filter_properties'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'filter_properties'"
op|']'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'image'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'security_groups'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'security_groups'"
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'block_device_mapping'"
op|']'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Building instances with routing_path=%(routing_path)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'routing_path'"
op|':'
name|'message'
op|'.'
name|'routing_path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'target_cell'
name|'in'
name|'target_cells'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'target_cell'
op|'.'
name|'is_me'
op|':'
newline|'\n'
comment|'# Need to create instance DB entries as the conductor'
nl|'\n'
comment|'# expects that the instance(s) already exists.'
nl|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_create_instances_here'
op|'('
name|'ctxt'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'instance_properties'
op|','
name|'instance_type'
op|','
name|'image'
op|','
nl|'\n'
name|'security_groups'
op|','
name|'block_device_mapping'
op|')'
newline|'\n'
comment|'# Need to record the create action in the db as the'
nl|'\n'
comment|'# conductor expects it to already exist.'
nl|'\n'
name|'self'
op|'.'
name|'_create_action_here'
op|'('
name|'ctxt'
op|','
name|'instance_uuids'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_task_api'
op|'.'
name|'build_instances'
op|'('
name|'ctxt'
op|','
nl|'\n'
op|'**'
name|'build_inst_kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'build_instances'
op|'('
name|'ctxt'
op|','
name|'target_cell'
op|','
nl|'\n'
name|'build_inst_kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Couldn\'t communicate with cell \'%s\'"'
op|')'
op|'%'
nl|'\n'
name|'target_cell'
op|'.'
name|'name'
op|')'
newline|'\n'
comment|'# FIXME(comstud): Would be nice to kick this back up so that'
nl|'\n'
comment|'# the parent cell could retry, if we had a parent.'
nl|'\n'
dedent|''
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|'"Couldn\'t communicate with any cells"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NoCellsAvailable'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|build_instances
dedent|''
name|'def'
name|'build_instances'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'build_inst_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'instance_uuids'
op|'='
op|'['
name|'inst'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'inst'
name|'in'
nl|'\n'
name|'build_inst_kwargs'
op|'['
string|"'instances'"
op|']'
op|']'
newline|'\n'
name|'instances'
op|'='
name|'build_inst_kwargs'
op|'['
string|"'instances'"
op|']'
newline|'\n'
name|'request_spec'
op|'='
name|'scheduler_utils'
op|'.'
name|'build_request_spec'
op|'('
name|'message'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'image'
op|','
name|'instances'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'build_inst_kwargs'
op|'['
string|"'filter_properties'"
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'.'
name|'update'
op|'('
op|'{'
string|"'context'"
op|':'
name|'message'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'scheduler'"
op|':'
name|'self'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
name|'message'
op|'.'
name|'routing_path'
op|','
nl|'\n'
string|"'host_sched_kwargs'"
op|':'
name|'build_inst_kwargs'
op|','
nl|'\n'
string|"'request_spec'"
op|':'
name|'request_spec'
op|'}'
op|')'
newline|'\n'
comment|'# NOTE(belliott) remove when deprecated schedule_run_instance'
nl|'\n'
comment|'# code gets removed.'
nl|'\n'
name|'filter_properties'
op|'['
string|"'cell_scheduler_method'"
op|']'
op|'='
string|"'build_instances'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_schedule_build_to_cells'
op|'('
name|'message'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'self'
op|'.'
name|'_build_instances'
op|','
name|'build_inst_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_instance
dedent|''
name|'def'
name|'run_instance'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'host_sched_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request_spec'
op|'='
name|'host_sched_kwargs'
op|'['
string|"'request_spec'"
op|']'
newline|'\n'
name|'instance_uuids'
op|'='
name|'request_spec'
op|'['
string|"'instance_uuids'"
op|']'
newline|'\n'
name|'filter_properties'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'host_sched_kwargs'
op|'['
string|"'filter_properties'"
op|']'
op|')'
newline|'\n'
name|'filter_properties'
op|'.'
name|'update'
op|'('
op|'{'
string|"'context'"
op|':'
name|'message'
op|'.'
name|'ctxt'
op|','
nl|'\n'
string|"'scheduler'"
op|':'
name|'self'
op|','
nl|'\n'
string|"'routing_path'"
op|':'
name|'message'
op|'.'
name|'routing_path'
op|','
nl|'\n'
string|"'host_sched_kwargs'"
op|':'
name|'host_sched_kwargs'
op|','
nl|'\n'
string|"'request_spec'"
op|':'
name|'request_spec'
op|'}'
op|')'
newline|'\n'
comment|'# NOTE(belliott) remove when deprecated schedule_run_instance'
nl|'\n'
comment|'# code gets removed.'
nl|'\n'
name|'filter_properties'
op|'['
string|"'cell_scheduler_method'"
op|']'
op|'='
string|"'schedule_run_instance'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_schedule_build_to_cells'
op|'('
name|'message'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'self'
op|'.'
name|'_run_instance'
op|','
name|'host_sched_kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_schedule_build_to_cells
dedent|''
name|'def'
name|'_schedule_build_to_cells'
op|'('
name|'self'
op|','
name|'message'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'method'
op|','
name|'method_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Pick a cell where we should create a new instance(s)."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'scheduler_retries'
op|')'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'target_cells'
op|'='
name|'self'
op|'.'
name|'_grab_target_cells'
op|'('
name|'filter_properties'
op|')'
newline|'\n'
name|'if'
name|'target_cells'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# a filter took care of scheduling.  skip.'
nl|'\n'
indent|'                        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'method'
op|'('
name|'message'
op|','
name|'target_cells'
op|','
name|'instance_uuids'
op|','
nl|'\n'
name|'method_kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NoCellsAvailable'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'i'
op|'=='
name|'max'
op|'('
number|'0'
op|','
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'scheduler_retries'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'raise'
newline|'\n'
dedent|''
name|'sleep_time'
op|'='
name|'max'
op|'('
number|'1'
op|','
name|'CONF'
op|'.'
name|'cells'
op|'.'
name|'scheduler_retry_delay'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"No cells available when scheduling.  Will "'
nl|'\n'
string|'"retry in %(sleep_time)s second(s)"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'sleep_time'"
op|':'
name|'sleep_time'
op|'}'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'sleep_time'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
dedent|''
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
name|'_'
op|'('
string|'"Error scheduling instances %(instance_uuids)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_uuids'"
op|':'
name|'instance_uuids'
op|'}'
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'message'
op|'.'
name|'ctxt'
newline|'\n'
name|'for'
name|'instance_uuid'
name|'in'
name|'instance_uuids'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'msg_runner'
op|'.'
name|'instance_update_at_top'
op|'('
name|'ctxt'
op|','
nl|'\n'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|','
nl|'\n'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_update'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_uuid'
op|','
nl|'\n'
op|'{'
string|"'vm_state'"
op|':'
name|'vm_states'
op|'.'
name|'ERROR'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
