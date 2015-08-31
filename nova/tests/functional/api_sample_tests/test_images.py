begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'functional'
op|'.'
name|'api_sample_tests'
name|'import'
name|'api_sample_base'
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
string|"'osapi_compute_extension'"
op|','
nl|'\n'
string|"'nova.api.openstack.compute.legacy_v2.extensions'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImagesSampleJsonTest
name|'class'
name|'ImagesSampleJsonTest'
op|'('
name|'api_sample_base'
op|'.'
name|'ApiSampleTestBaseV3'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|"'images'"
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"image-metadata"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_images_list
name|'def'
name|'test_images_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of images get list request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'images-list-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_get
dedent|''
name|'def'
name|'test_image_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of one single image details request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_images_details
dedent|''
name|'def'
name|'test_images_details'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of all images details request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/detail'"
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'images-details-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_get
dedent|''
name|'def'
name|'test_image_metadata_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of an image metadata request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s/metadata'"
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|"'image_id'"
op|']'
op|'='
name|'image_id'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-get-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_post
dedent|''
name|'def'
name|'test_image_metadata_post'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample to update metadata of an image metadata request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
nl|'\n'
string|"'images/%s/metadata'"
op|'%'
name|'image_id'
op|','
nl|'\n'
string|"'image-metadata-post-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-post-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_metadata_put
dedent|''
name|'def'
name|'test_image_metadata_put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of image metadata put request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'images/%s/metadata'"
op|'%'
nl|'\n'
op|'('
name|'image_id'
op|')'
op|','
string|"'image-metadata-put-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-metadata-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_meta_key_get
dedent|''
name|'def'
name|'test_image_meta_key_get'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of an image metadata key request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|'"kernel_id"'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'images/%s/metadata/%s'"
op|'%'
op|'('
name|'image_id'
op|','
name|'key'
op|')'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-meta-key-get'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_meta_key_put
dedent|''
name|'def'
name|'test_image_meta_key_put'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api sample of image metadata key put request.'
nl|'\n'
indent|'        '
name|'image_id'
op|'='
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
string|'"auto_disk_config"'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_put'
op|'('
string|"'images/%s/metadata/%s'"
op|'%'
op|'('
name|'image_id'
op|','
name|'key'
op|')'
op|','
nl|'\n'
string|"'image-meta-key-put-req'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'image-meta-key-put-resp'"
op|','
name|'subs'
op|','
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit