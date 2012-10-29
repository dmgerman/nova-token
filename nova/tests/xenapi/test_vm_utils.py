begin_unit
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'driver'
name|'as'
name|'xenapi_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'volume_utils'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetInstanceForVdisForSrTestCase
name|'class'
name|'GetInstanceForVdisForSrTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBase'
op|')'
op|':'
newline|'\n'
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
name|'GetInstanceForVdisForSrTestCase'
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
name|'disable_process_locking'
op|'='
name|'True'
op|','
nl|'\n'
name|'instance_name_template'
op|'='
string|"'%d'"
op|','
nl|'\n'
name|'firewall_driver'
op|'='
string|"'nova.virt.xenapi.firewall.'"
nl|'\n'
string|"'Dom0IptablesFirewallDriver'"
op|','
nl|'\n'
name|'xenapi_connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
op|','
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_vdis_for_sr
dedent|''
name|'def'
name|'test_get_instance_vdis_for_sr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
name|'fake'
op|'.'
name|'create_vm'
op|'('
string|'"foo"'
op|','
string|'"Running"'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'fake'
op|'.'
name|'create_sr'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'vdi_1'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
string|"'vdiname1'"
op|','
name|'sr_ref'
op|')'
newline|'\n'
name|'vdi_2'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
string|"'vdiname2'"
op|','
name|'sr_ref'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'vdi_ref'
name|'in'
op|'['
name|'vdi_1'
op|','
name|'vdi_2'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'fake'
op|'.'
name|'create_vbd'
op|'('
name|'vm_ref'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'list'
op|'('
name|'vm_utils'
op|'.'
name|'get_instance_vdis_for_sr'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'sr_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
name|'vdi_1'
op|','
name|'vdi_2'
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_instance_vdis_for_sr_no_vbd
dedent|''
name|'def'
name|'test_get_instance_vdis_for_sr_no_vbd'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_ref'
op|'='
name|'fake'
op|'.'
name|'create_vm'
op|'('
string|'"foo"'
op|','
string|'"Running"'
op|')'
newline|'\n'
name|'sr_ref'
op|'='
name|'fake'
op|'.'
name|'create_sr'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'list'
op|'('
name|'vm_utils'
op|'.'
name|'get_instance_vdis_for_sr'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'_session'
op|','
name|'vm_ref'
op|','
name|'sr_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
op|'['
op|']'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vdis_for_boot_from_vol
dedent|''
name|'def'
name|'test_get_vdis_for_boot_from_vol'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_params'
op|'='
op|'{'
string|"'sr_uuid'"
op|':'
string|"'falseSR'"
op|','
nl|'\n'
string|"'name_label'"
op|':'
string|"'fake_storage'"
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"'test purposes'"
op|','
nl|'\n'
string|"'server'"
op|':'
string|"'myserver'"
op|','
nl|'\n'
string|"'serverpath'"
op|':'
string|"'/local/scratch/myname'"
op|','
nl|'\n'
string|"'sr_type'"
op|':'
string|"'nfs'"
op|','
nl|'\n'
string|"'introduce_sr_keys'"
op|':'
op|'['
string|"'server'"
op|','
string|"'serverpath'"
op|','
string|"'sr_type'"
op|']'
op|','
nl|'\n'
string|"'vdi_uuid'"
op|':'
string|"'falseVDI'"
op|'}'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'vm_utils'
op|'.'
name|'get_vdis_for_boot_from_vol'
op|'('
name|'driver'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'dev_params'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'result'
op|'['
string|"'root'"
op|']'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'falseVDI'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vdis_for_boot_from_vol_failure
dedent|''
name|'def'
name|'test_get_vdis_for_boot_from_vol_failure'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|function|bad_introduce_sr
name|'def'
name|'bad_introduce_sr'
op|'('
name|'session'
op|','
name|'sr_uuid'
op|','
name|'label'
op|','
name|'sr_params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_utils'
op|','
string|"'introduce_sr'"
op|','
name|'bad_introduce_sr'
op|')'
newline|'\n'
name|'dev_params'
op|'='
op|'{'
string|"'sr_uuid'"
op|':'
string|"'falseSR'"
op|','
nl|'\n'
string|"'name_label'"
op|':'
string|"'fake_storage'"
op|','
nl|'\n'
string|"'name_description'"
op|':'
string|"'test purposes'"
op|','
nl|'\n'
string|"'server'"
op|':'
string|"'myserver'"
op|','
nl|'\n'
string|"'serverpath'"
op|':'
string|"'/local/scratch/myname'"
op|','
nl|'\n'
string|"'sr_type'"
op|':'
string|"'nfs'"
op|','
nl|'\n'
string|"'introduce_sr_keys'"
op|':'
op|'['
string|"'server'"
op|','
string|"'serverpath'"
op|','
string|"'sr_type'"
op|']'
op|','
nl|'\n'
string|"'vdi_uuid'"
op|':'
string|"'falseVDI'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'vm_utils'
op|'.'
name|'get_vdis_for_boot_from_vol'
op|','
nl|'\n'
name|'driver'
op|'.'
name|'_session'
op|','
name|'dev_params'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMRefOrRaiseVMFoundTestCase
dedent|''
dedent|''
name|'class'
name|'VMRefOrRaiseVMFoundTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_lookup_call
indent|'    '
name|'def'
name|'test_lookup_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'ignored'"
op|')'
newline|'\n'
nl|'\n'
name|'mock'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_return_value
dedent|''
name|'def'
name|'test_return_value'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'vmref'"
op|')'
newline|'\n'
nl|'\n'
name|'mock'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
nl|'\n'
string|"'vmref'"
op|','
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMRefOrRaiseVMNotFoundTestCase
dedent|''
dedent|''
name|'class'
name|'VMRefOrRaiseVMNotFoundTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_exception_raised
indent|'    '
name|'def'
name|'test_exception_raised'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'mock'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|','
nl|'\n'
name|'lambda'
op|':'
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
nl|'\n'
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exception_msg_contains_vm_name
dedent|''
name|'def'
name|'test_exception_msg_contains_vm_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock'
op|'='
name|'mox'
op|'.'
name|'Mox'
op|'('
op|')'
newline|'\n'
name|'mock'
op|'.'
name|'StubOutWithMock'
op|'('
name|'vm_utils'
op|','
string|"'lookup'"
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'lookup'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'mock'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vm_utils'
op|'.'
name|'vm_ref_or_raise'
op|'('
string|"'session'"
op|','
string|"'somename'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InstanceNotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
nl|'\n'
string|"'somename'"
name|'in'
name|'str'
op|'('
name|'e'
op|')'
op|')'
newline|'\n'
dedent|''
name|'mock'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
