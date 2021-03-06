begin_unit
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'fixture'
name|'as'
name|'utils_fixture'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'requests'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'trusted_filter'
newline|'\n'
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
name|'unit'
op|'.'
name|'scheduler'
name|'import'
name|'fakes'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|class|AttestationServiceTestCase
name|'class'
name|'AttestationServiceTestCase'
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
name|'AttestationServiceTestCase'
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
name|'api_url'
op|'='
string|"'/OpenAttestationWebServices/V1.0'"
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
string|"'localhost'"
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
string|"'8443'"
newline|'\n'
name|'self'
op|'.'
name|'statuses'
op|'='
op|'('
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'CREATED'
op|','
nl|'\n'
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'ACCEPTED'
op|','
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'NO_CONTENT'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'requests'
op|','
string|"'request'"
op|')'
newline|'\n'
DECL|member|test_do_request_possible_statuses
name|'def'
name|'test_do_request_possible_statuses'
op|'('
name|'self'
op|','
name|'request_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This test case checks if \'_do_request()\' method returns\n        appropriate status_code (200) and result (text converted to json),\n        while status_code returned by request is in one of fourth eligible\n        statuses\n        """'
newline|'\n'
nl|'\n'
name|'for'
name|'status_code'
name|'in'
name|'self'
op|'.'
name|'statuses'
op|':'
newline|'\n'
indent|'            '
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'status_code'
op|'='
name|'status_code'
newline|'\n'
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'text'
op|'='
string|'\'{"test": "test"}\''
newline|'\n'
nl|'\n'
name|'attestation_service'
op|'='
name|'trusted_filter'
op|'.'
name|'AttestationService'
op|'('
op|')'
newline|'\n'
name|'status'
op|','
name|'result'
op|'='
name|'attestation_service'
op|'.'
name|'_do_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
string|"'PollHosts'"
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'text'
op|')'
op|','
nl|'\n'
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'requests'
op|','
string|"'request'"
op|')'
newline|'\n'
DECL|member|test_do_request_other_status
name|'def'
name|'test_do_request_other_status'
op|'('
name|'self'
op|','
name|'request_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""This test case checks if \'_do_request()\' method returns\n        appropriate status (this returned by request method) and result\n        (None), while status_code returned by request is not in one of fourth\n        eligible statuses\n        """'
newline|'\n'
nl|'\n'
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'status_code'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'NOT_FOUND'
newline|'\n'
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'text'
op|'='
string|'\'{"test": "test"}\''
newline|'\n'
nl|'\n'
name|'attestation_service'
op|'='
name|'trusted_filter'
op|'.'
name|'AttestationService'
op|'('
op|')'
newline|'\n'
name|'status'
op|','
name|'result'
op|'='
name|'attestation_service'
op|'.'
name|'_do_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
string|"'PollHosts'"
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'NOT_FOUND'
op|','
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'result'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'requests'
op|','
string|"'request'"
op|')'
newline|'\n'
DECL|member|test_do_request_unconvertible_text
name|'def'
name|'test_do_request_unconvertible_text'
op|'('
name|'self'
op|','
name|'request_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'status_code'
name|'in'
name|'self'
op|'.'
name|'statuses'
op|':'
newline|'\n'
comment|'# this unconvertible_texts leads to TypeError and ValueError'
nl|'\n'
comment|'# in jsonutils.loads(res.text) in _do_request() method'
nl|'\n'
indent|'            '
name|'for'
name|'unconvertible_text'
name|'in'
op|'('
op|'{'
string|'"test"'
op|':'
string|'"test"'
op|'}'
op|','
string|"'{}{}'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'status_code'
op|'='
name|'status_code'
newline|'\n'
name|'request_mock'
op|'.'
name|'return_value'
op|'.'
name|'text'
op|'='
name|'unconvertible_text'
newline|'\n'
nl|'\n'
name|'attestation_service'
op|'='
name|'trusted_filter'
op|'.'
name|'AttestationService'
op|'('
op|')'
newline|'\n'
name|'status'
op|','
name|'result'
op|'='
name|'attestation_service'
op|'.'
name|'_do_request'
op|'('
nl|'\n'
string|"'POST'"
op|','
string|"'PollHosts'"
op|','
op|'{'
op|'}'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'status'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unconvertible_text'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'trusted_filter'
op|'.'
name|'AttestationService'
op|','
string|"'_request'"
op|')'
newline|'\n'
DECL|class|TestTrustedFilter
name|'class'
name|'TestTrustedFilter'
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
name|'TestTrustedFilter'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
comment|"# TrustedFilter's constructor creates the attestation cache, which"
nl|'\n'
comment|'# calls to get a list of all the compute nodes.'
nl|'\n'
name|'fake_compute_nodes'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|')'
name|'as'
name|'mocked'
op|':'
newline|'\n'
indent|'            '
name|'mocked'
op|'.'
name|'return_value'
op|'='
name|'fake_compute_nodes'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'trusted_filter'
op|'.'
name|'TrustedFilter'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_default_passes
dedent|''
dedent|''
name|'def'
name|'test_trusted_filter_default_passes'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_trusted_and_trusted_passes
dedent|''
name|'def'
name|'test_trusted_filter_trusted_and_trusted_passes'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"trusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
nl|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'trusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'req_mock'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"POST"'
op|','
string|'"PollHosts"'
op|','
op|'['
string|'"node1"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_trusted_and_untrusted_fails
dedent|''
name|'def'
name|'test_trusted_filter_trusted_and_untrusted_fails'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"untrusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'trusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_untrusted_and_trusted_fails
dedent|''
name|'def'
name|'test_trusted_filter_untrusted_and_trusted_fails'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"trusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'untrusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_untrusted_and_untrusted_passes
dedent|''
name|'def'
name|'test_trusted_filter_untrusted_and_untrusted_passes'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"untrusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'untrusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_update_cache
dedent|''
name|'def'
name|'test_trusted_filter_update_cache'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"untrusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'utils'
op|'.'
name|'isotime'
op|'('
op|')'
op|'}'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'untrusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
comment|'# Fill the caches'
newline|'\n'
nl|'\n'
name|'req_mock'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
name|'req_mock'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'time_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'utils_fixture'
op|'.'
name|'TimeFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'time_fixture'
op|'.'
name|'advance_time_seconds'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_auth_timeout'
op|'+'
number|'80'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_update_cache_timezone
dedent|''
name|'def'
name|'test_trusted_filter_update_cache_timezone'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"untrusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
string|'"2012-09-09T05:10:40-04:00"'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'untrusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'time_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'utils_fixture'
op|'.'
name|'TimeFixture'
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'normalize_time'
op|'('
nl|'\n'
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
string|'"2012-09-09T09:10:40Z"'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
comment|'# Fill the caches'
newline|'\n'
nl|'\n'
name|'req_mock'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
name|'req_mock'
op|'.'
name|'reset_mock'
op|'('
op|')'
newline|'\n'
name|'time_fixture'
op|'.'
name|'advance_time_seconds'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'trusted_computing'
op|'.'
name|'attestation_auth_timeout'
op|'-'
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_combine_hosts
dedent|''
name|'def'
name|'test_trusted_filter_combine_hosts'
op|'('
name|'self'
op|','
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_compute_nodes'
op|'='
op|'['
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'hypervisor_hostname'
op|'='
string|"'node1'"
op|')'
op|','
nl|'\n'
name|'objects'
op|'.'
name|'ComputeNode'
op|'('
name|'hypervisor_hostname'
op|'='
string|"'node2'"
op|')'
nl|'\n'
op|']'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.objects.ComputeNodeList.get_all'"
op|')'
name|'as'
name|'mocked'
op|':'
newline|'\n'
indent|'            '
name|'mocked'
op|'.'
name|'return_value'
op|'='
name|'fake_compute_nodes'
newline|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'='
name|'trusted_filter'
op|'.'
name|'TrustedFilter'
op|'('
op|')'
newline|'\n'
dedent|''
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"node1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"untrusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
string|'"2012-09-09T05:10:40-04:00"'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'trusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'node1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
comment|'# Fill the caches'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'req_mock'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'req_mock'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'call_args'
op|'='
name|'list'
op|'('
name|'req_mock'
op|'.'
name|'call_args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'expected_call_args'
op|'='
op|'['
string|"'POST'"
op|','
string|"'PollHosts'"
op|','
op|'['
string|"'node2'"
op|','
string|"'node1'"
op|']'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertJsonEqual'
op|'('
name|'call_args'
op|','
name|'expected_call_args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_trusted_filter_trusted_and_locale_formated_vtime_passes
dedent|''
name|'def'
name|'test_trusted_filter_trusted_and_locale_formated_vtime_passes'
op|'('
name|'self'
op|','
nl|'\n'
name|'req_mock'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'oat_data'
op|'='
op|'{'
string|'"hosts"'
op|':'
op|'['
op|'{'
string|'"host_name"'
op|':'
string|'"host1"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"trusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
nl|'\n'
string|'"%c"'
op|')'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"host_name"'
op|':'
string|'"host2"'
op|','
nl|'\n'
string|'"trust_lvl"'
op|':'
string|'"trusted"'
op|','
nl|'\n'
string|'"vtime"'
op|':'
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|'.'
name|'strftime'
op|'('
nl|'\n'
string|'"%D"'
op|')'
op|'}'
op|','
nl|'\n'
comment|'# This is just a broken date to ensure that'
nl|'\n'
comment|"# we're not just arbitrarily accepting any"
nl|'\n'
comment|'# date format.'
nl|'\n'
op|']'
op|'}'
newline|'\n'
name|'req_mock'
op|'.'
name|'return_value'
op|'='
name|'requests'
op|'.'
name|'codes'
op|'.'
name|'OK'
op|','
name|'oat_data'
newline|'\n'
name|'extra_specs'
op|'='
op|'{'
string|"'trust:trusted_host'"
op|':'
string|"'trusted'"
op|'}'
newline|'\n'
name|'spec_obj'
op|'='
name|'objects'
op|'.'
name|'RequestSpec'
op|'('
nl|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'ctx'
op|','
nl|'\n'
name|'flavor'
op|'='
name|'objects'
op|'.'
name|'Flavor'
op|'('
name|'memory_mb'
op|'='
number|'1024'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'extra_specs'
op|')'
op|')'
newline|'\n'
name|'host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host1'"
op|','
string|"'host1'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'bad_host'
op|'='
name|'fakes'
op|'.'
name|'FakeHostState'
op|'('
string|"'host2'"
op|','
string|"'host2'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'host'
op|','
name|'spec_obj'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'filt_cls'
op|'.'
name|'host_passes'
op|'('
name|'bad_host'
op|','
nl|'\n'
name|'spec_obj'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
