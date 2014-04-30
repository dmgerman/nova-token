begin_unit
comment|'# Copyright (c) 2012, Cloudscaling'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
string|'"""\nGuidelines for writing new hacking checks\n\n - Use only for Nova specific tests. OpenStack general tests\n   should be submitted to the common \'hacking\' module.\n - Pick numbers in the range N3xx. Find the current test with\n   the highest allocated number and then pick the next value.\n - Keep the test method code in the source file ordered based\n   on the N3xx value.\n - List the new rule in the top level HACKING.rst file\n - Add test cases for each new rule to nova/tests/test_hacking.py\n\n"""'
newline|'\n'
nl|'\n'
DECL|variable|session_check
name|'session_check'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"\\w*def [a-zA-Z0-9].*[(].*session.*[)]"'
op|')'
newline|'\n'
DECL|variable|cfg_re
name|'cfg_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r".*\\scfg\\."'
op|')'
newline|'\n'
DECL|variable|vi_header_re
name|'vi_header_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"^#\\s+vim?:.+"'
op|')'
newline|'\n'
DECL|variable|virt_file_re
name|'virt_file_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'r"\\./nova/(?:tests/)?virt/(\\w+)/"'
op|')'
newline|'\n'
DECL|variable|virt_import_re
name|'virt_import_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"^\\s*(?:import|from) nova\\.(?:tests\\.)?virt\\.(\\w+)"'
op|')'
newline|'\n'
DECL|variable|virt_config_re
name|'virt_config_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"CONF\\.import_opt\\(\'.*?\', \'nova\\.virt\\.(\\w+)(\'|.)"'
op|')'
newline|'\n'
DECL|variable|author_tag_re
name|'author_tag_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"^\\s*#\\s*@?(a|A)uthor:"'
op|')'
newline|'\n'
DECL|variable|asse_trueinst_re
name|'asse_trueinst_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertTrue\\(isinstance\\((\\w|\\.|\\\'|\\"|\\[|\\])+, "'
nl|'\n'
string|'"(\\w|\\.|\\\'|\\"|\\[|\\])+\\)\\)"'
op|')'
newline|'\n'
DECL|variable|asse_equal_type_re
name|'asse_equal_type_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertEqual\\(type\\((\\w|\\.|\\\'|\\"|\\[|\\])+\\), "'
nl|'\n'
string|'"(\\w|\\.|\\\'|\\"|\\[|\\])+\\)"'
op|')'
newline|'\n'
DECL|variable|asse_equal_end_with_none_re
name|'asse_equal_end_with_none_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertEqual\\((\\w|\\.|\\\'|\\"|\\[|\\])+, None\\)"'
op|')'
newline|'\n'
DECL|variable|asse_equal_start_with_none_re
name|'asse_equal_start_with_none_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
nl|'\n'
string|'r"(.)*assertEqual\\(None, (\\w|\\.|\\\'|\\"|\\[|\\])+\\)"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_db_in_virt
name|'def'
name|'import_no_db_in_virt'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for db calls from nova/virt\n\n    As of grizzly-2 all the database calls have been removed from\n    nova/virt, and we want to keep it that way.\n\n    N307\n    """'
newline|'\n'
name|'if'
string|'"nova/virt"'
name|'in'
name|'filename'
name|'and'
name|'not'
name|'filename'
op|'.'
name|'endswith'
op|'('
string|'"fake.py"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"from nova import db"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N307: nova.db import not allowed in nova/virt/*"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_db_session_in_public_api
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_db_session_in_public_api'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
string|'"db/api.py"'
name|'in'
name|'filename'
name|'or'
string|'"db/sqlalchemy/api.py"'
name|'in'
name|'filename'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'session_check'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N309: public db api methods may not accept session"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|use_timeutils_utcnow
dedent|''
dedent|''
dedent|''
name|'def'
name|'use_timeutils_utcnow'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg'
op|'='
string|'"N310: timeutils.utcnow() must be used instead of datetime.%s()"'
newline|'\n'
nl|'\n'
name|'datetime_funcs'
op|'='
op|'['
string|"'now'"
op|','
string|"'utcnow'"
op|']'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'datetime_funcs'
op|':'
newline|'\n'
indent|'        '
name|'pos'
op|'='
name|'logical_line'
op|'.'
name|'find'
op|'('
string|"'datetime.%s'"
op|'%'
name|'f'
op|')'
newline|'\n'
name|'if'
name|'pos'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
name|'pos'
op|','
name|'msg'
op|'%'
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_virt_name
dedent|''
dedent|''
dedent|''
name|'def'
name|'_get_virt_name'
op|'('
name|'regex'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'m'
op|'='
name|'regex'
op|'.'
name|'match'
op|'('
name|'data'
op|')'
newline|'\n'
name|'if'
name|'m'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'driver'
op|'='
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
newline|'\n'
comment|'# Ignore things we mis-detect as virt drivers in the regex'
nl|'\n'
name|'if'
name|'driver'
name|'in'
op|'['
string|'"test_virt_drivers"'
op|','
string|'"driver"'
op|','
string|'"firewall"'
op|','
nl|'\n'
string|'"disk"'
op|','
string|'"api"'
op|','
string|'"imagecache"'
op|','
string|'"cpu"'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
comment|'# TODO(berrange): remove once bugs 1261826 and 126182 are'
nl|'\n'
comment|'# fixed, or baremetal driver is removed, which is first.'
nl|'\n'
dedent|''
name|'if'
name|'driver'
op|'=='
string|'"baremetal"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'driver'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_virt_driver_import_deps
dedent|''
name|'def'
name|'import_no_virt_driver_import_deps'
op|'('
name|'physical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check virt drivers\' modules aren\'t imported by other drivers\n\n    Modules under each virt driver\'s directory are\n    considered private to that virt driver. Other drivers\n    in Nova must not access those drivers. Any code that\n    is to be shared should be refactored into a common\n    module\n\n    N311\n    """'
newline|'\n'
name|'thisdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_file_re'
op|','
name|'filename'
op|')'
newline|'\n'
name|'thatdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_import_re'
op|','
name|'physical_line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'thatdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
op|'!='
name|'thatdriver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
number|'0'
op|','
string|'"N311: importing code from other virt drivers forbidden"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_no_virt_driver_config_deps
dedent|''
dedent|''
name|'def'
name|'import_no_virt_driver_config_deps'
op|'('
name|'physical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check virt drivers\' config vars aren\'t used by other drivers\n\n    Modules under each virt driver\'s directory are\n    considered private to that virt driver. Other drivers\n    in Nova must not use their config vars. Any config vars\n    that are to be shared should be moved into a common module\n\n    N312\n    """'
newline|'\n'
name|'thisdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_file_re'
op|','
name|'filename'
op|')'
newline|'\n'
name|'thatdriver'
op|'='
name|'_get_virt_name'
op|'('
name|'virt_config_re'
op|','
name|'physical_line'
op|')'
newline|'\n'
name|'if'
op|'('
name|'thatdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
name|'is'
name|'not'
name|'None'
name|'and'
nl|'\n'
name|'thisdriver'
op|'!='
name|'thatdriver'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
number|'0'
op|','
string|'"N312: using config vars from other virt drivers forbidden"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|capital_cfg_help
dedent|''
dedent|''
name|'def'
name|'capital_cfg_help'
op|'('
name|'logical_line'
op|','
name|'tokens'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'msg'
op|'='
string|'"N313: capitalize help string"'
newline|'\n'
nl|'\n'
name|'if'
name|'cfg_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'t'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'tokens'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'tokens'
op|'['
name|'t'
op|']'
op|'['
number|'1'
op|']'
op|'=='
string|'"help"'
op|':'
newline|'\n'
indent|'                '
name|'txt'
op|'='
name|'tokens'
op|'['
name|'t'
op|'+'
number|'2'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'txt'
op|')'
op|'>'
number|'1'
name|'and'
name|'txt'
op|'['
number|'1'
op|']'
op|'.'
name|'islower'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'yield'
op|'('
number|'0'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_vi_headers
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_vi_headers'
op|'('
name|'physical_line'
op|','
name|'line_number'
op|','
name|'lines'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for vi editor configuration in source files.\n\n    By default vi modelines can only appear in the first or\n    last 5 lines of a source file.\n\n    N314\n    """'
newline|'\n'
comment|'# NOTE(gilliard): line_number is 1-indexed'
nl|'\n'
name|'if'
name|'line_number'
op|'<='
number|'5'
name|'or'
name|'line_number'
op|'>'
name|'len'
op|'('
name|'lines'
op|')'
op|'-'
number|'5'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'vi_header_re'
op|'.'
name|'match'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'0'
op|','
string|'"N314: Don\'t put vi configuration in source files"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_author_tags
dedent|''
dedent|''
dedent|''
name|'def'
name|'no_author_tags'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'author_tag_re'
op|'.'
name|'match'
op|'('
name|'physical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pos'
op|'='
name|'physical_line'
op|'.'
name|'find'
op|'('
string|"'author'"
op|')'
newline|'\n'
name|'return'
name|'pos'
op|','
string|'"N315: Don\'t use author tags"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_true_instance
dedent|''
dedent|''
name|'def'
name|'assert_true_instance'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertTrue(isinstance(a, b)) sentences\n\n    N316\n    """'
newline|'\n'
name|'if'
name|'asse_trueinst_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N316: assertTrue(isinstance(a, b)) sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_equal_type
dedent|''
dedent|''
name|'def'
name|'assert_equal_type'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertEqual(type(A), B) sentences\n\n    N317\n    """'
newline|'\n'
name|'if'
name|'asse_equal_type_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N317: assertEqual(type(A), B) sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|assert_equal_none
dedent|''
dedent|''
name|'def'
name|'assert_equal_none'
op|'('
name|'logical_line'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for assertEqual(A, None) or assertEqual(None, A) sentences\n\n    N318\n    """'
newline|'\n'
name|'res'
op|'='
op|'('
name|'asse_equal_start_with_none_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
name|'or'
nl|'\n'
name|'asse_equal_end_with_none_re'
op|'.'
name|'match'
op|'('
name|'logical_line'
op|')'
op|')'
newline|'\n'
name|'if'
name|'res'
op|':'
newline|'\n'
indent|'        '
name|'yield'
op|'('
number|'0'
op|','
string|'"N318: assertEqual(A, None) or assertEqual(None, A) "'
nl|'\n'
string|'"sentences not allowed"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|no_translate_debug_logs
dedent|''
dedent|''
name|'def'
name|'no_translate_debug_logs'
op|'('
name|'logical_line'
op|','
name|'filename'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check for \'LOG.debug(_(\'\n\n    As per our translation policy,\n    https://wiki.openstack.org/wiki/LoggingStandards#Log_Translation\n    we shouldn\'t translate debug level logs.\n\n    * This check assumes that \'LOG\' is a logger.\n    * Use filename so we can start enforcing this in specific folders instead\n      of needing to do so all at once.\n\n    N319\n    """'
newline|'\n'
name|'dirs'
op|'='
op|'['
string|'"nova/scheduler"'
op|','
nl|'\n'
string|'"nova/network"'
op|','
nl|'\n'
string|'"nova/volume"'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'if'
name|'max'
op|'('
op|'['
name|'name'
name|'in'
name|'filename'
name|'for'
name|'name'
name|'in'
name|'dirs'
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'logical_line'
op|'.'
name|'startswith'
op|'('
string|'"LOG.debug(_("'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
op|'('
number|'0'
op|','
string|'"N319 Don\'t translate debug level logs"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|factory
dedent|''
dedent|''
dedent|''
name|'def'
name|'factory'
op|'('
name|'register'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'register'
op|'('
name|'import_no_db_in_virt'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_db_session_in_public_api'
op|')'
newline|'\n'
name|'register'
op|'('
name|'use_timeutils_utcnow'
op|')'
newline|'\n'
name|'register'
op|'('
name|'import_no_virt_driver_import_deps'
op|')'
newline|'\n'
name|'register'
op|'('
name|'import_no_virt_driver_config_deps'
op|')'
newline|'\n'
name|'register'
op|'('
name|'capital_cfg_help'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_vi_headers'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_author_tags'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_true_instance'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_equal_type'
op|')'
newline|'\n'
name|'register'
op|'('
name|'assert_equal_none'
op|')'
newline|'\n'
name|'register'
op|'('
name|'no_translate_debug_logs'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
