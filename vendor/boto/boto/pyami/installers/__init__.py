begin_unit
comment|'# Copyright (c) 2006,2007,2008 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, '
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
comment|'#'
nl|'\n'
name|'from'
name|'boto'
op|'.'
name|'pyami'
op|'.'
name|'scriptbase'
name|'import'
name|'ScriptBase'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Installer
name|'class'
name|'Installer'
op|'('
name|'ScriptBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Abstract base class for installers\n    """'
newline|'\n'
nl|'\n'
DECL|member|add_cron
name|'def'
name|'add_cron'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'minute'
op|','
name|'hour'
op|','
name|'mday'
op|','
name|'month'
op|','
name|'wday'
op|','
name|'who'
op|','
name|'command'
op|','
name|'env'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add an entry to the system crontab.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|add_init_script
dedent|''
name|'def'
name|'add_init_script'
op|'('
name|'self'
op|','
name|'file'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add this file to the init.d directory\n        """'
newline|'\n'
nl|'\n'
DECL|member|add_env
dedent|''
name|'def'
name|'add_env'
op|'('
name|'self'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Add an environemnt variable\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|','
name|'service_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Stop a service.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|start
dedent|''
name|'def'
name|'start'
op|'('
name|'self'
op|','
name|'service_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Start a service.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|install
dedent|''
name|'def'
name|'install'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Do whatever is necessary to "install" the package.\n        """'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
