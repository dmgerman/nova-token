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
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'HelperBase'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi.volume_utils"'
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
string|'"""To raise errors related to SR, VDI, PBD, and VBD commands"""'
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
DECL|class|VolumeHelper
dedent|''
dedent|''
name|'class'
name|'VolumeHelper'
op|'('
name|'HelperBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The class that wraps the helper methods together.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_sr
name|'def'
name|'create_sr'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'label'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"creating sr within volume_utils"'
op|')'
op|')'
newline|'\n'
name|'type'
op|'='
name|'params'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'type is = %s'"
op|')'
op|'%'
name|'type'
op|')'
newline|'\n'
name|'if'
string|"'name_description'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
name|'params'
op|'['
string|"'name_description'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'name = %s'"
op|')'
op|'%'
name|'desc'
op|')'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'name_description'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'if'
string|"'id'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'params'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'get_xenapi_host'
op|'('
op|')'
op|','
nl|'\n'
name|'params'
op|','
nl|'\n'
string|"'0'"
op|','
name|'label'
op|','
name|'desc'
op|','
name|'type'
op|','
string|"''"
op|','
name|'False'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created %(label)s as %(sr_ref)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to create Storage Repository'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|introduce_sr
name|'def'
name|'introduce_sr'
op|'('
name|'cls'
op|','
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
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"introducing sr within volume_utils"'
op|')'
op|')'
newline|'\n'
name|'type'
op|'='
name|'params'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'sr_type'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'type is = %s'"
op|')'
op|'%'
name|'type'
op|')'
newline|'\n'
name|'if'
string|"'name_description'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
name|'params'
op|'['
string|"'name_description'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'name = %s'"
op|')'
op|'%'
name|'desc'
op|')'
newline|'\n'
name|'del'
name|'params'
op|'['
string|"'name_description'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'desc'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'if'
string|"'id'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'params'
op|'['
string|"'id'"
op|']'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.introduce"'
op|','
nl|'\n'
name|'sr_uuid'
op|','
nl|'\n'
name|'label'
op|','
nl|'\n'
name|'desc'
op|','
nl|'\n'
name|'type'
op|','
nl|'\n'
string|"''"
op|','
nl|'\n'
name|'False'
op|','
nl|'\n'
name|'params'
op|','
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Introduced %(label)s as %(sr_ref)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'#Create pbd'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating pbd for SR'"
op|')'
op|')'
newline|'\n'
name|'pbd_ref'
op|'='
name|'cls'
op|'.'
name|'create_pbd'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'params'
op|')'
newline|'\n'
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
comment|'#Plug pbd'
nl|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"PBD.plug"'
op|','
name|'pbd_ref'
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
name|'return'
name|'sr_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to introduce Storage Repository'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|forget_sr
name|'def'
name|'forget_sr'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Forgets the storage repository without destroying the VDIs within\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sr_ref'
op|'='
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to get SR using uuid'"
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
string|"'Forgetting SR %s...'"
op|')'
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'unplug_pbds'
op|'('
name|'session'
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
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
dedent|''
name|'except'
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to forget Storage Repository'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_sr_by_uuid
name|'def'
name|'find_sr_by_uuid'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the storage repository given a uuid.\n        """'
newline|'\n'
name|'for'
name|'sr_ref'
op|','
name|'sr_rec'
name|'in'
name|'cls'
op|'.'
name|'get_all_refs_and_recs'
op|'('
name|'session'
op|','
string|"'SR'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'sr_rec'
op|'['
string|"'uuid'"
op|']'
op|'=='
name|'sr_uuid'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'sr_ref'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_iscsi_storage
name|'def'
name|'create_iscsi_storage'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'info'
op|','
name|'label'
op|','
name|'description'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create an iSCSI storage repository that will be used to mount\n        the volume for the specified instance\n        """'
newline|'\n'
name|'sr_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_by_name_label"'
op|','
name|'label'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'sr_ref'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Introducing %s...'"
op|')'
op|','
name|'label'
op|')'
newline|'\n'
name|'record'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'chapuser'"
name|'in'
name|'info'
name|'and'
string|"'chappassword'"
name|'in'
name|'info'
op|':'
newline|'\n'
indent|'                '
name|'record'
op|'='
op|'{'
string|"'target'"
op|':'
name|'info'
op|'['
string|"'targetHost'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'info'
op|'['
string|"'targetPort'"
op|']'
op|','
nl|'\n'
string|"'targetIQN'"
op|':'
name|'info'
op|'['
string|"'targetIQN'"
op|']'
op|','
nl|'\n'
string|"'chapuser'"
op|':'
name|'info'
op|'['
string|"'chapuser'"
op|']'
op|','
nl|'\n'
string|"'chappassword'"
op|':'
name|'info'
op|'['
string|"'chappassword'"
op|']'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'record'
op|'='
op|'{'
string|"'target'"
op|':'
name|'info'
op|'['
string|"'targetHost'"
op|']'
op|','
nl|'\n'
string|"'port'"
op|':'
name|'info'
op|'['
string|"'targetPort'"
op|']'
op|','
nl|'\n'
string|"'targetIQN'"
op|':'
name|'info'
op|'['
string|"'targetIQN'"
op|']'
op|'}'
newline|'\n'
dedent|''
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
string|"'Introduced %(label)s as %(sr_ref)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'sr_ref'
newline|'\n'
dedent|''
name|'except'
name|'cls'
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
name|'raise'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to create Storage Repository'"
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'sr_ref'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_sr_from_vbd
name|'def'
name|'find_sr_from_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vbd_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find the SR reference from the VBD reference"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_vbd
name|'def'
name|'create_vbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
op|','
name|'userdevice'
op|','
name|'bootable'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VBD record.  Returns a Deferred that gives the new\n        VBD reference."""'
newline|'\n'
name|'vbd_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'VDI'"
op|']'
op|'='
name|'vdi_ref'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'userdevice'"
op|']'
op|'='
name|'str'
op|'('
name|'userdevice'
op|')'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'bootable'"
op|']'
op|'='
name|'bootable'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'mode'"
op|']'
op|'='
string|"'RW'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'type'"
op|']'
op|'='
string|"'disk'"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'unpluggable'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'empty'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vbd_rec'
op|'['
string|"'qos_supported_algorithms'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Creating VBD for VM %(vm_ref)s,'"
nl|'\n'
string|"' VDI %(vdi_ref)s ... '"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'vbd_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VBD.create'"
op|','
name|'vbd_rec'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Created VBD %(vbd_ref)s for VM %(vm_ref)s,'"
nl|'\n'
string|"' VDI %(vdi_ref)s.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'vbd_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_pbd
name|'def'
name|'create_pbd'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'get_xenapi_host'
op|'('
op|')'
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
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|unplug_pbds
name|'def'
name|'unplug_pbds'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pbds'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
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
string|"'Ignoring exception %(exc)s when getting PBDs'"
nl|'\n'
string|"' for %(sr_ref)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'pbd'
name|'in'
name|'pbds'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
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
name|'cls'
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
name|'warn'
op|'('
name|'_'
op|'('
string|"'Ignoring exception %(exc)s when unplugging'"
nl|'\n'
string|"' PBD %(pbd)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|introduce_vdi
name|'def'
name|'introduce_vdi'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Introduce VDI in the host"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
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
indent|'                '
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
name|'else'
op|':'
newline|'\n'
indent|'                '
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
indent|'            '
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
indent|'            '
name|'return'
name|'vdi_ref'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
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
name|'cls'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
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
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|purge_sr
name|'def'
name|'purge_sr'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'sr_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"SR.get_record"'
op|','
name|'sr_ref'
op|')'
newline|'\n'
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
dedent|''
name|'except'
name|'StorageError'
op|','
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Error finding vdis in SR %s'"
op|')'
op|'%'
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'vdi_ref'
name|'in'
name|'vdi_refs'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
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
dedent|''
name|'except'
name|'StorageError'
op|','
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
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to find vbd for vdi %s'"
op|')'
op|'%'
nl|'\n'
name|'vdi_ref'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'vbd_refs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'cls'
op|'.'
name|'forget_sr'
op|'('
name|'session'
op|','
name|'sr_rec'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|parse_volume_info
name|'def'
name|'parse_volume_info'
op|'('
name|'cls'
op|','
name|'connection_info'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Parse device_path and mountpoint as they can be used by XenAPI.\n        In particular, the mountpoint (e.g. /dev/sdc) must be translated\n        into a numeric literal.\n        FIXME(armando):\n        As for device_path, currently cannot be used as it is,\n        because it does not contain target information. As for interim\n        solution, target details are passed either via Flags or obtained\n        by iscsiadm. Long-term solution is to add a few more fields to the\n        db in the iscsi_target table with the necessary info and modify\n        the iscsi driver to set them.\n        """'
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
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'volume_id'
op|'='
name|'data'
op|'['
string|"'volume_id'"
op|']'
newline|'\n'
name|'target_portal'
op|'='
name|'data'
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
name|'data'
op|'['
string|"'target_iqn'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'(vol_id,number,host,port,iqn): (%s,%s,%s,%s)'"
op|','
nl|'\n'
name|'volume_id'
op|','
name|'target_host'
op|','
name|'target_port'
op|','
name|'target_iqn'
op|')'
newline|'\n'
name|'if'
op|'('
name|'device_number'
op|'<'
number|'0'
name|'or'
nl|'\n'
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
indent|'            '
name|'raise'
name|'StorageError'
op|'('
name|'_'
op|'('
string|"'Unable to obtain target information'"
nl|'\n'
string|"' %(data)s, %(mountpoint)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'connection_info'
name|'and'
nl|'\n'
name|'connection_info'
op|'['
string|"'auth_method'"
op|']'
op|'=='
string|"'CHAP'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_info'
op|'['
string|"'chapuser'"
op|']'
op|'='
name|'connection_info'
op|'['
string|"'auth_username'"
op|']'
newline|'\n'
name|'volume_info'
op|'['
string|"'chappassword'"
op|']'
op|'='
name|'connection_info'
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
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|mountpoint_to_number
name|'def'
name|'mountpoint_to_number'
op|'('
name|'cls'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Translate a mountpoint like /dev/sdc into a numeric"""'
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
indent|'            '
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
indent|'            '
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
string|"'^vd[a-p]$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'            '
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
string|"'^[0-9]+$'"
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'            '
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
indent|'            '
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
dedent|''
name|'def'
name|'_get_volume_id'
op|'('
name|'path_or_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve the volume id from device_path"""'
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
string|'"""Retrieve target host"""'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
op|'['
number|'0'
op|':'
name|'iscsi_string'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'target_host'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'target_host'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target_port
dedent|''
dedent|''
name|'def'
name|'_get_target_port'
op|'('
name|'iscsi_string'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve target port"""'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
op|'['
name|'iscsi_string'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'target_port'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FLAGS'
op|'.'
name|'target_port'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_iqn
dedent|''
dedent|''
name|'def'
name|'_get_iqn'
op|'('
name|'iscsi_string'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Retrieve target IQN"""'
newline|'\n'
name|'if'
name|'iscsi_string'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'iscsi_string'
newline|'\n'
dedent|''
name|'elif'
name|'iscsi_string'
name|'is'
name|'None'
name|'or'
name|'FLAGS'
op|'.'
name|'iqn_prefix'
op|':'
newline|'\n'
indent|'        '
name|'volume_id'
op|'='
name|'_get_volume_id'
op|'('
name|'id'
op|')'
newline|'\n'
name|'return'
string|"'%s:%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iqn_prefix'
op|','
name|'volume_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_target
dedent|''
dedent|''
name|'def'
name|'_get_target'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Gets iscsi name and portal from volume name and host.\n    For this method to work the following are needed:\n    1) volume_ref[\'host\'] must resolve to something rather than loopback\n    """'
newline|'\n'
name|'volume_ref'
op|'='
name|'db'
op|'.'
name|'volume_get'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_id'
op|')'
newline|'\n'
name|'result'
op|'='
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'r'
op|','
name|'_e'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'iscsiadm'"
op|','
nl|'\n'
string|"'-m'"
op|','
string|"'discovery'"
op|','
nl|'\n'
string|"'-t'"
op|','
string|"'sendtargets'"
op|','
nl|'\n'
string|"'-p'"
op|','
name|'volume_ref'
op|'['
string|"'host'"
op|']'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|','
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
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'volume_name'
op|'='
string|'"volume-%08x"'
op|'%'
name|'volume_id'
newline|'\n'
name|'for'
name|'target'
name|'in'
name|'r'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'FLAGS'
op|'.'
name|'iscsi_ip_prefix'
name|'in'
name|'target'
name|'and'
name|'volume_name'
name|'in'
name|'target'
op|':'
newline|'\n'
indent|'                '
op|'('
name|'location'
op|','
name|'_sep'
op|','
name|'iscsi_name'
op|')'
op|'='
name|'target'
op|'.'
name|'partition'
op|'('
string|'" "'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'iscsi_portal'
op|'='
name|'location'
op|'.'
name|'split'
op|'('
string|'","'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'result'
op|'='
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
endmarker|''
end_unit
