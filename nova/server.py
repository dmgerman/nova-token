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
nl|'\n'
string|'"""\nBase functionality for nova daemons - gradually being replaced with twistd.py.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'daemon'
newline|'\n'
name|'from'
name|'daemon'
name|'import'
name|'pidlockfile'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
name|'import'
name|'os'
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
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'DEFINE_bool'
op|'('
string|"'daemonize'"
op|','
name|'False'
op|','
string|"'daemonize this process'"
op|')'
newline|'\n'
comment|'# NOTE(termie): right now I am defaulting to using syslog when we daemonize'
nl|'\n'
comment|'#               it may be better to do something else -shrug-'
nl|'\n'
comment|'# NOTE(Devin): I think we should let each process have its own log file'
nl|'\n'
comment|'#              and put it in /var/logs/nova/(appname).log'
nl|'\n'
comment|'#              This makes debugging much easier and cuts down on sys log'
nl|'\n'
comment|'#              clutter.'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'use_syslog'"
op|','
name|'True'
op|','
string|"'output to syslog when daemonizing'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logfile'"
op|','
name|'None'
op|','
string|"'log file to output to'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'logdir'"
op|','
name|'None'
op|','
string|"'directory to keep log files in '"
nl|'\n'
string|"'(will be prepended to $logfile)'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'pidfile'"
op|','
name|'None'
op|','
string|"'pid file to output to'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'working_directory'"
op|','
string|"'./'"
op|','
string|"'working directory...'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'uid'"
op|','
name|'os'
op|'.'
name|'getuid'
op|'('
op|')'
op|','
string|"'uid under which to run'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'gid'"
op|','
name|'os'
op|'.'
name|'getgid'
op|'('
op|')'
op|','
string|"'gid under which to run'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stop
name|'def'
name|'stop'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Stop the daemon\n    """'
newline|'\n'
comment|'# Get the pid from the pidfile'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'pid'
op|'='
name|'int'
op|'('
name|'open'
op|'('
name|'pidfile'
op|','
string|"'r'"
op|')'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'        '
name|'message'
op|'='
string|'"pidfile %s does not exist. Daemon not running?\\n"'
newline|'\n'
name|'sys'
op|'.'
name|'stderr'
op|'.'
name|'write'
op|'('
name|'message'
op|'%'
name|'pidfile'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# Try killing the daemon process'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'while'
number|'1'
op|':'
newline|'\n'
indent|'            '
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
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'OSError'
op|','
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'err'
op|'='
name|'str'
op|'('
name|'err'
op|')'
newline|'\n'
name|'if'
name|'err'
op|'.'
name|'find'
op|'('
string|'"No such process"'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'remove'
op|'('
name|'pidfile'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'str'
op|'('
name|'err'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|serve
dedent|''
dedent|''
dedent|''
name|'def'
name|'serve'
op|'('
name|'name'
op|','
name|'main'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Controller for server"""'
newline|'\n'
name|'argv'
op|'='
name|'FLAGS'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'pidfile'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'pidfile'
op|'='
string|"'%s.pid'"
op|'%'
name|'name'
newline|'\n'
nl|'\n'
dedent|''
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Full set of FLAGS: \\n\\n\\n"'
op|')'
newline|'\n'
name|'for'
name|'flag'
name|'in'
name|'FLAGS'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"%s : %s"'
op|','
name|'flag'
op|','
name|'FLAGS'
op|'.'
name|'get'
op|'('
name|'flag'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'action'
op|'='
string|"'start'"
newline|'\n'
name|'if'
name|'len'
op|'('
name|'argv'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'        '
name|'action'
op|'='
name|'argv'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'action'
op|'=='
string|"'stop'"
op|':'
newline|'\n'
indent|'        '
name|'stop'
op|'('
name|'FLAGS'
op|'.'
name|'pidfile'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|"'restart'"
op|':'
newline|'\n'
indent|'        '
name|'stop'
op|'('
name|'FLAGS'
op|'.'
name|'pidfile'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'action'
op|'=='
string|"'start'"
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'usage: %s [options] [start|stop|restart]'"
op|'%'
name|'argv'
op|'['
number|'0'
op|']'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'daemonize'
op|'('
name|'argv'
op|','
name|'name'
op|','
name|'main'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemonize
dedent|''
name|'def'
name|'daemonize'
op|'('
name|'args'
op|','
name|'name'
op|','
name|'main'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Does the work of daemonizing the process"""'
newline|'\n'
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'amqplib'"
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARN'
op|')'
newline|'\n'
name|'files_to_keep'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'daemonize'
op|':'
newline|'\n'
indent|'        '
name|'logger'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'formatter'
op|'='
name|'logging'
op|'.'
name|'Formatter'
op|'('
nl|'\n'
name|'name'
op|'+'
string|"'(%(name)s): %(levelname)s %(message)s'"
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_syslog'
name|'and'
name|'not'
name|'FLAGS'
op|'.'
name|'logfile'
op|':'
newline|'\n'
indent|'            '
name|'syslog'
op|'='
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'('
name|'address'
op|'='
string|"'/dev/log'"
op|')'
newline|'\n'
name|'syslog'
op|'.'
name|'setFormatter'
op|'('
name|'formatter'
op|')'
newline|'\n'
name|'logger'
op|'.'
name|'addHandler'
op|'('
name|'syslog'
op|')'
newline|'\n'
name|'files_to_keep'
op|'.'
name|'append'
op|'('
name|'syslog'
op|'.'
name|'socket'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'FLAGS'
op|'.'
name|'logfile'
op|':'
newline|'\n'
indent|'                '
name|'FLAGS'
op|'.'
name|'logfile'
op|'='
string|"'%s.log'"
op|'%'
name|'name'
newline|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'logdir'
op|':'
newline|'\n'
indent|'                '
name|'FLAGS'
op|'.'
name|'logfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'logdir'
op|','
name|'FLAGS'
op|'.'
name|'logfile'
op|')'
newline|'\n'
dedent|''
name|'logfile'
op|'='
name|'logging'
op|'.'
name|'FileHandler'
op|'('
name|'FLAGS'
op|'.'
name|'logfile'
op|')'
newline|'\n'
name|'logfile'
op|'.'
name|'setFormatter'
op|'('
name|'formatter'
op|')'
newline|'\n'
name|'logger'
op|'.'
name|'addHandler'
op|'('
name|'logfile'
op|')'
newline|'\n'
name|'files_to_keep'
op|'.'
name|'append'
op|'('
name|'logfile'
op|'.'
name|'stream'
op|')'
newline|'\n'
dedent|''
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'None'
op|','
name|'None'
op|','
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'stdin'
op|','
name|'stdout'
op|','
name|'stderr'
op|'='
name|'sys'
op|'.'
name|'stdin'
op|','
name|'sys'
op|'.'
name|'stdout'
op|','
name|'sys'
op|'.'
name|'stderr'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'FLAGS'
op|'.'
name|'verbose'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'getLogger'
op|'('
op|')'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'WARNING'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'daemon'
op|'.'
name|'DaemonContext'
op|'('
nl|'\n'
name|'detach_process'
op|'='
name|'FLAGS'
op|'.'
name|'daemonize'
op|','
nl|'\n'
name|'working_directory'
op|'='
name|'FLAGS'
op|'.'
name|'working_directory'
op|','
nl|'\n'
name|'pidfile'
op|'='
name|'pidlockfile'
op|'.'
name|'TimeoutPIDLockFile'
op|'('
name|'FLAGS'
op|'.'
name|'pidfile'
op|','
nl|'\n'
name|'acquire_timeout'
op|'='
number|'1'
op|','
nl|'\n'
name|'threaded'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'stdin'
op|'='
name|'stdin'
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
name|'uid'
op|'='
name|'FLAGS'
op|'.'
name|'uid'
op|','
nl|'\n'
name|'gid'
op|'='
name|'FLAGS'
op|'.'
name|'gid'
op|','
nl|'\n'
name|'files_preserve'
op|'='
name|'files_to_keep'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'main'
op|'('
name|'args'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
