begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# Copyright 2012 Nebula, Inc.'
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
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_network'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
name|'import'
name|'integrated_helpers'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
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
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_ipv6'
op|'='
name|'False'
op|','
nl|'\n'
name|'osapi_compute_link_prefix'
op|'='
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
op|','
nl|'\n'
name|'osapi_glance_link_prefix'
op|'='
name|'self'
op|'.'
name|'_get_glance_host'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'all_extensions'
op|':'
newline|'\n'
indent|'            '
name|'ext'
op|'='
op|'['
name|'self'
op|'.'
name|'extension_name'
op|']'
name|'if'
name|'self'
op|'.'
name|'extension_name'
name|'else'
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'osapi_compute_extension'
op|'='
name|'ext'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'ApiSampleTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'fake_network'
op|'.'
name|'stub_compute_with_ips'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'generate_samples'
op|'='
name|'os'
op|'.'
name|'getenv'
op|'('
string|"'GENERATE_SAMPLES'"
op|')'
name|'is'
name|'not'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_pretty_data
dedent|''
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
name|'if'
name|'self'
op|'.'
name|'ctype'
op|'=='
string|"'json'"
op|':'
newline|'\n'
indent|'            '
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
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'xml'
op|'='
name|'etree'
op|'.'
name|'XML'
op|'('
name|'data'
op|')'
newline|'\n'
name|'data'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'xml'
op|','
name|'encoding'
op|'='
string|'"UTF-8"'
op|','
nl|'\n'
name|'xml_declaration'
op|'='
name|'True'
op|','
name|'pretty_print'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
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
dedent|''
name|'if'
name|'self'
op|'.'
name|'ctype'
op|'=='
string|"'json'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|function|to_dict
indent|'            '
name|'def'
name|'to_dict'
op|'('
name|'node'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ret'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'node'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'ret'
op|'.'
name|'update'
op|'('
name|'dict'
op|'('
name|'node'
op|'.'
name|'items'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'node'
op|'.'
name|'text'
op|':'
newline|'\n'
indent|'                    '
name|'ret'
op|'['
string|"'__content__'"
op|']'
op|'='
name|'node'
op|'.'
name|'text'
newline|'\n'
dedent|''
name|'if'
name|'node'
op|'.'
name|'tag'
op|':'
newline|'\n'
indent|'                    '
name|'ret'
op|'['
string|"'__tag__'"
op|']'
op|'='
name|'node'
op|'.'
name|'tag'
newline|'\n'
dedent|''
name|'if'
name|'node'
op|'.'
name|'nsmap'
op|':'
newline|'\n'
indent|'                    '
name|'ret'
op|'['
string|"'__nsmap__'"
op|']'
op|'='
name|'node'
op|'.'
name|'nsmap'
newline|'\n'
dedent|''
name|'for'
name|'element'
name|'in'
name|'node'
op|':'
newline|'\n'
indent|'                    '
name|'ret'
op|'.'
name|'setdefault'
op|'('
name|'node'
op|'.'
name|'tag'
op|','
op|'['
op|']'
op|')'
newline|'\n'
name|'ret'
op|'['
name|'node'
op|'.'
name|'tag'
op|']'
op|'.'
name|'append'
op|'('
name|'to_dict'
op|'('
name|'element'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
dedent|''
name|'return'
name|'to_dict'
op|'('
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'join'
op|'('
name|'dirname'
op|','
string|'"../../../doc"'
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
name|'template'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'open'
op|'('
name|'template'
op|','
string|"'w'"
op|')'
name|'as'
name|'outf'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
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
name|'name'
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
nl|'\n'
name|'_'
op|'('
string|"'Result: %(result)s is not a dict.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'raise'
name|'NoMatch'
op|'('
name|'_'
op|'('
string|"'Key mismatch:\\n'"
nl|'\n'
string|"'%(ex_keys)s\\n%(res_keys)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
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
name|'_'
op|'('
string|"'Result: %(result)s is not a list.'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'ex_obj'
op|','
name|'res_obj'
name|'in'
name|'zip'
op|'('
name|'sorted'
op|'('
name|'expected'
op|')'
op|','
name|'sorted'
op|'('
name|'result'
op|')'
op|')'
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
name|'ex_obj'
op|','
name|'res_obj'
op|')'
newline|'\n'
name|'matched_value'
op|'='
name|'res'
name|'or'
name|'matched_value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'expected'
op|','
name|'basestring'
op|')'
name|'and'
string|"'%'"
name|'in'
name|'expected'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
comment|'# NOTE(vish): escape stuff for regex'
nl|'\n'
indent|'                '
name|'for'
name|'char'
name|'in'
op|'['
string|"'['"
op|','
string|"']'"
op|','
string|"'<'"
op|','
string|"'>'"
op|','
string|"'?'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'expected'
op|'='
name|'expected'
op|'.'
name|'replace'
op|'('
name|'char'
op|','
string|"'\\%s'"
op|'%'
name|'char'
op|')'
newline|'\n'
dedent|''
name|'expected'
op|'='
name|'expected'
op|'%'
name|'subs'
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
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
name|'_'
op|'('
string|"'Values do not match:\\n'"
nl|'\n'
string|"'%(expected)s\\n%(result)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'match'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'NoMatch'
op|'('
name|'_'
op|'('
string|"'Values do not match:\\n'"
nl|'\n'
string|"'%(expected)s\\n%(result)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
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
name|'else'
op|':'
newline|'\n'
indent|'            '
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
name|'_'
op|'('
string|"'Values do not match:\\n'"
nl|'\n'
string|"'%(expected)s\\n%(result)s'"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'matched_value'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
name|'self'
op|'.'
name|'_read_template'
op|'('
name|'name'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'self'
op|'.'
name|'_objectify'
op|'('
name|'expected'
op|')'
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'_pretty_data'
op|'('
name|'response'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'generate_samples'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_write_sample'
op|'('
name|'name'
op|','
name|'result'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'_objectify'
op|'('
name|'result'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_compare_result'
op|'('
name|'subs'
op|','
name|'expected'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_host
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
name|'return'
op|'{'
nl|'\n'
string|"'timestamp'"
op|':'
string|"'[0-9]{4}-[0,1][0-9]-[0-3][0-9]T'"
nl|'\n'
string|"'[0-9]{2}:[0-9]{2}:[0-9]{2}'"
nl|'\n'
string|"'(Z|(\\+|-)[0-9]{2}:[0-9]{2})'"
op|','
nl|'\n'
string|"'password'"
op|':'
string|"'[0-9a-zA-Z]{12}'"
op|','
nl|'\n'
string|"'ip'"
op|':'
string|"'[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}'"
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
string|"'host'"
op|':'
name|'self'
op|'.'
name|'_get_host'
op|'('
op|')'
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
name|'if'
name|'self'
op|'.'
name|'generate_samples'
op|':'
newline|'\n'
indent|'            '
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
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsSampleJsonTest
dedent|''
dedent|''
name|'class'
name|'VersionsSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_servers_get
indent|'    '
name|'def'
name|'test_servers_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"''"
op|','
name|'strip_version'
op|'='
name|'True'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'versions-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'VersionsSampleXmlTest'
op|'('
name|'VersionsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleJsonTest
dedent|''
name|'class'
name|'ServersSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_servers_post
indent|'    '
name|'def'
name|'test_servers_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'image_id'"
op|':'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
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
op|'}'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers'"
op|','
string|"'server-post-req'"
op|','
name|'subs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
number|'202'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_servers_get
dedent|''
name|'def'
name|'test_servers_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'test_servers_post'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'hostid'"
op|']'
op|'='
string|"'[a-f0-9]+'"
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'server-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'ServersSampleXmlTest'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleAllExtensionJsonTest
dedent|''
name|'class'
name|'ServersSampleAllExtensionJsonTest'
op|'('
name|'ServersSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersSampleAllExtensionXmlTest
dedent|''
name|'class'
name|'ServersSampleAllExtensionXmlTest'
op|'('
name|'ServersSampleXmlTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsSampleJsonTest
dedent|''
name|'class'
name|'ExtensionsSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_extensions_get
name|'def'
name|'test_extensions_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'extensions'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'extensions-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionsSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'ExtensionsSampleXmlTest'
op|'('
name|'ExtensionsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsSampleJsonTest
dedent|''
name|'class'
name|'FlavorsSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_flavors_get
indent|'    '
name|'def'
name|'test_flavors_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors/1'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavor-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavors_list
dedent|''
name|'def'
name|'test_flavors_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'flavors'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'flavors-list-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'FlavorsSampleXmlTest'
op|'('
name|'FlavorsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsSampleAllExtensionJsonTest
dedent|''
name|'class'
name|'FlavorsSampleAllExtensionJsonTest'
op|'('
name|'FlavorsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlavorsSampleAllExtensionXmlTest
dedent|''
name|'class'
name|'FlavorsSampleAllExtensionXmlTest'
op|'('
name|'FlavorsSampleXmlTest'
op|')'
op|':'
newline|'\n'
DECL|variable|all_extensions
indent|'    '
name|'all_extensions'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesSampleJsonTest
dedent|''
name|'class'
name|'ImagesSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_images_list
indent|'    '
name|'def'
name|'test_images_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of images get list request"""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'images-list-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_get
dedent|''
name|'def'
name|'test_image_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of one single image details request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
number|'200'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_images_details
dedent|''
name|'def'
name|'test_images_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of all images details request"""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'images-details-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_get
dedent|''
name|'def'
name|'test_image_metadata_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of a image metadata request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s/metadata'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_post
dedent|''
name|'def'
name|'test_image_metadata_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample to update metadata of an image metadata request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
nl|'\n'
string|"'images/%s/metadata'"
op|'%'
name|'image_id'
op|','
nl|'\n'
string|"'image-metadata-post-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
number|'200'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-post-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_put
dedent|''
name|'def'
name|'test_image_metadata_put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of image metadata put request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'images/%s/metadata'"
op|'%'
name|'image_id'
op|','
nl|'\n'
string|"'image-metadata-put-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
number|'200'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-put-resp'"
op|','
nl|'\n'
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_meta_key_get
dedent|''
name|'def'
name|'test_image_meta_key_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of a image metadata key request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|'"kernel_id"'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s/metadata/%s'"
op|'%'
op|'('
name|'image_id'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-meta-key-get'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_meta_key_put
dedent|''
name|'def'
name|'test_image_meta_key_put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get api sample of image metadata key put request"""'
newline|'\n'
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|'"auto_disk_config"'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'images/%s/metadata/%s'"
op|'%'
op|'('
name|'image_id'
op|','
name|'key'
op|')'
op|','
nl|'\n'
string|"'image-meta-key-put-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status'
op|','
number|'200'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-meta-key-put-resp'"
op|','
nl|'\n'
name|'subs'
op|','
nl|'\n'
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'ImagesSampleXmlTest'
op|'('
name|'ImagesSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsSampleJsonTest
dedent|''
name|'class'
name|'LimitsSampleJsonTest'
op|'('
name|'ApiSampleTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_limits_get
indent|'    '
name|'def'
name|'test_limits_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'limits'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'limit-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LimitsSampleXmlTest
dedent|''
dedent|''
name|'class'
name|'LimitsSampleXmlTest'
op|'('
name|'LimitsSampleJsonTest'
op|')'
op|':'
newline|'\n'
DECL|variable|ctype
indent|'    '
name|'ctype'
op|'='
string|"'xml'"
newline|'\n'
dedent|''
endmarker|''
end_unit
