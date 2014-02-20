begin_unit
comment|'# Copyright 2014 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright 2012 University Of Minho'
nl|'\n'
comment|'# Copyright 2010 OpenStack Foundation'
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
string|'"""\nTests fot virt volumeutils.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
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
name|'import'
name|'volumeutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeUtilsTestCase
name|'class'
name|'VolumeUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_iscsi_initiator
indent|'    '
name|'def'
name|'test_get_iscsi_initiator'
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
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'initiator'
op|'='
string|"'fake.initiator.iqn'"
newline|'\n'
name|'rval'
op|'='
op|'('
string|'"junk\\nInitiatorName=%s\\njunk\\n"'
op|'%'
name|'initiator'
op|','
name|'None'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cat'"
op|','
string|"'/etc/iscsi/initiatorname.iscsi'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'rval'
op|')'
newline|'\n'
comment|'# Start test'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'volumeutils'
op|'.'
name|'get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'initiator'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_missing_iscsi_initiator
dedent|''
name|'def'
name|'test_get_missing_iscsi_initiator'
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
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'file_path'
op|'='
string|"'/etc/iscsi/initiatorname.iscsi'"
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cat'"
op|','
name|'file_path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'FileNotFound'
op|'('
name|'file_path'
op|'='
name|'file_path'
op|')'
nl|'\n'
op|')'
newline|'\n'
comment|'# Start test'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'volumeutils'
op|'.'
name|'get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'result'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
