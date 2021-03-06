begin_unit
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
name|'from'
name|'nova'
op|'.'
name|'scheduler'
op|'.'
name|'filters'
name|'import'
name|'extra_specs_ops'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtraSpecsOpsTestCase
name|'class'
name|'ExtraSpecsOpsTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_do_extra_specs_ops_test
indent|'    '
name|'def'
name|'_do_extra_specs_ops_test'
op|'('
name|'self'
op|','
name|'value'
op|','
name|'req'
op|','
name|'matches'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'assertion'
op|'='
name|'self'
op|'.'
name|'assertTrue'
name|'if'
name|'matches'
name|'else'
name|'self'
op|'.'
name|'assertFalse'
newline|'\n'
name|'assertion'
op|'('
name|'extra_specs_ops'
op|'.'
name|'match'
op|'('
name|'value'
op|','
name|'req'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_simple
dedent|''
name|'def'
name|'test_extra_specs_matches_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'1'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'1'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_simple
dedent|''
name|'def'
name|'test_extra_specs_fails_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"''"
op|','
nl|'\n'
name|'req'
op|'='
string|"'1'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_simple2
dedent|''
name|'def'
name|'test_extra_specs_fails_simple2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'3'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'1'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_simple3
dedent|''
name|'def'
name|'test_extra_specs_fails_simple3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'222'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'2'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_bogus_ops
dedent|''
name|'def'
name|'test_extra_specs_fails_with_bogus_ops'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'4'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'> 2'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_eq
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_eq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'123'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'= 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_eq2
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_eq2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'124'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'= 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_eq
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_eq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'34'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'= 234'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_eq3
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_eq3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'34'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'='"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_seq
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_seq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'123'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s== 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_seq
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_seq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'1234'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s== 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_sneq
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_sneq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'1234'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s!= 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_sneq
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_sneq'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'123'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s!= 123'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_sge
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_sge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'1000'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s>= 234'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_sle
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_sle'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'1234'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s<= 1000'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_sl
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_sl'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'2'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s< 12'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_sg
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_sg'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'s> 2'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_in
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_in'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12311321'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<in> 11'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_in2
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_in2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12311321'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<in> 12311321'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_in3
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_in3'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12311321'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<in> 12311321 <in>'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_in
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_in'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12310321'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<in> 11'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_in2
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_in2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12310321'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<in> 11 <in>'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_or
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_or'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<or> 11 <or> 12'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_or2
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_or2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'12'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<or> 11 <or> 12 <or>'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_or
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_or'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'13'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<or> 11 <or> 12'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_or2
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_or2'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'13'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<or> 11 <or> 12 <or>'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_le
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_le'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'2'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<= 10'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_le
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_le'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'3'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'<= 2'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_with_op_ge
dedent|''
name|'def'
name|'test_extra_specs_matches_with_op_ge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'3'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'>= 1'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_ge
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_ge'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
string|"'2'"
op|','
nl|'\n'
name|'req'
op|'='
string|"'>= 3'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_all_with_op_allin
dedent|''
name|'def'
name|'test_extra_specs_matches_all_with_op_allin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'['
string|"'aes'"
op|','
string|"'mmx'"
op|','
string|"'aux'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
name|'str'
op|'('
name|'values'
op|')'
op|','
nl|'\n'
name|'req'
op|'='
string|"'<all-in> aes mmx'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_matches_one_with_op_allin
dedent|''
name|'def'
name|'test_extra_specs_matches_one_with_op_allin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'['
string|"'aes'"
op|','
string|"'mmx'"
op|','
string|"'aux'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
name|'str'
op|'('
name|'values'
op|')'
op|','
nl|'\n'
name|'req'
op|'='
string|"'<all-in> mmx'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_with_op_allin
dedent|''
name|'def'
name|'test_extra_specs_fails_with_op_allin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'['
string|"'aes'"
op|','
string|"'mmx'"
op|','
string|"'aux'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
name|'str'
op|'('
name|'values'
op|')'
op|','
nl|'\n'
name|'req'
op|'='
string|"'<all-in>  txt'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_all_with_op_allin
dedent|''
name|'def'
name|'test_extra_specs_fails_all_with_op_allin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'['
string|"'aes'"
op|','
string|"'mmx'"
op|','
string|"'aux'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
name|'str'
op|'('
name|'values'
op|')'
op|','
nl|'\n'
name|'req'
op|'='
string|"'<all-in> txt 3dnow'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_extra_specs_fails_match_one_with_op_allin
dedent|''
name|'def'
name|'test_extra_specs_fails_match_one_with_op_allin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'values'
op|'='
op|'['
string|"'aes'"
op|','
string|"'mmx'"
op|','
string|"'aux'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_do_extra_specs_ops_test'
op|'('
nl|'\n'
name|'value'
op|'='
name|'str'
op|'('
name|'values'
op|')'
op|','
nl|'\n'
name|'req'
op|'='
string|"'<all-in> txt aes'"
op|','
nl|'\n'
name|'matches'
op|'='
name|'False'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
