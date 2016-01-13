begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
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
string|'"""\nThis is the single point of entry to generate the sample configuration\nfile for Nova. It collects all the necessary info from the other modules\nin this package. It is assumed that:\n* every other module in this package has a \'list_opts\' function which\n  return a dict where\n   * the keys are strings which are the group names\n   * the value of each key is a list of config options for that group\n* the nova.conf package doesn\'t have further packages with config options\n* this module is only used in the context of sample file generation\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
name|'import'
name|'importlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'pkgutil'
newline|'\n'
nl|'\n'
DECL|variable|LIST_OPTS_FUNC_NAME
name|'LIST_OPTS_FUNC_NAME'
op|'='
string|'"list_opts"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_tupleize
name|'def'
name|'_tupleize'
op|'('
name|'dct'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Take the dict of options and convert to the 2-tuple format."""'
newline|'\n'
name|'return'
op|'['
op|'('
name|'key'
op|','
name|'val'
op|')'
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'dct'
op|'.'
name|'items'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'opts'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'module_names'
op|'='
name|'_list_module_names'
op|'('
op|')'
newline|'\n'
name|'imported_modules'
op|'='
name|'_import_modules'
op|'('
name|'module_names'
op|')'
newline|'\n'
name|'_append_config_options'
op|'('
name|'imported_modules'
op|','
name|'opts'
op|')'
newline|'\n'
name|'return'
name|'_tupleize'
op|'('
name|'opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_list_module_names
dedent|''
name|'def'
name|'_list_module_names'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'module_names'
op|'='
op|'['
op|']'
newline|'\n'
name|'package_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
newline|'\n'
name|'for'
name|'_'
op|','
name|'modname'
op|','
name|'ispkg'
name|'in'
name|'pkgutil'
op|'.'
name|'iter_modules'
op|'('
name|'path'
op|'='
op|'['
name|'package_path'
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'modname'
op|'=='
string|'"opts"'
name|'or'
name|'ispkg'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'module_names'
op|'.'
name|'append'
op|'('
name|'modname'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'module_names'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_import_modules
dedent|''
name|'def'
name|'_import_modules'
op|'('
name|'module_names'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'imported_modules'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'modname'
name|'in'
name|'module_names'
op|':'
newline|'\n'
indent|'        '
name|'mod'
op|'='
name|'importlib'
op|'.'
name|'import_module'
op|'('
string|'"nova.conf."'
op|'+'
name|'modname'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'mod'
op|','
name|'LIST_OPTS_FUNC_NAME'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'"The module \'nova.conf.%s\' should have a \'%s\' "'
string|'"function which returns the config options."'
op|'%'
op|'('
name|'modname'
op|','
name|'LIST_OPTS_FUNC_NAME'
op|')'
newline|'\n'
name|'raise'
name|'Exception'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'imported_modules'
op|'.'
name|'append'
op|'('
name|'mod'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'imported_modules'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_process_old_opts
dedent|''
name|'def'
name|'_process_old_opts'
op|'('
name|'configs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert old-style 2-tuple configs to dicts."""'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'configs'
op|','
name|'tuple'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'configs'
op|'='
op|'['
name|'configs'
op|']'
newline|'\n'
dedent|''
name|'return'
op|'{'
name|'label'
op|':'
name|'options'
name|'for'
name|'label'
op|','
name|'options'
name|'in'
name|'configs'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_append_config_options
dedent|''
name|'def'
name|'_append_config_options'
op|'('
name|'imported_modules'
op|','
name|'config_options'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'mod'
name|'in'
name|'imported_modules'
op|':'
newline|'\n'
indent|'        '
name|'configs'
op|'='
name|'mod'
op|'.'
name|'list_opts'
op|'('
op|')'
newline|'\n'
comment|'# TODO(markus_z): Remove this compatibility shim once all list_opts()'
nl|'\n'
comment|'# functions have been updated to return dicts.'
nl|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'configs'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'configs'
op|'='
name|'_process_old_opts'
op|'('
name|'configs'
op|')'
newline|'\n'
dedent|''
name|'for'
name|'key'
op|','
name|'val'
name|'in'
name|'configs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'config_options'
op|'['
name|'key'
op|']'
op|'.'
name|'extend'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
