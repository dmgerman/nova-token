begin_unit
comment|'# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
comment|'# TODO(mikal): move eventlet imports to nova.__init__ once we move to PBR'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
comment|'# NOTE(mikal): All of this is because if dnspython is present in your'
nl|'\n'
comment|'# environment then eventlet monkeypatches socket.getaddrinfo() with an'
nl|'\n'
comment|"# implementation which doesn't work for IPv6. What we're checking here is"
nl|'\n'
comment|'# that the magic environment variable was set when the import happened.'
nl|'\n'
name|'if'
op|'('
string|"'eventlet'"
name|'in'
name|'sys'
op|'.'
name|'modules'
name|'and'
nl|'\n'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'EVENTLET_NO_GREENDNS'"
op|','
string|"''"
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'!='
string|"'yes'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'ImportError'
op|'('
string|"'eventlet imported before nova/cmd/__init__ '"
nl|'\n'
string|"'(env var set to %s)'"
nl|'\n'
op|'%'
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'EVENTLET_NO_GREENDNS'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'os'
op|'.'
name|'environ'
op|'['
string|"'EVENTLET_NO_GREENDNS'"
op|']'
op|'='
string|"'yes'"
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
nl|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
name|'os'
op|'='
name|'False'
op|')'
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
name|'gettextutils'
op|'.'
name|'enable_lazy'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
