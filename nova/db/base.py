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
string|'"""Base class for classes that need modular database access."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
newline|'\n'
nl|'\n'
DECL|variable|db_driver_opt
name|'db_driver_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'db_driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.db'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The driver to use for database access'"
op|')'
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
name|'register_opt'
op|'('
name|'db_driver_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Base
name|'class'
name|'Base'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""DB driver is injected in the init method."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'db_driver'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'db_driver'
op|':'
newline|'\n'
indent|'            '
name|'db_driver'
op|'='
name|'CONF'
op|'.'
name|'db_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
name|'db_driver'
op|')'
comment|'# pylint: disable=C0103'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
