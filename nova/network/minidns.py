begin_unit
comment|'# Copyright 2011 Andrew Bogott for the Wikimedia Foundation'
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
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'dns_driver'
newline|'\n'
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
DECL|class|MiniDNS
name|'class'
name|'MiniDNS'
op|'('
name|'dns_driver'
op|'.'
name|'DNSDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Trivial DNS driver. This will read/write to a local, flat file\n    and have no effect on your actual DNS system. This class is\n    strictly for testing purposes, and should keep you out of dependency\n    hell.\n\n    Note that there is almost certainly a race condition here that\n    will manifest anytime instances are rapidly created and deleted.\n    A proper implementation will need some manner of locking.\n    """'
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
name|'if'
name|'CONF'
op|'.'
name|'log_dir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'log_dir'
op|','
string|'"dnstest.txt"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tempdir'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'tempdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filename'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|','
string|'"dnstest.txt"'
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|"'minidns file is |%s|'"
op|')'
op|','
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|'"w+"'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
string|'"#  minidns\\n\\n\\n"'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_domains
dedent|''
dedent|''
name|'def'
name|'get_domains'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entries'
op|'='
op|'['
op|']'
newline|'\n'
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
name|'entry'
name|'and'
name|'entry'
op|'['
string|"'address'"
op|']'
op|'=='
string|"'domain'"
op|':'
newline|'\n'
indent|'                '
name|'entries'
op|'.'
name|'append'
op|'('
name|'entry'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'entries'
newline|'\n'
nl|'\n'
DECL|member|qualify
dedent|''
name|'def'
name|'qualify'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'domain'
op|':'
newline|'\n'
indent|'            '
name|'qualified'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
name|'name'
op|','
name|'domain'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'qualified'
op|'='
name|'name'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'qualified'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_entry
dedent|''
name|'def'
name|'create_entry'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|','
name|'type'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'_'
op|'('
string|'"Invalid name"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'type'
op|'.'
name|'lower'
op|'('
op|')'
op|'!='
string|"'a'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'_'
op|'('
string|'"This driver only supports "'
nl|'\n'
string|'"type \'a\'"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'get_entries_by_name'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FloatingIpDNSExists'
op|'('
name|'name'
op|'='
name|'name'
op|','
name|'domain'
op|'='
name|'domain'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'outfile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'a+'"
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'write'
op|'('
string|'"%s   %s   %s\\n"'
op|'%'
nl|'\n'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|','
name|'type'
op|')'
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|parse_line
dedent|''
name|'def'
name|'parse_line'
op|'('
name|'self'
op|','
name|'line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vals'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'vals'
op|')'
op|'<'
number|'3'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'entry'
op|'['
string|"'address'"
op|']'
op|'='
name|'vals'
op|'['
number|'0'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'entry'
op|'['
string|"'name'"
op|']'
op|'='
name|'vals'
op|'['
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'entry'
op|'['
string|"'type'"
op|']'
op|'='
name|'vals'
op|'['
number|'2'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
name|'entry'
op|'['
string|"'address'"
op|']'
op|'=='
string|"'domain'"
op|':'
newline|'\n'
indent|'                '
name|'entry'
op|'['
string|"'domain'"
op|']'
op|'='
name|'entry'
op|'['
string|"'name'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'entry'
op|'['
string|"'domain'"
op|']'
op|'='
name|'entry'
op|'['
string|"'name'"
op|']'
op|'.'
name|'partition'
op|'('
string|"'.'"
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'entry'
newline|'\n'
nl|'\n'
DECL|member|delete_entry
dedent|''
dedent|''
name|'def'
name|'delete_entry'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'_'
op|'('
string|'"Invalid name"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'deleted'
op|'='
name|'False'
newline|'\n'
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'outfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
string|"'w'"
op|','
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
op|'('
op|'('
name|'not'
name|'entry'
op|')'
name|'or'
nl|'\n'
name|'entry'
op|'['
string|"'name'"
op|']'
op|'!='
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'outfile'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'deleted'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'move'
op|'('
name|'outfile'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'deleted'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Cannot delete entry |%s|'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
DECL|member|modify_address
dedent|''
dedent|''
name|'def'
name|'modify_address'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'get_entries_by_name'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'outfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
string|"'w'"
op|','
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'entry'
name|'and'
nl|'\n'
name|'entry'
op|'['
string|"'name'"
op|']'
op|'=='
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'outfile'
op|'.'
name|'write'
op|'('
string|'"%s   %s   %s\\n"'
op|'%'
nl|'\n'
op|'('
name|'address'
op|','
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|','
name|'entry'
op|'['
string|"'type'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'outfile'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'move'
op|'('
name|'outfile'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_address
dedent|''
name|'def'
name|'get_entries_by_address'
op|'('
name|'self'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entries'
op|'='
op|'['
op|']'
newline|'\n'
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
name|'entry'
name|'and'
name|'entry'
op|'['
string|"'address'"
op|']'
op|'=='
name|'address'
op|'.'
name|'lower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'entry'
op|'['
string|"'name'"
op|']'
op|'.'
name|'endswith'
op|'('
name|'domain'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'name'
op|'='
name|'entry'
op|'['
string|"'name'"
op|']'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
name|'name'
name|'not'
name|'in'
name|'entries'
op|':'
newline|'\n'
indent|'                        '
name|'entries'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'entries'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_name
dedent|''
name|'def'
name|'get_entries_by_name'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entries'
op|'='
op|'['
op|']'
newline|'\n'
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'entry'
name|'and'
nl|'\n'
name|'entry'
op|'['
string|"'name'"
op|']'
op|'=='
name|'self'
op|'.'
name|'qualify'
op|'('
name|'name'
op|','
name|'domain'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'entries'
op|'.'
name|'append'
op|'('
name|'entry'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'entries'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_file
dedent|''
name|'def'
name|'delete_dns_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'remove'
op|'('
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'tempdir'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|create_domain
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_domain'
op|'('
name|'self'
op|','
name|'fqdomain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'get_entries_by_name'
op|'('
name|'fqdomain'
op|','
string|"''"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FloatingIpDNSExists'
op|'('
name|'name'
op|'='
name|'fqdomain'
op|','
name|'domain'
op|'='
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'outfile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'a+'"
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'write'
op|'('
string|'"%s   %s   %s\\n"'
op|'%'
nl|'\n'
op|'('
string|"'domain'"
op|','
name|'fqdomain'
op|','
string|"'domain'"
op|')'
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_domain
dedent|''
name|'def'
name|'delete_domain'
op|'('
name|'self'
op|','
name|'fqdomain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deleted'
op|'='
name|'False'
newline|'\n'
name|'infile'
op|'='
name|'open'
op|'('
name|'self'
op|'.'
name|'filename'
op|','
string|"'r'"
op|')'
newline|'\n'
name|'outfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
string|"'w'"
op|','
name|'delete'
op|'='
name|'False'
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'infile'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'parse_line'
op|'('
name|'line'
op|')'
newline|'\n'
name|'if'
op|'('
op|'('
name|'not'
name|'entry'
op|')'
name|'or'
nl|'\n'
name|'entry'
op|'['
string|"'domain'"
op|']'
op|'!='
name|'fqdomain'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'outfile'
op|'.'
name|'write'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"deleted %s"'
op|')'
op|','
name|'entry'
op|')'
newline|'\n'
name|'deleted'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'infile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'outfile'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'shutil'
op|'.'
name|'move'
op|'('
name|'outfile'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'filename'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'deleted'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Cannot delete domain |%s|'"
op|')'
op|','
name|'fqdomain'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
