begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'# Copyright (c) 2011 University of Southern California / ISI'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NodeDriver
name|'class'
name|'NodeDriver'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|cache_images
dedent|''
name|'def'
name|'cache_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|destroy_images
dedent|''
name|'def'
name|'destroy_images'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|activate_bootloader
dedent|''
name|'def'
name|'activate_bootloader'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deactivate_bootloader
dedent|''
name|'def'
name|'deactivate_bootloader'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|activate_node
dedent|''
name|'def'
name|'activate_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""For operations after power on."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deactivate_node
dedent|''
name|'def'
name|'deactivate_node'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""For operations before power off."""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
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
name|'node'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PowerManager
dedent|''
dedent|''
name|'class'
name|'PowerManager'
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
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'pass'
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
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
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
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
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
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
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
string|'"""Returns True or False according as the node\'s power state"""'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|'# TODO(NTTdocomo): split out console methods to its own class'
nl|'\n'
DECL|member|start_console
dedent|''
name|'def'
name|'start_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|stop_console
dedent|''
name|'def'
name|'stop_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
