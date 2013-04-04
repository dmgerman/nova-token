begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
string|'"""Starter script for Nova Console Proxy."""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'service'
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
name|'import_opt'
op|'('
string|"'console_topic'"
op|','
string|"'nova.console.rpcapi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'setup'
op|'('
string|'"nova"'
op|')'
newline|'\n'
name|'server'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-console'"
op|','
nl|'\n'
name|'topic'
op|'='
name|'CONF'
op|'.'
name|'console_topic'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'serve'
op|'('
name|'server'
op|')'
newline|'\n'
name|'service'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
