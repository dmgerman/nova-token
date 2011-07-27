begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""Tests for Direct API."""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'direct'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'test_cloud'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ArbitraryObject
name|'class'
name|'ArbitraryObject'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeService
dedent|''
name|'class'
name|'FakeService'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|echo
indent|'    '
name|'def'
name|'echo'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'data'"
op|':'
name|'data'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|context
dedent|''
name|'def'
name|'context'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'user'"
op|':'
name|'context'
op|'.'
name|'user_id'
op|','
nl|'\n'
string|"'project'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|invalid_return
dedent|''
name|'def'
name|'invalid_return'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'ArbitraryObject'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DirectTestCase
dedent|''
dedent|''
name|'class'
name|'DirectTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'DirectTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'direct'
op|'.'
name|'register_service'
op|'('
string|"'fake'"
op|','
name|'FakeService'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'router'
op|'='
name|'direct'
op|'.'
name|'PostParamsMiddleware'
op|'('
nl|'\n'
name|'direct'
op|'.'
name|'JsonParamsMiddleware'
op|'('
nl|'\n'
name|'direct'
op|'.'
name|'Router'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth_router'
op|'='
name|'direct'
op|'.'
name|'DelegatedAuthMiddleware'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'user1'"
op|','
string|"'proj1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'direct'
op|'.'
name|'ROUTES'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'super'
op|'('
name|'DirectTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delegated_auth
dedent|''
name|'def'
name|'test_delegated_auth'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/context'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-User'"
op|']'
op|'='
string|"'user1'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'X-OpenStack-Project'"
op|']'
op|'='
string|"'proj1'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'auth_router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'user'"
op|']'
op|','
string|"'user1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'data'
op|'['
string|"'project'"
op|']'
op|','
string|"'proj1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_params
dedent|''
name|'def'
name|'test_json_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/echo'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'json=%s'"
op|'%'
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'data'"
op|':'
string|"'foo'"
op|'}'
op|')'
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_parsed'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_parsed'
op|'['
string|"'data'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_params
dedent|''
name|'def'
name|'test_post_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/echo'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"'data=foo'"
newline|'\n'
name|'resp'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_parsed'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_parsed'
op|'['
string|"'data'"
op|']'
op|','
string|"'foo'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid
dedent|''
name|'def'
name|'test_invalid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/fake/invalid_return'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'openstack.context'"
op|']'
op|'='
name|'self'
op|'.'
name|'context'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'Error'
op|','
name|'req'
op|'.'
name|'get_response'
op|','
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_proxy
dedent|''
name|'def'
name|'test_proxy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'proxy'
op|'='
name|'direct'
op|'.'
name|'Proxy'
op|'('
name|'self'
op|'.'
name|'router'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'proxy'
op|'.'
name|'fake'
op|'.'
name|'echo'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'data'
op|'='
string|"'baz'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rv'
op|'['
string|"'data'"
op|']'
op|','
string|"'baz'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# NOTE(jkoelker): This fails using the EC2 api'
nl|'\n'
comment|'#class DirectCloudTestCase(test_cloud.CloudTestCase):'
nl|'\n'
comment|'#    def setUp(self):'
nl|'\n'
comment|'#        super(DirectCloudTestCase, self).setUp()'
nl|'\n'
comment|'#        compute_handle = compute.API(image_service=self.cloud.image_service)'
nl|'\n'
comment|'#        volume_handle = volume.API()'
nl|'\n'
comment|'#        network_handle = network.API()'
nl|'\n'
comment|"#        direct.register_service('compute', compute_handle)"
nl|'\n'
comment|"#        direct.register_service('volume', volume_handle)"
nl|'\n'
comment|"#        direct.register_service('network', network_handle)"
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        self.router = direct.JsonParamsMiddleware(direct.Router())'
nl|'\n'
comment|'#        proxy = direct.Proxy(self.router)'
nl|'\n'
comment|'#        self.cloud.compute_api = proxy.compute'
nl|'\n'
comment|'#        self.cloud.volume_api = proxy.volume'
nl|'\n'
comment|'#        self.cloud.network_api = proxy.network'
nl|'\n'
comment|'#        compute_handle.volume_api = proxy.volume'
nl|'\n'
comment|'#        compute_handle.network_api = proxy.network'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    def tearDown(self):'
nl|'\n'
comment|'#        super(DirectCloudTestCase, self).tearDown()'
nl|'\n'
comment|'#        direct.ROUTES = {}'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
