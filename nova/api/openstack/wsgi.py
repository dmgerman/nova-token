begin_unit
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'parsers'
name|'import'
name|'expat'
newline|'\n'
nl|'\n'
name|'import'
name|'faults'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XMLNS_V10
name|'XMLNS_V10'
op|'='
string|"'http://docs.rackspacecloud.com/servers/api/v1.0'"
newline|'\n'
DECL|variable|XMLNS_V11
name|'XMLNS_V11'
op|'='
string|"'http://docs.openstack.org/compute/api/v1.1'"
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.wsgi'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Request
name|'class'
name|'Request'
op|'('
name|'webob'
op|'.'
name|'Request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add some Openstack API-specific logic to the base webob.Request."""'
newline|'\n'
nl|'\n'
DECL|member|best_match_content_type
name|'def'
name|'best_match_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Determine the requested response content-type.\n\n        Based on the query extension then the Accept header.\n\n        """'
newline|'\n'
name|'supported'
op|'='
op|'('
string|"'application/json'"
op|','
string|"'application/xml'"
op|')'
newline|'\n'
nl|'\n'
name|'parts'
op|'='
name|'self'
op|'.'
name|'path'
op|'.'
name|'rsplit'
op|'('
string|"'.'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'ctype'
op|'='
string|"'application/{0}'"
op|'.'
name|'format'
op|'('
name|'parts'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'if'
name|'ctype'
name|'in'
name|'supported'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'ctype'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'bm'
op|'='
name|'self'
op|'.'
name|'accept'
op|'.'
name|'best_match'
op|'('
name|'supported'
op|')'
newline|'\n'
nl|'\n'
comment|"# default to application/json if we don't find a preference"
nl|'\n'
name|'return'
name|'bm'
name|'or'
string|"'application/json'"
newline|'\n'
nl|'\n'
DECL|member|get_content_type
dedent|''
name|'def'
name|'get_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Determine content type of the request body.\n\n        Does not do any body introspection, only checks header\n\n        """'
newline|'\n'
name|'if'
name|'not'
string|'"Content-Type"'
name|'in'
name|'self'
op|'.'
name|'headers'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'allowed_types'
op|'='
op|'('
string|'"application/xml"'
op|','
string|'"application/json"'
op|')'
newline|'\n'
name|'content_type'
op|'='
name|'self'
op|'.'
name|'content_type'
newline|'\n'
nl|'\n'
name|'if'
name|'content_type'
name|'not'
name|'in'
name|'allowed_types'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidContentType'
op|'('
name|'content_type'
op|'='
name|'content_type'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'content_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TextDeserializer
dedent|''
dedent|''
dedent|''
name|'class'
name|'TextDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Custom request body deserialization based on controller action name."""'
newline|'\n'
nl|'\n'
DECL|member|deserialize
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'datastring'
op|','
name|'action'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find local deserialization method and parse request body."""'
newline|'\n'
name|'action_method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'str'
op|'('
name|'action'
op|')'
op|','
name|'self'
op|'.'
name|'default'
op|')'
newline|'\n'
name|'return'
name|'action_method'
op|'('
name|'datastring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Default deserialization code should live here"""'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONDeserializer
dedent|''
dedent|''
name|'class'
name|'JSONDeserializer'
op|'('
name|'TextDeserializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_from_json
indent|'    '
name|'def'
name|'_from_json'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'loads'
op|'('
name|'datastring'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"cannot understand JSON"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MalformedRequestBody'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'body'"
op|':'
name|'self'
op|'.'
name|'_from_json'
op|'('
name|'datastring'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XMLDeserializer
dedent|''
dedent|''
name|'class'
name|'XMLDeserializer'
op|'('
name|'TextDeserializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'metadata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param metadata: information needed to deserialize xml into\n                         a dictionary.\n        """'
newline|'\n'
name|'super'
op|'('
name|'XMLDeserializer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'metadata'
op|'='
name|'metadata'
name|'or'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_from_xml
dedent|''
name|'def'
name|'_from_xml'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'plurals'
op|'='
name|'set'
op|'('
name|'self'
op|'.'
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'plurals'"
op|','
op|'{'
op|'}'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
op|'{'
name|'node'
op|'.'
name|'nodeName'
op|':'
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'node'
op|','
name|'plurals'
op|')'
op|'}'
newline|'\n'
dedent|''
name|'except'
name|'expat'
op|'.'
name|'ExpatError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"cannot understand XML"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'MalformedRequestBody'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_from_xml_node
dedent|''
dedent|''
name|'def'
name|'_from_xml_node'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'listnames'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert a minidom node to a simple Python type.\n\n        :param listnames: list of XML node names whose subnodes should\n                          be considered list items.\n\n        """'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'node'
op|'.'
name|'childNodes'
op|')'
op|'=='
number|'1'
name|'and'
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
op|'.'
name|'nodeType'
op|'=='
number|'3'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'node'
op|'.'
name|'childNodes'
op|'['
number|'0'
op|']'
op|'.'
name|'nodeValue'
newline|'\n'
dedent|''
name|'elif'
name|'node'
op|'.'
name|'nodeName'
name|'in'
name|'listnames'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'n'
op|','
name|'listnames'
op|')'
name|'for'
name|'n'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'='
name|'dict'
op|'('
op|')'
newline|'\n'
name|'for'
name|'attr'
name|'in'
name|'node'
op|'.'
name|'attributes'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'result'
op|'['
name|'attr'
op|']'
op|'='
name|'node'
op|'.'
name|'attributes'
op|'['
name|'attr'
op|']'
op|'.'
name|'nodeValue'
newline|'\n'
dedent|''
name|'for'
name|'child'
name|'in'
name|'node'
op|'.'
name|'childNodes'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'child'
op|'.'
name|'nodeType'
op|'!='
name|'node'
op|'.'
name|'TEXT_NODE'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'child'
op|'.'
name|'nodeName'
op|']'
op|'='
name|'self'
op|'.'
name|'_from_xml_node'
op|'('
name|'child'
op|','
nl|'\n'
name|'listnames'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'body'"
op|':'
name|'self'
op|'.'
name|'_from_xml'
op|'('
name|'datastring'
op|')'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestHeadersDeserializer
dedent|''
dedent|''
name|'class'
name|'RequestHeadersDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|deserialize
indent|'    '
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestDeserializer
dedent|''
dedent|''
name|'class'
name|'RequestDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Break up a Request object into more useful pieces."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'body_deserializers'
op|'='
name|'None'
op|','
name|'headers_deserializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'body_deserializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'XMLDeserializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/json'"
op|':'
name|'JSONDeserializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'body_deserializers'
op|'.'
name|'update'
op|'('
name|'body_deserializers'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'headers_deserializer'
op|'='
name|'headers_deserializer'
name|'or'
name|'RequestHeadersDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize
dedent|''
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Extract necessary pieces of the request.\n\n        :param request: Request object\n        :returns tuple of expected controller action name, dictionary of\n                 keyword arguments to pass to the controller, the expected\n                 content type of the response\n\n        """'
newline|'\n'
name|'action_args'
op|'='
name|'self'
op|'.'
name|'get_action_args'
op|'('
name|'request'
op|'.'
name|'environ'
op|')'
newline|'\n'
name|'action'
op|'='
name|'action_args'
op|'.'
name|'pop'
op|'('
string|"'action'"
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'action_args'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'deserialize_headers'
op|'('
name|'request'
op|','
name|'action'
op|')'
op|')'
newline|'\n'
name|'action_args'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'deserialize_body'
op|'('
name|'request'
op|','
name|'action'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'accept'
op|'='
name|'self'
op|'.'
name|'get_expected_content_type'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'action'
op|','
name|'action_args'
op|','
name|'accept'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize_headers
dedent|''
name|'def'
name|'deserialize_headers'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'headers_deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|deserialize_body
dedent|''
name|'def'
name|'deserialize_body'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'content_type'
op|'='
name|'request'
op|'.'
name|'get_content_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'content_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"No Content-Type provided in request"'
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'len'
op|'('
name|'request'
op|'.'
name|'body'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Empty body provided in request"'
op|')'
op|')'
newline|'\n'
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'deserializer'
op|'='
name|'self'
op|'.'
name|'get_body_deserializer'
op|'('
name|'content_type'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidContentType'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Unable to read body as provided Content-Type"'
op|')'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request'
op|'.'
name|'body'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_body_deserializer
dedent|''
name|'def'
name|'get_body_deserializer'
op|'('
name|'self'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'body_deserializers'
op|'['
name|'content_type'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidContentType'
op|'('
name|'content_type'
op|'='
name|'content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_expected_content_type
dedent|''
dedent|''
name|'def'
name|'get_expected_content_type'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_action_args
dedent|''
name|'def'
name|'get_action_args'
op|'('
name|'self'
op|','
name|'request_environment'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parse dictionary created by routes library."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'='
name|'request_environment'
op|'['
string|"'wsgiorg.routing_args'"
op|']'
op|'['
number|'1'
op|']'
op|'.'
name|'copy'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'args'
op|'['
string|"'controller'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'del'
name|'args'
op|'['
string|"'format'"
op|']'
newline|'\n'
dedent|''
name|'except'
name|'KeyError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'args'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DictSerializer
dedent|''
dedent|''
name|'class'
name|'DictSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Custom response body serialization based on controller action name."""'
newline|'\n'
nl|'\n'
DECL|member|serialize
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'data'
op|','
name|'action'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find local serialization method and encode response body."""'
newline|'\n'
name|'action_method'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'str'
op|'('
name|'action'
op|')'
op|','
name|'self'
op|'.'
name|'default'
op|')'
newline|'\n'
name|'return'
name|'action_method'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Default serialization code should live here"""'
newline|'\n'
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONDictSerializer
dedent|''
dedent|''
name|'class'
name|'JSONDictSerializer'
op|'('
name|'DictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|default
indent|'    '
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'dumps'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XMLDictSerializer
dedent|''
dedent|''
name|'class'
name|'XMLDictSerializer'
op|'('
name|'DictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'metadata'
op|'='
name|'None'
op|','
name|'xmlns'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param metadata: information needed to deserialize xml into\n                         a dictionary.\n        :param xmlns: XML namespace to include with serialized xml\n        """'
newline|'\n'
name|'super'
op|'('
name|'XMLDictSerializer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'metadata'
op|'='
name|'metadata'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'xmlns'
op|'='
name|'xmlns'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
comment|'# We expect data to contain a single key which is the XML root.'
nl|'\n'
indent|'        '
name|'root_key'
op|'='
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'self'
op|'.'
name|'metadata'
op|','
name|'root_key'
op|','
name|'data'
op|'['
name|'root_key'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_add_xmlns'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'node'
op|'.'
name|'toprettyxml'
op|'('
name|'indent'
op|'='
string|"'    '"
op|','
name|'encoding'
op|'='
string|"'utf-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_add_xmlns
dedent|''
name|'def'
name|'_add_xmlns'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'xmlns'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'xmlns'"
op|','
name|'self'
op|'.'
name|'xmlns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_to_xml_node
dedent|''
dedent|''
name|'def'
name|'_to_xml_node'
op|'('
name|'self'
op|','
name|'doc'
op|','
name|'metadata'
op|','
name|'nodename'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recursive method to convert data members to XML nodes."""'
newline|'\n'
name|'result'
op|'='
name|'doc'
op|'.'
name|'createElement'
op|'('
name|'nodename'
op|')'
newline|'\n'
nl|'\n'
comment|'# Set the xml namespace if one is specified'
nl|'\n'
comment|'# TODO(justinsb): We could also use prefixes on the keys'
nl|'\n'
name|'xmlns'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'xmlns'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'xmlns'
op|':'
newline|'\n'
indent|'            '
name|'result'
op|'.'
name|'setAttribute'
op|'('
string|"'xmlns'"
op|','
name|'xmlns'
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): accomplish this without a type-check'
nl|'\n'
dedent|''
name|'if'
name|'type'
op|'('
name|'data'
op|')'
name|'is'
name|'list'
op|':'
newline|'\n'
indent|'            '
name|'collections'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'list_collections'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'nodename'
name|'in'
name|'collections'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'='
name|'collections'
op|'['
name|'nodename'
op|']'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                    '
name|'node'
op|'='
name|'doc'
op|'.'
name|'createElement'
op|'('
name|'metadata'
op|'['
string|"'item_name'"
op|']'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
name|'metadata'
op|'['
string|"'item_key'"
op|']'
op|','
name|'str'
op|'('
name|'item'
op|')'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'singular'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'plurals'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
name|'nodename'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'singular'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'nodename'
op|'.'
name|'endswith'
op|'('
string|"'s'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'singular'
op|'='
name|'nodename'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'singular'
op|'='
string|"'item'"
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'metadata'
op|','
name|'singular'
op|','
name|'item'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
comment|'#TODO(bcwaldon): accomplish this without a type-check'
nl|'\n'
dedent|''
dedent|''
name|'elif'
name|'type'
op|'('
name|'data'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'collections'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'dict_collections'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'nodename'
name|'in'
name|'collections'
op|':'
newline|'\n'
indent|'                '
name|'metadata'
op|'='
name|'collections'
op|'['
name|'nodename'
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'data'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'node'
op|'='
name|'doc'
op|'.'
name|'createElement'
op|'('
name|'metadata'
op|'['
string|"'item_name'"
op|']'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
name|'metadata'
op|'['
string|"'item_key'"
op|']'
op|','
name|'str'
op|'('
name|'k'
op|')'
op|')'
newline|'\n'
name|'text'
op|'='
name|'doc'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'appendChild'
op|'('
name|'text'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
dedent|''
name|'attrs'
op|'='
name|'metadata'
op|'.'
name|'get'
op|'('
string|"'attributes'"
op|','
op|'{'
op|'}'
op|')'
op|'.'
name|'get'
op|'('
name|'nodename'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'data'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'k'
name|'in'
name|'attrs'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'.'
name|'setAttribute'
op|'('
name|'k'
op|','
name|'str'
op|'('
name|'v'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'node'
op|'='
name|'self'
op|'.'
name|'_to_xml_node'
op|'('
name|'doc'
op|','
name|'metadata'
op|','
name|'k'
op|','
name|'v'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Type is atom'
nl|'\n'
indent|'            '
name|'node'
op|'='
name|'doc'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseHeadersSerializer
dedent|''
dedent|''
name|'class'
name|'ResponseHeadersSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|serialize
indent|'    '
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'data'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'.'
name|'status_int'
op|'='
number|'200'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseSerializer
dedent|''
dedent|''
name|'class'
name|'ResponseSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Encode the necessary pieces into a response object"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'body_serializers'
op|'='
name|'None'
op|','
name|'headers_serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'XMLDictSerializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/json'"
op|':'
name|'JSONDictSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'body_serializers'
op|'.'
name|'update'
op|'('
name|'body_serializers'
name|'or'
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'headers_serializer'
op|'='
name|'headers_serializer'
name|'or'
name|'ResponseHeadersSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialize
dedent|''
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'response_data'
op|','
name|'content_type'
op|','
name|'action'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Serialize a dict into a string and wrap in a wsgi.Request object.\n\n        :param response_data: dict produced by the Controller\n        :param content_type: expected mimetype of serialized response body\n\n        """'
newline|'\n'
name|'response'
op|'='
name|'webob'
op|'.'
name|'Response'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'serialize_headers'
op|'('
name|'response'
op|','
name|'response_data'
op|','
name|'action'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'serialize_body'
op|'('
name|'response'
op|','
name|'response_data'
op|','
name|'content_type'
op|','
name|'action'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|serialize_headers
dedent|''
name|'def'
name|'serialize_headers'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'data'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'headers_serializer'
op|'.'
name|'serialize'
op|'('
name|'response'
op|','
name|'data'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|serialize_body
dedent|''
name|'def'
name|'serialize_body'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'data'
op|','
name|'content_type'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|'='
name|'content_type'
newline|'\n'
name|'serializer'
op|'='
name|'self'
op|'.'
name|'get_body_serializer'
op|'('
name|'content_type'
op|')'
newline|'\n'
name|'response'
op|'.'
name|'body'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'data'
op|','
name|'action'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_body_serializer
dedent|''
name|'def'
name|'get_body_serializer'
op|'('
name|'self'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'body_serializers'
op|'['
name|'content_type'
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'KeyError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidContentType'
op|'('
name|'content_type'
op|'='
name|'content_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Resource
dedent|''
dedent|''
dedent|''
name|'class'
name|'Resource'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""WSGI app that handles (de)serialization and controller dispatch.\n\n    WSGI app that reads routing information supplied by RoutesMiddleware\n    and calls the requested action method upon its controller.  All\n    controller action methods must accept a \'req\' argument, which is the\n    incoming wsgi.Request. If the operation is a PUT or POST, the controller\n    method must also accept a \'body\' argument (the deserialized request body).\n    They may raise a webob.exc exception or return a dict, which will be\n    serialized by requested content type.\n\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|','
name|'deserializer'
op|'='
name|'None'
op|','
name|'serializer'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        :param controller: object that implement methods created by routes lib\n        :param deserializer: object that can serialize the output of a\n                             controller into a webob response\n        :param serializer: object that can deserialize a webob request\n                           into necessary pieces\n\n        """'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'controller'
newline|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'='
name|'deserializer'
name|'or'
name|'RequestDeserializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'serializer'
op|'='
name|'serializer'
name|'or'
name|'ResponseSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""WSGI method that controls (de)serialization and method dispatch."""'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
string|'"%(method)s %(url)s"'
op|'%'
op|'{'
string|'"method"'
op|':'
name|'request'
op|'.'
name|'method'
op|','
nl|'\n'
string|'"url"'
op|':'
name|'request'
op|'.'
name|'url'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'action'
op|','
name|'args'
op|','
name|'accept'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'request'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidContentType'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unsupported Content-Type"'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'MalformedRequestBody'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Malformed request body"'
op|')'
newline|'\n'
name|'return'
name|'faults'
op|'.'
name|'Fault'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'action_result'
op|'='
name|'self'
op|'.'
name|'dispatch'
op|'('
name|'request'
op|','
name|'action'
op|','
name|'args'
op|')'
newline|'\n'
nl|'\n'
comment|'#TODO(bcwaldon): find a more elegant way to pass through non-dict types'
nl|'\n'
name|'if'
name|'type'
op|'('
name|'action_result'
op|')'
name|'is'
name|'dict'
op|':'
newline|'\n'
indent|'            '
name|'response'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'action_result'
op|','
name|'accept'
op|','
name|'action'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'response'
op|'='
name|'action_result'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'msg_dict'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'request'
op|'.'
name|'url'
op|','
name|'status'
op|'='
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"%(url)s returned with HTTP %(status)d"'
op|')'
op|'%'
name|'msg_dict'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'msg_dict'
op|'='
name|'dict'
op|'('
name|'url'
op|'='
name|'request'
op|'.'
name|'url'
op|','
name|'e'
op|'='
name|'e'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|'"%(url)s returned a fault: %(e)s"'
op|'%'
name|'msg_dict'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'info'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|dispatch
dedent|''
name|'def'
name|'dispatch'
op|'('
name|'self'
op|','
name|'request'
op|','
name|'action'
op|','
name|'action_args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find action-spefic method on controller and call it."""'
newline|'\n'
nl|'\n'
name|'controller_method'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'action'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'controller_method'
op|'('
name|'req'
op|'='
name|'request'
op|','
op|'**'
name|'action_args'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
op|','
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'str'
op|'('
name|'exc'
op|')'
op|')'
newline|'\n'
name|'return'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
