begin_unit
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""An input/output window for the glade reactor inspector.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'gtk'
newline|'\n'
name|'import'
name|'gobject'
newline|'\n'
name|'import'
name|'gtk'
op|'.'
name|'glade'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'util'
name|'import'
name|'sibpath'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'reflect'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'manhole'
op|'.'
name|'ui'
name|'import'
name|'gtk2manhole'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
op|'.'
name|'components'
name|'import'
name|'Adapter'
op|','
name|'registerAdapter'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'policies'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
op|','
name|'Interface'
newline|'\n'
nl|'\n'
comment|'# the glade file uses stock icons, which requires gnome to be installed'
nl|'\n'
name|'import'
name|'gnome'
newline|'\n'
DECL|variable|version
name|'version'
op|'='
string|'"$Revision: 1.1 $"'
op|'['
number|'11'
op|':'
op|'-'
number|'2'
op|']'
newline|'\n'
name|'gnome'
op|'.'
name|'init'
op|'('
string|'"gladereactor Inspector"'
op|','
name|'version'
op|')'
newline|'\n'
nl|'\n'
DECL|class|ConsoleOutput
name|'class'
name|'ConsoleOutput'
op|'('
name|'gtk2manhole'
op|'.'
name|'ConsoleOutput'
op|')'
op|':'
newline|'\n'
DECL|member|_captureLocalLog
indent|'    '
name|'def'
name|'_captureLocalLog'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fobs'
op|'='
name|'log'
op|'.'
name|'FileLogObserver'
op|'('
name|'gtk2manhole'
op|'.'
name|'_Notafile'
op|'('
name|'self'
op|','
string|'"log"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fobs'
op|'.'
name|'start'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop
dedent|''
name|'def'
name|'stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'fobs'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'fobs'
newline|'\n'
nl|'\n'
DECL|class|ConsoleInput
dedent|''
dedent|''
name|'class'
name|'ConsoleInput'
op|'('
name|'gtk2manhole'
op|'.'
name|'ConsoleInput'
op|')'
op|':'
newline|'\n'
DECL|member|sendMessage
indent|'    '
name|'def'
name|'sendMessage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'buffer'
op|'='
name|'self'
op|'.'
name|'textView'
op|'.'
name|'get_buffer'
op|'('
op|')'
newline|'\n'
name|'iter1'
op|','
name|'iter2'
op|'='
name|'buffer'
op|'.'
name|'get_bounds'
op|'('
op|')'
newline|'\n'
name|'text'
op|'='
name|'buffer'
op|'.'
name|'get_text'
op|'('
name|'iter1'
op|','
name|'iter2'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'do'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|member|do
dedent|''
name|'def'
name|'do'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'toplevel'
op|'.'
name|'do'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
DECL|class|INode
dedent|''
dedent|''
name|'class'
name|'INode'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A node in the inspector tree model.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__adapt__
name|'def'
name|'__adapt__'
op|'('
name|'adaptable'
op|','
name|'default'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'adaptable'
op|','
string|'"__dict__"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'InstanceNode'
op|'('
name|'adaptable'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'AttributesNode'
op|'('
name|'adaptable'
op|')'
newline|'\n'
nl|'\n'
DECL|class|InspectorNode
dedent|''
dedent|''
name|'class'
name|'InspectorNode'
op|'('
name|'Adapter'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'implements'
op|'('
name|'INode'
op|')'
newline|'\n'
nl|'\n'
DECL|member|postInit
name|'def'
name|'postInit'
op|'('
name|'self'
op|','
name|'offset'
op|','
name|'parent'
op|','
name|'slot'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'offset'
op|'='
name|'offset'
newline|'\n'
name|'self'
op|'.'
name|'parent'
op|'='
name|'parent'
newline|'\n'
name|'self'
op|'.'
name|'slot'
op|'='
name|'slot'
newline|'\n'
nl|'\n'
DECL|member|getPath
dedent|''
name|'def'
name|'getPath'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'L'
op|'='
op|'['
op|']'
newline|'\n'
name|'x'
op|'='
name|'self'
newline|'\n'
name|'while'
name|'x'
op|'.'
name|'parent'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'L'
op|'.'
name|'append'
op|'('
name|'x'
op|'.'
name|'offset'
op|')'
newline|'\n'
name|'x'
op|'='
name|'x'
op|'.'
name|'parent'
newline|'\n'
dedent|''
name|'L'
op|'.'
name|'reverse'
op|'('
op|')'
newline|'\n'
name|'return'
name|'L'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'slot'
op|','
name|'o'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'index'
op|')'
newline|'\n'
name|'n'
op|'='
name|'INode'
op|'('
name|'o'
op|','
name|'persist'
op|'='
name|'False'
op|')'
newline|'\n'
name|'n'
op|'.'
name|'postInit'
op|'('
name|'index'
op|','
name|'self'
op|','
name|'slot'
op|')'
newline|'\n'
name|'return'
name|'n'
newline|'\n'
nl|'\n'
DECL|member|origstr
dedent|''
name|'def'
name|'origstr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'str'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
newline|'\n'
nl|'\n'
DECL|member|format
dedent|''
name|'def'
name|'format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'self'
op|'.'
name|'slot'
op|','
name|'self'
op|'.'
name|'origstr'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConstantNode
dedent|''
dedent|''
name|'class'
name|'ConstantNode'
op|'('
name|'InspectorNode'
op|')'
op|':'
newline|'\n'
DECL|member|__len__
indent|'    '
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|class|DictionaryNode
dedent|''
dedent|''
name|'class'
name|'DictionaryNode'
op|'('
name|'InspectorNode'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'L'
op|'='
name|'self'
op|'.'
name|'original'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'L'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'L'
op|'['
name|'index'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
newline|'\n'
nl|'\n'
DECL|member|origstr
dedent|''
name|'def'
name|'origstr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Dictionary"'
newline|'\n'
nl|'\n'
DECL|class|ListNode
dedent|''
dedent|''
name|'class'
name|'ListNode'
op|'('
name|'InspectorNode'
op|')'
op|':'
newline|'\n'
DECL|member|get
indent|'    '
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'index'
op|','
name|'self'
op|'.'
name|'original'
op|'['
name|'index'
op|']'
newline|'\n'
nl|'\n'
DECL|member|origstr
dedent|''
name|'def'
name|'origstr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"List"'
newline|'\n'
nl|'\n'
DECL|member|__len__
dedent|''
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
newline|'\n'
nl|'\n'
DECL|class|AttributesNode
dedent|''
dedent|''
name|'class'
name|'AttributesNode'
op|'('
name|'InspectorNode'
op|')'
op|':'
newline|'\n'
DECL|member|__len__
indent|'    '
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'dir'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'L'
op|'='
name|'dir'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
newline|'\n'
name|'L'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'L'
op|'['
name|'index'
op|']'
op|','
name|'getattr'
op|'('
name|'self'
op|'.'
name|'original'
op|','
name|'L'
op|'['
name|'index'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|class|InstanceNode
dedent|''
dedent|''
name|'class'
name|'InstanceNode'
op|'('
name|'InspectorNode'
op|')'
op|':'
newline|'\n'
DECL|member|__len__
indent|'    '
name|'def'
name|'__len__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'self'
op|'.'
name|'original'
op|'.'
name|'__dict__'
op|')'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'index'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'hasattr'
op|'('
name|'self'
op|'.'
name|'original'
op|','
string|'"__class__"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'v'
op|'='
name|'self'
op|'.'
name|'original'
op|'.'
name|'__class__'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'v'
op|'='
name|'type'
op|'('
name|'self'
op|'.'
name|'original'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'"__class__"'
op|','
name|'v'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'index'
op|'-='
number|'1'
newline|'\n'
name|'L'
op|'='
name|'self'
op|'.'
name|'original'
op|'.'
name|'__dict__'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'L'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'return'
name|'L'
op|'['
name|'index'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'import'
name|'types'
newline|'\n'
nl|'\n'
name|'for'
name|'x'
name|'in'
name|'dict'
op|','
name|'types'
op|'.'
name|'DictProxyType'
op|':'
newline|'\n'
indent|'    '
name|'registerAdapter'
op|'('
name|'DictionaryNode'
op|','
name|'x'
op|','
name|'INode'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'x'
name|'in'
name|'list'
op|','
name|'tuple'
op|':'
newline|'\n'
indent|'    '
name|'registerAdapter'
op|'('
name|'ListNode'
op|','
name|'x'
op|','
name|'INode'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'x'
name|'in'
name|'int'
op|','
name|'str'
op|':'
newline|'\n'
indent|'    '
name|'registerAdapter'
op|'('
name|'ConstantNode'
op|','
name|'x'
op|','
name|'INode'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InspectorTreeModel
dedent|''
name|'class'
name|'InspectorTreeModel'
op|'('
name|'gtk'
op|'.'
name|'GenericTreeModel'
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
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gtk'
op|'.'
name|'GenericTreeModel'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'root'
op|'='
name|'INode'
op|'('
name|'root'
op|','
name|'persist'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'root'
op|'.'
name|'postInit'
op|'('
number|'0'
op|','
name|'None'
op|','
string|"'root'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_get_flags
dedent|''
name|'def'
name|'on_get_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
nl|'\n'
DECL|member|on_get_n_columns
dedent|''
name|'def'
name|'on_get_n_columns'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|on_get_column_type
dedent|''
name|'def'
name|'on_get_column_type'
op|'('
name|'self'
op|','
name|'index'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'gobject'
op|'.'
name|'TYPE_STRING'
newline|'\n'
nl|'\n'
DECL|member|on_get_path
dedent|''
name|'def'
name|'on_get_path'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'node'
op|'.'
name|'getPath'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_get_iter
dedent|''
name|'def'
name|'on_get_iter'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
name|'self'
op|'.'
name|'root'
newline|'\n'
name|'for'
name|'elem'
name|'in'
name|'path'
op|':'
newline|'\n'
indent|'            '
name|'x'
op|'='
name|'x'
op|'['
name|'elem'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'x'
newline|'\n'
nl|'\n'
DECL|member|on_get_value
dedent|''
name|'def'
name|'on_get_value'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'column'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'node'
op|'.'
name|'format'
op|'('
op|')'
op|'['
name|'column'
op|']'
newline|'\n'
nl|'\n'
DECL|member|on_iter_next
dedent|''
name|'def'
name|'on_iter_next'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'node'
op|'.'
name|'parent'
op|'['
name|'node'
op|'.'
name|'offset'
op|'+'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|on_iter_children
dedent|''
dedent|''
name|'def'
name|'on_iter_children'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'node'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|on_iter_has_child
dedent|''
name|'def'
name|'on_iter_has_child'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_iter_n_children
dedent|''
name|'def'
name|'on_iter_n_children'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'len'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_iter_nth_child
dedent|''
name|'def'
name|'on_iter_nth_child'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'n'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'node'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'node'
op|'['
name|'n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|on_iter_parent
dedent|''
name|'def'
name|'on_iter_parent'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'node'
op|'.'
name|'parent'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Inspectro
dedent|''
dedent|''
name|'class'
name|'Inspectro'
op|':'
newline|'\n'
DECL|variable|selected
indent|'    '
name|'selected'
op|'='
name|'None'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'o'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'xml'
op|'='
name|'x'
op|'='
name|'gtk'
op|'.'
name|'glade'
op|'.'
name|'XML'
op|'('
name|'sibpath'
op|'('
name|'__file__'
op|','
string|'"inspectro.glade"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tree_view'
op|'='
name|'x'
op|'.'
name|'get_widget'
op|'('
string|'"treeview"'
op|')'
newline|'\n'
name|'colnames'
op|'='
op|'['
string|'"Name"'
op|','
string|'"Value"'
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'colnames'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'tree_view'
op|'.'
name|'append_column'
op|'('
nl|'\n'
name|'gtk'
op|'.'
name|'TreeViewColumn'
op|'('
nl|'\n'
name|'colnames'
op|'['
name|'i'
op|']'
op|','
name|'gtk'
op|'.'
name|'CellRendererText'
op|'('
op|')'
op|','
name|'text'
op|'='
name|'i'
op|')'
op|')'
newline|'\n'
dedent|''
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'m'
name|'in'
name|'reflect'
op|'.'
name|'prefixedMethods'
op|'('
name|'self'
op|','
string|'"on_"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'m'
op|'.'
name|'im_func'
op|'.'
name|'__name__'
op|']'
op|'='
name|'m'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'xml'
op|'.'
name|'signal_autoconnect'
op|'('
name|'d'
op|')'
newline|'\n'
name|'if'
name|'o'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'inspect'
op|'('
name|'o'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'ns'
op|'='
op|'{'
string|"'inspect'"
op|':'
name|'self'
op|'.'
name|'inspect'
op|'}'
newline|'\n'
name|'iwidget'
op|'='
name|'x'
op|'.'
name|'get_widget'
op|'('
string|"'input'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'input'
op|'='
name|'ConsoleInput'
op|'('
name|'iwidget'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'input'
op|'.'
name|'toplevel'
op|'='
name|'self'
newline|'\n'
name|'iwidget'
op|'.'
name|'connect'
op|'('
string|'"key_press_event"'
op|','
name|'self'
op|'.'
name|'input'
op|'.'
name|'_on_key_press_event'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'output'
op|'='
name|'ConsoleOutput'
op|'('
name|'x'
op|'.'
name|'get_widget'
op|'('
string|"'output'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|select
dedent|''
name|'def'
name|'select'
op|'('
name|'self'
op|','
name|'o'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'selected'
op|'='
name|'o'
newline|'\n'
name|'self'
op|'.'
name|'ns'
op|'['
string|"'it'"
op|']'
op|'='
name|'o'
newline|'\n'
name|'self'
op|'.'
name|'xml'
op|'.'
name|'get_widget'
op|'('
string|'"itname"'
op|')'
op|'.'
name|'set_text'
op|'('
name|'repr'
op|'('
name|'o'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xml'
op|'.'
name|'get_widget'
op|'('
string|'"itpath"'
op|')'
op|'.'
name|'set_text'
op|'('
string|'"???"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|inspect
dedent|''
name|'def'
name|'inspect'
op|'('
name|'self'
op|','
name|'o'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'model'
op|'='
name|'InspectorTreeModel'
op|'('
name|'o'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tree_view'
op|'.'
name|'set_model'
op|'('
name|'self'
op|'.'
name|'model'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inspected'
op|'='
name|'o'
newline|'\n'
nl|'\n'
DECL|member|do
dedent|''
name|'def'
name|'do'
op|'('
name|'self'
op|','
name|'command'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'filename'
op|'='
string|"'<inspector>'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'print'
name|'repr'
op|'('
name|'command'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'code'
op|'='
name|'compile'
op|'('
name|'command'
op|','
name|'filename'
op|','
string|"'eval'"
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'                '
name|'code'
op|'='
name|'compile'
op|'('
name|'command'
op|','
name|'filename'
op|','
string|"'single'"
op|')'
newline|'\n'
dedent|''
name|'val'
op|'='
name|'eval'
op|'('
name|'code'
op|','
name|'self'
op|'.'
name|'ns'
op|','
name|'self'
op|'.'
name|'ns'
op|')'
newline|'\n'
name|'if'
name|'val'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'print'
name|'repr'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'ns'
op|'['
string|"'_'"
op|']'
op|'='
name|'val'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'err'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_inspect
dedent|''
dedent|''
name|'def'
name|'on_inspect'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'inspect'
op|'('
name|'self'
op|'.'
name|'selected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_inspect_new
dedent|''
name|'def'
name|'on_inspect_new'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'Inspectro'
op|'('
name|'self'
op|'.'
name|'selected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_row_activated
dedent|''
name|'def'
name|'on_row_activated'
op|'('
name|'self'
op|','
name|'tv'
op|','
name|'path'
op|','
name|'column'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'select'
op|'('
name|'self'
op|'.'
name|'model'
op|'.'
name|'on_get_iter'
op|'('
name|'path'
op|')'
op|'.'
name|'original'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoggingProtocol
dedent|''
dedent|''
name|'class'
name|'LoggingProtocol'
op|'('
name|'policies'
op|'.'
name|'ProtocolWrapper'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Log network traffic."""'
newline|'\n'
nl|'\n'
DECL|variable|logging
name|'logging'
op|'='
name|'True'
newline|'\n'
DECL|variable|logViewer
name|'logViewer'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'policies'
op|'.'
name|'ProtocolWrapper'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'inLog'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'outLog'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|write
dedent|''
name|'def'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'logging'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'outLog'
op|'.'
name|'append'
op|'('
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|','
name|'data'
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'logViewer'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'logViewer'
op|'.'
name|'updateOut'
op|'('
name|'self'
op|'.'
name|'outLog'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'policies'
op|'.'
name|'ProtocolWrapper'
op|'.'
name|'write'
op|'('
name|'self'
op|','
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dataReceived
dedent|''
name|'def'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'logging'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'inLog'
op|'.'
name|'append'
op|'('
op|'('
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|','
name|'data'
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'logViewer'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'logViewer'
op|'.'
name|'updateIn'
op|'('
name|'self'
op|'.'
name|'inLog'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'policies'
op|'.'
name|'ProtocolWrapper'
op|'.'
name|'dataReceived'
op|'('
name|'self'
op|','
name|'data'
op|')'
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
name|'r'
op|'='
string|'"wrapped "'
op|'+'
name|'repr'
op|'('
name|'self'
op|'.'
name|'wrappedProtocol'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'logging'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|'+='
string|'" (logging)"'
newline|'\n'
dedent|''
name|'return'
name|'r'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoggingFactory
dedent|''
dedent|''
name|'class'
name|'LoggingFactory'
op|'('
name|'policies'
op|'.'
name|'WrappingFactory'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrap protocols with logging wrappers."""'
newline|'\n'
nl|'\n'
DECL|variable|protocol
name|'protocol'
op|'='
name|'LoggingProtocol'
newline|'\n'
DECL|variable|logging
name|'logging'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|member|buildProtocol
name|'def'
name|'buildProtocol'
op|'('
name|'self'
op|','
name|'addr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'self'
op|'.'
name|'protocol'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'wrappedFactory'
op|'.'
name|'buildProtocol'
op|'('
name|'addr'
op|')'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'logging'
op|'='
name|'self'
op|'.'
name|'logging'
newline|'\n'
name|'return'
name|'p'
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
name|'r'
op|'='
string|'"wrapped "'
op|'+'
name|'repr'
op|'('
name|'self'
op|'.'
name|'wrappedFactory'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'logging'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|'+='
string|'" (logging)"'
newline|'\n'
dedent|''
name|'return'
name|'r'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LogViewer
dedent|''
dedent|''
name|'class'
name|'LogViewer'
op|':'
newline|'\n'
indent|'    '
string|'"""Display log of network traffic."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'p'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'p'
op|'='
name|'p'
newline|'\n'
name|'vals'
op|'='
op|'['
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|']'
newline|'\n'
name|'if'
name|'p'
op|'.'
name|'inLog'
op|':'
newline|'\n'
indent|'            '
name|'vals'
op|'.'
name|'append'
op|'('
name|'p'
op|'.'
name|'inLog'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'p'
op|'.'
name|'outLog'
op|':'
newline|'\n'
indent|'            '
name|'vals'
op|'.'
name|'append'
op|'('
name|'p'
op|'.'
name|'outLog'
op|'['
number|'0'
op|']'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'startTime'
op|'='
name|'min'
op|'('
name|'vals'
op|')'
newline|'\n'
name|'p'
op|'.'
name|'logViewer'
op|'='
name|'self'
newline|'\n'
name|'self'
op|'.'
name|'xml'
op|'='
name|'x'
op|'='
name|'gtk'
op|'.'
name|'glade'
op|'.'
name|'XML'
op|'('
name|'sibpath'
op|'('
name|'__file__'
op|','
string|'"logview.glade"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'xml'
op|'.'
name|'signal_autoconnect'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loglist'
op|'='
name|'self'
op|'.'
name|'xml'
op|'.'
name|'get_widget'
op|'('
string|'"loglist"'
op|')'
newline|'\n'
comment|'# setup model, connect it to my treeview'
nl|'\n'
name|'self'
op|'.'
name|'model'
op|'='
name|'gtk'
op|'.'
name|'ListStore'
op|'('
name|'str'
op|','
name|'str'
op|','
name|'str'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loglist'
op|'.'
name|'set_model'
op|'('
name|'self'
op|'.'
name|'model'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loglist'
op|'.'
name|'set_reorderable'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'loglist'
op|'.'
name|'set_headers_clickable'
op|'('
number|'1'
op|')'
newline|'\n'
comment|'# self.servers.set_headers_draggable(1)'
nl|'\n'
comment|'# add a column'
nl|'\n'
name|'for'
name|'col'
name|'in'
op|'['
nl|'\n'
name|'gtk'
op|'.'
name|'TreeViewColumn'
op|'('
string|"'Time'"
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'CellRendererText'
op|'('
op|')'
op|','
nl|'\n'
name|'text'
op|'='
number|'0'
op|')'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'TreeViewColumn'
op|'('
string|"'D'"
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'CellRendererText'
op|'('
op|')'
op|','
nl|'\n'
name|'text'
op|'='
number|'1'
op|')'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'TreeViewColumn'
op|'('
string|"'Data'"
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'CellRendererText'
op|'('
op|')'
op|','
nl|'\n'
name|'text'
op|'='
number|'2'
op|')'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'loglist'
op|'.'
name|'append_column'
op|'('
name|'col'
op|')'
newline|'\n'
name|'col'
op|'.'
name|'set_resizable'
op|'('
number|'1'
op|')'
newline|'\n'
dedent|''
name|'r'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'t'
op|','
name|'data'
name|'in'
name|'p'
op|'.'
name|'inLog'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|'.'
name|'append'
op|'('
op|'('
op|'('
name|'str'
op|'('
name|'t'
op|'-'
name|'self'
op|'.'
name|'startTime'
op|')'
op|','
string|'"R"'
op|','
name|'repr'
op|'('
name|'data'
op|')'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'t'
op|','
name|'data'
name|'in'
name|'p'
op|'.'
name|'outLog'
op|':'
newline|'\n'
indent|'            '
name|'r'
op|'.'
name|'append'
op|'('
op|'('
op|'('
name|'str'
op|'('
name|'t'
op|'-'
name|'self'
op|'.'
name|'startTime'
op|')'
op|','
string|'"S"'
op|','
name|'repr'
op|'('
name|'data'
op|')'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'r'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'r'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'model'
op|'.'
name|'append'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
DECL|member|updateIn
dedent|''
dedent|''
name|'def'
name|'updateIn'
op|'('
name|'self'
op|','
op|'('
name|'time'
op|','
name|'data'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'model'
op|'.'
name|'append'
op|'('
op|'('
name|'str'
op|'('
name|'time'
op|'-'
name|'self'
op|'.'
name|'startTime'
op|')'
op|','
string|'"R"'
op|','
name|'repr'
op|'('
name|'data'
op|')'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|updateOut
dedent|''
name|'def'
name|'updateOut'
op|'('
name|'self'
op|','
op|'('
name|'time'
op|','
name|'data'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'model'
op|'.'
name|'append'
op|'('
op|'('
name|'str'
op|'('
name|'time'
op|'-'
name|'self'
op|'.'
name|'startTime'
op|')'
op|','
string|'"S"'
op|','
name|'repr'
op|'('
name|'data'
op|')'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|on_logview_destroy
dedent|''
name|'def'
name|'on_logview_destroy'
op|'('
name|'self'
op|','
name|'w'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'p'
op|'.'
name|'logViewer'
op|'='
name|'None'
newline|'\n'
name|'del'
name|'self'
op|'.'
name|'p'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|main
dedent|''
dedent|''
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'x'
op|'='
name|'Inspectro'
op|'('
op|')'
newline|'\n'
name|'x'
op|'.'
name|'inspect'
op|'('
name|'x'
op|')'
newline|'\n'
name|'gtk'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|"'__main__'"
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'sys'
newline|'\n'
name|'log'
op|'.'
name|'startLogging'
op|'('
name|'sys'
op|'.'
name|'stdout'
op|')'
newline|'\n'
name|'main'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
