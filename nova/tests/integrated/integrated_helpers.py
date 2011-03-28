begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
string|'"""\nProvides common functionality for integrated unit tests\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
nl|'\n'
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
name|'import'
name|'service'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
comment|'# For the flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'api'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.tests.integrated'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_random_alphanumeric
name|'def'
name|'generate_random_alphanumeric'
op|'('
name|'length'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random alphanumeric string of specified length"""'
newline|'\n'
name|'return'
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
name|'ascii_uppercase'
op|'+'
name|'string'
op|'.'
name|'digits'
op|')'
nl|'\n'
name|'for'
name|'_x'
name|'in'
name|'range'
op|'('
name|'length'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_random_numeric
dedent|''
name|'def'
name|'generate_random_numeric'
op|'('
name|'length'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random numeric string of specified length"""'
newline|'\n'
name|'return'
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
name|'digits'
op|')'
nl|'\n'
name|'for'
name|'_x'
name|'in'
name|'range'
op|'('
name|'length'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|generate_new_element
dedent|''
name|'def'
name|'generate_new_element'
op|'('
name|'items'
op|','
name|'prefix'
op|','
name|'numeric'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates a random string with prefix, that is not in \'items\' list"""'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'numeric'
op|':'
newline|'\n'
indent|'            '
name|'candidate'
op|'='
name|'prefix'
op|'+'
name|'generate_random_numeric'
op|'('
number|'8'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'candidate'
op|'='
name|'prefix'
op|'+'
name|'generate_random_alphanumeric'
op|'('
number|'8'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'candidate'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'candidate'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Random collision on %s"'
op|'%'
name|'candidate'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestUser
dedent|''
dedent|''
name|'class'
name|'TestUser'
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
name|'name'
op|','
name|'secret'
op|','
name|'auth_url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'name'
op|'='
name|'name'
newline|'\n'
name|'self'
op|'.'
name|'secret'
op|'='
name|'secret'
newline|'\n'
name|'self'
op|'.'
name|'auth_url'
op|'='
name|'auth_url'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'auth_url'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"auth_url is required"'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'openstack_api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
name|'self'
op|'.'
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'secret'
op|','
nl|'\n'
name|'self'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_unused_server_name
dedent|''
name|'def'
name|'get_unused_server_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'servers'
op|'='
name|'self'
op|'.'
name|'openstack_api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'server_names'
op|'='
op|'['
name|'server'
op|'['
string|"'name'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'return'
name|'generate_new_element'
op|'('
name|'server_names'
op|','
string|"'server'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_invalid_image
dedent|''
name|'def'
name|'get_invalid_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'openstack_api'
op|'.'
name|'get_images'
op|'('
op|')'
newline|'\n'
name|'image_ids'
op|'='
op|'['
name|'image'
op|'['
string|"'id'"
op|']'
name|'for'
name|'image'
name|'in'
name|'images'
op|']'
newline|'\n'
name|'return'
name|'generate_new_element'
op|'('
name|'image_ids'
op|','
string|"''"
op|','
name|'numeric'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_valid_image
dedent|''
name|'def'
name|'get_valid_image'
op|'('
name|'self'
op|','
name|'create'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'images'
op|'='
name|'self'
op|'.'
name|'openstack_api'
op|'.'
name|'get_images'
op|'('
op|')'
newline|'\n'
name|'if'
name|'create'
name|'and'
name|'not'
name|'images'
op|':'
newline|'\n'
comment|'#TODO(justinsb): No way currently to create an image through API'
nl|'\n'
comment|'#created_image = self.openstack_api.post_image(image)'
nl|'\n'
comment|'#images.append(created_image)'
nl|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|'"No way to create an image through API"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'images'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'images'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IntegratedUnitTestContext
dedent|''
dedent|''
name|'class'
name|'IntegratedUnitTestContext'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'auth_manager'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api_service'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'auth_url'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'project_name'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'test_user'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup
dedent|''
name|'def'
name|'setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_start_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_test_user'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_test_user
dedent|''
name|'def'
name|'_create_test_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_user'
op|'='
name|'self'
op|'.'
name|'_create_unittest_user'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# No way to currently pass this through the OpenStack API'
nl|'\n'
name|'self'
op|'.'
name|'project_name'
op|'='
string|"'openstack'"
newline|'\n'
name|'self'
op|'.'
name|'_configure_project'
op|'('
name|'self'
op|'.'
name|'project_name'
op|','
name|'self'
op|'.'
name|'test_user'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_services
dedent|''
name|'def'
name|'_start_services'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_start_compute_service'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_start_volume_service'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_start_scheduler_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"#NOTE(justinsb): There's a bug here which is eluding me..."
nl|'\n'
comment|'#  If we start the network_service, all is good, but then subsequent'
nl|'\n'
comment|'#  tests fail: CloudTestCase.test_ajax_console in particular.'
nl|'\n'
comment|'#self._start_network_service()'
nl|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_start_api_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_compute_service
dedent|''
name|'def'
name|'_start_compute_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'compute_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-compute'"
op|')'
newline|'\n'
name|'compute_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'compute_service'
op|')'
newline|'\n'
name|'return'
name|'compute_service'
newline|'\n'
nl|'\n'
DECL|member|_start_network_service
dedent|''
name|'def'
name|'_start_network_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'network_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-network'"
op|')'
newline|'\n'
name|'network_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'network_service'
op|')'
newline|'\n'
name|'return'
name|'network_service'
newline|'\n'
nl|'\n'
DECL|member|_start_volume_service
dedent|''
name|'def'
name|'_start_volume_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'volume_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-volume'"
op|')'
newline|'\n'
name|'volume_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'volume_service'
op|')'
newline|'\n'
name|'return'
name|'volume_service'
newline|'\n'
nl|'\n'
DECL|member|_start_scheduler_service
dedent|''
name|'def'
name|'_start_scheduler_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'scheduler_service'
op|'='
name|'service'
op|'.'
name|'Service'
op|'.'
name|'create'
op|'('
name|'binary'
op|'='
string|"'nova-scheduler'"
op|')'
newline|'\n'
name|'scheduler_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'services'
op|'.'
name|'append'
op|'('
name|'scheduler_service'
op|')'
newline|'\n'
name|'return'
name|'scheduler_service'
newline|'\n'
nl|'\n'
DECL|member|cleanup
dedent|''
name|'def'
name|'cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'test_user'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'svc'
name|'in'
name|'self'
op|'.'
name|'services'
op|':'
newline|'\n'
indent|'            '
name|'svc'
op|'.'
name|'kill'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'services'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|_create_unittest_user
dedent|''
name|'def'
name|'_create_unittest_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'users'
op|'='
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'get_users'
op|'('
op|')'
newline|'\n'
name|'user_names'
op|'='
op|'['
name|'user'
op|'.'
name|'name'
name|'for'
name|'user'
name|'in'
name|'users'
op|']'
newline|'\n'
name|'auth_name'
op|'='
name|'generate_new_element'
op|'('
name|'user_names'
op|','
string|"'unittest_user_'"
op|')'
newline|'\n'
name|'auth_key'
op|'='
name|'generate_random_alphanumeric'
op|'('
number|'16'
op|')'
newline|'\n'
nl|'\n'
comment|"# Right now there's a bug where auth_name and auth_key are reversed"
nl|'\n'
comment|'# bug732907'
nl|'\n'
name|'auth_key'
op|'='
name|'auth_name'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'create_user'
op|'('
name|'auth_name'
op|','
name|'auth_name'
op|','
name|'auth_key'
op|','
name|'False'
op|')'
newline|'\n'
name|'return'
name|'TestUser'
op|'('
name|'auth_name'
op|','
name|'auth_key'
op|','
name|'self'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_configure_project
dedent|''
name|'def'
name|'_configure_project'
op|'('
name|'self'
op|','
name|'project_name'
op|','
name|'user'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'projects'
op|'='
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'get_projects'
op|'('
op|')'
newline|'\n'
name|'project_names'
op|'='
op|'['
name|'project'
op|'.'
name|'name'
name|'for'
name|'project'
name|'in'
name|'projects'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'project_name'
name|'in'
name|'project_names'
op|':'
newline|'\n'
indent|'            '
name|'project'
op|'='
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'create_project'
op|'('
name|'project_name'
op|','
nl|'\n'
name|'user'
op|'.'
name|'name'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
name|'member_users'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'auth_manager'
op|'.'
name|'add_to_project'
op|'('
name|'user'
op|'.'
name|'name'
op|','
name|'project_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_api_service
dedent|''
dedent|''
name|'def'
name|'_start_api_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'api_service'
op|'='
name|'service'
op|'.'
name|'ApiService'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'api_service'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'api_service'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"API Service was None"'
op|')'
newline|'\n'
nl|'\n'
comment|"#NOTE(justinsb): The API service doesn't have a kill method yet,"
nl|'\n'
comment|'#  so we treat it separately'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'api_service'
op|'='
name|'api_service'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'auth_url'
op|'='
string|"'http://localhost:8774/v1.1'"
newline|'\n'
nl|'\n'
name|'return'
name|'api_service'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_IntegratedTestBase
dedent|''
dedent|''
name|'class'
name|'_IntegratedTestBase'
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
name|'_IntegratedTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'='
name|'self'
op|'.'
name|'_get_flags'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
op|'**'
name|'f'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'IntegratedUnitTestContext'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'self'
op|'.'
name|'context'
op|'.'
name|'test_user'
newline|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'openstack_api'
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
name|'self'
op|'.'
name|'context'
op|'.'
name|'cleanup'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'_IntegratedTestBase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_flags
dedent|''
name|'def'
name|'_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""An opportunity to setup flags, before the services are started"""'
newline|'\n'
name|'f'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'f'
op|'['
string|"'image_service'"
op|']'
op|'='
string|"'nova.image.fake.MockImageService'"
newline|'\n'
name|'f'
op|'['
string|"'fake_network'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'f'
newline|'\n'
nl|'\n'
DECL|member|_build_minimal_create_server_request
dedent|''
name|'def'
name|'_build_minimal_create_server_request'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'get_valid_image'
op|'('
name|'create'
op|'='
name|'True'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Image: %s"'
op|'%'
name|'image'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'imageRef'"
name|'in'
name|'image'
op|':'
newline|'\n'
indent|'            '
name|'image_ref'
op|'='
name|'image'
op|'['
string|"'imageRef'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|"#NOTE(justinsb): The imageRef code hasn't yet landed"
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
string|'"imageRef not yet in images output"'
op|')'
newline|'\n'
name|'image_ref'
op|'='
name|'image'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'#TODO(justinsb): This is FUBAR'
nl|'\n'
name|'image_ref'
op|'='
name|'abs'
op|'('
name|'hash'
op|'('
name|'image_ref'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'image_ref'
op|'='
string|"'http://fake.server/%s'"
op|'%'
name|'image_ref'
newline|'\n'
nl|'\n'
comment|'# We now have a valid imageId'
nl|'\n'
dedent|''
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'image_ref'
newline|'\n'
nl|'\n'
comment|'# Set a valid flavorId'
nl|'\n'
name|'flavor'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_flavors'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Using flavor: %s"'
op|'%'
name|'flavor'
op|')'
newline|'\n'
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|'='
string|"'http://fake.server/%s'"
op|'%'
name|'flavor'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Set a valid server name'
nl|'\n'
name|'server_name'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'get_unused_server_name'
op|'('
op|')'
newline|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
name|'server_name'
newline|'\n'
nl|'\n'
name|'return'
name|'server'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
