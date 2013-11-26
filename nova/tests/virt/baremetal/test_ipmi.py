begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""Test class for baremetal IPMI power manager."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'stat'
newline|'\n'
name|'import'
name|'tempfile'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'utils'
name|'as'
name|'bm_db_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'ipmi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'utils'
name|'as'
name|'bm_utils'
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
nl|'\n'
DECL|class|BareMetalIPMITestCase
name|'class'
name|'BareMetalIPMITestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
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
name|'BareMetalIPMITestCase'
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
name|'node'
op|'='
name|'bm_db_utils'
op|'.'
name|'new_bm_node'
op|'('
nl|'\n'
name|'id'
op|'='
number|'123'
op|','
nl|'\n'
name|'pm_address'
op|'='
string|"'fake-address'"
op|','
nl|'\n'
name|'pm_user'
op|'='
string|"'fake-user'"
op|','
nl|'\n'
name|'pm_password'
op|'='
string|"'fake-password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'='
name|'ipmi'
op|'.'
name|'IPMI'
op|'('
name|'self'
op|'.'
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_construct
dedent|''
name|'def'
name|'test_construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'address'
op|','
string|"'fake-address'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'user'
op|','
string|"'fake-user'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'password'
op|','
string|"'fake-password'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_make_password_file
dedent|''
name|'def'
name|'test_make_password_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pw_file'
op|'='
name|'ipmi'
op|'.'
name|'_make_password_file'
op|'('
name|'self'
op|'.'
name|'node'
op|'['
string|"'pm_password'"
op|']'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'pw_file'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'os'
op|'.'
name|'stat'
op|'('
name|'pw_file'
op|')'
op|'['
name|'stat'
op|'.'
name|'ST_MODE'
op|']'
op|'&'
number|'0o777'
op|','
number|'0o600'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'pw_file'
op|','
string|'"r"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'pm_password'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pm_password'
op|','
name|'self'
op|'.'
name|'node'
op|'['
string|"'pm_password'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'pw_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_make_empty_password_file
dedent|''
dedent|''
name|'def'
name|'test_make_empty_password_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pw_file'
op|'='
name|'ipmi'
op|'.'
name|'_make_password_file'
op|'('
string|"''"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'isfile'
op|'('
name|'pw_file'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'os'
op|'.'
name|'stat'
op|'('
name|'pw_file'
op|')'
op|'['
name|'stat'
op|'.'
name|'ST_MODE'
op|']'
op|'&'
number|'0o777'
op|','
number|'0o600'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'pw_file'
op|','
string|'"rb"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'pm_password'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'b"\\0"'
op|','
name|'pm_password'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'pw_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exec_ipmitool
dedent|''
dedent|''
name|'def'
name|'test_exec_ipmitool'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pw_file'
op|'='
string|"'/tmp/password_file'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ipmi'
op|','
string|"'_make_password_file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'unlink_without_raise'"
op|')'
newline|'\n'
name|'ipmi'
op|'.'
name|'_make_password_file'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'password'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'pw_file'
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
nl|'\n'
string|"'ipmitool'"
op|','
nl|'\n'
string|"'-I'"
op|','
string|"'lanplus'"
op|','
nl|'\n'
string|"'-H'"
op|','
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'-U'"
op|','
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'user'
op|','
nl|'\n'
string|"'-f'"
op|','
name|'pw_file'
op|','
nl|'\n'
string|"'A'"
op|','
string|"'B'"
op|','
string|"'C'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
name|'attempts'
op|'='
number|'3'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
string|"''"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'pw_file'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|"'A B C'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_power_on_ok
dedent|''
name|'def'
name|'test_is_power_on_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is on\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'is_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_power_no_answer
dedent|''
name|'def'
name|'test_is_power_no_answer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Fake reply\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'is_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'res'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_already_on
dedent|''
name|'def'
name|'test_power_already_on'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ipmi_power_retry'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is on\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_ok
dedent|''
name|'def'
name|'test_power_on_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ipmi_power_retry'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power on"'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is on\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_fail
dedent|''
name|'def'
name|'test_power_on_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ipmi_power_retry'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power on"'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_max_retries
dedent|''
name|'def'
name|'test_power_on_max_retries'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ipmi_power_retry'
op|'='
number|'2'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power on"'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'retries'
op|','
number|'3'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_off_ok
dedent|''
name|'def'
name|'test_power_off_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ipmi_power_retry'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|','
string|"'_exec_ipmitool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is on\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power off"'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'['
string|'"Chassis Power is off\\n"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'_power_off'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'DELETED'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_pid_path
dedent|''
name|'def'
name|'test_get_console_pid_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'terminal_pid_dir'
op|'='
string|"'/tmp'"
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'path'
op|'='
name|'ipmi'
op|'.'
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'path'
op|','
string|"'/tmp/%s.pid'"
op|'%'
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_pid
dedent|''
name|'def'
name|'test_console_pid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fd'
op|','
name|'path'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'with'
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'fd'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
string|'"12345\\n"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ipmi'
op|','
string|"'_get_console_pid_path'"
op|')'
newline|'\n'
name|'ipmi'
op|'.'
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'pid'
op|'='
name|'ipmi'
op|'.'
name|'_get_console_pid'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pid'
op|','
number|'12345'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_pid_nan
dedent|''
name|'def'
name|'test_console_pid_nan'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fd'
op|','
name|'path'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'with'
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'fd'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
string|'"hello world\\n"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'ipmi'
op|','
string|"'_get_console_pid_path'"
op|')'
newline|'\n'
name|'ipmi'
op|'.'
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'pid'
op|'='
name|'ipmi'
op|'.'
name|'_get_console_pid'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'pid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_console_pid_file_not_found
dedent|''
name|'def'
name|'test_console_pid_file_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pid_path'
op|'='
name|'ipmi'
op|'.'
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'exists'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pid_path'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'pid'
op|'='
name|'ipmi'
op|'.'
name|'_get_console_pid'
op|'('
name|'self'
op|'.'
name|'ipmi'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'pid'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
