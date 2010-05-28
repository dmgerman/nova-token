begin_unit
name|'from'
name|'distutils'
op|'.'
name|'core'
name|'import'
name|'setup'
newline|'\n'
name|'from'
name|'distutils'
op|'.'
name|'extension'
name|'import'
name|'Extension'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'Pyrex'
op|'.'
name|'Distutils'
name|'import'
name|'build_ext'
newline|'\n'
comment|'# pyrex is available'
nl|'\n'
name|'setup'
op|'('
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'cfsupport'"
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
string|"'0.4'"
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|'"Enough CoreFoundation wrappers to deal with CFRunLoop"'
op|','
nl|'\n'
DECL|variable|long_description
name|'long_description'
op|'='
string|'"Pythonic wrappers for pieces of Apple\'s CoreFoundation API\'s that are not otherwise wrapped by MacPython.\\nPrimarily useful for dealing with CFRunLoop."'
op|','
nl|'\n'
DECL|variable|maintainer
name|'maintainer'
op|'='
string|"'Bob Ippolito'"
op|','
nl|'\n'
DECL|variable|maintainer_email
name|'maintainer_email'
op|'='
string|"'bob@redivi.com'"
op|','
nl|'\n'
DECL|variable|license
name|'license'
op|'='
string|"'Python'"
op|','
nl|'\n'
DECL|variable|platforms
name|'platforms'
op|'='
op|'['
string|"'Mac OSX'"
op|']'
op|','
nl|'\n'
DECL|variable|keywords
name|'keywords'
op|'='
op|'['
string|"'CoreFoundation'"
op|','
string|"'CFRunLoop'"
op|','
string|"'Cocoa'"
op|','
string|"'GUI'"
op|']'
op|','
nl|'\n'
DECL|variable|ext_modules
name|'ext_modules'
op|'='
op|'['
nl|'\n'
name|'Extension'
op|'('
nl|'\n'
string|"'cfsupport'"
op|','
nl|'\n'
op|'['
string|"'cfsupport.pyx'"
op|']'
op|','
nl|'\n'
DECL|variable|extra_link_args
name|'extra_link_args'
op|'='
op|'['
nl|'\n'
string|"'-framework'"
op|','
string|"'CoreFoundation'"
op|','
nl|'\n'
string|"'-framework'"
op|','
string|"'CoreServices'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|cmdclass
name|'cmdclass'
op|'='
op|'{'
string|"'build_ext'"
op|':'
name|'build_ext'
op|'}'
nl|'\n'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
comment|'# pyrex is not available, use existing .c'
nl|'\n'
indent|'    '
name|'setup'
op|'('
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|"'cfsupport'"
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
string|"'0.4'"
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|'"Enough CoreFoundation wrappers to deal with CFRunLoop"'
op|','
nl|'\n'
DECL|variable|long_description
name|'long_description'
op|'='
string|'"Pythonic wrappers for pieces of Apple\'s CoreFoundation API\'s that are not otherwise wrapped by MacPython.\\nPrimarily useful for dealing with CFRunLoop."'
op|','
nl|'\n'
DECL|variable|maintainer
name|'maintainer'
op|'='
string|"'Bob Ippolito'"
op|','
nl|'\n'
DECL|variable|maintainer_email
name|'maintainer_email'
op|'='
string|"'bob@redivi.com'"
op|','
nl|'\n'
DECL|variable|license
name|'license'
op|'='
string|"'Python'"
op|','
nl|'\n'
DECL|variable|platforms
name|'platforms'
op|'='
op|'['
string|"'Mac OSX'"
op|']'
op|','
nl|'\n'
DECL|variable|keywords
name|'keywords'
op|'='
op|'['
string|"'CoreFoundation'"
op|','
string|"'CFRunLoop'"
op|','
string|"'Cocoa'"
op|','
string|"'GUI'"
op|']'
op|','
nl|'\n'
DECL|variable|ext_modules
name|'ext_modules'
op|'='
op|'['
nl|'\n'
name|'Extension'
op|'('
nl|'\n'
string|"'cfsupport'"
op|','
nl|'\n'
op|'['
string|"'cfsupport.c'"
op|']'
op|','
nl|'\n'
DECL|variable|extra_link_args
name|'extra_link_args'
op|'='
op|'['
nl|'\n'
string|"'-framework'"
op|','
string|"'CoreFoundation'"
op|','
nl|'\n'
string|"'-framework'"
op|','
string|"'CoreServices'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
