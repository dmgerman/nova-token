begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
string|'"""\nThe VMware API VM utility module to build SOAP object specs.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vim_util'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|build_datastore_path
name|'def'
name|'build_datastore_path'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build the datastore compliant path."""'
newline|'\n'
name|'return'
string|'"[%s] %s"'
op|'%'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|split_datastore_path
dedent|''
name|'def'
name|'split_datastore_path'
op|'('
name|'datastore_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Split the VMware style datastore path to get the Datastore\n    name and the entity path.\n    """'
newline|'\n'
name|'spl'
op|'='
name|'datastore_path'
op|'.'
name|'split'
op|'('
string|"'['"
op|','
number|'1'
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
string|"']'"
op|','
number|'1'
op|')'
newline|'\n'
name|'path'
op|'='
string|'""'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'spl'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'datastore_url'
op|'='
name|'spl'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'datastore_url'
op|','
name|'path'
op|'='
name|'spl'
newline|'\n'
dedent|''
name|'return'
name|'datastore_url'
op|','
name|'path'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vm_create_spec
dedent|''
name|'def'
name|'get_vm_create_spec'
op|'('
name|'client_factory'
op|','
name|'instance'
op|','
name|'data_store_name'
op|','
nl|'\n'
name|'vif_infos'
op|','
name|'os_type'
op|'='
string|'"otherGuest"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the VM Create spec."""'
newline|'\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
name|'config_spec'
op|'.'
name|'name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'config_spec'
op|'.'
name|'guestId'
op|'='
name|'os_type'
newline|'\n'
nl|'\n'
name|'vm_file_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineFileInfo'"
op|')'
newline|'\n'
name|'vm_file_info'
op|'.'
name|'vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\n'
name|'config_spec'
op|'.'
name|'files'
op|'='
name|'vm_file_info'
newline|'\n'
nl|'\n'
name|'tools_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ToolsConfigInfo'"
op|')'
newline|'\n'
name|'tools_info'
op|'.'
name|'afterPowerOn'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'afterResume'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestStandby'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestShutdown'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestReboot'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'tools'
op|'='
name|'tools_info'
newline|'\n'
name|'config_spec'
op|'.'
name|'numCPUs'
op|'='
name|'int'
op|'('
name|'instance'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'config_spec'
op|'.'
name|'memoryMB'
op|'='
name|'int'
op|'('
name|'instance'
op|'['
string|"'memory_mb'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vif_spec_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'vif_info'
name|'in'
name|'vif_infos'
op|':'
newline|'\n'
indent|'        '
name|'vif_spec'
op|'='
name|'create_network_spec'
op|'('
name|'client_factory'
op|','
name|'vif_info'
op|')'
newline|'\n'
name|'vif_spec_list'
op|'.'
name|'append'
op|'('
name|'vif_spec'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'device_config_spec'
op|'='
name|'vif_spec_list'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\n'
name|'return'
name|'config_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_controller_spec
dedent|''
name|'def'
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
name|'key'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Builds a Config Spec for the LSI or Bus Logic Controller\'s addition\n    which acts as the controller for the virtual hard disk to be attached\n    to the VM.\n    """'
newline|'\n'
comment|'# Create a controller for the Virtual Hard Disk'
nl|'\n'
name|'virtual_device_config'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\n'
name|'if'
name|'adapter_type'
op|'=='
string|'"busLogic"'
op|':'
newline|'\n'
indent|'        '
name|'virtual_controller'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualBusLogicController'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'virtual_controller'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualLsiLogicController'"
op|')'
newline|'\n'
dedent|''
name|'virtual_controller'
op|'.'
name|'key'
op|'='
name|'key'
newline|'\n'
name|'virtual_controller'
op|'.'
name|'busNumber'
op|'='
number|'0'
newline|'\n'
name|'virtual_controller'
op|'.'
name|'sharedBus'
op|'='
string|'"noSharing"'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'device'
op|'='
name|'virtual_controller'
newline|'\n'
name|'return'
name|'virtual_device_config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_network_spec
dedent|''
name|'def'
name|'create_network_spec'
op|'('
name|'client_factory'
op|','
name|'vif_info'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Builds a config spec for the addition of a new network\n    adapter to the VM.\n    """'
newline|'\n'
name|'network_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'network_spec'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\n'
nl|'\n'
comment|'# Get the recommended card type for the VM based on the guest OS of the VM'
nl|'\n'
name|'net_device'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualPCNet32'"
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(asomya): Only works on ESXi if the portgroup binding is set to'
nl|'\n'
comment|'# ephemeral. Invalid configuration if set to static and the NIC does'
nl|'\n'
comment|'# not come up on boot if set to dynamic.'
nl|'\n'
name|'network_ref'
op|'='
name|'vif_info'
op|'['
string|"'network_ref'"
op|']'
newline|'\n'
name|'network_name'
op|'='
name|'vif_info'
op|'['
string|"'network_name'"
op|']'
newline|'\n'
name|'mac_address'
op|'='
name|'vif_info'
op|'['
string|"'mac_address'"
op|']'
newline|'\n'
name|'backing'
op|'='
name|'None'
newline|'\n'
name|'if'
op|'('
name|'network_ref'
name|'and'
nl|'\n'
name|'network_ref'
op|'['
string|"'type'"
op|']'
op|'=='
string|'"DistributedVirtualPortgroup"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'backing_name'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|"'ns0:VirtualEthernetCardDistributed'"
op|','
nl|'\n'
string|"'VirtualPortBackingInfo'"
op|']'
op|')'
newline|'\n'
name|'backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
name|'backing_name'
op|')'
newline|'\n'
name|'portgroup'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:DistributedVirtualSwitchPortConnection'"
op|')'
newline|'\n'
name|'portgroup'
op|'.'
name|'switchUuid'
op|'='
name|'network_ref'
op|'['
string|"'dvsw'"
op|']'
newline|'\n'
name|'portgroup'
op|'.'
name|'portgroupKey'
op|'='
name|'network_ref'
op|'['
string|"'dvpg'"
op|']'
newline|'\n'
name|'backing'
op|'.'
name|'port'
op|'='
name|'portgroup'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualEthernetCardNetworkBackingInfo'"
op|')'
newline|'\n'
name|'backing'
op|'.'
name|'deviceName'
op|'='
name|'network_name'
newline|'\n'
nl|'\n'
dedent|''
name|'connectable_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConnectInfo'"
op|')'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'startConnected'
op|'='
name|'True'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'allowGuestControl'
op|'='
name|'True'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'connected'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'net_device'
op|'.'
name|'connectable'
op|'='
name|'connectable_spec'
newline|'\n'
name|'net_device'
op|'.'
name|'backing'
op|'='
name|'backing'
newline|'\n'
nl|'\n'
comment|'# The Server assigns a Key to the device. Here we pass a -ve temporary key.'
nl|'\n'
comment|"# -ve because actual keys are +ve numbers and we don't"
nl|'\n'
comment|'# want a clash with the key that server might associate with the device'
nl|'\n'
name|'net_device'
op|'.'
name|'key'
op|'='
op|'-'
number|'47'
newline|'\n'
name|'net_device'
op|'.'
name|'addressType'
op|'='
string|'"manual"'
newline|'\n'
name|'net_device'
op|'.'
name|'macAddress'
op|'='
name|'mac_address'
newline|'\n'
name|'net_device'
op|'.'
name|'wakeOnLanEnabled'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'network_spec'
op|'.'
name|'device'
op|'='
name|'net_device'
newline|'\n'
name|'return'
name|'network_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_attach_config_spec
dedent|''
name|'def'
name|'get_vmdk_attach_config_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|','
nl|'\n'
name|'disk_type'
op|'='
string|'"preallocated"'
op|','
nl|'\n'
name|'file_path'
op|'='
name|'None'
op|','
nl|'\n'
name|'disk_size'
op|'='
name|'None'
op|','
nl|'\n'
name|'linked_clone'
op|'='
name|'False'
op|','
nl|'\n'
name|'controller_key'
op|'='
name|'None'
op|','
nl|'\n'
name|'unit_number'
op|'='
name|'None'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the vmdk attach config spec."""'
newline|'\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
nl|'\n'
comment|'# The controller Key pertains to the Key of the LSI Logic Controller, which'
nl|'\n'
comment|'# controls this Hard Disk'
nl|'\n'
name|'device_config_spec'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# For IDE devices, there are these two default controllers created in the'
nl|'\n'
comment|'# VM having keys 200 and 201'
nl|'\n'
name|'if'
name|'controller_key'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'adapter_type'
op|'=='
string|'"ide"'
op|':'
newline|'\n'
indent|'            '
name|'controller_key'
op|'='
number|'200'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'controller_key'
op|','
nl|'\n'
name|'adapter_type'
op|')'
newline|'\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'controller_spec'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'virtual_device_config_spec'
op|'='
name|'create_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'controller_key'
op|','
name|'disk_type'
op|','
name|'file_path'
op|','
nl|'\n'
name|'disk_size'
op|','
name|'linked_clone'
op|','
nl|'\n'
name|'unit_number'
op|','
name|'device_name'
op|')'
newline|'\n'
nl|'\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'virtual_device_config_spec'
op|')'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\n'
name|'return'
name|'config_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_detach_config_spec
dedent|''
name|'def'
name|'get_vmdk_detach_config_spec'
op|'('
name|'client_factory'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the vmdk detach config spec."""'
newline|'\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
nl|'\n'
name|'device_config_spec'
op|'='
op|'['
op|']'
newline|'\n'
name|'virtual_device_config_spec'
op|'='
name|'delete_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
nl|'\n'
name|'device'
op|')'
newline|'\n'
nl|'\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'virtual_device_config_spec'
op|')'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\n'
name|'return'
name|'config_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_path_and_adapter_type
dedent|''
name|'def'
name|'get_vmdk_path_and_adapter_type'
op|'('
name|'hardware_devices'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the vmdk file path and the storage adapter type."""'
newline|'\n'
name|'if'
name|'hardware_devices'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"ArrayOfVirtualDevice"'
op|':'
newline|'\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'hardware_devices'
op|'.'
name|'VirtualDevice'
newline|'\n'
dedent|''
name|'vmdk_file_path'
op|'='
name|'None'
newline|'\n'
name|'vmdk_controler_key'
op|'='
name|'None'
newline|'\n'
name|'disk_type'
op|'='
name|'None'
newline|'\n'
name|'unit_number'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'adapter_type_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'device'
name|'in'
name|'hardware_devices'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualDisk"'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'device'
op|'.'
name|'backing'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualDiskFlatVer2BackingInfo"'
op|':'
newline|'\n'
indent|'                '
name|'vmdk_file_path'
op|'='
name|'device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
newline|'\n'
name|'vmdk_controler_key'
op|'='
name|'device'
op|'.'
name|'controllerKey'
newline|'\n'
name|'if'
name|'getattr'
op|'('
name|'device'
op|'.'
name|'backing'
op|','
string|"'thinProvisioned'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'disk_type'
op|'='
string|'"thin"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'getattr'
op|'('
name|'device'
op|'.'
name|'backing'
op|','
string|"'eagerlyScrub'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'disk_type'
op|'='
string|'"eagerZeroedThick"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'disk_type'
op|'='
string|'"preallocated"'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'device'
op|'.'
name|'unitNumber'
op|'>'
name|'unit_number'
op|':'
newline|'\n'
indent|'                '
name|'unit_number'
op|'='
name|'device'
op|'.'
name|'unitNumber'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualLsiLogicController"'
op|':'
newline|'\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\n'
dedent|''
name|'elif'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualBusLogicController"'
op|':'
newline|'\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"busLogic"'
newline|'\n'
dedent|''
name|'elif'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualIDEController"'
op|':'
newline|'\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"ide"'
newline|'\n'
dedent|''
name|'elif'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualLsiLogicSASController"'
op|':'
newline|'\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'adapter_type'
op|'='
name|'adapter_type_dict'
op|'.'
name|'get'
op|'('
name|'vmdk_controler_key'
op|','
string|'""'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'vmdk_file_path'
op|','
name|'vmdk_controler_key'
op|','
name|'adapter_type'
op|','
nl|'\n'
name|'disk_type'
op|','
name|'unit_number'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rdm_disk
dedent|''
name|'def'
name|'get_rdm_disk'
op|'('
name|'hardware_devices'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Gets the RDM disk key."""'
newline|'\n'
name|'if'
name|'hardware_devices'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"ArrayOfVirtualDevice"'
op|':'
newline|'\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'hardware_devices'
op|'.'
name|'VirtualDevice'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'device'
name|'in'
name|'hardware_devices'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualDisk"'
name|'and'
nl|'\n'
name|'device'
op|'.'
name|'backing'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
nl|'\n'
string|'"VirtualDiskRawDiskMappingVer1BackingInfo"'
name|'and'
nl|'\n'
name|'device'
op|'.'
name|'backing'
op|'.'
name|'lunUuid'
op|'=='
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'device'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_copy_virtual_disk_spec
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_copy_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
name|'adapter_type'
op|'='
string|'"lsilogic"'
op|','
nl|'\n'
name|'disk_type'
op|'='
string|'"preallocated"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the Virtual Disk copy spec."""'
newline|'\n'
name|'dest_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDiskSpec'"
op|')'
newline|'\n'
name|'dest_spec'
op|'.'
name|'adapterType'
op|'='
name|'adapter_type'
newline|'\n'
name|'dest_spec'
op|'.'
name|'diskType'
op|'='
name|'disk_type'
newline|'\n'
name|'return'
name|'dest_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vmdk_create_spec
dedent|''
name|'def'
name|'get_vmdk_create_spec'
op|'('
name|'client_factory'
op|','
name|'size_in_kb'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|','
nl|'\n'
name|'disk_type'
op|'='
string|'"preallocated"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the virtual disk create spec."""'
newline|'\n'
name|'create_vmdk_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:FileBackedVirtualDiskSpec'"
op|')'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'adapterType'
op|'='
name|'adapter_type'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'diskType'
op|'='
name|'disk_type'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'capacityKb'
op|'='
name|'size_in_kb'
newline|'\n'
name|'return'
name|'create_vmdk_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_rdm_create_spec
dedent|''
name|'def'
name|'get_rdm_create_spec'
op|'('
name|'client_factory'
op|','
name|'device'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|','
nl|'\n'
name|'disk_type'
op|'='
string|'"rdmp"'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the RDM virtual disk create spec."""'
newline|'\n'
name|'create_vmdk_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:DeviceBackedVirtualDiskSpec'"
op|')'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'adapterType'
op|'='
name|'adapter_type'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'diskType'
op|'='
name|'disk_type'
newline|'\n'
name|'create_vmdk_spec'
op|'.'
name|'device'
op|'='
name|'device'
newline|'\n'
name|'return'
name|'create_vmdk_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_virtual_disk_spec
dedent|''
name|'def'
name|'create_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
name|'controller_key'
op|','
nl|'\n'
name|'disk_type'
op|'='
string|'"preallocated"'
op|','
nl|'\n'
name|'file_path'
op|'='
name|'None'
op|','
nl|'\n'
name|'disk_size'
op|'='
name|'None'
op|','
nl|'\n'
name|'linked_clone'
op|'='
name|'False'
op|','
nl|'\n'
name|'unit_number'
op|'='
name|'None'
op|','
nl|'\n'
name|'device_name'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Builds spec for the creation of a new/ attaching of an already existing\n    Virtual Disk to the VM.\n    """'
newline|'\n'
name|'virtual_device_config'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\n'
name|'if'
op|'('
name|'file_path'
name|'is'
name|'None'
op|')'
name|'or'
name|'linked_clone'
op|':'
newline|'\n'
indent|'        '
name|'virtual_device_config'
op|'.'
name|'fileOperation'
op|'='
string|'"create"'
newline|'\n'
nl|'\n'
dedent|''
name|'virtual_disk'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDisk'"
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'disk_type'
op|'=='
string|'"rdm"'
name|'or'
name|'disk_type'
op|'=='
string|'"rdmp"'
op|':'
newline|'\n'
indent|'        '
name|'disk_file_backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualDiskRawDiskMappingVer1BackingInfo'"
op|')'
newline|'\n'
name|'disk_file_backing'
op|'.'
name|'compatibilityMode'
op|'='
string|'"virtualMode"'
name|'if'
name|'disk_type'
op|'=='
string|'"rdm"'
name|'else'
string|'"physicalMode"'
newline|'\n'
name|'disk_file_backing'
op|'.'
name|'diskMode'
op|'='
string|'"independent_persistent"'
newline|'\n'
name|'disk_file_backing'
op|'.'
name|'deviceName'
op|'='
name|'device_name'
name|'or'
string|'""'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'disk_file_backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualDiskFlatVer2BackingInfo'"
op|')'
newline|'\n'
name|'disk_file_backing'
op|'.'
name|'diskMode'
op|'='
string|'"persistent"'
newline|'\n'
name|'if'
name|'disk_type'
op|'=='
string|'"thin"'
op|':'
newline|'\n'
indent|'            '
name|'disk_file_backing'
op|'.'
name|'thinProvisioned'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'disk_type'
op|'=='
string|'"eagerZeroedThick"'
op|':'
newline|'\n'
indent|'                '
name|'disk_file_backing'
op|'.'
name|'eagerlyScrub'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'disk_file_backing'
op|'.'
name|'fileName'
op|'='
name|'file_path'
name|'or'
string|'""'
newline|'\n'
nl|'\n'
name|'connectable_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConnectInfo'"
op|')'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'startConnected'
op|'='
name|'True'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'allowGuestControl'
op|'='
name|'False'
newline|'\n'
name|'connectable_spec'
op|'.'
name|'connected'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'linked_clone'
op|':'
newline|'\n'
indent|'        '
name|'virtual_disk'
op|'.'
name|'backing'
op|'='
name|'disk_file_backing'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'virtual_disk'
op|'.'
name|'backing'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'disk_file_backing'
op|')'
newline|'\n'
name|'virtual_disk'
op|'.'
name|'backing'
op|'.'
name|'fileName'
op|'='
string|'""'
newline|'\n'
name|'virtual_disk'
op|'.'
name|'backing'
op|'.'
name|'parent'
op|'='
name|'disk_file_backing'
newline|'\n'
dedent|''
name|'virtual_disk'
op|'.'
name|'connectable'
op|'='
name|'connectable_spec'
newline|'\n'
nl|'\n'
comment|'# The Server assigns a Key to the device. Here we pass a -ve random key.'
nl|'\n'
comment|"# -ve because actual keys are +ve numbers and we don't"
nl|'\n'
comment|'# want a clash with the key that server might associate with the device'
nl|'\n'
name|'virtual_disk'
op|'.'
name|'key'
op|'='
op|'-'
number|'100'
newline|'\n'
name|'virtual_disk'
op|'.'
name|'controllerKey'
op|'='
name|'controller_key'
newline|'\n'
name|'virtual_disk'
op|'.'
name|'unitNumber'
op|'='
name|'unit_number'
name|'or'
number|'0'
newline|'\n'
name|'virtual_disk'
op|'.'
name|'capacityInKB'
op|'='
name|'disk_size'
name|'or'
number|'0'
newline|'\n'
nl|'\n'
name|'virtual_device_config'
op|'.'
name|'device'
op|'='
name|'virtual_disk'
newline|'\n'
nl|'\n'
name|'return'
name|'virtual_device_config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_virtual_disk_spec
dedent|''
name|'def'
name|'delete_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Builds spec for the deletion of an already existing Virtual Disk from VM.\n    """'
newline|'\n'
name|'virtual_device_config'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'operation'
op|'='
string|'"remove"'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'fileOperation'
op|'='
string|'"destroy"'
newline|'\n'
name|'virtual_device_config'
op|'.'
name|'device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
name|'return'
name|'virtual_device_config'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_dummy_vm_create_spec
dedent|''
name|'def'
name|'get_dummy_vm_create_spec'
op|'('
name|'client_factory'
op|','
name|'name'
op|','
name|'data_store_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the dummy VM create spec."""'
newline|'\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'config_spec'
op|'.'
name|'guestId'
op|'='
string|'"otherGuest"'
newline|'\n'
nl|'\n'
name|'vm_file_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineFileInfo'"
op|')'
newline|'\n'
name|'vm_file_info'
op|'.'
name|'vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\n'
name|'config_spec'
op|'.'
name|'files'
op|'='
name|'vm_file_info'
newline|'\n'
nl|'\n'
name|'tools_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ToolsConfigInfo'"
op|')'
newline|'\n'
name|'tools_info'
op|'.'
name|'afterPowerOn'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'afterResume'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestStandby'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestShutdown'
op|'='
name|'True'
newline|'\n'
name|'tools_info'
op|'.'
name|'beforeGuestReboot'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'tools'
op|'='
name|'tools_info'
newline|'\n'
name|'config_spec'
op|'.'
name|'numCPUs'
op|'='
number|'1'
newline|'\n'
name|'config_spec'
op|'.'
name|'memoryMB'
op|'='
number|'4'
newline|'\n'
nl|'\n'
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
name|'controller_key'
op|')'
newline|'\n'
name|'disk_spec'
op|'='
name|'create_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
number|'1024'
op|','
name|'controller_key'
op|')'
newline|'\n'
nl|'\n'
name|'device_config_spec'
op|'='
op|'['
name|'controller_spec'
op|','
name|'disk_spec'
op|']'
newline|'\n'
nl|'\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\n'
name|'return'
name|'config_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_machine_id_change_spec
dedent|''
name|'def'
name|'get_machine_id_change_spec'
op|'('
name|'client_factory'
op|','
name|'machine_id_str'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the machine id change config spec."""'
newline|'\n'
name|'virtual_machine_config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
nl|'\n'
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\n'
nl|'\n'
name|'opt'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:OptionValue'"
op|')'
newline|'\n'
name|'opt'
op|'.'
name|'key'
op|'='
string|'"machine.id"'
newline|'\n'
name|'opt'
op|'.'
name|'value'
op|'='
name|'machine_id_str'
newline|'\n'
name|'virtual_machine_config_spec'
op|'.'
name|'extraConfig'
op|'='
op|'['
name|'opt'
op|']'
newline|'\n'
name|'return'
name|'virtual_machine_config_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_add_vswitch_port_group_spec
dedent|''
name|'def'
name|'get_add_vswitch_port_group_spec'
op|'('
name|'client_factory'
op|','
name|'vswitch_name'
op|','
nl|'\n'
name|'port_group_name'
op|','
name|'vlan_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Builds the virtual switch port group add spec."""'
newline|'\n'
name|'vswitch_port_group_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostPortGroupSpec'"
op|')'
newline|'\n'
name|'vswitch_port_group_spec'
op|'.'
name|'name'
op|'='
name|'port_group_name'
newline|'\n'
name|'vswitch_port_group_spec'
op|'.'
name|'vswitchName'
op|'='
name|'vswitch_name'
newline|'\n'
nl|'\n'
comment|'# VLAN ID of 0 means that VLAN tagging is not to be done for the network.'
nl|'\n'
name|'vswitch_port_group_spec'
op|'.'
name|'vlanId'
op|'='
name|'int'
op|'('
name|'vlan_id'
op|')'
newline|'\n'
nl|'\n'
name|'policy'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostNetworkPolicy'"
op|')'
newline|'\n'
name|'nicteaming'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostNicTeamingPolicy'"
op|')'
newline|'\n'
name|'nicteaming'
op|'.'
name|'notifySwitches'
op|'='
name|'True'
newline|'\n'
name|'policy'
op|'.'
name|'nicTeaming'
op|'='
name|'nicteaming'
newline|'\n'
nl|'\n'
name|'vswitch_port_group_spec'
op|'.'
name|'policy'
op|'='
name|'policy'
newline|'\n'
name|'return'
name|'vswitch_port_group_spec'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vm_ref_from_name
dedent|''
name|'def'
name|'get_vm_ref_from_name'
op|'('
name|'session'
op|','
name|'vm_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get reference to the VM with the name specified."""'
newline|'\n'
name|'vms'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_objects"'
op|','
nl|'\n'
string|'"VirtualMachine"'
op|','
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
name|'for'
name|'vm'
name|'in'
name|'vms'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vm'
op|'.'
name|'propSet'
op|'['
number|'0'
op|']'
op|'.'
name|'val'
op|'=='
name|'vm_name'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vm'
op|'.'
name|'obj'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_datastore_ref_and_name
dedent|''
name|'def'
name|'get_datastore_ref_and_name'
op|'('
name|'session'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the datastore list and choose the first local storage."""'
newline|'\n'
name|'data_stores'
op|'='
name|'session'
op|'.'
name|'_call_method'
op|'('
name|'vim_util'
op|','
string|'"get_objects"'
op|','
nl|'\n'
string|'"Datastore"'
op|','
op|'['
string|'"summary.type"'
op|','
string|'"summary.name"'
op|','
nl|'\n'
string|'"summary.capacity"'
op|','
string|'"summary.freeSpace"'
op|']'
op|')'
newline|'\n'
name|'for'
name|'elem'
name|'in'
name|'data_stores'
op|':'
newline|'\n'
indent|'        '
name|'ds_name'
op|'='
name|'None'
newline|'\n'
name|'ds_type'
op|'='
name|'None'
newline|'\n'
name|'ds_cap'
op|'='
name|'None'
newline|'\n'
name|'ds_free'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'prop'
name|'in'
name|'elem'
op|'.'
name|'propSet'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"summary.type"'
op|':'
newline|'\n'
indent|'                '
name|'ds_type'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"summary.name"'
op|':'
newline|'\n'
indent|'                '
name|'ds_name'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"summary.capacity"'
op|':'
newline|'\n'
indent|'                '
name|'ds_cap'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
dedent|''
name|'elif'
name|'prop'
op|'.'
name|'name'
op|'=='
string|'"summary.freeSpace"'
op|':'
newline|'\n'
indent|'                '
name|'ds_free'
op|'='
name|'prop'
op|'.'
name|'val'
newline|'\n'
comment|'# Local storage identifier'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ds_type'
op|'=='
string|'"VMFS"'
name|'or'
name|'ds_type'
op|'=='
string|'"NFS"'
op|':'
newline|'\n'
indent|'            '
name|'data_store_name'
op|'='
name|'ds_name'
newline|'\n'
name|'return'
name|'elem'
op|'.'
name|'obj'
op|','
name|'data_store_name'
op|','
name|'ds_cap'
op|','
name|'ds_free'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'data_store_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'DatastoreNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
