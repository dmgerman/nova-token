begin_unit
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nTests for L{twisted.python.hashlib}\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'trial'
op|'.'
name|'unittest'
name|'import'
name|'TestCase'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'hashlib'
name|'import'
name|'md5'
op|','
name|'sha1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HashObjectTests
name|'class'
name|'HashObjectTests'
op|'('
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests for the hash object APIs presented by L{hashlib}, C{md5} and C{sha1}.\n    """'
newline|'\n'
DECL|member|test_md5
name|'def'
name|'test_md5'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{hashlib.md5} returns an object which can be used to compute an MD5\n        hash as defined by U{RFC 1321<http://www.ietf.org/rfc/rfc1321.txt>}.\n        """'
newline|'\n'
comment|'# Test the result using values from section A.5 of the RFC.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
string|'"d41d8cd98f00b204e9800998ecf8427e"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"a"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
string|'"0cc175b9c0f1b6a831c399e269772661"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"abc"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
string|'"900150983cd24fb0d6963f7d28e17f72"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"message digest"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
string|'"f96b697d7cb7938d525a2f31aaf161d0"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"abcdefghijklmnopqrstuvwxyz"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
string|'"c3fcd3d76192e4007dfb496cca67e13b"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"'
nl|'\n'
string|'"0123456789"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
string|'"d174ab98d277d9f5a5611c2c9f419d9f"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
string|'"1234567890123456789012345678901234567890123456789012345678901"'
nl|'\n'
string|'"2345678901234567890"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
string|'"57edf4a22be3c955ac49da2e2107b67a"'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should have digest and update methods, too.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'md5'
op|'('
op|')'
op|'.'
name|'digest'
op|'('
op|')'
op|'.'
name|'encode'
op|'('
string|"'hex'"
op|')'
op|','
nl|'\n'
string|'"d41d8cd98f00b204e9800998ecf8427e"'
op|')'
newline|'\n'
name|'hash'
op|'='
name|'md5'
op|'('
op|')'
newline|'\n'
name|'hash'
op|'.'
name|'update'
op|'('
string|'"a"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'hash'
op|'.'
name|'digest'
op|'('
op|')'
op|'.'
name|'encode'
op|'('
string|"'hex'"
op|')'
op|','
nl|'\n'
string|'"0cc175b9c0f1b6a831c399e269772661"'
op|')'
newline|'\n'
nl|'\n'
comment|'# Instances of it should have a digest_size attribute'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'md5'
op|'('
op|')'
op|'.'
name|'digest_size'
op|','
number|'16'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_sha1
dedent|''
name|'def'
name|'test_sha1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        L{hashlib.sha1} returns an object which can be used to compute a SHA1\n        hash as defined by U{RFC 3174<http://tools.ietf.org/rfc/rfc3174.txt>}.\n        """'
newline|'\n'
DECL|function|format
name|'def'
name|'format'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
name|'s'
op|'.'
name|'split'
op|'('
op|')'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
comment|'# Test the result using values from section 7.3 of the RFC.'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'sha1'
op|'('
string|'"abc"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
name|'format'
op|'('
nl|'\n'
string|'"A9 99 3E 36 47 06 81 6A BA 3E 25 71 78 50 C2 6C 9C D0 D8 9D"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'sha1'
op|'('
string|'"abcdbcdecdefdefgefghfghighijhi"'
nl|'\n'
string|'"jkijkljklmklmnlmnomnopnopq"'
op|')'
op|'.'
name|'hexdigest'
op|'('
op|')'
op|','
nl|'\n'
name|'format'
op|'('
nl|'\n'
string|'"84 98 3E 44 1C 3B D2 6E BA AE 4A A1 F9 51 29 E5 E5 46 70 F1"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# It should have digest and update methods, too.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'sha1'
op|'('
string|'"abc"'
op|')'
op|'.'
name|'digest'
op|'('
op|')'
op|'.'
name|'encode'
op|'('
string|"'hex'"
op|')'
op|','
nl|'\n'
name|'format'
op|'('
nl|'\n'
string|'"A9 99 3E 36 47 06 81 6A BA 3E 25 71 78 50 C2 6C 9C D0 D8 9D"'
op|')'
op|')'
newline|'\n'
name|'hash'
op|'='
name|'sha1'
op|'('
op|')'
newline|'\n'
name|'hash'
op|'.'
name|'update'
op|'('
string|'"abc"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'hash'
op|'.'
name|'digest'
op|'('
op|')'
op|'.'
name|'encode'
op|'('
string|"'hex'"
op|')'
op|','
nl|'\n'
name|'format'
op|'('
nl|'\n'
string|'"A9 99 3E 36 47 06 81 6A BA 3E 25 71 78 50 C2 6C 9C D0 D8 9D"'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Instances of it should have a digest_size attribute.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'sha1'
op|'('
op|')'
op|'.'
name|'digest_size'
op|','
number|'20'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
