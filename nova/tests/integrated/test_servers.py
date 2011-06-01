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
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'import'
name|'integrated_helpers'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'verbose'
op|'='
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersTest
name|'class'
name|'ServersTest'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_servers
indent|'    '
name|'def'
name|'test_get_servers'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check that listing servers works."""'
newline|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'for'
name|'server'
name|'in'
name|'servers'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"server: %s"'
op|'%'
name|'server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_server
dedent|''
dedent|''
name|'def'
name|'test_create_and_delete_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates and deletes a server."""'
newline|'\n'
nl|'\n'
comment|'# Create server'
nl|'\n'
nl|'\n'
comment|'# Build the server data gradually, checking errors along the way'
nl|'\n'
name|'server'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'good_server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
comment|'# Without an imageRef, this throws 500.'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# With an invalid imageRef, this throws 500.'
nl|'\n'
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'self'
op|'.'
name|'user'
op|'.'
name|'get_invalid_image'
op|'('
op|')'
newline|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# Add a valid imageId/imageRef'
nl|'\n'
name|'server'
op|'['
string|"'imageId'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'imageId'"
op|')'
newline|'\n'
name|'server'
op|'['
string|"'imageRef'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'imageRef'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Without flavorId, this throws 500'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set a valid flavorId/flavorRef'
nl|'\n'
name|'server'
op|'['
string|"'flavorRef'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'flavorRef'"
op|')'
newline|'\n'
name|'server'
op|'['
string|"'flavorId'"
op|']'
op|'='
name|'good_server'
op|'.'
name|'get'
op|'('
string|"'flavorId'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Without a name, this throws 500'
nl|'\n'
comment|'# TODO(justinsb): Check whatever the spec says should be thrown here'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|','
name|'post'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set a valid server name'
nl|'\n'
name|'server'
op|'['
string|"'name'"
op|']'
op|'='
name|'good_server'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|"# Check it's there"
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should also be in the all-servers list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
op|')'
newline|'\n'
name|'server_ids'
op|'='
op|'['
name|'server'
op|'['
string|"'id'"
op|']'
name|'for'
name|'server'
name|'in'
name|'servers'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server_id'
name|'in'
name|'server_ids'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait (briefly) for creation'
nl|'\n'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'found_server'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'build'"
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"found server: %s"'
op|'%'
name|'found_server'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'retries'
op|'='
name|'retries'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'retries'
op|'>'
number|'5'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
nl|'\n'
comment|'# It should be available...'
nl|'\n'
comment|"# TODO(justinsb): Mock doesn't yet do this..."
nl|'\n'
comment|"#self.assertEqual('available', found_server['status'])"
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_delete_server
dedent|''
name|'def'
name|'_delete_server'
op|'('
name|'self'
op|','
name|'server_id'
op|')'
op|':'
newline|'\n'
comment|'# Delete the server'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'api'
op|'.'
name|'delete_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Wait (briefly) for deletion'
nl|'\n'
name|'for'
name|'_retries'
name|'in'
name|'range'
op|'('
number|'5'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'server_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'client'
op|'.'
name|'OpenStackApiNotFoundException'
op|':'
newline|'\n'
indent|'                '
name|'found_server'
op|'='
name|'None'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got 404, proceeding"'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Found_server=%s"'
op|'%'
name|'found_server'
op|')'
newline|'\n'
nl|'\n'
comment|"# TODO(justinsb): Mock doesn't yet do accurate state changes"
nl|'\n'
comment|"#if found_server['status'] != 'deleting':"
nl|'\n'
comment|'#    break'
nl|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|'# Should be gone'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_server'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_with_metadata
dedent|''
name|'def'
name|'test_create_server_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a server with metadata."""'
newline|'\n'
nl|'\n'
comment|'# Build the server data gradually, checking errors along the way'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'30'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key_%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value_%s'"
op|'%'
name|'i'
newline|'\n'
nl|'\n'
dedent|''
name|'server'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Reenable when bug fixed'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'created_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
comment|"# Check it's there"
nl|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The server should also be in the all-servers details list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'True'
op|')'
newline|'\n'
name|'server_map'
op|'='
name|'dict'
op|'('
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|','
name|'server'
op|')'
name|'for'
name|'server'
name|'in'
name|'servers'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'server_map'
op|'.'
name|'get'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found_server'
op|')'
newline|'\n'
comment|'# Details do include metadata'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# The server should also be in the all-servers summary list'
nl|'\n'
name|'servers'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_servers'
op|'('
name|'detail'
op|'='
name|'False'
op|')'
newline|'\n'
name|'server_map'
op|'='
name|'dict'
op|'('
op|'('
name|'server'
op|'['
string|"'id'"
op|']'
op|','
name|'server'
op|')'
name|'for'
name|'server'
name|'in'
name|'servers'
op|')'
newline|'\n'
name|'found_server'
op|'='
name|'server_map'
op|'.'
name|'get'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'found_server'
op|')'
newline|'\n'
comment|'# Summary should not include metadata'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_rebuild_server
dedent|''
name|'def'
name|'test_create_and_rebuild_server'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rebuild a server."""'
newline|'\n'
nl|'\n'
comment|'# create a server with initially has no metadata'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'server_post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# rebuild the server with metadata'
nl|'\n'
name|'post'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"imageRef"'
op|':'
string|'"https://localhost/v1.1/32278/images/2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"blah"'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rebuilt server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
op|'}'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'blah'"
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_rebuild_server_with_metadata
dedent|''
name|'def'
name|'test_create_and_rebuild_server_with_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rebuild a server with metadata."""'
newline|'\n'
nl|'\n'
comment|'# create a server with initially has no metadata'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'server_post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# rebuild the server with metadata'
nl|'\n'
name|'post'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"imageRef"'
op|':'
string|'"https://localhost/v1.1/32278/images/2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"blah"'
op|'}'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'30'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key_%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value_%s'"
op|'%'
name|'i'
newline|'\n'
nl|'\n'
dedent|''
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rebuilt server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'blah'"
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_rebuild_server_with_metadata_removal
dedent|''
name|'def'
name|'test_create_and_rebuild_server_with_metadata_removal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Rebuild a server with metadata."""'
newline|'\n'
nl|'\n'
comment|'# create a server with initially has no metadata'
nl|'\n'
name|'server'
op|'='
name|'self'
op|'.'
name|'_build_minimal_create_server_request'
op|'('
op|')'
newline|'\n'
name|'server_post'
op|'='
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'30'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'metadata'
op|'['
string|"'key_%s'"
op|'%'
name|'i'
op|']'
op|'='
string|"'value_%s'"
op|'%'
name|'i'
newline|'\n'
nl|'\n'
dedent|''
name|'server_post'
op|'['
string|"'server'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'created_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server'
op|'('
name|'server_post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"created_server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'created_server_id'
op|'='
name|'created_server'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
comment|'# rebuild the server with metadata'
nl|'\n'
name|'post'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'='
op|'{'
nl|'\n'
string|'"imageRef"'
op|':'
string|'"https://localhost/v1.1/32278/images/2"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"blah"'
op|'}'
newline|'\n'
nl|'\n'
name|'metadata'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'post'
op|'['
string|"'rebuild'"
op|']'
op|'['
string|"'metadata'"
op|']'
op|'='
name|'metadata'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'.'
name|'post_server_action'
op|'('
name|'created_server_id'
op|','
name|'post'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rebuilt server: %s"'
op|'%'
name|'created_server'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'created_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'found_server'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'created_server_id'
op|','
name|'found_server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'metadata'
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'blah'"
op|','
name|'found_server'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Cleanup'
nl|'\n'
name|'self'
op|'.'
name|'_delete_server'
op|'('
name|'created_server_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
