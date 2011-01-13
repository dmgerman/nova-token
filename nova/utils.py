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
string|'"""\nSystem-level utilities and helper functions.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'struct'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'sax'
name|'import'
name|'saxutils'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'event'
newline|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'exception'
name|'import'
name|'ProcessExecutionError'
newline|'\n'
name|'from'
name|'nova'
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
string|'"nova.utils"'
op|')'
newline|'\n'
DECL|variable|TIME_FORMAT
name|'TIME_FORMAT'
op|'='
string|'"%Y-%m-%dT%H:%M:%SZ"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_class
name|'def'
name|'import_class'
op|'('
name|'import_str'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a class from a string including module and class"""'
newline|'\n'
name|'mod_str'
op|','
name|'_sep'
op|','
name|'class_str'
op|'='
name|'import_str'
op|'.'
name|'rpartition'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
name|'mod_str'
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'sys'
op|'.'
name|'modules'
op|'['
name|'mod_str'
op|']'
op|','
name|'class_str'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ImportError'
op|','
name|'ValueError'
op|','
name|'AttributeError'
op|')'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'Inner Exception: %s'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Class %s cannot be found'"
op|')'
op|'%'
name|'class_str'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_object
dedent|''
dedent|''
name|'def'
name|'import_object'
op|'('
name|'import_str'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns an object including a module or module and class"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
name|'import_str'
op|')'
newline|'\n'
name|'return'
name|'sys'
op|'.'
name|'modules'
op|'['
name|'import_str'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'        '
name|'cls'
op|'='
name|'import_class'
op|'('
name|'import_str'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vpn_ping
dedent|''
dedent|''
name|'def'
name|'vpn_ping'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'timeout'
op|'='
number|'0.05'
op|','
name|'session_id'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sends a vpn negotiation packet and returns the server session.\n\n    Returns False on a failure. Basic packet structure is below.\n\n    Client packet (14 bytes)::\n     0 1      8 9  13\n    +-+--------+-----+\n    |x| cli_id |?????|\n    +-+--------+-----+\n    x = packet identifier 0x38\n    cli_id = 64 bit identifier\n    ? = unknown, probably flags/padding\n\n    Server packet (26 bytes)::\n     0 1      8 9  13 14    21 2225\n    +-+--------+-----+--------+----+\n    |x| srv_id |?????| cli_id |????|\n    +-+--------+-----+--------+----+\n    x = packet identifier 0x40\n    cli_id = 64 bit identifier\n    ? = unknown, probably flags/padding\n    bit 9 was 1 and the rest were 0 in testing\n    """'
newline|'\n'
name|'if'
name|'session_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'session_id'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
number|'0'
op|','
number|'0xffffffffffffffff'
op|')'
newline|'\n'
dedent|''
name|'sock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'data'
op|'='
name|'struct'
op|'.'
name|'pack'
op|'('
string|'"!BQxxxxxx"'
op|','
number|'0x38'
op|','
name|'session_id'
op|')'
newline|'\n'
name|'sock'
op|'.'
name|'sendto'
op|'('
name|'data'
op|','
op|'('
name|'address'
op|','
name|'port'
op|')'
op|')'
newline|'\n'
name|'sock'
op|'.'
name|'settimeout'
op|'('
name|'timeout'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'received'
op|'='
name|'sock'
op|'.'
name|'recv'
op|'('
number|'2048'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'timeout'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'sock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'fmt'
op|'='
string|'"!BQxxxxxQxxxx"'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'received'
op|')'
op|'!='
name|'struct'
op|'.'
name|'calcsize'
op|'('
name|'fmt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'print'
name|'struct'
op|'.'
name|'calcsize'
op|'('
name|'fmt'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
op|'('
name|'identifier'
op|','
name|'server_sess'
op|','
name|'client_sess'
op|')'
op|'='
name|'struct'
op|'.'
name|'unpack'
op|'('
name|'fmt'
op|','
name|'received'
op|')'
newline|'\n'
name|'if'
name|'identifier'
op|'=='
number|'0x40'
name|'and'
name|'client_sess'
op|'=='
name|'session_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'server_sess'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetchfile
dedent|''
dedent|''
name|'def'
name|'fetchfile'
op|'('
name|'url'
op|','
name|'target'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Fetching %s"'
op|')'
op|'%'
name|'url'
op|')'
newline|'\n'
comment|'#    c = pycurl.Curl()'
nl|'\n'
comment|'#    fp = open(target, "wb")'
nl|'\n'
comment|'#    c.setopt(c.URL, url)'
nl|'\n'
comment|'#    c.setopt(c.WRITEDATA, fp)'
nl|'\n'
comment|'#    c.perform()'
nl|'\n'
comment|'#    c.close()'
nl|'\n'
comment|'#    fp.close()'
nl|'\n'
name|'execute'
op|'('
string|'"curl --fail %s -o %s"'
op|'%'
op|'('
name|'url'
op|','
name|'target'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
dedent|''
name|'def'
name|'execute'
op|'('
name|'cmd'
op|','
name|'process_input'
op|'='
name|'None'
op|','
name|'addl_env'
op|'='
name|'None'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Running cmd (subprocess): %s"'
op|')'
op|','
name|'cmd'
op|')'
newline|'\n'
name|'env'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
name|'addl_env'
op|':'
newline|'\n'
indent|'        '
name|'env'
op|'.'
name|'update'
op|'('
name|'addl_env'
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmd'
op|','
name|'shell'
op|'='
name|'True'
op|','
name|'stdin'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'stderr'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
name|'env'
op|'='
name|'env'
op|')'
newline|'\n'
name|'result'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'process_input'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'        '
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
indent|'        '
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
newline|'\n'
name|'if'
name|'obj'
op|'.'
name|'returncode'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Result was %s"'
op|')'
op|'%'
op|'('
name|'obj'
op|'.'
name|'returncode'
op|')'
op|')'
newline|'\n'
name|'if'
name|'check_exit_code'
name|'and'
name|'obj'
op|'.'
name|'returncode'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'            '
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
name|'obj'
op|'.'
name|'returncode'
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
name|'cmd'
op|')'
newline|'\n'
comment|'# NOTE(termie): this appears to be necessary to let the subprocess call'
nl|'\n'
comment|'#               clean something up in between calls, without it two'
nl|'\n'
comment|'#               execute calls in a row hangs the second one'
nl|'\n'
dedent|''
dedent|''
name|'greenthread'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|abspath
dedent|''
name|'def'
name|'abspath'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
name|'s'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|novadir
dedent|''
name|'def'
name|'novadir'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'nova'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'nova'
op|'.'
name|'__file__'
op|')'
op|'.'
name|'split'
op|'('
string|"'nova/__init__.pyc'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|default_flagfile
dedent|''
name|'def'
name|'default_flagfile'
op|'('
name|'filename'
op|'='
string|"'nova.conf'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'arg'
name|'in'
name|'sys'
op|'.'
name|'argv'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'arg'
op|'.'
name|'find'
op|'('
string|"'flagfile'"
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isabs'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
comment|'# turn relative filename into an absolute path'
nl|'\n'
indent|'            '
name|'script_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'inspect'
op|'.'
name|'stack'
op|'('
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'script_dir'
op|','
name|'filename'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'flagfile'
op|'='
op|'['
string|"'--flagfile=%s'"
op|'%'
name|'filename'
op|']'
newline|'\n'
name|'sys'
op|'.'
name|'argv'
op|'='
name|'sys'
op|'.'
name|'argv'
op|'['
op|':'
number|'1'
op|']'
op|'+'
name|'flagfile'
op|'+'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|debug
dedent|''
dedent|''
dedent|''
name|'def'
name|'debug'
op|'('
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'debug in callback: %s'"
op|')'
op|','
name|'arg'
op|')'
newline|'\n'
name|'return'
name|'arg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|runthis
dedent|''
name|'def'
name|'runthis'
op|'('
name|'prompt'
op|','
name|'cmd'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Running %s"'
op|')'
op|','
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'rv'
op|','
name|'err'
op|'='
name|'execute'
op|'('
name|'cmd'
op|','
name|'check_exit_code'
op|'='
name|'check_exit_code'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_uid
dedent|''
name|'def'
name|'generate_uid'
op|'('
name|'topic'
op|','
name|'size'
op|'='
number|'8'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'characters'
op|'='
string|"'01234567890abcdefghijklmnopqrstuvwxyz'"
newline|'\n'
name|'choices'
op|'='
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
name|'characters'
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'size'
op|')'
op|']'
newline|'\n'
name|'return'
string|"'%s-%s'"
op|'%'
op|'('
name|'topic'
op|','
string|"''"
op|'.'
name|'join'
op|'('
name|'choices'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_mac
dedent|''
name|'def'
name|'generate_mac'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mac'
op|'='
op|'['
number|'0x02'
op|','
number|'0x16'
op|','
number|'0x3e'
op|','
nl|'\n'
name|'random'
op|'.'
name|'randint'
op|'('
number|'0x00'
op|','
number|'0x7f'
op|')'
op|','
nl|'\n'
name|'random'
op|'.'
name|'randint'
op|'('
number|'0x00'
op|','
number|'0xff'
op|')'
op|','
nl|'\n'
name|'random'
op|'.'
name|'randint'
op|'('
number|'0x00'
op|','
number|'0xff'
op|')'
op|']'
newline|'\n'
name|'return'
string|"':'"
op|'.'
name|'join'
op|'('
name|'map'
op|'('
name|'lambda'
name|'x'
op|':'
string|'"%02x"'
op|'%'
name|'x'
op|','
name|'mac'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|last_octet
dedent|''
name|'def'
name|'last_octet'
op|'('
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'int'
op|'('
name|'address'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utcnow
dedent|''
name|'def'
name|'utcnow'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Overridable version of datetime.datetime.utcnow."""'
newline|'\n'
name|'if'
name|'utcnow'
op|'.'
name|'override_time'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utcnow'
op|'.'
name|'override_time'
newline|'\n'
dedent|''
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utcnow_ts
name|'def'
name|'utcnow_ts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Timestamp version of our utcnow function."""'
newline|'\n'
name|'return'
name|'time'
op|'.'
name|'mktime'
op|'('
name|'utcnow'
op|'('
op|')'
op|'.'
name|'timetuple'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_time_override
dedent|''
name|'def'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Override utils.utcnow to return a constant time."""'
newline|'\n'
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'override_time'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|advance_time_delta
dedent|''
name|'def'
name|'advance_time_delta'
op|'('
name|'timedelta'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Advance overriden time using a datetime.timedelta."""'
newline|'\n'
name|'assert'
op|'('
name|'not'
name|'utcnow'
op|'.'
name|'override_time'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'utcnow'
op|'.'
name|'override_time'
op|'+='
name|'timedelta'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|advance_time_seconds
dedent|''
name|'def'
name|'advance_time_seconds'
op|'('
name|'seconds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Advance overriden time by seconds."""'
newline|'\n'
name|'advance_time_delta'
op|'('
name|'datetime'
op|'.'
name|'timedelta'
op|'('
number|'0'
op|','
name|'seconds'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|clear_time_override
dedent|''
name|'def'
name|'clear_time_override'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove the overridden time."""'
newline|'\n'
name|'utcnow'
op|'.'
name|'override_time'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|isotime
dedent|''
name|'def'
name|'isotime'
op|'('
name|'at'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns iso formatted utcnow."""'
newline|'\n'
name|'if'
name|'not'
name|'at'
op|':'
newline|'\n'
indent|'        '
name|'at'
op|'='
name|'utcnow'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'at'
op|'.'
name|'strftime'
op|'('
name|'TIME_FORMAT'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_isotime
dedent|''
name|'def'
name|'parse_isotime'
op|'('
name|'timestr'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Turn an iso formatted time back into a datetime"""'
newline|'\n'
name|'return'
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'timestr'
op|','
name|'TIME_FORMAT'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_mailmap
dedent|''
name|'def'
name|'parse_mailmap'
op|'('
name|'mailmap'
op|'='
string|"'.mailmap'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mapping'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'mailmap'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fp'
op|'='
name|'open'
op|'('
name|'mailmap'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'for'
name|'l'
name|'in'
name|'fp'
op|':'
newline|'\n'
indent|'            '
name|'l'
op|'='
name|'l'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'l'
op|'.'
name|'startswith'
op|'('
string|"'#'"
op|')'
name|'and'
string|"' '"
name|'in'
name|'l'
op|':'
newline|'\n'
indent|'                '
name|'canonical_email'
op|','
name|'alias'
op|'='
name|'l'
op|'.'
name|'split'
op|'('
string|"' '"
op|')'
newline|'\n'
name|'mapping'
op|'['
name|'alias'
op|']'
op|'='
name|'canonical_email'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'mapping'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|str_dict_replace
dedent|''
name|'def'
name|'str_dict_replace'
op|'('
name|'s'
op|','
name|'mapping'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'s1'
op|','
name|'s2'
name|'in'
name|'mapping'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'s'
op|'.'
name|'replace'
op|'('
name|'s1'
op|','
name|'s2'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'s'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LazyPluggable
dedent|''
name|'class'
name|'LazyPluggable'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A pluggable backend loaded lazily based on some value."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'pivot'
op|','
op|'**'
name|'backends'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__backends'
op|'='
name|'backends'
newline|'\n'
name|'self'
op|'.'
name|'__pivot'
op|'='
name|'pivot'
newline|'\n'
name|'self'
op|'.'
name|'__backend'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__get_backend
dedent|''
name|'def'
name|'__get_backend'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'__backend'
op|':'
newline|'\n'
indent|'            '
name|'backend_name'
op|'='
name|'self'
op|'.'
name|'__pivot'
op|'.'
name|'value'
newline|'\n'
name|'if'
name|'backend_name'
name|'not'
name|'in'
name|'self'
op|'.'
name|'__backends'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Invalid backend: %s'"
op|')'
op|'%'
name|'backend_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'backend'
op|'='
name|'self'
op|'.'
name|'__backends'
op|'['
name|'backend_name'
op|']'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'backend'
op|')'
op|'=='
name|'type'
op|'('
name|'tuple'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
name|'backend'
op|'['
number|'0'
op|']'
newline|'\n'
name|'fromlist'
op|'='
name|'backend'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'name'
op|'='
name|'backend'
newline|'\n'
name|'fromlist'
op|'='
name|'backend'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'__backend'
op|'='
name|'__import__'
op|'('
name|'name'
op|','
name|'None'
op|','
name|'None'
op|','
name|'fromlist'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'backend %s'"
op|')'
op|','
name|'self'
op|'.'
name|'__backend'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'__backend'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'backend'
op|'='
name|'self'
op|'.'
name|'__get_backend'
op|'('
op|')'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'backend'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoopingCall
dedent|''
dedent|''
name|'class'
name|'LoopingCall'
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
name|'f'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'args'
op|'='
name|'args'
newline|'\n'
name|'self'
op|'.'
name|'kw'
op|'='
name|'kw'
newline|'\n'
name|'self'
op|'.'
name|'f'
op|'='
name|'f'
newline|'\n'
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\n'
name|'done'
op|'='
name|'event'
op|'.'
name|'Event'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_inner
name|'def'
name|'_inner'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'now'
op|':'
newline|'\n'
indent|'                '
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'interval'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'while'
name|'self'
op|'.'
name|'_running'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'f'
op|'('
op|'*'
name|'self'
op|'.'
name|'args'
op|','
op|'**'
name|'self'
op|'.'
name|'kw'
op|')'
newline|'\n'
name|'greenthread'
op|'.'
name|'sleep'
op|'('
name|'interval'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'in looping call'"
op|')'
newline|'\n'
name|'done'
op|'.'
name|'send_exception'
op|'('
op|'*'
name|'sys'
op|'.'
name|'exc_info'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'done'
op|'.'
name|'send'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'done'
op|'='
name|'done'
newline|'\n'
nl|'\n'
name|'greenthread'
op|'.'
name|'spawn'
op|'('
name|'_inner'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'done'
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
name|'self'
op|'.'
name|'_running'
op|'='
name|'False'
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
name|'return'
name|'self'
op|'.'
name|'done'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|xhtml_escape
dedent|''
dedent|''
name|'def'
name|'xhtml_escape'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Escapes a string so it is valid within XML or XHTML.\n\n    Code is directly from the utf8 function in\n    http://github.com/facebook/tornado/blob/master/tornado/escape.py\n\n    """'
newline|'\n'
name|'return'
name|'saxutils'
op|'.'
name|'escape'
op|'('
name|'value'
op|','
op|'{'
string|'\'"\''
op|':'
string|'"&quot;"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utf8
dedent|''
name|'def'
name|'utf8'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Try to turn a string into utf-8 if possible.\n\n    Code is directly from the utf8 function in\n    http://github.com/facebook/tornado/blob/master/tornado/escape.py\n\n    """'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
op|'.'
name|'encode'
op|'('
string|'"utf-8"'
op|')'
newline|'\n'
dedent|''
name|'assert'
name|'isinstance'
op|'('
name|'value'
op|','
name|'str'
op|')'
newline|'\n'
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_primitive
dedent|''
name|'def'
name|'to_primitive'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'type'
op|'('
name|'value'
op|')'
name|'is'
name|'type'
op|'('
op|'['
op|']'
op|')'
name|'or'
name|'type'
op|'('
name|'value'
op|')'
name|'is'
name|'type'
op|'('
op|'('
name|'None'
op|','
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'o'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'value'
op|':'
newline|'\n'
indent|'            '
name|'o'
op|'.'
name|'append'
op|'('
name|'to_primitive'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'o'
newline|'\n'
dedent|''
name|'elif'
name|'type'
op|'('
name|'value'
op|')'
name|'is'
name|'type'
op|'('
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'o'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'value'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'o'
op|'['
name|'k'
op|']'
op|'='
name|'to_primitive'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'o'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'hasattr'
op|'('
name|'value'
op|','
string|"'iteritems'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'to_primitive'
op|'('
name|'dict'
op|'('
name|'value'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'hasattr'
op|'('
name|'value'
op|','
string|"'__iter__'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'to_primitive'
op|'('
name|'list'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dumps
dedent|''
dedent|''
name|'def'
name|'dumps'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'to_primitive'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|loads
dedent|''
name|'def'
name|'loads'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'s'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
