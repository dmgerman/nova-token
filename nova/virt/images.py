begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""\nHandling of VM disk images.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'urllib2'
newline|'\n'
name|'import'
name|'urlparse'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'manager'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'signer'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objectstore'
name|'import'
name|'image'
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
name|'flags'
op|'.'
name|'DEFINE_bool'
op|'('
string|"'use_s3'"
op|','
name|'True'
op|','
nl|'\n'
string|"'whether to get images from s3 or use local copy'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch
name|'def'
name|'fetch'
op|'('
name|'image'
op|','
name|'path'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'use_s3'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'_fetch_s3_image'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'='
name|'_fetch_local_image'
newline|'\n'
dedent|''
name|'return'
name|'f'
op|'('
name|'image'
op|','
name|'path'
op|','
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fetch_image_no_curl
dedent|''
name|'def'
name|'_fetch_image_no_curl'
op|'('
name|'url'
op|','
name|'path'
op|','
name|'headers'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'request'
op|'='
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'url'
op|')'
newline|'\n'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'add_header'
op|'('
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|function|urlretrieve
dedent|''
name|'def'
name|'urlretrieve'
op|'('
name|'urlfile'
op|','
name|'fpath'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'chunk'
op|'='
number|'1'
op|'*'
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'f'
op|'='
name|'open'
op|'('
name|'fpath'
op|','
string|'"wb"'
op|')'
newline|'\n'
name|'while'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'urlfile'
op|'.'
name|'read'
op|'('
name|'chunk'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'f'
op|'.'
name|'write'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'urlopened'
op|'='
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'request'
op|')'
newline|'\n'
name|'urlretrieve'
op|'('
name|'urlopened'
op|','
name|'path'
op|')'
newline|'\n'
name|'logging'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Finished retreving %s -- placed in %s"'
op|')'
op|','
name|'url'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fetch_s3_image
dedent|''
name|'def'
name|'_fetch_s3_image'
op|'('
name|'image'
op|','
name|'path'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'url'
op|'='
name|'image_url'
op|'('
name|'image'
op|')'
newline|'\n'
comment|'# This should probably move somewhere else, like e.g. a download_as'
nl|'\n'
comment|'# method on User objects and at the same time get rewritten to use'
nl|'\n'
comment|'# a web client.'
nl|'\n'
name|'headers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'headers'
op|'['
string|"'Date'"
op|']'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|'"%a, %d %b %Y %H:%M:%S GMT"'
op|','
name|'time'
op|'.'
name|'gmtime'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
op|'('
name|'_'
op|','
name|'_'
op|','
name|'url_path'
op|','
name|'_'
op|','
name|'_'
op|','
name|'_'
op|')'
op|'='
name|'urlparse'
op|'.'
name|'urlparse'
op|'('
name|'url'
op|')'
newline|'\n'
name|'access'
op|'='
name|'manager'
op|'.'
name|'AuthManager'
op|'('
op|')'
op|'.'
name|'get_access_key'
op|'('
name|'user'
op|','
name|'project'
op|')'
newline|'\n'
name|'signature'
op|'='
name|'signer'
op|'.'
name|'Signer'
op|'('
name|'user'
op|'.'
name|'secret'
op|'.'
name|'encode'
op|'('
op|')'
op|')'
op|'.'
name|'s3_authorization'
op|'('
name|'headers'
op|','
nl|'\n'
string|"'GET'"
op|','
nl|'\n'
name|'url_path'
op|')'
newline|'\n'
name|'headers'
op|'['
string|"'Authorization'"
op|']'
op|'='
string|"'AWS %s:%s'"
op|'%'
op|'('
name|'access'
op|','
name|'signature'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'.'
name|'startswith'
op|'('
string|"'win'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_fetch_image_no_curl'
op|'('
name|'url'
op|','
name|'path'
op|','
name|'headers'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'cmd'
op|'='
op|'['
string|"'/usr/bin/curl'"
op|','
string|"'--fail'"
op|','
string|"'--silent'"
op|','
name|'url'
op|']'
newline|'\n'
name|'for'
op|'('
name|'k'
op|','
name|'v'
op|')'
name|'in'
name|'headers'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'+='
op|'['
string|"'-H'"
op|','
string|"'%s: %s'"
op|'%'
op|'('
name|'k'
op|','
name|'v'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'+='
op|'['
string|"'-o'"
op|','
name|'path'
op|']'
newline|'\n'
name|'cmd_out'
op|'='
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
name|'cmd_out'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fetch_local_image
dedent|''
dedent|''
name|'def'
name|'_fetch_local_image'
op|'('
name|'image'
op|','
name|'path'
op|','
name|'user'
op|','
name|'project'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'source'
op|'='
name|'_image_path'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'image'
op|','
string|"'image'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'.'
name|'startswith'
op|'('
string|"'win'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'shutil'
op|'.'
name|'copy'
op|'('
name|'source'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cp %s %s'"
op|'%'
op|'('
name|'source'
op|','
name|'path'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_image_path
dedent|''
dedent|''
name|'def'
name|'_image_path'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'FLAGS'
op|'.'
name|'images_path'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_url
dedent|''
name|'def'
name|'image_url'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|'"http://%s:%s/_images/%s/image"'
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'s3_host'
op|','
name|'FLAGS'
op|'.'
name|'s3_port'
op|','
nl|'\n'
name|'image'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
