begin_unit
comment|'#    Copyright 2014 IBM Corp.'
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
name|'mock'
newline|'\n'
name|'import'
name|'stevedore'
newline|'\n'
nl|'\n'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
name|'as'
name|'fake_image'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'imagehandler'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'imagehandler'
name|'import'
name|'download'
name|'as'
name|'download_imagehandler'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageHandlerTestCase
name|'class'
name|'ImageHandlerTestCase'
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
name|'ImageHandlerTestCase'
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
name|'fake_driver'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
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
name|'self'
op|'.'
name|'image_service'
op|'='
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|'='
op|'['
op|']'
newline|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|'='
op|'{'
op|'}'
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
name|'fake_image'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'ImageHandlerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_match_locations_empty
dedent|''
name|'def'
name|'test_match_locations_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
op|'['
op|']'
op|','
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'matched'
op|')'
newline|'\n'
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
name|'None'
op|','
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'matched'
op|')'
newline|'\n'
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
op|'['
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'matched'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_match_locations_location_dependent
dedent|''
name|'def'
name|'test_match_locations_location_dependent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_locations'
op|'='
op|'['
op|'{'
string|"'url'"
op|':'
string|"'fake1://url'"
op|','
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'url'"
op|':'
string|"'fake2://url'"
op|','
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
name|'fake_locations'
op|','
op|'('
string|"'fake1'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|'{'
string|"'url'"
op|':'
string|"'fake1://url'"
op|','
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
op|']'
op|','
name|'matched'
op|')'
newline|'\n'
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
name|'fake_locations'
op|','
nl|'\n'
op|'('
string|"'no_existing'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
op|']'
op|','
name|'matched'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_match_locations_location_independent
dedent|''
name|'def'
name|'test_match_locations_location_independent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_locations'
op|'='
op|'['
op|'{'
string|"'url'"
op|':'
string|"'fake1://url'"
op|','
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'url'"
op|':'
string|"'fake2://url'"
op|','
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|'}'
op|']'
newline|'\n'
name|'matched'
op|'='
name|'imagehandler'
op|'.'
name|'_match_locations'
op|'('
name|'fake_locations'
op|','
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'fake_locations'
op|','
name|'matched'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_handler_association_hooks
dedent|''
name|'def'
name|'test_image_handler_association_hooks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'handler'
op|'='
string|"'fake_handler'"
newline|'\n'
name|'path'
op|'='
string|"'fake/image/path'"
newline|'\n'
name|'location'
op|'='
string|"'fake://image_location_url'"
newline|'\n'
name|'image_meta'
op|'='
string|"'fake_image_meta'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'_image_handler_asso'
op|'('
name|'handler'
op|','
name|'path'
op|','
name|'location'
op|','
name|'image_meta'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
name|'path'
op|','
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'('
name|'handler'
op|','
name|'location'
op|','
name|'image_meta'
op|')'
op|','
nl|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|'['
name|'path'
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'_image_handler_disasso'
op|'('
string|"'another_handler'"
op|','
nl|'\n'
string|"'another/fake/image/path'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'_image_handler_disasso'
op|'('
name|'handler'
op|','
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_load_image_handlers
dedent|''
name|'def'
name|'test_load_image_handlers'
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
name|'image_handlers'
op|'='
op|'['
string|"'download'"
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'load_image_handlers'
op|'('
name|'self'
op|'.'
name|'fake_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'download_imagehandler'
op|'.'
name|'DownloadImageHandler'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_load_image_handlers_with_invalid_handler_name
dedent|''
name|'def'
name|'test_load_image_handlers_with_invalid_handler_name'
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
name|'image_handlers'
op|'='
op|'['
string|"'invaild1'"
op|','
string|"'download'"
op|','
string|"'invaild2'"
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'load_image_handlers'
op|'('
name|'self'
op|'.'
name|'fake_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsInstance'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'download_imagehandler'
op|'.'
name|'DownloadImageHandler'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
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
name|'stevedore'
op|'.'
name|'extension'
op|','
string|"'ExtensionManager'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'stevedore'
op|'.'
name|'driver'
op|','
string|"'DriverManager'"
op|')'
newline|'\n'
DECL|member|test_load_image_handlers_with_deduplicating
name|'def'
name|'test_load_image_handlers_with_deduplicating'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_DriverManager'
op|','
nl|'\n'
name|'mock_ExtensionManager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'handlers'
op|'='
op|'['
string|"'handler1'"
op|','
string|"'handler2'"
op|','
string|"'handler3'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_fake_stevedore_driver_manager
name|'def'
name|'_fake_stevedore_driver_manager'
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
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|'**'
op|'{'
string|"'driver'"
op|':'
name|'kwargs'
op|'['
string|"'name'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mock_ExtensionManager'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'names.return_value'"
op|':'
name|'handlers'
op|'}'
op|')'
newline|'\n'
name|'mock_DriverManager'
op|'.'
name|'side_effect'
op|'='
name|'_fake_stevedore_driver_manager'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'image_handlers'
op|'='
op|'['
string|"'invaild1'"
op|','
string|"'handler1  '"
op|','
string|"'  handler3'"
op|','
nl|'\n'
string|"'invaild2'"
op|','
string|"'  handler2  '"
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'load_image_handlers'
op|'('
name|'self'
op|'.'
name|'fake_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
op|')'
newline|'\n'
name|'for'
name|'handler'
name|'in'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'handler'
name|'in'
name|'handlers'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'handler1'"
op|','
string|"'handler3'"
op|','
string|"'handler2'"
op|']'
op|','
nl|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
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
name|'stevedore'
op|'.'
name|'extension'
op|','
string|"'ExtensionManager'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'stevedore'
op|'.'
name|'driver'
op|','
string|"'DriverManager'"
op|')'
newline|'\n'
DECL|member|test_load_image_handlers_with_load_handler_failure
name|'def'
name|'test_load_image_handlers_with_load_handler_failure'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_DriverManager'
op|','
nl|'\n'
name|'mock_ExtensionManager'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'handlers'
op|'='
op|'['
string|"'raise_exception'"
op|','
string|"'download'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_fake_stevedore_driver_manager
name|'def'
name|'_fake_stevedore_driver_manager'
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
name|'if'
name|'kwargs'
op|'['
string|"'name'"
op|']'
op|'=='
string|"'raise_exception'"
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
string|"'handler failed to initialize.'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|'**'
op|'{'
string|"'driver'"
op|':'
name|'kwargs'
op|'['
string|"'name'"
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mock_ExtensionManager'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'names.return_value'"
op|':'
name|'handlers'
op|'}'
op|')'
newline|'\n'
name|'mock_DriverManager'
op|'.'
name|'side_effect'
op|'='
name|'_fake_stevedore_driver_manager'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'image_handlers'
op|'='
op|'['
string|"'raise_exception'"
op|','
string|"'download'"
op|','
nl|'\n'
string|"'raise_exception'"
op|','
string|"'download'"
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'load_image_handlers'
op|'('
name|'self'
op|'.'
name|'fake_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
string|"'download'"
op|']'
op|','
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
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
name|'download_imagehandler'
op|'.'
name|'DownloadImageHandler'
op|','
nl|'\n'
string|"'_fetch_image'"
op|')'
newline|'\n'
DECL|member|_handle_image_without_associated_handle
name|'def'
name|'_handle_image_without_associated_handle'
op|'('
name|'self'
op|','
name|'image_id'
op|','
nl|'\n'
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
nl|'\n'
name|'expected_handled_path'
op|','
nl|'\n'
name|'mock__fetch_image'
op|')'
op|':'
newline|'\n'
DECL|function|_fake_handler_fetch
indent|'        '
name|'def'
name|'_fake_handler_fetch'
op|'('
name|'context'
op|','
name|'image_meta'
op|','
name|'path'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'location'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'location'
op|'=='
name|'expected_handled_location'
newline|'\n'
nl|'\n'
dedent|''
name|'mock__fetch_image'
op|'.'
name|'side_effect'
op|'='
name|'_fake_handler_fetch'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'image_handlers'
op|'='
op|'['
string|"'download'"
op|']'
op|')'
newline|'\n'
name|'imagehandler'
op|'.'
name|'load_image_handlers'
op|'('
name|'self'
op|'.'
name|'fake_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'check_left_loc_count'
op|'='
name|'expected_handled_location'
name|'in'
name|'expected_locations'
newline|'\n'
name|'if'
name|'check_left_loc_count'
op|':'
newline|'\n'
indent|'            '
name|'unused_location_count'
op|'='
op|'('
name|'len'
op|'('
name|'expected_locations'
op|')'
op|'-'
nl|'\n'
name|'expected_locations'
op|'.'
name|'index'
op|'('
name|'expected_handled_location'
op|')'
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_fetch_image'
op|'('
name|'image_id'
op|','
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'check_left_loc_count'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'unused_location_count'
op|','
name|'len'
op|'('
name|'expected_locations'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
op|'('
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|'['
number|'0'
op|']'
op|','
name|'expected_handled_location'
op|')'
op|','
nl|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|'['
name|'expected_handled_path'
op|']'
op|'['
op|':'
number|'2'
op|']'
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
name|'download_imagehandler'
op|'.'
name|'DownloadImageHandler'
op|','
nl|'\n'
string|"'_fetch_image'"
op|')'
newline|'\n'
DECL|member|_fetch_image
name|'def'
name|'_fetch_image'
op|'('
name|'self'
op|','
name|'image_id'
op|','
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
name|'expected_handled_path'
op|','
nl|'\n'
name|'mock__fetch_image'
op|')'
op|':'
newline|'\n'
DECL|function|_fake_handler_fetch
indent|'        '
name|'def'
name|'_fake_handler_fetch'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_meta'
op|','
name|'path'
op|','
nl|'\n'
name|'user_id'
op|'='
name|'None'
op|','
name|'project_id'
op|'='
name|'None'
op|','
name|'location'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'location'
op|'=='
name|'expected_handled_location'
newline|'\n'
nl|'\n'
dedent|''
name|'mock__fetch_image'
op|'.'
name|'side_effect'
op|'='
name|'_fake_handler_fetch'
newline|'\n'
nl|'\n'
name|'for'
name|'handler_context'
name|'in'
name|'imagehandler'
op|'.'
name|'handle_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'image_id'
op|','
name|'target_path'
op|'='
name|'expected_handled_path'
op|')'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'handler'
op|','
name|'loc'
op|','
name|'image_meta'
op|')'
op|'='
name|'handler_context'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'handler'
op|','
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'if'
op|'('
name|'len'
op|'('
name|'expected_locations'
op|')'
op|'>'
number|'0'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_locations'
op|'.'
name|'pop'
op|'('
number|'0'
op|')'
op|','
name|'loc'
op|')'
newline|'\n'
dedent|''
name|'handler'
op|'.'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'image_meta'
op|','
nl|'\n'
name|'expected_handled_path'
op|','
name|'location'
op|'='
name|'loc'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_handle_image_without_associated_handle
dedent|''
dedent|''
name|'def'
name|'test_handle_image_without_associated_handle'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
newline|'\n'
name|'expected_locations'
op|'='
op|'['
string|"'fake_location'"
op|','
string|"'fake_location2'"
op|']'
newline|'\n'
comment|'# Image will be handled successful on second location.'
nl|'\n'
name|'expected_handled_location'
op|'='
string|"'fake_location2'"
newline|'\n'
name|'expected_handled_path'
op|'='
string|"'fake/image/path2'"
newline|'\n'
name|'self'
op|'.'
name|'_handle_image_without_associated_handle'
op|'('
name|'image_id'
op|','
nl|'\n'
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
nl|'\n'
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_handle_image_with_associated_handler
dedent|''
name|'def'
name|'test_handle_image_with_associated_handler'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'get_locations_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|_fake_get_locations
name|'def'
name|'_fake_get_locations'
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
name|'get_locations_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'image_id'
op|'='
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
newline|'\n'
name|'expected_locations'
op|'='
op|'['
string|"'fake_location'"
op|','
string|"'fake_location2'"
op|']'
newline|'\n'
name|'expected_handled_location'
op|'='
string|"'fake_location'"
newline|'\n'
name|'expected_handled_path'
op|'='
string|"'fake/image/path'"
newline|'\n'
nl|'\n'
comment|'# 1) Handle image without cached association information'
nl|'\n'
name|'self'
op|'.'
name|'_handle_image_without_associated_handle'
op|'('
name|'image_id'
op|','
nl|'\n'
name|'list'
op|'('
name|'expected_locations'
op|')'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
nl|'\n'
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'get_locations'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'side_effect'"
op|':'
name|'_fake_get_locations'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# 2) Handle image with cached association information'
nl|'\n'
name|'self'
op|'.'
name|'_fetch_image'
op|'('
name|'image_id'
op|','
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'self'
op|'.'
name|'get_locations_called'
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'get_locations_called'
newline|'\n'
nl|'\n'
DECL|member|test_handle_image_with_association_discarded
dedent|''
name|'def'
name|'test_handle_image_with_association_discarded'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'get_locations_called'
op|'='
name|'False'
newline|'\n'
name|'original_get_locations'
op|'='
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'get_locations'
newline|'\n'
nl|'\n'
DECL|function|_fake_get_locations
name|'def'
name|'_fake_get_locations'
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
name|'get_locations_called'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'original_get_locations'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_id'
op|'='
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
newline|'\n'
name|'expected_locations'
op|'='
op|'['
string|"'fake_location'"
op|','
string|"'fake_location2'"
op|']'
newline|'\n'
name|'expected_handled_location'
op|'='
string|"'fake_location'"
newline|'\n'
name|'expected_handled_path'
op|'='
string|"'fake/image/path'"
newline|'\n'
nl|'\n'
comment|'# 1) Handle image without cached association information'
nl|'\n'
name|'self'
op|'.'
name|'_handle_image_without_associated_handle'
op|'('
name|'image_id'
op|','
nl|'\n'
name|'list'
op|'('
name|'expected_locations'
op|')'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
nl|'\n'
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# 2) Clear cached association information'
nl|'\n'
name|'imagehandler'
op|'.'
name|'_IMAGE_HANDLERS_ASSO'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
comment|'# 3) Handle image with discarded association information'
nl|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'get_locations'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
op|'**'
op|'{'
string|"'side_effect'"
op|':'
name|'_fake_get_locations'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_fetch_image'
op|'('
name|'image_id'
op|','
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
name|'expected_handled_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'get_locations_called'
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'get_locations_called'
newline|'\n'
nl|'\n'
DECL|member|test_handle_image_no_handler_available
dedent|''
name|'def'
name|'test_handle_image_no_handler_available'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
string|"'155d900f-4e14-4e4c-a73d-069cbf4541e6'"
newline|'\n'
name|'expected_locations'
op|'='
op|'['
string|"'fake_location'"
op|','
string|"'fake_location2'"
op|']'
newline|'\n'
name|'expected_handled_location'
op|'='
string|"'fake_location3'"
newline|'\n'
name|'expected_handled_path'
op|'='
string|"'fake/image/path'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NoImageHandlerAvailable'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_handle_image_without_associated_handle'
op|','
nl|'\n'
name|'image_id'
op|','
nl|'\n'
name|'expected_locations'
op|','
nl|'\n'
name|'expected_handled_location'
op|','
nl|'\n'
name|'expected_handled_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
