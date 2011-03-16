begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
string|'"""\r\nThe VMware API VM utility module to build SOAP object specs.\r\n"""'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|build_datastore_path
name|'def'
name|'build_datastore_path'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Build the datastore compliant path."""'
newline|'\r\n'
name|'return'
string|'"[%s] %s"'
op|'%'
op|'('
name|'datastore_name'
op|','
name|'path'
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|split_datastore_path
dedent|''
name|'def'
name|'split_datastore_path'
op|'('
name|'datastore_path'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Split the VMWare style datastore path to get the Datastore\r\n    name and the entity path.\r\n    """'
newline|'\r\n'
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
newline|'\r\n'
name|'path'
op|'='
string|'""'
newline|'\r\n'
name|'if'
name|'len'
op|'('
name|'spl'
op|')'
op|'=='
number|'1'
op|':'
newline|'\r\n'
indent|'        '
name|'datastore_url'
op|'='
name|'spl'
op|'['
number|'0'
op|']'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'datastore_url'
op|','
name|'path'
op|'='
name|'spl'
newline|'\r\n'
dedent|''
name|'return'
name|'datastore_url'
op|','
name|'path'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
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
nl|'\r\n'
name|'network_name'
op|'='
string|'"vmnet0"'
op|','
nl|'\r\n'
name|'os_type'
op|'='
string|'"otherGuest"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the VM Create spec."""'
newline|'\r\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'guestId'
op|'='
name|'os_type'
newline|'\r\n'
nl|'\r\n'
name|'vm_file_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineFileInfo'"
op|')'
newline|'\r\n'
name|'vm_file_info'
op|'.'
name|'vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'files'
op|'='
name|'vm_file_info'
newline|'\r\n'
nl|'\r\n'
name|'tools_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ToolsConfigInfo'"
op|')'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'afterPowerOn'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'afterResume'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestStandby'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestShutdown'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestReboot'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'tools'
op|'='
name|'tools_info'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'numCPUs'
op|'='
name|'int'
op|'('
name|'instance'
op|'.'
name|'vcpus'
op|')'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'memoryMB'
op|'='
name|'int'
op|'('
name|'instance'
op|'.'
name|'memory_mb'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'nic_spec'
op|'='
name|'create_network_spec'
op|'('
name|'client_factory'
op|','
nl|'\r\n'
name|'network_name'
op|','
name|'instance'
op|'.'
name|'mac_address'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
name|'nic_spec'
op|']'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_controller_spec
dedent|''
name|'def'
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
name|'key'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds a Config Spec for the LSI Logic Controller\'s addition\r\n    which acts as the controller for the virtual hard disk to be attached\r\n    to the VM.\r\n    """'
newline|'\r\n'
comment|'# Create a controller for the Virtual Hard Disk'
nl|'\r\n'
name|'virtual_device_config'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\r\n'
name|'virtual_lsi'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualLsiLogicController'"
op|')'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'key'
op|'='
name|'key'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'busNumber'
op|'='
number|'0'
newline|'\r\n'
name|'virtual_lsi'
op|'.'
name|'sharedBus'
op|'='
string|'"noSharing"'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'device'
op|'='
name|'virtual_lsi'
newline|'\r\n'
name|'return'
name|'virtual_device_config'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_network_spec
dedent|''
name|'def'
name|'create_network_spec'
op|'('
name|'client_factory'
op|','
name|'network_name'
op|','
name|'mac_address'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds a config spec for the addition of a new network\r\n    adapter to the VM.\r\n    """'
newline|'\r\n'
name|'network_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\r\n'
name|'network_spec'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\r\n'
nl|'\r\n'
comment|'# Get the recommended card type for the VM based on the guest OS of the VM'
nl|'\r\n'
name|'net_device'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualPCNet32'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualEthernetCardNetworkBackingInfo'"
op|')'
newline|'\r\n'
name|'backing'
op|'.'
name|'deviceName'
op|'='
name|'network_name'
newline|'\r\n'
nl|'\r\n'
name|'connectable_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConnectInfo'"
op|')'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'startConnected'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'allowGuestControl'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'connected'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'net_device'
op|'.'
name|'connectable'
op|'='
name|'connectable_spec'
newline|'\r\n'
name|'net_device'
op|'.'
name|'backing'
op|'='
name|'backing'
newline|'\r\n'
nl|'\r\n'
comment|'# The Server assigns a Key to the device. Here we pass a -ve temporary key.'
nl|'\r\n'
comment|"# -ve because actual keys are +ve numbers and we don't"
nl|'\r\n'
comment|'# want a clash with the key that server might associate with the device'
nl|'\r\n'
name|'net_device'
op|'.'
name|'key'
op|'='
op|'-'
number|'47'
newline|'\r\n'
name|'net_device'
op|'.'
name|'addressType'
op|'='
string|'"manual"'
newline|'\r\n'
name|'net_device'
op|'.'
name|'macAddress'
op|'='
name|'mac_address'
newline|'\r\n'
name|'net_device'
op|'.'
name|'wakeOnLanEnabled'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'network_spec'
op|'.'
name|'device'
op|'='
name|'net_device'
newline|'\r\n'
name|'return'
name|'network_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_attach_config_spec
dedent|''
name|'def'
name|'get_vmdk_attach_config_spec'
op|'('
name|'client_factory'
op|','
nl|'\r\n'
name|'disksize'
op|','
name|'file_path'
op|','
name|'adapter_type'
op|'='
string|'"lsiLogic"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the vmdk attach config spec."""'
newline|'\r\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\r\n'
nl|'\r\n'
comment|'# The controller Key pertains to the Key of the LSI Logic Controller, which'
nl|'\r\n'
comment|'# controls this Hard Disk'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
op|']'
newline|'\r\n'
comment|'# For IDE devices, there are these two default controllers created in the'
nl|'\r\n'
comment|'# VM having keys 200 and 201'
nl|'\r\n'
name|'if'
name|'adapter_type'
op|'=='
string|'"ide"'
op|':'
newline|'\r\n'
indent|'        '
name|'controller_key'
op|'='
number|'200'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\r\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
nl|'\r\n'
name|'controller_key'
op|')'
newline|'\r\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'controller_spec'
op|')'
newline|'\r\n'
dedent|''
name|'virtual_device_config_spec'
op|'='
name|'create_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
nl|'\r\n'
name|'disksize'
op|','
name|'controller_key'
op|','
name|'file_path'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'.'
name|'append'
op|'('
name|'virtual_device_config_spec'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_vmdk_file_path_and_adapter_type
dedent|''
name|'def'
name|'get_vmdk_file_path_and_adapter_type'
op|'('
name|'client_factory'
op|','
name|'hardware_devices'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Gets the vmdk file path and the storage adapter type."""'
newline|'\r\n'
name|'if'
name|'hardware_devices'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"ArrayOfVirtualDevice"'
op|':'
newline|'\r\n'
indent|'        '
name|'hardware_devices'
op|'='
name|'hardware_devices'
op|'.'
name|'VirtualDevice'
newline|'\r\n'
dedent|''
name|'vmdk_file_path'
op|'='
name|'None'
newline|'\r\n'
name|'vmdk_controler_key'
op|'='
name|'None'
newline|'\r\n'
nl|'\r\n'
name|'adapter_type_dict'
op|'='
op|'{'
op|'}'
newline|'\r\n'
name|'for'
name|'device'
name|'in'
name|'hardware_devices'
op|':'
newline|'\r\n'
indent|'        '
name|'if'
name|'device'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'=='
string|'"VirtualDisk"'
name|'and'
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
newline|'\r\n'
indent|'            '
name|'vmdk_file_path'
op|'='
name|'device'
op|'.'
name|'backing'
op|'.'
name|'fileName'
newline|'\r\n'
name|'vmdk_controler_key'
op|'='
name|'device'
op|'.'
name|'controllerKey'
newline|'\r\n'
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
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\r\n'
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
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"busLogic"'
newline|'\r\n'
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
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"ide"'
newline|'\r\n'
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
newline|'\r\n'
indent|'            '
name|'adapter_type_dict'
op|'['
name|'device'
op|'.'
name|'key'
op|']'
op|'='
string|'"lsiLogic"'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'vmdk_file_path'
op|','
name|'adapter_type'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_copy_virtual_disk_spec
dedent|''
name|'def'
name|'get_copy_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
name|'adapter_type'
op|'='
string|'"lsilogic"'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the Virtual Disk copy spec."""'
newline|'\r\n'
name|'dest_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDiskSpec'"
op|')'
newline|'\r\n'
name|'dest_spec'
op|'.'
name|'adapterType'
op|'='
name|'adapter_type'
newline|'\r\n'
name|'dest_spec'
op|'.'
name|'diskType'
op|'='
string|'"thick"'
newline|'\r\n'
name|'return'
name|'dest_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
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
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the virtual disk create spec."""'
newline|'\r\n'
name|'create_vmdk_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:FileBackedVirtualDiskSpec'"
op|')'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'adapterType'
op|'='
name|'adapter_type'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'diskType'
op|'='
string|'"thick"'
newline|'\r\n'
name|'create_vmdk_spec'
op|'.'
name|'capacityKb'
op|'='
name|'size_in_kb'
newline|'\r\n'
name|'return'
name|'create_vmdk_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|create_virtual_disk_spec
dedent|''
name|'def'
name|'create_virtual_disk_spec'
op|'('
name|'client_factory'
op|','
nl|'\r\n'
name|'disksize'
op|','
name|'controller_key'
op|','
name|'file_path'
op|'='
name|'None'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""\r\n    Builds spec for the creation of a new/ attaching of an already existing\r\n    Virtual Disk to the VM.\r\n    """'
newline|'\r\n'
name|'virtual_device_config'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConfigSpec'"
op|')'
newline|'\r\n'
name|'virtual_device_config'
op|'.'
name|'operation'
op|'='
string|'"add"'
newline|'\r\n'
name|'if'
name|'file_path'
name|'is'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'virtual_device_config'
op|'.'
name|'fileOperation'
op|'='
string|'"create"'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'virtual_disk'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDisk'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'disk_file_backing'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDiskFlatVer2BackingInfo'"
op|')'
newline|'\r\n'
name|'disk_file_backing'
op|'.'
name|'diskMode'
op|'='
string|'"persistent"'
newline|'\r\n'
name|'disk_file_backing'
op|'.'
name|'thinProvisioned'
op|'='
name|'False'
newline|'\r\n'
name|'if'
name|'file_path'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\r\n'
indent|'        '
name|'disk_file_backing'
op|'.'
name|'fileName'
op|'='
name|'file_path'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'        '
name|'disk_file_backing'
op|'.'
name|'fileName'
op|'='
string|'""'
newline|'\r\n'
nl|'\r\n'
dedent|''
name|'connectable_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualDeviceConnectInfo'"
op|')'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'startConnected'
op|'='
name|'True'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'allowGuestControl'
op|'='
name|'False'
newline|'\r\n'
name|'connectable_spec'
op|'.'
name|'connected'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'virtual_disk'
op|'.'
name|'backing'
op|'='
name|'disk_file_backing'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'connectable'
op|'='
name|'connectable_spec'
newline|'\r\n'
nl|'\r\n'
comment|'# The Server assigns a Key to the device. Here we pass a -ve random key.'
nl|'\r\n'
comment|"# -ve because actual keys are +ve numbers and we don't"
nl|'\r\n'
comment|'# want a clash with the key that server might associate with the device'
nl|'\r\n'
name|'virtual_disk'
op|'.'
name|'key'
op|'='
op|'-'
number|'100'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'controllerKey'
op|'='
name|'controller_key'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'unitNumber'
op|'='
number|'0'
newline|'\r\n'
name|'virtual_disk'
op|'.'
name|'capacityInKB'
op|'='
name|'disksize'
newline|'\r\n'
nl|'\r\n'
name|'virtual_device_config'
op|'.'
name|'device'
op|'='
name|'virtual_disk'
newline|'\r\n'
nl|'\r\n'
name|'return'
name|'virtual_device_config'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
indent|'    '
string|'"""Builds the dummy VM create spec."""'
newline|'\r\n'
name|'config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'guestId'
op|'='
string|'"otherGuest"'
newline|'\r\n'
nl|'\r\n'
name|'vm_file_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineFileInfo'"
op|')'
newline|'\r\n'
name|'vm_file_info'
op|'.'
name|'vmPathName'
op|'='
string|'"["'
op|'+'
name|'data_store_name'
op|'+'
string|'"]"'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'files'
op|'='
name|'vm_file_info'
newline|'\r\n'
nl|'\r\n'
name|'tools_info'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:ToolsConfigInfo'"
op|')'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'afterPowerOn'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'afterResume'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestStandby'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestShutdown'
op|'='
name|'True'
newline|'\r\n'
name|'tools_info'
op|'.'
name|'beforeGuestReboot'
op|'='
name|'True'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'tools'
op|'='
name|'tools_info'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'numCPUs'
op|'='
number|'1'
newline|'\r\n'
name|'config_spec'
op|'.'
name|'memoryMB'
op|'='
number|'4'
newline|'\r\n'
nl|'\r\n'
name|'controller_key'
op|'='
op|'-'
number|'101'
newline|'\r\n'
name|'controller_spec'
op|'='
name|'create_controller_spec'
op|'('
name|'client_factory'
op|','
name|'controller_key'
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
name|'device_config_spec'
op|'='
op|'['
name|'controller_spec'
op|','
name|'disk_spec'
op|']'
newline|'\r\n'
nl|'\r\n'
name|'config_spec'
op|'.'
name|'deviceChange'
op|'='
name|'device_config_spec'
newline|'\r\n'
name|'return'
name|'config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_machine_id_change_spec
dedent|''
name|'def'
name|'get_machine_id_change_spec'
op|'('
name|'client_factory'
op|','
name|'mac'
op|','
name|'ip_addr'
op|','
name|'netmask'
op|','
name|'gateway'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the machine id change config spec."""'
newline|'\r\n'
name|'machine_id_str'
op|'='
string|'"%s;%s;%s;%s"'
op|'%'
op|'('
name|'mac'
op|','
name|'ip_addr'
op|','
name|'netmask'
op|','
name|'gateway'
op|')'
newline|'\r\n'
name|'virtual_machine_config_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:VirtualMachineConfigSpec'"
op|')'
newline|'\r\n'
nl|'\r\n'
name|'opt'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:OptionValue'"
op|')'
newline|'\r\n'
name|'opt'
op|'.'
name|'key'
op|'='
string|'"machine.id"'
newline|'\r\n'
name|'opt'
op|'.'
name|'value'
op|'='
name|'machine_id_str'
newline|'\r\n'
name|'virtual_machine_config_spec'
op|'.'
name|'extraConfig'
op|'='
op|'['
name|'opt'
op|']'
newline|'\r\n'
name|'return'
name|'virtual_machine_config_spec'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|function|get_add_vswitch_port_group_spec
dedent|''
name|'def'
name|'get_add_vswitch_port_group_spec'
op|'('
name|'client_factory'
op|','
name|'vswitch_name'
op|','
nl|'\r\n'
name|'port_group_name'
op|','
name|'vlan_id'
op|')'
op|':'
newline|'\r\n'
indent|'    '
string|'"""Builds the virtual switch port group add spec."""'
newline|'\r\n'
name|'vswitch_port_group_spec'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostPortGroupSpec'"
op|')'
newline|'\r\n'
name|'vswitch_port_group_spec'
op|'.'
name|'name'
op|'='
name|'port_group_name'
newline|'\r\n'
name|'vswitch_port_group_spec'
op|'.'
name|'vswitchName'
op|'='
name|'vswitch_name'
newline|'\r\n'
nl|'\r\n'
comment|'# VLAN ID of 0 means that VLAN tagging is not to be done for the network.'
nl|'\r\n'
name|'vswitch_port_group_spec'
op|'.'
name|'vlanId'
op|'='
name|'int'
op|'('
name|'vlan_id'
op|')'
newline|'\r\n'
nl|'\r\n'
name|'policy'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostNetworkPolicy'"
op|')'
newline|'\r\n'
name|'nicteaming'
op|'='
name|'client_factory'
op|'.'
name|'create'
op|'('
string|"'ns0:HostNicTeamingPolicy'"
op|')'
newline|'\r\n'
name|'nicteaming'
op|'.'
name|'notifySwitches'
op|'='
name|'True'
newline|'\r\n'
name|'policy'
op|'.'
name|'nicTeaming'
op|'='
name|'nicteaming'
newline|'\r\n'
nl|'\r\n'
name|'vswitch_port_group_spec'
op|'.'
name|'policy'
op|'='
name|'policy'
newline|'\r\n'
name|'return'
name|'vswitch_port_group_spec'
newline|'\r\n'
dedent|''
endmarker|''
end_unit
