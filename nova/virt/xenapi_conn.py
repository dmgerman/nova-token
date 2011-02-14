begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nA connection to XenServer or Xen Cloud Platform.\n\nThe concurrency model for this class is as follows:\n\nAll XenAPI calls are on a green thread (using eventlet\'s "tpool"\nthread pool). They are remote calls, and so may hang for the usual\nreasons.\n\nAll long-running XenAPI calls (VM.start, VM.reboot, etc) are called async\n(using XenAPI.VM.async_start etc). These return a task, which can then be\npolled for completion.\n\nThis combination of techniques means that we don\'t block the main thread at\nall, and at the same time we don\'t hold lots of threads waiting for\nlong-running operations.\n\nFIXME: get_info currently doesn\'t conform to these rules, and will block the\nreactor thread if the VM.get_by_name_label or VM.get_record calls block.\n\n**Related Flags**\n\n:xenapi_connection_url:  URL for connection to XenServer/Xen Cloud Platform.\n:xenapi_connection_username:  Username for connection to XenServer/Xen Cloud\n                              Platform (default: root).\n:xenapi_connection_password:  Password for connection to XenServer/Xen Cloud\n                              Platform.\n:xenapi_task_poll_interval:  The interval (seconds) used for polling of\n                             remote tasks (Async.VM.start, etc)\n                             (default: 0.5).\n:target_host:                the iSCSI Target Host IP address, i.e. the IP\n                             address for the nova-volume host\n:target_port:                iSCSI Target Port, 3260 Default\n:iqn_prefix:                 IQN Prefix, e.g. \'iqn.2010-10.org.openstack\'\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
name|'import'
name|'xmlrpclib'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'tpool'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'vmops'
name|'import'
name|'VMOps'
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
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.virt.xenapi"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_url'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'URL for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Required if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_username'"
op|','
nl|'\n'
string|"'root'"
op|','
nl|'\n'
string|"'Username for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_connection_password'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'Password for connection to XenServer/Xen Cloud Platform.'"
nl|'\n'
string|"' Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'xenapi_task_poll_interval'"
op|','
nl|'\n'
number|'0.5'
op|','
nl|'\n'
string|"'The interval used for polling of remote tasks '"
nl|'\n'
string|"'(Async.VM.start, etc). Used only if '"
nl|'\n'
string|"'connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_image_service'"
op|','
nl|'\n'
string|"'glance'"
op|','
nl|'\n'
string|"'Where to get VM images: glance or objectstore.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_float'
op|'('
string|"'xenapi_vhd_coalesce_poll_interval'"
op|','
nl|'\n'
number|'5.0'
op|','
nl|'\n'
string|"'The interval used for polling of coalescing vhds.'"
nl|'\n'
string|"'  Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'xenapi_vhd_coalesce_max_attempts'"
op|','
nl|'\n'
number|'5'
op|','
nl|'\n'
string|"'Max number of times to poll for VHD to coalesce.'"
nl|'\n'
string|"'  Used only if connection_type=xenapi.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'target_host'"
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
string|"'iSCSI Target Host'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'target_port'"
op|','
nl|'\n'
string|"'3260'"
op|','
nl|'\n'
string|"'iSCSI Target Port, 3260 Default'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'iqn_prefix'"
op|','
nl|'\n'
string|"'iqn.2010-10.org.openstack'"
op|','
nl|'\n'
string|"'IQN Prefix'"
op|')'
newline|'\n'
comment|'# NOTE(sirp): This is a work-around for a bug in Ubuntu Maverick, when we pull'
nl|'\n'
comment|'# support for it, we should remove this'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'xenapi_remap_vbd_dev'"
op|','
name|'False'
op|','
nl|'\n'
string|"'Used to enable the remapping of VBD dev '"
nl|'\n'
string|"'(Works around an issue in Ubuntu Maverick)'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'xenapi_remap_vbd_dev_prefix'"
op|','
string|"'sd'"
op|','
nl|'\n'
string|"'Specify prefix to remap VBD dev to '"
nl|'\n'
string|"'(ex. /dev/xvdb -> /dev/sdb)'"
op|')'
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
indent|'    '
string|'"""Note that XenAPI doesn\'t have a read-only connection mode, so\n    the read_only parameter is ignored."""'
newline|'\n'
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
name|'if'
name|'not'
name|'url'
name|'or'
name|'password'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Must specify xenapi_connection_url, '"
nl|'\n'
string|"'xenapi_connection_username (optionally), and '"
nl|'\n'
string|"'xenapi_connection_password to use '"
nl|'\n'
string|"'connection_type=xenapi'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'XenAPIConnection'
op|'('
name|'url'
op|','
name|'username'
op|','
name|'password'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIConnection
dedent|''
name|'class'
name|'XenAPIConnection'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A connection to XenServer or Xen Cloud Platform"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'XenAPISession'
op|'('
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'='
name|'VMOps'
op|'('
name|'session'
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
comment|'#FIXME(armando): implement this'
nl|'\n'
comment|'#NOTE(armando): would we need a method'
nl|'\n'
comment|'#to call when shutting down the host?'
nl|'\n'
comment|'#e.g. to do session logout?'
nl|'\n'
indent|'        '
name|'pass'
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
string|'"""List VM instances"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'list_instances'
op|'('
op|')'
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
string|'"""Create VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'spawn'
op|'('
name|'instance'
op|')'
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
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Create snapshot from a running VM instance """'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'snapshot'
op|'('
name|'instance'
op|','
name|'image_id'
op|')'
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
string|'"""Reboot VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'reboot'
op|'('
name|'instance'
op|')'
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
string|'"""Set the root/admin password on the VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'set_admin_password'
op|'('
name|'instance'
op|','
name|'new_pass'
op|')'
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
string|'"""Destroy VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'destroy'
op|'('
name|'instance'
op|')'
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
string|'"""Pause VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'pause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
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
string|'"""Unpause paused VM instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'unpause'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
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
string|'"""suspend the specified instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'suspend'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
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
string|'"""resume the specified instance"""'
newline|'\n'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'resume'
op|'('
name|'instance'
op|','
name|'callback'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_info
dedent|''
name|'def'
name|'get_info'
op|'('
name|'self'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM instance"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_info'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_diagnostics
dedent|''
name|'def'
name|'get_diagnostics'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return data about VM diagnostics"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_diagnostics'
op|'('
name|'instance'
op|')'
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
string|'"""Return snapshot of console"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_console_output'
op|'('
name|'instance'
op|')'
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
string|'"""Return link to instance\'s ajax console"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_vmops'
op|'.'
name|'get_ajax_console'
op|'('
name|'instance'
op|')'
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
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'attach_volume'
op|'('
name|'instance_name'
op|','
nl|'\n'
name|'device_path'
op|','
nl|'\n'
name|'mountpoint'
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
name|'return'
name|'self'
op|'.'
name|'_volumeops'
op|'.'
name|'detach_volume'
op|'('
name|'instance_name'
op|','
name|'mountpoint'
op|')'
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
name|'xs_url'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_connection_url'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'address'"
op|':'
name|'xs_url'
op|'.'
name|'netloc'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'FLAGS'
op|'.'
name|'xenapi_connection_username'
op|','
nl|'\n'
string|"'password'"
op|':'
name|'FLAGS'
op|'.'
name|'xenapi_connection_password'
op|'}'
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
string|'"""This method is supported only libvirt.  """'
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
string|'"""This method is supported only libvirt.."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only libvirt.'"
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
string|'"""This method is supported only libvirt.."""'
newline|'\n'
name|'return'
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
string|'"""This method is supported only libvirt.."""'
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
string|'"""This method is supported only libvirt.."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
string|"'This method is supported only libvirt.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPISession
dedent|''
dedent|''
name|'class'
name|'XenAPISession'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The session to invoke XenAPI SDK calls"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'user'
op|','
name|'pw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'XenAPI'
op|'='
name|'self'
op|'.'
name|'get_imported_xenapi'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'='
name|'self'
op|'.'
name|'_create_session'
op|'('
name|'url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'login_with_password'
op|'('
name|'user'
op|','
name|'pw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loop'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_imported_xenapi
dedent|''
name|'def'
name|'get_imported_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubout point. This can be replaced with a mock xenapi module."""'
newline|'\n'
name|'return'
name|'__import__'
op|'('
string|"'XenAPI'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi
dedent|''
name|'def'
name|'get_xenapi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the xenapi object"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
nl|'\n'
DECL|member|get_xenapi_host
dedent|''
name|'def'
name|'get_xenapi_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the xenapi host"""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'session'
op|'.'
name|'get_this_host'
op|'('
name|'self'
op|'.'
name|'_session'
op|'.'
name|'handle'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_xenapi
dedent|''
name|'def'
name|'call_xenapi'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the specified XenAPI method on a background thread."""'
newline|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'method'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'f'
op|'.'
name|'__getattr__'
op|'('
name|'m'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'f'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|call_xenapi_request
dedent|''
name|'def'
name|'call_xenapi_request'
op|'('
name|'self'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Some interactions with dom0, such as interacting with xenstore\'s\n        param record, require using the xenapi_request method of the session\n        object. This wraps that call on a background thread.\n        """'
newline|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi_request'
newline|'\n'
name|'return'
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'f'
op|','
name|'method'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|async_call_plugin
dedent|''
name|'def'
name|'async_call_plugin'
op|'('
name|'self'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call Async.host.call_plugin on a background thread."""'
newline|'\n'
name|'return'
name|'tpool'
op|'.'
name|'execute'
op|'('
name|'self'
op|'.'
name|'_unwrap_plugin_exceptions'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'Async'
op|'.'
name|'host'
op|'.'
name|'call_plugin'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_xenapi_host'
op|'('
op|')'
op|','
name|'plugin'
op|','
name|'fn'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_for_task
dedent|''
name|'def'
name|'wait_for_task'
op|'('
name|'self'
op|','
name|'id'
op|','
name|'task'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the result of the given task. The task is polled\n        until it completes. Not re-entrant."""'
newline|'\n'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loop'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'self'
op|'.'
name|'_poll_task'
op|','
name|'id'
op|','
name|'task'
op|','
name|'done'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loop'
op|'.'
name|'start'
op|'('
name|'FLAGS'
op|'.'
name|'xenapi_task_poll_interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
DECL|member|_stop_loop
dedent|''
name|'def'
name|'_stop_loop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop polling for task to finish."""'
newline|'\n'
comment|'#NOTE(sandy-walsh) Had to break this call out to support unit tests.'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'loop'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'loop'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_session
dedent|''
dedent|''
name|'def'
name|'_create_session'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubout point. This can be replaced with a mock session."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Session'
op|'('
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_poll_task
dedent|''
name|'def'
name|'_poll_task'
op|'('
name|'self'
op|','
name|'id'
op|','
name|'task'
op|','
name|'done'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Poll the given XenAPI task, and fire the given action if we\n        get a result.\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_name_label'
op|'('
name|'task'
op|')'
newline|'\n'
name|'status'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_status'
op|'('
name|'task'
op|')'
newline|'\n'
name|'action'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'instance_id'
op|'='
name|'int'
op|'('
name|'id'
op|')'
op|','
nl|'\n'
name|'action'
op|'='
name|'name'
op|'['
number|'0'
op|':'
number|'255'
op|']'
op|','
comment|'# Ensure action is never > 255'
nl|'\n'
name|'error'
op|'='
name|'None'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|'"pending"'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'status'
op|'=='
string|'"success"'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_result'
op|'('
name|'task'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Task [%(name)s] %(task)s status:"'
nl|'\n'
string|'" success    %(result)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send'
op|'('
name|'_parse_xmlrpc_value'
op|'('
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'error_info'
op|'='
name|'self'
op|'.'
name|'_session'
op|'.'
name|'xenapi'
op|'.'
name|'task'
op|'.'
name|'get_error_info'
op|'('
name|'task'
op|')'
newline|'\n'
name|'action'
op|'['
string|'"error"'
op|']'
op|'='
name|'str'
op|'('
name|'error_info'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Task [%(name)s] %(task)s status:"'
nl|'\n'
string|'" %(status)s    %(error_info)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'error_info'
op|')'
op|')'
newline|'\n'
dedent|''
name|'db'
op|'.'
name|'instance_action_create'
op|'('
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
op|','
name|'action'
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
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'exc'
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
op|'*'
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_stop_loop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_unwrap_plugin_exceptions
dedent|''
name|'def'
name|'_unwrap_plugin_exceptions'
op|'('
name|'self'
op|','
name|'func'
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
string|'"""Parse exception details"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'exc'
op|'.'
name|'details'
op|')'
op|'=='
number|'4'
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'0'
op|']'
op|'=='
string|"'XENAPI_PLUGIN_EXCEPTION'"
name|'and'
nl|'\n'
name|'exc'
op|'.'
name|'details'
op|'['
number|'2'
op|']'
op|'=='
string|"'Failure'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'params'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'params'
op|'='
name|'eval'
op|'('
name|'exc'
op|'.'
name|'details'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exc'
newline|'\n'
dedent|''
name|'raise'
name|'self'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'xmlrpclib'
op|'.'
name|'ProtocolError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Got exception: %s"'
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_parse_xmlrpc_value
dedent|''
dedent|''
dedent|''
name|'def'
name|'_parse_xmlrpc_value'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse the given value as if it were an XML-RPC value. This is\n    sometimes used as the format for the task.result field."""'
newline|'\n'
name|'if'
name|'not'
name|'val'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'val'
newline|'\n'
dedent|''
name|'x'
op|'='
name|'xmlrpclib'
op|'.'
name|'loads'
op|'('
nl|'\n'
string|'\'<?xml version="1.0"?><methodResponse><params><param>\''
op|'+'
nl|'\n'
name|'val'
op|'+'
nl|'\n'
string|"'</param></params></methodResponse>'"
op|')'
newline|'\n'
name|'return'
name|'x'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
