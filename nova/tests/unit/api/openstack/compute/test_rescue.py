begin_unit
comment|'#   Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'compute'
name|'import'
name|'rescue'
name|'as'
name|'rescue_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
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
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|UUID
name|'UUID'
op|'='
string|"'70f6db34-de8d-4fbd-aafb-4065bdfa6114'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rescue
name|'def'
name|'rescue'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|','
name|'rescue_password'
op|'='
name|'None'
op|','
nl|'\n'
name|'rescue_image_ref'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unrescue
dedent|''
name|'def'
name|'unrescue'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_compute_get
dedent|''
name|'def'
name|'fake_compute_get'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'return'
op|'{'
string|"'id'"
op|':'
number|'1'
op|','
string|"'uuid'"
op|':'
name|'UUID'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RescueTestV21
dedent|''
name|'class'
name|'RescueTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|image_uuid
indent|'    '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
DECL|variable|image_href
name|'image_href'
op|'='
string|"'http://localhost/v2/fake/images/%s'"
op|'%'
name|'image_uuid'
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
name|'super'
op|'('
name|'RescueTestV21'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"rescue"'
op|','
name|'rescue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"unrescue"'
op|','
name|'unrescue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'self'
op|'.'
name|'_set_up_controller'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_up_controller
dedent|''
name|'def'
name|'_set_up_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'rescue_v21'
op|'.'
name|'RescueController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_from_locked_server
dedent|''
name|'def'
name|'test_rescue_from_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_rescue_from_locked_server
indent|'        '
name|'def'
name|'fake_rescue_from_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|','
name|'rescue_password'
op|'='
name|'None'
op|','
name|'rescue_image_ref'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'rescue'"
op|','
nl|'\n'
name|'fake_rescue_from_locked_server'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"AABBCC112233"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_with_preset_password
dedent|''
name|'def'
name|'test_rescue_with_preset_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"AABBCC112233"'
op|'}'
op|'}'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"AABBCC112233"'
op|','
name|'resp'
op|'['
string|"'adminPass'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_generates_password
dedent|''
name|'def'
name|'test_rescue_generates_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'password_length'
op|','
name|'len'
op|'('
name|'resp'
op|'['
string|"'adminPass'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_of_rescued_instance
dedent|''
name|'def'
name|'test_rescue_of_rescued_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_rescue
name|'def'
name|'fake_rescue'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
string|"'fake message'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"rescue"'
op|','
name|'fake_rescue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unrescue
dedent|''
name|'def'
name|'test_unrescue'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'unrescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unrescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
comment|'# NOTE: on v2.1, http status code is set as wsgi_code of API'
nl|'\n'
comment|'# method instead of status_int in a response object.'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'rescue_v21'
op|'.'
name|'RescueController'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unrescue'
op|'.'
name|'wsgi_code'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'status_int'
op|'='
name|'resp'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unrescue_from_locked_server
dedent|''
name|'def'
name|'test_unrescue_from_locked_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_unrescue_from_locked_server
indent|'        '
name|'def'
name|'fake_unrescue_from_locked_server'
op|'('
name|'self'
op|','
name|'context'
op|','
nl|'\n'
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceIsLocked'
op|'('
name|'instance_uuid'
op|'='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'unrescue'"
op|','
nl|'\n'
name|'fake_unrescue_from_locked_server'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'unrescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unrescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unrescue_of_active_instance
dedent|''
name|'def'
name|'test_unrescue_of_active_instance'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'unrescue'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_unrescue
name|'def'
name|'fake_unrescue'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceInvalidState'
op|'('
string|"'fake message'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"unrescue"'
op|','
name|'fake_unrescue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPConflict'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unrescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_raises_unrescuable
dedent|''
name|'def'
name|'test_rescue_raises_unrescuable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_rescue
name|'def'
name|'fake_rescue'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotRescuable'
op|'('
string|"'fake message'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"rescue"'
op|','
name|'fake_rescue'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.rescue'"
op|')'
newline|'\n'
DECL|member|test_rescue_with_bad_image_specified
name|'def'
name|'test_rescue_with_bad_image_specified'
op|'('
name|'self'
op|','
name|'mock_compute_api_rescue'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"ABC123"'
op|','
nl|'\n'
string|'"rescue_image_ref"'
op|':'
string|'"img-id"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.rescue'"
op|')'
newline|'\n'
DECL|member|test_rescue_with_image_specified
name|'def'
name|'test_rescue_with_image_specified'
op|'('
name|'self'
op|','
name|'mock_compute_api_rescue'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'fake_compute_get'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"ABC123"'
op|','
nl|'\n'
string|'"rescue_image_ref"'
op|':'
name|'self'
op|'.'
name|'image_href'
op|'}'
op|'}'
newline|'\n'
name|'resp_json'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"ABC123"'
op|','
name|'resp_json'
op|'['
string|"'adminPass'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mock_compute_api_rescue'
op|'.'
name|'assert_called_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'rescue_password'
op|'='
string|"u'ABC123'"
op|','
nl|'\n'
name|'rescue_image_ref'
op|'='
name|'self'
op|'.'
name|'image_uuid'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.compute.api.API.rescue'"
op|')'
newline|'\n'
DECL|member|test_rescue_without_image_specified
name|'def'
name|'test_rescue_without_image_specified'
op|'('
name|'self'
op|','
name|'mock_compute_api_rescue'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'fake_compute_get'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"ABC123"'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'resp_json'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"ABC123"'
op|','
name|'resp_json'
op|'['
string|"'adminPass'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mock_compute_api_rescue'
op|'.'
name|'assert_called_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'instance'
op|','
nl|'\n'
name|'rescue_password'
op|'='
string|"u'ABC123'"
op|','
nl|'\n'
name|'rescue_image_ref'
op|'='
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_with_none
dedent|''
name|'def'
name|'test_rescue_with_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'password_length'
op|','
name|'len'
op|'('
name|'resp'
op|'['
string|"'adminPass'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_with_empty_dict
dedent|''
name|'def'
name|'test_rescue_with_empty_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'dict'
op|'('
op|')'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'CONF'
op|'.'
name|'password_length'
op|','
name|'len'
op|'('
name|'resp'
op|'['
string|"'adminPass'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_disable_password
dedent|''
name|'def'
name|'test_rescue_disable_password'
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
name|'enable_instance_password'
op|'='
name|'False'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'rescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'resp_json'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'adminPass'"
op|','
name|'resp_json'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_with_invalid_property
dedent|''
name|'def'
name|'test_rescue_with_invalid_property'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"test"'
op|':'
string|'"test"'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ValidationError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_req'
op|','
name|'UUID'
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RescuePolicyEnforcementV21
dedent|''
dedent|''
name|'class'
name|'RescuePolicyEnforcementV21'
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
name|'RescuePolicyEnforcementV21'
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
name|'controller'
op|'='
name|'rescue_v21'
op|'.'
name|'RescueController'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_policy_failed
dedent|''
name|'def'
name|'test_rescue_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-rescue"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"rescue"'
op|':'
op|'{'
string|'"adminPass"'
op|':'
string|'"AABBCC112233"'
op|'}'
op|'}'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unrescue_policy_failed
dedent|''
name|'def'
name|'test_unrescue_policy_failed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule_name'
op|'='
string|'"os_compute_api:os-rescue"'
newline|'\n'
name|'self'
op|'.'
name|'policy'
op|'.'
name|'set_rules'
op|'('
op|'{'
name|'rule_name'
op|':'
string|'"project:non_fake"'
op|'}'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'unrescue'
op|'='
name|'None'
op|')'
newline|'\n'
name|'exc'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
nl|'\n'
name|'exception'
op|'.'
name|'PolicyNotAuthorized'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_unrescue'
op|','
name|'self'
op|'.'
name|'req'
op|','
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|'"Policy doesn\'t allow %s to be performed."'
op|'%'
name|'rule_name'
op|','
nl|'\n'
name|'exc'
op|'.'
name|'format_message'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
