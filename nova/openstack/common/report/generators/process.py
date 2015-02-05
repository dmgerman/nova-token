begin_unit
comment|'# Copyright 2014 Red Hat, Inc.'
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
string|'"""Provides process-data generators\n\nThis modules defines a class for generating\nprocess data by way of the psutil package.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'psutil'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'report'
op|'.'
name|'models'
name|'import'
name|'process'
name|'as'
name|'pm'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ProcessReportGenerator
name|'class'
name|'ProcessReportGenerator'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Process Data Generator\n\n    This generator returns a\n    :class:`openstack.common.report.models.process.ProcessModel`\n    based on the current process (which will also include\n    all subprocesses, recursively) using the :class:`psutil.Process` class`.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'pm'
op|'.'
name|'ProcessModel'
op|'('
name|'psutil'
op|'.'
name|'Process'
op|'('
name|'os'
op|'.'
name|'getpid'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
