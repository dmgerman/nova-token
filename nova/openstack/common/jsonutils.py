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
string|"'''\nJSON related utilities.\n\nThis module provides a few things:\n\n    1) A handy function for getting an object down to something that can be\n    JSON serialized.  See to_primitive().\n\n    2) Wrappers around loads() and dumps().  The dumps() wrapper will\n    automatically use to_primitive() for you if needed.\n\n    3) This sets up anyjson to use the loads() and dumps() wrappers if anyjson\n    is available.\n'''"
newline|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'codecs'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'inspect'
newline|'\n'
name|'import'
name|'itertools'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'version_info'
op|'<'
op|'('
number|'2'
op|','
number|'7'
op|')'
op|':'
newline|'\n'
comment|'# On Python <= 2.6, json module is not C boosted, so try to use'
nl|'\n'
comment|'# simplejson module if available'
nl|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'simplejson'
name|'as'
name|'json'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'        '
name|'import'
name|'json'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'json'
newline|'\n'
nl|'\n'
dedent|''
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'six'
op|'.'
name|'moves'
op|'.'
name|'xmlrpc_client'
name|'as'
name|'xmlrpclib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'gettextutils'
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
name|'strutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'timeutils'
newline|'\n'
nl|'\n'
DECL|variable|netaddr
name|'netaddr'
op|'='
name|'importutils'
op|'.'
name|'try_import'
op|'('
string|'"netaddr"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_nasty_type_tests
name|'_nasty_type_tests'
op|'='
op|'['
name|'inspect'
op|'.'
name|'ismodule'
op|','
name|'inspect'
op|'.'
name|'isclass'
op|','
name|'inspect'
op|'.'
name|'ismethod'
op|','
nl|'\n'
name|'inspect'
op|'.'
name|'isfunction'
op|','
name|'inspect'
op|'.'
name|'isgeneratorfunction'
op|','
nl|'\n'
name|'inspect'
op|'.'
name|'isgenerator'
op|','
name|'inspect'
op|'.'
name|'istraceback'
op|','
name|'inspect'
op|'.'
name|'isframe'
op|','
nl|'\n'
name|'inspect'
op|'.'
name|'iscode'
op|','
name|'inspect'
op|'.'
name|'isbuiltin'
op|','
name|'inspect'
op|'.'
name|'isroutine'
op|','
nl|'\n'
name|'inspect'
op|'.'
name|'isabstract'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|_simple_types
name|'_simple_types'
op|'='
op|'('
name|'six'
op|'.'
name|'string_types'
op|'+'
name|'six'
op|'.'
name|'integer_types'
nl|'\n'
op|'+'
op|'('
name|'type'
op|'('
name|'None'
op|')'
op|','
name|'bool'
op|','
name|'float'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|to_primitive
name|'def'
name|'to_primitive'
op|'('
name|'value'
op|','
name|'convert_instances'
op|'='
name|'False'
op|','
name|'convert_datetime'
op|'='
name|'True'
op|','
nl|'\n'
name|'level'
op|'='
number|'0'
op|','
name|'max_depth'
op|'='
number|'3'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a complex object into primitives.\n\n    Handy for JSON serialization. We can optionally handle instances,\n    but since this is a recursive function, we could have cyclical\n    data structures.\n\n    To handle cyclical data structures we could track the actual objects\n    visited in a set, but not all objects are hashable. Instead we just\n    track the depth of the object inspections and don\'t go too deep.\n\n    Therefore, convert_instances=True is lossy ... be aware.\n\n    """'
newline|'\n'
comment|'# handle obvious types first - order of basic types determined by running'
nl|'\n'
comment|'# full tests on nova project, resulting in the following counts:'
nl|'\n'
comment|"# 572754 <type 'NoneType'>"
nl|'\n'
comment|"# 460353 <type 'int'>"
nl|'\n'
comment|"# 379632 <type 'unicode'>"
nl|'\n'
comment|"# 274610 <type 'str'>"
nl|'\n'
comment|"# 199918 <type 'dict'>"
nl|'\n'
comment|"# 114200 <type 'datetime.datetime'>"
nl|'\n'
comment|"#  51817 <type 'bool'>"
nl|'\n'
comment|"#  26164 <type 'list'>"
nl|'\n'
comment|"#   6491 <type 'float'>"
nl|'\n'
comment|"#    283 <type 'tuple'>"
nl|'\n'
comment|"#     19 <type 'long'>"
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'_simple_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
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
name|'if'
name|'convert_datetime'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'value'
newline|'\n'
nl|'\n'
comment|"# value of itertools.count doesn't get caught by nasty_type_tests"
nl|'\n'
comment|'# and results in infinite loop when list(value) is called.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'type'
op|'('
name|'value'
op|')'
op|'=='
name|'itertools'
op|'.'
name|'count'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
comment|'# FIXME(vish): Workaround for LP bug 852095. Without this workaround,'
nl|'\n'
comment|'#              tests that raise an exception in a mocked method that'
nl|'\n'
comment|'#              has a @wrap_exception with a notifier will fail. If'
nl|'\n'
comment|'#              we up the dependency to 0.5.4 (when it is released) we'
nl|'\n'
comment|'#              can remove this workaround.'
nl|'\n'
dedent|''
name|'if'
name|'getattr'
op|'('
name|'value'
op|','
string|"'__module__'"
op|','
name|'None'
op|')'
op|'=='
string|"'mox'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'mock'"
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'level'
op|'>'
name|'max_depth'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'?'"
newline|'\n'
nl|'\n'
comment|'# The try block may not be necessary after the class check above,'
nl|'\n'
comment|'# but just in case ...'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'recursive'
op|'='
name|'functools'
op|'.'
name|'partial'
op|'('
name|'to_primitive'
op|','
nl|'\n'
name|'convert_instances'
op|'='
name|'convert_instances'
op|','
nl|'\n'
name|'convert_datetime'
op|'='
name|'convert_datetime'
op|','
nl|'\n'
name|'level'
op|'='
name|'level'
op|','
nl|'\n'
name|'max_depth'
op|'='
name|'max_depth'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
op|'('
name|'k'
op|','
name|'recursive'
op|'('
name|'v'
op|')'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
op|'('
name|'list'
op|','
name|'tuple'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'recursive'
op|'('
name|'lv'
op|')'
name|'for'
name|'lv'
name|'in'
name|'value'
op|']'
newline|'\n'
nl|'\n'
comment|"# It's not clear why xmlrpclib created their own DateTime type, but"
nl|'\n'
comment|'# for our purposes, make it a datetime type which is explicitly'
nl|'\n'
comment|'# handled'
nl|'\n'
dedent|''
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'xmlrpclib'
op|'.'
name|'DateTime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
op|'*'
name|'tuple'
op|'('
name|'value'
op|'.'
name|'timetuple'
op|'('
op|')'
op|')'
op|'['
op|':'
number|'6'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'convert_datetime'
name|'and'
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
indent|'            '
name|'return'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'value'
op|','
name|'gettextutils'
op|'.'
name|'Message'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'value'
op|'.'
name|'data'
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
indent|'            '
name|'return'
name|'recursive'
op|'('
name|'dict'
op|'('
name|'value'
op|'.'
name|'iteritems'
op|'('
op|')'
op|')'
op|','
name|'level'
op|'='
name|'level'
op|'+'
number|'1'
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
indent|'            '
name|'return'
name|'recursive'
op|'('
name|'list'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'convert_instances'
name|'and'
name|'hasattr'
op|'('
name|'value'
op|','
string|"'__dict__'"
op|')'
op|':'
newline|'\n'
comment|'# Likely an instance of something. Watch for cycles.'
nl|'\n'
comment|'# Ignore class member vars.'
nl|'\n'
indent|'            '
name|'return'
name|'recursive'
op|'('
name|'value'
op|'.'
name|'__dict__'
op|','
name|'level'
op|'='
name|'level'
op|'+'
number|'1'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'netaddr'
name|'and'
name|'isinstance'
op|'('
name|'value'
op|','
name|'netaddr'
op|'.'
name|'IPAddress'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'any'
op|'('
name|'test'
op|'('
name|'value'
op|')'
name|'for'
name|'test'
name|'in'
name|'_nasty_type_tests'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|'# Class objects are tricky since they may define something like'
nl|'\n'
comment|"# __iter__ defined but it isn't callable as list()."
nl|'\n'
indent|'        '
name|'return'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'value'
op|')'
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
op|','
name|'default'
op|'='
name|'to_primitive'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|','
name|'default'
op|'='
name|'default'
op|','
op|'**'
name|'kwargs'
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
op|','
name|'encoding'
op|'='
string|"'utf-8'"
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'strutils'
op|'.'
name|'safe_decode'
op|'('
name|'s'
op|','
name|'encoding'
op|')'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load
dedent|''
name|'def'
name|'load'
op|'('
name|'fp'
op|','
name|'encoding'
op|'='
string|"'utf-8'"
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'json'
op|'.'
name|'load'
op|'('
name|'codecs'
op|'.'
name|'getreader'
op|'('
name|'encoding'
op|')'
op|'('
name|'fp'
op|')'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'anyjson'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'anyjson'
op|'.'
name|'_modules'
op|'.'
name|'append'
op|'('
op|'('
name|'__name__'
op|','
string|"'dumps'"
op|','
name|'TypeError'
op|','
nl|'\n'
string|"'loads'"
op|','
name|'ValueError'
op|','
string|"'load'"
op|')'
op|')'
newline|'\n'
name|'anyjson'
op|'.'
name|'force_implementation'
op|'('
name|'__name__'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
