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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|class|StorageError
name|'class'
name|'StorageError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""To raise errors related to SR, VDI, PBD, and VBD commands."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'StorageError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_handle_sr_params
dedent|''
dedent|''
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
DECL|function|create_sr
dedent|''
name|'def'
name|'create_sr'
op|'('
name|'session'
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
name|'_'
op|'('
string|"'Creating SR %s'"
op|')'
op|','
name|'label'
op|')'
newline|'\n'
name|'sr_type'
op|','
name|'sr_desc'
op|'='
name|'_handle_sr_params'
op|'('
name|'params'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.create"'
op|','
nl|'\n'
name|'session'
op|'.'
name|'host_ref'
op|','
nl|'\n'
name|'params'
op|','
nl|'\n'
string|"'0'"
op|','
name|'label'
op|','
name|'sr_desc'
op|','
name|'sr_type'
op|','
string|"''"
op|','
name|'False'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
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
name|'_'
op|'('
string|"'Introducing SR %s'"
op|')'
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
name|'_'
op|'('
string|"'Creating PBD for SR'"
op|')'
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
name|'_'
op|'('
string|"'Plugging SR'"
op|')'
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
string|'"""\n    Forgets the storage repository without destroying the VDIs within\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Forgetting SR...'"
op|')'
op|')'
newline|'\n'
name|'unplug_pbds'
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
string|'"""\n    Return the storage repository given a uuid.\n    """'
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
name|'StorageError'
op|'('
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
DECL|function|unplug_pbds
dedent|''
name|'def'
name|'unplug_pbds'
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
DECL|function|introduce_vdi
dedent|''
dedent|''
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
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.scan"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'if'
name|'vdi_uuid'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"vdi_uuid: %s"'
op|'%'
name|'vdi_uuid'
op|')'
newline|'\n'
name|'vdi_ref'
op|'='
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
indent|'            '
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
indent|'                '
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
indent|'                    '
name|'vdi_ref'
op|'='
name|'curr_ref'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'vdi_ref'
op|'='
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
name|'StorageError'
op|'('
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to get record'"
nl|'\n'
string|"' of VDI %s on'"
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to introduce VDI for SR %s'"
op|')'
nl|'\n'
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
name|'mountpoint_to_number'
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
name|'StorageError'
op|'('
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
name|'parse_volume_info'
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
DECL|function|parse_volume_info
dedent|''
name|'def'
name|'parse_volume_info'
op|'('
name|'connection_data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Parse device_path and mountpoint as they can be used by XenAPI.\n    In particular, the mountpoint (e.g. /dev/sdc) must be translated\n    into a numeric literal.\n    """'
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
name|'_'
op|'('
string|"'(vol_id,host,port,iqn): '"
nl|'\n'
string|"'(%(vol_id)s,%(host)s,%(port)s,%(iqn)s)'"
op|')'
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to obtain target information'"
nl|'\n'
string|"' %s'"
op|')'
op|'%'
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
DECL|function|mountpoint_to_number
dedent|''
name|'def'
name|'mountpoint_to_number'
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
DECL|function|_get_volume_id
dedent|''
dedent|''
name|'def'
name|'_get_volume_id'
op|'('
name|'path_or_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve the volume id from device_path."""'
newline|'\n'
comment|'# If we have the ID and not a path, just return it.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'path_or_id'
op|','
name|'int'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'path_or_id'
newline|'\n'
comment|'# n must contain at least the volume_id'
nl|'\n'
comment|'# :volume- is for remote volumes'
nl|'\n'
comment|'# -volume- is for local volumes'
nl|'\n'
comment|'# see compute/manager->setup_compute_volume'
nl|'\n'
dedent|''
name|'volume_id'
op|'='
name|'path_or_id'
op|'['
name|'path_or_id'
op|'.'
name|'find'
op|'('
string|"':volume-'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'if'
name|'volume_id'
op|'=='
name|'path_or_id'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'path_or_id'
op|'['
name|'path_or_id'
op|'.'
name|'find'
op|'('
string|"'-volume--'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|'.'
name|'replace'
op|'('
string|"'volume--'"
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'volume_id'
op|'.'
name|'replace'
op|'('
string|"'volume-'"
op|','
string|"''"
op|')'
newline|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|'['
number|'0'
op|':'
name|'volume_id'
op|'.'
name|'find'
op|'('
string|"'-'"
op|')'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'int'
op|'('
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_host
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
DECL|function|vbd_plug
dedent|''
name|'def'
name|'vbd_plug'
op|'('
name|'session'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'xenapi-events-'"
op|'+'
name|'vm_ref'
op|')'
newline|'\n'
DECL|function|synchronized_plug
name|'def'
name|'synchronized_plug'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.plug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(johngarbutt) we need to ensure there is only ever one VBD.plug'
nl|'\n'
comment|'# happening at once per VM due to a bug in XenServer 6.1 and 6.2'
nl|'\n'
dedent|''
name|'synchronized_plug'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vbd_unplug
dedent|''
name|'def'
name|'vbd_unplug'
op|'('
name|'session'
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'xenapi-events-'"
op|'+'
name|'vm_ref'
op|')'
newline|'\n'
DECL|function|synchronized_unplug
name|'def'
name|'synchronized_unplug'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VBD.unplug"'
op|','
name|'vbd_ref'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(johngarbutt) we need to ensure there is only ever one VBD.unplug'
nl|'\n'
comment|'# happening at once per VM due to a bug in XenServer 6.1 and 6.2'
nl|'\n'
dedent|''
name|'synchronized_unplug'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
