begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012, Red Hat, Inc.'
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
string|'"""\nClient side of the scheduler manager RPC API.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
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
nl|'\n'
nl|'\n'
DECL|class|SchedulerAPI
name|'class'
name|'SchedulerAPI'
op|'('
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'rpc'
op|'.'
name|'proxy'
op|'.'
name|'RpcProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the scheduler rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n    '''"
newline|'\n'
nl|'\n'
DECL|variable|BASE_RPC_API_VERSION
name|'BASE_RPC_API_VERSION'
op|'='
string|"'1.0'"
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
name|'SchedulerAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'topic'
op|'='
name|'FLAGS'
op|'.'
name|'scheduler_topic'
op|','
nl|'\n'
name|'default_version'
op|'='
name|'self'
op|'.'
name|'BASE_RPC_API_VERSION'
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
name|'ctxt'
op|','
name|'topic'
op|','
name|'request_spec'
op|','
name|'admin_password'
op|','
nl|'\n'
name|'injected_files'
op|','
name|'requested_networks'
op|','
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|','
name|'reservations'
op|','
name|'call'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc_method'
op|'='
name|'self'
op|'.'
name|'call'
name|'if'
name|'call'
name|'else'
name|'self'
op|'.'
name|'cast'
newline|'\n'
name|'return'
name|'rpc_method'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'run_instance'"
op|','
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'request_spec'
op|'='
name|'request_spec'
op|','
name|'admin_password'
op|'='
name|'admin_password'
op|','
nl|'\n'
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
name|'is_first_time'
op|'='
name|'is_first_time'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|','
nl|'\n'
name|'reservations'
op|'='
name|'reservations'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|prep_resize
dedent|''
name|'def'
name|'prep_resize'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'topic'
op|','
name|'instance_uuid'
op|','
name|'instance_type_id'
op|','
name|'image'
op|','
nl|'\n'
name|'update_db'
op|','
name|'request_spec'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'prep_resize'"
op|','
name|'topic'
op|'='
name|'topic'
op|','
nl|'\n'
name|'instance_uuid'
op|'='
name|'instance_uuid'
op|','
name|'instance_type_id'
op|'='
name|'instance_type_id'
op|','
nl|'\n'
name|'image'
op|'='
name|'image'
op|','
name|'update_db'
op|'='
name|'update_db'
op|','
name|'request_spec'
op|'='
name|'request_spec'
op|','
nl|'\n'
name|'filter_properties'
op|'='
name|'filter_properties'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|show_host_resources
dedent|''
name|'def'
name|'show_host_resources'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'show_host_resources'"
op|','
name|'host'
op|'='
name|'host'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'block_migration'
op|','
name|'disk_over_commit'
op|','
nl|'\n'
name|'instance_id'
op|','
name|'dest'
op|','
name|'topic'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(comstud): Call vs cast so we can get exceptions back, otherwise'
nl|'\n'
comment|"# this call in the scheduler driver doesn't return anything."
nl|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'call'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'live_migration'"
op|','
nl|'\n'
name|'block_migration'
op|'='
name|'block_migration'
op|','
nl|'\n'
name|'disk_over_commit'
op|'='
name|'disk_over_commit'
op|','
name|'instance_id'
op|'='
name|'instance_id'
op|','
nl|'\n'
name|'dest'
op|'='
name|'dest'
op|','
name|'topic'
op|'='
name|'topic'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_service_capabilities
dedent|''
name|'def'
name|'update_service_capabilities'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'service_name'
op|','
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fanout_cast'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'make_msg'
op|'('
string|"'update_service_capabilities'"
op|','
nl|'\n'
name|'service_name'
op|'='
name|'service_name'
op|','
name|'host'
op|'='
name|'host'
op|','
nl|'\n'
name|'capabilities'
op|'='
name|'capabilities'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
