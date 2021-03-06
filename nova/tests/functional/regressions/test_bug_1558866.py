begin_unit
comment|'# Copyright 2016 IBM Corp.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#      http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fixtures'
name|'as'
name|'nova_fixtures'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api'
name|'import'
name|'client'
name|'as'
name|'api_client'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
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
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'policy_fixture'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'null_kernel'"
op|','
string|"'nova.compute.api'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestServerGet
name|'class'
name|'TestServerGet'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'TestServerGet'
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
name|'useFixture'
op|'('
name|'policy_fixture'
op|'.'
name|'RealPolicyFixture'
op|'('
op|')'
op|')'
newline|'\n'
name|'api_fixture'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'nova_fixtures'
op|'.'
name|'OSAPIFixture'
op|'('
nl|'\n'
name|'api_version'
op|'='
string|"'v2.1'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'api'
op|'='
name|'api_fixture'
op|'.'
name|'api'
newline|'\n'
nl|'\n'
comment|'# the image fake backend needed for image discovery'
nl|'\n'
name|'image_service'
op|'='
name|'fake_image'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'fake_image'
op|'.'
name|'FakeImageService_reset'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(mriedem): This image has an invalid architecture metadata value'
nl|'\n'
comment|'# and is used for negative testing in the functional stack.'
nl|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'c456eb30-91d7-4f43-8f46-2efd9eccd744'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fake-image-invalid-arch'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
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
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'25165824'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'kernel_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'ramdisk_id'"
op|':'
name|'CONF'
op|'.'
name|'null_kernel'
op|','
nl|'\n'
string|"'architecture'"
op|':'
string|"'x64'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'image_id'
op|'='
name|'image_service'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flavor_id'
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
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_boot_server_with_invalid_image_meta
dedent|''
name|'def'
name|'test_boot_server_with_invalid_image_meta'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Regression test for bug #1558866.\n\n        Glance allows you to provide any architecture value for image meta\n        properties but nova validates the image metadata against the\n        nova.compute.arch.ALL values during the conversion to the ImageMeta\n        object. This test ensures we get a 400 back in that case rather than\n        a 500.\n        """'
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server1'"
op|','
nl|'\n'
name|'imageRef'
op|'='
name|'self'
op|'.'
name|'image_id'
op|','
nl|'\n'
name|'flavorRef'
op|'='
name|'self'
op|'.'
name|'flavor_id'
op|')'
newline|'\n'
name|'ex'
op|'='
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'api_client'
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
op|'{'
string|"'server'"
op|':'
name|'server'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'ex'
op|'.'
name|'response'
op|'.'
name|'status_code'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
