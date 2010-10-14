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
string|'"""Starting point for routing EC2 requests"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'routes'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
op|'.'
name|'ec2'
name|'import'
name|'apirequest'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'admin'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
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
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"api"'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|API
name|'class'
name|'API'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Routing for all EC2 API requests."""'
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
name|'application'
op|'='
name|'Authenticate'
op|'('
name|'Router'
op|'('
name|'Authorizer'
op|'('
name|'Executor'
op|'('
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Authenticate
dedent|''
dedent|''
name|'class'
name|'Authenticate'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Authenticate an EC2 request and add \'ec2.context\' to WSGI environ."""'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
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
comment|'# Read request signature and access id.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'signature'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'Signature'"
op|']'
newline|'\n'
name|'access'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'AWSAccessKeyId'"
op|']'
newline|'\n'
dedent|''
name|'except'
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
op|')'
newline|'\n'
nl|'\n'
comment|'# Make a copy of args for authentication and signature verification.'
nl|'\n'
dedent|''
name|'auth_params'
op|'='
name|'dict'
op|'('
name|'req'
op|'.'
name|'params'
op|')'
newline|'\n'
name|'auth_params'
op|'.'
name|'pop'
op|'('
string|"'Signature'"
op|')'
comment|'# not part of authentication args'
newline|'\n'
nl|'\n'
comment|'# Authenticate the request.'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
op|'('
name|'user'
op|','
name|'project'
op|')'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'authenticate'
op|'('
nl|'\n'
name|'access'
op|','
nl|'\n'
name|'signature'
op|','
nl|'\n'
name|'auth_params'
op|','
nl|'\n'
name|'req'
op|'.'
name|'method'
op|','
nl|'\n'
name|'req'
op|'.'
name|'host'
op|','
nl|'\n'
name|'req'
op|'.'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'Error'
op|','
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'logging'
op|'.'
name|'debug'
op|'('
string|'"Authentication Failure: %s"'
op|'%'
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Authenticated!'
nl|'\n'
dedent|''
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'user'
op|'='
name|'user'
op|','
nl|'\n'
name|'project'
op|'='
name|'project'
op|','
nl|'\n'
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.context'"
op|']'
op|'='
name|'ctxt'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Router
dedent|''
dedent|''
name|'class'
name|'Router'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Add ec2.\'controller\', .\'action\', and .\'action_args\' to WSGI environ."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Router'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'='
name|'routes'
op|'.'
name|'Mapper'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'map'
op|'.'
name|'connect'
op|'('
string|'"/{controller_name}/"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controllers'
op|'='
name|'dict'
op|'('
name|'Cloud'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
op|','
nl|'\n'
name|'Admin'
op|'='
name|'admin'
op|'.'
name|'AdminController'
op|'('
op|')'
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
comment|'# Obtain the appropriate controller and action for this request.'
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'match'
op|'='
name|'self'
op|'.'
name|'map'
op|'.'
name|'match'
op|'('
name|'req'
op|'.'
name|'path_info'
op|')'
newline|'\n'
name|'controller_name'
op|'='
name|'match'
op|'['
string|"'controller_name'"
op|']'
newline|'\n'
name|'controller'
op|'='
name|'self'
op|'.'
name|'controllers'
op|'['
name|'controller_name'
op|']'
newline|'\n'
dedent|''
name|'except'
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
dedent|''
name|'non_args'
op|'='
op|'['
string|"'Action'"
op|','
string|"'Signature'"
op|','
string|"'AWSAccessKeyId'"
op|','
string|"'SignatureMethod'"
op|','
nl|'\n'
string|"'SignatureVersion'"
op|','
string|"'Version'"
op|','
string|"'Timestamp'"
op|']'
newline|'\n'
name|'args'
op|'='
name|'dict'
op|'('
name|'req'
op|'.'
name|'params'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|'='
name|'req'
op|'.'
name|'params'
op|'['
string|"'Action'"
op|']'
comment|'# raise KeyError if omitted'
newline|'\n'
name|'for'
name|'non_arg'
name|'in'
name|'non_args'
op|':'
newline|'\n'
indent|'                '
name|'args'
op|'.'
name|'pop'
op|'('
name|'non_arg'
op|')'
comment|'# remove, but raise KeyError if omitted'
newline|'\n'
dedent|''
dedent|''
name|'except'
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
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'action: %s'"
op|'%'
name|'action'
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'args'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
string|"'arg: %s\\t\\tval: %s'"
op|'%'
op|'('
name|'key'
op|','
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Success!'
nl|'\n'
dedent|''
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.controller'"
op|']'
op|'='
name|'controller'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action'"
op|']'
op|'='
name|'action'
newline|'\n'
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action_args'"
op|']'
op|'='
name|'args'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Authorizer
dedent|''
dedent|''
name|'class'
name|'Authorizer'
op|'('
name|'wsgi'
op|'.'
name|'Middleware'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Authorize an EC2 API request.\n\n    Return a 401 if ec2.controller and ec2.action in WSGI environ may not be\n    executed in ec2.context.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'Authorizer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'action_roles'
op|'='
op|'{'
nl|'\n'
string|"'CloudController'"
op|':'
op|'{'
nl|'\n'
string|"'DescribeAvailabilityzones'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeRegions'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeSnapshots'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeKeyPairs'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'CreateKeyPair'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DeleteKeyPair'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeSecurityGroups'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'AuthorizeSecurityGroupIngress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'RevokeSecurityGroupIngress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'CreateSecurityGroup'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'DeleteSecurityGroup'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'GetConsoleOutput'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeVolumes'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'CreateVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'AttachVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DetachVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeInstances'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DescribeAddresses'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'AllocateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'ReleaseAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'AssociateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'DisassociateAddress'"
op|':'
op|'['
string|"'netadmin'"
op|']'
op|','
nl|'\n'
string|"'RunInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'TerminateInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'RebootInstances'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'UpdateInstance'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DeleteVolume'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeImages'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'DeregisterImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'RegisterImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'DescribeImageAttribute'"
op|':'
op|'['
string|"'all'"
op|']'
op|','
nl|'\n'
string|"'ModifyImageAttribute'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
string|"'UpdateImage'"
op|':'
op|'['
string|"'projectmanager'"
op|','
string|"'sysadmin'"
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'AdminController'"
op|':'
op|'{'
nl|'\n'
comment|"# All actions have the same permission: ['none'] (the default)"
nl|'\n'
comment|'# superusers will be allowed to run them'
nl|'\n'
comment|'# all others will get HTTPUnauthorized.'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.context'"
op|']'
newline|'\n'
name|'controller_name'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.controller'"
op|']'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
name|'action'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action'"
op|']'
newline|'\n'
name|'allowed_roles'
op|'='
name|'self'
op|'.'
name|'action_roles'
op|'['
name|'controller_name'
op|']'
op|'.'
name|'get'
op|'('
name|'action'
op|','
op|'['
string|"'none'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_matches_any_role'
op|'('
name|'context'
op|','
name|'allowed_roles'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'application'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnauthorized'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_matches_any_role
dedent|''
dedent|''
name|'def'
name|'_matches_any_role'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'roles'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if any role in roles is allowed in context."""'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_superuser'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
string|"'all'"
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
string|"'none'"
name|'in'
name|'roles'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'any'
op|'('
name|'context'
op|'.'
name|'project'
op|'.'
name|'has_role'
op|'('
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|','
name|'role'
op|')'
nl|'\n'
name|'for'
name|'role'
name|'in'
name|'roles'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Executor
dedent|''
dedent|''
name|'class'
name|'Executor'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Execute an EC2 API request.\n\n    Executes \'ec2.action\' upon \'ec2.controller\', passing \'ec2.context\' and\n    \'ec2.action_args\' (all variables in WSGI environ.)  Returns an XML\n    response, or a 400 upon failure.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
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
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.context'"
op|']'
newline|'\n'
name|'controller'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.controller'"
op|']'
newline|'\n'
name|'action'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action'"
op|']'
newline|'\n'
name|'args'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'ec2.action_args'"
op|']'
newline|'\n'
nl|'\n'
name|'api_request'
op|'='
name|'apirequest'
op|'.'
name|'APIRequest'
op|'('
name|'controller'
op|','
name|'action'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'api_request'
op|'.'
name|'send'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ApiError'
name|'as'
name|'ex'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'if'
name|'ex'
op|'.'
name|'code'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'ex'
op|'.'
name|'code'
op|','
name|'ex'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'ex'
op|'.'
name|'message'
op|')'
newline|'\n'
comment|'# TODO(vish): do something more useful with unknown exceptions'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'_error'
op|'('
name|'req'
op|','
name|'type'
op|'('
name|'ex'
op|')'
op|'.'
name|'__name__'
op|','
name|'str'
op|'('
name|'ex'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_error
dedent|''
dedent|''
name|'def'
name|'_error'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'code'
op|','
name|'message'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'resp'
op|'.'
name|'status'
op|'='
number|'400'
newline|'\n'
name|'resp'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
string|"'text/xml'"
newline|'\n'
name|'resp'
op|'.'
name|'body'
op|'='
op|'('
string|'\'<?xml version="1.0"?>\\n\''
nl|'\n'
string|"'<Response><Errors><Error><Code>%s</Code>'"
nl|'\n'
string|"'<Message>%s</Message></Error></Errors>'"
nl|'\n'
string|"'<RequestID>?</RequestID></Response>'"
op|')'
op|'%'
op|'('
name|'code'
op|','
name|'message'
op|')'
newline|'\n'
name|'return'
name|'resp'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
