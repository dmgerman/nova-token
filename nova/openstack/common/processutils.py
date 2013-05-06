begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation.'
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
string|'"""\nSystem-level utilities and helper functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'shlex'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
op|'.'
name|'green'
name|'import'
name|'subprocess'
newline|'\n'
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
name|'log'
name|'as'
name|'logging'
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
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnknownArgumentError
name|'class'
name|'UnknownArgumentError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'UnknownArgumentError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessExecutionError
dedent|''
dedent|''
name|'class'
name|'ProcessExecutionError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stdout'
op|'='
name|'None'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'exit_code'
op|'='
name|'None'
op|','
name|'cmd'
op|'='
name|'None'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'exit_code'
op|'='
name|'exit_code'
newline|'\n'
name|'self'
op|'.'
name|'stderr'
op|'='
name|'stderr'
newline|'\n'
name|'self'
op|'.'
name|'stdout'
op|'='
name|'stdout'
newline|'\n'
name|'self'
op|'.'
name|'cmd'
op|'='
name|'cmd'
newline|'\n'
name|'self'
op|'.'
name|'description'
op|'='
name|'description'
newline|'\n'
nl|'\n'
name|'if'
name|'description'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'description'
op|'='
string|'"Unexpected error while running command."'
newline|'\n'
dedent|''
name|'if'
name|'exit_code'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'exit_code'
op|'='
string|"'-'"
newline|'\n'
dedent|''
name|'message'
op|'='
op|'('
string|'"%s\\nCommand: %s\\nExit code: %s\\nStdout: %r\\nStderr: %r"'
nl|'\n'
op|'%'
op|'('
name|'description'
op|','
name|'cmd'
op|','
name|'exit_code'
op|','
name|'stdout'
op|','
name|'stderr'
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'ProcessExecutionError'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoRootWrapSpecified
dedent|''
dedent|''
name|'class'
name|'NoRootWrapSpecified'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'message'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NoRootWrapSpecified'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'message'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_subprocess_setup
dedent|''
dedent|''
name|'def'
name|'_subprocess_setup'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# Python installs a SIGPIPE handler by default. This is usually not what'
nl|'\n'
comment|'# non-Python subprocesses expect.'
nl|'\n'
indent|'    '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGPIPE'
op|','
name|'signal'
op|'.'
name|'SIG_DFL'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
dedent|''
name|'def'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Helper method to shell out and execute a command through subprocess with\n    optional retry.\n\n    :param cmd:             Passed to subprocess.Popen.\n    :type cmd:              string\n    :param process_input:   Send to opened process.\n    :type proces_input:     string\n    :param check_exit_code: Single bool, int, or list of allowed exit\n                            codes.  Defaults to [0].  Raise\n                            :class:`ProcessExecutionError` unless\n                            program exits with one of these code.\n    :type check_exit_code:  boolean, int, or [int]\n    :param delay_on_retry:  True | False. Defaults to True. If set to True,\n                            wait a short amount of time before retrying.\n    :type delay_on_retry:   boolean\n    :param attempts:        How many times to retry cmd.\n    :type attempts:         int\n    :param run_as_root:     True | False. Defaults to False. If set to True,\n                            the command is prefixed by the command specified\n                            in the root_helper kwarg.\n    :type run_as_root:      boolean\n    :param root_helper:     command to prefix to commands called with\n                            run_as_root=True\n    :type root_helper:      string\n    :param shell:           whether or not there should be a shell used to\n                            execute this command. Defaults to false.\n    :type shell:            boolean\n    :returns:               (stdout, stderr) from process execution\n    :raises:                :class:`UnknownArgumentError` on\n                            receiving unknown arguments\n    :raises:                :class:`ProcessExecutionError`\n    """'
newline|'\n'
nl|'\n'
name|'process_input'
op|'='
name|'kwargs'
op|'.'
name|'pop'
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
name|'pop'
op|'('
string|"'check_exit_code'"
op|','
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'ignore_exit_code'
op|'='
name|'False'
newline|'\n'
name|'delay_on_retry'
op|'='
name|'kwargs'
op|'.'
name|'pop'
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
name|'pop'
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
name|'pop'
op|'('
string|"'run_as_root'"
op|','
name|'False'
op|')'
newline|'\n'
name|'root_helper'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'root_helper'"
op|','
string|"''"
op|')'
newline|'\n'
name|'shell'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'shell'"
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'check_exit_code'
op|','
name|'bool'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ignore_exit_code'
op|'='
name|'not'
name|'check_exit_code'
newline|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'check_exit_code'
op|','
name|'int'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'check_exit_code'
op|'='
op|'['
name|'check_exit_code'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'UnknownArgumentError'
op|'('
name|'_'
op|'('
string|"'Got unknown keyword args '"
nl|'\n'
string|"'to utils.execute: %r'"
op|')'
op|'%'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'run_as_root'
name|'and'
name|'os'
op|'.'
name|'geteuid'
op|'('
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'root_helper'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NoRootWrapSpecified'
op|'('
nl|'\n'
name|'message'
op|'='
op|'('
string|"'Command requested root, but did not specify a root '"
nl|'\n'
string|"'helper.'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'cmd'
op|'='
name|'shlex'
op|'.'
name|'split'
op|'('
name|'root_helper'
op|')'
op|'+'
name|'list'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'='
name|'map'
op|'('
name|'str'
op|','
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'attempts'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'attempts'
op|'-='
number|'1'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Running cmd (subprocess): %s'"
op|')'
op|','
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'_PIPE'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
comment|'# pylint: disable=E1101'
newline|'\n'
nl|'\n'
name|'if'
name|'os'
op|'.'
name|'name'
op|'=='
string|"'nt'"
op|':'
newline|'\n'
indent|'                '
name|'preexec_fn'
op|'='
name|'None'
newline|'\n'
name|'close_fds'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'preexec_fn'
op|'='
name|'_subprocess_setup'
newline|'\n'
name|'close_fds'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'obj'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
nl|'\n'
name|'stdin'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'_PIPE'
op|','
nl|'\n'
name|'close_fds'
op|'='
name|'close_fds'
op|','
nl|'\n'
name|'preexec_fn'
op|'='
name|'preexec_fn'
op|','
nl|'\n'
name|'shell'
op|'='
name|'shell'
op|')'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'process_input'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
name|'process_input'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'obj'
op|'.'
name|'communicate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'.'
name|'stdin'
op|'.'
name|'close'
op|'('
op|')'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'_returncode'
op|'='
name|'obj'
op|'.'
name|'returncode'
comment|'# pylint: disable=E1101'
newline|'\n'
name|'if'
name|'_returncode'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Result was %s'"
op|')'
op|'%'
name|'_returncode'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'ignore_exit_code'
name|'and'
name|'_returncode'
name|'not'
name|'in'
name|'check_exit_code'
op|':'
newline|'\n'
indent|'                    '
op|'('
name|'stdout'
op|','
name|'stderr'
op|')'
op|'='
name|'result'
newline|'\n'
name|'raise'
name|'ProcessExecutionError'
op|'('
name|'exit_code'
op|'='
name|'_returncode'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'stdout'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'stderr'
op|','
nl|'\n'
name|'cmd'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'except'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'attempts'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'%r failed. Retrying.'"
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'if'
name|'delay_on_retry'
op|':'
newline|'\n'
indent|'                    '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'random'
op|'.'
name|'randint'
op|'('
number|'20'
op|','
number|'200'
op|')'
op|'/'
number|'100.0'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# NOTE(termie): this appears to be necessary to let the subprocess'
nl|'\n'
comment|'#               call clean something up in between calls, without'
nl|'\n'
comment|'#               it two execute calls in a row hangs the second one'
nl|'\n'
indent|'            '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
