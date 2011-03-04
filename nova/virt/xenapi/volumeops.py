begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nManagement class for Storage-related functions (attach, detach, etc).\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vm_utils'
name|'import'
name|'VMHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volume_utils'
name|'import'
name|'VolumeHelper'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'volume_utils'
name|'import'
name|'StorageError'
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
string|'"nova.virt.xenapi.volumeops"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeOps
name|'class'
name|'VolumeOps'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Management class for Volume-related tasks\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'session'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'session'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'session'
newline|'\n'
comment|'# Load XenAPI module in the helper classes respectively'
nl|'\n'
name|'VolumeHelper'
op|'.'
name|'XenAPI'
op|'='
name|'self'
op|'.'
name|'XenAPI'
newline|'\n'
name|'VMHelper'
op|'.'
name|'XenAPI'
op|'='
name|'self'
op|'.'
name|'XenAPI'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'device_path'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume storage to VM instance"""'
newline|'\n'
comment|'# Before we start, check that the VM exists'
nl|'\n'
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance %s not found'"
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
comment|'# NOTE: No Resource Pool concept so far'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Attach_volume: %(instance_name)s, %(device_path)s,"'
nl|'\n'
string|'" %(mountpoint)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# Create the iSCSI SR, and the PDB through which hosts access SRs.'
nl|'\n'
comment|'# But first, retrieve target info, like Host, IQN, LUN and SCSIID'
nl|'\n'
name|'vol_rec'
op|'='
name|'VolumeHelper'
op|'.'
name|'parse_volume_info'
op|'('
name|'device_path'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'label'
op|'='
string|"'SR-%s'"
op|'%'
name|'vol_rec'
op|'['
string|"'volumeId'"
op|']'
newline|'\n'
name|'description'
op|'='
string|"'Disk-for:%s'"
op|'%'
name|'instance_name'
newline|'\n'
comment|'# Create SR'
nl|'\n'
name|'sr_ref'
op|'='
name|'VolumeHelper'
op|'.'
name|'create_iscsi_storage'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'vol_rec'
op|','
nl|'\n'
name|'label'
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
comment|'# Introduce VDI  and attach VBD to VM'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'VolumeHelper'
op|'.'
name|'introduce_vdi'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'VolumeHelper'
op|'.'
name|'destroy_iscsi_storage'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to create VDI on SR %(sr_ref)s for'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'vbd_ref'
op|'='
name|'VMHelper'
op|'.'
name|'create_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'vol_rec'
op|'['
string|"'deviceNumber'"
op|']'
op|','
nl|'\n'
name|'False'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'VolumeHelper'
op|'.'
name|'destroy_iscsi_storage'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to use SR %(sr_ref)s for'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'task'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'call_xenapi'
op|'('
string|"'Async.VBD.plug'"
op|','
nl|'\n'
name|'vbd_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
op|','
name|'vol_rec'
op|'['
string|"'deviceNumber'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'VolumeHelper'
op|'.'
name|'destroy_iscsi_storage'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'sr_ref'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to attach volume to instance %s'"
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Mountpoint %(mountpoint)s attached to'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volume storage to VM instance"""'
newline|'\n'
comment|'# Before we start, check that the VM exists'
nl|'\n'
name|'vm_ref'
op|'='
name|'VMHelper'
op|'.'
name|'lookup'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'if'
name|'vm_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Instance %s not found'"
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
comment|'# Detach VBD from VM'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(instance_name)s, %(mountpoint)s"'
op|')'
nl|'\n'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'device_number'
op|'='
name|'VolumeHelper'
op|'.'
name|'mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vbd_ref'
op|'='
name|'VMHelper'
op|'.'
name|'find_vbd_by_number'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'device_number'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to locate volume %s'"
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'sr_ref'
op|'='
name|'VolumeHelper'
op|'.'
name|'find_sr_from_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'vbd_ref'
op|')'
newline|'\n'
name|'VMHelper'
op|'.'
name|'unplug_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to detach volume %s'"
op|')'
op|'%'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'VMHelper'
op|'.'
name|'destroy_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StorageError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
comment|'# Forget SR'
nl|'\n'
dedent|''
dedent|''
name|'VolumeHelper'
op|'.'
name|'destroy_iscsi_storage'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Mountpoint %(mountpoint)s detached from'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
