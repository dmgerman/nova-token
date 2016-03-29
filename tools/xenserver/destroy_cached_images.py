begin_unit
string|'"""\ndestroy_cached_images.py\n\nThis script is used to clean up Glance images that are cached in the SR. By\ndefault, this script will only cleanup unused cached images.\n\nOptions:\n\n    --dry_run - Don\'t actually destroy the VDIs\n    --all_cached - Destroy all cached images instead of just unused cached\n                   images.\n"""'
newline|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'eventlet'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
comment|'# If ../nova/__init__.py exists, add ../ to Python search path, so that'
nl|'\n'
comment|'# it will override what happens to be installed in /usr/(local/)lib/python...'
nl|'\n'
DECL|variable|POSSIBLE_TOPDIR
name|'POSSIBLE_TOPDIR'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'sys'
op|'.'
name|'argv'
op|'['
number|'0'
op|']'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|','
nl|'\n'
name|'os'
op|'.'
name|'pardir'
op|')'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'POSSIBLE_TOPDIR'
op|','
string|"'nova'"
op|','
string|"'__init__.py'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'sys'
op|'.'
name|'path'
op|'.'
name|'insert'
op|'('
number|'0'
op|','
name|'POSSIBLE_TOPDIR'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'client'
name|'import'
name|'session'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
DECL|variable|destroy_opts
name|'destroy_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'all_cached'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Destroy all cached images instead of just unused cached'"
nl|'\n'
string|"' images.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'dry_run'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Don\\'t actually delete the VDIs.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_cli_opts'
op|'('
name|'destroy_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|function|main
name|'def'
name|'main'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'config'
op|'.'
name|'parse_args'
op|'('
name|'sys'
op|'.'
name|'argv'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'monkey_patch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'_session'
op|'='
name|'session'
op|'.'
name|'XenAPISession'
op|'('
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_url'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_username'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'xenserver'
op|'.'
name|'connection_password'
op|')'
newline|'\n'
nl|'\n'
name|'sr_ref'
op|'='
name|'vm_utils'
op|'.'
name|'safe_find_sr'
op|'('
name|'_session'
op|')'
newline|'\n'
name|'destroyed'
op|'='
name|'vm_utils'
op|'.'
name|'destroy_cached_images'
op|'('
nl|'\n'
name|'_session'
op|','
name|'sr_ref'
op|','
name|'all_cached'
op|'='
name|'CONF'
op|'.'
name|'all_cached'
op|','
nl|'\n'
name|'dry_run'
op|'='
name|'CONF'
op|'.'
name|'dry_run'
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'--verbose'"
name|'in'
name|'sys'
op|'.'
name|'argv'
op|':'
newline|'\n'
indent|'        '
name|'print'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'destroyed'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'print'
string|'"Destroyed %d cached VDIs"'
op|'%'
name|'len'
op|'('
name|'destroyed'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
