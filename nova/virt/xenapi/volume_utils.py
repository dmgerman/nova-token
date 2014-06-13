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
string|'"""\nHelper methods for operations related to the management of volumes,\nand storage repositories\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
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
nl|'\n'
DECL|variable|xenapi_volume_utils_opts
name|'xenapi_volume_utils_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'introduce_vdi_retry_wait'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'20'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds to wait for an SR to settle '"
nl|'\n'
string|"'if the VDI does not exist when first introduced'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'xenapi_volume_utils_opts'
op|','
string|"'xenserver'"
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
DECL|function|_handle_sr_params
name|'def'
name|'_handle_sr_params'
op|'('
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
string|"'id'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'params'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'sr_type'
op|'='
name|'params'
op|'.'
name|'pop'
op|'('
string|"'sr_type'"
op|','
string|"'iscsi'"
op|')'
newline|'\n'
name|'sr_desc'
op|'='
name|'params'
op|'.'
name|'pop'
op|'('
string|"'name_description'"
op|','
string|"''"
op|')'
newline|'\n'
name|'return'
name|'sr_type'
op|','
name|'sr_desc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|introduce_sr
dedent|''
name|'def'
name|'introduce_sr'
op|'('
name|'session'
op|','
name|'sr_uuid'
op|','
name|'label'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Introducing SR %s'"
op|','
name|'label'
op|')'
newline|'\n'
nl|'\n'
name|'sr_type'
op|','
name|'sr_desc'
op|'='
name|'_handle_sr_params'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'SR.introduce'"
op|','
name|'sr_uuid'
op|','
name|'label'
op|','
name|'sr_desc'
op|','
nl|'\n'
name|'sr_type'
op|','
string|"''"
op|','
name|'False'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Creating PBD for SR'"
op|')'
newline|'\n'
name|'pbd_ref'
op|'='
name|'create_pbd'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Plugging SR'"
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"PBD.plug"'
op|','
name|'pbd_ref'
op|')'
newline|'\n'
nl|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.scan"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|forget_sr
dedent|''
name|'def'
name|'forget_sr'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Forgets the storage repository without destroying the VDIs within."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Forgetting SR...'"
op|')'
newline|'\n'
name|'_unplug_pbds'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.forget"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_sr_by_uuid
dedent|''
name|'def'
name|'find_sr_by_uuid'
op|'('
name|'session'
op|','
name|'sr_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the storage repository given a uuid."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_by_uuid"'
op|','
name|'sr_uuid'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'UUID_INVALID'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_sr_from_vbd
dedent|''
dedent|''
name|'def'
name|'find_sr_from_vbd'
op|'('
name|'session'
op|','
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find the SR reference from the VBD reference."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'vdi_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.get_VDI"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_SR"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to find SR from VBD %s'"
op|')'
op|'%'
name|'vbd_ref'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_pbd
dedent|''
name|'def'
name|'create_pbd'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'pbd_rec'
op|'['
string|"'host'"
op|']'
op|'='
name|'session'
op|'.'
name|'host_ref'
newline|'\n'
name|'pbd_rec'
op|'['
string|"'SR'"
op|']'
op|'='
name|'sr_ref'
newline|'\n'
name|'pbd_rec'
op|'['
string|"'device_config'"
op|']'
op|'='
name|'params'
newline|'\n'
name|'pbd_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"PBD.create"'
op|','
name|'pbd_rec'
op|')'
newline|'\n'
name|'return'
name|'pbd_ref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unplug_pbds
dedent|''
name|'def'
name|'_unplug_pbds'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pbds'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_PBDs"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Ignoring exception %(exc)s when getting PBDs'"
nl|'\n'
string|"' for %(sr_ref)s'"
op|')'
op|','
op|'{'
string|"'exc'"
op|':'
name|'exc'
op|','
string|"'sr_ref'"
op|':'
name|'sr_ref'
op|'}'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'pbd'
name|'in'
name|'pbds'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"PBD.unplug"'
op|','
name|'pbd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Ignoring exception %(exc)s when unplugging'"
nl|'\n'
string|"' PBD %(pbd)s'"
op|')'
op|','
op|'{'
string|"'exc'"
op|':'
name|'exc'
op|','
string|"'pbd'"
op|':'
name|'pbd'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_vdi_ref
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_vdi_ref'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|','
name|'target_lun'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'vdi_uuid'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"vdi_uuid: %s"'
op|'%'
name|'vdi_uuid'
op|')'
newline|'\n'
name|'return'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_by_uuid"'
op|','
name|'vdi_uuid'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'target_lun'
op|':'
newline|'\n'
indent|'        '
name|'vdi_refs'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_VDIs"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'for'
name|'curr_ref'
name|'in'
name|'vdi_refs'
op|':'
newline|'\n'
indent|'            '
name|'curr_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_record"'
op|','
name|'curr_ref'
op|')'
newline|'\n'
name|'if'
op|'('
string|"'sm_config'"
name|'in'
name|'curr_rec'
name|'and'
nl|'\n'
string|"'LUNid'"
name|'in'
name|'curr_rec'
op|'['
string|"'sm_config'"
op|']'
name|'and'
nl|'\n'
name|'curr_rec'
op|'['
string|"'sm_config'"
op|']'
op|'['
string|"'LUNid'"
op|']'
op|'=='
name|'str'
op|'('
name|'target_lun'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'curr_ref'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_VDIs"'
op|','
name|'sr_ref'
op|')'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|introduce_vdi
dedent|''
name|'def'
name|'introduce_vdi'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|'='
name|'None'
op|','
name|'target_lun'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Introduce VDI in the host."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'vdi_ref'
op|'='
name|'_get_vdi_ref'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|','
name|'target_lun'
op|')'
newline|'\n'
name|'if'
name|'vdi_ref'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'introduce_vdi_retry_wait'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.scan"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
name|'_get_vdi_ref'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|','
name|'target_lun'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to introduce VDI on SR %s'"
op|')'
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'vdi_ref'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'VDI not found on SR %(sr)s (vdi_uuid '"
nl|'\n'
string|"'%(vdi_uuid)s, target_lun %(target_lun)s)'"
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'sr'"
op|':'
name|'sr_ref'
op|','
string|"'vdi_uuid'"
op|':'
name|'vdi_uuid'
op|','
nl|'\n'
string|"'target_lun'"
op|':'
name|'target_lun'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_record"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'vdi_rec'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'type'
op|'('
name|'vdi_rec'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to get record of VDI %s on'"
op|')'
op|'%'
name|'vdi_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vdi_rec'
op|'['
string|"'managed'"
op|']'
op|':'
newline|'\n'
comment|'# We do not need to introduce the vdi'
nl|'\n'
indent|'        '
name|'return'
name|'vdi_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.introduce"'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'name_label'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'name_description'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'SR'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'type'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'sharable'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'read_only'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'other_config'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'location'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'xenstore_data'"
op|']'
op|','
nl|'\n'
name|'vdi_rec'
op|'['
string|"'sm_config'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to introduce VDI for SR %s'"
op|')'
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|purge_sr
dedent|''
dedent|''
name|'def'
name|'purge_sr'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
comment|'# Make sure no VBDs are referencing the SR VDIs'
nl|'\n'
indent|'    '
name|'vdi_refs'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_VDIs"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'for'
name|'vdi_ref'
name|'in'
name|'vdi_refs'
op|':'
newline|'\n'
indent|'        '
name|'vbd_refs'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_VBDs"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'if'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Cannot purge SR with referenced VDIs'"
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'forget_sr'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_device_number
dedent|''
name|'def'
name|'get_device_number'
op|'('
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'device_number'
op|'='
name|'_mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
newline|'\n'
name|'if'
name|'device_number'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to obtain target information %s'"
op|')'
op|'%'
nl|'\n'
name|'mountpoint'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'device_number'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_sr_info
dedent|''
name|'def'
name|'parse_sr_info'
op|'('
name|'connection_data'
op|','
name|'description'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'label'
op|'='
name|'connection_data'
op|'.'
name|'pop'
op|'('
string|"'name_label'"
op|','
nl|'\n'
string|"'tempSR-%s'"
op|'%'
name|'connection_data'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|')'
op|')'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'sr_uuid'"
name|'not'
name|'in'
name|'connection_data'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'_parse_volume_info'
op|'('
name|'connection_data'
op|')'
newline|'\n'
comment|"# This magic label sounds a lot like 'False Disc' in leet-speak"
nl|'\n'
name|'uuid'
op|'='
string|'"FA15E-D15C-"'
op|'+'
name|'str'
op|'('
name|'params'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'connection_data'
op|'['
string|"'sr_uuid'"
op|']'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'connection_data'
op|'.'
name|'get'
op|'('
string|"'introduce_sr_keys'"
op|','
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
name|'k'
op|']'
op|'='
name|'connection_data'
op|'['
name|'k'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'params'
op|'['
string|"'name_description'"
op|']'
op|'='
name|'connection_data'
op|'.'
name|'get'
op|'('
string|"'name_description'"
op|','
nl|'\n'
name|'description'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'uuid'
op|','
name|'label'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_volume_info
dedent|''
name|'def'
name|'_parse_volume_info'
op|'('
name|'connection_data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse device_path and mountpoint as they can be used by XenAPI.\n    In particular, the mountpoint (e.g. /dev/sdc) must be translated\n    into a numeric literal.\n    """'
newline|'\n'
name|'volume_id'
op|'='
name|'connection_data'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
name|'target_portal'
op|'='
name|'connection_data'
op|'['
string|"'target_portal'"
op|']'
newline|'\n'
name|'target_host'
op|'='
name|'_get_target_host'
op|'('
name|'target_portal'
op|')'
newline|'\n'
name|'target_port'
op|'='
name|'_get_target_port'
op|'('
name|'target_portal'
op|')'
newline|'\n'
name|'target_iqn'
op|'='
name|'connection_data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
nl|'\n'
name|'log_params'
op|'='
op|'{'
nl|'\n'
string|'"vol_id"'
op|':'
name|'volume_id'
op|','
nl|'\n'
string|'"host"'
op|':'
name|'target_host'
op|','
nl|'\n'
string|'"port"'
op|':'
name|'target_port'
op|','
nl|'\n'
string|'"iqn"'
op|':'
name|'target_iqn'
nl|'\n'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'(vol_id,host,port,iqn): '"
nl|'\n'
string|"'(%(vol_id)s,%(host)s,%(port)s,%(iqn)s)'"
op|','
name|'log_params'
op|')'
newline|'\n'
nl|'\n'
name|'if'
op|'('
name|'volume_id'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'target_host'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'target_iqn'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'StorageError'
op|'('
nl|'\n'
name|'reason'
op|'='
name|'_'
op|'('
string|"'Unable to obtain target information %s'"
op|')'
op|'%'
nl|'\n'
name|'connection_data'
op|')'
newline|'\n'
dedent|''
name|'volume_info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'volume_info'
op|'['
string|"'id'"
op|']'
op|'='
name|'volume_id'
newline|'\n'
name|'volume_info'
op|'['
string|"'target'"
op|']'
op|'='
name|'target_host'
newline|'\n'
name|'volume_info'
op|'['
string|"'port'"
op|']'
op|'='
name|'target_port'
newline|'\n'
name|'volume_info'
op|'['
string|"'targetIQN'"
op|']'
op|'='
name|'target_iqn'
newline|'\n'
name|'if'
op|'('
string|"'auth_method'"
name|'in'
name|'connection_data'
name|'and'
nl|'\n'
name|'connection_data'
op|'['
string|"'auth_method'"
op|']'
op|'=='
string|"'CHAP'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_info'
op|'['
string|"'chapuser'"
op|']'
op|'='
name|'connection_data'
op|'['
string|"'auth_username'"
op|']'
newline|'\n'
name|'volume_info'
op|'['
string|"'chappassword'"
op|']'
op|'='
name|'connection_data'
op|'['
string|"'auth_password'"
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'volume_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_mountpoint_to_number
dedent|''
name|'def'
name|'_mountpoint_to_number'
op|'('
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Translate a mountpoint like /dev/sdc into a numeric."""'
newline|'\n'
name|'if'
name|'mountpoint'
op|'.'
name|'startswith'
op|'('
string|"'/dev/'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mountpoint'
op|'='
name|'mountpoint'
op|'['
number|'5'
op|':'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'re'
op|'.'
name|'match'
op|'('
string|"'^[hs]d[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'ord'
op|'('
name|'mountpoint'
op|'['
number|'2'
op|':'
number|'3'
op|']'
op|')'
op|'-'
name|'ord'
op|'('
string|"'a'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'re'
op|'.'
name|'match'
op|'('
string|"'^x?vd[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'ord'
op|'('
name|'mountpoint'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|'-'
name|'ord'
op|'('
string|"'a'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'re'
op|'.'
name|'match'
op|'('
string|"'^[0-9]+$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'string'
op|'.'
name|'atoi'
op|'('
name|'mountpoint'
op|','
number|'10'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Mountpoint cannot be translated: %s'"
op|')'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'return'
op|'-'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_host
dedent|''
dedent|''
name|'def'
name|'_get_target_host'
op|'('
name|'iscsi_string'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve target host."""'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'iscsi_string'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'host'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'host'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'target_host'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_port
dedent|''
name|'def'
name|'_get_target_port'
op|'('
name|'iscsi_string'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve target port."""'
newline|'\n'
name|'if'
name|'iscsi_string'
name|'and'
string|"':'"
name|'in'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'target_port'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_vbd_by_number
dedent|''
name|'def'
name|'find_vbd_by_number'
op|'('
name|'session'
op|','
name|'vm_ref'
op|','
name|'dev_number'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the VBD reference from the device number."""'
newline|'\n'
name|'vbd_refs'
op|'='
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_VBDs'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
name|'requested_device'
op|'='
name|'str'
op|'('
name|'dev_number'
op|')'
newline|'\n'
name|'if'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'vbd_ref'
name|'in'
name|'vbd_refs'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'user_device'
op|'='
name|'session'
op|'.'
name|'VBD'
op|'.'
name|'get_userdevice'
op|'('
name|'vbd_ref'
op|')'
newline|'\n'
name|'if'
name|'user_device'
op|'=='
name|'requested_device'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'vbd_ref'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
string|'"Error looking up VBD %s for %s"'
op|'%'
op|'('
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|','
name|'exc_info'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
