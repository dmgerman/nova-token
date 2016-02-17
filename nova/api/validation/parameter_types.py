begin_unit
comment|'# Copyright 2014 NEC Corporation.  All rights reserved.'
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
string|'"""\nCommon parameter types for validating request Body.\n\n"""'
newline|'\n'
name|'import'
name|'copy'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'unicodedata'
newline|'\n'
nl|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ValidationRegex
name|'class'
name|'ValidationRegex'
op|'('
name|'object'
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
name|'regex'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'regex'
op|'='
name|'regex'
newline|'\n'
name|'self'
op|'.'
name|'reason'
op|'='
name|'reason'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_is_printable
dedent|''
dedent|''
name|'def'
name|'_is_printable'
op|'('
name|'char'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""determine if a unicode code point is printable.\n\n    This checks if the character is either "other" (mostly control\n    codes), or a non-horizontal space. All characters that don\'t match\n    those criteria are considered printable; that is: letters;\n    combining marks; numbers; punctuation; symbols; (horizontal) space\n    separators.\n    """'
newline|'\n'
name|'category'
op|'='
name|'unicodedata'
op|'.'
name|'category'
op|'('
name|'char'
op|')'
newline|'\n'
name|'return'
op|'('
name|'not'
name|'category'
op|'.'
name|'startswith'
op|'('
string|'"C"'
op|')'
name|'and'
nl|'\n'
op|'('
name|'not'
name|'category'
op|'.'
name|'startswith'
op|'('
string|'"Z"'
op|')'
name|'or'
name|'category'
op|'=='
string|'"Zs"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_all_chars
dedent|''
name|'def'
name|'_get_all_chars'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'0xFFFF'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'yield'
name|'six'
op|'.'
name|'unichr'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# build a regex that matches all printable characters. This allows'
nl|'\n'
comment|'# spaces in the middle of the name. Also note that the regexp below'
nl|'\n'
comment|'# deliberately allows the empty string. This is so only the constraint'
nl|'\n'
comment|'# which enforces a minimum length for the name is triggered when an'
nl|'\n'
comment|'# empty string is tested. Otherwise it is not deterministic which'
nl|'\n'
comment|'# constraint fails and this causes issues for some unittests when'
nl|'\n'
comment|'# PYTHONHASHSEED is set randomly.'
nl|'\n'
nl|'\n'
DECL|function|_build_regex_range
dedent|''
dedent|''
name|'def'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'True'
op|','
name|'invert'
op|'='
name|'False'
op|','
name|'exclude'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Build a range regex for a set of characters in utf8.\n\n    This builds a valid range regex for characters in utf8 by\n    iterating the entire space and building up a set of x-y ranges for\n    all the characters we find which are valid.\n\n    :param ws: should we include whitespace in this range.\n    :param exclude: any characters we want to exclude\n    :param invert: invert the logic\n\n    The inversion is useful when we want to generate a set of ranges\n    which is everything that\'s not a certain class. For instance,\n    produce all all the non printable characters as a set of ranges.\n    """'
newline|'\n'
name|'if'
name|'exclude'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'exclude'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'regex'
op|'='
string|'""'
newline|'\n'
comment|'# are we currently in a range'
nl|'\n'
name|'in_range'
op|'='
name|'False'
newline|'\n'
comment|'# last character we found, for closing ranges'
nl|'\n'
name|'last'
op|'='
name|'None'
newline|'\n'
comment|'# last character we added to the regex, this lets us know that we'
nl|'\n'
comment|"# already have B in the range, which means we don't need to close"
nl|'\n'
comment|"# it out with B-B. While the later seems to work, it's kind of bad form."
nl|'\n'
name|'last_added'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|valid_char
name|'def'
name|'valid_char'
op|'('
name|'char'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'char'
name|'in'
name|'exclude'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'elif'
name|'ws'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'_is_printable'
op|'('
name|'char'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Zs is the unicode class for space characters, of which'
nl|'\n'
comment|'# there are about 10 in this range.'
nl|'\n'
indent|'            '
name|'result'
op|'='
op|'('
name|'_is_printable'
op|'('
name|'char'
op|')'
name|'and'
nl|'\n'
name|'unicodedata'
op|'.'
name|'category'
op|'('
name|'char'
op|')'
op|'!='
string|'"Zs"'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'invert'
name|'is'
name|'True'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'not'
name|'result'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
comment|'# iterate through the entire character range. in_'
nl|'\n'
dedent|''
name|'for'
name|'c'
name|'in'
name|'_get_all_chars'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'valid_char'
op|'('
name|'c'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'in_range'
op|':'
newline|'\n'
indent|'                '
name|'regex'
op|'+='
name|'re'
op|'.'
name|'escape'
op|'('
name|'c'
op|')'
newline|'\n'
name|'last_added'
op|'='
name|'c'
newline|'\n'
dedent|''
name|'in_range'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'in_range'
name|'and'
name|'last'
op|'!='
name|'last_added'
op|':'
newline|'\n'
indent|'                '
name|'regex'
op|'+='
string|'"-"'
op|'+'
name|'re'
op|'.'
name|'escape'
op|'('
name|'last'
op|')'
newline|'\n'
dedent|''
name|'in_range'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'last'
op|'='
name|'c'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'in_range'
op|':'
newline|'\n'
indent|'            '
name|'regex'
op|'+='
string|'"-"'
op|'+'
name|'re'
op|'.'
name|'escape'
op|'('
name|'c'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'regex'
newline|'\n'
nl|'\n'
DECL|variable|valid_name_regex_base
dedent|''
name|'valid_name_regex_base'
op|'='
string|"'^(?![%s])[%s]*(?<![%s])$'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_name_regex
name|'valid_name_regex'
op|'='
name|'ValidationRegex'
op|'('
nl|'\n'
name|'valid_name_regex_base'
op|'%'
op|'('
nl|'\n'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|','
name|'invert'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'_build_regex_range'
op|'('
op|')'
op|','
nl|'\n'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|','
name|'invert'
op|'='
name|'True'
op|')'
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|'"printable characters. Can not start or end with whitespace."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# This regex allows leading/trailing whitespace'
nl|'\n'
DECL|variable|valid_name_leading_trailing_spaces_regex_base
name|'valid_name_leading_trailing_spaces_regex_base'
op|'='
op|'('
nl|'\n'
string|'"^[%(ws)s]*[%(no_ws)s]+[%(ws)s]*$|"'
nl|'\n'
string|'"^[%(ws)s]*[%(no_ws)s][%(no_ws)s%(ws)s]+[%(no_ws)s][%(ws)s]*$"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_cell_name_regex
name|'valid_cell_name_regex'
op|'='
name|'ValidationRegex'
op|'('
nl|'\n'
name|'valid_name_regex_base'
op|'%'
op|'('
nl|'\n'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|','
name|'invert'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
name|'_build_regex_range'
op|'('
name|'exclude'
op|'='
op|'['
string|"'!'"
op|','
string|"'.'"
op|','
string|"'@'"
op|']'
op|')'
op|','
nl|'\n'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|','
name|'invert'
op|'='
name|'True'
op|')'
op|')'
op|','
nl|'\n'
name|'_'
op|'('
string|'"printable characters except !, ., @. "'
nl|'\n'
string|'"Can not start or end with whitespace."'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|"# cell's name disallow '!',  '.' and '@'."
nl|'\n'
DECL|variable|valid_cell_name_leading_trailing_spaces_regex
name|'valid_cell_name_leading_trailing_spaces_regex'
op|'='
name|'ValidationRegex'
op|'('
nl|'\n'
name|'valid_name_leading_trailing_spaces_regex_base'
op|'%'
op|'{'
nl|'\n'
string|"'ws'"
op|':'
name|'_build_regex_range'
op|'('
name|'exclude'
op|'='
op|'['
string|"'!'"
op|','
string|"'.'"
op|','
string|"'@'"
op|']'
op|')'
op|','
nl|'\n'
string|"'no_ws'"
op|':'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|','
name|'exclude'
op|'='
op|'['
string|"'!'"
op|','
string|"'.'"
op|','
string|"'@'"
op|']'
op|')'
op|'}'
op|','
nl|'\n'
name|'_'
op|'('
string|'"printable characters except !, ., @, "'
nl|'\n'
string|'"with at least one non space character"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_name_leading_trailing_spaces_regex
name|'valid_name_leading_trailing_spaces_regex'
op|'='
name|'ValidationRegex'
op|'('
nl|'\n'
name|'valid_name_leading_trailing_spaces_regex_base'
op|'%'
op|'{'
nl|'\n'
string|"'ws'"
op|':'
name|'_build_regex_range'
op|'('
op|')'
op|','
nl|'\n'
string|"'no_ws'"
op|':'
name|'_build_regex_range'
op|'('
name|'ws'
op|'='
name|'False'
op|')'
op|'}'
op|','
nl|'\n'
name|'_'
op|'('
string|'"printable characters with at least one non space character"'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_name_regex_obj
name|'valid_name_regex_obj'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
name|'valid_name_regex'
op|'.'
name|'regex'
op|','
name|'re'
op|'.'
name|'UNICODE'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_description_regex_base
name|'valid_description_regex_base'
op|'='
string|"'^[%s]*$'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|valid_description_regex
name|'valid_description_regex'
op|'='
name|'valid_description_regex_base'
op|'%'
op|'('
nl|'\n'
name|'_build_regex_range'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|boolean
name|'boolean'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'boolean'"
op|','
string|"'string'"
op|']'
op|','
nl|'\n'
string|"'enum'"
op|':'
op|'['
name|'True'
op|','
string|"'True'"
op|','
string|"'TRUE'"
op|','
string|"'true'"
op|','
string|"'1'"
op|','
string|"'ON'"
op|','
string|"'On'"
op|','
string|"'on'"
op|','
nl|'\n'
string|"'YES'"
op|','
string|"'Yes'"
op|','
string|"'yes'"
op|','
nl|'\n'
name|'False'
op|','
string|"'False'"
op|','
string|"'FALSE'"
op|','
string|"'false'"
op|','
string|"'0'"
op|','
string|"'OFF'"
op|','
string|"'Off'"
op|','
string|"'off'"
op|','
nl|'\n'
string|"'NO'"
op|','
string|"'No'"
op|','
string|"'no'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|none
name|'none'
op|'='
op|'{'
nl|'\n'
string|"'enum'"
op|':'
op|'['
string|"'None'"
op|','
name|'None'
op|','
op|'{'
op|'}'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|positive_integer
name|'positive_integer'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'integer'"
op|','
string|"'string'"
op|']'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[0-9]*$'"
op|','
string|"'minimum'"
op|':'
number|'1'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|non_negative_integer
name|'non_negative_integer'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'integer'"
op|','
string|"'string'"
op|']'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[0-9]*$'"
op|','
string|"'minimum'"
op|':'
number|'0'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|hostname
name|'hostname'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
comment|'# NOTE: \'host\' is defined in "services" table, and that'
nl|'\n'
comment|'# means a hostname. The hostname grammar in RFC952 does'
nl|'\n'
comment|'# not allow for underscores in hostnames. However, this'
nl|'\n'
comment|'# schema allows them, because it sometimes occurs in'
nl|'\n'
comment|'# real systems.'
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-._]*$'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|hostname_or_ip_address
name|'hostname_or_ip_address'
op|'='
op|'{'
nl|'\n'
comment|'# NOTE: Allow to specify hostname, ipv4 and ipv6.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-_.:]*$'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
op|'{'
nl|'\n'
comment|"# NOTE: Nova v2.1 API contains some 'name' parameters such"
nl|'\n'
comment|'# as keypair, server, flavor, aggregate and so on. They are'
nl|'\n'
comment|'# stored in the DB and Nova specific parameters.'
nl|'\n'
comment|'# This definition is used for all their parameters.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'name'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cell_name
name|'cell_name'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'cell_name'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cell_name_leading_trailing_spaces
name|'cell_name_leading_trailing_spaces'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'cell_name_with_leading_trailing_spaces'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|name_with_leading_trailing_spaces
name|'name_with_leading_trailing_spaces'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'name_with_leading_trailing_spaces'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|description
name|'description'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'null'"
op|']'
op|','
string|"'minLength'"
op|':'
number|'0'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
name|'valid_description_regex'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|tcp_udp_port
name|'tcp_udp_port'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'integer'"
op|','
string|"'string'"
op|']'
op|','
string|"'pattern'"
op|':'
string|"'^[0-9]*$'"
op|','
nl|'\n'
string|"'minimum'"
op|':'
number|'0'
op|','
string|"'maximum'"
op|':'
number|'65535'
op|','
nl|'\n'
string|"'minLength'"
op|':'
number|'1'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|project_id
name|'project_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[a-zA-Z0-9-]*$'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|server_id
name|'server_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|image_id
name|'image_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|volume_id
name|'volume_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|network_id
name|'network_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|network_port_id
name|'network_port_id'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|admin_password
name|'admin_password'
op|'='
op|'{'
nl|'\n'
comment|'# NOTE: admin_password is the admin password of a server'
nl|'\n'
comment|"# instance, and it is not stored into nova's data base."
nl|'\n'
comment|'# In addition, users set sometimes long/strange string'
nl|'\n'
comment|'# as password. It is unnecessary to limit string length'
nl|'\n'
comment|'# and string pattern.'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|image_ref
name|'image_ref'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|flavor_ref
name|'flavor_ref'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'integer'"
op|']'
op|','
string|"'minLength'"
op|':'
number|'1'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|metadata
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'patternProperties'"
op|':'
op|'{'
nl|'\n'
string|"'^[a-zA-Z0-9-_:. ]{1,255}$'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'maxLength'"
op|':'
number|'255'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|metadata_with_null
name|'metadata_with_null'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'metadata_with_null'
op|'['
string|"'patternProperties'"
op|']'
op|'['
string|"'^[a-zA-Z0-9-_:. ]{1,255}$'"
op|']'
op|'['
string|"'type'"
op|']'
op|'='
op|'['
string|"'string'"
op|','
string|"'null'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|mac_address
name|'mac_address'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^([0-9a-fA-F]{2})(:[0-9a-fA-F]{2}){5}$'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ip_address
name|'ip_address'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'oneOf'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv4'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv6'"
op|'}'
nl|'\n'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ipv4
name|'ipv4'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'ipv4'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ipv6
name|'ipv6'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'ipv6'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cidr
name|'cidr'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'format'"
op|':'
string|"'cidr'"
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit
