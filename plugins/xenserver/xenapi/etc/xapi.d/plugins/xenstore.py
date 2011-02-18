begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
comment|'#'
nl|'\n'
comment|'# XenAPI plugin for reading/writing information to xenstore'
nl|'\n'
comment|'#'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'json'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
dedent|''
name|'import'
name|'subprocess'
newline|'\n'
nl|'\n'
name|'import'
name|'XenAPIPlugin'
newline|'\n'
nl|'\n'
name|'import'
name|'pluginlib_nova'
name|'as'
name|'pluginlib'
newline|'\n'
name|'pluginlib'
op|'.'
name|'configure_logging'
op|'('
string|'"xenstore"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|jsonify
name|'def'
name|'jsonify'
op|'('
name|'fnc'
op|')'
op|':'
newline|'\n'
DECL|function|wrapper
indent|'    '
name|'def'
name|'wrapper'
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
name|'ret'
op|'='
name|'fnc'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'json'
op|'.'
name|'loads'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'# Value should already be JSON-encoded, but some operations'
nl|'\n'
comment|'# may write raw sting values; this will catch those and'
nl|'\n'
comment|'# properly encode them.'
nl|'\n'
indent|'            '
name|'ret'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'ret'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
dedent|''
name|'return'
name|'wrapper'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|read_record
name|'def'
name|'read_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the value stored at the given path for the given dom_id.\n    These must be encoded as key/value pairs in arg_dict. You can\n    optinally include a key \'ignore_missing_path\'; if this is present\n    and boolean True, attempting to read a non-existent path will return\n    the string \'None\' instead of raising an exception.\n    """'
newline|'\n'
name|'cmd'
op|'='
string|'"xenstore-read /local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|'.'
name|'rstrip'
op|'('
string|'"\\n"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'pluginlib'
op|'.'
name|'PluginError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'arg_dict'
op|'.'
name|'get'
op|'('
string|'"ignore_missing_path"'
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'='
string|'"xenstore-exists /local/domain/%(dom_id)s/%(path)s; echo $?"'
newline|'\n'
name|'cmd'
op|'='
name|'cmd'
op|'%'
name|'arg_dict'
newline|'\n'
name|'ret'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
comment|'# If the path exists, the cmd should return "0"'
nl|'\n'
name|'if'
name|'ret'
op|'!='
string|'"0"'
op|':'
newline|'\n'
comment|'# No such path, so ignore the error and return the'
nl|'\n'
comment|"# string 'None', since None can't be marshalled"
nl|'\n'
comment|'# over RPC.'
nl|'\n'
indent|'                '
name|'return'
string|'"None"'
newline|'\n'
comment|"# Either we shouldn't ignore path errors, or another"
nl|'\n'
comment|'# error was hit. Re-raise.'
nl|'\n'
dedent|''
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|write_record
name|'def'
name|'write_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Writes to xenstore at the specified path. If there is information\n    already stored in that location, it is overwritten. As in read_record,\n    the dom_id and path must be specified in the arg_dict; additionally,\n    you must specify a \'value\' key, whose value must be a string. Typically,\n    you can json-ify more complex values and store the json output.\n    """'
newline|'\n'
name|'cmd'
op|'='
string|'"xenstore-write /local/domain/%(dom_id)s/%(path)s \'%(value)s\'"'
newline|'\n'
name|'cmd'
op|'='
name|'cmd'
op|'%'
name|'arg_dict'
newline|'\n'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'arg_dict'
op|'['
string|'"value"'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|list_records
name|'def'
name|'list_records'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns all the stored data at or below the given path for the\n    given dom_id. The data is returned as a json-ified dict, with the\n    path as the key and the stored value as the value. If the path\n    doesn\'t exist, an empty dict is returned.\n    """'
newline|'\n'
name|'cmd'
op|'='
string|'"xenstore-ls /local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
newline|'\n'
name|'cmd'
op|'='
name|'cmd'
op|'.'
name|'rstrip'
op|'('
string|'"/"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'recs'
op|'='
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'pluginlib'
op|'.'
name|'PluginError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|'"No such file or directory"'
name|'in'
string|'"%s"'
op|'%'
name|'e'
op|':'
newline|'\n'
comment|"# Path doesn't exist."
nl|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'return'
name|'str'
op|'('
name|'e'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
dedent|''
name|'base_path'
op|'='
name|'arg_dict'
op|'['
string|'"path"'
op|']'
newline|'\n'
name|'paths'
op|'='
name|'_paths_from_ls'
op|'('
name|'recs'
op|')'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'path'
name|'in'
name|'paths'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'base_path'
op|':'
newline|'\n'
indent|'            '
name|'arg_dict'
op|'['
string|'"path"'
op|']'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'base_path'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'arg_dict'
op|'['
string|'"path"'
op|']'
op|'='
name|'path'
newline|'\n'
dedent|''
name|'rec'
op|'='
name|'read_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'rec'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'rec'
newline|'\n'
dedent|''
name|'ret'
op|'['
name|'path'
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonify'
newline|'\n'
DECL|function|delete_record
name|'def'
name|'delete_record'
op|'('
name|'self'
op|','
name|'arg_dict'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Just like it sounds: it removes the record for the specified\n    VM and the specified path from xenstore.\n    """'
newline|'\n'
name|'cmd'
op|'='
string|'"xenstore-rm /local/domain/%(dom_id)s/%(path)s"'
op|'%'
name|'arg_dict'
newline|'\n'
name|'return'
name|'_run_command'
op|'('
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_paths_from_ls
dedent|''
name|'def'
name|'_paths_from_ls'
op|'('
name|'recs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The xenstore-ls command returns a listing that isn\'t terribly\n    useful. This method cleans that up into a dict with each path\n    as the key, and the associated string as the value.\n    """'
newline|'\n'
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'last_nm'
op|'='
string|'""'
newline|'\n'
name|'level'
op|'='
number|'0'
newline|'\n'
name|'path'
op|'='
op|'['
op|']'
newline|'\n'
name|'ret'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'ln'
name|'in'
name|'recs'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nm'
op|','
name|'val'
op|'='
name|'ln'
op|'.'
name|'rstrip'
op|'('
op|')'
op|'.'
name|'split'
op|'('
string|'" = "'
op|')'
newline|'\n'
name|'barename'
op|'='
name|'nm'
op|'.'
name|'lstrip'
op|'('
op|')'
newline|'\n'
name|'this_level'
op|'='
name|'len'
op|'('
name|'nm'
op|')'
op|'-'
name|'len'
op|'('
name|'barename'
op|')'
newline|'\n'
name|'if'
name|'this_level'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'.'
name|'append'
op|'('
name|'barename'
op|')'
newline|'\n'
name|'level'
op|'='
number|'0'
newline|'\n'
name|'path'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'=='
name|'level'
op|':'
newline|'\n'
comment|'# child of same parent'
nl|'\n'
indent|'            '
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'>'
name|'level'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'.'
name|'append'
op|'('
name|'last_nm'
op|')'
newline|'\n'
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
name|'level'
op|'='
name|'this_level'
newline|'\n'
dedent|''
name|'elif'
name|'this_level'
op|'<'
name|'level'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'path'
op|'['
op|':'
name|'this_level'
op|']'
newline|'\n'
name|'ret'
op|'.'
name|'append'
op|'('
string|'"%s/%s"'
op|'%'
op|'('
string|'"/"'
op|'.'
name|'join'
op|'('
name|'path'
op|')'
op|','
name|'barename'
op|')'
op|')'
newline|'\n'
name|'level'
op|'='
name|'this_level'
newline|'\n'
dedent|''
name|'last_nm'
op|'='
name|'barename'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_run_command
dedent|''
name|'def'
name|'_run_command'
op|'('
name|'cmd'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts out the basics of issuing system commands. If the command\n    returns anything in stderr, a PluginError is raised with that information.\n    Otherwise, the output from stdout is returned.\n    """'
newline|'\n'
name|'pipe'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
newline|'\n'
name|'proc'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
op|'['
name|'cmd'
op|']'
op|','
name|'shell'
op|'='
name|'True'
op|','
name|'stdin'
op|'='
name|'pipe'
op|','
name|'stdout'
op|'='
name|'pipe'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'pipe'
op|','
name|'close_fds'
op|'='
name|'True'
op|')'
newline|'\n'
name|'proc'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'err'
op|'='
name|'proc'
op|'.'
name|'stderr'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'pluginlib'
op|'.'
name|'PluginError'
op|'('
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'proc'
op|'.'
name|'stdout'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'XenAPIPlugin'
op|'.'
name|'dispatch'
op|'('
nl|'\n'
op|'{'
string|'"read_record"'
op|':'
name|'read_record'
op|','
nl|'\n'
string|'"write_record"'
op|':'
name|'write_record'
op|','
nl|'\n'
string|'"list_records"'
op|':'
name|'list_records'
op|','
nl|'\n'
string|'"delete_record"'
op|':'
name|'delete_record'
op|'}'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
