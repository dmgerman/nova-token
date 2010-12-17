begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'datetime'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'auth'
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
name|'as'
name|'exc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'auth'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'local'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'wsgi'
name|'import'
name|'Router'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Context
name|'class'
name|'Context'
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
DECL|class|FakeRouter
dedent|''
name|'class'
name|'FakeRouter'
op|'('
name|'Router'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'res'
op|'.'
name|'status'
op|'='
string|"'200'"
newline|'\n'
name|'res'
op|'.'
name|'headers'
op|'['
string|"'X-Test-Success'"
op|']'
op|'='
string|"'True'"
newline|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_auth_init
dedent|''
dedent|''
name|'def'
name|'fake_auth_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'self'
op|'.'
name|'db'
op|'='
name|'FakeAuthDatabase'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'Context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'auth'
op|'='
name|'FakeAuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|function|fake_wsgi
name|'def'
name|'fake_wsgi'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'req'
op|'.'
name|'body'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'.'
name|'environ'
op|'['
string|"'inst_dict'"
op|']'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'req'
op|'.'
name|'body'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_key_pair_funcs
dedent|''
name|'def'
name|'stub_out_key_pair_funcs'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|key_pair
indent|'    '
name|'def'
name|'key_pair'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'dict'
op|'('
name|'name'
op|'='
string|"'key'"
op|','
name|'public_key'
op|'='
string|"'public_key'"
op|')'
op|']'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'db'
op|','
string|"'key_pair_get_all_by_user'"
op|','
name|'key_pair'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_image_service
dedent|''
name|'def'
name|'stub_out_image_service'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_image_show
indent|'    '
name|'def'
name|'fake_image_show'
op|'('
name|'meh'
op|','
name|'context'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'dict'
op|'('
name|'kernelId'
op|'='
number|'1'
op|','
name|'ramdiskId'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'local'
op|'.'
name|'LocalImageService'
op|','
string|"'show'"
op|','
name|'fake_image_show'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_auth
dedent|''
name|'def'
name|'stub_out_auth'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_auth_init
indent|'    '
name|'def'
name|'fake_auth_init'
op|'('
name|'self'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'app'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fake_auth_init'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'AuthMiddleware'
op|','
nl|'\n'
string|"'__call__'"
op|','
name|'fake_wsgi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_rate_limiting
dedent|''
name|'def'
name|'stub_out_rate_limiting'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_rate_init
indent|'    '
name|'def'
name|'fake_rate_init'
op|'('
name|'self'
op|','
name|'app'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'RateLimitingMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'app'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'application'
op|'='
name|'app'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'RateLimitingMiddleware'
op|','
nl|'\n'
string|"'__init__'"
op|','
name|'fake_rate_init'
op|')'
newline|'\n'
nl|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'RateLimitingMiddleware'
op|','
nl|'\n'
string|"'__call__'"
op|','
name|'fake_wsgi'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_networking
dedent|''
name|'def'
name|'stub_out_networking'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|get_my_ip
indent|'    '
name|'def'
name|'get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'127.0.0.1'"
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'utils'
op|','
string|"'get_my_ip'"
op|','
name|'get_my_ip'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_glance
dedent|''
name|'def'
name|'stub_out_glance'
op|'('
name|'stubs'
op|','
name|'initial_fixtures'
op|'='
op|'['
op|']'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|FakeParallaxClient
indent|'    '
name|'class'
name|'FakeParallaxClient'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'        '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'initial_fixtures'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixtures'
op|'='
name|'initial_fixtures'
newline|'\n'
nl|'\n'
DECL|member|fake_get_image_index
dedent|''
name|'def'
name|'fake_get_image_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'f'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'f'
op|'['
string|"'name'"
op|']'
op|')'
nl|'\n'
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'fixtures'
op|']'
newline|'\n'
nl|'\n'
DECL|member|fake_get_image_details
dedent|''
name|'def'
name|'fake_get_image_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'fixtures'
newline|'\n'
nl|'\n'
DECL|member|fake_get_image_metadata
dedent|''
name|'def'
name|'fake_get_image_metadata'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'fixtures'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'f'
op|'['
string|"'id'"
op|']'
op|'=='
name|'image_id'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'f'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|fake_add_image_metadata
dedent|''
name|'def'
name|'fake_add_image_metadata'
op|'('
name|'self'
op|','
name|'image_data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'id'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'random'
op|'.'
name|'choice'
op|'('
name|'string'
op|'.'
name|'letters'
op|')'
name|'for'
name|'_'
name|'in'
name|'range'
op|'('
number|'20'
op|')'
op|')'
newline|'\n'
name|'image_data'
op|'['
string|"'id'"
op|']'
op|'='
name|'id'
newline|'\n'
name|'self'
op|'.'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'image_data'
op|')'
newline|'\n'
name|'return'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|fake_update_image_metadata
dedent|''
name|'def'
name|'fake_update_image_metadata'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'image_data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'self'
op|'.'
name|'fake_get_image_metadata'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'.'
name|'update'
op|'('
name|'image_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_delete_image_metadata
dedent|''
name|'def'
name|'fake_delete_image_metadata'
op|'('
name|'self'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'self'
op|'.'
name|'fake_get_image_metadata'
op|'('
name|'image_id'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'f'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exc'
op|'.'
name|'NotFound'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fixtures'
op|'.'
name|'remove'
op|'('
name|'f'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_delete_all
dedent|''
name|'def'
name|'fake_delete_all'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'fake_parallax_client'
op|'='
name|'FakeParallaxClient'
op|'('
name|'initial_fixtures'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'get_image_index'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_get_image_index'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'get_image_details'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_get_image_details'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'get_image_metadata'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_get_image_metadata'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'add_image_metadata'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_add_image_metadata'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'update_image_metadata'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_update_image_metadata'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'ParallaxClient'
op|','
string|"'delete_image_metadata'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_delete_image_metadata'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'image'
op|'.'
name|'glance'
op|'.'
name|'GlanceImageService'
op|','
string|"'delete_all'"
op|','
nl|'\n'
name|'fake_parallax_client'
op|'.'
name|'fake_delete_all'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeToken
dedent|''
name|'class'
name|'FakeToken'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kwargs'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequestContext
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeRequestContext'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'user'
op|','
name|'project'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'user_id'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'project_id'
op|'='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAuthDatabase
dedent|''
dedent|''
name|'class'
name|'FakeAuthDatabase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|data
indent|'    '
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_get_token
name|'def'
name|'auth_get_token'
op|'('
name|'context'
op|','
name|'token_hash'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'.'
name|'get'
op|'('
name|'token_hash'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_create_token
name|'def'
name|'auth_create_token'
op|'('
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_token'
op|'='
name|'FakeToken'
op|'('
name|'created_at'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'now'
op|'('
op|')'
op|','
op|'**'
name|'token'
op|')'
newline|'\n'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
name|'fake_token'
op|'.'
name|'token_hash'
op|']'
op|'='
name|'fake_token'
newline|'\n'
name|'return'
name|'fake_token'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|auth_destroy_token
name|'def'
name|'auth_destroy_token'
op|'('
name|'context'
op|','
name|'token'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'token'
op|'.'
name|'token_hash'
name|'in'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'['
string|"'token_hash'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeAuthManager
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeAuthManager'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|variable|auth_data
indent|'    '
name|'auth_data'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|add_user
name|'def'
name|'add_user'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'user'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'['
name|'key'
op|']'
op|'='
name|'user'
newline|'\n'
nl|'\n'
DECL|member|get_user
dedent|''
name|'def'
name|'get_user'
op|'('
name|'self'
op|','
name|'uid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'v'
op|'.'
name|'id'
op|'=='
name|'uid'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'v'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_user_from_access_key
dedent|''
name|'def'
name|'get_user_from_access_key'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'FakeAuthManager'
op|'.'
name|'auth_data'
op|'.'
name|'get'
op|'('
name|'key'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRateLimiter
dedent|''
dedent|''
name|'class'
name|'FakeRateLimiter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'application'
op|'='
name|'application'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
