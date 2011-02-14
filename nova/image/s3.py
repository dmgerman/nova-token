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
string|'"""\nProxy AMI-related calls from the cloud controller, to the running\nobjectstore service.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'import'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
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
name|'utils'
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
name|'image'
name|'import'
name|'service'
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
nl|'\n'
DECL|function|map_s3_to_base
name|'def'
name|'map_s3_to_base'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert from S3 format to format defined by BaseImageService."""'
newline|'\n'
name|'i'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'i'
op|'['
string|"'id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'imageId'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'name'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'imageId'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'kernel_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'kernelId'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'ramdisk_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'ramdiskId'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'location'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'imageLocation'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'owner_id'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'imageOwnerId'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'status'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'imageState'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'type'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'is_public'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'isPublic'"
op|')'
newline|'\n'
name|'i'
op|'['
string|"'architecture'"
op|']'
op|'='
name|'image'
op|'.'
name|'get'
op|'('
string|"'architecture'"
op|')'
newline|'\n'
name|'return'
name|'i'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|S3ImageService
dedent|''
name|'class'
name|'S3ImageService'
op|'('
name|'service'
op|'.'
name|'BaseImageService'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|modify
indent|'    '
name|'def'
name|'modify'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'operation'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'POST'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'self'
op|'.'
name|'_qs'
op|'('
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'operation'"
op|':'
name|'operation'
op|'}'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|','
name|'attributes'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""update an image\'s attributes / info.json"""'
newline|'\n'
name|'attributes'
op|'.'
name|'update'
op|'('
op|'{'
string|'"image_id"'
op|':'
name|'image_id'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'POST'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'self'
op|'.'
name|'_qs'
op|'('
name|'attributes'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|register
dedent|''
name|'def'
name|'register'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_location'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" rpc call to register a new image based from a manifest """'
newline|'\n'
name|'image_id'
op|'='
name|'utils'
op|'.'
name|'generate_uid'
op|'('
string|"'ami'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'PUT'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'self'
op|'.'
name|'_qs'
op|'('
op|'{'
string|"'image_location'"
op|':'
name|'image_location'
op|','
nl|'\n'
string|"'image_id'"
op|':'
name|'image_id'
op|'}'
op|')'
op|')'
newline|'\n'
name|'return'
name|'image_id'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of all images that a user can see."""'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'GET'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|')'
newline|'\n'
name|'images'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
op|'['
name|'map_s3_to_base'
op|'('
name|'i'
op|')'
name|'for'
name|'i'
name|'in'
name|'images'
op|']'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""return a image object if the context has permissions"""'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'connection_type'
op|'=='
string|"'fake'"
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'imageId'"
op|':'
string|"'bar'"
op|'}'
newline|'\n'
dedent|''
name|'result'
op|'='
name|'self'
op|'.'
name|'index'
op|'('
name|'context'
op|')'
newline|'\n'
name|'result'
op|'='
op|'['
name|'i'
name|'for'
name|'i'
name|'in'
name|'result'
name|'if'
name|'i'
op|'['
string|"'imageId'"
op|']'
op|'=='
name|'image_id'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
name|'_'
op|'('
string|"'Image %s could not be found'"
op|')'
nl|'\n'
op|'%'
name|'image_id'
op|')'
newline|'\n'
dedent|''
name|'image'
op|'='
name|'result'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'image'
newline|'\n'
nl|'\n'
DECL|member|deregister
dedent|''
name|'def'
name|'deregister'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'""" unregister an image """'
newline|'\n'
name|'self'
op|'.'
name|'_conn'
op|'('
name|'context'
op|')'
op|'.'
name|'make_request'
op|'('
nl|'\n'
name|'method'
op|'='
string|"'DELETE'"
op|','
nl|'\n'
name|'bucket'
op|'='
string|"'_images'"
op|','
nl|'\n'
name|'query_args'
op|'='
name|'self'
op|'.'
name|'_qs'
op|'('
op|'{'
string|"'image_id'"
op|':'
name|'image_id'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_conn
dedent|''
name|'def'
name|'_conn'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'access'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'context'
op|'.'
name|'user'
op|','
nl|'\n'
name|'context'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'secret'
op|'='
name|'str'
op|'('
name|'context'
op|'.'
name|'user'
op|'.'
name|'secret'
op|')'
newline|'\n'
name|'calling'
op|'='
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'OrdinaryCallingFormat'
op|'('
op|')'
newline|'\n'
name|'return'
name|'boto'
op|'.'
name|'s3'
op|'.'
name|'connection'
op|'.'
name|'S3Connection'
op|'('
name|'aws_access_key_id'
op|'='
name|'access'
op|','
nl|'\n'
name|'aws_secret_access_key'
op|'='
name|'secret'
op|','
nl|'\n'
name|'is_secure'
op|'='
name|'False'
op|','
nl|'\n'
name|'calling_format'
op|'='
name|'calling'
op|','
nl|'\n'
name|'port'
op|'='
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'host'
op|'='
name|'FLAGS'
op|'.'
name|'s3_host'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_qs
dedent|''
name|'def'
name|'_qs'
op|'('
name|'self'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pairs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'params'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pairs'
op|'.'
name|'append'
op|'('
name|'key'
op|'+'
string|"'='"
op|'+'
name|'urllib'
op|'.'
name|'quote'
op|'('
name|'params'
op|'['
name|'key'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'&'"
op|'.'
name|'join'
op|'('
name|'pairs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
