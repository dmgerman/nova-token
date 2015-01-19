begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""Generic Node base class for all workers that run on hosts."""'
newline|'\n'
nl|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'logging'
name|'as'
name|'std_logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# Importing just the symbol here because the io module does not'
nl|'\n'
comment|'# exist in Python 2.6.'
nl|'\n'
indent|'    '
name|'from'
name|'io'
name|'import'
name|'UnsupportedOperation'
comment|'# noqa'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
comment|'# Python 2.6'
nl|'\n'
DECL|variable|UnsupportedOperation
indent|'    '
name|'UnsupportedOperation'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'import'
name|'eventlet'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'eventlet_backdoor'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'_i18n'
name|'import'
name|'_LE'
op|','
name|'_LI'
op|','
name|'_LW'
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
name|'systemd'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'threadgroup'
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
DECL|function|_sighup_supported
name|'def'
name|'_sighup_supported'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'hasattr'
op|'('
name|'signal'
op|','
string|"'SIGHUP'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_daemon
dedent|''
name|'def'
name|'_is_daemon'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# The process group for a foreground process will match the'
nl|'\n'
comment|'# process group of the controlling terminal. If those values do'
nl|'\n'
comment|'# not match, or ioctl() fails on the stdout file handle, we assume'
nl|'\n'
comment|'# the process is running in the background as a daemon.'
nl|'\n'
comment|'# http://www.gnu.org/software/bash/manual/bashref.html#Job-Control-Basics'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'is_daemon'
op|'='
name|'os'
op|'.'
name|'getpgrp'
op|'('
op|')'
op|'!='
name|'os'
op|'.'
name|'tcgetpgrp'
op|'('
name|'sys'
op|'.'
name|'stdout'
op|'.'
name|'fileno'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'err'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOTTY'
op|':'
newline|'\n'
comment|'# Assume we are a daemon because there is no terminal.'
nl|'\n'
indent|'            '
name|'is_daemon'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'UnsupportedOperation'
op|':'
newline|'\n'
comment|'# Could not get the fileno for stdout, so we must be a daemon.'
nl|'\n'
indent|'        '
name|'is_daemon'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'is_daemon'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_sighup_and_daemon
dedent|''
name|'def'
name|'_is_sighup_and_daemon'
op|'('
name|'signo'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
op|'('
name|'_sighup_supported'
op|'('
op|')'
name|'and'
name|'signo'
op|'=='
name|'signal'
op|'.'
name|'SIGHUP'
op|')'
op|':'
newline|'\n'
comment|"# Avoid checking if we are a daemon, because the signal isn't"
nl|'\n'
comment|'# SIGHUP.'
nl|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'_is_daemon'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_signo_to_signame
dedent|''
name|'def'
name|'_signo_to_signame'
op|'('
name|'signo'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'signals'
op|'='
op|'{'
name|'signal'
op|'.'
name|'SIGTERM'
op|':'
string|"'SIGTERM'"
op|','
nl|'\n'
name|'signal'
op|'.'
name|'SIGINT'
op|':'
string|"'SIGINT'"
op|'}'
newline|'\n'
name|'if'
name|'_sighup_supported'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'signals'
op|'['
name|'signal'
op|'.'
name|'SIGHUP'
op|']'
op|'='
string|"'SIGHUP'"
newline|'\n'
dedent|''
name|'return'
name|'signals'
op|'['
name|'signo'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_set_signals_handler
dedent|''
name|'def'
name|'_set_signals_handler'
op|'('
name|'handler'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGTERM'
op|','
name|'handler'
op|')'
newline|'\n'
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGINT'
op|','
name|'handler'
op|')'
newline|'\n'
name|'if'
name|'_sighup_supported'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGHUP'
op|','
name|'handler'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Launcher
dedent|''
dedent|''
name|'class'
name|'Launcher'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Launch one or more services and wait for them to complete."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Initialize the service launcher.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'='
name|'Services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'backdoor_port'
op|'='
name|'eventlet_backdoor'
op|'.'
name|'initialize_if_enabled'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|launch_service
dedent|''
name|'def'
name|'launch_service'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Load and start the given service.\n\n        :param service: The service you would like to start.\n        :returns: None\n\n        """'
newline|'\n'
name|'service'
op|'.'
name|'backdoor_port'
op|'='
name|'self'
op|'.'
name|'backdoor_port'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'add'
op|'('
name|'service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stop all services which are currently running.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Waits until all services have been stopped, and then returns.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|restart
dedent|''
name|'def'
name|'restart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reload config files and restart service.\n\n        :returns: None\n\n        """'
newline|'\n'
name|'cfg'
op|'.'
name|'CONF'
op|'.'
name|'reload_config_files'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'restart'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SignalExit
dedent|''
dedent|''
name|'class'
name|'SignalExit'
op|'('
name|'SystemExit'
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
name|'signo'
op|','
name|'exccode'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'SignalExit'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'exccode'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'signo'
op|'='
name|'signo'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceLauncher
dedent|''
dedent|''
name|'class'
name|'ServiceLauncher'
op|'('
name|'Launcher'
op|')'
op|':'
newline|'\n'
DECL|member|_handle_signal
indent|'    '
name|'def'
name|'_handle_signal'
op|'('
name|'self'
op|','
name|'signo'
op|','
name|'frame'
op|')'
op|':'
newline|'\n'
comment|'# Allow the process to be killed again and die from natural causes'
nl|'\n'
indent|'        '
name|'_set_signals_handler'
op|'('
name|'signal'
op|'.'
name|'SIG_DFL'
op|')'
newline|'\n'
name|'raise'
name|'SignalExit'
op|'('
name|'signo'
op|')'
newline|'\n'
nl|'\n'
DECL|member|handle_signal
dedent|''
name|'def'
name|'handle_signal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_set_signals_handler'
op|'('
name|'self'
op|'.'
name|'_handle_signal'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wait_for_exit_or_signal
dedent|''
name|'def'
name|'_wait_for_exit_or_signal'
op|'('
name|'self'
op|','
name|'ready_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'status'
op|'='
name|'None'
newline|'\n'
name|'signo'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Full set of CONF:'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'log_opt_values'
op|'('
name|'LOG'
op|','
name|'std_logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ready_callback'
op|':'
newline|'\n'
indent|'                '
name|'ready_callback'
op|'('
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'ServiceLauncher'
op|','
name|'self'
op|')'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'SignalExit'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'signame'
op|'='
name|'_signo_to_signame'
op|'('
name|'exc'
op|'.'
name|'signo'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Caught %s, exiting'"
op|')'
op|','
name|'signame'
op|')'
newline|'\n'
name|'status'
op|'='
name|'exc'
op|'.'
name|'code'
newline|'\n'
name|'signo'
op|'='
name|'exc'
op|'.'
name|'signo'
newline|'\n'
dedent|''
name|'except'
name|'SystemExit'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
name|'exc'
op|'.'
name|'code'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'status'
op|','
name|'signo'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|','
name|'ready_callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'systemd'
op|'.'
name|'notify_once'
op|'('
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle_signal'
op|'('
op|')'
newline|'\n'
name|'status'
op|','
name|'signo'
op|'='
name|'self'
op|'.'
name|'_wait_for_exit_or_signal'
op|'('
name|'ready_callback'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'_is_sighup_and_daemon'
op|'('
name|'signo'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'status'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'restart'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServiceWrapper
dedent|''
dedent|''
dedent|''
name|'class'
name|'ServiceWrapper'
op|'('
name|'object'
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
name|'service'
op|','
name|'workers'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'service'
op|'='
name|'service'
newline|'\n'
name|'self'
op|'.'
name|'workers'
op|'='
name|'workers'
newline|'\n'
name|'self'
op|'.'
name|'children'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'forktimes'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessLauncher
dedent|''
dedent|''
name|'class'
name|'ProcessLauncher'
op|'('
name|'object'
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
name|'wait_interval'
op|'='
number|'0.01'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Constructor.\n\n        :param wait_interval: The interval to sleep for between checks\n                              of child process exit.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'children'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'sigcaught'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'running'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'wait_interval'
op|'='
name|'wait_interval'
newline|'\n'
name|'rfd'
op|','
name|'self'
op|'.'
name|'writepipe'
op|'='
name|'os'
op|'.'
name|'pipe'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'readpipe'
op|'='
name|'eventlet'
op|'.'
name|'greenio'
op|'.'
name|'GreenPipe'
op|'('
name|'rfd'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle_signal'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|handle_signal
dedent|''
name|'def'
name|'handle_signal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_set_signals_handler'
op|'('
name|'self'
op|'.'
name|'_handle_signal'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_handle_signal
dedent|''
name|'def'
name|'_handle_signal'
op|'('
name|'self'
op|','
name|'signo'
op|','
name|'frame'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'sigcaught'
op|'='
name|'signo'
newline|'\n'
name|'self'
op|'.'
name|'running'
op|'='
name|'False'
newline|'\n'
nl|'\n'
comment|'# Allow the process to be killed again and die from natural causes'
nl|'\n'
name|'_set_signals_handler'
op|'('
name|'signal'
op|'.'
name|'SIG_DFL'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_pipe_watcher
dedent|''
name|'def'
name|'_pipe_watcher'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# This will block until the write end is closed when the parent'
nl|'\n'
comment|'# dies unexpectedly'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'readpipe'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Parent process has died unexpectedly, exiting'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_child_process_handle_signal
dedent|''
name|'def'
name|'_child_process_handle_signal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Setup child signal handlers differently'
nl|'\n'
DECL|function|_sigterm
indent|'        '
name|'def'
name|'_sigterm'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGTERM'
op|','
name|'signal'
op|'.'
name|'SIG_DFL'
op|')'
newline|'\n'
name|'raise'
name|'SignalExit'
op|'('
name|'signal'
op|'.'
name|'SIGTERM'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_sighup
dedent|''
name|'def'
name|'_sighup'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGHUP'
op|','
name|'signal'
op|'.'
name|'SIG_DFL'
op|')'
newline|'\n'
name|'raise'
name|'SignalExit'
op|'('
name|'signal'
op|'.'
name|'SIGHUP'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGTERM'
op|','
name|'_sigterm'
op|')'
newline|'\n'
name|'if'
name|'_sighup_supported'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGHUP'
op|','
name|'_sighup'
op|')'
newline|'\n'
comment|'# Block SIGINT and let the parent send us a SIGTERM'
nl|'\n'
dedent|''
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGINT'
op|','
name|'signal'
op|'.'
name|'SIG_IGN'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_child_wait_for_exit_or_signal
dedent|''
name|'def'
name|'_child_wait_for_exit_or_signal'
op|'('
name|'self'
op|','
name|'launcher'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'status'
op|'='
number|'0'
newline|'\n'
name|'signo'
op|'='
number|'0'
newline|'\n'
nl|'\n'
comment|'# NOTE(johannes): All exceptions are caught to ensure this'
nl|'\n'
comment|"# doesn't fallback into the loop spawning children. It would"
nl|'\n'
comment|'# be bad for a child to spawn more children.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'launcher'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'SignalExit'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'signame'
op|'='
name|'_signo_to_signame'
op|'('
name|'exc'
op|'.'
name|'signo'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Child caught %s, exiting'"
op|')'
op|','
name|'signame'
op|')'
newline|'\n'
name|'status'
op|'='
name|'exc'
op|'.'
name|'code'
newline|'\n'
name|'signo'
op|'='
name|'exc'
op|'.'
name|'signo'
newline|'\n'
dedent|''
name|'except'
name|'SystemExit'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
name|'exc'
op|'.'
name|'code'
newline|'\n'
dedent|''
name|'except'
name|'BaseException'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|"'Unhandled exception'"
op|')'
op|')'
newline|'\n'
name|'status'
op|'='
number|'2'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'launcher'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'status'
op|','
name|'signo'
newline|'\n'
nl|'\n'
DECL|member|_child_process
dedent|''
name|'def'
name|'_child_process'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_child_process_handle_signal'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Reopen the eventlet hub to make sure we don't share an epoll"
nl|'\n'
comment|'# fd with parent and/or siblings, which would be bad'
nl|'\n'
name|'eventlet'
op|'.'
name|'hubs'
op|'.'
name|'use_hub'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Close write to ensure only parent has it open'
nl|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'self'
op|'.'
name|'writepipe'
op|')'
newline|'\n'
comment|'# Create greenthread to watch for parent to close pipe'
nl|'\n'
name|'eventlet'
op|'.'
name|'spawn_n'
op|'('
name|'self'
op|'.'
name|'_pipe_watcher'
op|')'
newline|'\n'
nl|'\n'
comment|'# Reseed random number generator'
nl|'\n'
name|'random'
op|'.'
name|'seed'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'launcher'
op|'='
name|'Launcher'
op|'('
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'launch_service'
op|'('
name|'service'
op|')'
newline|'\n'
name|'return'
name|'launcher'
newline|'\n'
nl|'\n'
DECL|member|_start_child
dedent|''
name|'def'
name|'_start_child'
op|'('
name|'self'
op|','
name|'wrap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'wrap'
op|'.'
name|'forktimes'
op|')'
op|'>'
name|'wrap'
op|'.'
name|'workers'
op|':'
newline|'\n'
comment|'# Limit ourselves to one process a second (over the period of'
nl|'\n'
comment|'# number of workers * 1 second). This will allow workers to'
nl|'\n'
comment|"# start up quickly but ensure we don't fork off children that"
nl|'\n'
comment|'# die instantly too quickly.'
nl|'\n'
indent|'            '
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'wrap'
op|'.'
name|'forktimes'
op|'['
number|'0'
op|']'
op|'<'
name|'wrap'
op|'.'
name|'workers'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Forking too fast, sleeping'"
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'wrap'
op|'.'
name|'forktimes'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'wrap'
op|'.'
name|'forktimes'
op|'.'
name|'append'
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'pid'
op|'='
name|'os'
op|'.'
name|'fork'
op|'('
op|')'
newline|'\n'
name|'if'
name|'pid'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'launcher'
op|'='
name|'self'
op|'.'
name|'_child_process'
op|'('
name|'wrap'
op|'.'
name|'service'
op|')'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_child_process_handle_signal'
op|'('
op|')'
newline|'\n'
name|'status'
op|','
name|'signo'
op|'='
name|'self'
op|'.'
name|'_child_wait_for_exit_or_signal'
op|'('
name|'launcher'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'_is_sighup_and_daemon'
op|'('
name|'signo'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'launcher'
op|'.'
name|'restart'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'_exit'
op|'('
name|'status'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Started child %d'"
op|')'
op|','
name|'pid'
op|')'
newline|'\n'
nl|'\n'
name|'wrap'
op|'.'
name|'children'
op|'.'
name|'add'
op|'('
name|'pid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'children'
op|'['
name|'pid'
op|']'
op|'='
name|'wrap'
newline|'\n'
nl|'\n'
name|'return'
name|'pid'
newline|'\n'
nl|'\n'
DECL|member|launch_service
dedent|''
name|'def'
name|'launch_service'
op|'('
name|'self'
op|','
name|'service'
op|','
name|'workers'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'wrap'
op|'='
name|'ServiceWrapper'
op|'('
name|'service'
op|','
name|'workers'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Starting %d workers'"
op|')'
op|','
name|'wrap'
op|'.'
name|'workers'
op|')'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'running'
name|'and'
name|'len'
op|'('
name|'wrap'
op|'.'
name|'children'
op|')'
op|'<'
name|'wrap'
op|'.'
name|'workers'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_start_child'
op|'('
name|'wrap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_wait_child
dedent|''
dedent|''
name|'def'
name|'_wait_child'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
comment|"# Don't block if no child processes have exited"
nl|'\n'
indent|'            '
name|'pid'
op|','
name|'status'
op|'='
name|'os'
op|'.'
name|'waitpid'
op|'('
number|'0'
op|','
name|'os'
op|'.'
name|'WNOHANG'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pid'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'exc'
op|'.'
name|'errno'
name|'not'
name|'in'
op|'('
name|'errno'
op|'.'
name|'EINTR'
op|','
name|'errno'
op|'.'
name|'ECHILD'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'WIFSIGNALED'
op|'('
name|'status'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'sig'
op|'='
name|'os'
op|'.'
name|'WTERMSIG'
op|'('
name|'status'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Child %(pid)d killed by signal %(sig)d'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'pid'
op|'='
name|'pid'
op|','
name|'sig'
op|'='
name|'sig'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'code'
op|'='
name|'os'
op|'.'
name|'WEXITSTATUS'
op|'('
name|'status'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Child %(pid)s exited with status %(code)d'"
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'pid'
op|'='
name|'pid'
op|','
name|'code'
op|'='
name|'code'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'pid'
name|'not'
name|'in'
name|'self'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|"'pid %d not in child list'"
op|')'
op|','
name|'pid'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'wrap'
op|'='
name|'self'
op|'.'
name|'children'
op|'.'
name|'pop'
op|'('
name|'pid'
op|')'
newline|'\n'
name|'wrap'
op|'.'
name|'children'
op|'.'
name|'remove'
op|'('
name|'pid'
op|')'
newline|'\n'
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
DECL|member|_respawn_children
dedent|''
name|'def'
name|'_respawn_children'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'while'
name|'self'
op|'.'
name|'running'
op|':'
newline|'\n'
indent|'            '
name|'wrap'
op|'='
name|'self'
op|'.'
name|'_wait_child'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'wrap'
op|':'
newline|'\n'
comment|'# Yield to other threads if no children have exited'
nl|'\n'
comment|'# Sleep for a short time to avoid excessive CPU usage'
nl|'\n'
comment|'# (see bug #1095346)'
nl|'\n'
indent|'                '
name|'eventlet'
op|'.'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'self'
op|'.'
name|'wait_interval'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'while'
name|'self'
op|'.'
name|'running'
name|'and'
name|'len'
op|'('
name|'wrap'
op|'.'
name|'children'
op|')'
op|'<'
name|'wrap'
op|'.'
name|'workers'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_start_child'
op|'('
name|'wrap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Loop waiting on children to die and respawning as necessary."""'
newline|'\n'
nl|'\n'
name|'systemd'
op|'.'
name|'notify_once'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Full set of CONF:'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'log_opt_values'
op|'('
name|'LOG'
op|','
name|'std_logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle_signal'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_respawn_children'
op|'('
op|')'
newline|'\n'
comment|"# No signal means that stop was called.  Don't clean up here."
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'sigcaught'
op|':'
newline|'\n'
indent|'                    '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'signame'
op|'='
name|'_signo_to_signame'
op|'('
name|'self'
op|'.'
name|'sigcaught'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Caught %s, stopping children'"
op|')'
op|','
name|'signame'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'_is_sighup_and_daemon'
op|'('
name|'self'
op|'.'
name|'sigcaught'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'pid'
name|'in'
name|'self'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGHUP'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'running'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'sigcaught'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'eventlet'
op|'.'
name|'greenlet'
op|'.'
name|'GreenletExit'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Wait called after thread killed. Cleaning up."'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Terminate child processes and wait on each."""'
newline|'\n'
name|'self'
op|'.'
name|'running'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'pid'
name|'in'
name|'self'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGTERM'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'exc'
op|'.'
name|'errno'
op|'!='
name|'errno'
op|'.'
name|'ESRCH'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
nl|'\n'
comment|'# Wait for children to die'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Waiting on %d children to exit'"
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'children'
op|')'
op|')'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'children'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_wait_child'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Service
dedent|''
dedent|''
dedent|''
dedent|''
name|'class'
name|'Service'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Service object for binaries running on hosts."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'threads'
op|'='
number|'1000'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tg'
op|'='
name|'threadgroup'
op|'.'
name|'ThreadGroup'
op|'('
name|'threads'
op|')'
newline|'\n'
nl|'\n'
comment|'# signal that the service is done shutting itself down:'
nl|'\n'
name|'self'
op|'.'
name|'_done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset
dedent|''
name|'def'
name|'reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(Fengqian): docs for Event.reset() recommend against using it'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|','
name|'graceful'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tg'
op|'.'
name|'stop'
op|'('
name|'graceful'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tg'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
comment|'# Signal that service cleanup is done:'
nl|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_done'
op|'.'
name|'ready'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_done'
op|'.'
name|'send'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Services
dedent|''
dedent|''
name|'class'
name|'Services'
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
name|'self'
op|'.'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'tg'
op|'='
name|'threadgroup'
op|'.'
name|'ThreadGroup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add
dedent|''
name|'def'
name|'add'
op|'('
name|'self'
op|','
name|'service'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'service'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tg'
op|'.'
name|'add_thread'
op|'('
name|'self'
op|'.'
name|'run_service'
op|','
name|'service'
op|','
name|'self'
op|'.'
name|'done'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# wait for graceful shutdown of services:'
nl|'\n'
indent|'        '
name|'for'
name|'service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'service'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'service'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Each service has performed cleanup, now signal that the run_service'
nl|'\n'
comment|'# wrapper threads can now die:'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'done'
op|'.'
name|'ready'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'done'
op|'.'
name|'send'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# reap threads:'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'tg'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait
dedent|''
name|'def'
name|'wait'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'tg'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|restart
dedent|''
name|'def'
name|'restart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
name|'for'
name|'restart_service'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'restart_service'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tg'
op|'.'
name|'add_thread'
op|'('
name|'self'
op|'.'
name|'run_service'
op|','
name|'restart_service'
op|','
name|'self'
op|'.'
name|'done'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|run_service
name|'def'
name|'run_service'
op|'('
name|'service'
op|','
name|'done'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Service start wrapper.\n\n        :param service: service to run\n        :param done: event to wait on until a shutdown is triggered\n        :returns: None\n\n        """'
newline|'\n'
name|'service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|launch
dedent|''
dedent|''
name|'def'
name|'launch'
op|'('
name|'service'
op|','
name|'workers'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'workers'
name|'is'
name|'None'
name|'or'
name|'workers'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'launcher'
op|'='
name|'ServiceLauncher'
op|'('
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'launch_service'
op|'('
name|'service'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'launcher'
op|'='
name|'ProcessLauncher'
op|'('
op|')'
newline|'\n'
name|'launcher'
op|'.'
name|'launch_service'
op|'('
name|'service'
op|','
name|'workers'
op|'='
name|'workers'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'launcher'
newline|'\n'
dedent|''
endmarker|''
end_unit
