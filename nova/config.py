begin_unit
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'from'
name|'oslo_cache'
name|'import'
name|'core'
name|'as'
name|'cache'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_db'
name|'import'
name|'options'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'common'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
op|'.'
name|'sqlalchemy'
name|'import'
name|'api'
name|'as'
name|'sqlalchemy_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'debugger'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'paths'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
DECL|variable|_DEFAULT_SQL_CONNECTION
name|'_DEFAULT_SQL_CONNECTION'
op|'='
string|"'sqlite:///'"
op|'+'
name|'paths'
op|'.'
name|'state_path_def'
op|'('
string|"'nova.sqlite'"
op|')'
newline|'\n'
nl|'\n'
name|'_EXTRA_DEFAULT_LOG_LEVELS'
op|'='
op|'['
string|"'glanceclient=WARN'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_args
name|'def'
name|'parse_args'
op|'('
name|'argv'
op|','
name|'default_config_files'
op|'='
name|'None'
op|','
name|'configure_db'
op|'='
name|'True'
op|','
nl|'\n'
name|'init_rpc'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'log'
op|'.'
name|'register_options'
op|'('
name|'CONF'
op|')'
newline|'\n'
comment|'# We use the oslo.log default log levels which includes suds=INFO'
nl|'\n'
comment|'# and add only the extra levels that Nova needs'
nl|'\n'
name|'log'
op|'.'
name|'set_defaults'
op|'('
name|'default_log_levels'
op|'='
name|'log'
op|'.'
name|'get_default_log_levels'
op|'('
op|')'
op|'+'
nl|'\n'
name|'_EXTRA_DEFAULT_LOG_LEVELS'
op|')'
newline|'\n'
name|'options'
op|'.'
name|'set_defaults'
op|'('
name|'CONF'
op|','
name|'connection'
op|'='
name|'_DEFAULT_SQL_CONNECTION'
op|','
nl|'\n'
name|'sqlite_db'
op|'='
string|"'nova.sqlite'"
op|')'
newline|'\n'
name|'rpc'
op|'.'
name|'set_defaults'
op|'('
name|'control_exchange'
op|'='
string|"'nova'"
op|')'
newline|'\n'
name|'cache'
op|'.'
name|'configure'
op|'('
name|'CONF'
op|')'
newline|'\n'
name|'debugger'
op|'.'
name|'register_cli_opts'
op|'('
op|')'
newline|'\n'
name|'config'
op|'.'
name|'set_middleware_defaults'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'CONF'
op|'('
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|','
nl|'\n'
name|'project'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'version'
op|'='
name|'version'
op|'.'
name|'version_string'
op|'('
op|')'
op|','
nl|'\n'
name|'default_config_files'
op|'='
name|'default_config_files'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'init_rpc'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'.'
name|'init'
op|'('
name|'CONF'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'configure_db'
op|':'
newline|'\n'
indent|'        '
name|'sqlalchemy_api'
op|'.'
name|'configure'
op|'('
name|'CONF'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
