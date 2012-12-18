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
string|'"""Metadata request handler."""'
newline|'\n'
name|'import'
name|'hashlib'
newline|'\n'
name|'import'
name|'hmac'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'metadata'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
DECL|variable|CACHE_EXPIRATION
name|'CACHE_EXPIRATION'
op|'='
number|'15'
comment|'# in seconds'
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
string|"'memcached_servers'"
op|','
string|"'nova.config'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_forwarded_for'"
op|','
string|"'nova.api.auth'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|metadata_proxy_opts
name|'metadata_proxy_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
nl|'\n'
string|"'service_quantum_metadata_proxy'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set flag to indicate Quantum will proxy metadata requests and '"
nl|'\n'
string|"'resolve instance ids.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
nl|'\n'
string|"'quantum_metadata_proxy_shared_secret'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Shared secret to validate proxies Quantum metadata requests'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'metadata_proxy_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'memcached_servers'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'memcache'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'nova'
op|'.'
name|'common'
name|'import'
name|'memorycache'
name|'as'
name|'memcache'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataRequestHandler
dedent|''
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Serve metadata."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
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
name|'_cache'
op|'='
name|'memcache'
op|'.'
name|'Client'
op|'('
name|'CONF'
op|'.'
name|'memcached_servers'
op|','
name|'debug'
op|'='
number|'0'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_metadata_by_remote_address
dedent|''
name|'def'
name|'get_metadata_by_remote_address'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FixedIpNotFoundForAddress'
op|'('
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cache_key'
op|'='
string|"'metadata-%s'"
op|'%'
name|'address'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'get'
op|'('
name|'cache_key'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'base'
op|'.'
name|'get_metadata_by_address'
op|'('
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'set'
op|'('
name|'cache_key'
op|','
name|'data'
op|','
name|'CACHE_EXPIRATION'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|get_metadata_by_instance_id
dedent|''
name|'def'
name|'get_metadata_by_instance_id'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cache_key'
op|'='
string|"'metadata-%s'"
op|'%'
name|'instance_id'
newline|'\n'
name|'data'
op|'='
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'get'
op|'('
name|'cache_key'
op|')'
newline|'\n'
name|'if'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'base'
op|'.'
name|'get_metadata_by_instance_id'
op|'('
name|'instance_id'
op|','
name|'address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_cache'
op|'.'
name|'set'
op|'('
name|'cache_key'
op|','
name|'data'
op|','
name|'CACHE_EXPIRATION'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
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
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
string|'"/"'
op|'+'
name|'req'
op|'.'
name|'path_info'
op|')'
op|'=='
string|'"/"'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'base'
op|'.'
name|'VERSIONS'
op|'+'
op|'['
string|'"latest"'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'CONF'
op|'.'
name|'service_quantum_metadata_proxy'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'_handle_instance_id_request'
op|'('
name|'req'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"X-Instance-ID present in request headers. The "'
nl|'\n'
string|'"\'service_quantum_metadata_proxy\' option must be enabled"'
nl|'\n'
string|'" to process this header."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'_handle_remote_ip_request'
op|'('
name|'req'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'meta_data'
op|'.'
name|'lookup'
op|'('
name|'req'
op|'.'
name|'path_info'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'base'
op|'.'
name|'InvalidMetadataPath'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'callable'
op|'('
name|'data'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'data'
op|'('
name|'req'
op|','
name|'meta_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'base'
op|'.'
name|'ec2_md_print'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_handle_remote_ip_request
dedent|''
name|'def'
name|'_handle_remote_ip_request'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata_by_remote_address'
op|'('
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'An unknown error has occurred. '"
nl|'\n'
string|"'Please try your request again.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
name|'remote_address'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'meta_data'
newline|'\n'
nl|'\n'
DECL|member|_handle_instance_id_request
dedent|''
name|'def'
name|'_handle_instance_id_request'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance_id'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID'"
op|')'
newline|'\n'
name|'signature'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Instance-ID-Signature'"
op|')'
newline|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
nl|'\n'
comment|'# Ensure that only one header was passed'
nl|'\n'
nl|'\n'
name|'if'
name|'instance_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'X-Instance-ID header is missing from request.'"
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'not'
name|'isinstance'
op|'('
name|'instance_id'
op|','
name|'basestring'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'Multiple X-Instance-ID headers found within request.'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'msg'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'expected_signature'
op|'='
name|'hmac'
op|'.'
name|'new'
op|'('
nl|'\n'
name|'CONF'
op|'.'
name|'quantum_metadata_proxy_shared_secret'
op|','
nl|'\n'
name|'instance_id'
op|','
nl|'\n'
name|'hashlib'
op|'.'
name|'sha256'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'expected_signature'
op|'!='
name|'signature'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance_id'
op|':'
newline|'\n'
indent|'                '
name|'w'
op|'='
name|'_'
op|'('
string|"'X-Instance-ID-Signature: %(signature)s does not match '"
nl|'\n'
string|"'the expected value: %(expected_signature)s for id: '"
nl|'\n'
string|"'%(instance_id)s.  Request From: %(remote_address)s'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'w'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'msg'
op|'='
name|'_'
op|'('
string|"'Invalid proxy request signature.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata_by_instance_id'
op|'('
name|'instance_id'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for instance id: %s'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'An unknown error has occurred. '"
nl|'\n'
string|"'Please try your request again.'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for instance id: %s'"
op|')'
op|','
nl|'\n'
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'meta_data'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
