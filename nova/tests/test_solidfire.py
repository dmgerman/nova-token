begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack LLC.'
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
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'solidfire'
name|'import'
name|'SolidFire'
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
nl|'\n'
DECL|class|SolidFireVolumeTestCase
name|'class'
name|'SolidFireVolumeTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|fake_issue_api_request
indent|'    '
name|'def'
name|'fake_issue_api_request'
op|'('
name|'obj'
op|','
name|'method'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'method'
name|'is'
string|"'GetClusterInfo'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake GetClusterInfo...'"
op|')'
newline|'\n'
name|'results'
op|'='
op|'{'
string|"'result'"
op|':'
op|'{'
string|"'clusterInfo'"
op|':'
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'fake-cluster'"
op|','
nl|'\n'
string|"'mvip'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'svip'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'uniqueID'"
op|':'
string|"'unqid'"
op|','
nl|'\n'
string|"'repCount'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'attributes'"
op|':'
op|'{'
op|'}'
op|'}'
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'results'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'method'
name|'is'
string|"'AddAccount'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake AddAccount...'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'result'"
op|':'
op|'{'
string|"'accountID'"
op|':'
number|'25'
op|'}'
op|','
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'method'
name|'is'
string|"'GetAccountByName'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake GetAccountByName...'"
op|')'
newline|'\n'
name|'results'
op|'='
op|'{'
string|"'result'"
op|':'
op|'{'
string|"'account'"
op|':'
nl|'\n'
op|'{'
string|"'accountID'"
op|':'
number|'25'
op|','
nl|'\n'
string|"'username'"
op|':'
name|'params'
op|'['
string|"'username'"
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'initiatorSecret'"
op|':'
string|"'123456789012'"
op|','
nl|'\n'
string|"'targetSecret'"
op|':'
string|"'123456789012'"
op|','
nl|'\n'
string|"'attributes'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'volumes'"
op|':'
op|'['
number|'6'
op|','
number|'7'
op|','
number|'20'
op|']'
op|'}'
op|'}'
op|','
nl|'\n'
string|'"id"'
op|':'
number|'1'
op|'}'
newline|'\n'
name|'return'
name|'results'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'method'
name|'is'
string|"'CreateVolume'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake CreateVolume...'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'result'"
op|':'
op|'{'
string|"'volumeID'"
op|':'
number|'5'
op|'}'
op|','
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'method'
name|'is'
string|"'DeleteVolume'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake DeleteVolume...'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'result'"
op|':'
op|'{'
op|'}'
op|','
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'method'
name|'is'
string|"'ListVolumesForAccount'"
op|':'
newline|'\n'
indent|'            '
name|'test_name'
op|'='
string|"'OS-VOLID-a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake ListVolumesForAccount...'"
op|')'
newline|'\n'
name|'result'
op|'='
op|'{'
string|"'result'"
op|':'
op|'{'
nl|'\n'
string|"'volumes'"
op|':'
op|'['
op|'{'
string|"'volumeID'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'test_name'
op|','
nl|'\n'
string|"'accountID'"
op|':'
number|'25'
op|','
nl|'\n'
string|"'sliceCount'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'totalSize'"
op|':'
number|'1048576'
op|'*'
number|'1024'
op|','
nl|'\n'
string|"'enable512e'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'access'"
op|':'
string|'"readWrite"'
op|','
nl|'\n'
string|"'status'"
op|':'
string|'"active"'
op|','
nl|'\n'
string|"'attributes'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'qos'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'iqn'"
op|':'
name|'test_name'
op|'}'
op|']'
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
string|"'Crap, unimplemented API call in Fake:%s'"
op|'%'
name|'method'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_issue_api_request_no_volume
dedent|''
dedent|''
name|'def'
name|'fake_issue_api_request_no_volume'
op|'('
name|'obj'
op|','
name|'method'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'method'
name|'is'
string|"'ListVolumesForAccount'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
string|"'Called Fake ListVolumesForAccount...'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'result'"
op|':'
op|'{'
string|"'volumes'"
op|':'
op|'['
op|']'
op|'}'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'obj'
op|'.'
name|'fake_issue_api_request'
op|'('
name|'method'
op|','
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_issue_api_request_fails
dedent|''
dedent|''
name|'def'
name|'fake_issue_api_request_fails'
op|'('
name|'obj'
op|','
name|'method'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'error'"
op|':'
op|'{'
string|"'code'"
op|':'
number|'000'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'DummyError'"
op|','
nl|'\n'
string|"'message'"
op|':'
string|"'This is a fake error response'"
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
number|'1'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|fake_volume_get
dedent|''
name|'def'
name|'fake_volume_get'
op|'('
name|'obj'
op|','
name|'key'
op|','
name|'default'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'qos'"
op|':'
string|"'fast'"
op|'}'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'testvol'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|'}'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'sfv'
op|'.'
name|'create_volume'
op|'('
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume_with_qos
dedent|''
name|'def'
name|'test_create_volume_with_qos'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'preset_qos'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'preset_qos'
op|'['
string|"'qos'"
op|']'
op|'='
string|"'fast'"
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
nl|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'testvol'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'['
name|'preset_qos'
op|']'
op|'}'
newline|'\n'
nl|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'sfv'
op|'.'
name|'create_volume'
op|'('
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume_fails
dedent|''
name|'def'
name|'test_create_volume_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_fails'
op|')'
newline|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'testvol'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|'}'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SolidFireAPIDataException'
op|','
nl|'\n'
name|'sfv'
op|'.'
name|'create_volume'
op|','
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_sfaccount
dedent|''
name|'def'
name|'test_create_sfaccount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
name|'account'
op|'='
name|'sfv'
op|'.'
name|'_create_sfaccount'
op|'('
string|"'project-id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'account'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_sfaccount_fails
dedent|''
name|'def'
name|'test_create_sfaccount_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_fails'
op|')'
newline|'\n'
name|'account'
op|'='
name|'sfv'
op|'.'
name|'_create_sfaccount'
op|'('
string|"'project-id'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'account'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sfaccount_by_name
dedent|''
name|'def'
name|'test_get_sfaccount_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
name|'account'
op|'='
name|'sfv'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
string|"'some-name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'account'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sfaccount_by_name_fails
dedent|''
name|'def'
name|'test_get_sfaccount_by_name_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_fails'
op|')'
newline|'\n'
name|'account'
op|'='
name|'sfv'
op|'.'
name|'_get_sfaccount_by_name'
op|'('
string|"'some-name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'account'
op|','
name|'None'
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test_volume'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|'}'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'model_update'
op|'='
name|'sfv'
op|'.'
name|'delete_volume'
op|'('
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume_fails_no_volume
dedent|''
name|'def'
name|'test_delete_volume_fails_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_no_volume'
op|')'
newline|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'no-name'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|'}'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'VolumeNotFound'
op|','
nl|'\n'
name|'sfv'
op|'.'
name|'delete_volume'
op|','
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume_fails_account_lookup
dedent|''
name|'def'
name|'test_delete_volume_fails_account_lookup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_fails'
op|')'
newline|'\n'
name|'testvol'
op|'='
op|'{'
string|"'project_id'"
op|':'
string|"'testprjid'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'no-name'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'a720b3c0-d1f0-11e1-9b23-0800200c9a66'"
op|'}'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SfAccountNotFound'
op|','
nl|'\n'
name|'sfv'
op|'.'
name|'delete_volume'
op|','
nl|'\n'
name|'testvol'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cluster_info
dedent|''
name|'def'
name|'test_get_cluster_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request'
op|')'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'sfv'
op|'.'
name|'_get_cluster_info'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_cluster_info_fail
dedent|''
name|'def'
name|'test_get_cluster_info_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'SolidFire'
op|','
string|"'_issue_api_request'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_issue_api_request_fails'
op|')'
newline|'\n'
name|'sfv'
op|'='
name|'SolidFire'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'SolidFireAPIException'
op|','
nl|'\n'
name|'sfv'
op|'.'
name|'_get_cluster_info'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
