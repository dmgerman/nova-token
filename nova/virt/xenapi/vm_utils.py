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
string|'"""\nHelper methods for operations related to the management of VM records and\ntheir attributes like VDIs, VIFs, as well as their lookup functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
op|'.'
name|'manager'
name|'import'
name|'AuthManager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'power_state'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XENAPI_POWER_STATE
name|'XENAPI_POWER_STATE'
op|'='
op|'{'
nl|'\n'
string|"'Halted'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
nl|'\n'
string|"'Running'"
op|':'
name|'power_state'
op|'.'
name|'RUNNING'
op|','
nl|'\n'
string|"'Paused'"
op|':'
name|'power_state'
op|'.'
name|'PAUSED'
op|','
nl|'\n'
string|"'Suspended'"
op|':'
name|'power_state'
op|'.'
name|'SHUTDOWN'
op|','
comment|'# FIXME'
nl|'\n'
string|"'Crashed'"
op|':'
name|'power_state'
op|'.'
name|'CRASHED'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XenAPI
name|'XenAPI'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMHelper
name|'class'
name|'VMHelper'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The class that wraps the helper methods together.\n    """'
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
name|'return'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|late_import
name|'def'
name|'late_import'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Load the XenAPI module in for helper class, if required.\n        This is to avoid to install the XenAPI library when other\n        hypervisors are used\n        """'
newline|'\n'
name|'global'
name|'XenAPI'
newline|'\n'
name|'if'
name|'XenAPI'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'XenAPI'
op|'='
name|'__import__'
op|'('
string|"'XenAPI'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_vm
name|'def'
name|'create_vm'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'kernel'
op|','
name|'ramdisk'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VM record.  Returns a Deferred that gives the new\n        VM reference."""'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'INSTANCE_TYPES'
op|'['
name|'instance'
op|'.'
name|'instance_type'
op|']'
newline|'\n'
name|'mem'
op|'='
name|'str'
op|'('
name|'long'
op|'('
name|'instance_type'
op|'['
string|"'memory_mb'"
op|']'
op|')'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|')'
newline|'\n'
name|'vcpus'
op|'='
name|'str'
op|'('
name|'instance_type'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'rec'
op|'='
op|'{'
nl|'\n'
string|"'name_label'"
op|':'
name|'instance'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'is_a_template'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'memory_static_min'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'memory_static_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_min'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'memory_dynamic_max'"
op|':'
name|'mem'
op|','
nl|'\n'
string|"'VCPUs_at_startup'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_max'"
op|':'
name|'vcpus'
op|','
nl|'\n'
string|"'VCPUs_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'actions_after_shutdown'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'actions_after_reboot'"
op|':'
string|"'restart'"
op|','
nl|'\n'
string|"'actions_after_crash'"
op|':'
string|"'destroy'"
op|','
nl|'\n'
string|"'PV_bootloader'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_kernel'"
op|':'
name|'kernel'
op|','
nl|'\n'
string|"'PV_ramdisk'"
op|':'
name|'ramdisk'
op|','
nl|'\n'
string|"'PV_args'"
op|':'
string|"'root=/dev/xvda1'"
op|','
nl|'\n'
string|"'PV_bootloader_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'PV_legacy_args'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_policy'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'HVM_boot_params'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'platform'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'PCI_bus'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'recommendations'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'affinity'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'user_version'"
op|':'
string|"'0'"
op|','
nl|'\n'
string|"'other_config'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VM %s...'"
op|','
name|'instance'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'vm_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VM.create'"
op|','
name|'rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VM %s as %s.'"
op|','
name|'instance'
op|'.'
name|'name'
op|','
name|'vm_ref'
op|')'
newline|'\n'
name|'return'
name|'vm_ref'
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
nl|'\n'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Creating VBD for VM %s, VDI %s ... '"
op|','
name|'vm_ref'
op|','
name|'vdi_ref'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VBD %s for VM %s, VDI %s.'"
op|','
name|'vbd_ref'
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'vdi_ref'
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
DECL|member|create_vif
name|'def'
name|'create_vif'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|','
name|'network_ref'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a VIF record.  Returns a Deferred that gives the new\n        VIF reference."""'
newline|'\n'
nl|'\n'
name|'vif_rec'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'device'"
op|']'
op|'='
string|"'0'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'network'"
op|']'
op|'='
name|'network_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'VM'"
op|']'
op|'='
name|'vm_ref'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MAC'"
op|']'
op|'='
name|'mac_address'
newline|'\n'
name|'vif_rec'
op|'['
string|"'MTU'"
op|']'
op|'='
string|"'1500'"
newline|'\n'
name|'vif_rec'
op|'['
string|"'other_config'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_type'"
op|']'
op|'='
string|"''"
newline|'\n'
name|'vif_rec'
op|'['
string|"'qos_algorithm_params'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Creating VIF for VM %s, network %s ... '"
op|','
name|'vm_ref'
op|','
nl|'\n'
name|'network_ref'
op|')'
newline|'\n'
name|'vif_ref'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|"'VIF.create'"
op|','
name|'vif_rec'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'Created VIF %s for VM %s, network %s.'"
op|','
name|'vif_ref'
op|','
nl|'\n'
name|'vm_ref'
op|','
name|'network_ref'
op|')'
newline|'\n'
name|'return'
name|'vif_ref'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|fetch_image
name|'def'
name|'fetch_image'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'image'
op|','
name|'user'
op|','
name|'project'
op|','
name|'use_sr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""use_sr: True to put the image as a VDI in an SR, False to place\n        it on dom0\'s filesystem.  The former is for VM disks, the latter for\n        its kernel and ramdisk (if external kernels are being used).\n        Returns a Deferred that gives the new VDI UUID."""'
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'images'
op|'.'
name|'image_url'
op|'('
name|'image'
op|')'
newline|'\n'
name|'access'
op|'='
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Asking xapi to fetch %s as %s"'
op|','
name|'url'
op|','
name|'access'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'use_sr'
name|'and'
string|"'get_vdi'"
name|'or'
string|"'get_kernel'"
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'args'
op|'['
string|"'src_url'"
op|']'
op|'='
name|'url'
newline|'\n'
name|'args'
op|'['
string|"'username'"
op|']'
op|'='
name|'access'
newline|'\n'
name|'args'
op|'['
string|"'password'"
op|']'
op|'='
name|'user'
op|'.'
name|'secret'
newline|'\n'
name|'if'
name|'use_sr'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'add_partition'"
op|']'
op|'='
string|"'true'"
newline|'\n'
dedent|''
name|'task'
op|'='
name|'session'
op|'.'
name|'async_call_plugin'
op|'('
string|"'objectstore'"
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
name|'uuid'
op|'='
name|'session'
op|'.'
name|'wait_for_task'
op|'('
name|'task'
op|')'
newline|'\n'
name|'return'
name|'uuid'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup
name|'def'
name|'lookup'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Look the instance i up, and returns it if available """'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'lookup_blocking'
op|'('
name|'session'
op|','
name|'i'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup_blocking
name|'def'
name|'lookup_blocking'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'i'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Synchronous lookup """'
newline|'\n'
name|'vms'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_by_name_label'
op|'('
name|'i'
op|')'
newline|'\n'
name|'n'
op|'='
name|'len'
op|'('
name|'vms'
op|')'
newline|'\n'
name|'if'
name|'n'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'n'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'duplicate name found: %s'"
op|'%'
name|'i'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vms'
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
DECL|member|lookup_vm_vdis
name|'def'
name|'lookup_vm_vdis'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Look for the VDIs that are attached to the VM """'
newline|'\n'
name|'return'
name|'VMHelper'
op|'.'
name|'lookup_vm_vdis_blocking'
op|'('
name|'session'
op|','
name|'vm'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup_vm_vdis_blocking
name|'def'
name|'lookup_vm_vdis_blocking'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Synchronous lookup_vm_vdis """'
newline|'\n'
comment|'# Firstly we get the VBDs, then the VDIs.'
nl|'\n'
comment|'# TODO(Armando): do we leave the read-only devices?'
nl|'\n'
name|'vbds'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM'
op|'.'
name|'get_VBDs'
op|'('
name|'vm'
op|')'
newline|'\n'
name|'vdis'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'vbds'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'vbd'
name|'in'
name|'vbds'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'vdi'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VBD'
op|'.'
name|'get_VDI'
op|'('
name|'vbd'
op|')'
newline|'\n'
comment|'# Test valid VDI'
nl|'\n'
name|'record'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VDI'
op|'.'
name|'get_record'
op|'('
name|'vdi'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'VDI %s is still available'"
op|','
name|'record'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'                    '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'vdis'
op|'.'
name|'append'
op|'('
name|'vdi'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'vdis'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'vdis'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|compile_info
name|'def'
name|'compile_info'
op|'('
name|'cls'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'state'"
op|':'
name|'XENAPI_POWER_STATE'
op|'['
name|'record'
op|'['
string|"'power_state'"
op|']'
op|']'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
name|'long'
op|'('
name|'record'
op|'['
string|"'memory_static_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'mem'"
op|':'
name|'long'
op|'('
name|'record'
op|'['
string|"'memory_dynamic_max'"
op|']'
op|')'
op|'>>'
number|'10'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
name|'record'
op|'['
string|"'VCPUs_max'"
op|']'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|compile_diagnostics
name|'def'
name|'compile_diagnostics'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'record'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Compile VM diagnostics data"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|'='
name|'session'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
newline|'\n'
name|'host_ip'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'host'
op|'.'
name|'get_record'
op|'('
name|'host'
op|')'
op|'['
string|'"address"'
op|']'
newline|'\n'
name|'metrics'
op|'='
name|'session'
op|'.'
name|'get_xenapi'
op|'('
op|')'
op|'.'
name|'VM_guest_metrics'
op|'.'
name|'get_record'
op|'('
nl|'\n'
name|'record'
op|'['
string|'"guest_metrics"'
op|']'
op|')'
newline|'\n'
name|'diags'
op|'='
op|'{'
nl|'\n'
string|'"Kernel"'
op|':'
name|'metrics'
op|'['
string|'"os_version"'
op|']'
op|'['
string|'"uname"'
op|']'
op|','
nl|'\n'
string|'"Distro"'
op|':'
name|'metrics'
op|'['
string|'"os_version"'
op|']'
op|'['
string|'"name"'
op|']'
op|'}'
newline|'\n'
name|'xml'
op|'='
name|'get_rrd'
op|'('
name|'host_ip'
op|','
name|'record'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
name|'if'
name|'xml'
op|':'
newline|'\n'
indent|'                '
name|'rrd'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'for'
name|'i'
op|','
name|'node'
name|'in'
name|'enumerate'
op|'('
name|'rrd'
op|'.'
name|'firstChild'
op|'.'
name|'childNodes'
op|')'
op|':'
newline|'\n'
comment|"# We don't want all of the extra garbage"
nl|'\n'
indent|'                    '
name|'if'
name|'i'
op|'>='
number|'3'
name|'and'
name|'i'
op|'<='
number|'11'
op|':'
newline|'\n'
indent|'                        '
name|'ref'
op|'='
name|'node'
op|'.'
name|'childNodes'
newline|'\n'
comment|'# Name and Value'
nl|'\n'
name|'diags'
op|'['
name|'ref'
op|'['
number|'0'
op|']'
op|'.'
name|'firstChild'
op|'.'
name|'data'
op|']'
op|'='
name|'ref'
op|'['
number|'6'
op|']'
op|'.'
name|'firstChild'
op|'.'
name|'data'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'diags'
newline|'\n'
dedent|''
name|'except'
name|'XenAPI'
op|'.'
name|'Failure'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|'"Unable to retrieve diagnostics"'
op|':'
name|'e'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rrd
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_rrd'
op|'('
name|'host'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the VM RRD XML as a string"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'urllib'
op|'.'
name|'urlopen'
op|'('
string|'"http://%s:%s@%s/vm_rrd?uuid=%s"'
op|'%'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
op|','
nl|'\n'
name|'host'
op|','
nl|'\n'
name|'uuid'
op|')'
op|')'
newline|'\n'
name|'return'
name|'xml'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
