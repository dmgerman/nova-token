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
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,'
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
string|'"""\nRepresents an EC2 Spot Instance Datafeed Subscription\n"""'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'ec2object'
name|'import'
name|'EC2Object'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'spotinstancerequest'
name|'import'
name|'SpotInstanceStateFault'
newline|'\n'
nl|'\n'
DECL|class|SpotDatafeedSubscription
name|'class'
name|'SpotDatafeedSubscription'
op|'('
name|'EC2Object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|'='
name|'None'
op|','
name|'owner_id'
op|'='
name|'None'
op|','
nl|'\n'
name|'bucket'
op|'='
name|'None'
op|','
name|'prefix'
op|'='
name|'None'
op|','
name|'state'
op|'='
name|'None'
op|','
name|'fault'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'EC2Object'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'owner_id'
op|'='
name|'owner_id'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'='
name|'bucket'
newline|'\n'
name|'self'
op|'.'
name|'prefix'
op|'='
name|'prefix'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'state'
newline|'\n'
name|'self'
op|'.'
name|'fault'
op|'='
name|'fault'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'SpotDatafeedSubscription:%s'"
op|'%'
name|'self'
op|'.'
name|'bucket'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'fault'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'fault'
op|'='
name|'SpotInstanceStateFault'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'fault'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'ownerId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'owner_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'bucket'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'bucket'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'prefix'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'prefix'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'state'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'delete_spot_datafeed_subscription'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
