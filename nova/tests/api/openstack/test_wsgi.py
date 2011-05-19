begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestTest
name|'class'
name|'RequestTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_content_type_missing
indent|'    '
name|'def'
name|'test_content_type_missing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
string|'"<body />"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidContentType'
op|','
nl|'\n'
name|'request'
op|'.'
name|'get_content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_unsupported
dedent|''
name|'def'
name|'test_content_type_unsupported'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"text/html"'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
string|'"asdf<br />"'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidContentType'
op|','
nl|'\n'
name|'request'
op|'.'
name|'get_content_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_with_charset
dedent|''
name|'def'
name|'test_content_type_with_charset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Content-Type"'
op|']'
op|'='
string|'"application/json; charset=UTF-8"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'get_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_from_accept_xml
dedent|''
name|'def'
name|'test_content_type_from_accept_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/xml"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/xml, application/json"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/json; q=0.3, application/xml; q=0.9"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_from_query_extension
dedent|''
name|'def'
name|'test_content_type_from_query_extension'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123.xml'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123.json'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123.invalid'"
op|')'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_accept_and_query_extension
dedent|''
name|'def'
name|'test_content_type_accept_and_query_extension'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123.xml'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/xml"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_content_type_accept_default
dedent|''
name|'def'
name|'test_content_type_accept_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/tests/123.unsupported'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|'"Accept"'
op|']'
op|'='
string|'"application/unsupported1"'
newline|'\n'
name|'result'
op|'='
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
string|'"application/json"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DictSerializerTest
dedent|''
dedent|''
name|'class'
name|'DictSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_dispatch
indent|'    '
name|'def'
name|'test_dispatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'DictSerializer'
op|'('
op|')'
newline|'\n'
name|'serializer'
op|'.'
name|'create'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'pants'"
newline|'\n'
name|'serializer'
op|'.'
name|'default'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'trousers'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
op|'}'
op|','
string|"'create'"
op|')'
op|','
string|"'pants'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dispatch_default
dedent|''
name|'def'
name|'test_dispatch_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'DictSerializer'
op|'('
op|')'
newline|'\n'
name|'serializer'
op|'.'
name|'create'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'pants'"
newline|'\n'
name|'serializer'
op|'.'
name|'default'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'trousers'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
op|'}'
op|','
string|"'update'"
op|')'
op|','
string|"'trousers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XMLDictSerializerTest
dedent|''
dedent|''
name|'class'
name|'XMLDictSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_xml
indent|'    '
name|'def'
name|'test_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'input_dict'
op|'='
name|'dict'
op|'('
name|'servers'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
op|'('
number|'2'
op|','
number|'3'
op|')'
op|')'
op|')'
newline|'\n'
name|'expected_xml'
op|'='
string|'\'<serversxmlns="asdf"><a>(2,3)</a></servers>\''
newline|'\n'
name|'xmlns'
op|'='
string|'"testing xmlns"'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|'('
name|'xmlns'
op|'='
string|'"asdf"'
op|')'
newline|'\n'
name|'result'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input_dict'
op|')'
newline|'\n'
name|'result'
op|'='
name|'result'
op|'.'
name|'replace'
op|'('
string|"'\\n'"
op|','
string|"''"
op|')'
op|'.'
name|'replace'
op|'('
string|"' '"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected_xml'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONDictSerializerTest
dedent|''
dedent|''
name|'class'
name|'JSONDictSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_json
indent|'    '
name|'def'
name|'test_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'input_dict'
op|'='
name|'dict'
op|'('
name|'servers'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
op|'('
number|'2'
op|','
number|'3'
op|')'
op|')'
op|')'
newline|'\n'
name|'expected_json'
op|'='
string|'\'{"servers":{"a":[2,3]}}\''
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'JSONDictSerializer'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'input_dict'
op|')'
newline|'\n'
name|'result'
op|'='
name|'result'
op|'.'
name|'replace'
op|'('
string|"'\\n'"
op|','
string|"''"
op|')'
op|'.'
name|'replace'
op|'('
string|"' '"
op|','
string|"''"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'expected_json'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TextDeserializerTest
dedent|''
dedent|''
name|'class'
name|'TextDeserializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_dispatch
indent|'    '
name|'def'
name|'test_dispatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'TextDeserializer'
op|'('
op|')'
newline|'\n'
name|'deserializer'
op|'.'
name|'create'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'pants'"
newline|'\n'
name|'deserializer'
op|'.'
name|'default'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'trousers'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
op|'{'
op|'}'
op|','
string|"'create'"
op|')'
op|','
string|"'pants'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dispatch_default
dedent|''
name|'def'
name|'test_dispatch_default'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'TextDeserializer'
op|'('
op|')'
newline|'\n'
name|'deserializer'
op|'.'
name|'create'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'pants'"
newline|'\n'
name|'deserializer'
op|'.'
name|'default'
op|'='
name|'lambda'
name|'x'
op|':'
string|"'trousers'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
op|'{'
op|'}'
op|','
string|"'update'"
op|')'
op|','
string|"'trousers'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JSONDeserializerTest
dedent|''
dedent|''
name|'class'
name|'JSONDeserializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_json
indent|'    '
name|'def'
name|'test_json'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
string|'"""{"a": {\n                "a1": "1",\n                "a2": "2",\n                "bs": ["1", "2", "3", {"c": {"c1": "1"}}],\n                "d": {"e": "1"},\n                "f": "1"}}"""'
newline|'\n'
name|'as_dict'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
op|'{'
nl|'\n'
string|"'a1'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'a2'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'bs'"
op|':'
op|'['
string|"'1'"
op|','
string|"'2'"
op|','
string|"'3'"
op|','
op|'{'
string|"'c'"
op|':'
name|'dict'
op|'('
name|'c1'
op|'='
string|"'1'"
op|')'
op|'}'
op|']'
op|','
nl|'\n'
string|"'d'"
op|':'
op|'{'
string|"'e'"
op|':'
string|"'1'"
op|'}'
op|','
nl|'\n'
string|"'f'"
op|':'
string|"'1'"
op|'}'
op|')'
newline|'\n'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'JSONDeserializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'data'
op|')'
op|','
name|'as_dict'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XMLDeserializerTest
dedent|''
dedent|''
name|'class'
name|'XMLDeserializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_xml
indent|'    '
name|'def'
name|'test_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
string|'"""\n            <a a1="1" a2="2">\n              <bs><b>1</b><b>2</b><b>3</b><b><c c1="1"/></b></bs>\n              <d><e>1</e></d>\n              <f>1</f>\n            </a>\n            """'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'as_dict'
op|'='
name|'dict'
op|'('
name|'a'
op|'='
op|'{'
nl|'\n'
string|"'a1'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'a2'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'bs'"
op|':'
op|'['
string|"'1'"
op|','
string|"'2'"
op|','
string|"'3'"
op|','
op|'{'
string|"'c'"
op|':'
name|'dict'
op|'('
name|'c1'
op|'='
string|"'1'"
op|')'
op|'}'
op|']'
op|','
nl|'\n'
string|"'d'"
op|':'
op|'{'
string|"'e'"
op|':'
string|"'1'"
op|'}'
op|','
nl|'\n'
string|"'f'"
op|':'
string|"'1'"
op|'}'
op|')'
newline|'\n'
name|'metadata'
op|'='
op|'{'
string|"'plurals'"
op|':'
op|'{'
string|"'bs'"
op|':'
string|"'b'"
op|','
string|"'ts'"
op|':'
string|"'t'"
op|'}'
op|'}'
newline|'\n'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'xml'
op|')'
op|','
name|'as_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_xml_empty
dedent|''
name|'def'
name|'test_xml_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
string|'"""<a></a>"""'
newline|'\n'
name|'as_dict'
op|'='
op|'{'
string|'"a"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'xml'
op|')'
op|','
name|'as_dict'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseSerializerTest
dedent|''
dedent|''
name|'class'
name|'ResponseSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|JSONSerializer
indent|'        '
name|'class'
name|'JSONSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|serialize
indent|'            '
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'pew_json'"
newline|'\n'
nl|'\n'
DECL|class|XMLSerializer
dedent|''
dedent|''
name|'class'
name|'XMLSerializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|serialize
indent|'            '
name|'def'
name|'serialize'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'pew_xml'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/json'"
op|':'
name|'JSONSerializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/XML'"
op|':'
name|'XMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'serializers'
op|'='
name|'self'
op|'.'
name|'serializers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_get_serializer
dedent|''
name|'def'
name|'test_get_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'get_serializer'
op|'('
string|"'application/json'"
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'serializers'
op|'['
string|"'application/json'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_serializer_unknown_content_type
dedent|''
name|'def'
name|'test_get_serializer_unknown_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidContentType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'get_serializer'
op|','
nl|'\n'
string|"'application/unknown'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_response
dedent|''
name|'def'
name|'test_serialize_response'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|'('
op|'{'
op|'}'
op|','
string|"'application/json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'headers'
op|'['
string|"'Content-Type'"
op|']'
op|','
string|"'application/json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'body'
op|','
string|"'pew_json'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serialize_response_dict_to_unknown_content_type
dedent|''
name|'def'
name|'test_serialize_response_dict_to_unknown_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidContentType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|','
nl|'\n'
string|"'application/unknown'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RequestDeserializerTest
dedent|''
dedent|''
name|'class'
name|'RequestDeserializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|JSONDeserializer
indent|'        '
name|'class'
name|'JSONDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|deserialize
indent|'            '
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'pew_json'"
newline|'\n'
nl|'\n'
DECL|class|XMLDeserializer
dedent|''
dedent|''
name|'class'
name|'XMLDeserializer'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|deserialize
indent|'            '
name|'def'
name|'deserialize'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'pew_xml'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'deserializers'
op|'='
op|'{'
nl|'\n'
string|"'application/json'"
op|':'
name|'JSONDeserializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/XML'"
op|':'
name|'XMLDeserializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'RequestDeserializer'
op|'('
nl|'\n'
name|'deserializers'
op|'='
name|'self'
op|'.'
name|'deserializers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|tearDown
dedent|''
name|'def'
name|'tearDown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|test_get_deserializer
dedent|''
name|'def'
name|'test_get_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'get_deserializer'
op|'('
string|"'application/json'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'self'
op|'.'
name|'deserializers'
op|'['
string|"'application/json'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_deserializer_unknown_content_type
dedent|''
name|'def'
name|'test_get_deserializer_unknown_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidContentType'
op|','
nl|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'get_deserializer'
op|','
nl|'\n'
string|"'application/unknown'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_expected_content_type
dedent|''
name|'def'
name|'test_get_expected_content_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/json'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'get_expected_content_type'
op|'('
name|'request'
op|')'
op|','
nl|'\n'
string|"'application/json'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_action_args
dedent|''
name|'def'
name|'test_get_action_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'env'
op|'='
op|'{'
nl|'\n'
string|"'wsgiorg.routing_args'"
op|':'
op|'['
name|'None'
op|','
op|'{'
nl|'\n'
string|"'controller'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'action'"
op|':'
string|"'update'"
op|','
nl|'\n'
string|"'id'"
op|':'
number|'12'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'action'"
op|':'
string|"'update'"
op|','
string|"'id'"
op|':'
number|'12'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'get_action_args'
op|'('
name|'env'
op|')'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserialize
dedent|''
name|'def'
name|'test_deserialize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_routing_args
indent|'        '
name|'def'
name|'fake_get_routing_args'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'action'"
op|':'
string|"'create'"
op|'}'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'get_action_args'
op|'='
name|'fake_get_routing_args'
newline|'\n'
nl|'\n'
name|'request'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'headers'
op|'['
string|"'Accept'"
op|']'
op|'='
string|"'application/xml'"
newline|'\n'
nl|'\n'
name|'deserialized'
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
name|'expected'
op|'='
op|'('
string|"'create'"
op|','
op|'{'
op|'}'
op|','
string|"'application/xml'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'deserialized'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceTest
dedent|''
dedent|''
name|'class'
name|'ResourceTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_dispatch
indent|'    '
name|'def'
name|'test_dispatch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|Controller
indent|'        '
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|index
indent|'            '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'pants'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'pants'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'resource'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
name|'actual'
op|'='
name|'resource'
op|'.'
name|'dispatch'
op|'('
name|'None'
op|','
string|"'index'"
op|','
op|'{'
string|"'pants'"
op|':'
string|"'off'"
op|'}'
op|')'
newline|'\n'
name|'expected'
op|'='
string|"'off'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'actual'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_dispatch_unknown_controller_action
dedent|''
name|'def'
name|'test_dispatch_unknown_controller_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|Controller
indent|'        '
name|'class'
name|'Controller'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|index
indent|'            '
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'pants'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'pants'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'resource'
op|'='
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'Controller'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'AttributeError'
op|','
name|'resource'
op|'.'
name|'dispatch'
op|','
nl|'\n'
name|'None'
op|','
string|"'create'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
