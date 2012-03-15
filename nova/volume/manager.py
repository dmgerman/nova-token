begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
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
string|'"""\nVolume manager manages creating, attaching, detaching, and persistent storage.\n\nPersistant storage volumes keep their state independent of instances.  You can\nattach to an instance, terminate the instance, spawn a new instance (even\none from a different image) and re-attach the volume with the same data\nintact.\n\n**Related Flags**\n\n:volume_topic:  What :mod:`rpc` topic to listen to (default: `volume`).\n:volume_manager:  The module name of a class derived from\n                  :class:`manager.Manager` (default:\n                  :class:`nova.volume.manager.Manager`).\n:storage_availability_zone:  Defaults to `nova`.\n:volume_driver:  Used by :class:`Manager`.  Defaults to\n                 :class:`nova.volume.driver.ISCSIDriver`.\n:volume_group:  Name of the group that will contain exported volumes (default:\n                `nova-volumes`)\n:num_shell_tries:  Number of times to attempt to run commands (default: 3)\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'import'
name|'manager'
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
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'volume_types'
newline|'\n'
nl|'\n'
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
DECL|variable|volume_manager_opts
name|'volume_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'storage_availability_zone'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'availability zone of this service'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'volume_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.volume.driver.ISCSIDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Driver to use for volume creation'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_local_volumes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'if True, will not discover local volumes'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'volume_force_update_capabilities'"
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
string|"'if True will force update capabilities on each check'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'volume_manager_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeManager
name|'class'
name|'VolumeManager'
op|'('
name|'manager'
op|'.'
name|'SchedulerDependentManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages attachable block storage devices."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'volume_driver'
op|'='
name|'None'
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
string|'"""Load the driver from the one specified in args, or from flags."""'
newline|'\n'
name|'if'
name|'not'
name|'volume_driver'
op|':'
newline|'\n'
indent|'            '
name|'volume_driver'
op|'='
name|'FLAGS'
op|'.'
name|'volume_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'volume_driver'
op|')'
newline|'\n'
name|'super'
op|'('
name|'VolumeManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'service_name'
op|'='
string|"'volume'"
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# NOTE(vish): Implementation specific db handling is done'
nl|'\n'
comment|'#             by the driver.'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'db'
op|'='
name|'self'
op|'.'
name|'db'
newline|'\n'
name|'self'
op|'.'
name|'_last_volume_stats'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do any initialization that needs to be run if this is a\n           standalone service."""'
newline|'\n'
nl|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'do_setup'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'check_for_setup_error'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_all_by_host'
op|'('
name|'ctxt'
op|','
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Re-exporting %s volumes"'
op|')'
op|','
name|'len'
op|'('
name|'volumes'
op|')'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
name|'in'
op|'['
string|"'available'"
op|','
string|"'in-use'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_export'
op|'('
name|'ctxt'
op|','
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"volume %s: skipping export"'
op|')'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and exports the volume."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"volume %s: creating"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
op|'{'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'host'
op|'}'
op|')'
newline|'\n'
comment|"# NOTE(vish): so we don't have to get volume from db again"
nl|'\n'
comment|'#             before passing it to the driver.'
nl|'\n'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'host'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol_name'
op|'='
name|'volume_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vol_size'
op|'='
name|'volume_ref'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %(vol_name)s: creating lv of"'
nl|'\n'
string|'" size %(vol_size)sG"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'snapshot_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'model_update'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'snapshot_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume_from_snapshot'
op|'('
nl|'\n'
name|'volume_ref'
op|','
nl|'\n'
name|'snapshot_ref'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'model_update'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'model_update'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: creating export"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_export'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
name|'if'
name|'model_update'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
name|'model_update'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'utils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'error'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'now'
op|'='
name|'utils'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'launched_at'"
op|':'
name|'now'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: created successfully"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_reset_stats'
op|'('
op|')'
newline|'\n'
name|'return'
name|'volume_id'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes and unexports volume."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'volume_ref'
op|'['
string|"'attach_status'"
op|']'
op|'=='
string|'"attached"'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Volume is still attached"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'!='
name|'self'
op|'.'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Volume is not local to this node"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_reset_stats'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: removing export"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'remove_export'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: deleting"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'delete_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'VolumeIsBusy'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: volume is busy"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'ensure_export'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'utils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'error_deleting'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"volume %s: deleted successfully"'
op|')'
op|','
name|'volume_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and exports the snapshot."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'snapshot_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"snapshot %s: creating"'
op|')'
op|','
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'snap_name'
op|'='
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"snapshot %(snap_name)s: creating"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_snapshot'
op|'('
name|'snapshot_ref'
op|')'
newline|'\n'
name|'if'
name|'model_update'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
name|'snapshot_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'model_update'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'utils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'error'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_ref'
op|'['
string|"'id'"
op|']'
op|','
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'progress'"
op|':'
string|"'100%'"
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"snapshot %s: created successfully"'
op|')'
op|','
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'snapshot_id'
newline|'\n'
nl|'\n'
DECL|member|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes and unexports snapshot."""'
newline|'\n'
name|'context'
op|'='
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
newline|'\n'
name|'snapshot_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_get'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"snapshot %s: deleting"'
op|')'
op|','
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'delete_snapshot'
op|'('
name|'snapshot_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'SnapshotIsBusy'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"snapshot %s: snapshot is busy"'
op|')'
op|','
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'available'"
op|'}'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'utils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'snapshot_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'error_deleting'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'snapshot_destroy'
op|'('
name|'context'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"snapshot %s: deleted successfully"'
op|')'
op|','
name|'snapshot_ref'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'instance_id'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates db to show volume is attached"""'
newline|'\n'
comment|'# TODO(vish): refactor this into a more general "reserve"'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_attached'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume_id'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates db to show volume is detached"""'
newline|'\n'
comment|'# TODO(vish): refactor this into a more general "unreserve"'
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_detached'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|initialize_connection
dedent|''
name|'def'
name|'initialize_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Prepare volume for connection from host represented by connector.\n\n        This method calls the driver initialize_connection and returns\n        it to the caller.  The connector parameter is a dictionary with\n        information about the host that will connect to the volume in the\n        following format::\n\n            {\n                \'ip\': ip,\n                \'initiator\': initiator,\n            }\n\n        ip: the ip address of the connecting machine\n\n        initiator: the iscsi initiator name of the connecting machine.\n        This can be None if the connecting machine does not support iscsi\n        connections.\n\n        driver is responsible for doing any necessary security setup and\n        returning a connection_info dictionary in the following format::\n\n            {\n                \'driver_volume_type\': driver_volume_type,\n                \'data\': data,\n            }\n\n        driver_volume_type: a string to identify the type of volume.  This\n                           can be used by the calling code to determine the\n                           strategy for connecting to the volume. This could\n                           be \'iscsi\', \'rbd\', \'sheepdog\', etc.\n\n        data: this is the data that the calling code will use to connect\n              to the volume. Keep in mind that this will be serialized to\n              json in various places, so it should not contain any non-json\n              data types.\n        """'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'initialize_connection'
op|'('
name|'volume_ref'
op|','
name|'connector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|terminate_connection
dedent|''
name|'def'
name|'terminate_connection'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|','
name|'connector'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cleanup connection from host represented by connector.\n\n        The format of connector is the same as for initialize_connection.\n        """'
newline|'\n'
name|'volume_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'terminate_connection'
op|'('
name|'volume_ref'
op|','
name|'connector'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_export
dedent|''
name|'def'
name|'check_for_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make sure whether volume is exported."""'
newline|'\n'
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'instance_ref'
op|'['
string|"'volumes'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'check_for_export'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_volume_stats_changed
dedent|''
dedent|''
name|'def'
name|'_volume_stats_changed'
op|'('
name|'self'
op|','
name|'stat1'
op|','
name|'stat2'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'FLAGS'
op|'.'
name|'volume_force_update_capabilities'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'stat1'
op|')'
op|'!='
name|'len'
op|'('
name|'stat2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'stat1'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'not'
name|'in'
name|'stat2'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'manager'
op|'.'
name|'periodic_task'
newline|'\n'
DECL|member|_report_driver_status
name|'def'
name|'_report_driver_status'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_stats'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'get_volume_stats'
op|'('
name|'refresh'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'volume_stats'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Checking volume capabilities"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_volume_stats_changed'
op|'('
name|'self'
op|'.'
name|'_last_volume_stats'
op|','
nl|'\n'
name|'volume_stats'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"New capabilities found: %s"'
op|')'
op|','
name|'volume_stats'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_last_volume_stats'
op|'='
name|'volume_stats'
newline|'\n'
nl|'\n'
comment|'# This will grab info about the host and queue it'
nl|'\n'
comment|'# to be sent to the Schedulers.'
nl|'\n'
name|'self'
op|'.'
name|'update_service_capabilities'
op|'('
name|'self'
op|'.'
name|'_last_volume_stats'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# avoid repeating fanouts'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'update_service_capabilities'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_reset_stats
dedent|''
dedent|''
dedent|''
name|'def'
name|'_reset_stats'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Clear capabilities"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_last_volume_stats'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|notification
dedent|''
name|'def'
name|'notification'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'event'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Notification {%s} received"'
op|')'
op|','
name|'event'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_reset_stats'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
