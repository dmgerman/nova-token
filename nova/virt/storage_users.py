begin_unit
comment|'# Copyright 2012 Michael Still and Canonical Inc'
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
nl|'\n'
name|'import'
name|'json'
newline|'\n'
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
name|'utils'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|TWENTY_FOUR_HOURS
name|'TWENTY_FOUR_HOURS'
op|'='
number|'3600'
op|'*'
number|'24'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(morganfainberg): Due to circular import dependencies, the use of the'
nl|'\n'
comment|'# CONF.instances_path needs to be wrapped so that it can be resolved at the'
nl|'\n'
comment|'# appropriate time. Because compute.manager imports this file, we end up in'
nl|'\n'
comment|'# a rather ugly dependency loop without moving this into a wrapped function.'
nl|'\n'
comment|'# This issue mostly stems from the use of a decorator for the lock'
nl|'\n'
comment|'# synchronize and the implications of how decorators wrap the wrapped function'
nl|'\n'
comment|'# or method.  If this needs to be used outside of compute.manager, it should'
nl|'\n'
comment|'# be refactored to eliminate this circular dependency loop.'
nl|'\n'
DECL|function|register_storage_use
name|'def'
name|'register_storage_use'
op|'('
name|'storage_path'
op|','
name|'hostname'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Identify the id of this instance storage."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(morganfainberg): config option import is avoided here since it is'
nl|'\n'
comment|'# explicitly imported from compute.manager and may cause issues with'
nl|'\n'
comment|'# defining options after config has been processed with the'
nl|'\n'
comment|'# wrapped-function style used here.'
nl|'\n'
name|'LOCK_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
string|"'locks'"
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'storage-registry-lock'"
op|','
name|'external'
op|'='
name|'True'
op|','
nl|'\n'
name|'lock_path'
op|'='
name|'LOCK_PATH'
op|')'
newline|'\n'
DECL|function|do_register_storage_use
name|'def'
name|'do_register_storage_use'
op|'('
name|'storage_path'
op|','
name|'hostname'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): this is required to determine if the instance storage is'
nl|'\n'
comment|'# shared, which is something that the image cache manager needs to'
nl|'\n'
comment|'# know. I can imagine other uses as well though.'
nl|'\n'
nl|'\n'
indent|'        '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'id_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'storage_path'
op|','
string|"'compute_nodes'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'id_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'id_path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'d'
op|'['
name|'hostname'
op|']'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'with'
name|'open'
op|'('
name|'id_path'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
name|'json'
op|'.'
name|'dumps'
op|'('
name|'d'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'do_register_storage_use'
op|'('
name|'storage_path'
op|','
name|'hostname'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(morganfainberg): Due to circular import dependencies, the use of the'
nl|'\n'
comment|'# CONF.instances_path needs to be wrapped so that it can be resolved at the'
nl|'\n'
comment|'# appropriate time. Because compute.manager imports this file, we end up in'
nl|'\n'
comment|'# a rather ugly dependency loop without moving this into a wrapped function.'
nl|'\n'
comment|'# This issue mostly stems from the use of a decorator for the lock'
nl|'\n'
comment|'# synchronize and the implications of how decorators wrap the wrapped function'
nl|'\n'
comment|'# or method.  If this needs to be used outside of compute.manager, it should'
nl|'\n'
comment|'# be refactored to eliminate this circular dependency loop.'
nl|'\n'
DECL|function|get_storage_users
dedent|''
name|'def'
name|'get_storage_users'
op|'('
name|'storage_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get a list of all the users of this storage path."""'
newline|'\n'
nl|'\n'
comment|'# NOTE(morganfainberg): config option import is avoided here since it is'
nl|'\n'
comment|'# explicitly imported from compute.manager and may cause issues with'
nl|'\n'
comment|'# defining options after config has been processed with the'
nl|'\n'
comment|'# wrapped-function style used here.'
nl|'\n'
name|'LOCK_PATH'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'instances_path'
op|','
string|"'locks'"
op|')'
newline|'\n'
nl|'\n'
op|'@'
name|'utils'
op|'.'
name|'synchronized'
op|'('
string|"'storage-registry-lock'"
op|','
name|'external'
op|'='
name|'True'
op|','
nl|'\n'
name|'lock_path'
op|'='
name|'LOCK_PATH'
op|')'
newline|'\n'
DECL|function|do_get_storage_users
name|'def'
name|'do_get_storage_users'
op|'('
name|'storage_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'id_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'storage_path'
op|','
string|"'compute_nodes'"
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'id_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'id_path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'f'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'recent_users'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'d'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'d'
op|'['
name|'node'
op|']'
op|'<'
name|'TWENTY_FOUR_HOURS'
op|':'
newline|'\n'
indent|'                '
name|'recent_users'
op|'.'
name|'append'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'recent_users'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'do_get_storage_users'
op|'('
name|'storage_path'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
