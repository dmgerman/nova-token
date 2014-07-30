begin_unit
comment|'# Copyright 2013 NEC Corporation.  All rights reserved.'
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
string|'"""\nInternal implementation of request Body validating middleware.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
nl|'\n'
name|'import'
name|'jsonschema'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'import'
name|'rfc3986'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'uuidutils'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'.'
name|'cls_checks'
op|'('
string|"'date-time'"
op|')'
newline|'\n'
DECL|function|_validate_datetime_format
name|'def'
name|'_validate_datetime_format'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'parse_isotime'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'.'
name|'cls_checks'
op|'('
string|"'base64'"
op|')'
newline|'\n'
DECL|function|_validate_base64_format
name|'def'
name|'_validate_base64_format'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'base64'
op|'.'
name|'decodestring'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'base64'
op|'.'
name|'binascii'
op|'.'
name|'Error'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'.'
name|'cls_checks'
op|'('
string|"'uuid'"
op|')'
newline|'\n'
DECL|function|_validate_uuid_format
name|'def'
name|'_validate_uuid_format'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'.'
name|'cls_checks'
op|'('
string|"'uri'"
op|')'
newline|'\n'
DECL|function|_validate_uri
name|'def'
name|'_validate_uri'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'rfc3986'
op|'.'
name|'is_valid_uri'
op|'('
name|'instance'
op|','
name|'require_scheme'
op|'='
name|'True'
op|','
nl|'\n'
name|'require_authority'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_SchemaValidator
dedent|''
name|'class'
name|'_SchemaValidator'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A validator class\n\n    This class is changed from Draft4Validator to validate minimum/maximum\n    value of a string number(e.g. \'10\'). This changes can be removed when\n    we tighten up the API definition and the XML conversion.\n    Also FormatCheckers are added for checking data formats which would be\n    passed through nova api commonly.\n\n    """'
newline|'\n'
DECL|variable|validator
name|'validator'
op|'='
name|'None'
newline|'\n'
DECL|variable|validator_org
name|'validator_org'
op|'='
name|'jsonschema'
op|'.'
name|'Draft4Validator'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'schema'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'validators'
op|'='
op|'{'
nl|'\n'
string|"'minimum'"
op|':'
name|'self'
op|'.'
name|'_validate_minimum'
op|','
nl|'\n'
string|"'maximum'"
op|':'
name|'self'
op|'.'
name|'_validate_maximum'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'validator_cls'
op|'='
name|'jsonschema'
op|'.'
name|'validators'
op|'.'
name|'extend'
op|'('
name|'self'
op|'.'
name|'validator_org'
op|','
nl|'\n'
name|'validators'
op|')'
newline|'\n'
name|'format_checker'
op|'='
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'validator'
op|'='
name|'validator_cls'
op|'('
name|'schema'
op|','
name|'format_checker'
op|'='
name|'format_checker'
op|')'
newline|'\n'
nl|'\n'
DECL|member|validate
dedent|''
name|'def'
name|'validate'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'validator'
op|'.'
name|'validate'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'jsonschema'
op|'.'
name|'ValidationError'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|'# NOTE: For whole OpenStack message consistency, this error'
nl|'\n'
comment|'#       message has been written as the similar format of WSME.'
nl|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'ex'
op|'.'
name|'path'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'detail'
op|'='
name|'_'
op|'('
string|'"Invalid input for field/attribute %(path)s."'
nl|'\n'
string|'" Value: %(value)s. %(message)s"'
op|')'
op|'%'
op|'{'
nl|'\n'
string|"'path'"
op|':'
name|'ex'
op|'.'
name|'path'
op|'.'
name|'pop'
op|'('
op|')'
op|','
string|"'value'"
op|':'
name|'ex'
op|'.'
name|'instance'
op|','
nl|'\n'
string|"'message'"
op|':'
name|'ex'
op|'.'
name|'message'
nl|'\n'
op|'}'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'detail'
op|'='
name|'ex'
op|'.'
name|'message'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'ValidationError'
op|'('
name|'detail'
op|'='
name|'detail'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|'# NOTE: If passing non string value to patternProperties parameter,'
nl|'\n'
comment|'#       TypeError happens. Here is for catching the TypeError.'
nl|'\n'
indent|'            '
name|'detail'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'ex'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ValidationError'
op|'('
name|'detail'
op|'='
name|'detail'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_number_from_str
dedent|''
dedent|''
name|'def'
name|'_number_from_str'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'int'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'float'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
DECL|member|_validate_minimum
dedent|''
name|'def'
name|'_validate_minimum'
op|'('
name|'self'
op|','
name|'validator'
op|','
name|'minimum'
op|','
name|'instance'
op|','
name|'schema'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_number_from_str'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'validator_org'
op|'.'
name|'VALIDATORS'
op|'['
string|"'minimum'"
op|']'
op|'('
name|'validator'
op|','
name|'minimum'
op|','
nl|'\n'
name|'instance'
op|','
name|'schema'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_validate_maximum
dedent|''
name|'def'
name|'_validate_maximum'
op|'('
name|'self'
op|','
name|'validator'
op|','
name|'maximum'
op|','
name|'instance'
op|','
name|'schema'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'self'
op|'.'
name|'_number_from_str'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'instance'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'validator_org'
op|'.'
name|'VALIDATORS'
op|'['
string|"'maximum'"
op|']'
op|'('
name|'validator'
op|','
name|'maximum'
op|','
nl|'\n'
name|'instance'
op|','
name|'schema'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
