begin_unit
comment|'# Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, '
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
name|'from'
name|'boto'
op|'.'
name|'sdb'
op|'.'
name|'db'
op|'.'
name|'manager'
name|'import'
name|'get_manager'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'sdb'
op|'.'
name|'db'
op|'.'
name|'property'
name|'import'
name|'Property'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'sdb'
op|'.'
name|'db'
op|'.'
name|'key'
name|'import'
name|'Key'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'sdb'
op|'.'
name|'db'
op|'.'
name|'query'
name|'import'
name|'Query'
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
nl|'\n'
DECL|class|ModelMeta
name|'class'
name|'ModelMeta'
op|'('
name|'type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"Metaclass for all Models"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'bases'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ModelMeta'
op|','
name|'cls'
op|')'
op|'.'
name|'__init__'
op|'('
name|'name'
op|','
name|'bases'
op|','
name|'dict'
op|')'
newline|'\n'
comment|'# Make sure this is a subclass of Model - mainly copied from django ModelBase (thanks!)'
nl|'\n'
name|'cls'
op|'.'
name|'__sub_classes__'
op|'='
op|'['
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'filter'
op|'('
name|'lambda'
name|'b'
op|':'
name|'issubclass'
op|'('
name|'b'
op|','
name|'Model'
op|')'
op|','
name|'bases'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'base'
name|'in'
name|'bases'
op|':'
newline|'\n'
indent|'                    '
name|'base'
op|'.'
name|'__sub_classes__'
op|'.'
name|'append'
op|'('
name|'cls'
op|')'
newline|'\n'
dedent|''
name|'cls'
op|'.'
name|'_manager'
op|'='
name|'get_manager'
op|'('
name|'cls'
op|')'
newline|'\n'
comment|'# look for all of the Properties and set their names'
nl|'\n'
name|'for'
name|'key'
name|'in'
name|'dict'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'isinstance'
op|'('
name|'dict'
op|'['
name|'key'
op|']'
op|','
name|'Property'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'property'
op|'='
name|'dict'
op|'['
name|'key'
op|']'
newline|'\n'
name|'property'
op|'.'
name|'__property_config__'
op|'('
name|'cls'
op|','
name|'key'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'prop_names'
op|'='
op|'['
op|']'
newline|'\n'
name|'props'
op|'='
name|'cls'
op|'.'
name|'properties'
op|'('
op|')'
newline|'\n'
name|'for'
name|'prop'
name|'in'
name|'props'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'prop'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'prop_names'
op|'.'
name|'append'
op|'('
name|'prop'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'setattr'
op|'('
name|'cls'
op|','
string|"'_prop_names'"
op|','
name|'prop_names'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'NameError'
op|':'
newline|'\n'
comment|"# 'Model' isn't defined yet, meaning we're looking at our own"
nl|'\n'
comment|'# Model class, defined below.'
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|Model
dedent|''
dedent|''
dedent|''
name|'class'
name|'Model'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|__metaclass__
indent|'    '
name|'__metaclass__'
op|'='
name|'ModelMeta'
newline|'\n'
DECL|variable|__consistent__
name|'__consistent__'
op|'='
name|'False'
comment|'# Consistent is set off by default'
newline|'\n'
DECL|variable|id
name|'id'
op|'='
name|'None'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_lineage
name|'def'
name|'get_lineage'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
op|'['
name|'c'
op|'.'
name|'__name__'
name|'for'
name|'c'
name|'in'
name|'cls'
op|'.'
name|'mro'
op|'('
op|')'
op|']'
newline|'\n'
name|'l'
op|'.'
name|'reverse'
op|'('
op|')'
newline|'\n'
name|'return'
string|"'.'"
op|'.'
name|'join'
op|'('
name|'l'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|kind
name|'def'
name|'kind'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_by_id
name|'def'
name|'_get_by_id'
op|'('
name|'cls'
op|','
name|'id'
op|','
name|'manager'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'manager'
op|':'
newline|'\n'
indent|'            '
name|'manager'
op|'='
name|'cls'
op|'.'
name|'_manager'
newline|'\n'
dedent|''
name|'return'
name|'manager'
op|'.'
name|'get_object'
op|'('
name|'cls'
op|','
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_id
name|'def'
name|'get_by_id'
op|'('
name|'cls'
op|','
name|'ids'
op|'='
name|'None'
op|','
name|'parent'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'ids'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'objs'
op|'='
op|'['
name|'cls'
op|'.'
name|'_get_by_id'
op|'('
name|'id'
op|')'
name|'for'
name|'id'
name|'in'
name|'ids'
op|']'
newline|'\n'
name|'return'
name|'objs'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cls'
op|'.'
name|'_get_by_id'
op|'('
name|'ids'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|get_by_ids
dedent|''
dedent|''
name|'get_by_ids'
op|'='
name|'get_by_id'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_by_key_name
name|'def'
name|'get_by_key_name'
op|'('
name|'cls'
op|','
name|'key_names'
op|','
name|'parent'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|','
string|'"Key Names are not currently supported"'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find
name|'def'
name|'find'
op|'('
name|'cls'
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'next_token'
op|'='
name|'None'
op|','
op|'**'
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'q'
op|'='
name|'Query'
op|'('
name|'cls'
op|','
name|'limit'
op|'='
name|'limit'
op|','
name|'next_token'
op|'='
name|'next_token'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'params'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'q'
op|'.'
name|'filter'
op|'('
string|"'%s ='"
op|'%'
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'q'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|lookup
name|'def'
name|'lookup'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'_manager'
op|'.'
name|'lookup'
op|'('
name|'cls'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|all
name|'def'
name|'all'
op|'('
name|'cls'
op|','
name|'limit'
op|'='
name|'None'
op|','
name|'next_token'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'.'
name|'find'
op|'('
name|'limit'
op|'='
name|'limit'
op|','
name|'next_token'
op|'='
name|'next_token'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_or_insert
name|'def'
name|'get_or_insert'
op|'('
name|'key_name'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|','
string|'"get_or_insert not currently supported"'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|properties
name|'def'
name|'properties'
op|'('
name|'cls'
op|','
name|'hidden'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'properties'
op|'='
op|'['
op|']'
newline|'\n'
name|'while'
name|'cls'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'cls'
op|'.'
name|'__dict__'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'prop'
op|'='
name|'cls'
op|'.'
name|'__dict__'
op|'['
name|'key'
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'prop'
op|','
name|'Property'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'hidden'
name|'or'
name|'not'
name|'prop'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'properties'
op|'.'
name|'append'
op|'('
name|'prop'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'cls'
op|'.'
name|'__bases__'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'cls'
op|'='
name|'cls'
op|'.'
name|'__bases__'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'cls'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'properties'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|find_property
name|'def'
name|'find_property'
op|'('
name|'cls'
op|','
name|'prop_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'property'
op|'='
name|'None'
newline|'\n'
name|'while'
name|'cls'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'cls'
op|'.'
name|'__dict__'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'prop'
op|'='
name|'cls'
op|'.'
name|'__dict__'
op|'['
name|'key'
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'prop'
op|','
name|'Property'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'not'
name|'prop'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
name|'and'
name|'prop_name'
op|'=='
name|'prop'
op|'.'
name|'name'
op|':'
newline|'\n'
indent|'                        '
name|'property'
op|'='
name|'prop'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'cls'
op|'.'
name|'__bases__'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'cls'
op|'='
name|'cls'
op|'.'
name|'__bases__'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'cls'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'property'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|get_xmlmanager
name|'def'
name|'get_xmlmanager'
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
string|"'_xmlmanager'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'from'
name|'boto'
op|'.'
name|'sdb'
op|'.'
name|'db'
op|'.'
name|'manager'
op|'.'
name|'xmlmanager'
name|'import'
name|'XMLManager'
newline|'\n'
name|'cls'
op|'.'
name|'_xmlmanager'
op|'='
name|'XMLManager'
op|'('
name|'cls'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|','
name|'False'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_xmlmanager'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_xml
name|'def'
name|'from_xml'
op|'('
name|'cls'
op|','
name|'fp'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xmlmanager'
op|'='
name|'cls'
op|'.'
name|'get_xmlmanager'
op|'('
op|')'
newline|'\n'
name|'return'
name|'xmlmanager'
op|'.'
name|'unmarshal_object'
op|'('
name|'fp'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'id'
op|'='
name|'None'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_loaded'
op|'='
name|'False'
newline|'\n'
comment|'# first initialize all properties to their default values'
nl|'\n'
name|'for'
name|'prop'
name|'in'
name|'self'
op|'.'
name|'properties'
op|'('
name|'hidden'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'prop'
op|'.'
name|'name'
op|','
name|'prop'
op|'.'
name|'default_value'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'kw'
op|'.'
name|'has_key'
op|'('
string|"'manager'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_manager'
op|'='
name|'kw'
op|'['
string|"'manager'"
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'id'
op|'='
name|'id'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'kw'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'key'
op|'!='
string|"'manager'"
op|':'
newline|'\n'
comment|"# We don't want any errors populating up when loading an object,"
nl|'\n'
comment|"# so if it fails we just revert to it's default value"
nl|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'setattr'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'kw'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'e'
op|':'
newline|'\n'
indent|'                    '
name|'boto'
op|'.'
name|'log'
op|'.'
name|'exception'
op|'('
name|'e'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'%s<%s>'"
op|'%'
op|'('
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__eq__
dedent|''
name|'def'
name|'__eq__'
op|'('
name|'self'
op|','
name|'other'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'other'
name|'and'
name|'isinstance'
op|'('
name|'other'
op|','
name|'Model'
op|')'
name|'and'
name|'self'
op|'.'
name|'id'
op|'=='
name|'other'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|_get_raw_item
dedent|''
name|'def'
name|'_get_raw_item'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'get_raw_item'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load
dedent|''
name|'def'
name|'load'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'id'
name|'and'
name|'not'
name|'self'
op|'.'
name|'_loaded'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'load_object'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|put
dedent|''
dedent|''
name|'def'
name|'put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'save_object'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|save
dedent|''
name|'save'
op|'='
name|'put'
newline|'\n'
nl|'\n'
DECL|member|delete
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'delete_object'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|key
dedent|''
name|'def'
name|'key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'Key'
op|'('
name|'obj'
op|'='
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_manager
dedent|''
name|'def'
name|'set_manager'
op|'('
name|'self'
op|','
name|'manager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_manager'
op|'='
name|'manager'
newline|'\n'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'props'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'prop'
name|'in'
name|'self'
op|'.'
name|'properties'
op|'('
name|'hidden'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'props'
op|'['
name|'prop'
op|'.'
name|'name'
op|']'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'prop'
op|'.'
name|'name'
op|')'
newline|'\n'
dedent|''
name|'obj'
op|'='
op|'{'
string|"'properties'"
op|':'
name|'props'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'id'
op|'}'
newline|'\n'
name|'return'
op|'{'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|':'
name|'obj'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|to_xml
dedent|''
name|'def'
name|'to_xml'
op|'('
name|'self'
op|','
name|'doc'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xmlmanager'
op|'='
name|'self'
op|'.'
name|'get_xmlmanager'
op|'('
op|')'
newline|'\n'
name|'doc'
op|'='
name|'xmlmanager'
op|'.'
name|'marshal_object'
op|'('
name|'self'
op|','
name|'doc'
op|')'
newline|'\n'
name|'return'
name|'doc'
newline|'\n'
nl|'\n'
DECL|class|Expando
dedent|''
dedent|''
name|'class'
name|'Expando'
op|'('
name|'Model'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__setattr__
indent|'    '
name|'def'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
name|'in'
name|'self'
op|'.'
name|'_prop_names'
op|':'
newline|'\n'
indent|'            '
name|'object'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'object'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'id'"
op|':'
newline|'\n'
indent|'            '
name|'object'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'set_key_value'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
name|'object'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'name'
op|'.'
name|'startswith'
op|'('
string|"'_'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'self'
op|'.'
name|'_manager'
op|'.'
name|'get_key_value'
op|'('
name|'self'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'value'
op|':'
newline|'\n'
indent|'                '
name|'object'
op|'.'
name|'__setattr__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
name|'return'
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'AttributeError'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
