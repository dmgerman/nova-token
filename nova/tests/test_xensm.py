begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""Test suite for Xen Storage Manager Volume Driver."""'
newline|'\n'
nl|'\n'
nl|'\n'
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
name|'import'
name|'flags'
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
name|'fake'
name|'as'
name|'xenapi_fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'xensm'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenSMTestCase
name|'class'
name|'XenSMTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for Xen Storage Manager Volume operations."""'
newline|'\n'
nl|'\n'
DECL|member|_get_sm_backend_params
name|'def'
name|'_get_sm_backend_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'config_params'
op|'='
op|'('
string|'"name_label=testsmbackend "'
nl|'\n'
string|'"server=localhost "'
nl|'\n'
string|'"serverpath=/tmp/nfspath"'
op|')'
newline|'\n'
name|'params'
op|'='
name|'dict'
op|'('
name|'flavor_id'
op|'='
number|'1'
op|','
nl|'\n'
name|'sr_uuid'
op|'='
name|'None'
op|','
nl|'\n'
name|'sr_type'
op|'='
string|"'nfs'"
op|','
nl|'\n'
name|'config_params'
op|'='
name|'config_params'
op|')'
newline|'\n'
name|'return'
name|'params'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'XenSMTestCase'
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
name|'user_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user_id'
op|','
name|'self'
op|'.'
name|'project_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'compute_driver'
op|'='
string|"'xenapi.XenAPIDriver'"
op|','
nl|'\n'
name|'xenapi_connection_url'
op|'='
string|"'http://test_url'"
op|','
nl|'\n'
name|'xenapi_connection_username'
op|'='
string|"'test_user'"
op|','
nl|'\n'
name|'xenapi_connection_password'
op|'='
string|"'test_pass'"
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
name|'xenapi_fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'xenapi_fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'xensm'
op|'.'
name|'XenSMDriver'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'db'
op|'='
name|'db'
newline|'\n'
nl|'\n'
DECL|member|_setup_step
dedent|''
name|'def'
name|'_setup_step'
op|'('
name|'self'
op|','
name|'ctxt'
op|')'
op|':'
newline|'\n'
comment|'# Create a fake backend conf'
nl|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_sm_backend_params'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'db'
op|'.'
name|'sm_backend_conf_create'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'params'
op|')'
newline|'\n'
comment|'# Call setup, the one time operation that will create a backend SR'
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'do_setup'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'return'
name|'beconf'
newline|'\n'
nl|'\n'
DECL|member|test_do_setup
dedent|''
name|'def'
name|'test_do_setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'self'
op|'.'
name|'_setup_step'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'db'
op|'.'
name|'sm_backend_conf_get'
op|'('
name|'ctxt'
op|','
name|'beconf'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'beconf'
op|'['
string|"'sr_uuid'"
op|']'
op|','
name|'basestring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_volume
dedent|''
name|'def'
name|'_create_volume'
op|'('
name|'self'
op|','
name|'size'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a volume object."""'
newline|'\n'
name|'vol'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'vol'
op|'['
string|"'size'"
op|']'
op|'='
name|'size'
newline|'\n'
name|'vol'
op|'['
string|"'user_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'project_id'"
op|']'
op|'='
string|"'fake'"
newline|'\n'
name|'vol'
op|'['
string|"'host'"
op|']'
op|'='
string|"'localhost'"
newline|'\n'
name|'vol'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
name|'vol'
op|'['
string|"'status'"
op|']'
op|'='
string|'"creating"'
newline|'\n'
name|'vol'
op|'['
string|"'attach_status'"
op|']'
op|'='
string|'"detached"'
newline|'\n'
name|'return'
name|'db'
op|'.'
name|'volume_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'vol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume
dedent|''
name|'def'
name|'test_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'self'
op|'.'
name|'_setup_step'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'sm_volume_get'
op|'('
name|'ctxt'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_local_path
dedent|''
name|'def'
name|'test_local_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'val'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'local_path'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'val'
op|','
name|'basestring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume
dedent|''
name|'def'
name|'test_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'self'
op|'.'
name|'_setup_step'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'delete_volume'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'db'
op|'.'
name|'sm_volume_get'
op|','
nl|'\n'
name|'ctxt'
op|','
nl|'\n'
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume_raises_notfound
dedent|''
name|'def'
name|'test_delete_volume_raises_notfound'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'self'
op|'.'
name|'_setup_step'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'delete_volume'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|'"FA15E-1D"'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_expected_conn
dedent|''
name|'def'
name|'_get_expected_conn'
op|'('
name|'self'
op|','
name|'beconf'
op|','
name|'vol'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'expected'
op|'['
string|"'volume_id'"
op|']'
op|'='
name|'unicode'
op|'('
name|'vol'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'flavor_id'"
op|']'
op|'='
name|'beconf'
op|'['
string|"'flavor_id'"
op|']'
newline|'\n'
name|'expected'
op|'['
string|"'sr_uuid'"
op|']'
op|'='
name|'unicode'
op|'('
name|'beconf'
op|'['
string|"'sr_uuid'"
op|']'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'sr_type'"
op|']'
op|'='
name|'unicode'
op|'('
name|'beconf'
op|'['
string|"'sr_type'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'expected'
newline|'\n'
nl|'\n'
DECL|member|test_initialize_connection
dedent|''
name|'def'
name|'test_initialize_connection'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'self'
op|'.'
name|'_setup_step'
op|'('
name|'ctxt'
op|')'
newline|'\n'
name|'beconf'
op|'='
name|'db'
op|'.'
name|'sm_backend_conf_get'
op|'('
name|'ctxt'
op|','
name|'beconf'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'volume'
op|'='
name|'self'
op|'.'
name|'_create_volume'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_volume'
op|'('
name|'volume'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'self'
op|'.'
name|'_get_expected_conn'
op|'('
name|'beconf'
op|','
name|'volume'
op|')'
newline|'\n'
name|'conn'
op|'='
name|'self'
op|'.'
name|'driver'
op|'.'
name|'initialize_connection'
op|'('
name|'volume'
op|','
string|"'fakeConnector'"
op|')'
newline|'\n'
name|'res'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
name|'in'
op|'['
string|"'volume_id'"
op|','
string|"'flavor_id'"
op|','
string|"'sr_uuid'"
op|','
string|"'sr_type'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'res'
op|'['
name|'key'
op|']'
op|'='
name|'conn'
op|'['
string|"'data'"
op|']'
op|'['
name|'key'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'expected'
op|','
name|'res'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'set'
op|'('
name|'conn'
op|'['
string|"'data'"
op|']'
op|'['
string|"'introduce_sr_keys'"
op|']'
op|')'
op|','
nl|'\n'
name|'set'
op|'('
op|'['
string|"u'sr_type'"
op|','
string|"u'server'"
op|','
string|"u'serverpath'"
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
