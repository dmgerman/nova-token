begin_unit
comment|'# -*- test-case-name: twisted.web.test.test_web -*-'
nl|'\n'
comment|'# Copyright (c) 2001-2009 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'cStringIO'
name|'import'
name|'StringIO'
newline|'\n'
name|'import'
name|'linecache'
newline|'\n'
name|'import'
name|'string'
op|','
name|'re'
newline|'\n'
name|'import'
name|'types'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'html'
op|','
name|'resource'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|redirectTo
name|'def'
name|'redirectTo'
op|'('
name|'URL'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'request'
op|'.'
name|'redirect'
op|'('
name|'URL'
op|')'
newline|'\n'
name|'return'
string|'"""\n<html>\n    <head>\n        <meta http-equiv=\\"refresh\\" content=\\"0;URL=%(url)s\\">\n    </head>\n    <body bgcolor=\\"#FFFFFF\\" text=\\"#000000\\">\n    <a href=\\"%(url)s\\">click here</a>\n    </body>\n</html>\n"""'
op|'%'
op|'{'
string|"'url'"
op|':'
name|'URL'
op|'}'
newline|'\n'
nl|'\n'
DECL|class|Redirect
dedent|''
name|'class'
name|'Redirect'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|isLeaf
indent|'    '
name|'isLeaf'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'url'
op|'='
name|'url'
newline|'\n'
nl|'\n'
DECL|member|render
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'redirectTo'
op|'('
name|'self'
op|'.'
name|'url'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|class|ChildRedirector
dedent|''
dedent|''
name|'class'
name|'ChildRedirector'
op|'('
name|'Redirect'
op|')'
op|':'
newline|'\n'
DECL|variable|isLeaf
indent|'    '
name|'isLeaf'
op|'='
number|'0'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
comment|'# XXX is this enough?'
nl|'\n'
indent|'        '
name|'if'
op|'('
op|'('
name|'url'
op|'.'
name|'find'
op|'('
string|"'://'"
op|')'
op|'=='
op|'-'
number|'1'
op|')'
nl|'\n'
name|'and'
op|'('
name|'not'
name|'url'
op|'.'
name|'startswith'
op|'('
string|"'..'"
op|')'
op|')'
nl|'\n'
name|'and'
op|'('
name|'not'
name|'url'
op|'.'
name|'startswith'
op|'('
string|"'/'"
op|')'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
op|'('
string|'"It seems you\'ve given me a redirect (%s) that is a child of myself! That\'s not good, it\'ll cause an infinite redirect."'
op|'%'
name|'url'
op|')'
newline|'\n'
dedent|''
name|'Redirect'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'url'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'newUrl'
op|'='
name|'self'
op|'.'
name|'url'
newline|'\n'
name|'if'
name|'not'
name|'newUrl'
op|'.'
name|'endswith'
op|'('
string|"'/'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'newUrl'
op|'+='
string|"'/'"
newline|'\n'
dedent|''
name|'newUrl'
op|'+='
name|'name'
newline|'\n'
name|'return'
name|'ChildRedirector'
op|'('
name|'newUrl'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'urlpath'
newline|'\n'
nl|'\n'
DECL|class|ParentRedirect
name|'class'
name|'ParentRedirect'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    I redirect to URLPath.here().\n    """'
newline|'\n'
DECL|variable|isLeaf
name|'isLeaf'
op|'='
number|'1'
newline|'\n'
DECL|member|render
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'redirectTo'
op|'('
name|'urlpath'
op|'.'
name|'URLPath'
op|'.'
name|'fromRequest'
op|'('
name|'request'
op|')'
op|'.'
name|'here'
op|'('
op|')'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DeferredResource
dedent|''
dedent|''
name|'class'
name|'DeferredResource'
op|'('
name|'resource'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    I wrap up a Deferred that will eventually result in a Resource\n    object.\n    """'
newline|'\n'
DECL|variable|isLeaf
name|'isLeaf'
op|'='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'d'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resource'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'d'
op|'='
name|'d'
newline|'\n'
nl|'\n'
DECL|member|getChild
dedent|''
name|'def'
name|'getChild'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|render
dedent|''
name|'def'
name|'render'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'self'
op|'.'
name|'_cbChild'
op|','
name|'request'
op|')'
op|'.'
name|'addErrback'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_ebChild'
op|','
name|'request'
op|')'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'web'
op|'.'
name|'server'
name|'import'
name|'NOT_DONE_YET'
newline|'\n'
name|'return'
name|'NOT_DONE_YET'
newline|'\n'
nl|'\n'
DECL|member|_cbChild
dedent|''
name|'def'
name|'_cbChild'
op|'('
name|'self'
op|','
name|'child'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'render'
op|'('
name|'resource'
op|'.'
name|'getChildForRequest'
op|'('
name|'child'
op|','
name|'request'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ebChild
dedent|''
name|'def'
name|'_ebChild'
op|'('
name|'self'
op|','
name|'reason'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'.'
name|'processingFailed'
op|'('
name|'reason'
op|')'
newline|'\n'
name|'return'
name|'reason'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'stylesheet'
op|'='
string|'"""\n<style type="text/css">\n    p.error {\n      color: red;\n      font-family: Verdana, Arial, helvetica, sans-serif;\n      font-weight: bold;\n    }\n\n    div {\n      font-family: Verdana, Arial, helvetica, sans-serif;\n    }\n\n    div.stackTrace {\n    }\n\n    div.frame {\n      padding: 1em;\n      background: white;\n      border-bottom: thin black dashed;\n    }\n\n    div.firstFrame {\n      padding: 1em;\n      background: white;\n      border-top: thin black dashed;\n      border-bottom: thin black dashed;\n    }\n\n    div.location {\n    }\n\n    div.snippet {\n      margin-bottom: 0.5em;\n      margin-left: 1em;\n      background: #FFFFDD;\n    }\n\n    div.snippetHighlightLine {\n      color: red;\n    }\n\n    span.code {\n      font-family: "Courier New", courier, monotype;\n    }\n\n    span.function {\n      font-weight: bold;\n      font-family: "Courier New", courier, monotype;\n    }\n\n    table.variables {\n      border-collapse: collapse;\n      margin-left: 1em;\n    }\n\n    td.varName {\n      vertical-align: top;\n      font-weight: bold;\n      padding-left: 0.5em;\n      padding-right: 0.5em;\n    }\n\n    td.varValue {\n      padding-left: 0.5em;\n      padding-right: 0.5em;\n    }\n\n    div.variables {\n      margin-bottom: 0.5em;\n    }\n\n    span.heading {\n      font-weight: bold;\n    }\n\n    div.dict {\n      background: #cccc99;\n      padding: 2px;\n      float: left;\n    }\n\n    td.dictKey {\n      background: #ffff99;\n      font-weight: bold;\n    }\n\n    td.dictValue {\n      background: #ffff99;\n    }\n\n    div.list {\n      background: #7777cc;\n      padding: 2px;\n      float: left;\n    }\n\n    div.listItem {\n      background: #9999ff;\n    }\n\n    div.instance {\n      background: #cc7777;\n      padding: 2px;\n      float: left;\n    }\n\n    span.instanceName {\n      font-weight: bold;\n      display: block;\n    }\n\n    span.instanceRepr {\n      background: #ff9999;\n      font-family: "Courier New", courier, monotype;\n    }\n\n    div.function {\n      background: orange;\n      font-weight: bold;\n      float: left;\n    }\n</style>\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|htmlrepr
name|'def'
name|'htmlrepr'
op|'('
name|'x'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'htmlReprTypes'
op|'.'
name|'get'
op|'('
name|'type'
op|'('
name|'x'
op|')'
op|','
name|'htmlUnknown'
op|')'
op|'('
name|'x'
op|')'
newline|'\n'
nl|'\n'
DECL|function|saferepr
dedent|''
name|'def'
name|'saferepr'
op|'('
name|'x'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'rx'
op|'='
name|'repr'
op|'('
name|'x'
op|')'
newline|'\n'
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'        '
name|'rx'
op|'='
string|'"<repr failed! %s instance at %s>"'
op|'%'
op|'('
name|'x'
op|'.'
name|'__class__'
op|','
name|'id'
op|'('
name|'x'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'rx'
newline|'\n'
nl|'\n'
DECL|function|htmlUnknown
dedent|''
name|'def'
name|'htmlUnknown'
op|'('
name|'x'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"'<code>'"
op|'+'
name|'html'
op|'.'
name|'escape'
op|'('
name|'saferepr'
op|'('
name|'x'
op|')'
op|')'
op|'+'
string|"'</code>'"
newline|'\n'
nl|'\n'
DECL|function|htmlDict
dedent|''
name|'def'
name|'htmlDict'
op|'('
name|'d'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'io'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'w'
op|'='
name|'io'
op|'.'
name|'write'
newline|'\n'
name|'w'
op|'('
string|'\'<div class="dict"><span class="heading">Dictionary instance @ %s</span>\''
op|'%'
name|'hex'
op|'('
name|'id'
op|'('
name|'d'
op|')'
op|')'
op|')'
newline|'\n'
name|'w'
op|'('
string|'\'<table class="dict">\''
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'d'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'if'
name|'k'
op|'=='
string|"'__builtins__'"
op|':'
newline|'\n'
indent|'            '
name|'v'
op|'='
string|"'builtin dictionary'"
newline|'\n'
dedent|''
name|'w'
op|'('
string|'\'<tr><td class="dictKey">%s</td><td class="dictValue">%s</td></tr>\''
op|'%'
op|'('
name|'htmlrepr'
op|'('
name|'k'
op|')'
op|','
name|'htmlrepr'
op|'('
name|'v'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'w'
op|'('
string|"'</table></div>'"
op|')'
newline|'\n'
name|'return'
name|'io'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|htmlList
dedent|''
name|'def'
name|'htmlList'
op|'('
name|'l'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'io'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'w'
op|'='
name|'io'
op|'.'
name|'write'
newline|'\n'
name|'w'
op|'('
string|'\'<div class="list"><span class="heading">List instance @ %s</span>\''
op|'%'
name|'hex'
op|'('
name|'id'
op|'('
name|'l'
op|')'
op|')'
op|')'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'l'
op|':'
newline|'\n'
indent|'        '
name|'w'
op|'('
string|'\'<div class="listItem">%s</div>\''
op|'%'
name|'htmlrepr'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
dedent|''
name|'w'
op|'('
string|"'</div>'"
op|')'
newline|'\n'
name|'return'
name|'io'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|htmlInst
dedent|''
name|'def'
name|'htmlInst'
op|'('
name|'i'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'hasattr'
op|'('
name|'i'
op|','
string|'"__html__"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'i'
op|'.'
name|'__html__'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'html'
op|'.'
name|'escape'
op|'('
name|'saferepr'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
string|'\'\'\'<div class="instance"><span class="instanceName">%s instance @ %s</span>\n              <span class="instanceRepr">%s</span></div>\n              \'\'\''
op|'%'
op|'('
name|'i'
op|'.'
name|'__class__'
op|','
name|'hex'
op|'('
name|'id'
op|'('
name|'i'
op|')'
op|')'
op|','
name|'s'
op|')'
newline|'\n'
nl|'\n'
DECL|function|htmlString
dedent|''
name|'def'
name|'htmlString'
op|'('
name|'s'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'html'
op|'.'
name|'escape'
op|'('
name|'saferepr'
op|'('
name|'s'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|htmlFunc
dedent|''
name|'def'
name|'htmlFunc'
op|'('
name|'f'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'('
string|'\'<div class="function">\''
op|'+'
nl|'\n'
name|'html'
op|'.'
name|'escape'
op|'('
string|'"function %s in file %s at line %s"'
op|'%'
nl|'\n'
op|'('
name|'f'
op|'.'
name|'__name__'
op|','
name|'f'
op|'.'
name|'func_code'
op|'.'
name|'co_filename'
op|','
nl|'\n'
name|'f'
op|'.'
name|'func_code'
op|'.'
name|'co_firstlineno'
op|')'
op|')'
op|'+'
nl|'\n'
string|"'</div>'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|htmlReprTypes
dedent|''
name|'htmlReprTypes'
op|'='
op|'{'
name|'types'
op|'.'
name|'DictType'
op|':'
name|'htmlDict'
op|','
nl|'\n'
name|'types'
op|'.'
name|'ListType'
op|':'
name|'htmlList'
op|','
nl|'\n'
name|'types'
op|'.'
name|'InstanceType'
op|':'
name|'htmlInst'
op|','
nl|'\n'
name|'types'
op|'.'
name|'StringType'
op|':'
name|'htmlString'
op|','
nl|'\n'
name|'types'
op|'.'
name|'FunctionType'
op|':'
name|'htmlFunc'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
nl|'\n'
DECL|function|htmlIndent
name|'def'
name|'htmlIndent'
op|'('
name|'snippetLine'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ret'
op|'='
name|'string'
op|'.'
name|'replace'
op|'('
name|'string'
op|'.'
name|'replace'
op|'('
name|'html'
op|'.'
name|'escape'
op|'('
name|'string'
op|'.'
name|'rstrip'
op|'('
name|'snippetLine'
op|')'
op|')'
op|','
nl|'\n'
string|"'  '"
op|','
string|"'&nbsp;'"
op|')'
op|','
nl|'\n'
string|"'\\t'"
op|','
string|"'&nbsp; &nbsp; &nbsp; &nbsp; '"
op|')'
newline|'\n'
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
DECL|function|formatFailure
dedent|''
name|'def'
name|'formatFailure'
op|'('
name|'myFailure'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
name|'exceptionHTML'
op|'='
string|'"""\n<p class="error">%s: %s</p>\n"""'
newline|'\n'
nl|'\n'
name|'frameHTML'
op|'='
string|'"""\n<div class="location">%s, line %s in <span class="function">%s</span></div>\n"""'
newline|'\n'
nl|'\n'
name|'snippetLineHTML'
op|'='
string|'"""\n<div class="snippetLine"><span class="lineno">%s</span><span class="code">%s</span></div>\n"""'
newline|'\n'
nl|'\n'
name|'snippetHighlightLineHTML'
op|'='
string|'"""\n<div class="snippetHighlightLine"><span class="lineno">%s</span><span class="code">%s</span></div>\n"""'
newline|'\n'
nl|'\n'
name|'variableHTML'
op|'='
string|'"""\n<tr class="varRow"><td class="varName">%s</td><td class="varValue">%s</td></tr>\n"""'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'myFailure'
op|','
name|'failure'
op|'.'
name|'Failure'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'html'
op|'.'
name|'PRE'
op|'('
name|'str'
op|'('
name|'myFailure'
op|')'
op|')'
newline|'\n'
dedent|''
name|'io'
op|'='
name|'StringIO'
op|'('
op|')'
newline|'\n'
name|'w'
op|'='
name|'io'
op|'.'
name|'write'
newline|'\n'
name|'w'
op|'('
name|'stylesheet'
op|')'
newline|'\n'
name|'w'
op|'('
string|'\'<a href="#tbend">\''
op|')'
newline|'\n'
name|'w'
op|'('
name|'exceptionHTML'
op|'%'
op|'('
name|'html'
op|'.'
name|'escape'
op|'('
name|'str'
op|'('
name|'myFailure'
op|'.'
name|'type'
op|')'
op|')'
op|','
nl|'\n'
name|'html'
op|'.'
name|'escape'
op|'('
name|'str'
op|'('
name|'myFailure'
op|'.'
name|'value'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
name|'w'
op|'('
string|"'</a>'"
op|')'
newline|'\n'
name|'w'
op|'('
string|'\'<div class="stackTrace">\''
op|')'
newline|'\n'
name|'first'
op|'='
number|'1'
newline|'\n'
name|'for'
name|'method'
op|','
name|'filename'
op|','
name|'lineno'
op|','
name|'localVars'
op|','
name|'globalVars'
name|'in'
name|'myFailure'
op|'.'
name|'frames'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'filename'
op|'=='
string|"'<string>'"
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'if'
name|'first'
op|':'
newline|'\n'
indent|'            '
name|'w'
op|'('
string|'\'<div class="firstFrame">\''
op|')'
newline|'\n'
name|'first'
op|'='
number|'0'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'w'
op|'('
string|'\'<div class="frame">\''
op|')'
newline|'\n'
dedent|''
name|'w'
op|'('
name|'frameHTML'
op|'%'
op|'('
name|'filename'
op|','
name|'lineno'
op|','
name|'method'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'w'
op|'('
string|'\'<div class="snippet">\''
op|')'
newline|'\n'
name|'textSnippet'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'snipLineNo'
name|'in'
name|'range'
op|'('
name|'lineno'
op|'-'
number|'2'
op|','
name|'lineno'
op|'+'
number|'2'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'snipLine'
op|'='
name|'linecache'
op|'.'
name|'getline'
op|'('
name|'filename'
op|','
name|'snipLineNo'
op|')'
newline|'\n'
name|'textSnippet'
op|'+='
name|'snipLine'
newline|'\n'
name|'snipLine'
op|'='
name|'htmlIndent'
op|'('
name|'snipLine'
op|')'
newline|'\n'
name|'if'
name|'snipLineNo'
op|'=='
name|'lineno'
op|':'
newline|'\n'
indent|'                '
name|'w'
op|'('
name|'snippetHighlightLineHTML'
op|'%'
op|'('
name|'snipLineNo'
op|','
name|'snipLine'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'w'
op|'('
name|'snippetLineHTML'
op|'%'
op|'('
name|'snipLineNo'
op|','
name|'snipLine'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'w'
op|'('
string|"'</div>'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Instance variables'
nl|'\n'
name|'for'
name|'name'
op|','
name|'var'
name|'in'
name|'localVars'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'name'
op|'=='
string|"'self'"
name|'and'
name|'hasattr'
op|'('
name|'var'
op|','
string|"'__dict__'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'usedVars'
op|'='
op|'['
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'var'
op|'.'
name|'__dict__'
op|'.'
name|'items'
op|'('
op|')'
nl|'\n'
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
string|"r'\\W'"
op|'+'
string|"'self.'"
op|'+'
name|'key'
op|'+'
string|"r'\\W'"
op|','
name|'textSnippet'
op|')'
op|']'
newline|'\n'
name|'if'
name|'usedVars'
op|':'
newline|'\n'
indent|'                    '
name|'w'
op|'('
string|'\'<div class="variables"><b>Self</b>\''
op|')'
newline|'\n'
name|'w'
op|'('
string|'\'<table class="variables">\''
op|')'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'usedVars'
op|':'
newline|'\n'
indent|'                        '
name|'w'
op|'('
name|'variableHTML'
op|'%'
op|'('
name|'key'
op|','
name|'htmlrepr'
op|'('
name|'value'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'w'
op|'('
string|"'</table></div>'"
op|')'
newline|'\n'
dedent|''
name|'break'
newline|'\n'
nl|'\n'
comment|'# Local and global vars'
nl|'\n'
dedent|''
dedent|''
name|'for'
name|'nm'
op|','
name|'varList'
name|'in'
op|'('
string|"'Locals'"
op|','
name|'localVars'
op|')'
op|','
op|'('
string|"'Globals'"
op|','
name|'globalVars'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'usedVars'
op|'='
op|'['
op|'('
name|'name'
op|','
name|'var'
op|')'
name|'for'
op|'('
name|'name'
op|','
name|'var'
op|')'
name|'in'
name|'varList'
nl|'\n'
name|'if'
name|'re'
op|'.'
name|'search'
op|'('
string|"r'\\W'"
op|'+'
name|'name'
op|'+'
string|"r'\\W'"
op|','
name|'textSnippet'
op|')'
op|']'
newline|'\n'
name|'if'
name|'usedVars'
op|':'
newline|'\n'
indent|'                '
name|'w'
op|'('
string|'\'<div class="variables"><b>%s</b><table class="variables">\''
op|'%'
name|'nm'
op|')'
newline|'\n'
name|'for'
name|'name'
op|','
name|'var'
name|'in'
name|'usedVars'
op|':'
newline|'\n'
indent|'                    '
name|'w'
op|'('
name|'variableHTML'
op|'%'
op|'('
name|'name'
op|','
name|'htmlrepr'
op|'('
name|'var'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'w'
op|'('
string|"'</table></div>'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'w'
op|'('
string|"'</div>'"
op|')'
comment|'# frame'
newline|'\n'
dedent|''
name|'w'
op|'('
string|"'</div>'"
op|')'
comment|'# stacktrace'
newline|'\n'
name|'w'
op|'('
string|'\'<a name="tbend"> </a>\''
op|')'
newline|'\n'
name|'w'
op|'('
name|'exceptionHTML'
op|'%'
op|'('
name|'html'
op|'.'
name|'escape'
op|'('
name|'str'
op|'('
name|'myFailure'
op|'.'
name|'type'
op|')'
op|')'
op|','
nl|'\n'
name|'html'
op|'.'
name|'escape'
op|'('
name|'str'
op|'('
name|'myFailure'
op|'.'
name|'value'
op|')'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'io'
op|'.'
name|'getvalue'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
