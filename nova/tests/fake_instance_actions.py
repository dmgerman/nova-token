begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2013 OpenStack LLC'
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
name|'import'
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_action_event_start
name|'def'
name|'fake_action_event_start'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_action_event_finish
dedent|''
name|'def'
name|'fake_action_event_finish'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_action_events
dedent|''
name|'def'
name|'stub_out_action_events'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'action_event_start'"
op|','
name|'fake_action_event_start'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'action_event_finish'"
op|','
name|'fake_action_event_finish'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
