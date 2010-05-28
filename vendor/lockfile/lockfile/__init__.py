begin_unit
nl|'\n'
string|'"""\nlockfile.py - Platform-independent advisory file locks.\n\nRequires Python 2.5 unless you apply 2.4.diff\nLocking is done on a per-thread basis instead of a per-process basis.\n\nUsage:\n\n>>> lock = LockFile(\'somefile\')\n>>> try:\n...     lock.acquire()\n... except AlreadyLocked:\n...     print \'somefile\', \'is locked already.\'\n... except LockFailed:\n...     print \'somefile\', \'can\\\\\'t be locked.\'\n... else:\n...     print \'got lock\'\ngot lock\n>>> print lock.is_locked()\nTrue\n>>> lock.release()\n\n>>> lock = LockFile(\'somefile\')\n>>> print lock.is_locked()\nFalse\n>>> with lock:\n...    print lock.is_locked()\nTrue\n>>> print lock.is_locked()\nFalse\n\n>>> lock = LockFile(\'somefile\')\n>>> # It is okay to lock twice from the same thread...\n>>> with lock:\n...     lock.acquire()\n...\n>>> # Though no counter is kept, so you can\'t unlock multiple times...\n>>> print lock.is_locked()\nFalse\n\nExceptions:\n\n    Error - base class for other exceptions\n        LockError - base class for all locking exceptions\n            AlreadyLocked - Another thread or process already holds the lock\n            LockFailed - Lock failed for some other reason\n        UnlockError - base class for all unlocking exceptions\n            AlreadyUnlocked - File was not locked.\n            NotMyLock - File was locked but not by the current thread/process\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'threading'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'urllib'
newline|'\n'
name|'import'
name|'warnings'
newline|'\n'
nl|'\n'
comment|'# Work with PEP8 and non-PEP8 versions of threading module.'
nl|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'threading'
op|','
string|'"current_thread"'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'threading'
op|'.'
name|'current_thread'
op|'='
name|'threading'
op|'.'
name|'currentThread'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'threading'
op|'.'
name|'Thread'
op|','
string|'"get_name"'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'threading'
op|'.'
name|'Thread'
op|'.'
name|'get_name'
op|'='
name|'threading'
op|'.'
name|'Thread'
op|'.'
name|'getName'
newline|'\n'
nl|'\n'
DECL|variable|__all__
dedent|''
name|'__all__'
op|'='
op|'['
string|"'Error'"
op|','
string|"'LockError'"
op|','
string|"'LockTimeout'"
op|','
string|"'AlreadyLocked'"
op|','
nl|'\n'
string|"'LockFailed'"
op|','
string|"'UnlockError'"
op|','
string|"'NotLocked'"
op|','
string|"'NotMyLock'"
op|','
nl|'\n'
string|"'LinkLockFile'"
op|','
string|"'MkdirLockFile'"
op|','
string|"'SQLiteLockFile'"
op|','
nl|'\n'
string|"'LockBase'"
op|']'
newline|'\n'
nl|'\n'
DECL|class|Error
name|'class'
name|'Error'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base class for other exceptions.\n\n    >>> try:\n    ...   raise Error\n    ... except Exception:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|LockError
dedent|''
name|'class'
name|'LockError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base class for error arising from attempts to acquire the lock.\n\n    >>> try:\n    ...   raise LockError\n    ... except Error:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|LockTimeout
dedent|''
name|'class'
name|'LockTimeout'
op|'('
name|'LockError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when lock creation fails within a user-defined period of time.\n\n    >>> try:\n    ...   raise LockTimeout\n    ... except LockError:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|AlreadyLocked
dedent|''
name|'class'
name|'AlreadyLocked'
op|'('
name|'LockError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Some other thread/process is locking the file.\n\n    >>> try:\n    ...   raise AlreadyLocked\n    ... except LockError:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|LockFailed
dedent|''
name|'class'
name|'LockFailed'
op|'('
name|'LockError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Lock file creation failed for some other reason.\n\n    >>> try:\n    ...   raise LockFailed\n    ... except LockError:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|UnlockError
dedent|''
name|'class'
name|'UnlockError'
op|'('
name|'Error'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Base class for errors arising from attempts to release the lock.\n\n    >>> try:\n    ...   raise UnlockError\n    ... except Error:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|NotLocked
dedent|''
name|'class'
name|'NotLocked'
op|'('
name|'UnlockError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when an attempt is made to unlock an unlocked file.\n\n    >>> try:\n    ...   raise NotLocked\n    ... except UnlockError:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|NotMyLock
dedent|''
name|'class'
name|'NotMyLock'
op|'('
name|'UnlockError'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Raised when an attempt is made to unlock a file someone else locked.\n\n    >>> try:\n    ...   raise NotMyLock\n    ... except UnlockError:\n    ...   pass\n    """'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|class|LockBase
dedent|''
name|'class'
name|'LockBase'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for platform-specific lock classes."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'threaded'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        >>> lock = LockBase(\'somefile\')\n        >>> lock = LockBase(\'somefile\', threaded=False)\n        """'
newline|'\n'
name|'self'
op|'.'
name|'path'
op|'='
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'lock_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'path'
op|')'
op|'+'
string|'".lock"'
newline|'\n'
name|'self'
op|'.'
name|'hostname'
op|'='
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'pid'
op|'='
name|'os'
op|'.'
name|'getpid'
op|'('
op|')'
newline|'\n'
name|'if'
name|'threaded'
op|':'
newline|'\n'
indent|'            '
name|'t'
op|'='
name|'threading'
op|'.'
name|'current_thread'
op|'('
op|')'
newline|'\n'
comment|'# Thread objects in Python 2.4 and earlier do not have ident'
nl|'\n'
comment|'# attrs.  Worm around that.'
nl|'\n'
name|'ident'
op|'='
name|'getattr'
op|'('
name|'t'
op|','
string|'"ident"'
op|','
name|'hash'
op|'('
name|'t'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tname'
op|'='
string|'"%x-"'
op|'%'
op|'('
name|'ident'
op|'&'
number|'0xffffffff'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'tname'
op|'='
string|'""'
newline|'\n'
dedent|''
name|'dirname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'self'
op|'.'
name|'lock_file'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'unique_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dirname'
op|','
nl|'\n'
string|'"%s.%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'hostname'
op|','
nl|'\n'
name|'self'
op|'.'
name|'tname'
op|','
nl|'\n'
name|'self'
op|'.'
name|'pid'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|acquire
dedent|''
name|'def'
name|'acquire'
op|'('
name|'self'
op|','
name|'timeout'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Acquire the lock.\n\n        * If timeout is omitted (or None), wait forever trying to lock the\n          file.\n\n        * If timeout > 0, try to acquire the lock for that many seconds.  If\n          the lock period expires and the file is still locked, raise\n          LockTimeout.\n\n        * If timeout <= 0, raise AlreadyLocked immediately if the file is\n          already locked.\n        """'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
string|'"implement in subclass"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|release
dedent|''
name|'def'
name|'release'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Release the lock.\n\n        If the file is not locked, raise NotLocked.\n        """'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
string|'"implement in subclass"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_locked
dedent|''
name|'def'
name|'is_locked'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Tell whether or not the file is locked.\n        """'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
string|'"implement in subclass"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|i_am_locking
dedent|''
name|'def'
name|'i_am_locking'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return True if this object is locking the file.\n        """'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
string|'"implement in subclass"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|break_lock
dedent|''
name|'def'
name|'break_lock'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Remove a lock.  Useful if a locking thread failed to unlock.\n        """'
newline|'\n'
name|'raise'
name|'NotImplemented'
op|'('
string|'"implement in subclass"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Context manager support.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'acquire'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
op|'*'
name|'_exc'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Context manager support.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'release'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fl_helper
dedent|''
dedent|''
name|'def'
name|'_fl_helper'
op|'('
name|'cls'
op|','
name|'mod'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'warnings'
op|'.'
name|'warn'
op|'('
string|'"Import from %s module instead of lockfile package"'
op|'%'
name|'mod'
op|','
nl|'\n'
name|'DeprecationWarning'
op|','
name|'stacklevel'
op|'='
number|'2'
op|')'
newline|'\n'
comment|"# This is a bit funky, but it's only for awhile.  The way the unit tests"
nl|'\n'
comment|'# are constructed this function winds up as an unbound method, so it'
nl|'\n'
comment|'# actually takes three args, not two.  We want to toss out self.'
nl|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'args'
op|'['
number|'0'
op|']'
op|','
name|'str'
op|')'
op|':'
newline|'\n'
comment|'# We are testing, avoid the first arg'
nl|'\n'
indent|'        '
name|'args'
op|'='
name|'args'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'args'
op|')'
op|'=='
number|'1'
name|'and'
name|'not'
name|'kwds'
op|':'
newline|'\n'
indent|'        '
name|'kwds'
op|'['
string|'"threaded"'
op|']'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'cls'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
nl|'\n'
DECL|function|LinkFileLock
dedent|''
name|'def'
name|'LinkFileLock'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Factory function provided for backwards compatibility.\n\n    Do not use in new code.  Instead, import LinkLockFile from the\n    lockfile.linklockfile module.\n    """'
newline|'\n'
name|'import'
name|'linklockfile'
newline|'\n'
name|'return'
name|'_fl_helper'
op|'('
name|'linklockfile'
op|'.'
name|'LinkLockFile'
op|','
string|'"lockfile.linklockfile"'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
nl|'\n'
DECL|function|MkdirFileLock
dedent|''
name|'def'
name|'MkdirFileLock'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Factory function provided for backwards compatibility.\n\n    Do not use in new code.  Instead, import MkdirLockFile from the\n    lockfile.mkdirlockfile module.\n    """'
newline|'\n'
name|'import'
name|'mkdirlockfile'
newline|'\n'
name|'return'
name|'_fl_helper'
op|'('
name|'mkdirlockfile'
op|'.'
name|'MkdirLockFile'
op|','
string|'"lockfile.mkdirlockfile"'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
nl|'\n'
DECL|function|SQLiteFileLock
dedent|''
name|'def'
name|'SQLiteFileLock'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Factory function provided for backwards compatibility.\n\n    Do not use in new code.  Instead, import SQLiteLockFile from the\n    lockfile.mkdirlockfile module.\n    """'
newline|'\n'
name|'import'
name|'sqlitelockfile'
newline|'\n'
name|'return'
name|'_fl_helper'
op|'('
name|'sqlitelockfile'
op|'.'
name|'SQLiteLockFile'
op|','
string|'"lockfile.sqlitelockfile"'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwds'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'os'
op|','
string|'"link"'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'linklockfile'
name|'as'
name|'_llf'
newline|'\n'
name|'LockFile'
op|'='
name|'_llf'
op|'.'
name|'LinkLockFile'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'mkdirlockfile'
name|'as'
name|'_mlf'
newline|'\n'
DECL|variable|LockFile
name|'LockFile'
op|'='
name|'_mlf'
op|'.'
name|'MkdirLockFile'
newline|'\n'
nl|'\n'
DECL|variable|FileLock
dedent|''
name|'FileLock'
op|'='
name|'LockFile'
newline|'\n'
nl|'\n'
endmarker|''
end_unit
