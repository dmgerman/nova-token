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
string|'"""\nVolume manager manages creating, attaching, detaching, and persistent storage.\n\nPersistant storage volumes keep their state independent of instances.  You can\nattach to an instance, terminate the instance, spawn a new instance (even\none from a different image) and re-attach the volume with the same data\nintact.\n\n**Related Flags**\n\n:volume_topic:  What :mod:`rpc` topic to listen to (default: `volume`).\n:volume_manager:  The module name of a class derived from\n                  :class:`manager.Manager` (default:\n                  :class:`nova.volume.manager.AOEManager`).\n:storage_availability_zone:  Defaults to `nova`.\n:volume_driver:  Used by :class:`AOEManager`.  Defaults to\n                 :class:`nova.volume.driver.AOEDriver`.\n:num_shelves:  Number of shelves for AoE (default: 100).\n:num_blades:  Number of vblades per shelf to allocate AoE storage from\n              (default: 16).\n:volume_group:  Name of the group that will contain exported volumes (default:\n                `nova-volumes`)\n:aoe_eth_dev:  Device name the volumes will be exported on (default: `eth0`).\n:num_shell_tries:  Number of times to attempt to run AoE commands (default: 3)\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
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
string|"'nova.volume.manager'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'storage_availability_zone'"
op|','
nl|'\n'
string|"'nova'"
op|','
nl|'\n'
string|"'availability zone of this service'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'volume_driver'"
op|','
string|"'nova.volume.driver.ISCSIDriver'"
op|','
nl|'\n'
string|"'Driver to use for volume creation'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vsa_volume_driver'"
op|','
string|"'nova.volume.san.ZadaraVsaDriver'"
op|','
nl|'\n'
string|"'Driver to use for FE/BE volume creation with VSA'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_boolean'
op|'('
string|"'use_local_volumes'"
op|','
name|'True'
op|','
nl|'\n'
string|"'if True, will not discover local volumes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'volume_state_interval'"
op|','
number|'60'
op|','
nl|'\n'
string|"'Interval in seconds for querying volumes status'"
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
name|'vsa_volume_driver'
op|'='
name|'None'
op|','
nl|'\n'
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
name|'if'
name|'not'
name|'vsa_volume_driver'
op|':'
newline|'\n'
indent|'            '
name|'vsa_volume_driver'
op|'='
name|'FLAGS'
op|'.'
name|'vsa_volume_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'vsadriver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'vsa_volume_driver'
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
name|'vsadriver'
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
comment|'#self._last_host_check = 0'
nl|'\n'
nl|'\n'
DECL|member|_get_driver
dedent|''
name|'def'
name|'_get_driver'
op|'('
name|'self'
op|','
name|'volume_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'volume_ref'
op|'['
string|"'to_vsa_id'"
op|']'
name|'is'
name|'None'
name|'and'
name|'volume_ref'
op|'['
string|"'from_vsa_id'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'driver'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'vsadriver'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
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
name|'self'
op|'.'
name|'driver'
op|'.'
name|'check_for_setup_error'
op|'('
op|')'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume'
op|')'
newline|'\n'
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
DECL|member|create_volumes
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_volumes'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'request_spec'
op|','
name|'availability_zone'
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
string|'"create_volumes called with req=%(request_spec)s, "'
string|'"availability_zone=%(availability_zone)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
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
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'model_update'
op|'='
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
comment|'# except Exception:'
nl|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
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
name|'self'
op|'.'
name|'_notify_vsa'
op|'('
name|'context'
op|','
name|'volume_ref'
op|','
string|"'error'"
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
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
nl|'\n'
name|'self'
op|'.'
name|'_notify_vsa'
op|'('
name|'context'
op|','
name|'volume_ref'
op|','
string|"'available'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'volume_id'
newline|'\n'
nl|'\n'
DECL|member|_notify_vsa
dedent|''
name|'def'
name|'_notify_vsa'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_ref'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'volume_ref'
op|'['
string|"'to_vsa_id'"
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'vsa_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"vsa_volume_created"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"vol_id"'
op|':'
name|'volume_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"vsa_id"'
op|':'
name|'volume_ref'
op|'['
string|"'to_vsa_id'"
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'status'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume_ref'
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
name|'raise'
newline|'\n'
nl|'\n'
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
comment|'# snapshot-related operations are irrelevant for vsadriver'
nl|'\n'
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
string|"'error'"
op|'}'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
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
comment|'# snapshot-related operations are irrelevant for vsadriver'
nl|'\n'
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
name|'Exception'
op|':'
newline|'\n'
indent|'            '
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
name|'raise'
newline|'\n'
nl|'\n'
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
DECL|member|setup_compute_volume
dedent|''
name|'def'
name|'setup_compute_volume'
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
string|'"""Setup remote volume on compute host.\n\n        Returns path to device."""'
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
name|'if'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'=='
name|'self'
op|'.'
name|'host'
name|'and'
name|'FLAGS'
op|'.'
name|'use_local_volumes'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'driver'
op|'.'
name|'local_path'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'driver'
op|'.'
name|'discover_volume'
op|'('
name|'context'
op|','
name|'volume_ref'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|remove_compute_volume
dedent|''
name|'def'
name|'remove_compute_volume'
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
string|'"""Remove remote volume on compute host."""'
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
name|'if'
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|'=='
name|'self'
op|'.'
name|'host'
name|'and'
name|'FLAGS'
op|'.'
name|'use_local_volumes'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'driver'
op|'.'
name|'undiscover_volume'
op|'('
name|'volume_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_export
dedent|''
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
name|'driver'
op|'='
name|'self'
op|'.'
name|'_get_driver'
op|'('
name|'volume'
op|')'
newline|'\n'
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
DECL|member|periodic_tasks
dedent|''
dedent|''
name|'def'
name|'periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
nl|'\n'
name|'error_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_report_driver_status'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Error during report_driver_status(): %s"'
op|')'
op|','
nl|'\n'
name|'unicode'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
name|'error_list'
op|'.'
name|'append'
op|'('
name|'ex'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'VolumeManager'
op|','
name|'self'
op|')'
op|'.'
name|'periodic_tasks'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'error_list'
newline|'\n'
nl|'\n'
DECL|member|_volume_stats_changed
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
comment|'#LOG.info(_("stat1=%s"), stat1)'
nl|'\n'
comment|'#LOG.info(_("stat2=%s"), stat2)'
nl|'\n'
nl|'\n'
indent|'        '
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
DECL|member|_report_driver_status
dedent|''
name|'def'
name|'_report_driver_status'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'#curr_time = time.time()'
nl|'\n'
comment|'#LOG.info(_("Report Volume node status"))'
nl|'\n'
comment|'#if curr_time - self._last_host_check > FLAGS.volume_state_interval:'
nl|'\n'
comment|'#    self._last_host_check = curr_time'
nl|'\n'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Updating volume status"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'volume_stats'
op|'='
name|'self'
op|'.'
name|'vsadriver'
op|'.'
name|'get_volume_stats'
op|'('
name|'refresh'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_volume_stats_changed'
op|'('
name|'self'
op|'.'
name|'_last_volume_stats'
op|','
name|'volume_stats'
op|')'
op|':'
newline|'\n'
indent|'            '
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
indent|'            '
name|'self'
op|'.'
name|'update_service_capabilities'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|notification
dedent|''
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
name|'_last_volume_stats'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
