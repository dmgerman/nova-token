begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack, LLC.'
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
string|'"""Handles ConsoleProxy API requests."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'rpcapi'
name|'as'
name|'compute_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'console'
name|'import'
name|'rpcapi'
name|'as'
name|'console_rpcapi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
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
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for spinning up or down console proxy connections."""'
newline|'\n'
nl|'\n'
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
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_consoles
dedent|''
name|'def'
name|'get_consoles'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_get_all_by_instance'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_console
dedent|''
name|'def'
name|'get_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'console_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_get'
op|'('
name|'context'
op|','
name|'console_uuid'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_console
dedent|''
name|'def'
name|'delete_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'console_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'console'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'console_get'
op|'('
name|'context'
op|','
name|'console_uuid'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'topic'
op|'='
name|'rpc'
op|'.'
name|'queue_get_for'
op|'('
name|'context'
op|','
name|'FLAGS'
op|'.'
name|'console_topic'
op|','
nl|'\n'
name|'console'
op|'['
string|"'pool'"
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'rpcapi'
op|'='
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|'('
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'rpcapi'
op|'.'
name|'remove_console'
op|'('
name|'context'
op|','
name|'console'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_console
dedent|''
name|'def'
name|'create_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
comment|'#NOTE(mdragon): If we wanted to return this the console info'
nl|'\n'
comment|'#               here, as we would need to do a call.'
nl|'\n'
comment|'#               They can just do an index later to fetch'
nl|'\n'
comment|'#               console info. I am not sure which is better'
nl|'\n'
comment|'#               here.'
nl|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_get_instance'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'topic'
op|'='
name|'self'
op|'.'
name|'_get_console_topic'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'host'"
op|']'
op|')'
op|','
newline|'\n'
name|'rpcapi'
op|'='
name|'console_rpcapi'
op|'.'
name|'ConsoleAPI'
op|'('
name|'topic'
op|'='
name|'topic'
op|')'
newline|'\n'
name|'rpcapi'
op|'.'
name|'add_console'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_console_topic
dedent|''
name|'def'
name|'_get_console_topic'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_host'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpcapi'
op|'='
name|'compute_rpcapi'
op|'.'
name|'ComputeAPI'
op|'('
op|')'
newline|'\n'
name|'return'
name|'rpcapi'
op|'.'
name|'get_console_topic'
op|'('
name|'context'
op|','
name|'instance_host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_instance
dedent|''
name|'def'
name|'_get_instance'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'instance'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
