begin_unit
comment|'# Copyright (c) 2012 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#    a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#    under the License.'
nl|'\n'
nl|'\n'
string|'"""Various utilities used by XenServer plugins."""'
newline|'\n'
nl|'\n'
name|'import'
name|'cPickle'
name|'as'
name|'pickle'
newline|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'XenAPIPlugin'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
DECL|variable|CHUNK_SIZE
name|'CHUNK_SIZE'
op|'='
number|'8192'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CommandNotFound
name|'class'
name|'CommandNotFound'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|delete_if_exists
dedent|''
name|'def'
name|'delete_if_exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
string|'"\'%s\' was already deleted, skipping delete"'
op|'%'
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_link
dedent|''
dedent|''
dedent|''
name|'def'
name|'_link'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Hard-linking file \'%s\' -> \'%s\'"'
op|'%'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'link'
op|'('
name|'src'
op|','
name|'dst'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_rename
dedent|''
name|'def'
name|'_rename'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Renaming file \'%s\' -> \'%s\'"'
op|'%'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'os'
op|'.'
name|'rename'
op|'('
name|'src'
op|','
name|'dst'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'EXDEV'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"Invalid cross-device link.  Perhaps %s and %s should "'
nl|'\n'
string|'"be symlinked on the same filesystem?"'
op|'%'
op|'('
name|'src'
op|','
name|'dst'
op|')'
op|')'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_subprocess
dedent|''
dedent|''
name|'def'
name|'make_subprocess'
op|'('
name|'cmdline'
op|','
name|'stdout'
op|'='
name|'False'
op|','
name|'stderr'
op|'='
name|'False'
op|','
name|'stdin'
op|'='
name|'False'
op|','
nl|'\n'
name|'universal_newlines'
op|'='
name|'False'
op|','
name|'close_fds'
op|'='
name|'True'
op|','
name|'env'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Make a subprocess according to the given command-line string\n    """'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"Running cmd \'%s\'"'
op|'%'
string|'" "'
op|'.'
name|'join'
op|'('
name|'cmdline'
op|')'
op|')'
newline|'\n'
name|'kwargs'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'kwargs'
op|'['
string|"'stdout'"
op|']'
op|'='
name|'stdout'
name|'and'
name|'subprocess'
op|'.'
name|'PIPE'
name|'or'
name|'None'
newline|'\n'
name|'kwargs'
op|'['
string|"'stderr'"
op|']'
op|'='
name|'stderr'
name|'and'
name|'subprocess'
op|'.'
name|'PIPE'
name|'or'
name|'None'
newline|'\n'
name|'kwargs'
op|'['
string|"'stdin'"
op|']'
op|'='
name|'stdin'
name|'and'
name|'subprocess'
op|'.'
name|'PIPE'
name|'or'
name|'None'
newline|'\n'
name|'kwargs'
op|'['
string|"'universal_newlines'"
op|']'
op|'='
name|'universal_newlines'
newline|'\n'
name|'kwargs'
op|'['
string|"'close_fds'"
op|']'
op|'='
name|'close_fds'
newline|'\n'
name|'kwargs'
op|'['
string|"'env'"
op|']'
op|'='
name|'env'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'proc'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
name|'cmdline'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'errno'
op|'=='
name|'errno'
op|'.'
name|'ENOENT'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'CommandNotFound'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'proc'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SubprocessException
dedent|''
name|'class'
name|'SubprocessException'
op|'('
name|'Exception'
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
name|'cmdline'
op|','
name|'ret'
op|','
name|'out'
op|','
name|'err'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'Exception'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
string|'"\'%s\' returned non-zero exit code: "'
nl|'\n'
string|'"retcode=%i, out=\'%s\', stderr=\'%s\'"'
nl|'\n'
op|'%'
op|'('
name|'cmdline'
op|','
name|'ret'
op|','
name|'out'
op|','
name|'err'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cmdline'
op|'='
name|'cmdline'
newline|'\n'
name|'self'
op|'.'
name|'ret'
op|'='
name|'ret'
newline|'\n'
name|'self'
op|'.'
name|'out'
op|'='
name|'out'
newline|'\n'
name|'self'
op|'.'
name|'err'
op|'='
name|'err'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|finish_subprocess
dedent|''
dedent|''
name|'def'
name|'finish_subprocess'
op|'('
name|'proc'
op|','
name|'cmdline'
op|','
name|'cmd_input'
op|'='
name|'None'
op|','
name|'ok_exit_codes'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Ensure that the process returned a zero exit code indicating success\n    """'
newline|'\n'
name|'if'
name|'ok_exit_codes'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'ok_exit_codes'
op|'='
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'proc'
op|'.'
name|'communicate'
op|'('
name|'cmd_input'
op|')'
newline|'\n'
nl|'\n'
name|'ret'
op|'='
name|'proc'
op|'.'
name|'returncode'
newline|'\n'
name|'if'
name|'ret'
name|'not'
name|'in'
name|'ok_exit_codes'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'SubprocessException'
op|'('
string|"' '"
op|'.'
name|'join'
op|'('
name|'cmdline'
op|')'
op|','
name|'ret'
op|','
name|'out'
op|','
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
newline|'\n'
nl|'\n'
DECL|function|run_command
dedent|''
name|'def'
name|'run_command'
op|'('
name|'cmd'
op|','
name|'cmd_input'
op|'='
name|'None'
op|','
name|'ok_exit_codes'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Abstracts out the basics of issuing system commands. If the command\n    returns anything in stderr, an exception is raised with that information.\n    Otherwise, the output from stdout is returned.\n\n    cmd_input is passed to the process on standard input.\n    """'
newline|'\n'
name|'proc'
op|'='
name|'make_subprocess'
op|'('
name|'cmd'
op|','
name|'stdout'
op|'='
name|'True'
op|','
name|'stderr'
op|'='
name|'True'
op|','
name|'stdin'
op|'='
name|'True'
op|','
nl|'\n'
name|'close_fds'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'finish_subprocess'
op|'('
name|'proc'
op|','
name|'cmd'
op|','
name|'cmd_input'
op|'='
name|'cmd_input'
op|','
nl|'\n'
name|'ok_exit_codes'
op|'='
name|'ok_exit_codes'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_staging_area
dedent|''
name|'def'
name|'make_staging_area'
op|'('
name|'sr_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    The staging area is a place where we can temporarily store and\n    manipulate VHDs. The use of the staging area is different for upload and\n    download:\n\n    Download\n    ========\n\n    When we download the tarball, the VHDs contained within will have names\n    like "snap.vhd" and "image.vhd". We need to assign UUIDs to them before\n    moving them into the SR. However, since \'image.vhd\' may be a base_copy, we\n    need to link it to \'snap.vhd\' (using vhd-util modify) before moving both\n    into the SR (otherwise the SR.scan will cause \'image.vhd\' to be deleted).\n    The staging area gives us a place to perform these operations before they\n    are moved to the SR, scanned, and then registered with XenServer.\n\n    Upload\n    ======\n\n    On upload, we want to rename the VHDs to reflect what they are, \'snap.vhd\'\n    in the case of the snapshot VHD, and \'image.vhd\' in the case of the\n    base_copy. The staging area provides a directory in which we can create\n    hard-links to rename the VHDs without affecting what\'s in the SR.\n\n\n    NOTE\n    ====\n\n    The staging area is created as a subdirectory within the SR in order to\n    guarantee that it resides within the same filesystem and therefore permit\n    hard-linking and cheap file moves.\n    """'
newline|'\n'
name|'staging_path'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
name|'dir'
op|'='
name|'sr_path'
op|')'
newline|'\n'
name|'return'
name|'staging_path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|cleanup_staging_area
dedent|''
name|'def'
name|'cleanup_staging_area'
op|'('
name|'staging_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remove staging area directory\n\n    On upload, the staging area contains hard-links to the VHDs in the SR;\n    it\'s safe to remove the staging-area because the SR will keep the link\n    count > 0 (so the VHDs in the SR will not be deleted).\n    """'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'staging_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'staging_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_handle_old_style_images
dedent|''
dedent|''
name|'def'
name|'_handle_old_style_images'
op|'('
name|'staging_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Rename files to conform to new image format, if needed.\n\n    Old-Style:\n\n        snap.vhd -> image.vhd -> base.vhd\n\n    New-Style:\n\n        0.vhd -> 1.vhd -> ... (n-1).vhd\n\n    The New-Style format has the benefit of being able to support a VDI chain\n    of arbitrary length.\n    """'
newline|'\n'
name|'file_num'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'filename'
name|'in'
op|'('
string|"'snap.vhd'"
op|','
string|"'image.vhd'"
op|','
string|"'base.vhd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
name|'filename'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'_rename'
op|'('
name|'path'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
string|'"%d.vhd"'
op|'%'
name|'file_num'
op|')'
op|')'
newline|'\n'
name|'file_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_assert_vhd_not_hidden
dedent|''
dedent|''
dedent|''
name|'def'
name|'_assert_vhd_not_hidden'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sanity check to ensure that only appropriate VHDs are marked as hidden.\n\n    If this flag is incorrectly set, then when we move the VHD into the SR, it\n    will be deleted out from under us.\n    """'
newline|'\n'
name|'query_cmd'
op|'='
op|'['
string|'"vhd-util"'
op|','
string|'"query"'
op|','
string|'"-n"'
op|','
name|'path'
op|','
string|'"-f"'
op|']'
newline|'\n'
name|'out'
op|'='
name|'run_command'
op|'('
name|'query_cmd'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'line'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'startswith'
op|'('
string|"'hidden'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'value'
op|'=='
string|'"1"'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"VHD %(path)s is marked as hidden without child"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_validate_vhd
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'_validate_vhd'
op|'('
name|'vdi_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This checks for several errors in the VHD structure.\n\n    Most notably, it checks that the timestamp in the footer is correct, but\n    may pick up other errors also.\n\n    This check ensures that the timestamps listed in the VHD footer aren\'t in\n    the future.  This can occur during a migration if the clocks on the the two\n    Dom0\'s are out-of-sync. This would corrupt the SR if it were imported, so\n    generate an exception to bail.\n    """'
newline|'\n'
name|'check_cmd'
op|'='
op|'['
string|'"vhd-util"'
op|','
string|'"check"'
op|','
string|'"-n"'
op|','
name|'vdi_path'
op|','
string|'"-p"'
op|']'
newline|'\n'
name|'out'
op|'='
name|'run_command'
op|'('
name|'check_cmd'
op|','
name|'ok_exit_codes'
op|'='
op|'['
number|'0'
op|','
number|'22'
op|']'
op|')'
newline|'\n'
name|'first_line'
op|'='
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
string|"'invalid'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'footer'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'            '
name|'part'
op|'='
string|"'footer'"
newline|'\n'
dedent|''
name|'elif'
string|"'header'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'            '
name|'part'
op|'='
string|"'header'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'part'
op|'='
string|"'setting'"
newline|'\n'
nl|'\n'
dedent|''
name|'details'
op|'='
name|'first_line'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'details'
op|')'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'            '
name|'details'
op|'='
name|'details'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'details'
op|'='
name|'first_line'
newline|'\n'
nl|'\n'
dedent|''
name|'extra'
op|'='
string|"''"
newline|'\n'
name|'if'
string|"'timestamp'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'            '
name|'extra'
op|'='
op|'('
string|'" ensure source and destination host machines have "'
nl|'\n'
string|'"time set correctly"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"VDI Error details: %s"'
op|'%'
name|'out'
op|')'
newline|'\n'
nl|'\n'
name|'raise'
name|'Exception'
op|'('
nl|'\n'
string|'"VDI \'%(vdi_path)s\' has an invalid %(part)s: \'%(details)s\'"'
nl|'\n'
string|'"%(extra)s"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_validate_vdi_chain
dedent|''
dedent|''
name|'def'
name|'_validate_vdi_chain'
op|'('
name|'vdi_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    This check ensures that the parent pointers on the VHDs are valid\n    before we move the VDI chain to the SR. This is *very* important\n    because a bad parent pointer will corrupt the SR causing a cascade of\n    failures.\n    """'
newline|'\n'
DECL|function|get_parent_path
name|'def'
name|'get_parent_path'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'query_cmd'
op|'='
op|'['
string|'"vhd-util"'
op|','
string|'"query"'
op|','
string|'"-n"'
op|','
name|'path'
op|','
string|'"-p"'
op|']'
newline|'\n'
name|'out'
op|'='
name|'run_command'
op|'('
name|'query_cmd'
op|','
name|'ok_exit_codes'
op|'='
op|'['
number|'0'
op|','
number|'22'
op|']'
op|')'
newline|'\n'
name|'first_line'
op|'='
name|'out'
op|'.'
name|'splitlines'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'first_line'
op|'.'
name|'endswith'
op|'('
string|'".vhd"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'first_line'
newline|'\n'
dedent|''
name|'elif'
string|"'has no parent'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
string|"'query failed'"
name|'in'
name|'first_line'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"VDI \'%(path)s\' not present which breaks"'
nl|'\n'
string|'" the VDI chain, bailing out"'
op|'%'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Unexpected output \'%(out)s\' from vhd-util"'
op|'%'
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'cur_path'
op|'='
name|'vdi_path'
newline|'\n'
name|'while'
name|'cur_path'
op|':'
newline|'\n'
indent|'        '
name|'_validate_vhd'
op|'('
name|'cur_path'
op|')'
newline|'\n'
name|'cur_path'
op|'='
name|'get_parent_path'
op|'('
name|'cur_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_validate_sequenced_vhds
dedent|''
dedent|''
name|'def'
name|'_validate_sequenced_vhds'
op|'('
name|'staging_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This check ensures that the VHDs in the staging area are sequenced\n    properly from 0 to n-1 with no gaps.\n    """'
newline|'\n'
name|'seq_num'
op|'='
number|'0'
newline|'\n'
name|'filenames'
op|'='
name|'os'
op|'.'
name|'listdir'
op|'('
name|'staging_path'
op|')'
newline|'\n'
name|'for'
name|'filename'
name|'in'
name|'filenames'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'filename'
op|'.'
name|'endswith'
op|'('
string|"'.vhd'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# Ignore legacy swap embedded in the image, generated on-the-fly now'
nl|'\n'
dedent|''
name|'if'
name|'filename'
op|'=='
string|'"swap.vhd"'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
string|'"%d.vhd"'
op|'%'
name|'seq_num'
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
name|'vhd_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
string|'"Corrupt image. Expected seq number: %d. Files: %s"'
nl|'\n'
op|'%'
op|'('
name|'seq_num'
op|','
name|'filenames'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'seq_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|import_vhds
dedent|''
dedent|''
name|'def'
name|'import_vhds'
op|'('
name|'sr_path'
op|','
name|'staging_path'
op|','
name|'uuid_stack'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Move VHDs from staging area into the SR.\n\n    The staging area is necessary because we need to perform some fixups\n    (assigning UUIDs, relinking the VHD chain) before moving into the SR,\n    otherwise the SR manager process could potentially delete the VHDs out from\n    under us.\n\n    Returns: A dict of imported VHDs:\n\n        {\'root\': {\'uuid\': \'ffff-aaaa\'}}\n    """'
newline|'\n'
name|'_handle_old_style_images'
op|'('
name|'staging_path'
op|')'
newline|'\n'
name|'_validate_sequenced_vhds'
op|'('
name|'staging_path'
op|')'
newline|'\n'
nl|'\n'
name|'files_to_move'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|'# Collect sequenced VHDs and assign UUIDs to them'
nl|'\n'
name|'seq_num'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'orig_vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
string|'"%d.vhd"'
op|'%'
name|'seq_num'
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
name|'orig_vhd_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
nl|'\n'
comment|'# Rename (0, 1 .. N).vhd -> aaaa-bbbb-cccc-dddd.vhd'
nl|'\n'
dedent|''
name|'vhd_uuid'
op|'='
name|'uuid_stack'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'vhd_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
string|'"%s.vhd"'
op|'%'
name|'vhd_uuid'
op|')'
newline|'\n'
name|'_rename'
op|'('
name|'orig_vhd_path'
op|','
name|'vhd_path'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'seq_num'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'leaf_vhd_path'
op|'='
name|'vhd_path'
newline|'\n'
name|'leaf_vhd_uuid'
op|'='
name|'vhd_uuid'
newline|'\n'
nl|'\n'
dedent|''
name|'files_to_move'
op|'.'
name|'append'
op|'('
name|'vhd_path'
op|')'
newline|'\n'
name|'seq_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
comment|'# Re-link VHDs, in reverse order, from base-copy -> leaf'
nl|'\n'
dedent|''
name|'parent_path'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'vhd_path'
name|'in'
name|'reversed'
op|'('
name|'files_to_move'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'parent_path'
op|':'
newline|'\n'
comment|'# Link to parent'
nl|'\n'
indent|'            '
name|'modify_cmd'
op|'='
op|'['
string|'"vhd-util"'
op|','
string|'"modify"'
op|','
string|'"-n"'
op|','
name|'vhd_path'
op|','
nl|'\n'
string|'"-p"'
op|','
name|'parent_path'
op|']'
newline|'\n'
name|'run_command'
op|'('
name|'modify_cmd'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'parent_path'
op|'='
name|'vhd_path'
newline|'\n'
nl|'\n'
comment|'# Sanity check the leaf VHD'
nl|'\n'
dedent|''
name|'_assert_vhd_not_hidden'
op|'('
name|'leaf_vhd_path'
op|')'
newline|'\n'
name|'_validate_vdi_chain'
op|'('
name|'leaf_vhd_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Move files into SR'
nl|'\n'
name|'for'
name|'orig_path'
name|'in'
name|'files_to_move'
op|':'
newline|'\n'
indent|'        '
name|'new_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'sr_path'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'orig_path'
op|')'
op|')'
newline|'\n'
name|'_rename'
op|'('
name|'orig_path'
op|','
name|'new_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'imported_vhds'
op|'='
name|'dict'
op|'('
name|'root'
op|'='
name|'dict'
op|'('
name|'uuid'
op|'='
name|'leaf_vhd_uuid'
op|')'
op|')'
newline|'\n'
name|'return'
name|'imported_vhds'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|prepare_staging_area
dedent|''
name|'def'
name|'prepare_staging_area'
op|'('
name|'sr_path'
op|','
name|'staging_path'
op|','
name|'vdi_uuids'
op|','
name|'seq_num'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Hard-link VHDs into staging area."""'
newline|'\n'
name|'for'
name|'vdi_uuid'
name|'in'
name|'vdi_uuids'
op|':'
newline|'\n'
indent|'        '
name|'source'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'sr_path'
op|','
string|'"%s.vhd"'
op|'%'
name|'vdi_uuid'
op|')'
newline|'\n'
name|'link_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'staging_path'
op|','
string|'"%d.vhd"'
op|'%'
name|'seq_num'
op|')'
newline|'\n'
name|'_link'
op|'('
name|'source'
op|','
name|'link_name'
op|')'
newline|'\n'
name|'seq_num'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_tarball
dedent|''
dedent|''
name|'def'
name|'create_tarball'
op|'('
name|'fileobj'
op|','
name|'path'
op|','
name|'callback'
op|'='
name|'None'
op|','
name|'compression_level'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a tarball from a given path.\n\n    :param fileobj: a file-like object holding the tarball byte-stream.\n                    If None, then only the callback will be used.\n    :param path: path to create tarball from\n    :param callback: optional callback to call on each chunk written\n    :param compression_level: compression level, e.g., 9 for gzip -9.\n    """'
newline|'\n'
name|'tar_cmd'
op|'='
op|'['
string|'"tar"'
op|','
string|'"-zc"'
op|','
string|'"--directory=%s"'
op|'%'
name|'path'
op|','
string|'"."'
op|']'
newline|'\n'
name|'env'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
name|'if'
name|'compression_level'
name|'and'
number|'1'
op|'<='
name|'compression_level'
op|'<='
number|'9'
op|':'
newline|'\n'
indent|'        '
name|'env'
op|'['
string|'"GZIP"'
op|']'
op|'='
string|'"-%d"'
op|'%'
name|'compression_level'
newline|'\n'
dedent|''
name|'tar_proc'
op|'='
name|'make_subprocess'
op|'('
name|'tar_cmd'
op|','
name|'stdout'
op|'='
name|'True'
op|','
name|'stderr'
op|'='
name|'True'
op|','
name|'env'
op|'='
name|'env'
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'chunk'
op|'='
name|'tar_proc'
op|'.'
name|'stdout'
op|'.'
name|'read'
op|'('
name|'CHUNK_SIZE'
op|')'
newline|'\n'
name|'if'
name|'chunk'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'callback'
op|':'
newline|'\n'
indent|'            '
name|'callback'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'fileobj'
op|':'
newline|'\n'
indent|'            '
name|'fileobj'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'finish_subprocess'
op|'('
name|'tar_proc'
op|','
name|'tar_cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_tarball
dedent|''
name|'def'
name|'extract_tarball'
op|'('
name|'fileobj'
op|','
name|'path'
op|','
name|'callback'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract a tarball to a given path.\n\n    :param fileobj: a file-like object holding the tarball byte-stream\n    :param path: path to extract tarball into\n    :param callback: optional callback to call on each chunk read\n    """'
newline|'\n'
name|'tar_cmd'
op|'='
op|'['
string|'"tar"'
op|','
string|'"-zx"'
op|','
string|'"--directory=%s"'
op|'%'
name|'path'
op|']'
newline|'\n'
name|'tar_proc'
op|'='
name|'make_subprocess'
op|'('
name|'tar_cmd'
op|','
name|'stderr'
op|'='
name|'True'
op|','
name|'stdin'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'while'
name|'True'
op|':'
newline|'\n'
indent|'        '
name|'chunk'
op|'='
name|'fileobj'
op|'.'
name|'read'
op|'('
name|'CHUNK_SIZE'
op|')'
newline|'\n'
name|'if'
name|'chunk'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'            '
name|'break'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'callback'
op|':'
newline|'\n'
indent|'            '
name|'callback'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'tar_proc'
op|'.'
name|'stdin'
op|'.'
name|'write'
op|'('
name|'chunk'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'finish_subprocess'
op|'('
name|'tar_proc'
op|','
name|'tar_cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_handle_serialization
dedent|''
name|'def'
name|'_handle_serialization'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
DECL|function|wrapped
indent|'    '
name|'def'
name|'wrapped'
op|'('
name|'session'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'pickle'
op|'.'
name|'loads'
op|'('
name|'params'
op|'['
string|"'params'"
op|']'
op|')'
newline|'\n'
name|'rv'
op|'='
name|'func'
op|'('
name|'session'
op|','
op|'*'
name|'params'
op|'['
string|"'args'"
op|']'
op|','
op|'**'
name|'params'
op|'['
string|"'kwargs'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'pickle'
op|'.'
name|'dumps'
op|'('
name|'rv'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_plugin_calls
dedent|''
name|'def'
name|'register_plugin_calls'
op|'('
op|'*'
name|'funcs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around XenAPIPlugin.dispatch which handles pickle\n    serialization.\n    """'
newline|'\n'
name|'wrapped_dict'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'func'
name|'in'
name|'funcs'
op|':'
newline|'\n'
indent|'        '
name|'wrapped_dict'
op|'['
name|'func'
op|'.'
name|'__name__'
op|']'
op|'='
name|'_handle_serialization'
op|'('
name|'func'
op|')'
newline|'\n'
dedent|''
name|'XenAPIPlugin'
op|'.'
name|'dispatch'
op|'('
name|'wrapped_dict'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
