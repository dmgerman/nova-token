begin_unit
comment|'#!/usr/bin/python'
nl|'\n'
nl|'\n'
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
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'setuptools'
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
name|'distutils'
op|'.'
name|'core'
name|'import'
name|'setup'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'boto'
name|'import'
name|'Version'
newline|'\n'
nl|'\n'
name|'setup'
op|'('
name|'name'
op|'='
string|'"boto"'
op|','
nl|'\n'
DECL|variable|version
name|'version'
op|'='
name|'Version'
op|','
nl|'\n'
DECL|variable|description
name|'description'
op|'='
string|'"Amazon Web Services Library"'
op|','
nl|'\n'
DECL|variable|long_description
name|'long_description'
op|'='
string|'"Python interface to Amazon\'s Web Services."'
op|','
nl|'\n'
DECL|variable|author
name|'author'
op|'='
string|'"Mitch Garnaat"'
op|','
nl|'\n'
DECL|variable|author_email
name|'author_email'
op|'='
string|'"mitch@garnaat.com"'
op|','
nl|'\n'
DECL|variable|scripts
name|'scripts'
op|'='
op|'['
string|'"bin/sdbadmin"'
op|','
string|'"bin/elbadmin"'
op|','
string|'"bin/cfadmin"'
op|','
nl|'\n'
string|'"bin/s3put"'
op|','
string|'"bin/fetch_file"'
op|','
string|'"bin/launch_instance"'
op|','
nl|'\n'
string|'"bin/list_instances"'
op|','
string|'"bin/taskadmin"'
op|','
string|'"bin/kill_instance"'
op|','
nl|'\n'
string|'"bin/bundle_image"'
op|','
string|'"bin/pyami_sendmail"'
op|']'
op|','
nl|'\n'
DECL|variable|url
name|'url'
op|'='
string|'"http://code.google.com/p/boto/"'
op|','
nl|'\n'
DECL|variable|packages
name|'packages'
op|'='
op|'['
string|"'boto'"
op|','
string|"'boto.sqs'"
op|','
string|"'boto.s3'"
op|','
nl|'\n'
string|"'boto.ec2'"
op|','
string|"'boto.ec2.cloudwatch'"
op|','
string|"'boto.ec2.autoscale'"
op|','
string|"'boto.ec2.elb'"
op|','
nl|'\n'
string|"'boto.sdb'"
op|','
string|"'boto.sdb.persist'"
op|','
string|"'boto.sdb.db'"
op|','
string|"'boto.sdb.db.manager'"
op|','
nl|'\n'
string|"'boto.mturk'"
op|','
string|"'boto.pyami'"
op|','
string|"'boto.mashups'"
op|','
string|"'boto.contrib'"
op|','
string|"'boto.manage'"
op|','
nl|'\n'
string|"'boto.services'"
op|','
string|"'boto.tests'"
op|','
string|"'boto.cloudfront'"
op|','
string|"'boto.rds'"
op|','
string|"'boto.vpc'"
op|','
nl|'\n'
string|"'boto.fps'"
op|','
string|"'boto.emr'"
op|']'
op|','
nl|'\n'
DECL|variable|license
name|'license'
op|'='
string|"'MIT'"
op|','
nl|'\n'
DECL|variable|platforms
name|'platforms'
op|'='
string|"'Posix; MacOS X; Windows'"
op|','
nl|'\n'
DECL|variable|classifiers
name|'classifiers'
op|'='
op|'['
string|"'Development Status :: 3 - Alpha'"
op|','
nl|'\n'
string|"'Intended Audience :: Developers'"
op|','
nl|'\n'
string|"'License :: OSI Approved :: MIT License'"
op|','
nl|'\n'
string|"'Operating System :: OS Independent'"
op|','
nl|'\n'
string|"'Topic :: Internet'"
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|')'
newline|'\n'
endmarker|''
end_unit
