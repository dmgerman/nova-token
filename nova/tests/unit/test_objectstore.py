begin_unit
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
string|'"""\nUnittets for S3 objectstore clone.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'from'
name|'boto'
name|'import'
name|'exception'
name|'as'
name|'boto_exception'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'s3'
name|'import'
name|'connection'
name|'as'
name|'s3'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'s3server'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
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
string|"'s3_host'"
op|','
string|"'nova.image.s3'"
op|')'
newline|'\n'
nl|'\n'
comment|"# Create a unique temporary directory. We don't delete after test to"
nl|'\n'
comment|'# allow checking the contents after running tests. Users and/or tools'
nl|'\n'
comment|'# running the tests need to remove the tests directories.'
nl|'\n'
DECL|variable|OSS_TEMPDIR
name|'OSS_TEMPDIR'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'prefix'
op|'='
string|"'test_oss-'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Create bucket/images path'
nl|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'OSS_TEMPDIR'
op|','
string|"'images'"
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'makedirs'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'OSS_TEMPDIR'
op|','
string|"'buckets'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|S3APITestCase
name|'class'
name|'S3APITestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Test objectstore through S3 API."""'
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
string|'"""Setup users, projects, and start a test server."""'
newline|'\n'
name|'super'
op|'('
name|'S3APITestCase'
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
name|'flags'
op|'('
name|'buckets_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'OSS_TEMPDIR'
op|','
string|"'buckets'"
op|')'
op|','
nl|'\n'
name|'s3_host'
op|'='
string|"'127.0.0.1'"
op|')'
newline|'\n'
nl|'\n'
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'CONF'
op|'.'
name|'buckets_path'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'CONF'
op|'.'
name|'buckets_path'
op|')'
newline|'\n'
nl|'\n'
name|'router'
op|'='
name|'s3server'
op|'.'
name|'S3Application'
op|'('
name|'CONF'
op|'.'
name|'buckets_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'='
name|'wsgi'
op|'.'
name|'Server'
op|'('
string|'"S3 Objectstore"'
op|','
nl|'\n'
name|'router'
op|','
nl|'\n'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'s3_host'
op|','
nl|'\n'
name|'port'
op|'='
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'has_section'
op|'('
string|"'Boto'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'boto'
op|'.'
name|'config'
op|'.'
name|'add_section'
op|'('
string|"'Boto'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'boto'
op|'.'
name|'config'
op|'.'
name|'set'
op|'('
string|"'Boto'"
op|','
string|"'num_retries'"
op|','
string|"'0'"
op|')'
newline|'\n'
name|'conn'
op|'='
name|'s3'
op|'.'
name|'S3Connection'
op|'('
name|'aws_access_key_id'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
string|"'fake'"
op|','
nl|'\n'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'s3_host'
op|','
nl|'\n'
name|'port'
op|'='
name|'self'
op|'.'
name|'server'
op|'.'
name|'port'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'calling_format'
op|'='
name|'s3'
op|'.'
name|'OrdinaryCallingFormat'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'='
name|'conn'
newline|'\n'
nl|'\n'
DECL|function|get_http_connection
name|'def'
name|'get_http_connection'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Get a new S3 connection, don\'t attempt to reuse connections."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'new_http_connection'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_http_connection'
op|'='
name|'get_http_connection'
newline|'\n'
nl|'\n'
DECL|member|_ensure_no_buckets
dedent|''
name|'def'
name|'_ensure_no_buckets'
op|'('
name|'self'
op|','
name|'buckets'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'buckets'
op|')'
op|','
number|'0'
op|','
string|'"Bucket list was not empty"'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_ensure_one_bucket
dedent|''
name|'def'
name|'_ensure_one_bucket'
op|'('
name|'self'
op|','
name|'buckets'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'buckets'
op|')'
op|','
number|'1'
op|','
nl|'\n'
string|'"Bucket list didn\'t have exactly one element in it"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'buckets'
op|'['
number|'0'
op|']'
op|'.'
name|'name'
op|','
name|'name'
op|','
string|'"Wrong name"'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|test_list_buckets
dedent|''
name|'def'
name|'test_list_buckets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Make sure we are starting with no buckets.'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'_ensure_no_buckets'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_buckets'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_delete_bucket
dedent|''
name|'def'
name|'test_create_and_delete_bucket'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test bucket creation and deletion.'
nl|'\n'
indent|'        '
name|'bucket_name'
op|'='
string|"'testbucket'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_one_bucket'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_buckets'
op|'('
op|')'
op|','
name|'bucket_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'delete_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_ensure_no_buckets'
op|'('
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_all_buckets'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_bucket_and_key_and_delete_key_again
dedent|''
name|'def'
name|'test_create_bucket_and_key_and_delete_key_again'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Test key operations on buckets.'
nl|'\n'
indent|'        '
name|'bucket_name'
op|'='
string|"'testbucket'"
newline|'\n'
name|'key_name'
op|'='
string|"'somekey'"
newline|'\n'
name|'key_contents'
op|'='
string|"'somekey'"
newline|'\n'
nl|'\n'
name|'b'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'create_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'k'
op|'='
name|'b'
op|'.'
name|'new_key'
op|'('
name|'key_name'
op|')'
newline|'\n'
name|'k'
op|'.'
name|'set_contents_from_string'
op|'('
name|'key_contents'
op|')'
newline|'\n'
nl|'\n'
name|'bucket'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure the contents are correct'
nl|'\n'
name|'key'
op|'='
name|'bucket'
op|'.'
name|'get_key'
op|'('
name|'key_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'key'
op|'.'
name|'get_contents_as_string'
op|'('
op|')'
op|','
name|'key_contents'
op|','
nl|'\n'
string|'"Bad contents"'
op|')'
newline|'\n'
nl|'\n'
comment|'# delete the key'
nl|'\n'
name|'key'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_ensure_no_buckets'
op|'('
name|'bucket'
op|'.'
name|'get_all_keys'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unknown_bucket
dedent|''
name|'def'
name|'test_unknown_bucket'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(unicell): Since Boto v2.25.0, the underlying implementation'
nl|'\n'
comment|'# of get_bucket method changed from GET to HEAD.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Prior to v2.25.0, default validate=True fetched a list of keys in the'
nl|'\n'
comment|'# bucket and raises S3ResponseError. As a side effect of switching to'
nl|'\n'
comment|'# HEAD request, get_bucket call now generates less error message.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# To keep original semantics, additional get_all_keys call is'
nl|'\n'
comment|'# suggestted per Boto document. This case tests both validate=False and'
nl|'\n'
comment|'# validate=True case for completeness.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://docs.pythonboto.org/en/latest/releasenotes/v2.25.0.html'
nl|'\n'
comment|'# http://docs.pythonboto.org/en/latest/s3_tut.html#accessing-a-bucket'
nl|'\n'
indent|'        '
name|'bucket_name'
op|'='
string|"'falalala'"
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'boto_exception'
op|'.'
name|'S3ResponseError'
op|','
nl|'\n'
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_bucket'
op|','
nl|'\n'
name|'bucket_name'
op|')'
newline|'\n'
name|'bucket'
op|'='
name|'self'
op|'.'
name|'conn'
op|'.'
name|'get_bucket'
op|'('
name|'bucket_name'
op|','
name|'validate'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'boto_exception'
op|'.'
name|'S3ResponseError'
op|','
nl|'\n'
name|'bucket'
op|'.'
name|'get_all_keys'
op|','
nl|'\n'
name|'maxkeys'
op|'='
number|'0'
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
string|'"""Tear down test server."""'
newline|'\n'
name|'self'
op|'.'
name|'server'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'S3APITestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit