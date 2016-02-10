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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'oslo_messaging'
name|'as'
name|'messaging'
newline|'\n'
name|'from'
name|'oslo_versionedobjects'
name|'import'
name|'base'
name|'as'
name|'ovo_base'
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
name|'import'
name|'nova'
op|'.'
name|'conf'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
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
comment|"# NOTE(hanlind): This shouldn't be called anymore but leaving it for"
nl|'\n'
comment|'# now just in case. Collect the object version manifest and redirect'
nl|'\n'
comment|'# to the newer backport call.'
nl|'\n'
indent|'        '
name|'object_versions'
op|'='
name|'ovo_base'
op|'.'
name|'obj_tree_get_versions'
op|'('
name|'objinst'
op|'.'
name|'obj_name'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'object_backport_versions'
op|'('
name|'context'
op|','
name|'objinst'
op|','
name|'object_versions'
op|')'
newline|'\n'
nl|'\n'
DECL|member|object_backport_versions
dedent|''
name|'def'
name|'object_backport_versions'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'objinst'
op|','
name|'object_versions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'object_backport_versions'
op|'('
name|'context'
op|','
name|'objinst'
op|','
nl|'\n'
name|'object_versions'
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
nl|'\n'
DECL|class|ComputeTaskAPI
dedent|''
dedent|''
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
