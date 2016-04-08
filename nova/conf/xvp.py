begin_unit
comment|'# Copyright 2016 OpenStack Foundation'
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
name|'from'
name|'nova'
op|'.'
name|'conf'
name|'import'
name|'paths'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|xvp_group
name|'xvp_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
nl|'\n'
string|"'xvp'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'XVP options'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|xvp_opts
name|'xvp_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_xvp_conf_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'paths'
op|'.'
name|'basedir_def'
op|'('
string|"'nova/console/xvp.conf.template'"
op|')'
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'XVP conf template'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_xvp_conf'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/etc/xvp.conf'"
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Generated XVP conf file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_xvp_pid'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/var/run/xvp.pid'"
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'XVP master process pid file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_xvp_log'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/var/log/xvp.log'"
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'XVP log file'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'console_xvp_multiplex_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5900'
op|','
nl|'\n'
DECL|variable|deprecated_group
name|'deprecated_group'
op|'='
string|"'DEFAULT'"
op|','
nl|'\n'
DECL|variable|min
name|'min'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|max
name|'max'
op|'='
number|'65535'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Port for XVP to multiplex VNC connections on'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_group'
op|'('
name|'xvp_group'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'xvp_opts'
op|','
name|'group'
op|'='
name|'xvp_group'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
name|'xvp_group'
op|':'
name|'xvp_opts'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit