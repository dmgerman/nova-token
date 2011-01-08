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
string|'"""\nDrivers for volumes.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
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
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.volume.driver"'
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'volume_group'"
op|','
string|"'nova-volumes'"
op|','
nl|'\n'
string|"'Name for the VG that will contain exported volumes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'aoe_eth_dev'"
op|','
string|"'eth0'"
op|','
nl|'\n'
string|"'Which device to export the volumes on'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'num_shell_tries'"
op|','
number|'3'
op|','
nl|'\n'
string|"'number of times to attempt to run flakey shell commands'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'num_shelves'"
op|','
nl|'\n'
number|'100'
op|','
nl|'\n'
string|"'Number of vblade shelves'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'blades_per_shelf'"
op|','
nl|'\n'
number|'16'
op|','
nl|'\n'
string|"'Number of vblade blades per shelf'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'iscsi_num_targets'"
op|','
nl|'\n'
number|'100'
op|','
nl|'\n'
string|"'Number of iscsi target ids per host'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'iscsi_target_prefix'"
op|','
string|"'iqn.2010-10.org.openstack:'"
op|','
nl|'\n'
string|"'prefix for iscsi volumes'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'iscsi_ip_prefix'"
op|','
string|"'127.0'"
op|','
nl|'\n'
string|"'discover volumes on the ip that starts with this prefix'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeDriver
name|'class'
name|'VolumeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Executes commands relating to Volumes."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'execute'
op|'='
name|'utils'
op|'.'
name|'execute'
op|','
nl|'\n'
name|'sync_exec'
op|'='
name|'utils'
op|'.'
name|'execute'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): db is set by Manager'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'db'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'='
name|'execute'
newline|'\n'
name|'self'
op|'.'
name|'_sync_exec'
op|'='
name|'sync_exec'
newline|'\n'
nl|'\n'
DECL|member|_try_execute
dedent|''
name|'def'
name|'_try_execute'
op|'('
name|'self'
op|','
name|'command'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Volume commands can partially fail due to timing, but'
nl|'\n'
comment|'#             running them a second time on failure will usually'
nl|'\n'
comment|'#             recover nicely.'
nl|'\n'
indent|'        '
name|'tries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_execute'
op|'('
name|'command'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'                '
name|'tries'
op|'='
name|'tries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'tries'
op|'>='
name|'FLAGS'
op|'.'
name|'num_shell_tries'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"Recovering from a failed execute.  "'
nl|'\n'
string|'"Try number %s"'
op|')'
op|','
name|'tries'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'tries'
op|'**'
number|'2'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_setup_error
dedent|''
dedent|''
dedent|''
name|'def'
name|'check_for_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns an error if prerequisites aren\'t met"""'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
string|'"/dev/%s"'
op|'%'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"volume group %s doesn\'t exist"'
op|')'
nl|'\n'
op|'%'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a logical volume."""'
newline|'\n'
name|'if'
name|'int'
op|'('
name|'volume'
op|'['
string|"'size'"
op|']'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'sizestr'
op|'='
string|"'100M'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sizestr'
op|'='
string|"'%sG'"
op|'%'
name|'volume'
op|'['
string|"'size'"
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_try_execute'
op|'('
string|'"sudo lvcreate -L %s -n %s %s"'
op|'%'
nl|'\n'
op|'('
name|'sizestr'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a logical volume."""'
newline|'\n'
name|'self'
op|'.'
name|'_try_execute'
op|'('
string|'"sudo lvremove -f %s/%s"'
op|'%'
nl|'\n'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|local_path
dedent|''
name|'def'
name|'local_path'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): stops deprecation warning'
nl|'\n'
indent|'        '
name|'escaped_group'
op|'='
name|'FLAGS'
op|'.'
name|'volume_group'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'--'"
op|')'
newline|'\n'
name|'escaped_name'
op|'='
name|'volume'
op|'['
string|"'name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'--'"
op|')'
newline|'\n'
name|'return'
string|'"/dev/mapper/%s-%s"'
op|'%'
op|'('
name|'escaped_group'
op|','
name|'escaped_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
dedent|''
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Synchronously recreates an export for a logical volume."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Exports the volume."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_export
dedent|''
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an export for a logical volume."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|discover_volume
dedent|''
name|'def'
name|'discover_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Discover volume on a remote host."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|undiscover_volume
dedent|''
name|'def'
name|'undiscover_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Undiscover volume on a remote host."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AOEDriver
dedent|''
dedent|''
name|'class'
name|'AOEDriver'
op|'('
name|'VolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Implements AOE specific volume commands."""'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): we depend on vblade-persist for recreating exports'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_ensure_blades
dedent|''
name|'def'
name|'_ensure_blades'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that blades have been created in datastore."""'
newline|'\n'
name|'total_blades'
op|'='
name|'FLAGS'
op|'.'
name|'num_shelves'
op|'*'
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'db'
op|'.'
name|'export_device_count'
op|'('
name|'context'
op|')'
op|'>='
name|'total_blades'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'for'
name|'shelf_id'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'num_shelves'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'blade_id'
name|'in'
name|'xrange'
op|'('
name|'FLAGS'
op|'.'
name|'blades_per_shelf'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'dev'
op|'='
op|'{'
string|"'shelf_id'"
op|':'
name|'shelf_id'
op|','
string|"'blade_id'"
op|':'
name|'blade_id'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'export_device_create_safe'
op|'('
name|'context'
op|','
name|'dev'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates an export for a logical volume."""'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_blades'
op|'('
name|'context'
op|')'
newline|'\n'
op|'('
name|'shelf_id'
op|','
nl|'\n'
name|'blade_id'
op|')'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_allocate_shelf_and_blade'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_try_execute'
op|'('
nl|'\n'
string|'"sudo vblade-persist setup %s %s %s /dev/%s/%s"'
op|'%'
nl|'\n'
op|'('
name|'shelf_id'
op|','
nl|'\n'
name|'blade_id'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'aoe_eth_dev'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|')'
newline|'\n'
comment|'# NOTE(vish): The standard _try_execute does not work here'
nl|'\n'
comment|'#             because these methods throw errors if other'
nl|'\n'
comment|'#             volumes on this host are in the process of'
nl|'\n'
comment|'#             being created.  The good news is the command'
nl|'\n'
comment|'#             still works for the other volumes, so we'
nl|'\n'
comment|'#             just wait a bit for the current volume to'
nl|'\n'
comment|'#             be ready and ignore any errors.'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo vblade-persist auto all"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo vblade-persist start all"'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_export
dedent|''
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an export for a logical volume."""'
newline|'\n'
op|'('
name|'shelf_id'
op|','
nl|'\n'
name|'blade_id'
op|')'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_shelf_and_blade'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_try_execute'
op|'('
string|'"sudo vblade-persist stop %s %s"'
op|'%'
nl|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_try_execute'
op|'('
string|'"sudo vblade-persist destroy %s %s"'
op|'%'
nl|'\n'
op|'('
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|discover_volume
dedent|''
name|'def'
name|'discover_volume'
op|'('
name|'self'
op|','
name|'_volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Discover volume on a remote host."""'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo aoe-discover"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo aoe-stat"'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|undiscover_volume
dedent|''
name|'def'
name|'undiscover_volume'
op|'('
name|'self'
op|','
name|'_volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Undiscover volume on a remote host."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAOEDriver
dedent|''
dedent|''
name|'class'
name|'FakeAOEDriver'
op|'('
name|'AOEDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Logs calls instead of executing."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'FakeAOEDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'execute'
op|'='
name|'self'
op|'.'
name|'fake_execute'
op|','
nl|'\n'
name|'sync_exec'
op|'='
name|'self'
op|'.'
name|'fake_execute'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_setup_error
dedent|''
name|'def'
name|'check_for_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No setup necessary in fake mode."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|fake_execute
name|'def'
name|'fake_execute'
op|'('
name|'cmd'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Execute that simply logs the command."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"FAKE AOE: %s"'
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ISCSIDriver
dedent|''
dedent|''
name|'class'
name|'ISCSIDriver'
op|'('
name|'VolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Executes commands relating to ISCSI volumes."""'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Synchronously recreates an export for a logical volume."""'
newline|'\n'
name|'iscsi_target'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_iscsi_target_num'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'iscsi_name'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iscsi_target_prefix'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'volume_path'
op|'='
string|'"/dev/%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_sync_exec'
op|'('
string|'"sudo ietadm --op new "'
nl|'\n'
string|'"--tid=%s --params Name=%s"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_target'
op|','
name|'iscsi_name'
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_sync_exec'
op|'('
string|'"sudo ietadm --op new --tid=%s "'
nl|'\n'
string|'"--lun=0 --params Path=%s,Type=fileio"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_target'
op|','
name|'volume_path'
op|')'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ensure_iscsi_targets
dedent|''
name|'def'
name|'_ensure_iscsi_targets'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure that target ids have been created in datastore."""'
newline|'\n'
name|'host_iscsi_targets'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'iscsi_target_count_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'if'
name|'host_iscsi_targets'
op|'>='
name|'FLAGS'
op|'.'
name|'iscsi_num_targets'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
comment|'# NOTE(vish): Target ids start at 1, not 0.'
nl|'\n'
dedent|''
name|'for'
name|'target_num'
name|'in'
name|'xrange'
op|'('
number|'1'
op|','
name|'FLAGS'
op|'.'
name|'iscsi_num_targets'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'target'
op|'='
op|'{'
string|"'host'"
op|':'
name|'host'
op|','
string|"'target_num'"
op|':'
name|'target_num'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'iscsi_target_create_safe'
op|'('
name|'context'
op|','
name|'target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates an export for a logical volume."""'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_iscsi_targets'
op|'('
name|'context'
op|','
name|'volume'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'iscsi_target'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_allocate_iscsi_target'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'iscsi_name'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'iscsi_target_prefix'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'volume_path'
op|'='
string|'"/dev/%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'volume_group'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo ietadm --op new "'
nl|'\n'
string|'"--tid=%s --params Name=%s"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_target'
op|','
name|'iscsi_name'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo ietadm --op new --tid=%s "'
nl|'\n'
string|'"--lun=0 --params Path=%s,Type=fileio"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_target'
op|','
name|'volume_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_export
dedent|''
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an export for a logical volume."""'
newline|'\n'
name|'iscsi_target'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_iscsi_target_num'
op|'('
name|'context'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo ietadm --op delete --tid=%s "'
nl|'\n'
string|'"--lun=0"'
op|'%'
name|'iscsi_target'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo ietadm --op delete --tid=%s"'
op|'%'
nl|'\n'
name|'iscsi_target'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_name_and_portal
dedent|''
name|'def'
name|'_get_name_and_portal'
op|'('
name|'self'
op|','
name|'volume_name'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets iscsi name and portal from volume name and host."""'
newline|'\n'
op|'('
name|'out'
op|','
name|'_err'
op|')'
op|'='
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m discovery -t "'
nl|'\n'
string|'"sendtargets -p %s"'
op|'%'
name|'host'
op|')'
newline|'\n'
name|'for'
name|'target'
name|'in'
name|'out'
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
name|'return'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
newline|'\n'
nl|'\n'
DECL|member|discover_volume
dedent|''
name|'def'
name|'discover_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Discover volume on a remote host."""'
newline|'\n'
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|'='
name|'self'
op|'.'
name|'_get_name_and_portal'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m node -T %s -p %s --login"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m node -T %s -p %s --op update "'
nl|'\n'
string|'"-n node.startup -v automatic"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|')'
newline|'\n'
name|'return'
string|'"/dev/iscsi/%s"'
op|'%'
name|'volume'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|undiscover_volume
dedent|''
name|'def'
name|'undiscover_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Undiscover volume on a remote host."""'
newline|'\n'
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|'='
name|'self'
op|'.'
name|'_get_name_and_portal'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m node -T %s -p %s --op update "'
nl|'\n'
string|'"-n node.startup -v manual"'
op|'%'
nl|'\n'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m node -T %s -p %s --logout "'
op|'%'
nl|'\n'
op|'('
name|'iscsi_name'
op|','
name|'iscsi_portal'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo iscsiadm -m node --op delete "'
nl|'\n'
string|'"--targetname %s"'
op|'%'
name|'iscsi_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeISCSIDriver
dedent|''
dedent|''
name|'class'
name|'FakeISCSIDriver'
op|'('
name|'ISCSIDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Logs calls instead of executing."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
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
name|'super'
op|'('
name|'FakeISCSIDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'execute'
op|'='
name|'self'
op|'.'
name|'fake_execute'
op|','
nl|'\n'
name|'sync_exec'
op|'='
name|'self'
op|'.'
name|'fake_execute'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_setup_error
dedent|''
name|'def'
name|'check_for_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""No setup necessary in fake mode."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|fake_execute
name|'def'
name|'fake_execute'
op|'('
name|'cmd'
op|','
op|'*'
name|'_args'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Execute that simply logs the command."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"FAKE ISCSI: %s"'
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
