begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Cloudscaling, Inc.'
nl|'\n'
comment|'# Author: Matthew Hooker <matt@cloudscaling.com>'
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
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'re'
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
DECL|function|_get_path_validator_regex
name|'def'
name|'_get_path_validator_regex'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# rfc3986 path validator regex from'
nl|'\n'
comment|'# http://jmrware.com/articles/2009/uri_regexp/URI_regex.html'
nl|'\n'
indent|'    '
name|'pchar'
op|'='
string|'"([A-Za-z0-9\\-._~!$&\'()*+,;=:@]|%[0-9A-Fa-f]{2})"'
newline|'\n'
name|'path'
op|'='
string|'"((/{pchar}*)*|"'
newline|'\n'
name|'path'
op|'+='
string|'"/({pchar}+(/{pchar}*)*)?|"'
newline|'\n'
name|'path'
op|'+='
string|'"{pchar}+(/{pchar}*)*|"'
newline|'\n'
name|'path'
op|'+='
string|'"{pchar}+(/{pchar}*)*|)"'
newline|'\n'
name|'path'
op|'='
name|'path'
op|'.'
name|'format'
op|'('
name|'pchar'
op|'='
name|'pchar'
op|')'
newline|'\n'
name|'return'
name|'re'
op|'.'
name|'compile'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|VALIDATE_PATH_RE
dedent|''
name|'VALIDATE_PATH_RE'
op|'='
name|'_get_path_validator_regex'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_str
name|'def'
name|'validate_str'
op|'('
name|'max_length'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|_do
indent|'    '
name|'def'
name|'_do'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'val'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'max_length'
name|'and'
name|'len'
op|'('
name|'val'
op|')'
op|'>'
name|'max_length'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_do'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_int
dedent|''
name|'def'
name|'validate_int'
op|'('
name|'max_value'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|_do
indent|'    '
name|'def'
name|'_do'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'val'
op|','
name|'int'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'max_value'
name|'and'
name|'val'
op|'>'
name|'max_value'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_do'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_url_path
dedent|''
name|'def'
name|'validate_url_path'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""True if val is matched by the path component grammar in rfc3986."""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'validate_str'
op|'('
op|')'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'VALIDATE_PATH_RE'
op|'.'
name|'match'
op|'('
name|'val'
op|')'
op|'.'
name|'end'
op|'('
op|')'
op|'=='
name|'len'
op|'('
name|'val'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_image_path
dedent|''
name|'def'
name|'validate_image_path'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'validate_str'
op|'('
op|')'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'bucket_name'
op|'='
name|'val'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'manifest_path'
op|'='
name|'val'
op|'['
name|'len'
op|'('
name|'bucket_name'
op|')'
op|'+'
number|'1'
op|':'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'len'
op|'('
name|'bucket_name'
op|')'
name|'or'
name|'not'
name|'len'
op|'('
name|'manifest_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'val'
op|'['
number|'0'
op|']'
op|'=='
string|"'/'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# make sure the image path if rfc3986 compliant'
nl|'\n'
comment|"# prepend '/' to make input validate"
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'validate_url_path'
op|'('
string|"'/'"
op|'+'
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_user_data
dedent|''
name|'def'
name|'validate_user_data'
op|'('
name|'user_data'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Check if the user_data is encoded properly."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'user_data'
op|'='
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'user_data'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate
dedent|''
name|'def'
name|'validate'
op|'('
name|'args'
op|','
name|'validator'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Validate values of args against validators in validator.\n\n    :param args:      Dict of values to be validated.\n    :param validator: A dict where the keys map to keys in args\n                      and the values are validators.\n                      Applies each validator to ``args[key]``\n    :returns: True if validation succeeds. Otherwise False.\n\n    A validator should be a callable which accepts 1 argument and which\n    returns True if the argument passes validation. False otherwise.\n    A validator should not raise an exception to indicate validity of the\n    argument.\n\n    Only validates keys which show up in both args and validator.\n\n    """'
newline|'\n'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'validator'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'key'
name|'not'
name|'in'
name|'args'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'='
name|'validator'
op|'['
name|'key'
op|']'
newline|'\n'
name|'assert'
name|'callable'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'f'
op|'('
name|'args'
op|'['
name|'key'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(key)s with value %(value)s failed"'
nl|'\n'
string|'" validator %(name)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'key'"
op|':'
name|'key'
op|','
string|"'value'"
op|':'
name|'args'
op|'['
name|'key'
op|']'
op|','
string|"'name'"
op|':'
name|'f'
op|'.'
name|'__name__'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
endmarker|''
end_unit
