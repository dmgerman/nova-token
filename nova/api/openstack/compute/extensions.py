begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'extensions'
name|'as'
name|'base_extensions'
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
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.compute.extensions'"
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
DECL|class|ExtensionManager
name|'class'
name|'ExtensionManager'
op|'('
name|'base_extensions'
op|'.'
name|'ExtensionManager'
op|')'
op|':'
newline|'\n'
DECL|member|__new__
indent|'    '
name|'def'
name|'__new__'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'cls'
op|'.'
name|'_ext_mgr'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'audit'
op|'('
name|'_'
op|'('
string|"'Initializing extension manager.'"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cls'
op|'.'
name|'_ext_mgr'
op|'='
name|'super'
op|'('
name|'ExtensionManager'
op|','
name|'cls'
op|')'
op|'.'
name|'__new__'
op|'('
name|'cls'
op|')'
newline|'\n'
nl|'\n'
name|'cls'
op|'.'
name|'cls_list'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_compute_extension'
newline|'\n'
name|'cls'
op|'.'
name|'_ext_mgr'
op|'.'
name|'extensions'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'cls'
op|'.'
name|'_ext_mgr'
op|'.'
name|'_load_extensions'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'cls'
op|'.'
name|'_ext_mgr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionMiddleware
dedent|''
dedent|''
name|'class'
name|'ExtensionMiddleware'
op|'('
name|'base_extensions'
op|'.'
name|'ExtensionMiddleware'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'application'
op|','
name|'ext_mgr'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'ext_mgr'
op|':'
newline|'\n'
indent|'            '
name|'ext_mgr'
op|'='
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'ExtensionMiddleware'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'application'
op|','
name|'ext_mgr'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
