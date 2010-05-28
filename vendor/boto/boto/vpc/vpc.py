begin_unit
comment|'# Copyright (c) 2009 Mitch Garnaat http://garnaat.org/'
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
string|'"""\nRepresents a Virtual Private Cloud.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'ec2object'
name|'import'
name|'EC2Object'
newline|'\n'
nl|'\n'
DECL|class|VPC
name|'class'
name|'VPC'
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
name|'id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'dhcp_options_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'state'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'cidr_block'
op|'='
name|'None'
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
string|"'VPC:%s'"
op|'%'
name|'self'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|endElement
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
string|"'vpcId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'dhcpOptionsId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'dhcp_options_id'
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
name|'elif'
name|'name'
op|'=='
string|"'cidrBlock'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'cidr_block'
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
name|'delete_vpc'
op|'('
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
