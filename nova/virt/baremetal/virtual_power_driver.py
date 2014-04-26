begin_unit
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# All Rights Reserved.'
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
comment|'#'
nl|'\n'
comment|'# Virtual power driver'
nl|'\n'
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
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
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
name|'importutils'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'common'
name|'as'
name|'connection'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virtual_power_ssh_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP or name to virtual power host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'virtual_power_ssh_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'22'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Port to use for ssh to virtual power host'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virtual_power_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'virsh'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base command to use for virtual power(vbox, virsh)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virtual_power_host_user'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'User to execute virtual power commands as'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virtual_power_host_pass'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password for virtual power host_user'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'virtual_power_host_key'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The ssh key for virtual power host_user'"
op|')'
op|','
nl|'\n'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|baremetal_vp
name|'baremetal_vp'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Baremetal Options'"
op|')'
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
name|'register_group'
op|'('
name|'baremetal_vp'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|','
name|'baremetal_vp'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_conn
name|'_conn'
op|'='
name|'None'
newline|'\n'
DECL|variable|_vp_cmd
name|'_vp_cmd'
op|'='
name|'None'
newline|'\n'
DECL|variable|_cmds
name|'_cmds'
op|'='
name|'None'
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
DECL|function|_normalize_mac
name|'def'
name|'_normalize_mac'
op|'('
name|'mac'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'mac'
op|'.'
name|'replace'
op|'('
string|"':'"
op|','
string|"''"
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtualPowerManager
dedent|''
name|'class'
name|'VirtualPowerManager'
op|'('
name|'base'
op|'.'
name|'PowerManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Virtual Power Driver for Baremetal Nova Compute\n\n    This PowerManager class provides mechanism for controlling the power state\n    of VMs based on their name and MAC address. It uses ssh to connect to the\n    VM\'s host and issue commands.\n\n    Node will be matched based on mac address\n\n    NOTE: for use in dev/test environments only!\n\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'_conn'
newline|'\n'
name|'global'
name|'_cmds'
newline|'\n'
nl|'\n'
name|'if'
name|'_cmds'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Setting up %s commands."'
op|')'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_type'
op|')'
newline|'\n'
name|'_vpc'
op|'='
string|"'nova.virt.baremetal.virtual_power_driver_settings.%s'"
op|'%'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_type'
newline|'\n'
name|'_cmds'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'_vpc'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_vp_cmd'
op|'='
name|'_cmds'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'connection_data'
op|'='
name|'_conn'
newline|'\n'
name|'node'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'node'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'instance'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_node_name'
op|'='
name|'instance'
op|'.'
name|'get'
op|'('
string|"'hostname'"
op|','
string|'""'
op|')'
newline|'\n'
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'ifs'
op|'='
name|'db'
op|'.'
name|'bm_interface_get_all_by_bm_node_id'
op|'('
name|'context'
op|','
name|'node'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mac_addresses'
op|'='
op|'['
name|'_normalize_mac'
op|'('
name|'i'
op|'['
string|"'address'"
op|']'
op|')'
name|'for'
name|'i'
name|'in'
name|'ifs'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_connection'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_matched_name'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_get_conn
dedent|''
name|'def'
name|'_get_conn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_ssh_host'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'virtual_power_ssh_host not defined. Can not Start'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_user'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'virtual_power_host_user not defined. Can not Start'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_pass'
op|':'
newline|'\n'
comment|'# it is ok to not have a password if you have a keyfile'
nl|'\n'
indent|'            '
name|'if'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_key'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|"'virtual_power_host_pass/key not set. Can not Start'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'_conn'
op|'='
name|'connection'
op|'.'
name|'Connection'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_ssh_host'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_user'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_pass'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_ssh_port'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'virtual_power_host_key'
op|')'
newline|'\n'
name|'return'
name|'_conn'
newline|'\n'
nl|'\n'
DECL|member|_set_connection
dedent|''
name|'def'
name|'_set_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_connection'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'connection_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'connection_data'
op|'='
name|'self'
op|'.'
name|'_get_conn'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_connection'
op|'='
name|'connection'
op|'.'
name|'ssh_connect'
op|'('
name|'self'
op|'.'
name|'connection_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_full_node_list
dedent|''
dedent|''
name|'def'
name|'_get_full_node_list'
op|'('
name|'self'
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
string|'"Getting full node list."'
op|')'
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'list_cmd'
newline|'\n'
name|'full_list'
op|'='
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'full_list'
newline|'\n'
nl|'\n'
DECL|member|_check_for_node
dedent|''
name|'def'
name|'_check_for_node'
op|'('
name|'self'
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
string|'"Looking up Name for Mac address %s."'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_mac_addresses'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_matched_name'
op|'='
string|"''"
newline|'\n'
name|'full_node_list'
op|'='
name|'self'
op|'.'
name|'_get_full_node_list'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'full_node_list'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'get_node_macs'
op|'.'
name|'replace'
op|'('
string|"'{_NodeName_}'"
op|','
name|'node'
op|')'
newline|'\n'
name|'mac_address_list'
op|'='
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'mac'
name|'in'
name|'mac_address_list'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'_normalize_mac'
op|'('
name|'mac'
op|')'
name|'in'
name|'self'
op|'.'
name|'_mac_addresses'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_matched_name'
op|'='
op|'('
string|'\'"%s"\''
op|'%'
name|'node'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'_matched_name'
newline|'\n'
nl|'\n'
DECL|member|activate_node
dedent|''
name|'def'
name|'activate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"activate_node name %s"'
op|')'
op|','
name|'self'
op|'.'
name|'_node_name'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'start_cmd'
newline|'\n'
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|reboot_node
dedent|''
name|'def'
name|'reboot_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"reset node: %s"'
op|')'
op|','
name|'self'
op|'.'
name|'_node_name'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'reboot_cmd'
newline|'\n'
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|deactivate_node
dedent|''
name|'def'
name|'deactivate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"deactivate_node name %s"'
op|')'
op|','
name|'self'
op|'.'
name|'_node_name'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'stop_cmd'
newline|'\n'
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'is_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|is_power_on
dedent|''
name|'def'
name|'is_power_on'
op|'('
name|'self'
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
string|'"Checking if %s is running"'
op|')'
op|','
name|'self'
op|'.'
name|'_node_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_check_for_node'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'err_msg'
op|'='
name|'_'
op|'('
string|'\'Node "%(name)s" with MAC address %(mac)s not found.\''
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'err_msg'
op|','
op|'{'
string|"'name'"
op|':'
name|'self'
op|'.'
name|'_node_name'
op|','
nl|'\n'
string|"'mac'"
op|':'
name|'self'
op|'.'
name|'_mac_addresses'
op|'}'
op|')'
newline|'\n'
comment|'# in our case the _node_name is the node_id'
nl|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NodeNotFound'
op|'('
name|'node_id'
op|'='
name|'self'
op|'.'
name|'_node_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'='
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'list_running_cmd'
newline|'\n'
name|'running_node_list'
op|'='
name|'self'
op|'.'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'node'
name|'in'
name|'running_node_list'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_matched_name'
name|'in'
name|'node'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_run_command
dedent|''
name|'def'
name|'_run_command'
op|'('
name|'self'
op|','
name|'cmd'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Run a remote command using an active ssh connection.\n\n        :param command: String with the command to run.\n\n        If {_NodeName_} is in the command it will get replaced by\n        the _matched_name value.\n\n        base_cmd will also get prepended to the command.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_set_connection'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'cmd'
op|'='
name|'cmd'
op|'.'
name|'replace'
op|'('
string|"'{_NodeName_}'"
op|','
name|'self'
op|'.'
name|'_matched_name'
op|')'
newline|'\n'
nl|'\n'
name|'cmd'
op|'='
string|"'%s %s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_vp_cmd'
op|'.'
name|'base_cmd'
op|','
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'stdout'
op|','
name|'stderr'
op|'='
name|'processutils'
op|'.'
name|'ssh_execute'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_connection'
op|','
name|'cmd'
op|','
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
name|'result'
op|'='
name|'stdout'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'splitlines'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Result for run_command: %s'"
op|')'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Error running command: %s"'
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
