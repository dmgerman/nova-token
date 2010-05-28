begin_unit
comment|'# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/'
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
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'utils'
name|'import'
name|'get_instance_metadata'
op|','
name|'get_instance_userdata'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'pyami'
op|'.'
name|'config'
name|'import'
name|'Config'
op|','
name|'BotoConfigPath'
newline|'\n'
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
DECL|class|Bootstrap
name|'class'
name|'Bootstrap'
op|'('
name|'ScriptBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The Bootstrap class is instantiated and run as part of the PyAMI\n    instance initialization process.  The methods in this class will\n    be run from the rc.local script of the instance and will be run\n    as the root user.\n\n    The main purpose of this class is to make sure the boto distribution\n    on the instance is the one required.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'working_dir'
op|'='
string|"'/mnt/pyami'"
newline|'\n'
name|'self'
op|'.'
name|'write_metadata'
op|'('
op|')'
newline|'\n'
name|'ScriptBase'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|write_metadata
dedent|''
name|'def'
name|'write_metadata'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fp'
op|'='
name|'open'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'expanduser'
op|'('
name|'BotoConfigPath'
op|')'
op|','
string|"'w'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'[Instance]\\n'"
op|')'
newline|'\n'
name|'inst_data'
op|'='
name|'get_instance_metadata'
op|'('
op|')'
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'inst_data'
op|':'
newline|'\n'
indent|'            '
name|'fp'
op|'.'
name|'write'
op|'('
string|"'%s = %s\\n'"
op|'%'
op|'('
name|'key'
op|','
name|'inst_data'
op|'['
name|'key'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'user_data'
op|'='
name|'get_instance_userdata'
op|'('
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'\\n%s\\n'"
op|'%'
name|'user_data'
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'[Pyami]\\n'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'working_dir = %s\\n'"
op|'%'
name|'self'
op|'.'
name|'working_dir'
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
comment|'# This file has the AWS credentials, should we lock it down?'
nl|'\n'
comment|'# os.chmod(BotoConfigPath, stat.S_IREAD | stat.S_IWRITE)'
nl|'\n'
comment|'# now that we have written the file, read it into a pyami Config object'
nl|'\n'
name|'boto'
op|'.'
name|'config'
op|'='
name|'Config'
op|'('
op|')'
newline|'\n'
name|'boto'
op|'.'
name|'init_logging'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_working_dir
dedent|''
name|'def'
name|'create_working_dir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'boto'
op|'.'
name|'log'
op|'.'
name|'info'
op|'('
string|"'Working directory: %s'"
op|'%'
name|'self'
op|'.'
name|'working_dir'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'working_dir'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'mkdir'
op|'('
name|'self'
op|'.'
name|'working_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|member|load_boto
dedent|''
dedent|''
name|'def'
name|'load_boto'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'update'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Boto'"
op|','
string|"'boto_update'"
op|','
string|"'svn:HEAD'"
op|')'
newline|'\n'
name|'if'
name|'update'
op|'.'
name|'startswith'
op|'('
string|"'svn'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'update'
op|'.'
name|'find'
op|'('
string|"':'"
op|')'
op|'>='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'method'
op|','
name|'version'
op|'='
name|'update'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
newline|'\n'
name|'version'
op|'='
string|"'-r%s'"
op|'%'
name|'version'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'version'
op|'='
string|"'-rHEAD'"
newline|'\n'
dedent|''
name|'location'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Boto'"
op|','
string|"'boto_location'"
op|','
string|"'/usr/local/boto'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|"'svn update %s %s'"
op|'%'
op|'('
name|'version'
op|','
name|'location'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# first remove the symlink needed when running from subversion'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'run'
op|'('
string|"'rm /usr/local/lib/python2.5/site-packages/boto'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|"'easy_install %s'"
op|'%'
name|'update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fetch_s3_file
dedent|''
dedent|''
name|'def'
name|'fetch_s3_file'
op|'('
name|'self'
op|','
name|'s3_file'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'s3_file'
op|'.'
name|'startswith'
op|'('
string|"'s3:'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'bucket_name'
op|','
name|'key_name'
op|'='
name|'s3_file'
op|'['
name|'len'
op|'('
string|"'s3:'"
op|')'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'c'
op|'='
name|'boto'
op|'.'
name|'connect_s3'
op|'('
op|')'
newline|'\n'
name|'bucket'
op|'='
name|'c'
op|'.'
name|'get_bucket'
op|'('
name|'bucket_name'
op|')'
newline|'\n'
name|'key'
op|'='
name|'bucket'
op|'.'
name|'get_key'
op|'('
name|'key_name'
op|')'
newline|'\n'
name|'boto'
op|'.'
name|'log'
op|'.'
name|'info'
op|'('
string|"'Fetching %s/%s'"
op|'%'
op|'('
name|'bucket'
op|'.'
name|'name'
op|','
name|'key'
op|'.'
name|'name'
op|')'
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'working_dir'
op|','
name|'key'
op|'.'
name|'name'
op|')'
newline|'\n'
name|'key'
op|'.'
name|'get_contents_to_filename'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'boto'
op|'.'
name|'log'
op|'.'
name|'exception'
op|'('
string|"'Problem Retrieving file: %s'"
op|'%'
name|'s3_file'
op|')'
newline|'\n'
name|'path'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|load_packages
dedent|''
name|'def'
name|'load_packages'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'package_str'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'Pyami'"
op|','
string|"'packages'"
op|')'
newline|'\n'
name|'if'
name|'package_str'
op|':'
newline|'\n'
indent|'            '
name|'packages'
op|'='
name|'package_str'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
newline|'\n'
name|'for'
name|'package'
name|'in'
name|'packages'
op|':'
newline|'\n'
indent|'                '
name|'package'
op|'='
name|'package'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'package'
op|'.'
name|'startswith'
op|'('
string|"'s3:'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'package'
op|'='
name|'self'
op|'.'
name|'fetch_s3_file'
op|'('
name|'package'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'package'
op|':'
newline|'\n'
comment|'# if the "package" is really a .py file, it doesn\'t have to'
nl|'\n'
comment|'# be installed, just being in the working dir is enough'
nl|'\n'
indent|'                    '
name|'if'
name|'not'
name|'package'
op|'.'
name|'endswith'
op|'('
string|"'.py'"
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'self'
op|'.'
name|'run'
op|'('
string|"'easy_install -Z %s'"
op|'%'
name|'package'
op|','
name|'exit_on_error'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|main
dedent|''
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'create_working_dir'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'load_boto'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'load_packages'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'notify'
op|'('
string|"'Bootstrap Completed for %s'"
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get_instance'
op|'('
string|"'instance-id'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
comment|'# because bootstrap starts before any logging configuration can be loaded from'
nl|'\n'
comment|'# the boto config files, we will manually enable logging to /var/log/boto.log'
nl|'\n'
indent|'    '
name|'boto'
op|'.'
name|'set_file_logger'
op|'('
string|"'bootstrap'"
op|','
string|"'/var/log/boto.log'"
op|')'
newline|'\n'
DECL|variable|bs
name|'bs'
op|'='
name|'Bootstrap'
op|'('
op|')'
newline|'\n'
name|'bs'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
