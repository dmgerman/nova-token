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
string|'"""Fake LDAP server for test harness.\n\nThis class does very little error checking, and knows nothing about ldap\nclass definitions.  It implements the minimum emulation of the python ldap\nlibrary to work with nova.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'fnmatch'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Store
name|'class'
name|'Store'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'__class__'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Attempted to instantiate singleton'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|instance
name|'def'
name|'instance'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'cls'
op|','
string|"'_instance'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'_StorageDict'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_StorageDict
dedent|''
dedent|''
name|'class'
name|'_StorageDict'
op|'('
name|'dict'
op|')'
op|':'
newline|'\n'
DECL|member|keys
indent|'    '
name|'def'
name|'keys'
op|'('
name|'self'
op|','
name|'pat'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ret'
op|'='
name|'super'
op|'('
name|'_StorageDict'
op|','
name|'self'
op|')'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
name|'if'
name|'pat'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'fnmatch'
op|'.'
name|'filter'
op|'('
name|'ret'
op|','
name|'pat'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|flushdb
dedent|''
dedent|''
name|'def'
name|'flushdb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'clear'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|hgetall
dedent|''
name|'def'
name|'hgetall'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns the hash for the given key; creates\n        the hash if the key doesn\'t exist."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
name|'key'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'return'
name|'self'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
DECL|member|hget
dedent|''
dedent|''
name|'def'
name|'hget'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'field'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hashdict'
op|'='
name|'self'
op|'.'
name|'hgetall'
op|'('
name|'key'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'hashdict'
op|'['
name|'field'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'hashdict'
op|'['
name|'field'
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'return'
name|'hashdict'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
DECL|member|hset
dedent|''
dedent|''
name|'def'
name|'hset'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'field'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hashdict'
op|'='
name|'self'
op|'.'
name|'hgetall'
op|'('
name|'key'
op|')'
newline|'\n'
name|'hashdict'
op|'['
name|'field'
op|']'
op|'='
name|'val'
newline|'\n'
nl|'\n'
DECL|member|hmset
dedent|''
name|'def'
name|'hmset'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hashdict'
op|'='
name|'self'
op|'.'
name|'hgetall'
op|'('
name|'key'
op|')'
newline|'\n'
name|'for'
name|'field'
op|','
name|'val'
name|'in'
name|'value_dict'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'hashdict'
op|'['
name|'field'
op|']'
op|'='
name|'val'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|SCOPE_BASE
dedent|''
dedent|''
dedent|''
name|'SCOPE_BASE'
op|'='
number|'0'
newline|'\n'
DECL|variable|SCOPE_ONELEVEL
name|'SCOPE_ONELEVEL'
op|'='
number|'1'
comment|'# Not implemented'
newline|'\n'
DECL|variable|SCOPE_SUBTREE
name|'SCOPE_SUBTREE'
op|'='
number|'2'
newline|'\n'
DECL|variable|MOD_ADD
name|'MOD_ADD'
op|'='
number|'0'
newline|'\n'
DECL|variable|MOD_DELETE
name|'MOD_DELETE'
op|'='
number|'1'
newline|'\n'
DECL|variable|MOD_REPLACE
name|'MOD_REPLACE'
op|'='
number|'2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NO_SUCH_OBJECT
name|'class'
name|'NO_SUCH_OBJECT'
op|'('
name|'Exception'
op|')'
op|':'
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'    '
string|'"""Duplicate exception class from real LDAP module."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OBJECT_CLASS_VIOLATION
dedent|''
name|'class'
name|'OBJECT_CLASS_VIOLATION'
op|'('
name|'Exception'
op|')'
op|':'
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'    '
string|'"""Duplicate exception class from real LDAP module."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SERVER_DOWN
dedent|''
name|'class'
name|'SERVER_DOWN'
op|'('
name|'Exception'
op|')'
op|':'
comment|'# pylint: disable=C0103'
newline|'\n'
indent|'    '
string|'"""Duplicate exception class from real LDAP module."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|initialize
dedent|''
name|'def'
name|'initialize'
op|'('
name|'_uri'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Opens a fake connection with an LDAP server."""'
newline|'\n'
name|'return'
name|'FakeLDAP'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_match_query
dedent|''
name|'def'
name|'_match_query'
op|'('
name|'query'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Match an ldap query to an attribute dictionary.\n\n    The characters &, |, and ! are supported in the query. No syntax checking\n    is performed, so malformed queries will not work correctly.\n    """'
newline|'\n'
comment|'# cut off the parentheses'
nl|'\n'
name|'inner'
op|'='
name|'query'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
name|'if'
name|'inner'
op|'.'
name|'startswith'
op|'('
string|"'&'"
op|')'
op|':'
newline|'\n'
comment|'# cut off the &'
nl|'\n'
indent|'        '
name|'l'
op|','
name|'r'
op|'='
name|'_paren_groups'
op|'('
name|'inner'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
name|'return'
name|'_match_query'
op|'('
name|'l'
op|','
name|'attrs'
op|')'
name|'and'
name|'_match_query'
op|'('
name|'r'
op|','
name|'attrs'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'inner'
op|'.'
name|'startswith'
op|'('
string|"'|'"
op|')'
op|':'
newline|'\n'
comment|'# cut off the |'
nl|'\n'
indent|'        '
name|'l'
op|','
name|'r'
op|'='
name|'_paren_groups'
op|'('
name|'inner'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
name|'return'
name|'_match_query'
op|'('
name|'l'
op|','
name|'attrs'
op|')'
name|'or'
name|'_match_query'
op|'('
name|'r'
op|','
name|'attrs'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'inner'
op|'.'
name|'startswith'
op|'('
string|"'!'"
op|')'
op|':'
newline|'\n'
comment|'# cut off the ! and the nested parentheses'
nl|'\n'
indent|'        '
name|'return'
name|'not'
name|'_match_query'
op|'('
name|'query'
op|'['
number|'2'
op|':'
op|'-'
number|'1'
op|']'
op|','
name|'attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'('
name|'k'
op|','
name|'_sep'
op|','
name|'v'
op|')'
op|'='
name|'inner'
op|'.'
name|'partition'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'return'
name|'_match'
op|'('
name|'k'
op|','
name|'v'
op|','
name|'attrs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_paren_groups
dedent|''
name|'def'
name|'_paren_groups'
op|'('
name|'source'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Split a string into parenthesized groups."""'
newline|'\n'
name|'count'
op|'='
number|'0'
newline|'\n'
name|'start'
op|'='
number|'0'
newline|'\n'
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'pos'
name|'in'
name|'xrange'
op|'('
name|'len'
op|'('
name|'source'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'source'
op|'['
name|'pos'
op|']'
op|'=='
string|"'('"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'start'
op|'='
name|'pos'
newline|'\n'
dedent|''
name|'count'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'source'
op|'['
name|'pos'
op|']'
op|'=='
string|"')'"
op|':'
newline|'\n'
indent|'            '
name|'count'
op|'-='
number|'1'
newline|'\n'
name|'if'
name|'count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'.'
name|'append'
op|'('
name|'source'
op|'['
name|'start'
op|':'
name|'pos'
op|'+'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_match
dedent|''
name|'def'
name|'_match'
op|'('
name|'key'
op|','
name|'value'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Match a given key and value against an attribute list."""'
newline|'\n'
name|'if'
name|'key'
name|'not'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
comment|'# This is a wild card search. Implemented as all or nothing for now.'
nl|'\n'
dedent|''
name|'if'
name|'value'
op|'=='
string|'"*"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'key'
op|'!='
string|'"objectclass"'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
name|'in'
name|'attrs'
op|'['
name|'key'
op|']'
newline|'\n'
comment|'# it is an objectclass check, so check subclasses'
nl|'\n'
dedent|''
name|'values'
op|'='
name|'_subs'
op|'('
name|'value'
op|')'
newline|'\n'
name|'for'
name|'v'
name|'in'
name|'values'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'v'
name|'in'
name|'attrs'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_subs
dedent|''
name|'def'
name|'_subs'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns a list of subclass strings.\n\n    The strings represent the ldap object class plus any subclasses that\n    inherit from it. Fakeldap doesn\'t know about the ldap object structure,\n    so subclasses need to be defined manually in the dictionary below.\n\n    """'
newline|'\n'
name|'subs'
op|'='
op|'{'
string|"'groupOfNames'"
op|':'
op|'['
string|"'novaProject'"
op|']'
op|'}'
newline|'\n'
name|'if'
name|'value'
name|'in'
name|'subs'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'value'
op|']'
op|'+'
name|'subs'
op|'['
name|'value'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'['
name|'value'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_from_json
dedent|''
name|'def'
name|'_from_json'
op|'('
name|'encoded'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert attribute values from json representation.\n\n    Args:\n    encoded -- a json encoded string\n\n    Returns a list of strings\n\n    """'
newline|'\n'
name|'return'
op|'['
name|'str'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'encoded'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_to_json
dedent|''
name|'def'
name|'_to_json'
op|'('
name|'unencoded'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert attribute values into json representation.\n\n    Args:\n    unencoded -- an unencoded string or list of strings.  If it\n        is a single string, it will be converted into a list.\n\n    Returns a json string\n\n    """'
newline|'\n'
name|'return'
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'list'
op|'('
name|'unencoded'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|server_fail
dedent|''
name|'server_fail'
op|'='
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLDAP
name|'class'
name|'FakeLDAP'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Fake LDAP connection."""'
newline|'\n'
nl|'\n'
DECL|member|simple_bind_s
name|'def'
name|'simple_bind_s'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is ignored, but provided for compatibility."""'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
dedent|''
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|unbind_s
dedent|''
name|'def'
name|'unbind_s'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This method is ignored, but provided for compatibility."""'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
dedent|''
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|add_s
dedent|''
name|'def'
name|'add_s'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add an object with the specified attributes at dn."""'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
nl|'\n'
dedent|''
name|'key'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|','
name|'dn'
op|')'
newline|'\n'
name|'value_dict'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'_to_json'
op|'('
name|'v'
op|')'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'attr'
op|']'
op|')'
newline|'\n'
name|'Store'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'hmset'
op|'('
name|'key'
op|','
name|'value_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_s
dedent|''
name|'def'
name|'delete_s'
op|'('
name|'self'
op|','
name|'dn'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove the ldap object at specified dn."""'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
nl|'\n'
dedent|''
name|'Store'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'delete'
op|'('
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|','
name|'dn'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_s
dedent|''
name|'def'
name|'modify_s'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modify the object at dn using the attribute list.\n\n        :param dn: a dn\n        :param attrs: a list of tuples in the following form::\n\n            ([MOD_ADD | MOD_DELETE | MOD_REPACE], attribute, value)\n\n        """'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
nl|'\n'
dedent|''
name|'store'
op|'='
name|'Store'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|','
name|'dn'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'cmd'
op|','
name|'k'
op|','
name|'v'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'            '
name|'values'
op|'='
name|'_from_json'
op|'('
name|'store'
op|'.'
name|'hget'
op|'('
name|'key'
op|','
name|'k'
op|')'
op|')'
newline|'\n'
name|'if'
name|'cmd'
op|'=='
name|'MOD_ADD'
op|':'
newline|'\n'
indent|'                '
name|'values'
op|'.'
name|'append'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'cmd'
op|'=='
name|'MOD_REPLACE'
op|':'
newline|'\n'
indent|'                '
name|'values'
op|'='
op|'['
name|'v'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'values'
op|'.'
name|'remove'
op|'('
name|'v'
op|')'
newline|'\n'
dedent|''
name|'values'
op|'='
name|'store'
op|'.'
name|'hset'
op|'('
name|'key'
op|','
name|'k'
op|','
name|'_to_json'
op|'('
name|'values'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modrdn_s
dedent|''
dedent|''
name|'def'
name|'modrdn_s'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'newrdn'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oldobj'
op|'='
name|'self'
op|'.'
name|'search_s'
op|'('
name|'dn'
op|','
name|'SCOPE_BASE'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'oldobj'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NO_SUCH_OBJECT'
op|'('
op|')'
newline|'\n'
dedent|''
name|'newdn'
op|'='
string|'"%s,%s"'
op|'%'
op|'('
name|'newrdn'
op|','
name|'dn'
op|'.'
name|'partition'
op|'('
string|"','"
op|')'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'newattrs'
op|'='
name|'oldobj'
op|'['
number|'0'
op|']'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
name|'modlist'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'attrtype'
name|'in'
name|'newattrs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'modlist'
op|'.'
name|'append'
op|'('
op|'('
name|'attrtype'
op|','
name|'newattrs'
op|'['
name|'attrtype'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'add_s'
op|'('
name|'newdn'
op|','
name|'modlist'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'delete_s'
op|'('
name|'dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|search_s
dedent|''
name|'def'
name|'search_s'
op|'('
name|'self'
op|','
name|'dn'
op|','
name|'scope'
op|','
name|'query'
op|'='
name|'None'
op|','
name|'fields'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Search for all matching objects under dn using the query.\n\n        Args:\n        dn -- dn to search under\n        scope -- only SCOPE_BASE and SCOPE_SUBTREE are supported\n        query -- query to filter objects by\n        fields -- fields to return. Returns all fields if not specified\n\n        """'
newline|'\n'
name|'if'
name|'server_fail'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'SERVER_DOWN'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'scope'
op|'!='
name|'SCOPE_BASE'
name|'and'
name|'scope'
op|'!='
name|'SCOPE_SUBTREE'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NotImplementedError'
op|'('
name|'str'
op|'('
name|'scope'
op|')'
op|')'
newline|'\n'
dedent|''
name|'store'
op|'='
name|'Store'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'if'
name|'scope'
op|'=='
name|'SCOPE_BASE'
op|':'
newline|'\n'
indent|'            '
name|'pattern'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|','
name|'dn'
op|')'
newline|'\n'
name|'keys'
op|'='
name|'store'
op|'.'
name|'keys'
op|'('
name|'pattern'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'keys'
op|'='
name|'store'
op|'.'
name|'keys'
op|'('
string|'"%s*%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|','
name|'dn'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'keys'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NO_SUCH_OBJECT'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'objects'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'keys'
op|':'
newline|'\n'
comment|'# get the attributes from the store'
nl|'\n'
indent|'            '
name|'attrs'
op|'='
name|'store'
op|'.'
name|'hgetall'
op|'('
name|'key'
op|')'
newline|'\n'
comment|'# turn the values from the store into lists'
nl|'\n'
comment|'# pylint: disable=E1103'
nl|'\n'
name|'attrs'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'_from_json'
op|'('
name|'v'
op|')'
op|')'
nl|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'attrs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
comment|'# filter the objects by query'
nl|'\n'
name|'if'
name|'not'
name|'query'
name|'or'
name|'_match_query'
op|'('
name|'query'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
comment|'# filter the attributes by fields'
nl|'\n'
indent|'                '
name|'attrs'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'attrs'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'not'
name|'fields'
name|'or'
name|'k'
name|'in'
name|'fields'
op|']'
op|')'
newline|'\n'
name|'objects'
op|'.'
name|'append'
op|'('
op|'('
name|'key'
op|'['
name|'len'
op|'('
name|'self'
op|'.'
name|'__prefix'
op|')'
op|':'
op|']'
op|','
name|'attrs'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'objects'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|__prefix
name|'def'
name|'__prefix'
op|'('
name|'self'
op|')'
op|':'
comment|'# pylint: disable=R0201'
newline|'\n'
indent|'        '
string|'"""Get the prefix to use for all keys."""'
newline|'\n'
name|'return'
string|"'ldap:'"
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
