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
comment|'# Copyright 2010 Anso Labs, LLC'
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
string|'"""\n  Fake LDAP server for test harnesses.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'datastore'
newline|'\n'
nl|'\n'
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
nl|'\n'
nl|'\n'
DECL|class|NO_SUCH_OBJECT
name|'class'
name|'NO_SUCH_OBJECT'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|initialize
dedent|''
name|'def'
name|'initialize'
op|'('
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FakeLDAP'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLDAP
dedent|''
name|'class'
name|'FakeLDAP'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|simple_bind_s
indent|'    '
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
string|'"""This method is ignored, but provided for compatibility"""'
newline|'\n'
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
string|'"""This method is ignored, but provided for compatibility"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_paren_groups
dedent|''
name|'def'
name|'_paren_groups'
op|'('
name|'self'
op|','
name|'source'
op|')'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'if'
name|'source'
op|'['
name|'pos'
op|']'
op|'=='
string|"'('"
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'count'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
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
indent|'                '
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
indent|'                    '
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
DECL|member|_match_query
dedent|''
name|'def'
name|'_match_query'
op|'('
name|'self'
op|','
name|'query'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
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
indent|'            '
name|'l'
op|','
name|'r'
op|'='
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_match_query'
op|'('
name|'l'
op|','
name|'attrs'
op|')'
name|'and'
name|'self'
op|'.'
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
indent|'            '
name|'l'
op|','
name|'r'
op|'='
name|'self'
op|'.'
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
name|'self'
op|'.'
name|'_match_query'
op|'('
name|'l'
op|','
name|'attrs'
op|')'
name|'or'
name|'self'
op|'.'
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
indent|'            '
name|'return'
name|'not'
name|'self'
op|'.'
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
name|'sep'
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
name|'self'
op|'.'
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
DECL|member|_subs
dedent|''
name|'def'
name|'_subs'
op|'('
name|'self'
op|','
name|'v'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'subs'
op|'='
op|'{'
nl|'\n'
string|"'groupOfNames'"
op|':'
op|'['
string|"'novaProject'"
op|']'
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'v'
name|'in'
name|'subs'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'v'
op|']'
op|'+'
name|'subs'
op|'['
name|'v'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'['
name|'v'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_match
dedent|''
name|'def'
name|'_match'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|','
name|'attrs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attrs'
op|'.'
name|'has_key'
op|'('
name|'k'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'v'
name|'in'
name|'self'
op|'.'
name|'_subs'
op|'('
name|'v'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'v'
name|'in'
name|'attrs'
op|'['
name|'k'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
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
string|'"""search for all matching objects under dn using the query\n        only SCOPE_SUBTREE is supported.\n        """'
newline|'\n'
name|'if'
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
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'keys'
op|'='
name|'redis'
op|'.'
name|'keys'
op|'('
name|'self'
op|'.'
name|'_redis_prefix'
op|'+'
string|"'*'"
op|'+'
name|'dn'
op|')'
newline|'\n'
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
comment|'# get the attributes from redis'
nl|'\n'
indent|'            '
name|'attrs'
op|'='
name|'redis'
op|'.'
name|'hgetall'
op|'('
name|'key'
op|')'
newline|'\n'
comment|'# turn the values from redis into lists'
nl|'\n'
name|'attrs'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'self'
op|'.'
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
name|'self'
op|'.'
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
name|'_redis_prefix'
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
name|'if'
name|'objects'
op|'=='
op|'['
op|']'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'NO_SUCH_OBJECT'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'objects'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|_redis_prefix
name|'def'
name|'_redis_prefix'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'ldap:'"
newline|'\n'
nl|'\n'
DECL|member|_from_json
dedent|''
name|'def'
name|'_from_json'
op|'('
name|'self'
op|','
name|'encoded'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert attribute values from json representation."""'
newline|'\n'
comment|'# return as simple strings instead of unicode strings'
nl|'\n'
name|'return'
op|'['
name|'str'
op|'('
name|'x'
op|')'
name|'for'
name|'x'
name|'in'
name|'json'
op|'.'
name|'loads'
op|'('
name|'encoded'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_to_json
dedent|''
name|'def'
name|'_to_json'
op|'('
name|'self'
op|','
name|'unencoded'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert attribute values into json representation."""'
newline|'\n'
comment|'# all values are returned as lists from ldap'
nl|'\n'
name|'return'
name|'json'
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
name|'key'
op|'='
name|'self'
op|'.'
name|'_redis_prefix'
op|'+'
name|'dn'
newline|'\n'
nl|'\n'
name|'value_dict'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'k'
op|','
name|'self'
op|'.'
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
name|'datastore'
op|'.'
name|'Redis'
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
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'_redis_prefix'
op|'+'
name|'dn'
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
string|'"""Modify the object at dn using the attribute list.\n        attr is a list of tuples in the following form:\n            ([MOD_ADD | MOD_DELETE], attribute, value)\n        """'
newline|'\n'
name|'redis'
op|'='
name|'datastore'
op|'.'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'_redis_prefix'
op|'+'
name|'dn'
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
name|'self'
op|'.'
name|'_from_json'
op|'('
name|'redis'
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
name|'redis'
op|'.'
name|'hset'
op|'('
name|'key'
op|','
name|'k'
op|','
name|'self'
op|'.'
name|'_to_json'
op|'('
name|'values'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
