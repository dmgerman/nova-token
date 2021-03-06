begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'console'
name|'import'
name|'manager'
name|'as'
name|'console_manager'
comment|'# noqa - only for cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'test_servers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesSamplesJsonTest
name|'class'
name|'ConsolesSamplesJsonTest'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_dir
indent|'    '
name|'sample_dir'
op|'='
string|'"consoles"'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConsolesSamplesJsonTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'console_public_hostname'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'console_host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'console_driver'
op|'='
string|"'nova.console.fake.FakeConsoleProxy'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'console'
op|'='
name|'self'
op|'.'
name|'start_service'
op|'('
string|"'console'"
op|','
name|'host'
op|'='
string|"'fake'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_consoles
dedent|''
name|'def'
name|'_create_consoles'
op|'('
name|'self'
op|','
name|'server_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/consoles'"
op|'%'
name|'server_uuid'
op|','
nl|'\n'
string|"'consoles-create-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_consoles
dedent|''
name|'def'
name|'test_create_consoles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_consoles'
op|'('
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_consoles
dedent|''
name|'def'
name|'test_list_consoles'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_consoles'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/consoles'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'consoles-list-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_get
dedent|''
name|'def'
name|'test_console_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_consoles'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'servers/%s/consoles/1'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'consoles-get-resp'"
op|','
op|'{'
op|'}'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_delete
dedent|''
name|'def'
name|'test_console_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_consoles'
op|'('
name|'uuid'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_delete'
op|'('
string|"'servers/%s/consoles/1'"
op|'%'
name|'uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
