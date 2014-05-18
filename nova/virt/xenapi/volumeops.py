begin_unit
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright (c) 2013 OpenStack Foundation'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'volume_utils'
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
string|'"""Management class for Volume-related tasks."""'
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
name|'_session'
op|'='
name|'session'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|','
nl|'\n'
name|'hotplug'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume to VM instance."""'
newline|'\n'
comment|'#TODO(johngarbutt) move this into _attach_volume_to_vm'
nl|'\n'
name|'dev_number'
op|'='
name|'volume_utils'
op|'.'
name|'get_device_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
nl|'\n'
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_attach_volume'
op|'('
name|'connection_info'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'instance_name'
op|','
name|'dev_number'
op|','
name|'hotplug'
op|')'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
dedent|''
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Attach volume to hypervisor, but not the VM."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_attach_volume'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume
dedent|''
name|'def'
name|'_attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'vm_ref'
op|'='
name|'None'
op|','
name|'instance_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'dev_number'
op|'='
name|'None'
op|','
name|'hotplug'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_check_is_supported_driver_type'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
name|'connection_data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'sr_ref'
op|','
name|'sr_uuid'
op|'='
name|'self'
op|'.'
name|'_connect_to_volume_provider'
op|'('
name|'connection_data'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'self'
op|'.'
name|'_connect_hypervisor_to_volume'
op|'('
name|'sr_ref'
op|','
nl|'\n'
name|'connection_data'
op|')'
newline|'\n'
name|'vdi_uuid'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VDI'
op|'.'
name|'get_uuid'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Connected volume (vdi_uuid): %s'"
op|')'
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vm_ref'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_attach_volume_to_vm'
op|'('
name|'vdi_ref'
op|','
name|'vm_ref'
op|','
name|'instance_name'
op|','
nl|'\n'
name|'dev_number'
op|','
name|'hotplug'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'('
name|'sr_uuid'
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): Forgetting the SR will have the effect of'
nl|'\n'
comment|'# cleaning up the VDI and VBD records, so no need to handle'
nl|'\n'
comment|'# that explicitly.'
nl|'\n'
indent|'                '
name|'volume_utils'
op|'.'
name|'forget_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_is_supported_driver_type
dedent|''
dedent|''
dedent|''
name|'def'
name|'_check_is_supported_driver_type'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'driver_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
newline|'\n'
name|'if'
name|'driver_type'
name|'not'
name|'in'
op|'['
string|"'iscsi'"
op|','
string|"'xensm'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeDriverNotFound'
op|'('
name|'driver_type'
op|'='
name|'driver_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_connect_to_volume_provider
dedent|''
dedent|''
name|'def'
name|'_connect_to_volume_provider'
op|'('
name|'self'
op|','
name|'connection_data'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|'='
name|'volume_utils'
op|'.'
name|'parse_sr_info'
op|'('
nl|'\n'
name|'connection_data'
op|','
string|"'Disk-for:%s'"
op|'%'
name|'instance_name'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_by_uuid'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'sr_ref'
op|':'
newline|'\n'
comment|'# introduce SR because not already present'
nl|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'introduce_sr'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_uuid'
op|','
name|'sr_label'
op|','
name|'sr_params'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'('
name|'sr_ref'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_connect_hypervisor_to_volume
dedent|''
name|'def'
name|'_connect_hypervisor_to_volume'
op|'('
name|'self'
op|','
name|'sr_ref'
op|','
name|'connection_data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Connect volume to hypervisor: %s"'
op|')'
op|','
name|'connection_data'
op|')'
newline|'\n'
name|'if'
string|"'vdi_uuid'"
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|','
nl|'\n'
name|'vdi_uuid'
op|'='
name|'connection_data'
op|'['
string|"'vdi_uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
string|"'target_lun'"
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|','
nl|'\n'
name|'target_lun'
op|'='
name|'connection_data'
op|'['
string|"'target_lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(sirp): This will introduce the first VDI in the SR'
nl|'\n'
indent|'            '
name|'vdi_ref'
op|'='
name|'volume_utils'
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
nl|'\n'
dedent|''
name|'return'
name|'vdi_ref'
newline|'\n'
nl|'\n'
DECL|member|_attach_volume_to_vm
dedent|''
name|'def'
name|'_attach_volume_to_vm'
op|'('
name|'self'
op|','
name|'vdi_ref'
op|','
name|'vm_ref'
op|','
name|'instance_name'
op|','
name|'dev_number'
op|','
nl|'\n'
name|'hotplug'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Attach_volume vdi: %(vdi_ref)s vm: %(vm_ref)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
op|'{'
string|"'vdi_ref'"
op|':'
name|'vdi_ref'
op|','
string|"'vm_ref'"
op|':'
name|'vm_ref'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# osvol is added to the vbd so we can spot which vbds are volumes'
nl|'\n'
name|'vbd_ref'
op|'='
name|'vm_utils'
op|'.'
name|'create_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'dev_number'
op|','
name|'bootable'
op|'='
name|'False'
op|','
nl|'\n'
name|'osvol'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'hotplug'
op|':'
newline|'\n'
comment|'# NOTE(johngarbutt) can only call VBD.plug on a running vm'
nl|'\n'
indent|'            '
name|'running'
op|'='
name|'not'
name|'vm_utils'
op|'.'
name|'is_vm_shutdown'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'running'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Plugging VBD: %s"'
op|')'
op|'%'
name|'vbd_ref'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VBD'
op|'.'
name|'plug'
op|'('
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Dev %(dev_number)s attached to'"
nl|'\n'
string|"' instance %(instance_name)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'dev_number'"
op|':'
name|'dev_number'
op|'}'
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
name|'connection_info'
op|','
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach volume storage to VM instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Detach_volume: %(instance_name)s, %(mountpoint)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'vm_ref'
op|'='
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'instance_name'
op|')'
newline|'\n'
nl|'\n'
name|'device_number'
op|'='
name|'volume_utils'
op|'.'
name|'get_device_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'vbd_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_vbd_by_number'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'device_number'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vbd_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|"# NOTE(sirp): If we don't find the VBD then it must have been"
nl|'\n'
comment|'# detached previously.'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Skipping detach because VBD for %s was not found'"
op|')'
op|','
nl|'\n'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_detach_vbds_and_srs'
op|'('
name|'vm_ref'
op|','
op|'['
name|'vbd_ref'
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Mountpoint %(mountpoint)s detached from instance'"
nl|'\n'
string|"' %(instance_name)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'instance_name'"
op|':'
name|'instance_name'
op|','
nl|'\n'
string|"'mountpoint'"
op|':'
name|'mountpoint'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_detach_vbds_and_srs
dedent|''
dedent|''
name|'def'
name|'_detach_vbds_and_srs'
op|'('
name|'self'
op|','
name|'vm_ref'
op|','
name|'vbd_refs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'is_vm_shutdown'
op|'='
name|'vm_utils'
op|'.'
name|'is_vm_shutdown'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
comment|'# find sr before we destroy the vbd'
nl|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_from_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'is_vm_shutdown'
op|':'
newline|'\n'
indent|'                '
name|'vm_utils'
op|'.'
name|'unplug_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'vm_utils'
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
comment|'# Forget (i.e. disconnect) SR only if not in use'
nl|'\n'
name|'volume_utils'
op|'.'
name|'purge_sr'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_all
dedent|''
dedent|''
name|'def'
name|'detach_all'
op|'('
name|'self'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Detach all cinder volumes."""'
newline|'\n'
name|'vbd_refs'
op|'='
name|'self'
op|'.'
name|'_get_all_volume_vbd_refs'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'if'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_detach_vbds_and_srs'
op|'('
name|'vm_ref'
op|','
name|'vbd_refs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_all_volume_vbd_refs
dedent|''
dedent|''
name|'def'
name|'_get_all_volume_vbd_refs'
op|'('
name|'self'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return VBD refs for all Nova/Cinder volumes."""'
newline|'\n'
name|'vbd_refs'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VM'
op|'.'
name|'get_VBDs'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'other_config'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VBD'
op|'.'
name|'get_other_config'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
name|'if'
name|'other_config'
op|'.'
name|'get'
op|'('
string|"'osvol'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'yield'
name|'vbd_ref'
newline|'\n'
nl|'\n'
DECL|member|find_bad_volumes
dedent|''
dedent|''
dedent|''
name|'def'
name|'find_bad_volumes'
op|'('
name|'self'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find any volumes with their connection severed.\n\n        Certain VM operations (e.g. `VM.start`, `VM.reboot`, etc.) will not\n        work when a VBD is present that points to a non-working volume. To work\n        around this, we scan for non-working volumes and detach them before\n        retrying a failed operation.\n        """'
newline|'\n'
name|'bad_devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'vbd_refs'
op|'='
name|'self'
op|'.'
name|'_get_all_volume_vbd_refs'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'volume_utils'
op|'.'
name|'find_sr_from_vbd'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# TODO(sirp): bug1152401 This relies on a 120 sec timeout'
nl|'\n'
comment|'# within XenServer, update this to fail-fast when this is fixed'
nl|'\n'
comment|'# upstream'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'_session'
op|'.'
name|'SR'
op|'.'
name|'scan'
op|'('
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'SR_BACKEND_FAILURE_40'"
op|':'
newline|'\n'
indent|'                    '
name|'device'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'VBD'
op|'.'
name|'get_device'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
name|'bad_devices'
op|'.'
name|'append'
op|'('
string|"'/dev/%s'"
op|'%'
name|'device'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'bad_devices'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
