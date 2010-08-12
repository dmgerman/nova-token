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
name|'os'
op|'.'
name|'path'
newline|'\n'
name|'import'
name|'time'
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
name|'process'
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
name|'auth'
name|'import'
name|'manager'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
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
nl|'\n'
comment|'# This should probably move somewhere else, like e.g. a download_as'
nl|'\n'
comment|'# method on User objects and at the same time get rewritten to use'
nl|'\n'
comment|'# twisted web client.'
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
name|'cmd'
op|'='
op|'['
string|"'/usr/bin/curl'"
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
indent|'        '
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
name|'return'
name|'process'
op|'.'
name|'SharedPool'
op|'('
op|')'
op|'.'
name|'execute'
op|'('
name|'executable'
op|'='
name|'cmd'
op|'['
number|'0'
op|']'
op|','
name|'args'
op|'='
name|'cmd'
op|'['
number|'1'
op|':'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|_fetch_local_image
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
string|"'%s/image'"
op|'%'
name|'image'
op|')'
newline|'\n'
name|'return'
name|'process'
op|'.'
name|'simple_execute'
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
DECL|function|_image_path
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
