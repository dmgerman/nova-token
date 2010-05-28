begin_unit
comment|'# Copyright (c) 2006-2009 Mitch Garnaat http://garnaat.org/'
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
string|'"""\nThis installer will install mysql-server on an Ubuntu machine.\nIn addition to the normal installation done by apt-get, it will\nalso configure the new MySQL server to store it\'s data files in\na different location.  By default, this is /mnt but that can be\nconfigured in the [MySQL] section of the boto config file passed\nto the instance.\n"""'
newline|'\n'
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
name|'ShellCommand'
newline|'\n'
name|'from'
name|'ConfigParser'
name|'import'
name|'SafeConfigParser'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'ConfigSection'
op|'='
string|'"""\n[MySQL]\nroot_password = <will be used as MySQL root password, default none>\ndata_dir = <new data dir for MySQL, default is /mnt>\n"""'
newline|'\n'
nl|'\n'
DECL|class|MySQL
name|'class'
name|'MySQL'
op|'('
name|'Installer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|install
indent|'    '
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
string|"'apt-get update'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|"'apt-get -y install mysql-server'"
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
nl|'\n'
comment|'#    def set_root_password(self, password=None):'
nl|'\n'
comment|'#        if not password:'
nl|'\n'
comment|"#            password = boto.config.get('MySQL', 'root_password')"
nl|'\n'
comment|'#        if password:'
nl|'\n'
comment|"#            self.run('mysqladmin -u root password %s' % password)"
nl|'\n'
comment|'#        return password'
nl|'\n'
nl|'\n'
DECL|member|change_data_dir
dedent|''
name|'def'
name|'change_data_dir'
op|'('
name|'self'
op|','
name|'password'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data_dir'
op|'='
name|'boto'
op|'.'
name|'config'
op|'.'
name|'get'
op|'('
string|"'MySQL'"
op|','
string|"'data_dir'"
op|','
string|"'/mnt'"
op|')'
newline|'\n'
name|'fresh_install'
op|'='
name|'False'
op|';'
newline|'\n'
name|'is_mysql_running_command'
op|'='
name|'ShellCommand'
op|'('
string|"'mysqladmin ping'"
op|')'
comment|'# exit status 0 if mysql is running'
newline|'\n'
name|'is_mysql_running_command'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
name|'if'
name|'is_mysql_running_command'
op|'.'
name|'getStatus'
op|'('
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
comment|"# mysql is running. This is the state apt-get will leave it in. If it isn't running, "
nl|'\n'
comment|"# that means mysql was already installed on the AMI and there's no need to stop it,"
nl|'\n'
comment|'# saving 40 seconds on instance startup.'
nl|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'10'
op|')'
comment|'#trying to stop mysql immediately after installing it fails'
newline|'\n'
comment|'# We need to wait until mysql creates the root account before we kill it'
nl|'\n'
comment|'# or bad things will happen'
nl|'\n'
name|'i'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'run'
op|'('
string|'"echo \'quit\' | mysql -u root"'
op|')'
op|'!='
number|'0'
name|'and'
name|'i'
op|'<'
number|'5'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'run'
op|'('
string|"'/etc/init.d/mysql stop'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run'
op|'('
string|'"pkill -9 mysql"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'mysql_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'data_dir'
op|','
string|"'mysql'"
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
name|'mysql_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'run'
op|'('
string|"'mkdir %s'"
op|'%'
name|'mysql_path'
op|')'
newline|'\n'
name|'fresh_install'
op|'='
name|'True'
op|';'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'run'
op|'('
string|"'chown -R mysql:mysql %s'"
op|'%'
name|'mysql_path'
op|')'
newline|'\n'
name|'fp'
op|'='
name|'open'
op|'('
string|"'/etc/mysql/conf.d/use_mnt.cnf'"
op|','
string|"'w'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'# created by pyami\\n'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'# use the %s volume for data\\n'"
op|'%'
name|'data_dir'
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'[mysqld]\\n'"
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'datadir = %s\\n'"
op|'%'
name|'mysql_path'
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'write'
op|'('
string|"'log_bin = %s\\n'"
op|'%'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'mysql_path'
op|','
string|"'mysql-bin.log'"
op|')'
op|')'
newline|'\n'
name|'fp'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'if'
name|'fresh_install'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'run'
op|'('
string|"'cp -pr /var/lib/mysql/* %s/'"
op|'%'
name|'mysql_path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'start'
op|'('
string|"'mysql'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'#get the password ubuntu expects to use:'
nl|'\n'
indent|'            '
name|'config_parser'
op|'='
name|'SafeConfigParser'
op|'('
op|')'
newline|'\n'
name|'config_parser'
op|'.'
name|'read'
op|'('
string|"'/etc/mysql/debian.cnf'"
op|')'
newline|'\n'
name|'password'
op|'='
name|'config_parser'
op|'.'
name|'get'
op|'('
string|"'client'"
op|','
string|"'password'"
op|')'
newline|'\n'
comment|'# start the mysql deamon, then mysql with the required grant statement piped into it:'
nl|'\n'
name|'self'
op|'.'
name|'start'
op|'('
string|"'mysql'"
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'10'
op|')'
comment|'#time for mysql to start'
newline|'\n'
name|'grant_command'
op|'='
string|'"echo \\"GRANT ALL PRIVILEGES ON *.* TO \'debian-sys-maint\'@\'localhost\' IDENTIFIED BY \'%s\' WITH GRANT OPTION;\\" | mysql"'
op|'%'
name|'password'
newline|'\n'
name|'while'
name|'self'
op|'.'
name|'run'
op|'('
name|'grant_command'
op|')'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'5'
op|')'
newline|'\n'
comment|'# leave mysqld running'
nl|'\n'
nl|'\n'
DECL|member|main
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
name|'install'
op|'('
op|')'
newline|'\n'
comment|"# change_data_dir runs 'mysql -u root' which assumes there is no mysql password, i"
nl|'\n'
comment|'# and changing that is too ugly to be worth it:'
nl|'\n'
comment|'#self.set_root_password()'
nl|'\n'
name|'self'
op|'.'
name|'change_data_dir'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
