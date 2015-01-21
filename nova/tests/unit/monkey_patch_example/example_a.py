begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""Example Module A for testing utils.monkey_patch()."""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|example_function_a
name|'def'
name|'example_function_a'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'Example function'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExampleClassA
dedent|''
name|'class'
name|'ExampleClassA'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|example_method
indent|'    '
name|'def'
name|'example_method'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'Example method'"
newline|'\n'
nl|'\n'
DECL|member|example_method_add
dedent|''
name|'def'
name|'example_method_add'
op|'('
name|'self'
op|','
name|'arg1'
op|','
name|'arg2'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'arg1'
op|'+'
name|'arg2'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
