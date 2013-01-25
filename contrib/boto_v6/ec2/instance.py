begin_unit
string|"'''\nCreated on 2010/12/20\n\n@author: Nachi Ueno <ueno.nachi@lab.ntt.co.jp>\n'''"
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
name|'import'
name|'instance'
newline|'\n'
name|'from'
name|'boto'
name|'import'
name|'resultset'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ReservationV6
name|'class'
name|'ReservationV6'
op|'('
name|'instance'
op|'.'
name|'Reservation'
op|')'
op|':'
newline|'\n'
DECL|member|startElement
indent|'    '
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
string|"'instancesSet'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instances'
op|'='
name|'resultset'
op|'.'
name|'ResultSet'
op|'('
op|'['
op|'('
string|"'item'"
op|','
name|'InstanceV6'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instances'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'groupSet'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'groups'
op|'='
name|'resultset'
op|'.'
name|'ResultSet'
op|'('
op|'['
op|'('
string|"'item'"
op|','
name|'instance'
op|'.'
name|'Group'
op|')'
op|']'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'groups'
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
nl|'\n'
DECL|class|InstanceV6
dedent|''
dedent|''
dedent|''
name|'class'
name|'InstanceV6'
op|'('
name|'instance'
op|'.'
name|'Instance'
op|')'
op|':'
newline|'\n'
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
name|'instance'
op|'.'
name|'Instance'
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
name|'dns_name_v6'
op|'='
name|'None'
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
name|'instance'
op|'.'
name|'Instance'
op|'.'
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
newline|'\n'
name|'if'
name|'name'
op|'=='
string|"'dnsNameV6'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'dns_name_v6'
op|'='
name|'value'
newline|'\n'
nl|'\n'
DECL|member|_update
dedent|''
dedent|''
name|'def'
name|'_update'
op|'('
name|'self'
op|','
name|'updated'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'update'
op|'('
name|'updated'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'dns_name_v6'
op|'='
name|'updated'
op|'.'
name|'dns_name_v6'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
