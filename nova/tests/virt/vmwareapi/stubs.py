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
name|'import'
name|'contextlib'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'NOT_AUTHENTICATED'
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
DECL|function|fake_session_file_exception
dedent|''
name|'def'
name|'fake_session_file_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fault_list'
op|'='
op|'['
name|'error_util'
op|'.'
name|'FILE_ALREADY_EXISTS'
op|']'
newline|'\n'
name|'raise'
name|'error_util'
op|'.'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
nl|'\n'
name|'Exception'
op|'('
string|"'fake'"
op|')'
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
nl|'\n'
nl|'\n'
DECL|function|fake_suds_context
dedent|''
name|'def'
name|'fake_suds_context'
op|'('
name|'calls'
op|'='
op|'{'
op|'}'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Generate a suds client which automatically mocks all SOAP method calls.\n\n    Calls are stored in <calls>, indexed by the name of the call. If you need\n    to mock the behaviour of specific API calls you can pre-populate <calls>\n    with appropriate Mock objects.\n    """'
newline|'\n'
nl|'\n'
DECL|class|fake_factory
name|'class'
name|'fake_factory'
op|':'
newline|'\n'
DECL|member|create
indent|'        '
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'mock'
op|'.'
name|'NonCallableMagicMock'
op|'('
name|'name'
op|'='
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|class|fake_service
dedent|''
dedent|''
name|'class'
name|'fake_service'
op|':'
newline|'\n'
DECL|member|__getattr__
indent|'        '
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr_name'
name|'in'
name|'calls'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'calls'
op|'['
name|'attr_name'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_call'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'name'
op|'='
name|'attr_name'
op|')'
newline|'\n'
name|'calls'
op|'['
name|'attr_name'
op|']'
op|'='
name|'mock_call'
newline|'\n'
name|'return'
name|'mock_call'
newline|'\n'
nl|'\n'
DECL|class|fake_client
dedent|''
dedent|''
name|'class'
name|'fake_client'
op|':'
newline|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'wdsl_url'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'service'
op|'='
name|'fake_service'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'factory'
op|'='
name|'fake_factory'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'suds.client.Client'"
op|','
name|'fake_client'
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# As we're not connecting to a real host there's no need to wait"
nl|'\n'
comment|'# between retries'
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'driver'
op|','
string|"'TIME_BETWEEN_API_CALL_RETRIES'"
op|','
number|'0'
op|')'
nl|'\n'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
