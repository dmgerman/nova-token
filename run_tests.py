begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
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
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
comment|'# Colorizer Code is borrowed from Twisted:'
nl|'\n'
comment|'# Copyright (c) 2001-2010 Twisted Matrix Laboratories.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Permission is hereby granted, free of charge, to any person obtaining'
nl|'\n'
comment|'#    a copy of this software and associated documentation files (the'
nl|'\n'
comment|'#    "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'#    without limitation the rights to use, copy, modify, merge, publish,'
nl|'\n'
comment|'#    distribute, sublicense, and/or sell copies of the Software, and to'
nl|'\n'
comment|'#    permit persons to whom the Software is furnished to do so, subject to'
nl|'\n'
comment|'#    the following conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    The above copyright notice and this permission notice shall be'
nl|'\n'
comment|'#    included in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,'
nl|'\n'
comment|'#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF'
nl|'\n'
comment|'#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND'
nl|'\n'
comment|'#    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE'
nl|'\n'
comment|'#    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION'
nl|'\n'
comment|'#    OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION'
nl|'\n'
comment|'#    WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'nose'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nose'
name|'import'
name|'core'
newline|'\n'
name|'from'
name|'nose'
name|'import'
name|'result'
newline|'\n'
nl|'\n'
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
op|'.'
name|'tests'
name|'import'
name|'fake_flags'
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
nl|'\n'
nl|'\n'
DECL|class|_AnsiColorizer
name|'class'
name|'_AnsiColorizer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A colorizer is an object that loosely wraps around a stream, allowing\n    callers to write text to the stream in a particular color.\n\n    Colorizer classes must implement C{supported()} and C{write(text, color)}.\n    """'
newline|'\n'
DECL|variable|_colors
name|'_colors'
op|'='
name|'dict'
op|'('
name|'black'
op|'='
number|'30'
op|','
name|'red'
op|'='
number|'31'
op|','
name|'green'
op|'='
number|'32'
op|','
name|'yellow'
op|'='
number|'33'
op|','
nl|'\n'
name|'blue'
op|'='
number|'34'
op|','
name|'magenta'
op|'='
number|'35'
op|','
name|'cyan'
op|'='
number|'36'
op|','
name|'white'
op|'='
number|'37'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stream'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stream'
op|'='
name|'stream'
newline|'\n'
nl|'\n'
DECL|member|supported
dedent|''
name|'def'
name|'supported'
op|'('
name|'cls'
op|','
name|'stream'
op|'='
name|'sys'
op|'.'
name|'stdout'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        A class method that returns True if the current platform supports\n        coloring terminal output using this method. Returns False otherwise.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'stream'
op|'.'
name|'isatty'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
comment|'# auto color only on TTYs'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'import'
name|'curses'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'curses'
op|'.'
name|'tigetnum'
op|'('
string|'"colors"'
op|')'
op|'>'
number|'2'
newline|'\n'
dedent|''
name|'except'
name|'curses'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'                    '
name|'curses'
op|'.'
name|'setupterm'
op|'('
op|')'
newline|'\n'
name|'return'
name|'curses'
op|'.'
name|'tigetnum'
op|'('
string|'"colors"'
op|')'
op|'>'
number|'2'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
comment|'# guess false in case of error'
nl|'\n'
name|'return'
name|'False'
newline|'\n'
DECL|variable|supported
dedent|''
dedent|''
dedent|''
name|'supported'
op|'='
name|'classmethod'
op|'('
name|'supported'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'text'
op|','
name|'color'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Write the given text to the stream in the given color.\n\n        @param text: Text to be written to the stream.\n\n        @param color: A string label for a color. e.g. \'red\', \'white\'.\n        """'
newline|'\n'
name|'color'
op|'='
name|'self'
op|'.'
name|'_colors'
op|'['
name|'color'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
string|"'\\x1b[%s;1m%s\\x1b[0m'"
op|'%'
op|'('
name|'color'
op|','
name|'text'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_Win32Colorizer
dedent|''
dedent|''
name|'class'
name|'_Win32Colorizer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    See _AnsiColorizer docstring.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stream'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'win32console'
name|'import'
name|'GetStdHandle'
op|','
name|'STD_OUT_HANDLE'
op|','
name|'FOREGROUND_RED'
op|','
name|'FOREGROUND_BLUE'
op|','
name|'FOREGROUND_GREEN'
op|','
name|'FOREGROUND_INTENSITY'
newline|'\n'
name|'red'
op|','
name|'green'
op|','
name|'blue'
op|','
name|'bold'
op|'='
op|'('
name|'FOREGROUND_RED'
op|','
name|'FOREGROUND_GREEN'
op|','
nl|'\n'
name|'FOREGROUND_BLUE'
op|','
name|'FOREGROUND_INTENSITY'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'='
name|'stream'
newline|'\n'
name|'self'
op|'.'
name|'screenBuffer'
op|'='
name|'GetStdHandle'
op|'('
name|'STD_OUT_HANDLE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_colors'
op|'='
op|'{'
nl|'\n'
string|"'normal'"
op|':'
name|'red'
op|'|'
name|'green'
op|'|'
name|'blue'
op|','
nl|'\n'
string|"'red'"
op|':'
name|'red'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'green'"
op|':'
name|'green'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'blue'"
op|':'
name|'blue'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'yellow'"
op|':'
name|'red'
op|'|'
name|'green'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'magenta'"
op|':'
name|'red'
op|'|'
name|'blue'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'cyan'"
op|':'
name|'green'
op|'|'
name|'blue'
op|'|'
name|'bold'
op|','
nl|'\n'
string|"'white'"
op|':'
name|'red'
op|'|'
name|'green'
op|'|'
name|'blue'
op|'|'
name|'bold'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|supported
dedent|''
name|'def'
name|'supported'
op|'('
name|'cls'
op|','
name|'stream'
op|'='
name|'sys'
op|'.'
name|'stdout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'import'
name|'win32console'
newline|'\n'
name|'screenBuffer'
op|'='
name|'win32console'
op|'.'
name|'GetStdHandle'
op|'('
nl|'\n'
name|'win32console'
op|'.'
name|'STD_OUT_HANDLE'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'import'
name|'pywintypes'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'screenBuffer'
op|'.'
name|'SetConsoleTextAttribute'
op|'('
nl|'\n'
name|'win32console'
op|'.'
name|'FOREGROUND_RED'
op|'|'
nl|'\n'
name|'win32console'
op|'.'
name|'FOREGROUND_GREEN'
op|'|'
nl|'\n'
name|'win32console'
op|'.'
name|'FOREGROUND_BLUE'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'pywintypes'
op|'.'
name|'error'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
DECL|variable|supported
dedent|''
dedent|''
name|'supported'
op|'='
name|'classmethod'
op|'('
name|'supported'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'text'
op|','
name|'color'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'color'
op|'='
name|'self'
op|'.'
name|'_colors'
op|'['
name|'color'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'screenBuffer'
op|'.'
name|'SetConsoleTextAttribute'
op|'('
name|'color'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'screenBuffer'
op|'.'
name|'SetConsoleTextAttribute'
op|'('
name|'self'
op|'.'
name|'_colors'
op|'['
string|"'normal'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_NullColorizer
dedent|''
dedent|''
name|'class'
name|'_NullColorizer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    See _AnsiColorizer docstring.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'stream'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stream'
op|'='
name|'stream'
newline|'\n'
nl|'\n'
DECL|member|supported
dedent|''
name|'def'
name|'supported'
op|'('
name|'cls'
op|','
name|'stream'
op|'='
name|'sys'
op|'.'
name|'stdout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
DECL|variable|supported
dedent|''
name|'supported'
op|'='
name|'classmethod'
op|'('
name|'supported'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'text'
op|','
name|'color'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|class|NovaTestResult
dedent|''
dedent|''
name|'class'
name|'NovaTestResult'
op|'('
name|'result'
op|'.'
name|'TextTestResult'
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
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'.'
name|'TextTestResult'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_last_case'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'colorizer'
op|'='
name|'None'
newline|'\n'
comment|'# NOTE(vish): reset stdout for the terminal check'
nl|'\n'
name|'stdout'
op|'='
name|'sys'
op|'.'
name|'stdout'
newline|'\n'
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'sys'
op|'.'
name|'__stdout__'
newline|'\n'
name|'for'
name|'colorizer'
name|'in'
op|'['
name|'_Win32Colorizer'
op|','
name|'_AnsiColorizer'
op|','
name|'_NullColorizer'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'colorizer'
op|'.'
name|'supported'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'colorizer'
op|'='
name|'colorizer'
op|'('
name|'self'
op|'.'
name|'stream'
op|')'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'sys'
op|'.'
name|'stdout'
op|'='
name|'stdout'
newline|'\n'
nl|'\n'
DECL|member|getDescription
dedent|''
name|'def'
name|'getDescription'
op|'('
name|'self'
op|','
name|'test'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'test'
op|')'
newline|'\n'
nl|'\n'
DECL|member|addSuccess
dedent|''
name|'def'
name|'addSuccess'
op|'('
name|'self'
op|','
name|'test'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'unittest'
op|'.'
name|'TestResult'
op|'.'
name|'addSuccess'
op|'('
name|'self'
op|','
name|'test'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'showAll'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'colorizer'
op|'.'
name|'write'
op|'('
string|'"OK"'
op|','
string|"'green'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'writeln'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'dots'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|addFailure
dedent|''
dedent|''
name|'def'
name|'addFailure'
op|'('
name|'self'
op|','
name|'test'
op|','
name|'err'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'unittest'
op|'.'
name|'TestResult'
op|'.'
name|'addFailure'
op|'('
name|'self'
op|','
name|'test'
op|','
name|'err'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'showAll'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'colorizer'
op|'.'
name|'write'
op|'('
string|'"FAIL"'
op|','
string|"'red'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'writeln'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'dots'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
string|"'F'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|addError
dedent|''
dedent|''
name|'def'
name|'addError'
op|'('
name|'self'
op|','
name|'test'
op|','
name|'err'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Overrides normal addError to add support for\n        errorClasses. If the exception is a registered class, the\n        error will be added to the list for that class, not errors.\n        """'
newline|'\n'
name|'stream'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|"'stream'"
op|','
name|'None'
op|')'
newline|'\n'
name|'ec'
op|','
name|'ev'
op|','
name|'tb'
op|'='
name|'err'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'exc_info'
op|'='
name|'self'
op|'.'
name|'_exc_info_to_string'
op|'('
name|'err'
op|','
name|'test'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|'# 2.3 compat'
nl|'\n'
indent|'            '
name|'exc_info'
op|'='
name|'self'
op|'.'
name|'_exc_info_to_string'
op|'('
name|'err'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'cls'
op|','
op|'('
name|'storage'
op|','
name|'label'
op|','
name|'isfail'
op|')'
name|'in'
name|'self'
op|'.'
name|'errorClasses'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'result'
op|'.'
name|'isclass'
op|'('
name|'ec'
op|')'
name|'and'
name|'issubclass'
op|'('
name|'ec'
op|','
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'isfail'
op|':'
newline|'\n'
indent|'                    '
name|'test'
op|'.'
name|'passed'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'storage'
op|'.'
name|'append'
op|'('
op|'('
name|'test'
op|','
name|'exc_info'
op|')'
op|')'
newline|'\n'
comment|'# Might get patched into a streamless result'
nl|'\n'
name|'if'
name|'stream'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'self'
op|'.'
name|'showAll'
op|':'
newline|'\n'
indent|'                        '
name|'message'
op|'='
op|'['
name|'label'
op|']'
newline|'\n'
name|'detail'
op|'='
name|'result'
op|'.'
name|'_exception_detail'
op|'('
name|'err'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'if'
name|'detail'
op|':'
newline|'\n'
indent|'                            '
name|'message'
op|'.'
name|'append'
op|'('
name|'detail'
op|')'
newline|'\n'
dedent|''
name|'stream'
op|'.'
name|'writeln'
op|'('
string|'": "'
op|'.'
name|'join'
op|'('
name|'message'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'dots'
op|':'
newline|'\n'
indent|'                        '
name|'stream'
op|'.'
name|'write'
op|'('
name|'label'
op|'['
op|':'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'errors'
op|'.'
name|'append'
op|'('
op|'('
name|'test'
op|','
name|'exc_info'
op|')'
op|')'
newline|'\n'
name|'test'
op|'.'
name|'passed'
op|'='
name|'False'
newline|'\n'
name|'if'
name|'stream'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'showAll'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'colorizer'
op|'.'
name|'write'
op|'('
string|'"ERROR"'
op|','
string|"'red'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'writeln'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'dots'
op|':'
newline|'\n'
indent|'                '
name|'stream'
op|'.'
name|'write'
op|'('
string|"'E'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|startTest
dedent|''
dedent|''
dedent|''
name|'def'
name|'startTest'
op|'('
name|'self'
op|','
name|'test'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'unittest'
op|'.'
name|'TestResult'
op|'.'
name|'startTest'
op|'('
name|'self'
op|','
name|'test'
op|')'
newline|'\n'
name|'current_case'
op|'='
name|'test'
op|'.'
name|'test'
op|'.'
name|'__class__'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'showAll'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'current_case'
op|'!='
name|'self'
op|'.'
name|'_last_case'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'stream'
op|'.'
name|'writeln'
op|'('
name|'current_case'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_last_case'
op|'='
name|'current_case'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stream'
op|'.'
name|'write'
op|'('
nl|'\n'
string|"'    %s'"
op|'%'
name|'str'
op|'('
name|'test'
op|'.'
name|'test'
op|'.'
name|'_testMethodName'
op|')'
op|'.'
name|'ljust'
op|'('
number|'60'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'.'
name|'flush'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaTestRunner
dedent|''
dedent|''
dedent|''
name|'class'
name|'NovaTestRunner'
op|'('
name|'core'
op|'.'
name|'TextTestRunner'
op|')'
op|':'
newline|'\n'
DECL|member|_makeResult
indent|'    '
name|'def'
name|'_makeResult'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'NovaTestResult'
op|'('
name|'self'
op|'.'
name|'stream'
op|','
nl|'\n'
name|'self'
op|'.'
name|'descriptions'
op|','
nl|'\n'
name|'self'
op|'.'
name|'verbosity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'config'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'logging'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
DECL|variable|testdir
name|'testdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|'"nova"'
op|','
string|'"tests"'
op|')'
op|')'
newline|'\n'
DECL|variable|c
name|'c'
op|'='
name|'config'
op|'.'
name|'Config'
op|'('
name|'stream'
op|'='
name|'sys'
op|'.'
name|'stdout'
op|','
nl|'\n'
name|'env'
op|'='
name|'os'
op|'.'
name|'environ'
op|','
nl|'\n'
name|'verbosity'
op|'='
number|'3'
op|','
nl|'\n'
name|'workingDir'
op|'='
name|'testdir'
op|','
nl|'\n'
name|'plugins'
op|'='
name|'core'
op|'.'
name|'DefaultPluginManager'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|runner
name|'runner'
op|'='
name|'NovaTestRunner'
op|'('
name|'stream'
op|'='
name|'c'
op|'.'
name|'stream'
op|','
nl|'\n'
name|'verbosity'
op|'='
name|'c'
op|'.'
name|'verbosity'
op|','
nl|'\n'
name|'config'
op|'='
name|'c'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
name|'not'
name|'core'
op|'.'
name|'run'
op|'('
name|'config'
op|'='
name|'c'
op|','
name|'testRunner'
op|'='
name|'runner'
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
