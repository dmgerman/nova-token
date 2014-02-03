begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'openstack'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
DECL|variable|ALIAS
name|'ALIAS'
op|'='
string|'"os-scheduler-hints"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerHintsController
name|'class'
name|'SchedulerHintsController'
op|'('
name|'wsgi'
op|'.'
name|'Controller'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_extract_scheduler_hints
name|'def'
name|'_extract_scheduler_hints'
op|'('
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hints'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'attr'
op|'='
string|"'%s:scheduler_hints'"
op|'%'
name|'ALIAS'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'attr'
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'                '
name|'hints'
op|'.'
name|'update'
op|'('
name|'body'
op|'['
name|'attr'
op|']'
op|')'
newline|'\n'
comment|'# Fail if non-dict provided'
nl|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Malformed scheduler_hints attribute"'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'hints'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'extends'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'hints'
op|'='
name|'self'
op|'.'
name|'_extract_scheduler_hints'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'server'"
name|'in'
name|'body'
op|':'
newline|'\n'
indent|'            '
name|'body'
op|'['
string|"'server'"
op|']'
op|'['
string|"'scheduler_hints'"
op|']'
op|'='
name|'hints'
newline|'\n'
dedent|''
name|'yield'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SchedulerHints
dedent|''
dedent|''
name|'class'
name|'SchedulerHints'
op|'('
name|'extensions'
op|'.'
name|'V3APIExtensionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Pass arbitrary key/value pairs to the scheduler."""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"SchedulerHints"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
name|'ALIAS'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get_controller_extensions
name|'def'
name|'get_controller_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'controller'
op|'='
name|'SchedulerHintsController'
op|'('
op|')'
newline|'\n'
name|'ext'
op|'='
name|'extensions'
op|'.'
name|'ControllerExtension'
op|'('
name|'self'
op|','
string|"'servers'"
op|','
name|'controller'
op|')'
newline|'\n'
name|'return'
op|'['
name|'ext'
op|']'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|server_create
dedent|''
name|'def'
name|'server_create'
op|'('
name|'self'
op|','
name|'server_dict'
op|','
name|'create_kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'create_kwargs'
op|'['
string|"'scheduler_hints'"
op|']'
op|'='
name|'server_dict'
op|'.'
name|'get'
op|'('
string|"'scheduler_hints'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
