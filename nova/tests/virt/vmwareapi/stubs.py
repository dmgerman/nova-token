begin_unit
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nStubouts for the test suite\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'network_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'vmware_images'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_vim_object
name|'def'
name|'fake_get_vim_object'
op|'('
name|'arg'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out the VMwareAPISession\'s get_vim_object method."""'
newline|'\n'
name|'return'
name|'fake'
op|'.'
name|'FakeVim'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_is_vim_object
dedent|''
name|'def'
name|'fake_is_vim_object'
op|'('
name|'arg'
op|','
name|'module'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out the VMwareAPISession\'s is_vim_object method."""'
newline|'\n'
name|'return'
name|'isinstance'
op|'('
name|'module'
op|','
name|'fake'
op|'.'
name|'FakeVim'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_temp_method_exception
dedent|''
name|'def'
name|'fake_temp_method_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'error_util'
op|'.'
name|'VimFaultException'
op|'('
nl|'\n'
op|'['
name|'error_util'
op|'.'
name|'FAULT_NOT_AUTHENTICATED'
op|']'
op|','
nl|'\n'
string|'"Session Empty/Not Authenticated"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_temp_session_exception
dedent|''
name|'def'
name|'fake_temp_session_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'error_util'
op|'.'
name|'SessionConnectionException'
op|'('
op|'['
op|']'
op|','
nl|'\n'
string|'"Session Exception"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|set_stubs
dedent|''
name|'def'
name|'set_stubs'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Set the stubs."""'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'network_util'
op|','
string|"'get_network_with_the_name'"
op|','
nl|'\n'
name|'fake'
op|'.'
name|'fake_get_network'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'fetch_image'"
op|','
name|'fake'
op|'.'
name|'fake_fetch_image'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'get_vmdk_size_and_properties'"
op|','
nl|'\n'
name|'fake'
op|'.'
name|'fake_get_vmdk_size_and_properties'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmware_images'
op|','
string|"'upload_image'"
op|','
name|'fake'
op|'.'
name|'fake_upload_image'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|'.'
name|'VMwareAPISession'
op|','
string|'"_get_vim_object"'
op|','
nl|'\n'
name|'fake_get_vim_object'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'driver'
op|'.'
name|'VMwareAPISession'
op|','
string|'"_is_vim_object"'
op|','
nl|'\n'
name|'fake_is_vim_object'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
