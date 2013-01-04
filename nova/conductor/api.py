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
string|'"""Handles all requests to the conductor service"""'
newline|'\n'
nl|'\n'
name|'import'
name|'functools'
newline|'\n'
nl|'\n'
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
name|'import'
name|'exception'
name|'as'
name|'exc'
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
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
string|"'the topic conductor nodes listen on'"
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
string|"'full class name for the Manager for conductor'"
op|')'
op|','
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
nl|'\n'
DECL|class|ExceptionHelper
name|'class'
name|'ExceptionHelper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class to wrap another and translate the ClientExceptions raised by its\n    function calls to the actual ones"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'target'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_target'
op|'='
name|'target'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'func'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'_target'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'func'
op|')'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rpc_common'
op|'.'
name|'ClientException'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
op|'('
name|'e'
op|'.'
name|'_exc_info'
op|'['
number|'1'
op|']'
op|','
name|'None'
op|','
name|'e'
op|'.'
name|'_exc_info'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalAPI
dedent|''
dedent|''
name|'class'
name|'LocalAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A local version of the conductor API that does database updates\n    locally instead of via RPC"""'
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
string|'"""Perform an instance update in the database"""'
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
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_by_uuid
dedent|''
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
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
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all
dedent|''
name|'def'
name|'instance_get_all'
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
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
op|'{'
op|'}'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_filters
dedent|''
name|'def'
name|'instance_get_all_by_filters'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|'='
string|"'created_at'"
op|','
nl|'\n'
name|'sort_dir'
op|'='
string|"'desc'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|','
nl|'\n'
name|'sort_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_hung_in_rebooting
dedent|''
name|'def'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'context'
op|','
nl|'\n'
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_active_by_window
dedent|''
name|'def'
name|'instance_get_active_by_window'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'host'
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
name|'instance_get_active_by_window'
op|'('
nl|'\n'
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'project_id'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_get
dedent|''
name|'def'
name|'migration_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'migration_get'
op|'('
name|'context'
op|','
name|'migration_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_update
dedent|''
name|'def'
name|'migration_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'migration_update'
op|'('
name|'context'
op|','
name|'migration'
op|','
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_host_add
dedent|''
name|'def'
name|'aggregate_host_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
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
name|'aggregate_host_add'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_host_delete
dedent|''
name|'def'
name|'aggregate_host_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
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
name|'aggregate_host_delete'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get
dedent|''
name|'def'
name|'aggregate_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'aggregate_get'
op|'('
name|'context'
op|','
name|'aggregate_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get_by_host
dedent|''
name|'def'
name|'aggregate_get_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'key'
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
name|'aggregate_get_by_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_add
dedent|''
name|'def'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
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
name|'aggregate_metadata_add'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_delete
dedent|''
name|'def'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'aggregate_metadata_delete'
op|'('
name|'context'
op|','
nl|'\n'
name|'aggregate'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
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
name|'raise'
name|'exc'
op|'.'
name|'InvalidRequest'
newline|'\n'
nl|'\n'
DECL|member|security_group_get_by_instance
dedent|''
name|'def'
name|'security_group_get_by_instance'
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
name|'security_group_get_by_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_rule_get_by_security_group
dedent|''
name|'def'
name|'security_group_rule_get_by_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'secgroup'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'secgroup'
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
DECL|member|agent_build_get_by_triple
dedent|''
name|'def'
name|'agent_build_get_by_triple'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'agent_build_get_by_triple'
op|'('
name|'context'
op|','
name|'hypervisor'
op|','
nl|'\n'
name|'os'
op|','
name|'architecture'
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy
dedent|''
name|'def'
name|'block_device_mapping_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'bdms'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_destroy'
op|'('
name|'context'
op|','
name|'bdms'
op|'='
name|'bdms'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy_by_instance_and_device
dedent|''
name|'def'
name|'block_device_mapping_destroy_by_instance_and_device'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_destroy'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|','
name|'device_name'
op|'='
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy_by_instance_and_volume
dedent|''
name|'def'
name|'block_device_mapping_destroy_by_instance_and_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'block_device_mapping_destroy'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|','
name|'volume_id'
op|'='
name|'volume_id'
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
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Conductor API that does updates via RPC to the ConductorManager"""'
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
name|'conductor_rpcapi'
op|'='
name|'rpcapi'
op|'.'
name|'ConductorAPI'
op|'('
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
op|'**'
name|'updates'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Perform an instance update in the database"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'instance_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
nl|'\n'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_destroy
dedent|''
name|'def'
name|'instance_destroy'
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
name|'conductor_rpcapi'
op|'.'
name|'instance_destroy'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_by_uuid
dedent|''
name|'def'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all
dedent|''
name|'def'
name|'instance_get_all'
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
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
op|'{'
op|'}'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
op|'{'
string|"'host'"
op|':'
name|'host'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_by_filters
dedent|''
name|'def'
name|'instance_get_all_by_filters'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|'='
string|"'created_at'"
op|','
nl|'\n'
name|'sort_dir'
op|'='
string|"'desc'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'instance_get_all_by_filters'
op|'('
name|'context'
op|','
nl|'\n'
name|'filters'
op|','
nl|'\n'
name|'sort_key'
op|','
nl|'\n'
name|'sort_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_all_hung_in_rebooting
dedent|''
name|'def'
name|'instance_get_all_hung_in_rebooting'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'instance_get_all_hung_in_rebooting'
op|'('
nl|'\n'
name|'context'
op|','
name|'timeout'
op|')'
newline|'\n'
nl|'\n'
DECL|member|instance_get_active_by_window
dedent|''
name|'def'
name|'instance_get_active_by_window'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|'='
name|'None'
op|','
nl|'\n'
name|'project_id'
op|'='
name|'None'
op|','
name|'host'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'instance_get_active_by_window'
op|'('
nl|'\n'
name|'context'
op|','
name|'begin'
op|','
name|'end'
op|','
name|'project_id'
op|','
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_get
dedent|''
name|'def'
name|'migration_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'migration_get'
op|'('
name|'context'
op|','
name|'migration_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|migration_update
dedent|''
name|'def'
name|'migration_update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'migration'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'migration_update'
op|'('
name|'context'
op|','
name|'migration'
op|','
nl|'\n'
name|'status'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_host_add
dedent|''
name|'def'
name|'aggregate_host_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_host_add'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_host_delete
dedent|''
name|'def'
name|'aggregate_host_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_host_delete'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get
dedent|''
name|'def'
name|'aggregate_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_get'
op|'('
name|'context'
op|','
name|'aggregate_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_get_by_host
dedent|''
name|'def'
name|'aggregate_get_by_host'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|','
name|'key'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_get_by_host'
op|'('
name|'context'
op|','
name|'host'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_add
dedent|''
name|'def'
name|'aggregate_metadata_add'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_metadata_add'
op|'('
name|'context'
op|','
name|'aggregate'
op|','
nl|'\n'
name|'metadata'
op|','
nl|'\n'
name|'set_delete'
op|')'
newline|'\n'
nl|'\n'
DECL|member|aggregate_metadata_delete
dedent|''
name|'def'
name|'aggregate_metadata_delete'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'aggregate'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'aggregate_metadata_delete'
op|'('
name|'context'
op|','
nl|'\n'
name|'aggregate'
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
name|'conductor_rpcapi'
op|'.'
name|'bw_usage_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'mac'
op|','
nl|'\n'
name|'start_period'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'bw_usage_update'
op|'('
nl|'\n'
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
op|')'
newline|'\n'
nl|'\n'
comment|"#NOTE(mtreinish): This doesn't work on multiple conductors without any"
nl|'\n'
comment|"# topic calculation in conductor_rpcapi. So the host param isn't used"
nl|'\n'
comment|'# currently.'
nl|'\n'
DECL|member|get_backdoor_port
dedent|''
name|'def'
name|'get_backdoor_port'
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
name|'conductor_rpcapi'
op|'.'
name|'get_backdoor_port'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_get_by_instance
dedent|''
name|'def'
name|'security_group_get_by_instance'
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
name|'conductor_rpcapi'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|security_group_rule_get_by_security_group
dedent|''
name|'def'
name|'security_group_rule_get_by_security_group'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'secgroup'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'security_group_rule_get_by_security_group'
op|'('
nl|'\n'
name|'context'
op|','
name|'secgroup'
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
name|'conductor_rpcapi'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|agent_build_get_by_triple
dedent|''
name|'def'
name|'agent_build_get_by_triple'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'hypervisor'
op|','
name|'os'
op|','
name|'architecture'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'agent_build_get_by_triple'
op|'('
name|'context'
op|','
nl|'\n'
name|'hypervisor'
op|','
nl|'\n'
name|'os'
op|','
nl|'\n'
name|'architecture'
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
name|'conductor_rpcapi'
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
name|'conductor_rpcapi'
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
name|'conductor_rpcapi'
op|'.'
name|'block_device_mapping_update_or_create'
op|'('
nl|'\n'
name|'context'
op|','
name|'values'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy
dedent|''
name|'def'
name|'block_device_mapping_destroy'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'bdms'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'block_device_mapping_destroy'
op|'('
name|'context'
op|','
nl|'\n'
name|'bdms'
op|'='
name|'bdms'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy_by_instance_and_device
dedent|''
name|'def'
name|'block_device_mapping_destroy_by_instance_and_device'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'device_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'block_device_mapping_destroy'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|','
name|'device_name'
op|'='
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|block_device_mapping_destroy_by_instance_and_volume
dedent|''
name|'def'
name|'block_device_mapping_destroy_by_instance_and_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'conductor_rpcapi'
op|'.'
name|'block_device_mapping_destroy'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|'='
name|'instance'
op|','
name|'volume_id'
op|'='
name|'volume_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
