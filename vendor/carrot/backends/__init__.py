begin_unit
string|'"""\n\nWorking with Backends.\n\n"""'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'carrot'
op|'.'
name|'utils'
name|'import'
name|'rpartition'
newline|'\n'
nl|'\n'
DECL|variable|DEFAULT_BACKEND
name|'DEFAULT_BACKEND'
op|'='
string|'"carrot.backends.pyamqplib.Backend"'
newline|'\n'
nl|'\n'
DECL|variable|BACKEND_ALIASES
name|'BACKEND_ALIASES'
op|'='
op|'{'
nl|'\n'
string|'"amqp"'
op|':'
string|'"carrot.backends.pyamqplib.Backend"'
op|','
nl|'\n'
string|'"amqplib"'
op|':'
string|'"carrot.backends.pyamqplib.Backend"'
op|','
nl|'\n'
string|'"stomp"'
op|':'
string|'"carrot.backends.pystomp.Backend"'
op|','
nl|'\n'
string|'"stompy"'
op|':'
string|'"carrot.backends.pystomp.Backend"'
op|','
nl|'\n'
string|'"memory"'
op|':'
string|'"carrot.backends.queue.Backend"'
op|','
nl|'\n'
string|'"mem"'
op|':'
string|'"carrot.backends.queue.Backend"'
op|','
nl|'\n'
string|'"pika"'
op|':'
string|'"carrot.backends.pikachu.AsyncoreBackend"'
op|','
nl|'\n'
string|'"pikachu"'
op|':'
string|'"carrot.backends.pikachu.AsyncoreBackend"'
op|','
nl|'\n'
string|'"syncpika"'
op|':'
string|'"carrot.backends.pikachu.SyncBackend"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|_backend_cache
name|'_backend_cache'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|resolve_backend
name|'def'
name|'resolve_backend'
op|'('
name|'backend'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'backend'
op|'='
name|'BACKEND_ALIASES'
op|'.'
name|'get'
op|'('
name|'backend'
op|','
name|'backend'
op|')'
newline|'\n'
name|'backend_module_name'
op|','
name|'_'
op|','
name|'backend_cls_name'
op|'='
name|'rpartition'
op|'('
name|'backend'
op|','
string|'"."'
op|')'
newline|'\n'
name|'return'
name|'backend_module_name'
op|','
name|'backend_cls_name'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_backend_cls
dedent|''
name|'def'
name|'_get_backend_cls'
op|'('
name|'backend'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'backend_module_name'
op|','
name|'backend_cls_name'
op|'='
name|'resolve_backend'
op|'('
name|'backend'
op|')'
newline|'\n'
name|'__import__'
op|'('
name|'backend_module_name'
op|')'
newline|'\n'
name|'backend_module'
op|'='
name|'sys'
op|'.'
name|'modules'
op|'['
name|'backend_module_name'
op|']'
newline|'\n'
name|'return'
name|'getattr'
op|'('
name|'backend_module'
op|','
name|'backend_cls_name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_backend_cls
dedent|''
name|'def'
name|'get_backend_cls'
op|'('
name|'backend'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get backend class by name.\n\n    The backend string is the full path to a backend class, e.g.::\n\n        "carrot.backends.pyamqplib.Backend"\n\n    If the name does not include "``.``" (is not fully qualified),\n    the alias table will be consulted.\n\n    """'
newline|'\n'
name|'backend'
op|'='
name|'backend'
name|'or'
name|'DEFAULT_BACKEND'
newline|'\n'
name|'if'
name|'backend'
name|'not'
name|'in'
name|'_backend_cache'
op|':'
newline|'\n'
indent|'        '
name|'_backend_cache'
op|'['
name|'backend'
op|']'
op|'='
name|'_get_backend_cls'
op|'('
name|'backend'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_backend_cache'
op|'['
name|'backend'
op|']'
newline|'\n'
dedent|''
endmarker|''
end_unit
