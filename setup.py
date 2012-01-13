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
name|'import'
name|'gettext'
newline|'\n'
name|'import'
name|'glob'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'setuptools'
name|'import'
name|'find_packages'
newline|'\n'
name|'from'
name|'setuptools'
op|'.'
name|'command'
op|'.'
name|'sdist'
name|'import'
name|'sdist'
newline|'\n'
nl|'\n'
comment|'# In order to run the i18n commands for compiling and'
nl|'\n'
comment|'# installing message catalogs, we use DistUtilsExtra.'
nl|'\n'
comment|"# Don't make this a hard requirement, but warn that"
nl|'\n'
comment|"# i18n commands won't be available if DistUtilsExtra is"
nl|'\n'
comment|'# not installed...'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'DistUtilsExtra'
op|'.'
name|'auto'
name|'import'
name|'setup'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'setuptools'
name|'import'
name|'setup'
newline|'\n'
name|'print'
string|'"Warning: DistUtilsExtra required to use i18n builders. "'
newline|'\n'
name|'print'
string|'"To build nova with support for message catalogs, you need "'
newline|'\n'
name|'print'
string|'"  https://launchpad.net/python-distutils-extra >= 2.18"'
newline|'\n'
nl|'\n'
dedent|''
name|'gettext'
op|'.'
name|'install'
op|'('
string|"'nova'"
op|','
name|'unicode'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'version'
newline|'\n'
nl|'\n'
DECL|variable|nova_cmdclass
name|'nova_cmdclass'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'sphinx'
op|'.'
name|'setup_command'
name|'import'
name|'BuildDoc'
newline|'\n'
nl|'\n'
DECL|class|local_BuildDoc
name|'class'
name|'local_BuildDoc'
op|'('
name|'BuildDoc'
op|')'
op|':'
newline|'\n'
DECL|member|run
indent|'        '
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'builder'
name|'in'
op|'['
string|"'html'"
op|','
string|"'man'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'builder'
op|'='
name|'builder'
newline|'\n'
name|'self'
op|'.'
name|'finalize_options'
op|'('
op|')'
newline|'\n'
name|'BuildDoc'
op|'.'
name|'run'
op|'('
name|'self'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'nova_cmdclass'
op|'['
string|"'build_sphinx'"
op|']'
op|'='
name|'local_BuildDoc'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_data_files
dedent|''
name|'def'
name|'find_data_files'
op|'('
name|'destdir'
op|','
name|'srcdir'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'package_data'
op|'='
op|'['
op|']'
newline|'\n'
name|'files'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'d'
name|'in'
name|'glob'
op|'.'
name|'glob'
op|'('
string|"'%s/*'"
op|'%'
op|'('
name|'srcdir'
op|','
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isdir'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'package_data'
op|'+='
name|'find_data_files'
op|'('
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'destdir'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'d'
op|')'
op|')'
op|','
name|'d'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'+='
op|'['
name|'d'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'package_data'
op|'+='
op|'['
op|'('
name|'destdir'
op|','
name|'files'
op|')'
op|']'
newline|'\n'
name|'return'
name|'package_data'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'setup'
op|'('
name|'name'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'version'
op|'.'
name|'canonical_version_string'
op|'('
op|')'
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|"'cloud computing fabric controller'"
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|"'OpenStack'"
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|"'nova@lists.launchpad.net'"
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|"'http://www.openstack.org/'"
op|','
nl|'\n'
DECL|variable|cmdclass
name|'cmdclass'
op|'='
name|'nova_cmdclass'
op|','
nl|'\n'
DECL|variable|packages
name|'packages'
op|'='
name|'find_packages'
op|'('
name|'exclude'
op|'='
op|'['
string|"'bin'"
op|','
string|"'smoketests'"
op|']'
op|')'
op|','
nl|'\n'
DECL|variable|include_package_data
name|'include_package_data'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|test_suite
name|'test_suite'
op|'='
string|"'nose.collector'"
op|','
nl|'\n'
DECL|variable|data_files
name|'data_files'
op|'='
name|'find_data_files'
op|'('
string|"'share/nova'"
op|','
string|"'tools'"
op|')'
op|','
nl|'\n'
DECL|variable|scripts
name|'scripts'
op|'='
op|'['
string|"'bin/nova-ajax-console-proxy'"
op|','
nl|'\n'
string|"'bin/nova-api'"
op|','
nl|'\n'
string|"'bin/nova-api-ec2'"
op|','
nl|'\n'
string|"'bin/nova-api-metadata'"
op|','
nl|'\n'
string|"'bin/nova-api-os-compute'"
op|','
nl|'\n'
string|"'bin/nova-api-os-volume'"
op|','
nl|'\n'
string|"'bin/nova-compute'"
op|','
nl|'\n'
string|"'bin/nova-console'"
op|','
nl|'\n'
string|"'bin/nova-dhcpbridge'"
op|','
nl|'\n'
string|"'bin/nova-direct-api'"
op|','
nl|'\n'
string|"'bin/nova-logspool'"
op|','
nl|'\n'
string|"'bin/nova-manage'"
op|','
nl|'\n'
string|"'bin/nova-network'"
op|','
nl|'\n'
string|"'bin/nova-objectstore'"
op|','
nl|'\n'
string|"'bin/nova-rootwrap'"
op|','
nl|'\n'
string|"'bin/nova-scheduler'"
op|','
nl|'\n'
string|"'bin/nova-spoolsentry'"
op|','
nl|'\n'
string|"'bin/stack'"
op|','
nl|'\n'
string|"'bin/nova-volume'"
op|','
nl|'\n'
string|"'bin/nova-vncproxy'"
op|','
nl|'\n'
string|"'tools/nova-debug'"
op|']'
op|','
nl|'\n'
DECL|variable|py_modules
name|'py_modules'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
endmarker|''
end_unit
