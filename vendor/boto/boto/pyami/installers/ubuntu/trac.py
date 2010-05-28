begin_unit
comment|'# Copyright (c) 2008 Chris Moyer http://coredumped.org'
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
name|'from'
name|'boto'
op|'.'
name|'pyami'
op|'.'
name|'installers'
op|'.'
name|'ubuntu'
op|'.'
name|'installer'
name|'import'
name|'Installer'
newline|'\n'
name|'import'
name|'boto'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
DECL|class|Trac
name|'class'
name|'Trac'
op|'('
name|'Installer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Install Trac and DAV-SVN\n    Sets up a Vhost pointing to [Trac]->home\n    Using the config parameter [Trac]->hostname\n    Sets up a trac environment for every directory found under [Trac]->data_dir\n\n    [Trac]\n    name = My Foo Server\n    hostname = trac.foo.com\n    home = /mnt/sites/trac\n    data_dir = /mnt/trac\n    svn_dir = /mnt/subversion\n    server_admin = root@foo.com\n    sdb_auth_domain = users\n    # Optional\n    SSLCertificateFile = /mnt/ssl/foo.crt\n    SSLCertificateKeyFile = /mnt/ssl/foo.key\n    SSLCertificateChainFile = /mnt/ssl/FooCA.crt\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|install
name|'def'
name|'install'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'run'
op|'('
string|"'apt-get -y install trac'"
op|','
name|'notify'
op|'='
name|'True'
op|','
name|'exit_on_error'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|"'apt-get -y install libapache2-svn'"
op|','
name|'notify'
op|'='
name|'True'
op|','
name|'exit_on_error'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"a2enmod ssl"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"a2enmod mod_python"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"a2enmod dav_svn"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"a2enmod rewrite"'
op|')'
newline|'\n'
comment|'# Make sure that boto.log is writable by everyone so that subversion post-commit hooks can '
nl|'\n'
comment|'# write to it.'
nl|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"touch /var/log/boto.log"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"chmod a+w /var/log/boto.log"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_vhost
dedent|''
name|'def'
name|'setup_vhost'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'domain'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"hostname"'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'domain'
op|':'
newline|'\n'
indent|'            '
name|'domain_info'
op|'='
name|'domain'
op|'.'
name|'split'
op|'('
string|"'.'"
op|')'
newline|'\n'
name|'cnf'
op|'='
name|'open'
op|'('
string|'"/etc/apache2/sites-available/%s"'
op|'%'
name|'domain_info'
op|'['
number|'0'
op|']'
op|','
string|'"w"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"NameVirtualHost *:80\\n"'
op|')'
newline|'\n'
name|'if'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"SSLCertificateFile"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"NameVirtualHost *:443\\n\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"<VirtualHost *:80>\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tServerAdmin %s\\n"'
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"server_admin"'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tServerName %s\\n"'
op|'%'
name|'domain'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tRewriteEngine On\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tRewriteRule ^(.*)$ https://%s$1\\n"'
op|'%'
name|'domain'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"</VirtualHost>\\n\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"<VirtualHost *:443>\\n"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"<VirtualHost *:80>\\n"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tServerAdmin %s\\n"'
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"server_admin"'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tServerName %s\\n"'
op|'%'
name|'domain'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tDocumentRoot %s\\n"'
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"home"'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t<Directory %s>\\n"'
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"home"'
op|')'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tOptions FollowSymLinks Indexes MultiViews\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tAllowOverride All\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tOrder allow,deny\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tallow from all\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t</Directory>\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t<Location />\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tAuthType Basic\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tAuthName \\"%s\\"\\n"'
op|'%'
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"name"'
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tRequire valid-user\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tAuthUserFile /mnt/apache/passwd/passwords\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t</Location>\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'data_dir'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"data_dir"'
op|')'
newline|'\n'
name|'for'
name|'env'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'data_dir'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
op|'('
name|'env'
op|'['
number|'0'
op|']'
op|'!='
string|'"."'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t<Location /trac/%s>\\n"'
op|'%'
name|'env'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tSetHandler mod_python\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tPythonInterpreter main_interpreter\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tPythonHandler trac.web.modpython_frontend\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tPythonOption TracEnv %s/%s\\n"'
op|'%'
op|'('
name|'data_dir'
op|','
name|'env'
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tPythonOption TracUriRoot /trac/%s\\n"'
op|'%'
name|'env'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t</Location>\\n"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'svn_dir'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"svn_dir"'
op|')'
newline|'\n'
name|'for'
name|'env'
name|'in'
name|'os'
op|'.'
name|'listdir'
op|'('
name|'svn_dir'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
op|'('
name|'env'
op|'['
number|'0'
op|']'
op|'!='
string|'"."'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t<Location /svn/%s>\\n"'
op|'%'
name|'env'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tDAV svn\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t\\tSVNPath %s/%s\\n"'
op|'%'
op|'('
name|'svn_dir'
op|','
name|'env'
op|')'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\t</Location>\\n"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tErrorLog /var/log/apache2/error.log\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tLogLevel warn\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tCustomLog /var/log/apache2/access.log combined\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tServerSignature On\\n"'
op|')'
newline|'\n'
name|'SSLCertificateFile'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"SSLCertificateFile"'
op|')'
newline|'\n'
name|'if'
name|'SSLCertificateFile'
op|':'
newline|'\n'
indent|'                '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tSSLEngine On\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tSSLCertificateFile %s\\n"'
op|'%'
name|'SSLCertificateFile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'SSLCertificateKeyFile'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"SSLCertificateKeyFile"'
op|')'
newline|'\n'
name|'if'
name|'SSLCertificateKeyFile'
op|':'
newline|'\n'
indent|'                '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tSSLCertificateKeyFile %s\\n"'
op|'%'
name|'SSLCertificateKeyFile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'SSLCertificateChainFile'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|'"Trac"'
op|','
string|'"SSLCertificateChainFile"'
op|')'
newline|'\n'
name|'if'
name|'SSLCertificateChainFile'
op|':'
newline|'\n'
indent|'                '
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"\\tSSLCertificateChainFile %s\\n"'
op|'%'
name|'SSLCertificateChainFile'
op|')'
newline|'\n'
dedent|''
name|'cnf'
op|'.'
name|'write'
op|'('
string|'"</VirtualHost>\\n"'
op|')'
newline|'\n'
name|'cnf'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"a2ensite %s"'
op|'%'
name|'domain_info'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"/etc/init.d/apache2 force-reload"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|main
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
name|'install'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'setup_vhost'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
