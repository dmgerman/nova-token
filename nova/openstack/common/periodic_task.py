begin_unit
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
name|'copy'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'_i18n'
name|'import'
name|'_'
op|','
name|'_LE'
op|','
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|periodic_opts
name|'periodic_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'run_external_periodic_tasks'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Some periodic tasks can be run in a separate process. '"
nl|'\n'
string|"'Should we run them here?'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'periodic_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_INTERVAL
name|'DEFAULT_INTERVAL'
op|'='
number|'60.0'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Entry point for oslo.config-generator."""'
newline|'\n'
name|'return'
op|'['
op|'('
name|'None'
op|','
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'periodic_opts'
op|')'
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InvalidPeriodicTaskArg
dedent|''
name|'class'
name|'InvalidPeriodicTaskArg'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|variable|message
indent|'    '
name|'message'
op|'='
name|'_'
op|'('
string|'"Unexpected argument for periodic task creation: %(arg)s."'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|periodic_task
dedent|''
name|'def'
name|'periodic_task'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Decorator to indicate that a method is a periodic task.\n\n    This decorator can be used in two ways:\n\n        1. Without arguments \'@periodic_task\', this will be run on the default\n           interval of 60 seconds.\n\n        2. With arguments:\n           @periodic_task(spacing=N [, run_immediately=[True|False]])\n           this will be run on approximately every N seconds. If this number is\n           negative the periodic task will be disabled. If the run_immediately\n           argument is provided and has a value of \'True\', the first run of the\n           task will be shortly after task scheduler starts.  If\n           run_immediately is omitted or set to \'False\', the first time the\n           task runs will be approximately N seconds after the task scheduler\n           starts.\n    """'
newline|'\n'
DECL|function|decorator
name|'def'
name|'decorator'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
comment|'# Test for old style invocation'
nl|'\n'
indent|'        '
name|'if'
string|"'ticks_between_runs'"
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidPeriodicTaskArg'
op|'('
name|'arg'
op|'='
string|"'ticks_between_runs'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Control if run at all'
nl|'\n'
dedent|''
name|'f'
op|'.'
name|'_periodic_task'
op|'='
name|'True'
newline|'\n'
name|'f'
op|'.'
name|'_periodic_external_ok'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'external_process_ok'"
op|','
name|'False'
op|')'
newline|'\n'
name|'if'
name|'f'
op|'.'
name|'_periodic_external_ok'
name|'and'
name|'not'
name|'CONF'
op|'.'
name|'run_external_periodic_tasks'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'_periodic_enabled'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'_periodic_enabled'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'enabled'"
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Control frequency'
nl|'\n'
dedent|''
name|'f'
op|'.'
name|'_periodic_spacing'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'spacing'"
op|','
number|'0'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'_periodic_immediate'
op|'='
name|'kwargs'
op|'.'
name|'pop'
op|'('
string|"'run_immediately'"
op|','
name|'False'
op|')'
newline|'\n'
name|'if'
name|'f'
op|'.'
name|'_periodic_immediate'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'_periodic_last_run'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'_periodic_last_run'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'f'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): The `if` is necessary to allow the decorator to be used with'
nl|'\n'
comment|'# and without parenthesis.'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# In the 'with-parenthesis' case (with kwargs present), this function needs"
nl|'\n'
comment|'# to return a decorator function since the interpreter will invoke it like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   periodic_task(*args, **kwargs)(f)'
nl|'\n'
comment|'#'
nl|'\n'
comment|"# In the 'without-parenthesis' case, the original function will be passed"
nl|'\n'
comment|'# in as the first argument, like:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   periodic_task(f)'
nl|'\n'
dedent|''
name|'if'
name|'kwargs'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'decorator'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'decorator'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_PeriodicTasksMeta
dedent|''
dedent|''
name|'class'
name|'_PeriodicTasksMeta'
op|'('
name|'type'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'cls'
op|','
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Metaclass that allows us to collect decorated periodic tasks."""'
newline|'\n'
name|'super'
op|'('
name|'_PeriodicTasksMeta'
op|','
name|'cls'
op|')'
op|'.'
name|'__init__'
op|'('
name|'names'
op|','
name|'bases'
op|','
name|'dict_'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(sirp): if the attribute is not present then we must be the base'
nl|'\n'
comment|'# class, so, go ahead an initialize it. If the attribute is present,'
nl|'\n'
comment|"# then we're a subclass so make a copy of it so we don't step on our"
nl|'\n'
comment|"# parent's toes."
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'='
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'['
op|':'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_spacing'
op|'='
name|'cls'
op|'.'
name|'_periodic_spacing'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'.'
name|'_periodic_spacing'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'value'
name|'in'
name|'cls'
op|'.'
name|'__dict__'
op|'.'
name|'values'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'getattr'
op|'('
name|'value'
op|','
string|"'_periodic_task'"
op|','
name|'False'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'='
name|'value'
newline|'\n'
name|'name'
op|'='
name|'task'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
name|'if'
name|'task'
op|'.'
name|'_periodic_spacing'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Skipping periodic task %(task)s because '"
nl|'\n'
string|"'its interval is negative'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'task'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'task'
op|'.'
name|'_periodic_enabled'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Skipping periodic task %(task)s because '"
nl|'\n'
string|"'it is disabled'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'task'"
op|':'
name|'name'
op|'}'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
comment|'# A periodic spacing of zero indicates that this task should'
nl|'\n'
comment|'# be run on the default interval to avoid running too'
nl|'\n'
comment|'# frequently.'
nl|'\n'
dedent|''
name|'if'
name|'task'
op|'.'
name|'_periodic_spacing'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'task'
op|'.'
name|'_periodic_spacing'
op|'='
name|'DEFAULT_INTERVAL'
newline|'\n'
nl|'\n'
dedent|''
name|'cls'
op|'.'
name|'_periodic_tasks'
op|'.'
name|'append'
op|'('
op|'('
name|'name'
op|','
name|'task'
op|')'
op|')'
newline|'\n'
name|'cls'
op|'.'
name|'_periodic_spacing'
op|'['
name|'name'
op|']'
op|'='
name|'task'
op|'.'
name|'_periodic_spacing'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_nearest_boundary
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_nearest_boundary'
op|'('
name|'last_run'
op|','
name|'spacing'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find nearest boundary which is in the past, which is a multiple of the\n    spacing with the last run as an offset.\n\n    Eg if last run was 10 and spacing was 7, the new last run could be: 17, 24,\n    31, 38...\n\n    0% to 5% of the spacing value will be added to this value to ensure tasks\n    do not synchronize. This jitter is rounded to the nearest second, this\n    means that spacings smaller than 20 seconds will not have jitter.\n    """'
newline|'\n'
name|'current_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'if'
name|'last_run'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'current_time'
newline|'\n'
dedent|''
name|'delta'
op|'='
name|'current_time'
op|'-'
name|'last_run'
newline|'\n'
name|'offset'
op|'='
name|'delta'
op|'%'
name|'spacing'
newline|'\n'
comment|'# Add up to 5% jitter'
nl|'\n'
name|'jitter'
op|'='
name|'int'
op|'('
name|'spacing'
op|'*'
op|'('
name|'random'
op|'.'
name|'random'
op|'('
op|')'
op|'/'
number|'20'
op|')'
op|')'
newline|'\n'
name|'return'
name|'current_time'
op|'-'
name|'offset'
op|'+'
name|'jitter'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'six'
op|'.'
name|'add_metaclass'
op|'('
name|'_PeriodicTasksMeta'
op|')'
newline|'\n'
DECL|class|PeriodicTasks
name|'class'
name|'PeriodicTasks'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'PeriodicTasks'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_periodic_last_run'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'name'
op|','
name|'task'
name|'in'
name|'self'
op|'.'
name|'_periodic_tasks'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_periodic_last_run'
op|'['
name|'name'
op|']'
op|'='
name|'task'
op|'.'
name|'_periodic_last_run'
newline|'\n'
nl|'\n'
DECL|member|run_periodic_tasks
dedent|''
dedent|''
name|'def'
name|'run_periodic_tasks'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'raise_on_error'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tasks to be run at a periodic interval."""'
newline|'\n'
name|'idle_for'
op|'='
name|'DEFAULT_INTERVAL'
newline|'\n'
name|'for'
name|'task_name'
op|','
name|'task'
name|'in'
name|'self'
op|'.'
name|'_periodic_tasks'
op|':'
newline|'\n'
indent|'            '
name|'full_task_name'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
name|'self'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
op|','
name|'task_name'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'spacing'
op|'='
name|'self'
op|'.'
name|'_periodic_spacing'
op|'['
name|'task_name'
op|']'
newline|'\n'
name|'last_run'
op|'='
name|'self'
op|'.'
name|'_periodic_last_run'
op|'['
name|'task_name'
op|']'
newline|'\n'
nl|'\n'
comment|'# Check if due, if not skip'
nl|'\n'
name|'idle_for'
op|'='
name|'min'
op|'('
name|'idle_for'
op|','
name|'spacing'
op|')'
newline|'\n'
name|'if'
name|'last_run'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'delta'
op|'='
name|'last_run'
op|'+'
name|'spacing'
op|'-'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'if'
name|'delta'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                    '
name|'idle_for'
op|'='
name|'min'
op|'('
name|'idle_for'
op|','
name|'delta'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Running periodic task %(full_task_name)s"'
op|','
nl|'\n'
op|'{'
string|'"full_task_name"'
op|':'
name|'full_task_name'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_periodic_last_run'
op|'['
name|'task_name'
op|']'
op|'='
name|'_nearest_boundary'
op|'('
nl|'\n'
name|'last_run'
op|','
name|'spacing'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'task'
op|'('
name|'self'
op|','
name|'context'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'raise_on_error'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Error during %(full_task_name)s: %(e)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|'"full_task_name"'
op|':'
name|'full_task_name'
op|','
string|'"e"'
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'idle_for'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
