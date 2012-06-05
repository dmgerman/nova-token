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
string|'"""\nUnit Tests for remote procedure calls using kombu + ssl\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'kombu'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rpc'
name|'import'
name|'impl_kombu'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|kombu
indent|'    '
name|'kombu'
op|'='
name|'None'
newline|'\n'
DECL|variable|impl_kombu
name|'impl_kombu'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Flag settings we will ensure get passed to amqplib'
nl|'\n'
DECL|variable|SSL_VERSION
dedent|''
name|'SSL_VERSION'
op|'='
string|'"SSLv2"'
newline|'\n'
DECL|variable|SSL_CERT
name|'SSL_CERT'
op|'='
string|'"/tmp/cert.blah.blah"'
newline|'\n'
DECL|variable|SSL_CA_CERT
name|'SSL_CA_CERT'
op|'='
string|'"/tmp/cert.ca.blah.blah"'
newline|'\n'
DECL|variable|SSL_KEYFILE
name|'SSL_KEYFILE'
op|'='
string|'"/tmp/keyfile.blah.blah"'
newline|'\n'
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
DECL|class|RpcKombuSslTestCase
name|'class'
name|'RpcKombuSslTestCase'
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
name|'RpcKombuSslTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'if'
name|'kombu'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'kombu_ssl_keyfile'
op|'='
name|'SSL_KEYFILE'
op|','
nl|'\n'
name|'kombu_ssl_ca_certs'
op|'='
name|'SSL_CA_CERT'
op|','
nl|'\n'
name|'kombu_ssl_certfile'
op|'='
name|'SSL_CERT'
op|','
nl|'\n'
name|'kombu_ssl_version'
op|'='
name|'SSL_VERSION'
op|','
nl|'\n'
name|'rabbit_use_ssl'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'kombu'
name|'is'
name|'None'
op|','
string|'"Test requires kombu"'
op|')'
newline|'\n'
DECL|member|test_ssl_on_extended
name|'def'
name|'test_ssl_on_extended'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rpc'
op|'='
name|'impl_kombu'
newline|'\n'
name|'conn'
op|'='
name|'rpc'
op|'.'
name|'create_connection'
op|'('
name|'FLAGS'
op|','
name|'True'
op|')'
newline|'\n'
name|'c'
op|'='
name|'conn'
op|'.'
name|'connection'
newline|'\n'
comment|'#This might be kombu version dependent...'
nl|'\n'
comment|'#Since we are now peaking into the internals of kombu...'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'isinstance'
op|'('
name|'c'
op|'.'
name|'connection'
op|'.'
name|'ssl'
op|','
name|'dict'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'SSL_VERSION'
op|','
name|'c'
op|'.'
name|'connection'
op|'.'
name|'ssl'
op|'.'
name|'get'
op|'('
string|'"ssl_version"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'SSL_CERT'
op|','
name|'c'
op|'.'
name|'connection'
op|'.'
name|'ssl'
op|'.'
name|'get'
op|'('
string|'"certfile"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'SSL_CA_CERT'
op|','
name|'c'
op|'.'
name|'connection'
op|'.'
name|'ssl'
op|'.'
name|'get'
op|'('
string|'"ca_certs"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'SSL_KEYFILE'
op|','
name|'c'
op|'.'
name|'connection'
op|'.'
name|'ssl'
op|'.'
name|'get'
op|'('
string|'"keyfile"'
op|')'
op|')'
newline|'\n'
comment|'#That hash then goes into amqplib which then goes'
nl|'\n'
comment|'#Into python ssl creation...'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
