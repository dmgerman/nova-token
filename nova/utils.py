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
name|'logging'
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
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
op|'.'
name|'threads'
name|'import'
name|'deferToThread'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
string|"'Class %s cannot be found'"
op|'%'
name|'class_str'
op|')'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Fetching %s"'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Result was %s"'
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
op|'<>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Unexpected exit code: %s.  result=%s"'
nl|'\n'
op|'%'
op|'('
name|'obj'
op|'.'
name|'returncode'
op|','
name|'result'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
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
op|'['
string|"'--flagfile=%s'"
op|'%'
name|'filename'
op|']'
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'debug in callback: %s'"
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
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Running %s"'
op|'%'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'exit_code'
op|'='
name|'subprocess'
op|'.'
name|'call'
op|'('
name|'cmd'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'prompt'
op|'%'
op|'('
name|'exit_code'
op|')'
op|')'
newline|'\n'
name|'if'
name|'check_exit_code'
name|'and'
name|'exit_code'
op|'<>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"Unexpected exit code: %s from cmd: %s"'
nl|'\n'
op|'%'
op|'('
name|'exit_code'
op|','
name|'cmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_uid
dedent|''
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
op|'['
name|'random'
op|'.'
name|'choice'
op|'('
string|"'01234567890abcdefghijklmnopqrstuvwxyz'"
op|')'
name|'for'
name|'x'
name|'in'
name|'xrange'
op|'('
name|'size'
op|')'
op|']'
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
name|'random'
op|'.'
name|'randint'
op|'('
number|'0x00'
op|','
number|'0xff'
op|')'
nl|'\n'
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
DECL|function|get_my_ip
dedent|''
name|'def'
name|'get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|"''' returns the actual ip of the local machine.\n    '''"
newline|'\n'
name|'if'
name|'getattr'
op|'('
name|'FLAGS'
op|','
string|"'fake_tests'"
op|','
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'127.0.0.1'"
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
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
name|'SOCK_STREAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'www.google.com'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'gaierror'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
string|'"Couldn\'t get IP, using 127.0.0.1 %s"'
op|','
name|'ex'
op|')'
newline|'\n'
name|'return'
string|'"127.0.0.1"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|isotime
dedent|''
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
name|'if'
name|'not'
name|'at'
op|':'
newline|'\n'
indent|'        '
name|'at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
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
DECL|function|deferredToThread
dedent|''
name|'def'
name|'deferredToThread'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
DECL|function|g
indent|'    '
name|'def'
name|'g'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'deferToThread'
op|'('
name|'f'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'g'
newline|'\n'
dedent|''
endmarker|''
end_unit
