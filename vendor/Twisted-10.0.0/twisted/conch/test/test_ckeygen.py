begin_unit
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.conch.scripts.ckeygen}.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'from'
name|'StringIO'
name|'import'
name|'StringIO'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'Crypto'
newline|'\n'
name|'import'
name|'pyasn1'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|skip
indent|'    '
name|'skip'
op|'='
string|'"PyCrypto and pyasn1 required for twisted.conch.scripts.ckeygen."'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'conch'
op|'.'
name|'ssh'
op|'.'
name|'keys'
name|'import'
name|'Key'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'conch'
op|'.'
name|'scripts'
op|'.'
name|'ckeygen'
name|'import'
name|'printFingerprint'
op|','
name|'_saveKey'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'filepath'
name|'import'
name|'FilePath'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
op|'.'
name|'unittest'
name|'import'
name|'TestCase'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'conch'
op|'.'
name|'test'
op|'.'
name|'keydata'
name|'import'
name|'publicRSA_openssh'
op|','
name|'privateRSA_openssh'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|KeyGenTests
name|'class'
name|'KeyGenTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for various functions used to implement the I{ckeygen} script.\n    """'
newline|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Patch C{sys.stdout} with a L{StringIO} instance to tests can make\n        assertions about what\'s printed.\n        """'
newline|'\n'
name|'self'
op|'.'
name|'stdout'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'patch'
op|'('
name|'sys'
op|','
string|"'stdout'"
op|','
name|'self'
op|'.'
name|'stdout'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_printFingerprint
dedent|''
name|'def'
name|'test_printFingerprint'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{printFingerprint} writes a line to standard out giving the number of\n        bits of the key, its fingerprint, and the basename of the file from it\n        was read.\n        """'
newline|'\n'
name|'filename'
op|'='
name|'self'
op|'.'
name|'mktemp'
op|'('
op|')'
newline|'\n'
name|'FilePath'
op|'('
name|'filename'
op|')'
op|'.'
name|'setContent'
op|'('
name|'publicRSA_openssh'
op|')'
newline|'\n'
name|'printFingerprint'
op|'('
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'stdout'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
nl|'\n'
string|"'768 3d:13:5f:cb:c9:79:8a:93:06:27:65:bc:3d:0b:8f:af temp\\n'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_saveKey
dedent|''
name|'def'
name|'test_saveKey'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{_saveKey} writes the private and public parts of a key to two\n        different files and writes a report of this to standard out.\n        """'
newline|'\n'
name|'base'
op|'='
name|'FilePath'
op|'('
name|'self'
op|'.'
name|'mktemp'
op|'('
op|')'
op|')'
newline|'\n'
name|'base'
op|'.'
name|'makedirs'
op|'('
op|')'
newline|'\n'
name|'filename'
op|'='
name|'base'
op|'.'
name|'child'
op|'('
string|"'id_rsa'"
op|')'
op|'.'
name|'path'
newline|'\n'
name|'key'
op|'='
name|'Key'
op|'.'
name|'fromString'
op|'('
name|'privateRSA_openssh'
op|')'
newline|'\n'
name|'_saveKey'
op|'('
nl|'\n'
name|'key'
op|'.'
name|'keyObject'
op|','
nl|'\n'
op|'{'
string|"'filename'"
op|':'
name|'filename'
op|','
string|"'pass'"
op|':'
string|"'passphrase'"
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'stdout'
op|'.'
name|'getvalue'
op|'('
op|')'
op|','
nl|'\n'
string|'"Your identification has been saved in %s\\n"'
nl|'\n'
string|'"Your public key has been saved in %s.pub\\n"'
nl|'\n'
string|'"The key fingerprint is:\\n"'
nl|'\n'
string|'"3d:13:5f:cb:c9:79:8a:93:06:27:65:bc:3d:0b:8f:af\\n"'
op|'%'
op|'('
nl|'\n'
name|'filename'
op|','
nl|'\n'
name|'filename'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'key'
op|'.'
name|'fromString'
op|'('
nl|'\n'
name|'base'
op|'.'
name|'child'
op|'('
string|"'id_rsa'"
op|')'
op|'.'
name|'getContent'
op|'('
op|')'
op|','
name|'None'
op|','
string|"'passphrase'"
op|')'
op|','
nl|'\n'
name|'key'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'Key'
op|'.'
name|'fromString'
op|'('
name|'base'
op|'.'
name|'child'
op|'('
string|"'id_rsa.pub'"
op|')'
op|'.'
name|'getContent'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'key'
op|'.'
name|'public'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
