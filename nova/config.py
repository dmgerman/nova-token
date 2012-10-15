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
comment|'# Copyright 2012 Red Hat, Inc.'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_args
name|'def'
name|'parse_args'
op|'('
name|'argv'
op|','
name|'default_config_files'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'CONF'
op|'.'
name|'disable_interspersed_args'
op|'('
op|')'
newline|'\n'
name|'return'
name|'argv'
op|'['
op|':'
number|'1'
op|']'
op|'+'
name|'CONF'
op|'('
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|','
nl|'\n'
name|'project'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'default_config_files'
op|'='
name|'default_config_files'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
