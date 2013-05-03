begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
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
string|'"""This modules stubs out functions in nova.utils."""'
newline|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
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
DECL|variable|_fake_execute_repliers
name|'_fake_execute_repliers'
op|'='
op|'['
op|']'
newline|'\n'
DECL|variable|_fake_execute_log
name|'_fake_execute_log'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute_get_log
name|'def'
name|'fake_execute_get_log'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_fake_execute_log'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute_clear_log
dedent|''
name|'def'
name|'fake_execute_clear_log'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_fake_execute_log'
newline|'\n'
name|'_fake_execute_log'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute_set_repliers
dedent|''
name|'def'
name|'fake_execute_set_repliers'
op|'('
name|'repliers'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Allows the client to configure replies to commands."""'
newline|'\n'
name|'global'
name|'_fake_execute_repliers'
newline|'\n'
name|'_fake_execute_repliers'
op|'='
name|'repliers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute_default_reply_handler
dedent|''
name|'def'
name|'fake_execute_default_reply_handler'
op|'('
op|'*'
name|'ignore_args'
op|','
op|'**'
name|'ignore_kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A reply handler for commands that haven\'t been added to the reply list.\n\n    Returns empty strings for stdout and stderr.\n\n    """'
newline|'\n'
name|'return'
string|"''"
op|','
string|"''"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_execute
dedent|''
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd_parts'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This function stubs out execute.\n\n    It optionally executes a preconfigued function to return expected data.\n\n    """'
newline|'\n'
name|'global'
name|'_fake_execute_repliers'
newline|'\n'
nl|'\n'
name|'process_input'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'process_input'"
op|','
name|'None'
op|')'
newline|'\n'
name|'check_exit_code'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'check_exit_code'"
op|','
number|'0'
op|')'
newline|'\n'
name|'delay_on_retry'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'delay_on_retry'"
op|','
name|'True'
op|')'
newline|'\n'
name|'attempts'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'attempts'"
op|','
number|'1'
op|')'
newline|'\n'
name|'run_as_root'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'run_as_root'"
op|','
name|'False'
op|')'
newline|'\n'
name|'cmd_str'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
name|'str'
op|'('
name|'part'
op|')'
name|'for'
name|'part'
name|'in'
name|'cmd_parts'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Faking execution of cmd (subprocess): %s"'
op|')'
op|','
name|'cmd_str'
op|')'
newline|'\n'
name|'_fake_execute_log'
op|'.'
name|'append'
op|'('
name|'cmd_str'
op|')'
newline|'\n'
nl|'\n'
name|'reply_handler'
op|'='
name|'fake_execute_default_reply_handler'
newline|'\n'
nl|'\n'
name|'for'
name|'fake_replier'
name|'in'
name|'_fake_execute_repliers'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'re'
op|'.'
name|'match'
op|'('
name|'fake_replier'
op|'['
number|'0'
op|']'
op|','
name|'cmd_str'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'reply_handler'
op|'='
name|'fake_replier'
op|'['
number|'1'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Faked command matched %s'"
op|')'
op|'%'
name|'fake_replier'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'reply_handler'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
comment|'# If the reply handler is a string, return it as stdout'
nl|'\n'
indent|'        '
name|'reply'
op|'='
name|'reply_handler'
op|','
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|'# Alternative is a function, so call it'
nl|'\n'
indent|'            '
name|'reply'
op|'='
name|'reply_handler'
op|'('
name|'cmd_parts'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'process_input'
op|','
nl|'\n'
name|'delay_on_retry'
op|'='
name|'delay_on_retry'
op|','
nl|'\n'
name|'attempts'
op|'='
name|'attempts'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'run_as_root'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Faked command raised an exception %s'"
op|')'
op|','
name|'e'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'stdout'
op|'='
name|'reply'
op|'['
number|'0'
op|']'
newline|'\n'
name|'stderr'
op|'='
name|'reply'
op|'['
number|'1'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Reply to faked command is stdout=\'%(stdout)s\' "'
nl|'\n'
string|'"stderr=\'%(stderr)s\'"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Replicate the sleep call in the real function'
nl|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'return'
name|'reply'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_utils_execute
dedent|''
name|'def'
name|'stub_out_utils_execute'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fake_execute_set_repliers'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'fake_execute_clear_log'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
