begin_unit
comment|'#  Copyright 2013 Cloudbase Solutions Srl'
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
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'rdpconsoleutilsv2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RDPConsoleUtilsV2TestCase
name|'class'
name|'RDPConsoleUtilsV2TestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|_FAKE_RDP_PORT
indent|'    '
name|'_FAKE_RDP_PORT'
op|'='
number|'1000'
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
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'='
name|'rdpconsoleutilsv2'
op|'.'
name|'RDPConsoleUtilsV2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'.'
name|'_conn'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'RDPConsoleUtilsV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_rdp_console_port
dedent|''
name|'def'
name|'test_get_rdp_console_port'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'conn'
op|'='
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'.'
name|'_conn'
newline|'\n'
name|'mock_rdp_setting_data'
op|'='
name|'conn'
op|'.'
name|'Msvm_TerminalServiceSettingData'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_rdp_setting_data'
op|'.'
name|'ListenerPort'
op|'='
name|'self'
op|'.'
name|'_FAKE_RDP_PORT'
newline|'\n'
nl|'\n'
name|'listener_port'
op|'='
name|'self'
op|'.'
name|'_rdpconsoleutils'
op|'.'
name|'get_rdp_console_port'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_FAKE_RDP_PORT'
op|','
name|'listener_port'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
