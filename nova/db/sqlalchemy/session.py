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
string|'"""\nSession Handling for SQLAlchemy backend\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'patcher'
newline|'\n'
name|'eventlet'
op|'.'
name|'patcher'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
op|'.'
name|'db_pool'
newline|'\n'
name|'import'
name|'sqlalchemy'
op|'.'
name|'orm'
newline|'\n'
name|'import'
name|'sqlalchemy'
op|'.'
name|'pool'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'log'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'nova'
op|'.'
name|'log'
op|'.'
name|'getLogger'
op|'('
string|'"nova.db.sqlalchemy"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'MySQLdb'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|MySQLdb
indent|'    '
name|'MySQLdb'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_ENGINE
dedent|''
name|'_ENGINE'
op|'='
name|'None'
newline|'\n'
DECL|variable|_MAKER
name|'_MAKER'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_session
name|'def'
name|'get_session'
op|'('
name|'autocommit'
op|'='
name|'True'
op|','
name|'expire_on_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy session."""'
newline|'\n'
name|'global'
name|'_ENGINE'
op|','
name|'_MAKER'
newline|'\n'
nl|'\n'
name|'if'
name|'_MAKER'
name|'is'
name|'None'
name|'or'
name|'_ENGINE'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'_ENGINE'
op|'='
name|'get_engine'
op|'('
op|')'
newline|'\n'
name|'_MAKER'
op|'='
name|'get_maker'
op|'('
name|'_ENGINE'
op|','
name|'autocommit'
op|','
name|'expire_on_commit'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'session'
op|'='
name|'_MAKER'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'query'
op|'='
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'wrap_db_error'
op|'('
name|'session'
op|'.'
name|'query'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'flush'
op|'='
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'wrap_db_error'
op|'('
name|'session'
op|'.'
name|'flush'
op|')'
newline|'\n'
name|'return'
name|'session'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_engine
dedent|''
name|'def'
name|'get_engine'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy engine."""'
newline|'\n'
name|'connection_dict'
op|'='
name|'sqlalchemy'
op|'.'
name|'engine'
op|'.'
name|'url'
op|'.'
name|'make_url'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|')'
newline|'\n'
nl|'\n'
name|'engine_args'
op|'='
op|'{'
nl|'\n'
string|'"pool_recycle"'
op|':'
name|'FLAGS'
op|'.'
name|'sql_idle_timeout'
op|','
nl|'\n'
string|'"echo"'
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
string|'"sqlite"'
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'        '
name|'engine_args'
op|'['
string|'"poolclass"'
op|']'
op|'='
name|'sqlalchemy'
op|'.'
name|'pool'
op|'.'
name|'NullPool'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'MySQLdb'
name|'and'
string|'"mysql"'
name|'in'
name|'connection_dict'
op|'.'
name|'drivername'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Using mysql/eventlet db_pool."'
op|')'
op|')'
newline|'\n'
name|'pool_args'
op|'='
op|'{'
nl|'\n'
string|'"db"'
op|':'
name|'connection_dict'
op|'.'
name|'database'
op|','
nl|'\n'
string|'"passwd"'
op|':'
name|'connection_dict'
op|'.'
name|'password'
op|','
nl|'\n'
string|'"host"'
op|':'
name|'connection_dict'
op|'.'
name|'host'
op|','
nl|'\n'
string|'"user"'
op|':'
name|'connection_dict'
op|'.'
name|'username'
op|','
nl|'\n'
string|'"min_size"'
op|':'
name|'FLAGS'
op|'.'
name|'sql_min_pool_size'
op|','
nl|'\n'
string|'"max_size"'
op|':'
name|'FLAGS'
op|'.'
name|'sql_max_pool_size'
op|','
nl|'\n'
string|'"max_idle"'
op|':'
name|'FLAGS'
op|'.'
name|'sql_idle_timeout'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'creator'
op|'='
name|'eventlet'
op|'.'
name|'db_pool'
op|'.'
name|'ConnectionPool'
op|'('
name|'MySQLdb'
op|','
op|'**'
name|'pool_args'
op|')'
newline|'\n'
name|'engine_args'
op|'['
string|'"pool_size"'
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'sql_max_pool_size'
newline|'\n'
name|'engine_args'
op|'['
string|'"pool_timeout"'
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'sql_pool_timeout'
newline|'\n'
name|'engine_args'
op|'['
string|'"creator"'
op|']'
op|'='
name|'creator'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'sqlalchemy'
op|'.'
name|'create_engine'
op|'('
name|'FLAGS'
op|'.'
name|'sql_connection'
op|','
op|'**'
name|'engine_args'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_maker
dedent|''
name|'def'
name|'get_maker'
op|'('
name|'engine'
op|','
name|'autocommit'
op|'='
name|'True'
op|','
name|'expire_on_commit'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a SQLAlchemy sessionmaker using the given engine."""'
newline|'\n'
name|'return'
name|'sqlalchemy'
op|'.'
name|'orm'
op|'.'
name|'sessionmaker'
op|'('
name|'bind'
op|'='
name|'engine'
op|','
nl|'\n'
name|'autocommit'
op|'='
name|'autocommit'
op|','
nl|'\n'
name|'expire_on_commit'
op|'='
name|'expire_on_commit'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
