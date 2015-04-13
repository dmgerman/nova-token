begin_unit
comment|'#    Copyright 2013 IBM Corp.'
nl|'\n'
comment|'#    Copyright 2013 Red Hat, Inc.'
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
string|'"""Client side of the conductor RPC API."""'
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
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'objects_base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'conductor'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to conductor services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConductorAPI
name|'class'
name|'ConductorAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Client side of the conductor RPC API\n\n    API version history:\n\n    * 1.0 - Initial version.\n    * 1.1 - Added migration_update\n    * 1.2 - Added instance_get_by_uuid and instance_get_all_by_host\n    * 1.3 - Added aggregate_host_add and aggregate_host_delete\n    * 1.4 - Added migration_get\n    * 1.5 - Added bw_usage_update\n    * 1.6 - Added get_backdoor_port()\n    * 1.7 - Added aggregate_get_by_host, aggregate_metadata_add,\n      and aggregate_metadata_delete\n    * 1.8 - Added security_group_get_by_instance and\n      security_group_rule_get_by_security_group\n    * 1.9 - Added provider_fw_rule_get_all\n    * 1.10 - Added agent_build_get_by_triple\n    * 1.11 - Added aggregate_get\n    * 1.12 - Added block_device_mapping_update_or_create\n    * 1.13 - Added block_device_mapping_get_all_by_instance\n    * 1.14 - Added block_device_mapping_destroy\n    * 1.15 - Added instance_get_all_by_filters and\n      instance_get_all_hung_in_rebooting and\n      instance_get_active_by_window\n      Deprecated instance_get_all_by_host\n    * 1.16 - Added instance_destroy\n    * 1.17 - Added instance_info_cache_delete\n    * 1.18 - Added instance_type_get\n    * 1.19 - Added vol_get_usage_by_time and vol_usage_update\n    * 1.20 - Added migration_get_unconfirmed_by_dest_compute\n    * 1.21 - Added service_get_all_by\n    * 1.22 - Added ping\n    * 1.23 - Added instance_get_all\n             Un-Deprecate instance_get_all_by_host\n    * 1.24 - Added instance_get\n    * 1.25 - Added action_event_start and action_event_finish\n    * 1.26 - Added instance_info_cache_update\n    * 1.27 - Added service_create\n    * 1.28 - Added binary arg to service_get_all_by\n    * 1.29 - Added service_destroy\n    * 1.30 - Added migration_create\n    * 1.31 - Added migration_get_in_progress_by_host_and_node\n    * 1.32 - Added optional node to instance_get_all_by_host\n    * 1.33 - Added compute_node_create and compute_node_update\n    * 1.34 - Added service_update\n    * 1.35 - Added instance_get_active_by_window_joined\n    * 1.36 - Added instance_fault_create\n    * 1.37 - Added task_log_get, task_log_begin_task, task_log_end_task\n    * 1.38 - Added service name to instance_update\n    * 1.39 - Added notify_usage_exists\n    * 1.40 - Added security_groups_trigger_handler and\n      security_groups_trigger_members_refresh\n      Remove instance_get_active_by_window\n    * 1.41 - Added fixed_ip_get_by_instance, network_get,\n      instance_floating_address_get_all, quota_commit,\n      quota_rollback\n    * 1.42 - Added get_ec2_ids, aggregate_metadata_get_by_host\n    * 1.43 - Added compute_stop\n    * 1.44 - Added compute_node_delete\n    * 1.45 - Added project_id to quota_commit and quota_rollback\n    * 1.46 - Added compute_confirm_resize\n    * 1.47 - Added columns_to_join to instance_get_all_by_host and\n      instance_get_all_by_filters\n    * 1.48 - Added compute_unrescue\n\n    ... Grizzly supports message version 1.48.  So, any changes to existing\n    methods in 2.x after that point should be done such that they can\n    handle the version_cap being set to 1.48.\n\n    * 1.49 - Added columns_to_join to instance_get_by_uuid\n    * 1.50 - Added object_action() and object_class_action()\n    * 1.51 - Added the \'legacy\' argument to\n             block_device_mapping_get_all_by_instance\n    * 1.52 - Pass instance objects for compute_confirm_resize\n    * 1.53 - Added compute_reboot\n    * 1.54 - Added \'update_cells\' argument to bw_usage_update\n    * 1.55 - Pass instance objects for compute_stop\n    * 1.56 - Remove compute_confirm_resize and\n             migration_get_unconfirmed_by_dest_compute\n    * 1.57 - Remove migration_create()\n    * 1.58 - Remove migration_get()\n\n    ... Havana supports message version 1.58.  So, any changes to existing\n    methods in 1.x after that point should be done such that they can\n    handle the version_cap being set to 1.58.\n\n    * 1.59 - Remove instance_info_cache_update()\n    * 1.60 - Remove aggregate_metadata_add() and aggregate_metadata_delete()\n    * ...  - Remove security_group_get_by_instance() and\n             security_group_rule_get_by_security_group()\n    * 1.61 - Return deleted instance from instance_destroy()\n    * 1.62 - Added object_backport()\n    * 1.63 - Changed the format of values[\'stats\'] from a dict to a JSON string\n             in compute_node_update()\n    * 1.64 - Added use_slave to instance_get_all_filters()\n           - Remove instance_type_get()\n           - Remove aggregate_get()\n           - Remove aggregate_get_by_host()\n           - Remove instance_get()\n           - Remove migration_update()\n           - Remove block_device_mapping_destroy()\n\n    * 2.0  - Drop backwards compatibility\n           - Remove quota_rollback() and quota_commit()\n           - Remove aggregate_host_add() and aggregate_host_delete()\n           - Remove network_migrate_instance_start() and\n             network_migrate_instance_finish()\n           - Remove vol_get_usage_by_time\n\n    ... Icehouse supports message version 2.0.  So, any changes to\n    existing methods in 2.x after that point should be done such\n    that they can handle the version_cap being set to 2.0.\n\n    * Remove instance_destroy()\n    * Remove compute_unrescue()\n    * Remove instance_get_all_by_filters()\n    * Remove instance_get_active_by_window_joined()\n    * Remove instance_fault_create()\n    * Remove action_event_start() and action_event_finish()\n    * Remove instance_get_by_uuid()\n    * Remove agent_build_get_by_triple()\n\n    ... Juno supports message version 2.0.  So, any changes to\n    existing methods in 2.x after that point should be done such\n    that they can handle the version_cap being set to 2.0.\n\n    * 2.1  - Make notify_usage_exists() take an instance object\n    * Remove bw_usage_update()\n    * Remove notify_usage_exists()\n    * Remove get_ec2_ids()\n\n    """'
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.48'"
op|','
nl|'\n'
string|"'havana'"
op|':'
string|"'1.58'"
op|','
nl|'\n'
string|"'icehouse'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
string|"'juno'"
op|':'
string|"'2.0'"
op|','
nl|'\n'
op|'}'
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
name|'super'
op|'('
name|'ConductorAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
op|','
name|'version'
op|'='
string|"'2.0'"
op|')'
newline|'\n'
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'conductor'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'conductor'
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
nl|'\n'
name|'version_cap'
op|'='
name|'version_cap'
op|','
nl|'\n'
name|'serializer'
op|'='
name|'serializer'
op|')'
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
name|'updates'
op|','
nl|'\n'
name|'service'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'updates'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'instance_update'"
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|'='
name|'updates_p'
op|','
nl|'\n'
name|'service'
op|'='
name|'service'
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
nl|'\n'
name|'host'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
nl|'\n'
string|"'migration_get_in_progress_by_host_and_node'"
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'node'
op|'='
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
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'aggregate_metadata_get_by_host'"
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'key'
op|'='
name|'key'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'provider_fw_rule_get_all'"
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
op|','
nl|'\n'
name|'create'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'block_device_mapping_update_or_create'"
op|','
nl|'\n'
name|'values'
op|'='
name|'values'
op|','
name|'create'
op|'='
name|'create'
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
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'block_device_mapping_get_all_by_instance'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|','
name|'legacy'
op|'='
name|'legacy'
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
name|'instance_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'vol_usage_update'"
op|','
nl|'\n'
name|'vol_id'
op|'='
name|'vol_id'
op|','
name|'rd_req'
op|'='
name|'rd_req'
op|','
nl|'\n'
name|'rd_bytes'
op|'='
name|'rd_bytes'
op|','
name|'wr_req'
op|'='
name|'wr_req'
op|','
nl|'\n'
name|'wr_bytes'
op|'='
name|'wr_bytes'
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance_p'
op|','
name|'last_refreshed'
op|'='
name|'last_refreshed'
op|','
nl|'\n'
name|'update_totals'
op|'='
name|'update_totals'
op|')'
newline|'\n'
nl|'\n'
DECL|member|service_get_all_by
dedent|''
name|'def'
name|'service_get_all_by'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|','
name|'binary'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'service_get_all_by'"
op|','
nl|'\n'
name|'topic'
op|'='
name|'topic'
op|','
name|'host'
op|'='
name|'host'
op|','
name|'binary'
op|'='
name|'binary'
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
name|'node'
op|'='
name|'None'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'instance_get_all_by_host'"
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'node'
op|'='
name|'node'
op|','
nl|'\n'
name|'columns_to_join'
op|'='
name|'columns_to_join'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'service_create'"
op|','
name|'values'
op|'='
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'service_destroy'"
op|','
name|'service_id'
op|'='
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'compute_node_create'"
op|','
name|'values'
op|'='
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'node'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'compute_node_update'"
op|','
nl|'\n'
name|'node'
op|'='
name|'node_p'
op|','
name|'values'
op|'='
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
name|'node_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'node'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'compute_node_delete'"
op|','
name|'node'
op|'='
name|'node_p'
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
name|'service_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
comment|"# (NOTE:jichenjc)If we're calling this periodically, it makes no"
nl|'\n'
comment|'# sense for the RPC timeout to be more than the service'
nl|'\n'
comment|'# report interval. Select 5 here is only find a reaonable long'
nl|'\n'
comment|'# interval as threshold.'
nl|'\n'
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'report_interval'
newline|'\n'
name|'if'
name|'timeout'
name|'and'
name|'timeout'
op|'>'
number|'5'
op|':'
newline|'\n'
indent|'            '
name|'timeout'
op|'-='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'timeout'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'timeout'
op|'='
name|'timeout'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'service_update'"
op|','
nl|'\n'
name|'service'
op|'='
name|'service_p'
op|','
name|'values'
op|'='
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'task_log_get'"
op|','
nl|'\n'
name|'task_name'
op|'='
name|'task_name'
op|','
name|'begin'
op|'='
name|'begin'
op|','
name|'end'
op|'='
name|'end'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'state'
op|'='
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'task_log_begin_task'"
op|','
nl|'\n'
name|'task_name'
op|'='
name|'task_name'
op|','
nl|'\n'
name|'begin'
op|'='
name|'begin'
op|','
name|'end'
op|'='
name|'end'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'task_items'
op|'='
name|'task_items'
op|','
name|'message'
op|'='
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
name|'errors'
op|','
nl|'\n'
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'task_log_end_task'"
op|','
nl|'\n'
name|'task_name'
op|'='
name|'task_name'
op|','
name|'begin'
op|'='
name|'begin'
op|','
name|'end'
op|'='
name|'end'
op|','
nl|'\n'
name|'host'
op|'='
name|'host'
op|','
name|'errors'
op|'='
name|'errors'
op|','
name|'message'
op|'='
name|'message'
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
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'args'
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'security_groups_trigger_handler'"
op|','
nl|'\n'
name|'event'
op|'='
name|'event'
op|','
name|'args'
op|'='
name|'args_p'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'security_groups_trigger_members_refresh'"
op|','
nl|'\n'
name|'group_ids'
op|'='
name|'group_ids'
op|')'
newline|'\n'
nl|'\n'
DECL|member|object_class_action
dedent|''
name|'def'
name|'object_class_action'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objname'
op|','
name|'objmethod'
op|','
name|'objver'
op|','
nl|'\n'
name|'args'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'object_class_action'"
op|','
nl|'\n'
name|'objname'
op|'='
name|'objname'
op|','
name|'objmethod'
op|'='
name|'objmethod'
op|','
nl|'\n'
name|'objver'
op|'='
name|'objver'
op|','
name|'args'
op|'='
name|'args'
op|','
name|'kwargs'
op|'='
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|object_action
dedent|''
name|'def'
name|'object_action'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objinst'
op|','
name|'objmethod'
op|','
name|'args'
op|','
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'object_action'"
op|','
name|'objinst'
op|'='
name|'objinst'
op|','
nl|'\n'
name|'objmethod'
op|'='
name|'objmethod'
op|','
name|'args'
op|'='
name|'args'
op|','
name|'kwargs'
op|'='
name|'kwargs'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'object_backport'"
op|','
name|'objinst'
op|'='
name|'objinst'
op|','
nl|'\n'
name|'target_version'
op|'='
name|'target_version'
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
string|'"""Client side of the conductor \'compute\' namespaced RPC API\n\n    API version history:\n\n    1.0 - Initial version (empty).\n    1.1 - Added unified migrate_server call.\n    1.2 - Added build_instances\n    1.3 - Added unshelve_instance\n    1.4 - Added reservations to migrate_server.\n    1.5 - Added the leagacy_bdm parameter to build_instances\n    1.6 - Made migrate_server use instance objects\n    1.7 - Do not send block_device_mapping and legacy_bdm to build_instances\n    1.8 - Add rebuild_instance\n    1.9 - Converted requested_networks to NetworkRequestList object\n    1.10 - Made migrate_server() and build_instances() send flavor objects\n    1.11 - Added clean_shutdown to migrate_server()\n\n    """'
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
name|'super'
op|'('
name|'ComputeTaskAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'conductor'
op|'.'
name|'topic'
op|','
nl|'\n'
name|'namespace'
op|'='
string|"'compute_task'"
op|','
nl|'\n'
name|'version'
op|'='
string|"'1.0'"
op|')'
newline|'\n'
name|'serializer'
op|'='
name|'objects_base'
op|'.'
name|'NovaObjectSerializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'serializer'
op|'='
name|'serializer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migrate_server
dedent|''
name|'def'
name|'migrate_server'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'scheduler_hint'
op|','
name|'live'
op|','
name|'rebuild'
op|','
nl|'\n'
name|'flavor'
op|','
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'None'
op|','
name|'clean_shutdown'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kw'
op|'='
op|'{'
string|"'instance'"
op|':'
name|'instance'
op|','
string|"'scheduler_hint'"
op|':'
name|'scheduler_hint'
op|','
nl|'\n'
string|"'live'"
op|':'
name|'live'
op|','
string|"'rebuild'"
op|':'
name|'rebuild'
op|','
string|"'flavor'"
op|':'
name|'flavor'
op|','
nl|'\n'
string|"'block_migration'"
op|':'
name|'block_migration'
op|','
nl|'\n'
string|"'disk_over_commit'"
op|':'
name|'disk_over_commit'
op|','
nl|'\n'
string|"'reservations'"
op|':'
name|'reservations'
op|','
nl|'\n'
string|"'clean_shutdown'"
op|':'
name|'clean_shutdown'
op|'}'
newline|'\n'
name|'version'
op|'='
string|"'1.11'"
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'kw'
op|'['
string|"'clean_shutdown'"
op|']'
newline|'\n'
name|'version'
op|'='
string|"'1.10'"
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kw'
op|'['
string|"'flavor'"
op|']'
op|'='
name|'objects_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'flavor'
op|')'
newline|'\n'
name|'version'
op|'='
string|"'1.6'"
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kw'
op|'['
string|"'instance'"
op|']'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
nl|'\n'
name|'objects_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
name|'version'
op|'='
string|"'1.4'"
newline|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'return'
name|'cctxt'
op|'.'
name|'call'
op|'('
name|'context'
op|','
string|"'migrate_server'"
op|','
op|'**'
name|'kw'
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
name|'image_p'
op|'='
name|'jsonutils'
op|'.'
name|'to_primitive'
op|'('
name|'image'
op|')'
newline|'\n'
name|'version'
op|'='
string|"'1.10'"
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.9'"
newline|'\n'
name|'if'
string|"'instance_type'"
name|'in'
name|'filter_properties'
op|':'
newline|'\n'
indent|'                '
name|'flavor'
op|'='
name|'filter_properties'
op|'['
string|"'instance_type'"
op|']'
newline|'\n'
name|'flavor_p'
op|'='
name|'objects_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'flavor'
op|')'
newline|'\n'
name|'filter_properties'
op|'='
name|'dict'
op|'('
name|'filter_properties'
op|','
nl|'\n'
name|'instance_type'
op|'='
name|'flavor_p'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'kw'
op|'='
op|'{'
string|"'instances'"
op|':'
name|'instances'
op|','
string|"'image'"
op|':'
name|'image_p'
op|','
nl|'\n'
string|"'filter_properties'"
op|':'
name|'filter_properties'
op|','
nl|'\n'
string|"'admin_password'"
op|':'
name|'admin_password'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
name|'injected_files'
op|','
nl|'\n'
string|"'requested_networks'"
op|':'
name|'requested_networks'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
name|'security_groups'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'version'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.8'"
newline|'\n'
name|'kw'
op|'['
string|"'requested_networks'"
op|']'
op|'='
name|'kw'
op|'['
string|"'requested_networks'"
op|']'
op|'.'
name|'as_tuples'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
string|"'1.7'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
string|"'1.5'"
newline|'\n'
name|'bdm_p'
op|'='
name|'objects_base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'block_device_mapping'
op|')'
newline|'\n'
name|'kw'
op|'.'
name|'update'
op|'('
op|'{'
string|"'block_device_mapping'"
op|':'
name|'bdm_p'
op|','
nl|'\n'
string|"'legacy_bdm'"
op|':'
name|'legacy_bdm'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
string|"'build_instances'"
op|','
op|'**'
name|'kw'
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
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.3'"
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
string|"'unshelve_instance'"
op|','
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
name|'ctxt'
op|','
name|'instance'
op|','
name|'new_pass'
op|','
name|'injected_files'
op|','
nl|'\n'
name|'image_ref'
op|','
name|'orig_image_ref'
op|','
name|'orig_sys_metadata'
op|','
name|'bdms'
op|','
nl|'\n'
name|'recreate'
op|'='
name|'False'
op|','
name|'on_shared_storage'
op|'='
name|'False'
op|','
name|'host'
op|'='
name|'None'
op|','
nl|'\n'
name|'preserve_ephemeral'
op|'='
name|'False'
op|','
name|'kwargs'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
string|"'1.8'"
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'rebuild_instance'"
op|','
nl|'\n'
name|'instance'
op|'='
name|'instance'
op|','
name|'new_pass'
op|'='
name|'new_pass'
op|','
nl|'\n'
name|'injected_files'
op|'='
name|'injected_files'
op|','
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
name|'bdms'
op|'='
name|'bdms'
op|','
nl|'\n'
name|'recreate'
op|'='
name|'recreate'
op|','
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
