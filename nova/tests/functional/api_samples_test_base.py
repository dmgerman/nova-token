begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
name|'import'
name|'integrated_helpers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NoMatch
name|'class'
name|'NoMatch'
op|'('
name|'test'
op|'.'
name|'TestingException'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ApiSampleTestBase
dedent|''
name|'class'
name|'ApiSampleTestBase'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'json'"
newline|'\n'
DECL|variable|all_extensions
name|'all_extensions'
op|'='
name|'False'
newline|'\n'
DECL|variable|extension_name
name|'extension_name'
op|'='
name|'None'
newline|'\n'
DECL|variable|request_api_version
name|'request_api_version'
op|'='
name|'None'
newline|'\n'
DECL|variable|_use_common_server_api_samples
name|'_use_common_server_api_samples'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|_pretty_data
name|'def'
name|'_pretty_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
op|','
name|'sort_keys'
op|'='
name|'True'
op|','
nl|'\n'
name|'indent'
op|'='
number|'4'
op|')'
newline|'\n'
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'line'
op|'.'
name|'rstrip'
op|'('
op|')'
name|'for'
name|'line'
name|'in'
name|'data'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_objectify
dedent|''
name|'def'
name|'_objectify'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
comment|'# NOTE(vish): allow non-quoted replacements to survive json'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|'r\'([^"])%\\((.+)\\)s([^"])\''
op|','
string|'r\'\\1"%(int:\\2)s"\\3\''
op|','
name|'data'
op|')'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_sample_path
name|'def'
name|'_get_sample_path'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'dirname'
op|','
name|'suffix'
op|'='
string|"''"
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
op|'['
name|'dirname'
op|']'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
string|"'api_samples'"
op|')'
newline|'\n'
name|'if'
name|'cls'
op|'.'
name|'all_extensions'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'.'
name|'append'
op|'('
string|"'all_extensions'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cls'
op|'.'
name|'extension_name'
op|':'
newline|'\n'
indent|'            '
name|'alias'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'cls'
op|'.'
name|'extension_name'
op|')'
op|'.'
name|'alias'
newline|'\n'
name|'parts'
op|'.'
name|'append'
op|'('
name|'alias'
op|')'
newline|'\n'
dedent|''
name|'parts'
op|'.'
name|'append'
op|'('
name|'name'
op|'+'
string|'"."'
op|'+'
name|'cls'
op|'.'
name|'ctype'
op|'+'
name|'suffix'
op|')'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
op|'*'
name|'parts'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_sample
name|'def'
name|'_get_sample'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'api_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
newline|'\n'
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dirname'
op|','
string|'"../../../doc"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_get_sample_path'
op|'('
name|'name'
op|','
name|'dirname'
op|','
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_template
name|'def'
name|'_get_template'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'api_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
newline|'\n'
name|'return'
name|'cls'
op|'.'
name|'_get_sample_path'
op|'('
name|'name'
op|','
name|'dirname'
op|','
name|'suffix'
op|'='
string|"'.tpl'"
op|','
nl|'\n'
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_read_template
dedent|''
name|'def'
name|'_read_template'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'template'
op|'='
name|'self'
op|'.'
name|'_get_template'
op|'('
name|'name'
op|','
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'template'
op|')'
name|'as'
name|'inf'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'inf'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_write_template
dedent|''
dedent|''
name|'def'
name|'_write_template'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_get_template'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request_api_version'
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'outf'
op|':'
newline|'\n'
indent|'            '
name|'outf'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_write_sample
dedent|''
dedent|''
name|'def'
name|'_write_sample'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'_get_sample'
op|'('
nl|'\n'
name|'name'
op|','
name|'self'
op|'.'
name|'request_api_version'
op|')'
op|','
string|"'w'"
op|')'
name|'as'
name|'outf'
op|':'
newline|'\n'
indent|'            '
name|'outf'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_compare_result
dedent|''
dedent|''
name|'def'
name|'_compare_result'
op|'('
name|'self'
op|','
name|'subs'
op|','
name|'expected'
op|','
name|'result'
op|','
name|'result_str'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'matched_value'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'expected'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'result'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
string|"'%(result_str)s: %(result)s is not a dict.'"
nl|'\n'
op|'%'
op|'{'
string|"'result_str'"
op|':'
name|'result_str'
op|','
string|"'result'"
op|':'
name|'result'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'ex_keys'
op|'='
name|'sorted'
op|'('
name|'expected'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_keys'
op|'='
name|'sorted'
op|'('
name|'result'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'ex_keys'
op|'!='
name|'res_keys'
op|':'
newline|'\n'
indent|'                '
name|'ex_delta'
op|'='
op|'['
op|']'
newline|'\n'
name|'res_delta'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'ex_keys'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'key'
name|'not'
name|'in'
name|'res_keys'
op|':'
newline|'\n'
indent|'                        '
name|'ex_delta'
op|'.'
name|'append'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'key'
name|'in'
name|'res_keys'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'key'
name|'not'
name|'in'
name|'ex_keys'
op|':'
newline|'\n'
indent|'                        '
name|'res_delta'
op|'.'
name|'append'
op|'('
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'NoMatch'
op|'('
nl|'\n'
string|"'Dictionary key mismatch:\\n'"
nl|'\n'
string|"'Extra key(s) in template:\\n%(ex_delta)s\\n'"
nl|'\n'
string|"'Extra key(s) in %(result_str)s:\\n%(res_delta)s\\n'"
op|'%'
nl|'\n'
op|'{'
string|"'ex_delta'"
op|':'
name|'ex_delta'
op|','
string|"'result_str'"
op|':'
name|'result_str'
op|','
nl|'\n'
string|"'res_delta'"
op|':'
name|'res_delta'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'ex_keys'
op|':'
newline|'\n'
indent|'                '
name|'res'
op|'='
name|'self'
op|'.'
name|'_compare_result'
op|'('
name|'subs'
op|','
name|'expected'
op|'['
name|'key'
op|']'
op|','
name|'result'
op|'['
name|'key'
op|']'
op|','
nl|'\n'
name|'result_str'
op|')'
newline|'\n'
name|'matched_value'
op|'='
name|'res'
name|'or'
name|'matched_value'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'expected'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'result'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
nl|'\n'
string|"'%(result_str)s: %(result)s is not a list.'"
op|'%'
nl|'\n'
op|'{'
string|"'result_str'"
op|':'
name|'result_str'
op|','
string|"'result'"
op|':'
name|'result'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'expected'
op|'='
name|'expected'
op|'['
op|':'
op|']'
newline|'\n'
name|'extra'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'res_obj'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'i'
op|','
name|'ex_obj'
name|'in'
name|'enumerate'
op|'('
name|'expected'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'try'
op|':'
newline|'\n'
indent|'                        '
name|'matched_value'
op|'='
name|'self'
op|'.'
name|'_compare_result'
op|'('
name|'subs'
op|','
name|'ex_obj'
op|','
nl|'\n'
name|'res_obj'
op|','
nl|'\n'
name|'result_str'
op|')'
newline|'\n'
name|'del'
name|'expected'
op|'['
name|'i'
op|']'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'except'
name|'NoMatch'
op|':'
newline|'\n'
indent|'                        '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'extra'
op|'.'
name|'append'
op|'('
name|'res_obj'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'error'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'expected'
op|':'
newline|'\n'
indent|'                '
name|'error'
op|'.'
name|'append'
op|'('
string|"'Extra list items in template:'"
op|')'
newline|'\n'
name|'error'
op|'.'
name|'extend'
op|'('
op|'['
name|'repr'
op|'('
name|'o'
op|')'
name|'for'
name|'o'
name|'in'
name|'expected'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'extra'
op|':'
newline|'\n'
indent|'                '
name|'error'
op|'.'
name|'append'
op|'('
string|"'Extra list items in %(result_str)s:'"
op|'%'
nl|'\n'
op|'{'
string|"'result_str'"
op|':'
name|'result_str'
op|'}'
op|')'
newline|'\n'
name|'error'
op|'.'
name|'extend'
op|'('
op|'['
name|'repr'
op|'('
name|'o'
op|')'
name|'for'
name|'o'
name|'in'
name|'extra'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'error'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'error'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'expected'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
name|'and'
string|"'%'"
name|'in'
name|'expected'
op|':'
newline|'\n'
comment|'# NOTE(vish): escape stuff for regex'
nl|'\n'
indent|'            '
name|'for'
name|'char'
name|'in'
string|"'[]<>?'"
op|':'
newline|'\n'
indent|'                '
name|'expected'
op|'='
name|'expected'
op|'.'
name|'replace'
op|'('
name|'char'
op|','
string|"'\\\\%s'"
op|'%'
name|'char'
op|')'
newline|'\n'
comment|'# NOTE(vish): special handling of subs that are not quoted. We are'
nl|'\n'
comment|'#             expecting an int but we had to pass in a string'
nl|'\n'
comment|'#             so the json would parse properly.'
nl|'\n'
dedent|''
name|'if'
name|'expected'
op|'.'
name|'startswith'
op|'('
string|'"%(int:"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'str'
op|'('
name|'result'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'expected'
op|'.'
name|'replace'
op|'('
string|"'int:'"
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'expected'
op|'='
name|'expected'
op|'%'
name|'subs'
newline|'\n'
name|'expected'
op|'='
string|"'^%s$'"
op|'%'
name|'expected'
newline|'\n'
name|'match'
op|'='
name|'re'
op|'.'
name|'match'
op|'('
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
nl|'\n'
string|"'Values do not match:\\n'"
nl|'\n'
string|"'Template: %(expected)s\\n%(result_str)s: %(result)s'"
op|'%'
nl|'\n'
op|'{'
string|"'expected'"
op|':'
name|'expected'
op|','
string|"'result_str'"
op|':'
name|'result_str'
op|','
nl|'\n'
string|"'result'"
op|':'
name|'result'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'matched_value'
op|'='
name|'match'
op|'.'
name|'group'
op|'('
string|"'id'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'matched_value'
op|'='
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'expected'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(danms): Ignore whitespace in this comparison'
nl|'\n'
indent|'                '
name|'expected'
op|'='
name|'expected'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'result'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'='
name|'result'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'expected'
op|'!='
name|'result'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
nl|'\n'
string|"'Values do not match:\\n'"
nl|'\n'
string|"'Template: %(expected)s\\n%(result_str)s: '"
nl|'\n'
string|"'%(result)s'"
op|'%'
op|'{'
string|"'expected'"
op|':'
name|'expected'
op|','
nl|'\n'
string|"'result_str'"
op|':'
name|'result_str'
op|','
nl|'\n'
string|"'result'"
op|':'
name|'result'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'matched_value'
newline|'\n'
nl|'\n'
DECL|member|generalize_subs
dedent|''
name|'def'
name|'generalize_subs'
op|'('
name|'self'
op|','
name|'subs'
op|','
name|'vanilla_regexes'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Give the test a chance to modify subs after the server response\n        was verified, and before the on-disk doc/api_samples file is checked.\n        This may be needed by some tests to convert exact matches expected\n        from the server into pattern matches to verify what is in the\n        sample file.\n\n        If there are no changes to be made, subs is returned unharmed.\n        """'
newline|'\n'
name|'return'
name|'subs'
newline|'\n'
nl|'\n'
DECL|member|_verify_response
dedent|''
name|'def'
name|'_verify_response'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'subs'
op|','
name|'response'
op|','
name|'exp_code'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
name|'exp_code'
op|')'
newline|'\n'
name|'response_data'
op|'='
name|'response'
op|'.'
name|'content'
newline|'\n'
name|'response_data'
op|'='
name|'self'
op|'.'
name|'_pretty_data'
op|'('
name|'response_data'
op|')'
newline|'\n'
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
name|'_get_template'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request_api_version'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_write_template'
op|'('
name|'name'
op|','
name|'response_data'
op|')'
newline|'\n'
name|'template_data'
op|'='
name|'response_data'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'template_data'
op|'='
name|'self'
op|'.'
name|'_read_template'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'self'
op|'.'
name|'generate_samples'
name|'and'
nl|'\n'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'_get_sample'
op|'('
nl|'\n'
name|'name'
op|','
name|'self'
op|'.'
name|'request_api_version'
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_write_sample'
op|'('
name|'name'
op|','
name|'response_data'
op|')'
newline|'\n'
name|'sample_data'
op|'='
name|'response_data'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'file'
op|'('
name|'self'
op|'.'
name|'_get_sample'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'request_api_version'
op|')'
op|')'
name|'as'
name|'sample'
op|':'
newline|'\n'
indent|'                '
name|'sample_data'
op|'='
name|'sample'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'template_data'
op|'='
name|'self'
op|'.'
name|'_objectify'
op|'('
name|'template_data'
op|')'
newline|'\n'
name|'response_data'
op|'='
name|'self'
op|'.'
name|'_objectify'
op|'('
name|'response_data'
op|')'
newline|'\n'
name|'response_result'
op|'='
name|'self'
op|'.'
name|'_compare_result'
op|'('
name|'subs'
op|','
name|'template_data'
op|','
nl|'\n'
name|'response_data'
op|','
string|'"Response"'
op|')'
newline|'\n'
comment|'# NOTE(danms): replace some of the subs with patterns for the'
nl|'\n'
comment|"# doc/api_samples check, which won't have things like the"
nl|'\n'
comment|'# correct compute host name. Also let the test do some of its'
nl|'\n'
comment|'# own generalization, if necessary'
nl|'\n'
name|'vanilla_regexes'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'compute_host'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'host_name'"
op|']'
newline|'\n'
name|'subs'
op|'['
string|"'id'"
op|']'
op|'='
name|'vanilla_regexes'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'generalize_subs'
op|'('
name|'subs'
op|','
name|'vanilla_regexes'
op|')'
newline|'\n'
name|'sample_data'
op|'='
name|'self'
op|'.'
name|'_objectify'
op|'('
name|'sample_data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_compare_result'
op|'('
name|'subs'
op|','
name|'template_data'
op|','
name|'sample_data'
op|','
string|'"Sample"'
op|')'
newline|'\n'
name|'return'
name|'response_result'
newline|'\n'
dedent|''
name|'except'
name|'NoMatch'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_get_host
dedent|''
dedent|''
name|'def'
name|'_get_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'http://openstack.example.com'"
newline|'\n'
nl|'\n'
DECL|member|_get_glance_host
dedent|''
name|'def'
name|'_get_glance_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'http://glance.openstack.example.com'"
newline|'\n'
nl|'\n'
DECL|member|_get_regexes
dedent|''
name|'def'
name|'_get_regexes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'ctype'
op|'=='
string|"'json'"
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
string|'r\'(\\\\"|[^"])*\''
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
string|"r'[^<]*'"
newline|'\n'
dedent|''
name|'isotime_re'
op|'='
string|"'\\d{4}-[0,1]\\d-[0-3]\\dT\\d{2}:\\d{2}:\\d{2}Z'"
newline|'\n'
name|'strtime_re'
op|'='
string|"'\\d{4}-[0,1]\\d-[0-3]\\dT\\d{2}:\\d{2}:\\d{2}\\.\\d{6}'"
newline|'\n'
name|'xmltime_re'
op|'='
op|'('
string|"'\\d{4}-[0,1]\\d-[0-3]\\d '"
nl|'\n'
string|"'\\d{2}:\\d{2}:\\d{2}'"
nl|'\n'
string|"'(\\.\\d{6})?(\\+00:00)?'"
op|')'
newline|'\n'
name|'return'
op|'{'
nl|'\n'
string|"'isotime'"
op|':'
name|'isotime_re'
op|','
nl|'\n'
string|"'strtime'"
op|':'
name|'strtime_re'
op|','
nl|'\n'
string|"'strtime_or_none'"
op|':'
string|"r'None|%s'"
op|'%'
name|'strtime_re'
op|','
nl|'\n'
string|"'xmltime'"
op|':'
name|'xmltime_re'
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'[0-9a-zA-Z]{1,12}'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'"
op|','
nl|'\n'
string|"'ip6'"
op|':'
string|"'([0-9a-zA-Z]{1,4}:){1,7}:?[0-9a-zA-Z]{1,4}'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'(?P<id>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}'"
nl|'\n'
string|"'-[0-9a-f]{4}-[0-9a-f]{12})'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}'"
nl|'\n'
string|"'-[0-9a-f]{4}-[0-9a-f]{12}'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
string|"'r-[0-9a-zA-Z]{8}'"
op|','
nl|'\n'
string|"'private_key'"
op|':'
string|"'-----BEGIN RSA PRIVATE KEY-----'"
nl|'\n'
string|"'[a-zA-Z0-9\\n/+=]*'"
nl|'\n'
string|"'-----END RSA PRIVATE KEY-----'"
op|','
nl|'\n'
string|"'public_key'"
op|':'
string|"'ssh-rsa[ a-zA-Z0-9/+=]*'"
nl|'\n'
string|"'Generated-by-Nova'"
op|','
nl|'\n'
string|"'fingerprint'"
op|':'
string|"'([0-9a-f]{2}:){15}[0-9a-f]{2}'"
op|','
nl|'\n'
string|"'keypair_type'"
op|':'
string|"'ssh|x509'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'host_name'"
op|':'
string|"'[0-9a-z]{32}'"
op|','
nl|'\n'
string|"'glance_host'"
op|':'
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|','
nl|'\n'
string|"'compute_host'"
op|':'
name|'self'
op|'.'
name|'compute'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'text'"
op|':'
name|'text'
op|','
nl|'\n'
string|"'int'"
op|':'
string|"'[0-9]+'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_response
dedent|''
name|'def'
name|'_get_response'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'method'
op|','
name|'body'
op|'='
name|'None'
op|','
name|'strip_version'
op|'='
name|'False'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/'"
op|'+'
name|'self'
op|'.'
name|'ctype'
newline|'\n'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/'"
op|'+'
name|'self'
op|'.'
name|'ctype'
newline|'\n'
name|'if'
name|'api_version'
op|':'
newline|'\n'
indent|'            '
name|'headers'
op|'['
string|"'X-OpenStack-Nova-API-Version'"
op|']'
op|'='
name|'api_version'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'api'
op|'.'
name|'api_request'
op|'('
name|'url'
op|','
name|'body'
op|'='
name|'body'
op|','
name|'method'
op|'='
name|'method'
op|','
nl|'\n'
name|'headers'
op|'='
name|'headers'
op|','
name|'strip_version'
op|'='
name|'strip_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_get
dedent|''
name|'def'
name|'_do_get'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'strip_version'
op|'='
name|'False'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_response'
op|'('
name|'url'
op|','
string|"'GET'"
op|','
name|'strip_version'
op|'='
name|'strip_version'
op|','
nl|'\n'
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_post
dedent|''
name|'def'
name|'_do_post'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'name'
op|','
name|'subs'
op|','
name|'method'
op|'='
string|"'POST'"
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'self'
op|'.'
name|'_read_template'
op|'('
name|'name'
op|')'
op|'%'
name|'subs'
newline|'\n'
name|'sample'
op|'='
name|'self'
op|'.'
name|'_get_sample'
op|'('
name|'name'
op|','
name|'self'
op|'.'
name|'request_api_version'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'generate_samples'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'sample'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_write_sample'
op|'('
name|'name'
op|','
name|'body'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_get_response'
op|'('
name|'url'
op|','
name|'method'
op|','
name|'body'
op|','
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_put
dedent|''
name|'def'
name|'_do_put'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'name'
op|','
name|'subs'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_do_post'
op|'('
name|'url'
op|','
name|'name'
op|','
name|'subs'
op|','
name|'method'
op|'='
string|"'PUT'"
op|','
nl|'\n'
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_do_delete
dedent|''
name|'def'
name|'_do_delete'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'api_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_get_response'
op|'('
name|'url'
op|','
string|"'DELETE'"
op|','
name|'api_version'
op|'='
name|'api_version'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
