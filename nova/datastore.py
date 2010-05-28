begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright [2010] [Anso Labs, LLC]'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""\nDatastore:\n\nProviders the Keeper class, a simple pseudo-dictionary that\npersists on disk.\n\nMAKE Sure that ReDIS is running, and your flags are set properly,\nbefore trying to run this.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sqlite3'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'vendor'
newline|'\n'
name|'import'
name|'redis'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'datastore_path'"
op|','
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'../keeper'"
op|')'
op|','
nl|'\n'
string|"'where keys are stored on disk'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'redis_host'"
op|','
string|"'127.0.0.1'"
op|','
nl|'\n'
string|"'Host that redis is running on.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'redis_port'"
op|','
number|'6379'
op|','
nl|'\n'
string|"'Port that redis is running on.'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'redis_db'"
op|','
number|'0'
op|','
string|"'Multiple DB keeps tests away'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'keeper_backend'"
op|','
string|"'redis'"
op|','
nl|'\n'
string|"'which backend to use for keeper'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Redis
name|'class'
name|'Redis'
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
string|"'Attempted to instantiate singleton'"
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
name|'inst'
op|'='
name|'redis'
op|'.'
name|'Redis'
op|'('
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'redis_host'
op|','
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'redis_port'
op|','
name|'db'
op|'='
name|'FLAGS'
op|'.'
name|'redis_db'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'_instance'
op|'='
name|'inst'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_instance'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RedisModel
dedent|''
dedent|''
name|'class'
name|'RedisModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Wrapper around redis-backed properties """'
newline|'\n'
DECL|variable|object_type
name|'object_type'
op|'='
string|"'generic'"
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'object_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" loads an object from the datastore if exists """'
newline|'\n'
name|'self'
op|'.'
name|'object_id'
op|'='
name|'object_id'
newline|'\n'
name|'self'
op|'.'
name|'initial_state'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'hgetall'
op|'('
name|'self'
op|'.'
name|'__redis_key'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'state'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'initial_state'
op|'='
name|'self'
op|'.'
name|'state'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'set_default_state'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_default_state
dedent|''
dedent|''
name|'def'
name|'set_default_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'state'
op|'='
op|'{'
string|"'state'"
op|':'
string|"'pending'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'['
name|'self'
op|'.'
name|'object_type'
op|'+'
string|'"_id"'
op|']'
op|'='
name|'self'
op|'.'
name|'object_id'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|__redis_key
name|'def'
name|'__redis_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" Magic string for instance keys """'
newline|'\n'
name|'return'
string|"'%s:%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'object_type'
op|','
name|'self'
op|'.'
name|'object_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__repr__
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
string|'"<%s:%s>"'
op|'%'
op|'('
name|'self'
op|'.'
name|'object_type'
op|','
name|'self'
op|'.'
name|'object_id'
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
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|keys
dedent|''
name|'def'
name|'keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'keys'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy
dedent|''
name|'def'
name|'copy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'copyDict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'self'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'copyDict'
op|'['
name|'item'
op|']'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'copyDict'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'.'
name|'get'
op|'('
name|'item'
op|','
name|'default'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
op|'='
name|'val'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state'
op|'['
name|'item'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" We don\'t support this """'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
string|'"Silly monkey, we NEED all our properties."'
op|')'
newline|'\n'
nl|'\n'
DECL|member|save
dedent|''
name|'def'
name|'save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" update the directory with the state from this instance """'
newline|'\n'
comment|'# TODO(ja): implement hmset in redis-py and use it'
nl|'\n'
comment|'# instead of multiple calls to hset'
nl|'\n'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'self'
op|'.'
name|'state'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# if (not self.initial_state.has_key(key)'
nl|'\n'
comment|'# or self.initial_state[key] != val):'
nl|'\n'
indent|'                '
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'hset'
op|'('
name|'self'
op|'.'
name|'__redis_key'
op|','
name|'key'
op|','
name|'val'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'initial_state'
op|'=='
op|'{'
op|'}'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'first_save'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'initial_state'
op|'='
name|'self'
op|'.'
name|'state'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|first_save
dedent|''
name|'def'
name|'first_save'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|destroy
dedent|''
name|'def'
name|'destroy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" deletes all related records from datastore.\n         does NOT do anything to running state.\n        """'
newline|'\n'
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
name|'__redis_key'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|slugify
dedent|''
dedent|''
name|'def'
name|'slugify'
op|'('
name|'key'
op|','
name|'prefix'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Key has to be a valid filename. Slugify solves that.\n    """'
newline|'\n'
name|'return'
string|'"%s%s"'
op|'%'
op|'('
name|'prefix'
op|','
name|'key'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SqliteKeeper
dedent|''
name|'class'
name|'SqliteKeeper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Keeper implementation in SQLite, mostly for in-memory testing """'
newline|'\n'
DECL|variable|_conn
name|'_conn'
op|'='
op|'{'
op|'}'
comment|'# class variable'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'prefix'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'prefix'
op|'='
name|'prefix'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|conn
name|'def'
name|'conn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'prefix'
name|'not'
name|'in'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|"'no sqlite connection (%s), making new'"
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'datastore_path'
op|'!='
string|"':memory:'"
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
name|'conn'
op|'='
name|'sqlite3'
op|'.'
name|'connect'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
string|"'%s.sqlite'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'conn'
op|'='
name|'sqlite3'
op|'.'
name|'connect'
op|'('
string|"':memory:'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'c'
op|'='
name|'conn'
op|'.'
name|'cursor'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'execute'
op|'('
string|"'''CREATE TABLE data (item text, value text)'''"
op|')'
newline|'\n'
name|'conn'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'create table failed'"
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|'['
name|'self'
op|'.'
name|'prefix'
op|']'
op|'='
name|'conn'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|'['
name|'self'
op|'.'
name|'prefix'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
comment|"#logging.debug('sqlite deleting %s', item)"
nl|'\n'
indent|'        '
name|'c'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'cursor'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'.'
name|'execute'
op|'('
string|"'DELETE FROM data WHERE item = ?'"
op|','
op|'('
name|'item'
op|','
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'delete failed: %s'"
op|','
name|'item'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
comment|"#logging.debug('sqlite getting %s', item)"
nl|'\n'
indent|'        '
name|'result'
op|'='
name|'None'
newline|'\n'
name|'c'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'cursor'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'.'
name|'execute'
op|'('
string|"'SELECT value FROM data WHERE item = ?'"
op|','
op|'('
name|'item'
op|','
op|')'
op|')'
newline|'\n'
name|'row'
op|'='
name|'c'
op|'.'
name|'fetchone'
op|'('
op|')'
newline|'\n'
name|'if'
name|'row'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'row'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'select failed: %s'"
op|','
name|'item'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
comment|"#logging.debug('sqlite got %s: %s', item, result)"
nl|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serialized_value'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
newline|'\n'
name|'insert'
op|'='
name|'True'
newline|'\n'
name|'if'
name|'self'
op|'['
name|'item'
op|']'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'insert'
op|'='
name|'False'
newline|'\n'
comment|"#logging.debug('sqlite insert %s: %s', item, value)"
nl|'\n'
dedent|''
name|'c'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'cursor'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'insert'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'execute'
op|'('
string|"'INSERT INTO data VALUES (?, ?)'"
op|','
nl|'\n'
op|'('
name|'item'
op|','
name|'serialized_value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'execute'
op|'('
string|"'UPDATE data SET item=?, value=? WHERE item = ?'"
op|','
nl|'\n'
op|'('
name|'item'
op|','
name|'serialized_value'
op|','
name|'item'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'conn'
op|'.'
name|'commit'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'exception'
op|'('
string|"'select failed: %s'"
op|','
name|'item'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'c'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'prefix'
name|'not'
name|'in'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'datastore_path'
op|'!='
string|"':memory:'"
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
string|"'%s.sqlite'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|')'
newline|'\n'
dedent|''
name|'del'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|'['
name|'self'
op|'.'
name|'prefix'
op|']'
newline|'\n'
nl|'\n'
DECL|member|clear_all
dedent|''
name|'def'
name|'clear_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'conn'
name|'in'
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'conn'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'datastore_path'
op|'!='
string|"':memory:'"
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
nl|'\n'
string|"'%s.sqlite'"
op|'%'
name|'self'
op|'.'
name|'prefix'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'_conn'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|set_add
dedent|''
name|'def'
name|'set_add'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'group'
op|'.'
name|'append'
op|'('
name|'value'
op|')'
newline|'\n'
name|'self'
op|'['
name|'item'
op|']'
op|'='
name|'group'
newline|'\n'
nl|'\n'
DECL|member|set_is_member
dedent|''
name|'def'
name|'set_is_member'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'value'
name|'in'
name|'group'
newline|'\n'
nl|'\n'
DECL|member|set_remove
dedent|''
name|'def'
name|'set_remove'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'group'
op|'.'
name|'remove'
op|'('
name|'value'
op|')'
newline|'\n'
name|'self'
op|'['
name|'item'
op|']'
op|'='
name|'group'
newline|'\n'
nl|'\n'
DECL|member|set_fetch
dedent|''
name|'def'
name|'set_fetch'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
comment|"# TODO(termie): I don't really know what set_fetch is supposed to do"
nl|'\n'
indent|'        '
name|'group'
op|'='
name|'self'
op|'['
name|'item'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'group'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
name|'iter'
op|'('
name|'group'
op|')'
newline|'\n'
nl|'\n'
DECL|class|JsonKeeper
dedent|''
dedent|''
name|'class'
name|'JsonKeeper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Simple dictionary class that persists using\n    JSON in files saved to disk.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'prefix'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'prefix'
op|'='
name|'prefix'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Removing a key means deleting a file from disk.\n        """'
newline|'\n'
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'path'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
name|'item'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'remove'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Fetch file contents and dejsonify them.\n        """'
newline|'\n'
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'path'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
name|'item'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'json'
op|'.'
name|'load'
op|'('
name|'open'
op|'('
name|'path'
op|','
string|"'r'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        JSON encode value and save to file.\n        """'
newline|'\n'
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'path'
op|'='
string|'"%s/%s"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'datastore_path'
op|','
name|'item'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|'"w"'
op|')'
name|'as'
name|'blobfile'
op|':'
newline|'\n'
indent|'            '
name|'blobfile'
op|'.'
name|'write'
op|'('
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RedisKeeper
dedent|''
dedent|''
name|'class'
name|'RedisKeeper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Simple dictionary class that persists using\n    ReDIS.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'prefix'
op|'='
string|'"redis-"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'prefix'
op|'='
name|'prefix'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'ping'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        JSON encode value and save to file.\n        """'
newline|'\n'
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'set'
op|'('
name|'item'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
name|'return'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'value'
op|'='
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'get'
op|'('
name|'item'
op|')'
newline|'\n'
name|'if'
name|'value'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'json'
op|'.'
name|'loads'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__delitem__
dedent|''
dedent|''
name|'def'
name|'__delitem__'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'return'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'delete'
op|'('
name|'item'
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear
dedent|''
name|'def'
name|'clear'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|clear_all
dedent|''
name|'def'
name|'clear_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_add
dedent|''
name|'def'
name|'set_add'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'return'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sadd'
op|'('
name|'item'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_is_member
dedent|''
name|'def'
name|'set_is_member'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'return'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sismember'
op|'('
name|'item'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_remove
dedent|''
name|'def'
name|'set_remove'
op|'('
name|'self'
op|','
name|'item'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'return'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'srem'
op|'('
name|'item'
op|','
name|'json'
op|'.'
name|'dumps'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_fetch
dedent|''
name|'def'
name|'set_fetch'
op|'('
name|'self'
op|','
name|'item'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'item'
op|'='
name|'slugify'
op|'('
name|'item'
op|','
name|'self'
op|'.'
name|'prefix'
op|')'
newline|'\n'
name|'for'
name|'obj'
name|'in'
name|'Redis'
op|'.'
name|'instance'
op|'('
op|')'
op|'.'
name|'sinter'
op|'('
op|'['
name|'item'
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'yield'
name|'json'
op|'.'
name|'loads'
op|'('
name|'obj'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|Keeper
dedent|''
dedent|''
dedent|''
name|'def'
name|'Keeper'
op|'('
name|'prefix'
op|'='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'KEEPERS'
op|'='
op|'{'
string|"'redis'"
op|':'
name|'RedisKeeper'
op|','
nl|'\n'
string|"'sqlite'"
op|':'
name|'SqliteKeeper'
op|'}'
newline|'\n'
name|'return'
name|'KEEPERS'
op|'['
name|'FLAGS'
op|'.'
name|'keeper_backend'
op|']'
op|'('
name|'prefix'
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
