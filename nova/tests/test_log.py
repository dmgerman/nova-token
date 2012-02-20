begin_unit
name|'import'
name|'cStringIO'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_context
name|'def'
name|'_fake_context'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'context'
op|'.'
name|'RequestContext'
op|'('
number|'1'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoggerTestCase
dedent|''
name|'class'
name|'LoggerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LoggerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_handlers_have_nova_formatter
dedent|''
name|'def'
name|'test_handlers_have_nova_formatter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'formatters'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'h'
name|'in'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'h'
op|'.'
name|'formatter'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'f'
op|','
name|'log'
op|'.'
name|'LegacyNovaFormatter'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'formatters'
op|'.'
name|'append'
op|'('
name|'f'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assert_'
op|'('
name|'formatters'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'formatters'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'handlers'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_handles_context_kwarg
dedent|''
name|'def'
name|'test_handles_context_kwarg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'log'
op|'.'
name|'info'
op|'('
string|'"foo"'
op|','
name|'context'
op|'='
name|'_fake_context'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'True'
op|')'
comment|"# didn't raise exception"
newline|'\n'
nl|'\n'
DECL|member|test_audit_handles_context_arg
dedent|''
name|'def'
name|'test_audit_handles_context_arg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'log'
op|'.'
name|'audit'
op|'('
string|'"foo"'
op|','
name|'context'
op|'='
name|'_fake_context'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assert_'
op|'('
name|'True'
op|')'
comment|"# didn't raise exception"
newline|'\n'
nl|'\n'
DECL|member|test_will_be_verbose_if_verbose_flag_set
dedent|''
name|'def'
name|'test_will_be_verbose_if_verbose_flag_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|','
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'getEffectiveLevel'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_will_not_be_verbose_if_verbose_flag_not_set
dedent|''
name|'def'
name|'test_will_not_be_verbose_if_verbose_flag_not_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'verbose'
op|'='
name|'False'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'INFO'
op|','
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'getEffectiveLevel'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_no_logging_via_module
dedent|''
name|'def'
name|'test_no_logging_via_module'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'func'
name|'in'
op|'('
string|"'critical'"
op|','
string|"'error'"
op|','
string|"'exception'"
op|','
string|"'warning'"
op|','
string|"'warn'"
op|','
nl|'\n'
string|"'info'"
op|','
string|"'debug'"
op|','
string|"'log'"
op|','
string|"'audit'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
name|'getattr'
op|','
name|'log'
op|','
name|'func'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LogHandlerTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'LogHandlerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_log_path_logdir
indent|'    '
name|'def'
name|'test_log_path_logdir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'logdir'
op|'='
string|"'/some/path'"
op|','
name|'logfile'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'log'
op|'.'
name|'_get_log_file_path'
op|'('
name|'binary'
op|'='
string|"'foo-bar'"
op|')'
op|','
nl|'\n'
string|"'/some/path/foo-bar.log'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_log_path_logfile
dedent|''
name|'def'
name|'test_log_path_logfile'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'logfile'
op|'='
string|"'/some/path/foo-bar.log'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'log'
op|'.'
name|'_get_log_file_path'
op|'('
name|'binary'
op|'='
string|"'foo-bar'"
op|')'
op|','
nl|'\n'
string|"'/some/path/foo-bar.log'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_log_path_none
dedent|''
name|'def'
name|'test_log_path_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'logdir'
op|'='
name|'None'
op|','
name|'logfile'
op|'='
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'log'
op|'.'
name|'_get_log_file_path'
op|'('
name|'binary'
op|'='
string|"'foo-bar'"
op|')'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_log_path_logfile_overrides_logdir
dedent|''
name|'def'
name|'test_log_path_logfile_overrides_logdir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'logdir'
op|'='
string|"'/some/other/path'"
op|','
nl|'\n'
name|'logfile'
op|'='
string|"'/some/path/foo-bar.log'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'log'
op|'.'
name|'_get_log_file_path'
op|'('
name|'binary'
op|'='
string|"'foo-bar'"
op|')'
op|','
nl|'\n'
string|"'/some/path/foo-bar.log'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaFormatterTestCase
dedent|''
dedent|''
name|'class'
name|'NovaFormatterTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NovaFormatterTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'logging_context_format_string'
op|'='
string|'"HAS CONTEXT "'
nl|'\n'
string|'"[%(request_id)s]: "'
nl|'\n'
string|'"%(message)s"'
op|','
nl|'\n'
name|'logging_default_format_string'
op|'='
string|'"NOCTXT: %(message)s"'
op|','
nl|'\n'
name|'logging_debug_format_suffix'
op|'='
string|'"--DBG"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
name|'self'
op|'.'
name|'stream'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'log'
op|'.'
name|'LegacyNovaFormatter'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'addHandler'
op|'('
name|'self'
op|'.'
name|'handler'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'level'
op|'='
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'getEffectiveLevel'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'self'
op|'.'
name|'level'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'removeHandler'
op|'('
name|'self'
op|'.'
name|'handler'
op|')'
newline|'\n'
name|'super'
op|'('
name|'NovaFormatterTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_uncontextualized_log
dedent|''
name|'def'
name|'test_uncontextualized_log'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'log'
op|'.'
name|'info'
op|'('
string|'"foo"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"NOCTXT: foo\\n"'
op|','
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_contextualized_log
dedent|''
name|'def'
name|'test_contextualized_log'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'_fake_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'info'
op|'('
string|'"bar"'
op|','
name|'context'
op|'='
name|'ctxt'
op|')'
newline|'\n'
name|'expected'
op|'='
string|'"HAS CONTEXT [%s]: bar\\n"'
op|'%'
name|'ctxt'
op|'.'
name|'request_id'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_debugging_log
dedent|''
name|'def'
name|'test_debugging_log'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'log'
op|'.'
name|'debug'
op|'('
string|'"baz"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"NOCTXT: baz --DBG\\n"'
op|','
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NovaLoggerTestCase
dedent|''
dedent|''
name|'class'
name|'NovaLoggerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NovaLoggerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'levels'
op|'='
name|'FLAGS'
op|'.'
name|'default_log_levels'
newline|'\n'
name|'levels'
op|'.'
name|'append'
op|'('
string|'"nova-test=AUDIT"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'default_log_levels'
op|'='
name|'levels'
op|','
nl|'\n'
name|'verbose'
op|'='
name|'True'
op|')'
newline|'\n'
name|'log'
op|'.'
name|'setup'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova-test'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_has_level_from_flags
dedent|''
name|'def'
name|'test_has_level_from_flags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'AUDIT'
op|','
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'getEffectiveLevel'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_child_log_has_level_of_parent_flag
dedent|''
name|'def'
name|'test_child_log_has_level_of_parent_flag'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'l'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'nova-test.foo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'AUDIT'
op|','
name|'l'
op|'.'
name|'logger'
op|'.'
name|'getEffectiveLevel'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONFormatterTestCase
dedent|''
dedent|''
name|'class'
name|'JSONFormatterTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'JSONFormatterTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'='
name|'log'
op|'.'
name|'getLogger'
op|'('
string|"'test-json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stream'
op|'='
name|'cStringIO'
op|'.'
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'handler'
op|'='
name|'logging'
op|'.'
name|'StreamHandler'
op|'('
name|'self'
op|'.'
name|'stream'
op|')'
newline|'\n'
name|'handler'
op|'.'
name|'setFormatter'
op|'('
name|'log'
op|'.'
name|'JSONFormatter'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'addHandler'
op|'('
name|'handler'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'logger'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json
dedent|''
name|'def'
name|'test_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_msg'
op|'='
string|"'This is a %(test)s line'"
newline|'\n'
name|'test_data'
op|'='
op|'{'
string|"'test'"
op|':'
string|"'log'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'log'
op|'.'
name|'debug'
op|'('
name|'test_msg'
op|','
name|'test_data'
op|')'
newline|'\n'
nl|'\n'
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'extra'"
name|'in'
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test-json'"
op|','
name|'data'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_msg'
op|'%'
name|'test_data'
op|','
name|'data'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_msg'
op|','
name|'data'
op|'['
string|"'msg'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_data'
op|','
name|'data'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test_log.py'"
op|','
name|'data'
op|'['
string|"'filename'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test_json'"
op|','
name|'data'
op|'['
string|"'funcname'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'DEBUG'"
op|','
name|'data'
op|'['
string|"'levelname'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|','
name|'data'
op|'['
string|"'levelno'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'data'
op|'['
string|"'traceback'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_json_exception
dedent|''
name|'def'
name|'test_json_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'test_msg'
op|'='
string|"'This is %s'"
newline|'\n'
name|'test_data'
op|'='
string|"'exceptional'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|"'This is exceptional'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'log'
op|'.'
name|'exception'
op|'('
name|'test_msg'
op|','
name|'test_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'self'
op|'.'
name|'stream'
op|'.'
name|'getvalue'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'extra'"
name|'in'
name|'data'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'test-json'"
op|','
name|'data'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_msg'
op|'%'
name|'test_data'
op|','
name|'data'
op|'['
string|"'message'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_msg'
op|','
name|'data'
op|'['
string|"'msg'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'test_data'
op|']'
op|','
name|'data'
op|'['
string|"'args'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'ERROR'"
op|','
name|'data'
op|'['
string|"'levelname'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'logging'
op|'.'
name|'ERROR'
op|','
name|'data'
op|'['
string|"'levelno'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'data'
op|'['
string|"'traceback'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
