begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
string|'"""Handles all requests to the conductor service."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'baserpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'conductor'
name|'import'
name|'rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LI'
op|','
name|'_LW'
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
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|conductor_opts
name|'conductor_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_local'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Perform nova-conductor operations locally'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'conductor'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The topic on which conductor nodes listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.conductor.manager.ConductorManager'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Full class name for the Manager for conductor'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'workers'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of workers for OpenStack Conductor service. '"
nl|'\n'
string|"'The default will be the number of CPUs available.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
DECL|variable|conductor_group
name|'conductor_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'conductor'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Conductor Options'"
op|')'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_group'
op|'('
name|'conductor_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'conductor_opts'
op|','
name|'conductor_group'
op|')'
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
nl|'\n'
DECL|class|LocalAPI
name|'class'
name|'LocalAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A local version of the conductor API that does database updates\n    locally instead of via RPC.\n    """'
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
comment|'# TODO(danms): This needs to be something more generic for'
nl|'\n'
comment|'# other/future users of this sort of functionality.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'='
name|'utils'
op|'.'
name|'ExceptionHelper'
op|'('
name|'manager'
op|'.'
name|'ConductorManager'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_until_ready
dedent|''
name|'def'
name|'wait_until_ready'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# nothing to wait for in the local case.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform an instance update in the database."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|','
string|"'compute'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_host
dedent|''
name|'def'
name|'instance_get_all_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_get_all_by_host'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'None'
op|','
name|'columns_to_join'
op|'='
name|'columns_to_join'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_host_and_node
dedent|''
name|'def'
name|'instance_get_all_by_host_and_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'node'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_get_in_progress_by_host_and_node
dedent|''
name|'def'
name|'migration_get_in_progress_by_host_and_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'migration_get_in_progress_by_host_and_node'
op|'('
nl|'\n'
name|'context'
op|','
name|'host'
op|','
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_get_by_host
dedent|''
name|'def'
name|'aggregate_metadata_get_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
nl|'\n'
name|'key'
op|'='
string|"'availability_zone'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'aggregate_metadata_get_by_host'
op|'('
name|'context'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bw_usage_get
dedent|''
name|'def'
name|'bw_usage_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'uuid'
op|','
name|'start_period'
op|','
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'bw_usage_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|bw_usage_update
dedent|''
name|'def'
name|'bw_usage_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'bw_in'
op|','
name|'bw_out'
op|','
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|','
nl|'\n'
name|'last_refreshed'
op|'='
name|'None'
op|','
name|'update_cells'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'bw_usage_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
name|'start_period'
op|','
nl|'\n'
name|'bw_in'
op|','
name|'bw_out'
op|','
nl|'\n'
name|'last_ctr_in'
op|','
name|'last_ctr_out'
op|','
nl|'\n'
name|'last_refreshed'
op|','
nl|'\n'
name|'update_cells'
op|'='
name|'update_cells'
op|')'
newline|'\n'
nl|'\n'
DECL|member|provider_fw_rule_get_all
dedent|''
name|'def'
name|'provider_fw_rule_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_create
dedent|''
name|'def'
name|'block_device_mapping_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'values'
op|','
nl|'\n'
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_update
dedent|''
name|'def'
name|'block_device_mapping_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'bdm_id'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
name|'dict'
op|'('
name|'values'
op|')'
newline|'\n'
name|'values'
op|'['
string|"'id'"
op|']'
op|'='
name|'bdm_id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
nl|'\n'
name|'context'
op|','
name|'values'
op|','
name|'create'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_update_or_create
dedent|''
name|'def'
name|'block_device_mapping_update_or_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
name|'context'
op|','
nl|'\n'
name|'values'
op|','
nl|'\n'
name|'create'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_get_all_by_instance
dedent|''
name|'def'
name|'block_device_mapping_get_all_by_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'legacy'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'legacy'
op|')'
newline|'\n'
nl|'\n'
DECL|member|vol_get_usage_by_time
dedent|''
name|'def'
name|'vol_get_usage_by_time'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'start_time'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'vol_get_usage_by_time'
op|'('
name|'context'
op|','
name|'start_time'
op|')'
newline|'\n'
nl|'\n'
DECL|member|vol_usage_update
dedent|''
name|'def'
name|'vol_usage_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vol_id'
op|','
name|'rd_req'
op|','
name|'rd_bytes'
op|','
name|'wr_req'
op|','
nl|'\n'
name|'wr_bytes'
op|','
name|'instance'
op|','
name|'last_refreshed'
op|'='
name|'None'
op|','
nl|'\n'
name|'update_totals'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'vol_usage_update'
op|'('
name|'context'
op|','
name|'vol_id'
op|','
nl|'\n'
name|'rd_req'
op|','
name|'rd_bytes'
op|','
nl|'\n'
name|'wr_req'
op|','
name|'wr_bytes'
op|','
nl|'\n'
name|'instance'
op|','
name|'last_refreshed'
op|','
nl|'\n'
name|'update_totals'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_all
dedent|''
name|'def'
name|'service_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'topic'
op|'='
name|'None'
op|','
nl|'\n'
name|'binary'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_all_by_topic
dedent|''
name|'def'
name|'service_get_all_by_topic'
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
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'host'
op|'='
name|'None'
op|','
name|'binary'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_all_by_host
dedent|''
name|'def'
name|'service_get_all_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'host'
op|','
name|'topic'
op|'='
name|'None'
op|','
nl|'\n'
name|'binary'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_by_host_and_topic
dedent|''
name|'def'
name|'service_get_by_host_and_topic'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
name|'topic'
op|','
name|'host'
op|','
nl|'\n'
name|'binary'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_by_compute_host
dedent|''
name|'def'
name|'service_get_by_compute_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
string|"'compute'"
op|','
name|'host'
op|','
nl|'\n'
name|'binary'
op|'='
name|'None'
op|')'
newline|'\n'
comment|'# FIXME(comstud): A major revision bump to 2.0 should return a'
nl|'\n'
comment|"# single entry, so we should just return 'result' at that point."
nl|'\n'
name|'return'
name|'result'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|service_get_by_args
dedent|''
name|'def'
name|'service_get_by_args'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'binary'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_get_all_by'
op|'('
name|'context'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'binary'
op|'='
name|'binary'
op|','
name|'topic'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_create
dedent|''
name|'def'
name|'service_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_destroy
dedent|''
name|'def'
name|'service_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'service_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_destroy'
op|'('
name|'context'
op|','
name|'service_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_create
dedent|''
name|'def'
name|'compute_node_create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'compute_node_create'
op|'('
name|'context'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_update
dedent|''
name|'def'
name|'compute_node_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'values'
op|','
name|'prune_stats'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(belliott) ignore prune_stats param, it's no longer relevant"
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'compute_node_update'
op|'('
name|'context'
op|','
name|'node'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|compute_node_delete
dedent|''
name|'def'
name|'compute_node_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'compute_node_delete'
op|'('
name|'context'
op|','
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_update
dedent|''
name|'def'
name|'service_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'service'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'service_update'
op|'('
name|'context'
op|','
name|'service'
op|','
name|'values'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_get
dedent|''
name|'def'
name|'task_log_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
name|'state'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'task_log_get'
op|'('
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
nl|'\n'
name|'host'
op|','
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_begin_task
dedent|''
name|'def'
name|'task_log_begin_task'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'task_items'
op|'='
name|'None'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'task_log_begin_task'
op|'('
name|'context'
op|','
name|'task_name'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'task_items'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|task_log_end_task
dedent|''
name|'def'
name|'task_log_end_task'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'task_name'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'errors'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'task_log_end_task'
op|'('
name|'context'
op|','
name|'task_name'
op|','
nl|'\n'
name|'begin'
op|','
name|'end'
op|','
name|'host'
op|','
nl|'\n'
name|'errors'
op|','
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|notify_usage_exists
dedent|''
name|'def'
name|'notify_usage_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'current_period'
op|'='
name|'False'
op|','
nl|'\n'
name|'ignore_missing_network_data'
op|'='
name|'True'
op|','
nl|'\n'
name|'system_metadata'
op|'='
name|'None'
op|','
name|'extra_usage_info'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'notify_usage_exists'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'current_period'
op|','
name|'ignore_missing_network_data'
op|','
nl|'\n'
name|'system_metadata'
op|','
name|'extra_usage_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_groups_trigger_handler
dedent|''
name|'def'
name|'security_groups_trigger_handler'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'event'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'security_groups_trigger_handler'
op|'('
name|'context'
op|','
nl|'\n'
name|'event'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_groups_trigger_members_refresh
dedent|''
name|'def'
name|'security_groups_trigger_members_refresh'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'group_ids'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'security_groups_trigger_members_refresh'
op|'('
name|'context'
op|','
nl|'\n'
name|'group_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_ec2_ids
dedent|''
name|'def'
name|'get_ec2_ids'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'get_ec2_ids'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|object_backport
dedent|''
name|'def'
name|'object_backport'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objinst'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'object_backport'
op|'('
name|'context'
op|','
name|'objinst'
op|','
name|'target_version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalComputeTaskAPI
dedent|''
dedent|''
name|'class'
name|'LocalComputeTaskAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# TODO(danms): This needs to be something more generic for'
nl|'\n'
comment|'# other/future users of this sort of functionality.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'='
name|'utils'
op|'.'
name|'ExceptionHelper'
op|'('
nl|'\n'
name|'manager'
op|'.'
name|'ComputeTaskManager'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|resize_instance
dedent|''
name|'def'
name|'resize_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'extra_instance_updates'
op|','
nl|'\n'
name|'scheduler_hint'
op|','
name|'flavor'
op|','
name|'reservations'
op|','
nl|'\n'
name|'clean_shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(comstud): 'extra_instance_updates' is not used here but is"
nl|'\n'
comment|'# needed for compatibility with the cells_rpcapi version of this'
nl|'\n'
comment|'# method.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'migrate_server'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
name|'live'
op|'='
name|'False'
op|','
name|'rebuild'
op|'='
name|'False'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavor'
op|','
name|'block_migration'
op|'='
name|'None'
op|','
name|'disk_over_commit'
op|'='
name|'None'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'reservations'
op|','
name|'clean_shutdown'
op|'='
name|'clean_shutdown'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migrate_instance
dedent|''
name|'def'
name|'live_migrate_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'host_name'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler_hint'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host_name'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'migrate_server'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
name|'True'
op|','
name|'False'
op|','
name|'None'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
name|'None'
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
name|'context'
op|','
name|'instances'
op|','
name|'image'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'admin_password'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|','
name|'security_groups'
op|','
name|'block_device_mapping'
op|','
nl|'\n'
name|'legacy_bdm'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'build_instances'
op|','
name|'context'
op|','
nl|'\n'
name|'instances'
op|'='
name|'instances'
op|','
name|'image'
op|'='
name|'image'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'security_groups'
op|'='
name|'security_groups'
op|','
nl|'\n'
name|'block_device_mapping'
op|'='
name|'block_device_mapping'
op|','
nl|'\n'
name|'legacy_bdm'
op|'='
name|'legacy_bdm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unshelve_instance
dedent|''
name|'def'
name|'unshelve_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'unshelve_instance'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rebuild_instance
dedent|''
name|'def'
name|'rebuild_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'orig_image_ref'
op|','
name|'image_ref'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'new_pass'
op|','
name|'orig_sys_metadata'
op|','
nl|'\n'
name|'bdms'
op|','
name|'recreate'
op|'='
name|'False'
op|','
name|'on_shared_storage'
op|'='
name|'False'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|'='
name|'False'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'kwargs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# kwargs unused but required for cell compatibility.'
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'rebuild_instance'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|','
nl|'\n'
name|'new_pass'
op|'='
name|'new_pass'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'image_ref'
op|'='
name|'image_ref'
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
name|'orig_image_ref'
op|','
nl|'\n'
name|'orig_sys_metadata'
op|'='
name|'orig_sys_metadata'
op|','
nl|'\n'
name|'bdms'
op|'='
name|'bdms'
op|','
nl|'\n'
name|'recreate'
op|'='
name|'recreate'
op|','
nl|'\n'
name|'on_shared_storage'
op|'='
name|'on_shared_storage'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|'='
name|'preserve_ephemeral'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
dedent|''
dedent|''
name|'class'
name|'API'
op|'('
name|'LocalAPI'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor API that does updates via RPC to the ConductorManager."""'
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
name|'_manager'
op|'='
name|'rpcapi'
op|'.'
name|'ConductorAPI'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'base_rpcapi'
op|'='
name|'baserpc'
op|'.'
name|'BaseAPI'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_until_ready
dedent|''
name|'def'
name|'wait_until_ready'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'early_timeout'
op|'='
number|'10'
op|','
name|'early_attempts'
op|'='
number|'10'
op|')'
op|':'
newline|'\n'
indent|'        '
string|"'''Wait until a conductor service is up and running.\n\n        This method calls the remote ping() method on the conductor topic until\n        it gets a response.  It starts with a shorter timeout in the loop\n        (early_timeout) up to early_attempts number of tries.  It then drops\n        back to the globally configured timeout for rpc calls for each retry.\n        '''"
newline|'\n'
name|'attempt'
op|'='
number|'0'
newline|'\n'
name|'timeout'
op|'='
name|'early_timeout'
newline|'\n'
comment|'# if we show the timeout message, make sure we show a similar'
nl|'\n'
comment|'# message saying that everything is now working to avoid'
nl|'\n'
comment|'# confusion'
nl|'\n'
name|'has_timedout'
op|'='
name|'False'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
comment|'# NOTE(danms): Try ten times with a short timeout, and then punt'
nl|'\n'
comment|'# to the configured RPC timeout after that'
nl|'\n'
indent|'            '
name|'if'
name|'attempt'
op|'=='
name|'early_attempts'
op|':'
newline|'\n'
indent|'                '
name|'timeout'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'attempt'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# NOTE(russellb): This is running during service startup. If we'
nl|'\n'
comment|'# allow an exception to be raised, the service will shut down.'
nl|'\n'
comment|"# This may fail the first time around if nova-conductor wasn't"
nl|'\n'
comment|'# running when this service started.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'base_rpcapi'
op|'.'
name|'ping'
op|'('
name|'context'
op|','
string|"'1.21 GigaWatts'"
op|','
nl|'\n'
name|'timeout'
op|'='
name|'timeout'
op|')'
newline|'\n'
name|'if'
name|'has_timedout'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'nova-conductor connection '"
nl|'\n'
string|"'established successfully'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'messaging'
op|'.'
name|'MessagingTimeout'
op|':'
newline|'\n'
indent|'                '
name|'has_timedout'
op|'='
name|'True'
newline|'\n'
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'Timed out waiting for nova-conductor.  '"
nl|'\n'
string|"'Is it running? Or did this service start '"
nl|'\n'
string|"'before nova-conductor?  '"
nl|'\n'
string|"'Reattempting establishment of '"
nl|'\n'
string|"'nova-conductor connection...'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_update
dedent|''
dedent|''
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform an instance update in the database."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|','
string|"'conductor'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ComputeTaskAPI
dedent|''
dedent|''
name|'class'
name|'ComputeTaskAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""ComputeTask API that queues up compute tasks for nova-conductor."""'
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
name|'conductor_compute_rpcapi'
op|'='
name|'rpcapi'
op|'.'
name|'ComputeTaskAPI'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|resize_instance
dedent|''
name|'def'
name|'resize_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'extra_instance_updates'
op|','
nl|'\n'
name|'scheduler_hint'
op|','
name|'flavor'
op|','
name|'reservations'
op|','
nl|'\n'
name|'clean_shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(comstud): 'extra_instance_updates' is not used here but is"
nl|'\n'
comment|'# needed for compatibility with the cells_rpcapi version of this'
nl|'\n'
comment|'# method.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_compute_rpcapi'
op|'.'
name|'migrate_server'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
name|'live'
op|'='
name|'False'
op|','
name|'rebuild'
op|'='
name|'False'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'flavor'
op|','
name|'block_migration'
op|'='
name|'None'
op|','
name|'disk_over_commit'
op|'='
name|'None'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'reservations'
op|','
name|'clean_shutdown'
op|'='
name|'clean_shutdown'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migrate_instance
dedent|''
name|'def'
name|'live_migrate_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'host_name'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler_hint'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host_name'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'conductor_compute_rpcapi'
op|'.'
name|'migrate_server'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
name|'True'
op|','
name|'False'
op|','
name|'None'
op|','
nl|'\n'
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
name|'None'
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
name|'context'
op|','
name|'instances'
op|','
name|'image'
op|','
name|'filter_properties'
op|','
nl|'\n'
name|'admin_password'
op|','
name|'injected_files'
op|','
name|'requested_networks'
op|','
nl|'\n'
name|'security_groups'
op|','
name|'block_device_mapping'
op|','
name|'legacy_bdm'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_compute_rpcapi'
op|'.'
name|'build_instances'
op|'('
name|'context'
op|','
nl|'\n'
name|'instances'
op|'='
name|'instances'
op|','
name|'image'
op|'='
name|'image'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'admin_password'
op|'='
name|'admin_password'
op|','
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'requested_networks'
op|'='
name|'requested_networks'
op|','
nl|'\n'
name|'security_groups'
op|'='
name|'security_groups'
op|','
nl|'\n'
name|'block_device_mapping'
op|'='
name|'block_device_mapping'
op|','
nl|'\n'
name|'legacy_bdm'
op|'='
name|'legacy_bdm'
op|')'
newline|'\n'
nl|'\n'
DECL|member|unshelve_instance
dedent|''
name|'def'
name|'unshelve_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_compute_rpcapi'
op|'.'
name|'unshelve_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|rebuild_instance
dedent|''
name|'def'
name|'rebuild_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'orig_image_ref'
op|','
name|'image_ref'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'new_pass'
op|','
name|'orig_sys_metadata'
op|','
nl|'\n'
name|'bdms'
op|','
name|'recreate'
op|'='
name|'False'
op|','
name|'on_shared_storage'
op|'='
name|'False'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|'='
name|'False'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'kwargs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# kwargs unused but required for cell compatibility'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'conductor_compute_rpcapi'
op|'.'
name|'rebuild_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|','
nl|'\n'
name|'new_pass'
op|'='
name|'new_pass'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
nl|'\n'
name|'image_ref'
op|'='
name|'image_ref'
op|','
nl|'\n'
name|'orig_image_ref'
op|'='
name|'orig_image_ref'
op|','
nl|'\n'
name|'orig_sys_metadata'
op|'='
name|'orig_sys_metadata'
op|','
nl|'\n'
name|'bdms'
op|'='
name|'bdms'
op|','
nl|'\n'
name|'recreate'
op|'='
name|'recreate'
op|','
nl|'\n'
name|'on_shared_storage'
op|'='
name|'on_shared_storage'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|'='
name|'preserve_ephemeral'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
