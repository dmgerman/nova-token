begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExampleSkipTestCase
name|'class'
name|'ExampleSkipTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'test'
op|'.'
name|'skip_test'
op|'('
string|'"testing skipping"'
op|')'
newline|'\n'
DECL|member|test_skip_test
name|'def'
name|'test_skip_test'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'os'
op|'.'
name|'getenv'
op|'('
string|'"USER"'
op|')'
op|','
nl|'\n'
string|'"Skiping -- Environment variable USER exists"'
op|')'
newline|'\n'
DECL|member|test_skip_if_env_user_exists
name|'def'
name|'test_skip_if_env_user_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_unless'
op|'('
name|'os'
op|'.'
name|'getenv'
op|'('
string|'"FOO"'
op|')'
op|','
nl|'\n'
string|'"Skipping -- Environment variable FOO does not exist"'
op|')'
newline|'\n'
DECL|member|test_skip_unless_env_foo_exists
name|'def'
name|'test_skip_unless_env_foo_exists'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'x'
op|'='
number|'1'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
