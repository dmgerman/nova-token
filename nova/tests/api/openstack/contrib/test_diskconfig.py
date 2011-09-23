begin_unit
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'json'
newline|'\n'
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
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'image'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'diskconfig'
name|'import'
name|'DiskConfigController'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'contrib'
op|'.'
name|'diskconfig'
name|'import'
name|'ImageDiskConfigController'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskConfigTest
name|'class'
name|'DiskConfigTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_retrieve_disk_config
indent|'    '
name|'def'
name|'test_retrieve_disk_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_compute_get
indent|'        '
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
indent|'            '
name|'return'
op|'{'
string|"'managed_disk'"
op|':'
name|'True'
op|'}'
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
string|"'routing_get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/servers/50/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'managed_disk'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|','
number|'50'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_disk_config
dedent|''
name|'def'
name|'test_set_disk_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_compute_get
indent|'        '
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
indent|'            '
name|'return'
op|'{'
string|"'managed_disk'"
op|':'
string|"'True'"
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_update
dedent|''
name|'def'
name|'fake_compute_update'
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
name|'return'
op|'{'
string|"'managed_disk'"
op|':'
string|"'False'"
op|'}'
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
string|"'update'"
op|','
name|'fake_compute_update'
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
string|"'routing_get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/servers/50/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'server'"
op|':'
op|'{'
string|"'managed_disk'"
op|':'
name|'False'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'managed_disk'"
op|']'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|','
number|'50'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_retrieve_disk_config_bad_server_fails
dedent|''
name|'def'
name|'test_retrieve_disk_config_bad_server_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_compute_get
indent|'        '
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
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
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
string|"'routing_get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/servers/50/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_set_disk_config_bad_server_fails
dedent|''
name|'def'
name|'test_set_disk_config_bad_server_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_get
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
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_compute_update
dedent|''
name|'def'
name|'fake_compute_update'
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
name|'self'
op|'.'
name|'called'
op|'='
name|'True'
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
string|"'update'"
op|','
name|'fake_compute_update'
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
string|"'routing_get'"
op|','
name|'fake_compute_get'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/servers/50/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
string|"'server'"
op|':'
op|'{'
string|"'managed_disk'"
op|':'
name|'False'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'called'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageDiskConfigTest
dedent|''
dedent|''
name|'class'
name|'ImageDiskConfigTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NOW_GLANCE_FORMAT
indent|'    '
name|'NOW_GLANCE_FORMAT'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
DECL|variable|NOW_API_FORMAT
name|'NOW_API_FORMAT'
op|'='
string|'"2010-10-11T10:30:22Z"'
newline|'\n'
nl|'\n'
DECL|member|test_image_get_disk_config
name|'def'
name|'test_image_get_disk_config'
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
name|'image_service'
op|'='
string|"'nova.image.glance.GlanceImageService'"
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_glance'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_image_service_show
name|'def'
name|'fake_image_service_show'
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
name|'return'
op|'{'
string|"'properties'"
op|':'
op|'{'
string|"'managed_disk'"
op|':'
name|'True'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'image'
op|'.'
name|'glance'
op|'.'
name|'GlanceImageService'
op|','
string|"'show'"
op|','
nl|'\n'
name|'fake_image_service_show'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/images/10/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'managed_disk'"
op|']'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'body'
op|'['
string|"'image'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
op|','
number|'10'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_get_disk_config_no_image_fails
dedent|''
name|'def'
name|'test_image_get_disk_config_no_image_fails'
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
name|'image_service'
op|'='
string|"'nova.image.glance.GlanceImageService'"
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_glance'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_image_service_show
name|'def'
name|'fake_image_service_show'
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
name|'NotFound'
op|'('
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
name|'image'
op|'.'
name|'glance'
op|'.'
name|'GlanceImageService'
op|','
string|"'show'"
op|','
nl|'\n'
name|'fake_image_service_show'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/openstack/images/10/os-disk-config'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_make_image_fixtures
name|'def'
name|'_make_image_fixtures'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
number|'123'
newline|'\n'
name|'base_attrs'
op|'='
op|'{'
string|"'created_at'"
op|':'
name|'cls'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'cls'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
nl|'\n'
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|add_fixture
name|'def'
name|'add_fixture'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'kwargs'
op|'.'
name|'update'
op|'('
name|'base_attrs'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Public image'
nl|'\n'
dedent|''
name|'add_fixture'
op|'('
name|'id'
op|'='
number|'1'
op|','
name|'name'
op|'='
string|"'snapshot'"
op|','
name|'is_public'
op|'='
name|'False'
op|','
nl|'\n'
name|'status'
op|'='
string|"'active'"
op|','
name|'properties'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'fixtures'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
