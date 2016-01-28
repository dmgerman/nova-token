begin_unit
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
string|'"""\nThis provides a sphinx extension able to list the implemented versioned\nnotifications into the developer documentation.\n\nIt is used via a single directive in the .rst file\n\n  .. versioned_notifications::\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'sphinx'
op|'.'
name|'util'
op|'.'
name|'compat'
name|'import'
name|'Directive'
newline|'\n'
name|'from'
name|'docutils'
name|'import'
name|'nodes'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'notification'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|full_name
name|'def'
name|'full_name'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'cls'
op|'.'
name|'__module__'
op|'+'
string|"'.'"
op|'+'
name|'cls'
op|'.'
name|'__name__'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionedNotificationDirective
dedent|''
name|'class'
name|'VersionedNotificationDirective'
op|'('
name|'Directive'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|LINK_PREFIX
indent|'    '
name|'LINK_PREFIX'
op|'='
string|"'https://git.openstack.org/cgit/openstack/nova/plain/'"
newline|'\n'
DECL|variable|SAMPLE_ROOT
name|'SAMPLE_ROOT'
op|'='
string|"'doc/notification_samples/'"
newline|'\n'
nl|'\n'
DECL|member|run
name|'def'
name|'run'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'='
name|'self'
op|'.'
name|'_collect_notifications'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_build_markup'
op|'('
name|'notifications'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_collect_notifications
dedent|''
name|'def'
name|'_collect_notifications'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'notifications'
op|'='
op|'['
op|']'
newline|'\n'
name|'ovos'
op|'='
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'obj_classes'
op|'('
op|')'
newline|'\n'
name|'for'
name|'name'
op|','
name|'cls'
name|'in'
name|'ovos'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'cls'
op|'='
name|'cls'
op|'['
number|'0'
op|']'
newline|'\n'
name|'if'
op|'('
name|'issubclass'
op|'('
name|'cls'
op|','
name|'notification'
op|'.'
name|'NotificationBase'
op|')'
name|'and'
nl|'\n'
name|'cls'
op|'!='
name|'notification'
op|'.'
name|'NotificationBase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'                '
name|'payload_name'
op|'='
name|'cls'
op|'.'
name|'fields'
op|'['
string|"'payload'"
op|']'
op|'.'
name|'objname'
newline|'\n'
name|'payload_cls'
op|'='
name|'ovos'
op|'['
name|'payload_name'
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'notifications'
op|'.'
name|'append'
op|'('
op|'('
name|'full_name'
op|'('
name|'cls'
op|')'
op|','
name|'full_name'
op|'('
name|'payload_cls'
op|')'
op|','
nl|'\n'
name|'cls'
op|'.'
name|'sample'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'notifications'
newline|'\n'
nl|'\n'
DECL|member|_build_markup
dedent|''
name|'def'
name|'_build_markup'
op|'('
name|'self'
op|','
name|'notifications'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'content'
op|'='
op|'['
op|']'
newline|'\n'
name|'cols'
op|'='
op|'['
string|"'Notification class'"
op|','
string|"'Payload class'"
op|','
string|"'Sample file link'"
op|']'
newline|'\n'
name|'table'
op|'='
name|'nodes'
op|'.'
name|'table'
op|'('
op|')'
newline|'\n'
name|'content'
op|'.'
name|'append'
op|'('
name|'table'
op|')'
newline|'\n'
name|'group'
op|'='
name|'nodes'
op|'.'
name|'tgroup'
op|'('
name|'cols'
op|'='
name|'len'
op|'('
name|'cols'
op|')'
op|')'
newline|'\n'
name|'table'
op|'.'
name|'append'
op|'('
name|'group'
op|')'
newline|'\n'
nl|'\n'
name|'head'
op|'='
name|'nodes'
op|'.'
name|'thead'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'append'
op|'('
name|'head'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'cols'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'group'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'colspec'
op|'('
name|'colwidth'
op|'='
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'body'
op|'='
name|'nodes'
op|'.'
name|'tbody'
op|'('
op|')'
newline|'\n'
name|'group'
op|'.'
name|'append'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
comment|'# fill the table header'
nl|'\n'
name|'row'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
name|'body'
op|'.'
name|'append'
op|'('
name|'row'
op|')'
newline|'\n'
name|'for'
name|'col_name'
name|'in'
name|'cols'
op|':'
newline|'\n'
indent|'            '
name|'col'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'append'
op|'('
name|'col'
op|')'
newline|'\n'
name|'text'
op|'='
name|'nodes'
op|'.'
name|'strong'
op|'('
name|'text'
op|'='
name|'col_name'
op|')'
newline|'\n'
name|'col'
op|'.'
name|'append'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
comment|'# fill the table content, one notification per row'
nl|'\n'
dedent|''
name|'for'
name|'name'
op|','
name|'payload'
op|','
name|'sample'
name|'in'
name|'notifications'
op|':'
newline|'\n'
indent|'            '
name|'row'
op|'='
name|'nodes'
op|'.'
name|'row'
op|'('
op|')'
newline|'\n'
name|'body'
op|'.'
name|'append'
op|'('
name|'row'
op|')'
newline|'\n'
name|'col'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'append'
op|'('
name|'col'
op|')'
newline|'\n'
name|'text'
op|'='
name|'nodes'
op|'.'
name|'literal'
op|'('
name|'text'
op|'='
name|'name'
op|')'
newline|'\n'
name|'col'
op|'.'
name|'append'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'col'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'append'
op|'('
name|'col'
op|')'
newline|'\n'
name|'text'
op|'='
name|'nodes'
op|'.'
name|'literal'
op|'('
name|'text'
op|'='
name|'payload'
op|')'
newline|'\n'
name|'col'
op|'.'
name|'append'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'col'
op|'='
name|'nodes'
op|'.'
name|'entry'
op|'('
op|')'
newline|'\n'
name|'row'
op|'.'
name|'append'
op|'('
name|'col'
op|')'
newline|'\n'
name|'ref'
op|'='
name|'nodes'
op|'.'
name|'reference'
op|'('
name|'refuri'
op|'='
name|'self'
op|'.'
name|'LINK_PREFIX'
op|'+'
nl|'\n'
name|'self'
op|'.'
name|'SAMPLE_ROOT'
op|'+'
name|'sample'
op|')'
newline|'\n'
name|'txt'
op|'='
name|'nodes'
op|'.'
name|'inline'
op|'('
op|')'
newline|'\n'
name|'col'
op|'.'
name|'append'
op|'('
name|'txt'
op|')'
newline|'\n'
name|'txt'
op|'.'
name|'append'
op|'('
name|'ref'
op|')'
newline|'\n'
name|'ref'
op|'.'
name|'append'
op|'('
name|'nodes'
op|'.'
name|'literal'
op|'('
name|'text'
op|'='
name|'sample'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'content'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'app'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'app'
op|'.'
name|'add_directive'
op|'('
string|"'versioned_notifications'"
op|','
nl|'\n'
name|'VersionedNotificationDirective'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
