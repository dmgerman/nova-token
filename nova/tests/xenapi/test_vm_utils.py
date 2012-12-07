begin_unit
name|'import'
name|'mox'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
DECL|variable|XENSM_TYPE
name|'XENSM_TYPE'
op|'='
string|"'xensm'"
newline|'\n'
DECL|variable|ISCSI_TYPE
name|'ISCSI_TYPE'
op|'='
string|"'iscsi'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fake_dev_params
name|'def'
name|'get_fake_dev_params'
op|'('
name|'sr_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fakes'
op|'='
op|'{'
name|'XENSM_TYPE'
op|':'
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
nl|'\n'
string|"'serverpath'"
op|','
nl|'\n'
string|"'sr_type'"
op|']'
op|','
nl|'\n'
string|"'vdi_uuid'"
op|':'
string|"'falseVDI'"
op|'}'
op|','
nl|'\n'
name|'ISCSI_TYPE'
op|':'
op|'{'
string|"'volume_id'"
op|':'
string|"'fake_volume_id'"
op|','
nl|'\n'
string|"'target_lun'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'target_iqn'"
op|':'
string|"'fake_iqn:volume-fake_volume_id'"
op|','
nl|'\n'
string|"'target_portal'"
op|':'
string|"u'localhost:3260'"
op|','
nl|'\n'
string|"'target_discovered'"
op|':'
name|'False'
op|'}'
op|','
op|'}'
newline|'\n'
name|'return'
name|'fakes'
op|'['
name|'sr_type'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GetInstanceForVdisForSrTestCase
dedent|''
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
DECL|member|test_get_vdis_for_boot_from_vol_with_sr_uuid
dedent|''
name|'def'
name|'test_get_vdis_for_boot_from_vol_with_sr_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_params'
op|'='
name|'get_fake_dev_params'
op|'('
name|'XENSM_TYPE'
op|')'
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
name|'get_fake_dev_params'
op|'('
name|'XENSM_TYPE'
op|')'
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
DECL|member|test_get_vdis_for_boot_from_iscsi_vol_missing_sr_uuid
dedent|''
name|'def'
name|'test_get_vdis_for_boot_from_iscsi_vol_missing_sr_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dev_params'
op|'='
name|'get_fake_dev_params'
op|'('
name|'ISCSI_TYPE'
op|')'
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
name|'assertNotEquals'
op|'('
name|'result'
op|'['
string|"'root'"
op|']'
op|'['
string|"'uuid'"
op|']'
op|','
name|'None'
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
nl|'\n'
nl|'\n'
DECL|class|BittorrentTestCase
dedent|''
dedent|''
name|'class'
name|'BittorrentTestCase'
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
name|'BittorrentTestCase'
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
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_uses_bittorrent
dedent|''
name|'def'
name|'test_image_uses_bittorrent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys_meta'
op|'='
op|'{'
string|"'image_bittorrent'"
op|':'
name|'True'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'xenapi_torrent_images'
op|'='
string|"'some'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'vm_utils'
op|'.'
name|'_image_uses_bittorrent'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_image
dedent|''
name|'def'
name|'_test_create_image'
op|'('
name|'self'
op|','
name|'cache_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys_meta'
op|'='
op|'{'
string|"'image_cache_in_nova'"
op|':'
name|'True'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
op|'{'
string|"'system_metadata'"
op|':'
name|'sys_meta'
op|'}'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get_by_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'cache_images'
op|'='
name|'cache_type'
op|')'
newline|'\n'
nl|'\n'
name|'was'
op|'='
op|'{'
string|"'called'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_create_cached_image
name|'def'
name|'fake_create_cached_image'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'was'
op|'['
string|"'called'"
op|']'
op|'='
string|"'some'"
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_create_cached_image'"
op|','
nl|'\n'
name|'fake_create_cached_image'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_fetch_image
name|'def'
name|'fake_fetch_image'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'was'
op|'['
string|"'called'"
op|']'
op|'='
string|"'none'"
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_fetch_image'"
op|','
nl|'\n'
name|'fake_fetch_image'
op|')'
newline|'\n'
nl|'\n'
name|'vm_utils'
op|'.'
name|'_create_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'None'
op|','
name|'instance'
op|','
nl|'\n'
string|"'foo'"
op|','
string|"'bar'"
op|','
string|"'baz'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'was'
op|'['
string|"'called'"
op|']'
op|','
name|'cache_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_cached
dedent|''
name|'def'
name|'test_create_image_cached'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_image'
op|'('
string|"'some'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_image_uncached
dedent|''
name|'def'
name|'test_create_image_uncached'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_create_image'
op|'('
string|"'none'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
