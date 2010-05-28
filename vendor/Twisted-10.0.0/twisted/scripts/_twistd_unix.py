begin_unit
comment|'# -*- test-case-name: twisted.test.test_twistd -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
name|'import'
name|'os'
op|','
name|'errno'
op|','
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
op|','
name|'syslog'
op|','
name|'logfile'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'util'
name|'import'
name|'switchUID'
op|','
name|'uidFromString'
op|','
name|'gidFromString'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'application'
name|'import'
name|'app'
op|','
name|'service'
newline|'\n'
name|'from'
name|'twisted'
name|'import'
name|'copyright'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_umask
name|'def'
name|'_umask'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'8'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServerOptions
dedent|''
name|'class'
name|'ServerOptions'
op|'('
name|'app'
op|'.'
name|'ServerOptions'
op|')'
op|':'
newline|'\n'
DECL|variable|synopsis
indent|'    '
name|'synopsis'
op|'='
string|'"Usage: twistd [options]"'
newline|'\n'
nl|'\n'
DECL|variable|optFlags
name|'optFlags'
op|'='
op|'['
op|'['
string|"'nodaemon'"
op|','
string|"'n'"
op|','
string|'"don\'t daemonize, don\'t use default umask of 0077"'
op|']'
op|','
nl|'\n'
op|'['
string|"'originalname'"
op|','
name|'None'
op|','
string|'"Don\'t try to change the process name"'
op|']'
op|','
nl|'\n'
op|'['
string|"'syslog'"
op|','
name|'None'
op|','
string|'"Log to syslog, not to file"'
op|']'
op|','
nl|'\n'
op|'['
string|"'euid'"
op|','
string|"''"
op|','
nl|'\n'
string|'"Set only effective user-id rather than real user-id. "'
nl|'\n'
string|'"(This option has no effect unless the server is running as "'
nl|'\n'
string|'"root, in which case it means not to shed all privileges "'
nl|'\n'
string|'"after binding ports, retaining the option to regain "'
nl|'\n'
string|'"privileges in cases such as spawning processes. "'
nl|'\n'
string|'"Use with caution.)"'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|optParameters
name|'optParameters'
op|'='
op|'['
nl|'\n'
op|'['
string|"'prefix'"
op|','
name|'None'
op|','
string|"'twisted'"
op|','
nl|'\n'
string|'"use the given prefix when syslogging"'
op|']'
op|','
nl|'\n'
op|'['
string|"'pidfile'"
op|','
string|"''"
op|','
string|"'twistd.pid'"
op|','
nl|'\n'
string|'"Name of the pidfile"'
op|']'
op|','
nl|'\n'
op|'['
string|"'chroot'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
string|"'Chroot to a supplied directory before running'"
op|']'
op|','
nl|'\n'
op|'['
string|"'uid'"
op|','
string|"'u'"
op|','
name|'None'
op|','
string|'"The uid to run as."'
op|','
name|'uidFromString'
op|']'
op|','
nl|'\n'
op|'['
string|"'gid'"
op|','
string|"'g'"
op|','
name|'None'
op|','
string|'"The gid to run as."'
op|','
name|'gidFromString'
op|']'
op|','
nl|'\n'
op|'['
string|"'umask'"
op|','
name|'None'
op|','
name|'None'
op|','
nl|'\n'
string|'"The (octal) file creation mask to apply."'
op|','
name|'_umask'
op|']'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|zsh_altArgDescr
name|'zsh_altArgDescr'
op|'='
op|'{'
string|'"prefix"'
op|':'
string|'"Use the given prefix when syslogging (default: twisted)"'
op|','
nl|'\n'
string|'"pidfile"'
op|':'
string|'"Name of the pidfile (default: twistd.pid)"'
op|','
op|'}'
newline|'\n'
comment|'#zsh_multiUse = ["foo", "bar"]'
nl|'\n'
comment|'#zsh_mutuallyExclusive = [("foo", "bar"), ("bar", "baz")]'
nl|'\n'
DECL|variable|zsh_actions
name|'zsh_actions'
op|'='
op|'{'
string|'"pidfile"'
op|':'
string|'\'_files -g "*.pid"\''
op|','
string|'"chroot"'
op|':'
string|"'_dirs'"
op|'}'
newline|'\n'
DECL|variable|zsh_actionDescr
name|'zsh_actionDescr'
op|'='
op|'{'
string|'"chroot"'
op|':'
string|'"chroot directory"'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|opt_version
name|'def'
name|'opt_version'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Print version information and exit.\n        """'
newline|'\n'
name|'print'
string|"'twistd (the Twisted daemon) %s'"
op|'%'
name|'copyright'
op|'.'
name|'version'
newline|'\n'
name|'print'
name|'copyright'
op|'.'
name|'copyright'
newline|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|postOptions
dedent|''
name|'def'
name|'postOptions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'.'
name|'ServerOptions'
op|'.'
name|'postOptions'
op|'('
name|'self'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'['
string|"'pidfile'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'['
string|"'pidfile'"
op|']'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'self'
op|'['
string|"'pidfile'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|checkPID
dedent|''
dedent|''
dedent|''
name|'def'
name|'checkPID'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'pidfile'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pid'
op|'='
name|'int'
op|'('
name|'open'
op|'('
name|'pidfile'
op|')'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'exit'
op|'('
string|"'Pidfile %s contains non-numeric value'"
op|'%'
name|'pidfile'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'why'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'why'
op|'['
number|'0'
op|']'
op|'=='
name|'errno'
op|'.'
name|'ESRCH'
op|':'
newline|'\n'
comment|'# The pid doesnt exists.'
nl|'\n'
indent|'                '
name|'log'
op|'.'
name|'msg'
op|'('
string|"'Removing stale pidfile %s'"
op|'%'
name|'pidfile'
op|','
name|'isError'
op|'='
name|'True'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'remove'
op|'('
name|'pidfile'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
string|'"Can\'t check status of PID %s from pidfile %s: %s"'
op|'%'
nl|'\n'
op|'('
name|'pid'
op|','
name|'pidfile'
op|','
name|'why'
op|'['
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'sys'
op|'.'
name|'exit'
op|'('
string|'"""\\\nAnother twistd server is running, PID %s\\n\nThis could either be a previously started instance of your application or a\ndifferent application entirely. To start a new one, either run it in some other\ndirectory, or use the --pidfile and --logfile parameters to avoid clashes.\n"""'
op|'%'
name|'pid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnixAppLogger
dedent|''
dedent|''
dedent|''
name|'class'
name|'UnixAppLogger'
op|'('
name|'app'
op|'.'
name|'AppLogger'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A logger able to log to syslog, to files, and to stdout.\n\n    @ivar _syslog: A flag indicating whether to use syslog instead of file\n        logging.\n    @type _syslog: C{bool}\n\n    @ivar _syslogPrefix: If C{sysLog} is C{True}, the string prefix to use for\n        syslog messages.\n    @type _syslogPrefix: C{str}\n\n    @ivar _nodaemon: A flag indicating the process will not be daemonizing.\n    @type _nodaemon: C{bool}\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'options'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'.'
name|'AppLogger'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'options'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_syslog'
op|'='
name|'options'
op|'.'
name|'get'
op|'('
string|'"syslog"'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_syslogPrefix'
op|'='
name|'options'
op|'.'
name|'get'
op|'('
string|'"prefix"'
op|','
string|'""'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_nodaemon'
op|'='
name|'options'
op|'.'
name|'get'
op|'('
string|'"nodaemon"'
op|','
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|_getLogObserver
dedent|''
name|'def'
name|'_getLogObserver'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create and return a suitable log observer for the given configuration.\n\n        The observer will go to syslog using the prefix C{_syslogPrefix} if\n        C{_syslog} is true.  Otherwise, it will go to the file named\n        C{_logfilename} or, if C{_nodaemon} is true and C{_logfilename} is\n        C{"-"}, to stdout.\n\n        @return: An object suitable to be passed to C{log.addObserver}.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_syslog'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'syslog'
op|'.'
name|'SyslogObserver'
op|'('
name|'self'
op|'.'
name|'_syslogPrefix'
op|')'
op|'.'
name|'emit'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_logfilename'
op|'=='
string|"'-'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_nodaemon'
op|':'
newline|'\n'
indent|'                '
name|'sys'
op|'.'
name|'exit'
op|'('
string|"'Daemons cannot log to stdout, exiting!'"
op|')'
newline|'\n'
dedent|''
name|'logFile'
op|'='
name|'sys'
op|'.'
name|'stdout'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'_nodaemon'
name|'and'
name|'not'
name|'self'
op|'.'
name|'_logfilename'
op|':'
newline|'\n'
indent|'            '
name|'logFile'
op|'='
name|'sys'
op|'.'
name|'stdout'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_logfilename'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_logfilename'
op|'='
string|"'twistd.log'"
newline|'\n'
dedent|''
name|'logFile'
op|'='
name|'logfile'
op|'.'
name|'LogFile'
op|'.'
name|'fromFullPath'
op|'('
name|'self'
op|'.'
name|'_logfilename'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'import'
name|'signal'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Override if signal is set to None or SIG_DFL (0)'
nl|'\n'
indent|'                '
name|'if'
name|'not'
name|'signal'
op|'.'
name|'getsignal'
op|'('
name|'signal'
op|'.'
name|'SIGUSR1'
op|')'
op|':'
newline|'\n'
DECL|function|rotateLog
indent|'                    '
name|'def'
name|'rotateLog'
op|'('
name|'signal'
op|','
name|'frame'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'callFromThread'
op|'('
name|'logFile'
op|'.'
name|'rotate'
op|')'
newline|'\n'
dedent|''
name|'signal'
op|'.'
name|'signal'
op|'('
name|'signal'
op|'.'
name|'SIGUSR1'
op|','
name|'rotateLog'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'log'
op|'.'
name|'FileLogObserver'
op|'('
name|'logFile'
op|')'
op|'.'
name|'emit'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|daemonize
dedent|''
dedent|''
name|'def'
name|'daemonize'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# See http://www.erlenstar.demon.co.uk/unix/faq_toc.html#TOC16'
nl|'\n'
indent|'    '
name|'if'
name|'os'
op|'.'
name|'fork'
op|'('
op|')'
op|':'
comment|'# launch child and...'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'_exit'
op|'('
number|'0'
op|')'
comment|'# kill off parent'
newline|'\n'
dedent|''
name|'os'
op|'.'
name|'setsid'
op|'('
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'fork'
op|'('
op|')'
op|':'
comment|'# launch child and...'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'_exit'
op|'('
number|'0'
op|')'
comment|'# kill off parent again.'
newline|'\n'
dedent|''
name|'null'
op|'='
name|'os'
op|'.'
name|'open'
op|'('
string|"'/dev/null'"
op|','
name|'os'
op|'.'
name|'O_RDWR'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'dup2'
op|'('
name|'null'
op|','
name|'i'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'!='
name|'errno'
op|'.'
name|'EBADF'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'os'
op|'.'
name|'close'
op|'('
name|'null'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|launchWithName
dedent|''
name|'def'
name|'launchWithName'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'name'
name|'and'
name|'name'
op|'!='
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'exe'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'realpath'
op|'('
name|'sys'
op|'.'
name|'executable'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'Changing process name to '"
op|'+'
name|'name'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'execv'
op|'('
name|'exe'
op|','
op|'['
name|'name'
op|','
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|','
string|"'--originalname'"
op|']'
op|'+'
name|'sys'
op|'.'
name|'argv'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|UnixApplicationRunner
dedent|''
dedent|''
name|'class'
name|'UnixApplicationRunner'
op|'('
name|'app'
op|'.'
name|'ApplicationRunner'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    An ApplicationRunner which does Unix-specific things, like fork,\n    shed privileges, and maintain a PID file.\n    """'
newline|'\n'
DECL|variable|loggerFactory
name|'loggerFactory'
op|'='
name|'UnixAppLogger'
newline|'\n'
nl|'\n'
DECL|member|preApplication
name|'def'
name|'preApplication'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Do pre-application-creation setup.\n        """'
newline|'\n'
name|'checkPID'
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|"'pidfile'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'config'
op|'['
string|"'nodaemon'"
op|']'
op|'='
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|"'nodaemon'"
op|']'
nl|'\n'
name|'or'
name|'self'
op|'.'
name|'config'
op|'['
string|"'debug'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'oldstdout'
op|'='
name|'sys'
op|'.'
name|'stdout'
newline|'\n'
name|'self'
op|'.'
name|'oldstderr'
op|'='
name|'sys'
op|'.'
name|'stderr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|postApplication
dedent|''
name|'def'
name|'postApplication'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        To be called after the application is created: start the\n        application and run the reactor. After the reactor stops,\n        clean up PID files and such.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'startApplication'
op|'('
name|'self'
op|'.'
name|'application'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'startReactor'
op|'('
name|'None'
op|','
name|'self'
op|'.'
name|'oldstdout'
op|','
name|'self'
op|'.'
name|'oldstderr'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'removePID'
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|"'pidfile'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|removePID
dedent|''
name|'def'
name|'removePID'
op|'('
name|'self'
op|','
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove the specified PID file, if possible.  Errors are logged, not\n        raised.\n\n        @type pidfile: C{str}\n        @param pidfile: The path to the PID tracking file.\n        """'
newline|'\n'
name|'if'
name|'not'
name|'pidfile'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'pidfile'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'EACCES'
name|'or'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'EPERM'
op|':'
newline|'\n'
indent|'                '
name|'log'
op|'.'
name|'msg'
op|'('
string|'"Warning: No permission to delete pid file"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'log'
op|'.'
name|'err'
op|'('
name|'e'
op|','
string|'"Failed to unlink PID file"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'err'
op|'('
name|'None'
op|','
string|'"Failed to unlink PID file"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setupEnvironment
dedent|''
dedent|''
name|'def'
name|'setupEnvironment'
op|'('
name|'self'
op|','
name|'chroot'
op|','
name|'rundir'
op|','
name|'nodaemon'
op|','
name|'umask'
op|','
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Set the filesystem root, the working directory, and daemonize.\n\n        @type chroot: C{str} or L{NoneType}\n        @param chroot: If not None, a path to use as the filesystem root (using\n            L{os.chroot}).\n\n        @type rundir: C{str}\n        @param rundir: The path to set as the working directory.\n\n        @type nodaemon: C{bool}\n        @param nodaemon: A flag which, if set, indicates that daemonization\n            should not be done.\n\n        @type umask: C{int} or L{NoneType}\n        @param umask: The value to which to change the process umask.\n\n        @type pidfile: C{str} or L{NoneType}\n        @param pidfile: If not C{None}, the path to a file into which to put\n            the PID of this process.\n        """'
newline|'\n'
name|'daemon'
op|'='
name|'not'
name|'nodaemon'
newline|'\n'
nl|'\n'
name|'if'
name|'chroot'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'chroot'
op|'('
name|'chroot'
op|')'
newline|'\n'
name|'if'
name|'rundir'
op|'=='
string|"'.'"
op|':'
newline|'\n'
indent|'                '
name|'rundir'
op|'='
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'os'
op|'.'
name|'chdir'
op|'('
name|'rundir'
op|')'
newline|'\n'
name|'if'
name|'daemon'
name|'and'
name|'umask'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'umask'
op|'='
number|'077'
newline|'\n'
dedent|''
name|'if'
name|'umask'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'umask'
op|'('
name|'umask'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'daemon'
op|':'
newline|'\n'
indent|'            '
name|'daemonize'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'pidfile'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'open'
op|'('
name|'pidfile'
op|','
string|"'wb'"
op|')'
newline|'\n'
name|'f'
op|'.'
name|'write'
op|'('
name|'str'
op|'('
name|'os'
op|'.'
name|'getpid'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|shedPrivileges
dedent|''
dedent|''
name|'def'
name|'shedPrivileges'
op|'('
name|'self'
op|','
name|'euid'
op|','
name|'uid'
op|','
name|'gid'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Change the UID and GID or the EUID and EGID of this process.\n\n        @type euid: C{bool}\n        @param euid: A flag which, if set, indicates that only the I{effective}\n            UID and GID should be set.\n\n        @type uid: C{int} or C{NoneType}\n        @param uid: If not C{None}, the UID to which to switch.\n\n        @type gid: C{int} or C{NoneType}\n        @param gid: If not C{None}, the GID to which to switch.\n        """'
newline|'\n'
name|'if'
name|'uid'
name|'is'
name|'not'
name|'None'
name|'or'
name|'gid'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'switchUID'
op|'('
name|'uid'
op|','
name|'gid'
op|','
name|'euid'
op|')'
newline|'\n'
name|'extra'
op|'='
name|'euid'
name|'and'
string|"'e'"
name|'or'
string|"''"
newline|'\n'
name|'log'
op|'.'
name|'msg'
op|'('
string|"'set %suid/%sgid %s/%s'"
op|'%'
op|'('
name|'extra'
op|','
name|'extra'
op|','
name|'uid'
op|','
name|'gid'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|startApplication
dedent|''
dedent|''
name|'def'
name|'startApplication'
op|'('
name|'self'
op|','
name|'application'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Configure global process state based on the given application and run\n        the application.\n\n        @param application: An object which can be adapted to\n            L{service.IProcess} and L{service.IService}.\n        """'
newline|'\n'
name|'process'
op|'='
name|'service'
op|'.'
name|'IProcess'
op|'('
name|'application'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'config'
op|'['
string|"'originalname'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'launchWithName'
op|'('
name|'process'
op|'.'
name|'processName'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'setupEnvironment'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'config'
op|'['
string|"'chroot'"
op|']'
op|','
name|'self'
op|'.'
name|'config'
op|'['
string|"'rundir'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'config'
op|'['
string|"'nodaemon'"
op|']'
op|','
name|'self'
op|'.'
name|'config'
op|'['
string|"'umask'"
op|']'
op|','
nl|'\n'
name|'self'
op|'.'
name|'config'
op|'['
string|"'pidfile'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'service'
op|'.'
name|'IService'
op|'('
name|'application'
op|')'
op|'.'
name|'privilegedStartService'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'uid'
op|','
name|'gid'
op|'='
name|'self'
op|'.'
name|'config'
op|'['
string|"'uid'"
op|']'
op|','
name|'self'
op|'.'
name|'config'
op|'['
string|"'gid'"
op|']'
newline|'\n'
name|'if'
name|'uid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'uid'
op|'='
name|'process'
op|'.'
name|'uid'
newline|'\n'
dedent|''
name|'if'
name|'gid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'gid'
op|'='
name|'process'
op|'.'
name|'gid'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'shedPrivileges'
op|'('
name|'self'
op|'.'
name|'config'
op|'['
string|"'euid'"
op|']'
op|','
name|'uid'
op|','
name|'gid'
op|')'
newline|'\n'
name|'app'
op|'.'
name|'startApplication'
op|'('
name|'application'
op|','
name|'not'
name|'self'
op|'.'
name|'config'
op|'['
string|"'no_save'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
