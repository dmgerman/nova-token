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
string|'"""\nRoot WSGI middleware for all API controllers.\n\n**Related Flags**\n\n:osapi_subdomain:  subdomain running the OpenStack API (default: api)\n:ec2api_subdomain:  subdomain running the EC2 API (default: ec2)\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'routes'
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
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'cloudpipe'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'ec2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'metadatarequesthandler'
newline|'\n'
nl|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'osapi_subdomain'"
op|','
string|"'api'"
op|','
nl|'\n'
string|"'subdomain running the OpenStack API'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'ec2api_subdomain'"
op|','
string|"'ec2'"
op|','
nl|'\n'
string|"'subdomain running the EC2 API'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Router'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Routes top-level requests to the appropriate controller."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'default_api'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'osapi_subdomain'
op|'='
op|'{'
string|"'sub_domain'"
op|':'
op|'['
name|'FLAGS'
op|'.'
name|'osapi_subdomain'
op|']'
op|'}'
newline|'\n'
name|'ec2api_subdomain'
op|'='
op|'{'
string|"'sub_domain'"
op|':'
op|'['
name|'FLAGS'
op|'.'
name|'ec2api_subdomain'
op|']'
op|'}'
newline|'\n'
name|'if'
name|'default_api'
op|'=='
string|"'os'"
op|':'
newline|'\n'
indent|'            '
name|'osapi_subdomain'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'elif'
name|'default_api'
op|'=='
string|"'ec2'"
op|':'
newline|'\n'
indent|'            '
name|'ec2api_subdomain'
op|'='
op|'{'
op|'}'
newline|'\n'
dedent|''
name|'mapper'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'sub_domains'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/"'
op|','
name|'controller'
op|'='
name|'self'
op|'.'
name|'osapi_versions'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'osapi_subdomain'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/v1.0/{path_info:.*}"'
op|','
name|'controller'
op|'='
name|'openstack'
op|'.'
name|'API'
op|'('
op|')'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'osapi_subdomain'
op|')'
newline|'\n'
nl|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/"'
op|','
name|'controller'
op|'='
name|'self'
op|'.'
name|'ec2api_versions'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'ec2api_subdomain'
op|')'
newline|'\n'
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/services/{path_info:.*}"'
op|','
name|'controller'
op|'='
name|'ec2'
op|'.'
name|'API'
op|'('
op|')'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'ec2api_subdomain'
op|')'
newline|'\n'
name|'mrh'
op|'='
name|'metadatarequesthandler'
op|'.'
name|'MetadataRequestHandler'
op|'('
op|')'
newline|'\n'
name|'for'
name|'s'
name|'in'
op|'['
string|"'/latest'"
op|','
nl|'\n'
string|"'/2009-04-04'"
op|','
nl|'\n'
string|"'/2008-09-01'"
op|','
nl|'\n'
string|"'/2008-02-01'"
op|','
nl|'\n'
string|"'/2007-12-15'"
op|','
nl|'\n'
string|"'/2007-10-10'"
op|','
nl|'\n'
string|"'/2007-08-29'"
op|','
nl|'\n'
string|"'/2007-03-01'"
op|','
nl|'\n'
string|"'/2007-01-19'"
op|','
nl|'\n'
string|"'/1.0'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'mapper'
op|'.'
name|'connect'
op|'('
string|"'%s/{path_info:.*}'"
op|'%'
name|'s'
op|','
name|'controller'
op|'='
name|'mrh'
op|','
nl|'\n'
name|'conditions'
op|'='
name|'ec2api_subdomain'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mapper'
op|'.'
name|'connect'
op|'('
string|'"/cloudpipe/{path_info:.*}"'
op|','
name|'controller'
op|'='
name|'cloudpipe'
op|'.'
name|'API'
op|'('
op|')'
op|')'
newline|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'mapper'
op|')'
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
DECL|member|osapi_versions
name|'def'
name|'osapi_versions'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Respond to a request for all OpenStack API versions."""'
newline|'\n'
name|'response'
op|'='
op|'{'
nl|'\n'
string|'"versions"'
op|':'
op|'['
nl|'\n'
name|'dict'
op|'('
name|'status'
op|'='
string|'"CURRENT"'
op|','
name|'id'
op|'='
string|'"v1.0"'
op|')'
op|']'
op|'}'
newline|'\n'
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"application/xml"'
op|':'
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
name|'dict'
op|'('
name|'version'
op|'='
op|'['
string|'"status"'
op|','
string|'"id"'
op|']'
op|')'
op|'}'
op|'}'
newline|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Serializer'
op|'('
name|'req'
op|'.'
name|'environ'
op|','
name|'metadata'
op|')'
op|'.'
name|'to_content_type'
op|'('
name|'response'
op|')'
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
DECL|member|ec2api_versions
name|'def'
name|'ec2api_versions'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Respond to a request for all EC2 versions."""'
newline|'\n'
comment|'# available api versions'
nl|'\n'
name|'versions'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
string|"'%s\\n'"
op|'%'
name|'v'
name|'for'
name|'v'
name|'in'
name|'versions'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
