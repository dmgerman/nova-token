begin_unit
comment|'#    Copyright 2012 IBM Corp.'
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
name|'import'
name|'contextlib'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtAPI
name|'class'
name|'VirtAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|provider_fw_rule_get_all
indent|'    '
name|'def'
name|'provider_fw_rule_get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the provider firewall rules\n        :param context: security context\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'contextlib'
op|'.'
name|'contextmanager'
newline|'\n'
DECL|member|wait_for_instance_event
name|'def'
name|'wait_for_instance_event'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'event_names'
op|','
name|'deadline'
op|'='
number|'300'
op|','
nl|'\n'
name|'error_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
