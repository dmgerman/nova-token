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
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
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
name|'process'
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
nl|'\n'
nl|'\n'
DECL|class|AOEDriver
name|'class'
name|'AOEDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Executes commands relating to AOE volumes."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'execute'
op|'='
name|'process'
op|'.'
name|'simple_execute'
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
name|'self'
op|'.'
name|'_execute'
op|'='
name|'execute'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|_try_execute
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
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
name|'command'
op|')'
newline|'\n'
name|'defer'
op|'.'
name|'returnValue'
op|'('
name|'True'
op|')'
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
name|'logging'
op|'.'
name|'exception'
op|'('
string|'"Recovering from a failed execute."'
nl|'\n'
string|'"Try number %s"'
op|','
name|'tries'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sleep %s"'
op|'%'
name|'tries'
op|'**'
number|'2'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|create_volume
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'volume_name'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a logical volume."""'
newline|'\n'
comment|'# NOTE(vish): makes sure that the volume group exists'
nl|'\n'
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"vgs %s"'
op|'%'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
newline|'\n'
name|'if'
name|'int'
op|'('
name|'size'
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
name|'size'
newline|'\n'
dedent|''
name|'yield'
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
name|'volume_name'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'volume_group'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|delete_volume
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a logical volume."""'
newline|'\n'
name|'yield'
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
name|'volume_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|create_export
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'volume_name'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates an export for a logical volume."""'
newline|'\n'
name|'yield'
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
name|'volume_name'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|discover_volume
name|'def'
name|'discover_volume'
op|'('
name|'self'
op|','
name|'_volume_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Discover volume on a remote host."""'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo aoe-discover"'
op|')'
newline|'\n'
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sudo aoe-stat"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|remove_export
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'_volume_name'
op|','
name|'shelf_id'
op|','
name|'blade_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes an export for a logical volume."""'
newline|'\n'
name|'yield'
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
name|'yield'
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
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|member|ensure_exports
name|'def'
name|'ensure_exports'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Runs all existing exports."""'
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
name|'yield'
name|'self'
op|'.'
name|'_execute'
op|'('
string|'"sleep 2"'
op|')'
newline|'\n'
name|'yield'
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
name|'yield'
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
name|'self'
op|'.'
name|'fake_execute'
op|')'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"FAKE AOE: %s"'
op|','
name|'cmd'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
