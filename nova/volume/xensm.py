begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'driver'
name|'import'
name|'VolumeDriver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi_conn'
name|'import'
name|'XenAPISession'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volumeops'
name|'import'
name|'VolumeOps'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.volume.xensm"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenSMDriver
name|'class'
name|'XenSMDriver'
op|'('
name|'VolumeDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_convert_config_params
indent|'    '
name|'def'
name|'_convert_config_params'
op|'('
name|'self'
op|','
name|'conf_str'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'dict'
op|'('
op|'['
name|'item'
op|'.'
name|'split'
op|'('
string|'"="'
op|')'
name|'for'
name|'item'
name|'in'
name|'conf_str'
op|'.'
name|'split'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'params'
newline|'\n'
nl|'\n'
DECL|member|_get_introduce_sr_keys
dedent|''
name|'def'
name|'_get_introduce_sr_keys'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'name_label'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'params'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
dedent|''
name|'keys'
op|'='
name|'params'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'keys'
op|'.'
name|'append'
op|'('
string|"'sr_type'"
op|')'
newline|'\n'
name|'return'
name|'keys'
newline|'\n'
nl|'\n'
DECL|member|_create_storage_repo
dedent|''
name|'def'
name|'_create_storage_repo'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'backend_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Either creates or introduces SR on host\n        depending on whether it exists in xapi db."""'
newline|'\n'
name|'params'
op|'='
name|'self'
op|'.'
name|'_convert_config_params'
op|'('
name|'backend_ref'
op|'['
string|"'config_params'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'name_label'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'label'
op|'='
name|'params'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'name_label'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'label'
op|'='
string|"'SR-'"
op|'+'
name|'str'
op|'('
name|'backend_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'['
string|"'sr_type'"
op|']'
op|'='
name|'backend_ref'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'backend_ref'
op|'['
string|"'sr_uuid'"
op|']'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# run the sr create command'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'SR name = %s'"
op|')'
op|'%'
name|'label'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Params: %s'"
op|')'
op|'%'
name|'str'
op|'('
name|'params'
op|')'
op|')'
newline|'\n'
name|'sr_uuid'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'create_sr'
op|'('
name|'label'
op|','
name|'params'
op|')'
newline|'\n'
comment|'# update sr_uuid and created in db'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to create sr %s...continuing"'
op|')'
op|'%'
name|'str'
op|'('
name|'backend_ref'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Create failed'"
op|')'
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
string|"'SR UUID of new SR is: %s'"
op|')'
op|'%'
name|'sr_uuid'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_backend_conf_update'
op|'('
name|'context'
op|','
nl|'\n'
name|'backend_ref'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'dict'
op|'('
name|'sr_uuid'
op|'='
name|'sr_uuid'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to update db"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# sr introduce, if not already done'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'introduce_sr'
op|'('
name|'backend_ref'
op|'['
string|"'sr_uuid'"
op|']'
op|','
name|'label'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Failed to introduce sr %s...continuing"'
op|')'
op|'%'
name|'str'
op|'('
name|'backend_ref'
op|'['
string|"'id'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_storage_repos
dedent|''
dedent|''
dedent|''
name|'def'
name|'_create_storage_repos'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create/Introduce storage repositories at start."""'
newline|'\n'
name|'backends'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_backend_conf_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
name|'for'
name|'backend'
name|'in'
name|'backends'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_create_storage_repo'
op|'('
name|'context'
op|','
name|'backend'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to reach backend %d'"
op|')'
op|'%'
name|'backend'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
dedent|''
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
string|'"""Connect to the hypervisor."""'
newline|'\n'
nl|'\n'
comment|'# This driver leverages Xen storage manager, and hence requires'
nl|'\n'
comment|'# hypervisor to be Xen'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'!='
string|"'xenapi'"
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
string|"'XenSMDriver requires xenapi connection'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'url'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
newline|'\n'
name|'username'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
newline|'\n'
name|'password'
op|'='
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'='
name|'XenAPISession'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'='
name|'VolumeOps'
op|'('
name|'session'
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
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to initiate session"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'super'
op|'('
name|'XenSMDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'execute'
op|'='
name|'utils'
op|'.'
name|'execute'
op|','
nl|'\n'
name|'sync_exec'
op|'='
name|'utils'
op|'.'
name|'execute'
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
DECL|member|do_setup
dedent|''
name|'def'
name|'do_setup'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Setup includes creating or introducing storage repos\n           existing in the database and destroying deleted ones."""'
newline|'\n'
nl|'\n'
comment|'# TODO purge storage repos'
nl|'\n'
name|'self'
op|'.'
name|'ctxt'
op|'='
name|'ctxt'
newline|'\n'
name|'self'
op|'.'
name|'_create_storage_repos'
op|'('
name|'ctxt'
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
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a logical volume. Can optionally return a Dictionary of\n        changes to the volume object to be persisted."""'
newline|'\n'
nl|'\n'
comment|'# For now the scheduling logic will be to try to fit the volume in'
nl|'\n'
comment|'# the first available backend.'
nl|'\n'
comment|'# TODO better scheduling once APIs are in place'
nl|'\n'
name|'sm_vol_rec'
op|'='
name|'None'
newline|'\n'
name|'backends'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_backend_conf_get_all'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|')'
newline|'\n'
name|'for'
name|'backend'
name|'in'
name|'backends'
op|':'
newline|'\n'
comment|'# Ensure that storage repo exists, if not create.'
nl|'\n'
comment|'# This needs to be done because if nova compute and'
nl|'\n'
comment|'# volume are both running on this host, then, as a'
nl|'\n'
comment|'# part of detach_volume, compute could potentially forget SR'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'_create_storage_repo'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'backend'
op|')'
newline|'\n'
name|'sm_vol_rec'
op|'='
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'create_volume_for_sm'
op|'('
name|'volume'
op|','
nl|'\n'
name|'backend'
op|'['
string|"'sr_uuid'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'sm_vol_rec'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Volume will be created in backend - %d'"
op|')'
op|'%'
name|'backend'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'sm_vol_rec'
op|':'
newline|'\n'
comment|'# Update db'
nl|'\n'
indent|'            '
name|'sm_vol_rec'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'sm_vol_rec'
op|'['
string|"'backend_id'"
op|']'
op|'='
name|'backend'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_volume_create'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'sm_vol_rec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to update volume in db"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'else'
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
string|"'Unable to create volume'"
op|')'
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
name|'volume'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'vol_rec'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_volume_get'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# If compute runs on this node, detach could have disconnected SR'
nl|'\n'
indent|'            '
name|'backend_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_backend_conf_get'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'vol_rec'
op|'['
string|"'backend_id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_storage_repo'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'backend_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'delete_volume_for_sm'
op|'('
name|'vol_rec'
op|'['
string|"'vdi_uuid'"
op|']'
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
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to delete vdi"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_volume_delete'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
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
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to delete volume in db"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|local_path
dedent|''
dedent|''
name|'def'
name|'local_path'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|undiscover_volume
dedent|''
name|'def'
name|'undiscover_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Undiscover volume on a remote host."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|discover_volume
dedent|''
name|'def'
name|'discover_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_setup_error
dedent|''
name|'def'
name|'check_for_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Exports the volume."""'
newline|'\n'
comment|'# !!! TODO'
nl|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|remove_export
dedent|''
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an export for a logical volume."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
dedent|''
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Safely, synchronously recreates an export for a logical volume."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|initialize_connection
dedent|''
name|'def'
name|'initialize_connection'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'xensm_properties'
op|'='
name|'dict'
op|'('
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_volume_get'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
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
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to find volume in db"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Keep the volume id key consistent with what ISCSI driver calls it'
nl|'\n'
dedent|''
name|'xensm_properties'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'xensm_properties'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'del'
name|'xensm_properties'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'backend_conf'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'sm_backend_conf_get'
op|'('
name|'self'
op|'.'
name|'ctxt'
op|','
nl|'\n'
name|'xensm_properties'
op|'['
string|"'backend_id'"
op|']'
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
name|'exception'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"Failed to find backend in db"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'params'
op|'='
name|'self'
op|'.'
name|'_convert_config_params'
op|'('
name|'backend_conf'
op|'['
string|"'config_params'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'xensm_properties'
op|'['
string|"'flavor_id'"
op|']'
op|'='
name|'backend_conf'
op|'['
string|"'flavor_id'"
op|']'
newline|'\n'
name|'xensm_properties'
op|'['
string|"'sr_uuid'"
op|']'
op|'='
name|'backend_conf'
op|'['
string|"'sr_uuid'"
op|']'
newline|'\n'
name|'xensm_properties'
op|'['
string|"'sr_type'"
op|']'
op|'='
name|'backend_conf'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
name|'xensm_properties'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'xensm_properties'
op|'['
string|"'introduce_sr_keys'"
op|']'
op|'='
name|'self'
op|'.'
name|'_get_introduce_sr_keys'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'driver_volume_type'"
op|':'
string|"'xensm'"
op|','
nl|'\n'
string|"'data'"
op|':'
name|'xensm_properties'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|terminate_connection
dedent|''
name|'def'
name|'terminate_connection'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
