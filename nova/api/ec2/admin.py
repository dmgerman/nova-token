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
string|'"""\nAdmin API controller, exposed through http via the api worker.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'IPy'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
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
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
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
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.ec2.admin'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|user_dict
name|'def'
name|'user_dict'
op|'('
name|'user'
op|','
name|'base64_file'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert the user object to a result dict"""'
newline|'\n'
name|'if'
name|'user'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'username'"
op|':'
name|'user'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'accesskey'"
op|':'
name|'user'
op|'.'
name|'access'
op|','
nl|'\n'
string|"'secretkey'"
op|':'
name|'user'
op|'.'
name|'secret'
op|','
nl|'\n'
string|"'file'"
op|':'
name|'base64_file'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|project_dict
dedent|''
dedent|''
name|'def'
name|'project_dict'
op|'('
name|'project'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert the project object to a result dict"""'
newline|'\n'
name|'if'
name|'project'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
nl|'\n'
string|"'projectname'"
op|':'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'project_manager_id'"
op|':'
name|'project'
op|'.'
name|'project_manager_id'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'project'
op|'.'
name|'description'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|host_dict
dedent|''
dedent|''
name|'def'
name|'host_dict'
op|'('
name|'host'
op|','
name|'compute_service'
op|','
name|'instances'
op|','
name|'volume_service'
op|','
name|'volumes'
op|','
name|'now'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a host model object to a result dict"""'
newline|'\n'
name|'rv'
op|'='
op|'{'
string|"'hostname'"
op|':'
name|'host'
op|','
string|"'instance_count'"
op|':'
name|'len'
op|'('
name|'instances'
op|')'
op|','
nl|'\n'
string|"'volume_count'"
op|':'
name|'len'
op|'('
name|'volumes'
op|')'
op|'}'
newline|'\n'
name|'if'
name|'compute_service'
op|':'
newline|'\n'
indent|'        '
name|'latest'
op|'='
name|'compute_service'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'compute_service'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
name|'delta'
op|'='
name|'now'
op|'-'
name|'latest'
newline|'\n'
name|'if'
name|'delta'
op|'.'
name|'seconds'
op|'<='
name|'FLAGS'
op|'.'
name|'service_down_time'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'compute'"
op|']'
op|'='
string|"'up'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'compute'"
op|']'
op|'='
string|"'down'"
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'volume_service'
op|':'
newline|'\n'
indent|'        '
name|'latest'
op|'='
name|'volume_service'
op|'['
string|"'updated_at'"
op|']'
name|'or'
name|'volume_service'
op|'['
string|"'created_at'"
op|']'
newline|'\n'
name|'delta'
op|'='
name|'now'
op|'-'
name|'latest'
newline|'\n'
name|'if'
name|'delta'
op|'.'
name|'seconds'
op|'<='
name|'FLAGS'
op|'.'
name|'service_down_time'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'volume'"
op|']'
op|'='
string|"'up'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'volume'"
op|']'
op|'='
string|"'down'"
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_dict
dedent|''
name|'def'
name|'instance_dict'
op|'('
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'name'"
op|':'
name|'inst'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'memory_mb'"
op|':'
name|'inst'
op|'['
string|"'memory_mb'"
op|']'
op|','
nl|'\n'
string|"'vcpus'"
op|':'
name|'inst'
op|'['
string|"'vcpus'"
op|']'
op|','
nl|'\n'
string|"'disk_gb'"
op|':'
name|'inst'
op|'['
string|"'local_gb'"
op|']'
op|','
nl|'\n'
string|"'flavor_id'"
op|':'
name|'inst'
op|'['
string|"'flavorid'"
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|vpn_dict
dedent|''
name|'def'
name|'vpn_dict'
op|'('
name|'project'
op|','
name|'vpn_instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'rv'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'project'
op|'.'
name|'id'
op|','
nl|'\n'
string|"'public_ip'"
op|':'
name|'project'
op|'.'
name|'vpn_ip'
op|','
nl|'\n'
string|"'public_port'"
op|':'
name|'project'
op|'.'
name|'vpn_port'
op|'}'
newline|'\n'
name|'if'
name|'vpn_instance'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'['
string|"'instance_id'"
op|']'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'vpn_instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'rv'
op|'['
string|"'created_at'"
op|']'
op|'='
name|'utils'
op|'.'
name|'isotime'
op|'('
name|'vpn_instance'
op|'['
string|"'created_at'"
op|']'
op|')'
newline|'\n'
name|'address'
op|'='
name|'vpn_instance'
op|'.'
name|'get'
op|'('
string|"'fixed_ip'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'address'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'internal_ip'"
op|']'
op|'='
name|'address'
op|'['
string|"'address'"
op|']'
newline|'\n'
dedent|''
name|'if'
name|'project'
op|'.'
name|'vpn_ip'
name|'and'
name|'project'
op|'.'
name|'vpn_port'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'utils'
op|'.'
name|'vpn_ping'
op|'('
name|'project'
op|'.'
name|'vpn_ip'
op|','
name|'project'
op|'.'
name|'vpn_port'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'running'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'down'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'down - invalid project vpn config'"
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'rv'
op|'['
string|"'state'"
op|']'
op|'='
string|"'pending'"
newline|'\n'
dedent|''
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AdminController
dedent|''
name|'class'
name|'AdminController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    API Controller for users, hosts, nodes, and workers.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__str__
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'AdminController'"
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
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
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|describe_instance_types
dedent|''
name|'def'
name|'describe_instance_types'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all active instance types data (vcpus, memory, etc.)"""'
newline|'\n'
name|'return'
op|'{'
string|"'instanceTypeSet'"
op|':'
op|'['
name|'instance_dict'
op|'('
name|'v'
op|')'
name|'for'
name|'v'
name|'in'
nl|'\n'
name|'db'
op|'.'
name|'instance_type_get_all'
op|'('
name|'context'
op|')'
op|'.'
name|'values'
op|'('
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|describe_user
dedent|''
name|'def'
name|'describe_user'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'name'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns user data, including access and secret keys."""'
newline|'\n'
name|'return'
name|'user_dict'
op|'('
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|describe_users
dedent|''
name|'def'
name|'describe_users'
op|'('
name|'self'
op|','
name|'_context'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all users - should be changed to deal with a list."""'
newline|'\n'
name|'return'
op|'{'
string|"'userSet'"
op|':'
nl|'\n'
op|'['
name|'user_dict'
op|'('
name|'u'
op|')'
name|'for'
name|'u'
name|'in'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_users'
op|'('
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|register_user
dedent|''
name|'def'
name|'register_user'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new user, and returns generated credentials."""'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Creating new user: %s"'
op|')'
op|','
name|'name'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'user_dict'
op|'('
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'create_user'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deregister_user
dedent|''
name|'def'
name|'deregister_user'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Deletes a single user (NOT undoable.)\n           Should throw an exception if the user has instances,\n           volumes, or buckets remaining.\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Deleting user: %s"'
op|')'
op|','
name|'name'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_user'
op|'('
name|'name'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|describe_roles
dedent|''
name|'def'
name|'describe_roles'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_roles'
op|'='
name|'True'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of allowed roles."""'
newline|'\n'
name|'roles'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_roles'
op|'('
name|'project_roles'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'roles'"
op|':'
op|'['
op|'{'
string|"'role'"
op|':'
name|'r'
op|'}'
name|'for'
name|'r'
name|'in'
name|'roles'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|describe_user_roles
dedent|''
name|'def'
name|'describe_user_roles'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user'
op|','
name|'project'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns a list of roles for the given user.\n           Omitting project will return any global roles that the user has.\n           Specifying project will return only project specific roles.\n        """'
newline|'\n'
name|'roles'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user_roles'
op|'('
name|'user'
op|','
name|'project'
op|'='
name|'project'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'roles'"
op|':'
op|'['
op|'{'
string|"'role'"
op|':'
name|'r'
op|'}'
name|'for'
name|'r'
name|'in'
name|'roles'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|modify_user_role
dedent|''
name|'def'
name|'modify_user_role'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user'
op|','
name|'role'
op|','
name|'project'
op|'='
name|'None'
op|','
nl|'\n'
name|'operation'
op|'='
string|"'add'"
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or remove a role for a user and project."""'
newline|'\n'
name|'if'
name|'operation'
op|'=='
string|"'add'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'project'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Adding role %(role)s to user %(user)s"'
nl|'\n'
string|'" for project %(project)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Adding sitewide role %(role)s to"'
nl|'\n'
string|'" user %(user)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
dedent|''
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'add_role'
op|'('
name|'user'
op|','
name|'role'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'operation'
op|'=='
string|"'remove'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'project'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Removing role %(role)s from user %(user)s"'
nl|'\n'
string|'" for project %(project)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Removing sitewide role %(role)s"'
nl|'\n'
string|'" from user %(user)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
dedent|''
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'remove_role'
op|'('
name|'user'
op|','
name|'role'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|"'operation must be add or remove'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|generate_x509_for_user
dedent|''
name|'def'
name|'generate_x509_for_user'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'project'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Generates and returns an x509 certificate for a single user.\n           Is usually called from a client that will wrap this with\n           access and secret key info, and return a zip file.\n        """'
newline|'\n'
name|'if'
name|'project'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'project'
op|'='
name|'name'
newline|'\n'
dedent|''
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'project'
op|')'
newline|'\n'
name|'user'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_user'
op|'('
name|'name'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Getting x509 for user: %(name)s"'
nl|'\n'
string|'" on project: %(project)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'user_dict'
op|'('
name|'user'
op|','
name|'base64'
op|'.'
name|'b64encode'
op|'('
name|'project'
op|'.'
name|'get_credentials'
op|'('
name|'user'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|describe_project
dedent|''
name|'def'
name|'describe_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns project data, including member ids."""'
newline|'\n'
name|'return'
name|'project_dict'
op|'('
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|describe_projects
dedent|''
name|'def'
name|'describe_projects'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns all projects - should be changed to deal with a list."""'
newline|'\n'
name|'return'
op|'{'
string|"'projectSet'"
op|':'
nl|'\n'
op|'['
name|'project_dict'
op|'('
name|'u'
op|')'
name|'for'
name|'u'
name|'in'
nl|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_projects'
op|'('
name|'user'
op|'='
name|'user'
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|register_project
dedent|''
name|'def'
name|'register_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'manager_user'
op|','
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
name|'member_users'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a new project"""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Create project %(name)s managed by"'
nl|'\n'
string|'" %(manager_user)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'return'
name|'project_dict'
op|'('
nl|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'create_project'
op|'('
nl|'\n'
name|'name'
op|','
nl|'\n'
name|'manager_user'
op|','
nl|'\n'
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
name|'member_users'
op|'='
name|'None'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_project
dedent|''
name|'def'
name|'modify_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
name|'manager_user'
op|','
name|'description'
op|'='
name|'None'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Modifies a project"""'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"Modify project: %(name)s managed by"'
nl|'\n'
string|'" %(manager_user)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'modify_project'
op|'('
name|'name'
op|','
nl|'\n'
name|'manager_user'
op|'='
name|'manager_user'
op|','
nl|'\n'
name|'description'
op|'='
name|'description'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|deregister_project
dedent|''
name|'def'
name|'deregister_project'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Permanently deletes a project."""'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|'"Delete project: %s"'
op|')'
op|','
name|'name'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'delete_project'
op|'('
name|'name'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|describe_project_members
dedent|''
name|'def'
name|'describe_project_members'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'name'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'project'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_project'
op|'('
name|'name'
op|')'
newline|'\n'
name|'result'
op|'='
op|'{'
nl|'\n'
string|"'members'"
op|':'
op|'['
op|'{'
string|"'member'"
op|':'
name|'m'
op|'}'
name|'for'
name|'m'
name|'in'
name|'project'
op|'.'
name|'member_ids'
op|']'
op|'}'
newline|'\n'
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|modify_project_member
dedent|''
name|'def'
name|'modify_project_member'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'user'
op|','
name|'project'
op|','
name|'operation'
op|','
nl|'\n'
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or remove a user from a project."""'
newline|'\n'
name|'if'
name|'operation'
op|'=='
string|"'add'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Adding user %(user)s to project %(project)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'add_to_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'operation'
op|'=='
string|"'remove'"
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Removing user %(user)s from"'
nl|'\n'
string|'" project %(project)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'msg'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'remove_from_project'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|"'operation must be add or remove'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_vpn_for
dedent|''
name|'def'
name|'_vpn_for'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the VPN instance for a project ID."""'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'db'
op|'.'
name|'instance_get_all_by_project'
op|'('
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'instance'
op|'['
string|"'image_id'"
op|']'
op|'=='
name|'str'
op|'('
name|'FLAGS'
op|'.'
name|'vpn_image_id'
op|')'
nl|'\n'
name|'and'
name|'not'
name|'instance'
op|'['
string|"'state_description'"
op|']'
name|'in'
nl|'\n'
op|'['
string|"'shutting_down'"
op|','
string|"'shutdown'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|member|start_vpn
dedent|''
dedent|''
dedent|''
name|'def'
name|'start_vpn'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_vpn_for'
op|'('
name|'context'
op|','
name|'project'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'instance'
op|':'
newline|'\n'
comment|'# NOTE(vish) import delayed because of __init__.py'
nl|'\n'
indent|'            '
name|'from'
name|'nova'
op|'.'
name|'cloudpipe'
name|'import'
name|'pipelib'
newline|'\n'
name|'pipe'
op|'='
name|'pipelib'
op|'.'
name|'CloudPipe'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'pipe'
op|'.'
name|'launch_vpn_instance'
op|'('
name|'project'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'db'
op|'.'
name|'NoMoreNetworks'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
string|'"Unable to claim IP for VPN instance"'
nl|'\n'
string|'", ensure it isn\'t running, and try "'
nl|'\n'
string|'"again in a few minutes"'
op|')'
newline|'\n'
dedent|''
name|'instance'
op|'='
name|'self'
op|'.'
name|'_vpn_for'
op|'('
name|'context'
op|','
name|'project'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'instance_id'"
op|':'
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|describe_vpns
dedent|''
name|'def'
name|'describe_vpns'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vpns'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'project'
name|'in'
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_projects'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_vpn_for'
op|'('
name|'context'
op|','
name|'project'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'vpns'
op|'.'
name|'append'
op|'('
name|'vpn_dict'
op|'('
name|'project'
op|','
name|'instance'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'items'"
op|':'
name|'vpns'
op|'}'
newline|'\n'
nl|'\n'
comment|"# FIXME(vish): these host commands don't work yet, perhaps some of the"
nl|'\n'
comment|'#              required data can be retrieved from service objects?'
nl|'\n'
nl|'\n'
DECL|member|describe_hosts
dedent|''
name|'def'
name|'describe_hosts'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns status info for all nodes. Includes:\n            * Hostname\n            * Compute (up, down, None)\n            * Instance count\n            * Volume (up, down, None)\n            * Volume Count\n        """'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all'
op|'('
name|'context'
op|','
name|'False'
op|')'
newline|'\n'
name|'now'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'rv'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'host'
name|'in'
op|'['
name|'service'
op|'['
string|"'host'"
op|']'
name|'for'
name|'service'
name|'in'
name|'services'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'host'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'                '
name|'hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'host'
name|'in'
name|'hosts'
op|':'
newline|'\n'
indent|'            '
name|'compute'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'services'
name|'if'
name|'s'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
name|'and'
name|'s'
op|'['
string|"'binary'"
op|']'
op|'=='
string|"'nova-compute'"
op|']'
newline|'\n'
name|'if'
name|'compute'
op|':'
newline|'\n'
indent|'                '
name|'compute'
op|'='
name|'compute'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'instances'
op|'='
name|'db'
op|'.'
name|'instance_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'volume'
op|'='
op|'['
name|'s'
name|'for'
name|'s'
name|'in'
name|'services'
name|'if'
name|'s'
op|'['
string|"'host'"
op|']'
op|'=='
name|'host'
name|'and'
name|'s'
op|'['
string|"'binary'"
op|']'
op|'=='
string|"'nova-volume'"
op|']'
newline|'\n'
name|'if'
name|'volume'
op|':'
newline|'\n'
indent|'                '
name|'volume'
op|'='
name|'volume'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'volumes'
op|'='
name|'db'
op|'.'
name|'volume_get_all_by_host'
op|'('
name|'context'
op|','
name|'host'
op|')'
newline|'\n'
name|'rv'
op|'.'
name|'append'
op|'('
name|'host_dict'
op|'('
name|'host'
op|','
name|'compute'
op|','
name|'instances'
op|','
name|'volume'
op|','
name|'volumes'
op|','
nl|'\n'
name|'now'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
op|'{'
string|"'hosts'"
op|':'
name|'rv'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|describe_host
dedent|''
name|'def'
name|'describe_host'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'name'
op|','
op|'**'
name|'_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns status info for single node."""'
newline|'\n'
name|'return'
name|'host_dict'
op|'('
name|'db'
op|'.'
name|'host_get'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_provider_fw_rule_exists
dedent|''
name|'def'
name|'_provider_fw_rule_exists'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'rule'
op|')'
op|':'
newline|'\n'
comment|'# TODO(todd): we call this repeatedly, can we filter by protocol?'
nl|'\n'
indent|'        '
name|'for'
name|'old_rule'
name|'in'
name|'db'
op|'.'
name|'provider_fw_rule_get_all'
op|'('
name|'context'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'all'
op|'('
op|'['
name|'rule'
op|'['
name|'k'
op|']'
op|'=='
name|'old_rule'
op|'['
name|'k'
op|']'
name|'for'
name|'k'
name|'in'
op|'('
string|"'cidr'"
op|','
string|"'from_port'"
op|','
nl|'\n'
string|"'to_port'"
op|','
string|"'protocol'"
op|')'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|block_external_addresses
dedent|''
name|'def'
name|'block_external_addresses'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add provider-level firewall rules to block incoming traffic."""'
newline|'\n'
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Blocking traffic to all projects incoming from %s'"
op|')'
op|','
nl|'\n'
name|'cidr'
op|','
name|'context'
op|'='
name|'context'
op|')'
newline|'\n'
name|'cidr'
op|'='
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'cidr'
op|')'
op|'.'
name|'decode'
op|'('
op|')'
newline|'\n'
comment|'# raise if invalid'
nl|'\n'
name|'IPy'
op|'.'
name|'IP'
op|'('
name|'cidr'
op|')'
newline|'\n'
name|'rule'
op|'='
op|'{'
string|"'cidr'"
op|':'
name|'cidr'
op|'}'
newline|'\n'
name|'tcp_rule'
op|'='
name|'rule'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'tcp_rule'
op|'.'
name|'update'
op|'('
op|'{'
string|"'protocol'"
op|':'
string|"'tcp'"
op|','
string|"'from_port'"
op|':'
number|'1'
op|','
string|"'to_port'"
op|':'
number|'65535'
op|'}'
op|')'
newline|'\n'
name|'udp_rule'
op|'='
name|'rule'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'udp_rule'
op|'.'
name|'update'
op|'('
op|'{'
string|"'protocol'"
op|':'
string|"'udp'"
op|','
string|"'from_port'"
op|':'
number|'1'
op|','
string|"'to_port'"
op|':'
number|'65535'
op|'}'
op|')'
newline|'\n'
name|'icmp_rule'
op|'='
name|'rule'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'icmp_rule'
op|'.'
name|'update'
op|'('
op|'{'
string|"'protocol'"
op|':'
string|"'icmp'"
op|','
string|"'from_port'"
op|':'
op|'-'
number|'1'
op|','
nl|'\n'
string|"'to_port'"
op|':'
name|'None'
op|'}'
op|')'
newline|'\n'
name|'rules_added'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_provider_fw_rule_exists'
op|'('
name|'context'
op|','
name|'tcp_rule'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'provider_fw_rule_create'
op|'('
name|'context'
op|','
name|'tcp_rule'
op|')'
newline|'\n'
name|'rules_added'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_provider_fw_rule_exists'
op|'('
name|'context'
op|','
name|'udp_rule'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'provider_fw_rule_create'
op|'('
name|'context'
op|','
name|'udp_rule'
op|')'
newline|'\n'
name|'rules_added'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'_provider_fw_rule_exists'
op|'('
name|'context'
op|','
name|'icmp_rule'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'db'
op|'.'
name|'provider_fw_rule_create'
op|'('
name|'context'
op|','
name|'icmp_rule'
op|')'
newline|'\n'
name|'rules_added'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'rules_added'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ApiError'
op|'('
name|'_'
op|'('
string|"'Duplicate rule'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'trigger_provider_fw_rules_refresh'
op|'('
name|'context'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'status'"
op|':'
string|"'OK'"
op|','
string|"'message'"
op|':'
string|"'Added %s rules'"
op|'%'
name|'rules_added'
op|'}'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
