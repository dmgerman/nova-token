begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 United States Government as represented by the'
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
nl|'\n'
string|'"""Unit tests for `nova.wsgi`."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLoaderNothingExists
name|'class'
name|'TestLoaderNothingExists'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Loader tests where os.path.exists always returns False."""'
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
name|'TestLoaderNothingExists'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|','
name|'lambda'
name|'_'
op|':'
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_not_found
dedent|''
name|'def'
name|'test_config_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'ConfigNotFound'
op|','
nl|'\n'
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Loader'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestLoaderNormalFilesystem
dedent|''
dedent|''
name|'class'
name|'TestLoaderNormalFilesystem'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Loader tests with normal filesystem (unmodified os.path module)."""'
newline|'\n'
nl|'\n'
name|'_paste_config'
op|'='
string|'"""\n[app:test_app]\nuse = egg:Paste#static\ndocument_root = /tmp\n    """'
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
name|'TestLoaderNormalFilesystem'
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
name|'config'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
name|'mode'
op|'='
string|'"w+t"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'write'
op|'('
name|'self'
op|'.'
name|'_paste_config'
op|'.'
name|'lstrip'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'seek'
op|'('
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loader'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Loader'
op|'('
name|'self'
op|'.'
name|'config'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_config_found
dedent|''
name|'def'
name|'test_config_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'config'
op|'.'
name|'name'
op|','
name|'self'
op|'.'
name|'loader'
op|'.'
name|'config_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_app_not_found
dedent|''
name|'def'
name|'test_app_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'nova'
op|'.'
name|'exception'
op|'.'
name|'PasteAppNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|','
nl|'\n'
string|'"nonexistent app"'
op|','
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_app_found
dedent|''
name|'def'
name|'test_app_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url_parser'
op|'='
name|'self'
op|'.'
name|'loader'
op|'.'
name|'load_app'
op|'('
string|'"test_app"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"/tmp"'
op|','
name|'url_parser'
op|'.'
name|'directory'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'config'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'TestLoaderNormalFilesystem'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestWSGIServer
dedent|''
dedent|''
name|'class'
name|'TestWSGIServer'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI server tests."""'
newline|'\n'
nl|'\n'
DECL|member|test_no_app
name|'def'
name|'test_no_app'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_app"'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"test_app"'
op|','
name|'server'
op|'.'
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_random_port
dedent|''
name|'def'
name|'test_start_random_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_random_port"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"127.0.0.1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'server'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_random_port_with_ipv6
dedent|''
name|'def'
name|'test_start_random_port_with_ipv6'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"test_random_port"'
op|','
name|'None'
op|','
nl|'\n'
name|'host'
op|'='
string|'"::1"'
op|','
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"::1"'
op|','
name|'server'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
number|'0'
op|','
name|'server'
op|'.'
name|'port'
op|')'
newline|'\n'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'server'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
