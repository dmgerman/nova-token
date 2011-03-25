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
string|'"""\nA fake (in-memory) hypervisor+api.\n\nAllows nova testing w/o a hypervisor.  This module also documents the\nsemantics of real hypervisor connections.\n\n"""'
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
name|'utils'
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
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_connection
name|'def'
name|'get_connection'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
comment|'# The read_only parameter is ignored.'
nl|'\n'
indent|'    '
name|'return'
name|'FakeConnection'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeInstance
dedent|''
name|'class'
name|'FakeInstance'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'state'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeConnection
dedent|''
dedent|''
name|'class'
name|'FakeConnection'
op|'('
name|'driver'
op|'.'
name|'ComputeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The interface to this class talks in terms of \'instances\' (Amazon EC2 and\n    internal Nova terminology), by which we mean \'running virtual machine\'\n    (XenAPI terminology) or domain (Xen or libvirt terminology).\n\n    An instance has an ID, which is the identifier chosen by Nova to represent\n    the instance further up the stack.  This is unfortunately also called a\n    \'name\' elsewhere.  As far as this layer is concerned, \'instance ID\' and\n    \'instance name\' are synonyms.\n\n    Note that the instance ID or name is not human-readable or\n    customer-controlled -- it\'s an internal ID chosen by Nova.  At the\n    nova.virt layer, instances do not have human-readable names at all -- such\n    things are only known higher up the stack.\n\n    Most virtualization platforms will also have their own identity schemes,\n    to uniquely identify a VM or domain.  These IDs must stay internal to the\n    platform-specific layer, and never escape the connection interface.  The\n    platform-specific layer is responsible for keeping track of which instance\n    ID maps to which platform-specific ID, and vice versa.\n\n    In contrast, the list_disks and list_interfaces calls may return\n    platform-specific IDs.  These identify a specific virtual disk or specific\n    virtual network interface, and these IDs are opaque to the rest of Nova.\n\n    Some methods here take an instance of nova.compute.service.Instance.  This\n    is the datastructure used by nova.compute to store details regarding an\n    instance, and pass them into this layer.  This layer is responsible for\n    translating that generic datastructure into terms that are specific to the\n    virtualization platform.\n    """'
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
name|'self'
op|'.'
name|'instances'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize anything that is necessary for the driver to function,\n        including catching up with currently running VM\'s on the given host.\n        """'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|list_instances
dedent|''
name|'def'
name|'list_instances'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the names of all the instances known to the virtualization\n        layer, as a list.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_map_to_instance_info
dedent|''
name|'def'
name|'_map_to_instance_info'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'utils'
op|'.'
name|'check_isinstance'
op|'('
name|'instance'
op|','
name|'FakeInstance'
op|')'
newline|'\n'
name|'info'
op|'='
name|'driver'
op|'.'
name|'InstanceInfo'
op|'('
name|'instance'
op|'.'
name|'name'
op|','
name|'instance'
op|'.'
name|'state'
op|')'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
nl|'\n'
DECL|member|list_instances_detail
dedent|''
name|'def'
name|'list_instances_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'info_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'info_list'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_map_to_instance_info'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'info_list'
newline|'\n'
nl|'\n'
DECL|member|spawn
dedent|''
name|'def'
name|'spawn'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a new instance/VM/domain on the virtualization platform.\n\n        The given parameter is an instance of nova.compute.service.Instance.\n        This function should use the data there to guide the creation of\n        the new instance.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n\n        Once this successfully completes, the instance should be\n        running (power_state.RUNNING).\n\n        If this fails, any partial instance should be completely\n        cleaned up, and the virtualization platform should be in the state\n        that it was before this call began.\n        """'
newline|'\n'
nl|'\n'
name|'name'
op|'='
name|'instance'
op|'.'
name|'name'
newline|'\n'
name|'state'
op|'='
name|'power_state'
op|'.'
name|'RUNNING'
newline|'\n'
name|'fake_instance'
op|'='
name|'FakeInstance'
op|'('
name|'name'
op|','
name|'state'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'['
name|'name'
op|']'
op|'='
name|'fake_instance'
newline|'\n'
nl|'\n'
DECL|member|snapshot
dedent|''
name|'def'
name|'snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Snapshots the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The second parameter is the name of the snapshot.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|reboot
dedent|''
name|'def'
name|'reboot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Reboot the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|get_host_ip_addr
dedent|''
name|'def'
name|'get_host_ip_addr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Retrieves the IP address of the dom0\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|resize
dedent|''
name|'def'
name|'resize'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'flavor'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Resizes/Migrates the specified instance.\n\n        The flavor parameter determines whether or not the instance RAM and\n        disk space are modified, and if so, to what size.\n\n        The work will be done asynchronously. This function returns a task\n        that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|set_admin_password
dedent|''
name|'def'
name|'set_admin_password'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'new_pass'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Set the root password on the specified instance.\n\n        The first parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name. The second\n        parameter is the value of the new password.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|inject_file
dedent|''
name|'def'
name|'inject_file'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'b64_path'
op|','
name|'b64_contents'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Writes a file on the specified instance.\n\n        The first parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name. The second\n        parameter is the base64-encoded path to which the file is to be\n        written on the instance; the third is the contents of the file, also\n        base64-encoded.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|rescue
dedent|''
name|'def'
name|'rescue'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Rescue the specified instance.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unrescue
dedent|''
name|'def'
name|'unrescue'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Unrescue the specified instance.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|migrate_disk_and_power_off
dedent|''
name|'def'
name|'migrate_disk_and_power_off'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Transfers the disk of a running instance in multiple phases, turning\n        off the instance before the end.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|attach_disk
dedent|''
name|'def'
name|'attach_disk'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Attaches the disk to an instance given the metadata disk_info\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|pause
dedent|''
name|'def'
name|'pause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Pause the specified instance.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unpause
dedent|''
name|'def'
name|'unpause'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Unpause the specified instance.\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|suspend
dedent|''
name|'def'
name|'suspend'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        suspend the specified instance\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|resume
dedent|''
name|'def'
name|'resume'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'callback'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        resume the specified instance\n        """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Destroy (shutdown and delete) the specified instance.\n\n        The given parameter is an instance of nova.compute.service.Instance,\n        and so the instance is being specified as instance.name.\n\n        The work will be done asynchronously.  This function returns a\n        task that allows the caller to detect when it is complete.\n        """'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance'
op|'.'
name|'name'
op|']'
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
string|'"""Attach the disk at device_path to the instance at mountpoint"""'
newline|'\n'
name|'return'
name|'True'
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
string|'"""Detach the disk attached to the instance at mountpoint"""'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get a block of information about the given instance.  This is returned\n        as a dictionary containing \'state\': The power_state of the instance,\n        \'max_mem\': The maximum memory for the instance, in KiB, \'mem\': The\n        current memory the instance has, in KiB, \'num_cpu\': The current number\n        of virtual CPUs the instance has, \'cpu_time\': The total CPU time used\n        by the instance, in nanoseconds.\n\n        This method should raise exception.NotFound if the hypervisor has no\n        knowledge of the instance\n        """'
newline|'\n'
name|'if'
name|'instance_name'
name|'not'
name|'in'
name|'self'
op|'.'
name|'instances'
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
string|'"Instance %s Not Found"'
op|')'
nl|'\n'
op|'%'
name|'instance_name'
op|')'
newline|'\n'
dedent|''
name|'i'
op|'='
name|'self'
op|'.'
name|'instances'
op|'['
name|'instance_name'
op|']'
newline|'\n'
name|'return'
op|'{'
string|"'state'"
op|':'
name|'i'
op|'.'
name|'state'
op|','
nl|'\n'
string|"'max_mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'mem'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'num_cpu'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'cpu_time'"
op|':'
number|'0'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|list_disks
dedent|''
name|'def'
name|'list_disks'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual disks attached to the specified\n        instance, as a list.  These IDs are opaque to the caller (they are\n        only useful for giving back to this layer as a parameter to\n        disk_stats).  These IDs only need to be unique for a given instance.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
string|"'A_DISK'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|list_interfaces
dedent|''
name|'def'
name|'list_interfaces'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return the IDs of all the virtual network interfaces attached to the\n        specified instance, as a list.  These IDs are opaque to the caller\n        (they are only useful for giving back to this layer as a parameter to\n        interface_stats).  These IDs only need to be unique for a given\n        instance.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
string|"'A_VIF'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|block_stats
dedent|''
name|'def'
name|'block_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'disk_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given disk_id on the\n        given instance_name.  These are returned as [rd_req, rd_bytes, wr_req,\n        wr_bytes, errs], where rd indicates read, wr indicates write, req is\n        the total number of I/O requests made, bytes is the total number of\n        bytes transferred, and errs is the number of requests held up due to a\n        full pipeline.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
name|'None'
op|']'
newline|'\n'
nl|'\n'
DECL|member|interface_stats
dedent|''
name|'def'
name|'interface_stats'
op|'('
name|'self'
op|','
name|'instance_name'
op|','
name|'iface_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return performance counters associated with the given iface_id on the\n        given instance_id.  These are returned as [rx_bytes, rx_packets,\n        rx_errs, rx_drop, tx_bytes, tx_packets, tx_errs, tx_drop], where rx\n        indicates receive, tx indicates transmit, bytes and packets indicate\n        the total number of bytes or packets transferred, and errs and dropped\n        is the total number of packets failed / dropped.\n\n        All counters are long integers.\n\n        This method is optional.  On some platforms (e.g. XenAPI) performance\n        statistics can be retrieved directly in aggregate form, without Nova\n        having to do the aggregation.  On those platforms, this method is\n        unused.\n\n        Note that this function takes an instance ID, not a\n        compute.service.Instance, so that it can be called by compute.monitor.\n        """'
newline|'\n'
name|'return'
op|'['
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|','
number|'0L'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_console_output
dedent|''
name|'def'
name|'get_console_output'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'FAKE CONSOLE OUTPUT'"
newline|'\n'
nl|'\n'
DECL|member|get_ajax_console
dedent|''
name|'def'
name|'get_ajax_console'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'token'"
op|':'
string|"'FAKETOKEN'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fakeajaxconsole.com'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'6969'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_vnc_console
dedent|''
name|'def'
name|'get_vnc_console'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'token'"
op|':'
string|"'FAKETOKEN'"
op|','
nl|'\n'
string|"'host'"
op|':'
string|"'fakevncconsole.com'"
op|','
nl|'\n'
string|"'port'"
op|':'
number|'6969'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_console_pool_info
dedent|''
name|'def'
name|'get_console_pool_info'
op|'('
name|'self'
op|','
name|'console_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'address'"
op|':'
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'username'"
op|':'
string|"'fakeuser'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'fakepassword'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_rules
dedent|''
name|'def'
name|'refresh_security_group_rules'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called after a change to security groups.\n\n        All security groups and their associated rules live in the datastore,\n        and calling this method should apply the updated rules to instances\n        running the specified security group.\n\n        An error should be raised if the operation cannot complete.\n\n        """'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|refresh_security_group_members
dedent|''
name|'def'
name|'refresh_security_group_members'
op|'('
name|'self'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is called when a security group is added to an instance.\n\n        This message is sent to the virtualization drivers on hosts that are\n        running an instance that belongs to a security group that has a rule\n        that references the security group identified by `security_group_id`.\n        It is the responsiblity of this method to make sure any rules\n        that authorize traffic flow with members of the security group are\n        updated and any new members can communicate, and any removed members\n        cannot.\n\n        Scenario:\n            * we are running on host \'H0\' and we have an instance \'i-0\'.\n            * instance \'i-0\' is a member of security group \'speaks-b\'\n            * group \'speaks-b\' has an ingress rule that authorizes group \'b\'\n            * another host \'H1\' runs an instance \'i-1\'\n            * instance \'i-1\' is a member of security group \'b\'\n\n            When \'i-1\' launches or terminates we will recieve the message\n            to update members of group \'b\', at which time we will make\n            any changes needed to the rules for instance \'i-0\' to allow\n            or deny traffic coming from \'i-1\', depending on if it is being\n            added or removed from the group.\n\n        In this scenario, \'i-1\' could just as easily have been running on our\n        host \'H0\' and this method would still have been called.  The point was\n        that this method isn\'t called on the host where instances of that\n        group are running (as is the case with\n        :method:`refresh_security_group_rules`) but is called where references\n        are made to authorizing those instances.\n\n        An error should be raised if the operation cannot complete.\n\n        """'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|update_available_resource
dedent|''
name|'def'
name|'update_available_resource'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|compare_cpu
dedent|''
name|'def'
name|'compare_cpu'
op|'('
name|'self'
op|','
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|ensure_filtering_rules_for_instance
dedent|''
name|'def'
name|'ensure_filtering_rules_for_instance'
op|'('
name|'self'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|live_migration
dedent|''
name|'def'
name|'live_migration'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_ref'
op|','
name|'dest'
op|','
nl|'\n'
name|'post_method'
op|','
name|'recover_method'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
DECL|member|unfilter_instance
dedent|''
name|'def'
name|'unfilter_instance'
op|'('
name|'self'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is supported only by libvirt."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only by libvirt.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_vm
dedent|''
name|'def'
name|'test_remove_vm'
op|'('
name|'self'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Removes the named VM, as if it crashed. For testing"""'
newline|'\n'
name|'self'
op|'.'
name|'instances'
op|'.'
name|'pop'
op|'('
name|'instance_name'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
