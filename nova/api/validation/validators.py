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
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'import'
name|'jsonschema'
newline|'\n'
name|'from'
name|'jsonschema'
name|'import'
name|'exceptions'
name|'as'
name|'jsonschema_exc'
newline|'\n'
name|'import'
name|'netaddr'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
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
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
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
string|"'cidr'"
op|')'
newline|'\n'
DECL|function|_validate_cidr_format
name|'def'
name|'_validate_cidr_format'
op|'('
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'netaddr'
op|'.'
name|'IPNetwork'
op|'('
name|'cidr'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'netaddr'
op|'.'
name|'AddrFormatError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
string|"'/'"
name|'not'
name|'in'
name|'cidr'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
string|"'\\s'"
op|','
name|'cidr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
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
dedent|''
op|'@'
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|'.'
name|'cls_checks'
op|'('
string|"'name_with_leading_trailing_spaces'"
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidName'
op|')'
newline|'\n'
DECL|function|_validate_name_with_leading_trailing_spaces
name|'def'
name|'_validate_name_with_leading_trailing_spaces'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'regex'
op|'='
name|'parameter_types'
op|'.'
name|'valid_name_leading_trailing_spaces_regex'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
name|'regex'
op|'.'
name|'regex'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|"# The name must be string type. If instance isn't string type, the"
nl|'\n'
comment|'# TypeError will be raised at here.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InvalidName'
op|'('
name|'reason'
op|'='
name|'regex'
op|'.'
name|'reason'
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
string|"'name'"
op|','
name|'exception'
op|'.'
name|'InvalidName'
op|')'
newline|'\n'
DECL|function|_validate_name
name|'def'
name|'_validate_name'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'regex'
op|'='
name|'parameter_types'
op|'.'
name|'valid_name_regex'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
name|'regex'
op|'.'
name|'regex'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|"# The name must be string type. If instance isn't string type, the"
nl|'\n'
comment|'# TypeError will be raised at here.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InvalidName'
op|'('
name|'reason'
op|'='
name|'regex'
op|'.'
name|'reason'
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
string|"'cell_name_with_leading_trailing_spaces'"
op|','
nl|'\n'
name|'exception'
op|'.'
name|'InvalidName'
op|')'
newline|'\n'
DECL|function|_validate_cell_name_with_leading_trailing_spaces
name|'def'
name|'_validate_cell_name_with_leading_trailing_spaces'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'regex'
op|'='
name|'parameter_types'
op|'.'
name|'valid_cell_name_leading_trailing_spaces_regex'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
name|'regex'
op|'.'
name|'regex'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|"# The name must be string type. If instance isn't string type, the"
nl|'\n'
comment|'# TypeError will be raised at here.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InvalidName'
op|'('
name|'reason'
op|'='
name|'regex'
op|'.'
name|'reason'
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
string|"'cell_name'"
op|','
name|'exception'
op|'.'
name|'InvalidName'
op|')'
newline|'\n'
DECL|function|_validate_cell_name
name|'def'
name|'_validate_cell_name'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'regex'
op|'='
name|'parameter_types'
op|'.'
name|'valid_cell_name_regex'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
name|'regex'
op|'.'
name|'regex'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'TypeError'
op|':'
newline|'\n'
comment|"# The name must be string type. If instance isn't string type, the"
nl|'\n'
comment|'# TypeError will be raised at here.'
nl|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'InvalidName'
op|'('
name|'reason'
op|'='
name|'regex'
op|'.'
name|'reason'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_soft_validate_additional_properties
dedent|''
name|'def'
name|'_soft_validate_additional_properties'
op|'('
name|'validator'
op|','
nl|'\n'
name|'additional_properties_value'
op|','
nl|'\n'
name|'instance'
op|','
nl|'\n'
name|'schema'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""This validator function is used for legacy v2 compatible mode in v2.1.\n    This will skip all the additional properties checking but keep check the\n    \'patternProperties\'. \'patternProperties\' is used for metadata API.\n\n    If there are not any properties on the instance that are not specified in\n    the schema, this will return without any effect. If there are any such\n    extra properties, they will be handled as follows:\n\n    - if the validator passed to the method is not of type "object", this\n      method will return without any effect.\n    - if the \'additional_properties_value\' parameter is True, this method will\n      return without any effect.\n    - if the schema has an additionalProperties value of True, the extra\n      properties on the instance will not be touched.\n    - if the schema has an additionalProperties value of False and there\n      aren\'t patternProperties specified, the extra properties will be stripped\n      from the instance.\n    - if the schema has an additionalProperties value of False and there\n      are patternProperties specified, the extra properties will not be\n      touched and raise validation error if pattern doesn\'t match.\n    """'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'validator'
op|'.'
name|'is_type'
op|'('
name|'instance'
op|','
string|'"object"'
op|')'
name|'or'
nl|'\n'
name|'additional_properties_value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'properties'
op|'='
name|'schema'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'patterns'
op|'='
string|'"|"'
op|'.'
name|'join'
op|'('
name|'schema'
op|'.'
name|'get'
op|'('
string|'"patternProperties"'
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
name|'extra_properties'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'prop'
name|'in'
name|'instance'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'prop'
name|'not'
name|'in'
name|'properties'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'patterns'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'re'
op|'.'
name|'search'
op|'('
name|'patterns'
op|','
name|'prop'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'extra_properties'
op|'.'
name|'add'
op|'('
name|'prop'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'extra_properties'
op|'.'
name|'add'
op|'('
name|'prop'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'not'
name|'extra_properties'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'patterns'
op|':'
newline|'\n'
indent|'        '
name|'error'
op|'='
string|'"Additional properties are not allowed (%s %s unexpected)"'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'extra_properties'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'verb'
op|'='
string|'"was"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'verb'
op|'='
string|'"were"'
newline|'\n'
dedent|''
name|'yield'
name|'jsonschema_exc'
op|'.'
name|'ValidationError'
op|'('
nl|'\n'
name|'error'
op|'%'
op|'('
string|'", "'
op|'.'
name|'join'
op|'('
name|'repr'
op|'('
name|'extra'
op|')'
name|'for'
name|'extra'
name|'in'
name|'extra_properties'
op|')'
op|','
nl|'\n'
name|'verb'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'prop'
name|'in'
name|'extra_properties'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'instance'
op|'['
name|'prop'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FormatChecker
dedent|''
dedent|''
dedent|''
name|'class'
name|'FormatChecker'
op|'('
name|'jsonschema'
op|'.'
name|'FormatChecker'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A FormatChecker can output the message from cause exception\n\n       We need understandable validation errors messages for users. When a\n       custom checker has an exception, the FormatChecker will output a\n       readable message provided by the checker.\n    """'
newline|'\n'
nl|'\n'
DECL|member|check
name|'def'
name|'check'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'format'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check whether the instance conforms to the given format.\n\n        :argument instance: the instance to check\n        :type: any primitive type (str, number, bool)\n        :argument str format: the format that instance should conform to\n        :raises: :exc:`FormatError` if instance does not conform to format\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'format'
name|'not'
name|'in'
name|'self'
op|'.'
name|'checkers'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
comment|'# For safety reasons custom checkers can be registered with'
nl|'\n'
comment|'# allowed exception types. Anything else will fall into the'
nl|'\n'
comment|'# default formatter.'
nl|'\n'
dedent|''
name|'func'
op|','
name|'raises'
op|'='
name|'self'
op|'.'
name|'checkers'
op|'['
name|'format'
op|']'
newline|'\n'
name|'result'
op|','
name|'cause'
op|'='
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'func'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'raises'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'cause'
op|'='
name|'e'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'result'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
string|'"%r is not a %r"'
op|'%'
op|'('
name|'instance'
op|','
name|'format'
op|')'
newline|'\n'
name|'raise'
name|'jsonschema_exc'
op|'.'
name|'FormatError'
op|'('
name|'msg'
op|','
name|'cause'
op|'='
name|'cause'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_SchemaValidator
dedent|''
dedent|''
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
op|','
name|'relax_additional_properties'
op|'='
name|'False'
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
name|'if'
name|'relax_additional_properties'
op|':'
newline|'\n'
indent|'            '
name|'validators'
op|'['
nl|'\n'
string|"'additionalProperties'"
op|']'
op|'='
name|'_soft_validate_additional_properties'
newline|'\n'
nl|'\n'
dedent|''
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
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'ex'
op|'.'
name|'cause'
op|','
name|'exception'
op|'.'
name|'InvalidName'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'detail'
op|'='
name|'ex'
op|'.'
name|'cause'
op|'.'
name|'format_message'
op|'('
op|')'
newline|'\n'
dedent|''
name|'elif'
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
comment|'# NOTE: For whole OpenStack message consistency, this error'
nl|'\n'
comment|'#       message has been written as the similar format of WSME.'
nl|'\n'
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
