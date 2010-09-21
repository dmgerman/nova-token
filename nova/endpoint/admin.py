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
nl|'\n'
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
op|'.'
name|'auth'
name|'import'
name|'manager'
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
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a host model object to a result dict"""'
newline|'\n'
name|'if'
name|'host'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'host'
op|'.'
name|'state'
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
DECL|function|admin_only
dedent|''
dedent|''
name|'def'
name|'admin_only'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator for admin-only API calls"""'
newline|'\n'
DECL|function|wrapper
name|'def'
name|'wrapper'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Internal wrapper method for admin-only API calls"""'
newline|'\n'
name|'context'
op|'='
name|'args'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_admin'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'target'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'wrapper'
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
string|'"""\n    API Controller for users, hosts, nodes, and workers.\n    Trivial admin_only wrapper will be replaced with RBAC,\n    allowing project managers to administer project users.\n    """'
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_user
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_users
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|register_user
name|'def'
name|'register_user'
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
string|'"""Creates a new user, and returns generated credentials."""'
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|deregister_user
name|'def'
name|'deregister_user'
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
string|'"""Deletes a single user (NOT undoable.)\n           Should throw an exception if the user has instances,\n           volumes, or buckets remaining.\n        """'
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
nl|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_roles
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_user_roles
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|modify_user_role
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
string|"'operation must be add or remove'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|generate_x509_for_user
name|'def'
name|'generate_x509_for_user'
op|'('
name|'self'
op|','
name|'_context'
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_project
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_projects
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|register_project
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|deregister_project
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_project_members
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
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|modify_project_member
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
string|"'operation must be add or remove'"
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
comment|"# FIXME(vish): these host commands don't work yet, perhaps some of the"
nl|'\n'
comment|'#              required data can be retrieved from service objects?'
nl|'\n'
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_hosts
name|'def'
name|'describe_hosts'
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
string|'"""Returns status info for all nodes. Includes:\n            * Disk Space\n            * Instance List\n            * RAM used\n            * CPU used\n            * DHCP servers running\n            * Iptables / bridges\n        """'
newline|'\n'
name|'return'
op|'{'
string|"'hostSet'"
op|':'
op|'['
name|'host_dict'
op|'('
name|'h'
op|')'
name|'for'
name|'h'
name|'in'
name|'db'
op|'.'
name|'host_get_all'
op|'('
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'admin_only'
newline|'\n'
DECL|member|describe_host
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
dedent|''
dedent|''
endmarker|''
end_unit
