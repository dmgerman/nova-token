begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""\nClient side of the console RPC API.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
name|'import'
name|'messaging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'rpc'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_opts
name|'rpcapi_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console_topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'console'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The topic console proxy nodes listen on'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'rpcapi_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_opt
name|'rpcapi_cap_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'console'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to console services'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'rpcapi_cap_opt'
op|','
string|"'upgrade_levels'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAPI
name|'class'
name|'ConsoleAPI'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|"'''Client side of the console rpc API.\n\n    API version history:\n\n        1.0 - Initial version.\n        1.1 - Added get_backdoor_port()\n\n        ... Grizzly and Havana support message version 1.1.  So, any changes to\n        existing methods in 1.x after that point should be done such that they\n        can handle the version_cap being set to 1.1.\n\n        2.0 - Major API rev for Icehouse\n    '''"
newline|'\n'
nl|'\n'
DECL|variable|VERSION_ALIASES
name|'VERSION_ALIASES'
op|'='
op|'{'
nl|'\n'
string|"'grizzly'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
string|"'havana'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'topic'
op|'='
name|'None'
op|','
name|'server'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConsoleAPI'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'topic'
op|'='
name|'topic'
name|'if'
name|'topic'
name|'else'
name|'CONF'
op|'.'
name|'console_topic'
newline|'\n'
name|'target'
op|'='
name|'messaging'
op|'.'
name|'Target'
op|'('
name|'topic'
op|'='
name|'topic'
op|','
name|'server'
op|'='
name|'server'
op|','
name|'version'
op|'='
string|"'2.0'"
op|')'
newline|'\n'
name|'version_cap'
op|'='
name|'self'
op|'.'
name|'VERSION_ALIASES'
op|'.'
name|'get'
op|'('
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'console'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'upgrade_levels'
op|'.'
name|'console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'rpc'
op|'.'
name|'get_client'
op|'('
name|'target'
op|','
name|'version_cap'
op|'='
name|'version_cap'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_compat_version
dedent|''
name|'def'
name|'_get_compat_version'
op|'('
name|'self'
op|','
name|'current'
op|','
name|'havana_compat'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'client'
op|'.'
name|'can_send_version'
op|'('
name|'current'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'havana_compat'
newline|'\n'
dedent|''
name|'return'
name|'current'
newline|'\n'
nl|'\n'
DECL|member|add_console
dedent|''
name|'def'
name|'add_console'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'add_console'"
op|','
name|'instance_id'
op|'='
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_console
dedent|''
name|'def'
name|'remove_console'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'console_id'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(russellb) Havana compat'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'self'
op|'.'
name|'_get_compat_version'
op|'('
string|"'2.0'"
op|','
string|"'1.0'"
op|')'
newline|'\n'
name|'cctxt'
op|'='
name|'self'
op|'.'
name|'client'
op|'.'
name|'prepare'
op|'('
name|'version'
op|'='
name|'version'
op|')'
newline|'\n'
name|'cctxt'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
string|"'remove_console'"
op|','
name|'console_id'
op|'='
name|'console_id'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
