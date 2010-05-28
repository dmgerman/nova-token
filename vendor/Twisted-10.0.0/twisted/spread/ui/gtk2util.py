begin_unit
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'nested_scopes'
newline|'\n'
nl|'\n'
name|'import'
name|'gtk'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
name|'import'
name|'copyright'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'python'
name|'import'
name|'failure'
op|','
name|'log'
op|','
name|'util'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'spread'
name|'import'
name|'pb'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'cred'
op|'.'
name|'credentials'
name|'import'
name|'UsernamePassword'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'error'
name|'as'
name|'netError'
newline|'\n'
nl|'\n'
DECL|function|login
name|'def'
name|'login'
op|'('
name|'client'
op|'='
name|'None'
op|','
op|'**'
name|'defaults'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    @param host:\n    @param port:\n    @param identityName:\n    @param password:\n    @param serviceName:\n    @param perspectiveName:\n\n    @returntype: Deferred RemoteReference of Perspective\n    """'
newline|'\n'
name|'d'
op|'='
name|'defer'
op|'.'
name|'Deferred'
op|'('
op|')'
newline|'\n'
name|'LoginDialog'
op|'('
name|'client'
op|','
name|'d'
op|','
name|'defaults'
op|')'
newline|'\n'
name|'return'
name|'d'
newline|'\n'
nl|'\n'
DECL|class|GladeKeeper
dedent|''
name|'class'
name|'GladeKeeper'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    @cvar gladefile: The file in which the glade GUI definition is kept.\n    @type gladefile: str\n\n    @cvar _widgets: Widgets that should be attached to me as attributes.\n    @type _widgets: list of strings\n    """'
newline|'\n'
nl|'\n'
DECL|variable|gladefile
name|'gladefile'
op|'='
name|'None'
newline|'\n'
DECL|variable|_widgets
name|'_widgets'
op|'='
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'gtk'
name|'import'
name|'glade'
newline|'\n'
name|'self'
op|'.'
name|'glade'
op|'='
name|'glade'
op|'.'
name|'XML'
op|'('
name|'self'
op|'.'
name|'gladefile'
op|')'
newline|'\n'
nl|'\n'
comment|'# mold can go away when we get a newer pygtk (post 1.99.14)'
nl|'\n'
name|'mold'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'dir'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mold'
op|'['
name|'k'
op|']'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
name|'k'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'glade'
op|'.'
name|'signal_autoconnect'
op|'('
name|'mold'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setWidgets'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setWidgets
dedent|''
name|'def'
name|'_setWidgets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'get_widget'
op|'='
name|'self'
op|'.'
name|'glade'
op|'.'
name|'get_widget'
newline|'\n'
name|'for'
name|'widgetName'
name|'in'
name|'self'
op|'.'
name|'_widgets'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
string|'"_"'
op|'+'
name|'widgetName'
op|','
name|'get_widget'
op|'('
name|'widgetName'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoginDialog
dedent|''
dedent|''
dedent|''
name|'class'
name|'LoginDialog'
op|'('
name|'GladeKeeper'
op|')'
op|':'
newline|'\n'
comment|'# IdentityConnector host port identityName password'
nl|'\n'
comment|'# requestLogin -> identityWrapper or login failure'
nl|'\n'
comment|'# requestService serviceName perspectiveName client'
nl|'\n'
nl|'\n'
comment|'# window killed'
nl|'\n'
comment|'# cancel button pressed'
nl|'\n'
comment|'# login button activated'
nl|'\n'
nl|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'['
string|"'host'"
op|','
string|"'port'"
op|','
string|"'identityName'"
op|','
string|"'password'"
op|','
nl|'\n'
string|"'perspectiveName'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|_widgets
name|'_widgets'
op|'='
op|'('
string|'"hostEntry"'
op|','
string|'"portEntry"'
op|','
string|'"identityNameEntry"'
op|','
string|'"passwordEntry"'
op|','
nl|'\n'
string|'"perspectiveNameEntry"'
op|','
string|'"statusBar"'
op|','
nl|'\n'
string|'"loginDialog"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_advancedControls
name|'_advancedControls'
op|'='
op|'['
string|"'perspectiveLabel'"
op|','
string|"'perspectiveNameEntry'"
op|','
nl|'\n'
string|"'protocolLabel'"
op|','
string|"'versionLabel'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|gladefile
name|'gladefile'
op|'='
name|'util'
op|'.'
name|'sibpath'
op|'('
name|'__file__'
op|','
string|'"login2.glade"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'client'
op|','
name|'deferred'
op|','
name|'defaults'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'client'
op|'='
name|'client'
newline|'\n'
name|'self'
op|'.'
name|'deferredResult'
op|'='
name|'deferred'
newline|'\n'
nl|'\n'
name|'GladeKeeper'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'setDefaults'
op|'('
name|'defaults'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_loginDialog'
op|'.'
name|'show'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setDefaults
dedent|''
name|'def'
name|'setDefaults'
op|'('
name|'self'
op|','
name|'defaults'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'defaults'
op|'.'
name|'has_key'
op|'('
string|"'port'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'defaults'
op|'['
string|"'port'"
op|']'
op|'='
name|'str'
op|'('
name|'pb'
op|'.'
name|'portno'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'defaults'
op|'['
string|"'port'"
op|']'
op|','
op|'('
name|'int'
op|','
name|'long'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'defaults'
op|'['
string|"'port'"
op|']'
op|'='
name|'str'
op|'('
name|'defaults'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'defaults'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'k'
name|'in'
name|'self'
op|'.'
name|'fields'
op|':'
newline|'\n'
indent|'                '
name|'widget'
op|'='
name|'getattr'
op|'('
name|'self'
op|','
string|'"_%sEntry"'
op|'%'
op|'('
name|'k'
op|','
op|')'
op|')'
newline|'\n'
name|'widget'
op|'.'
name|'set_text'
op|'('
name|'v'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setWidgets
dedent|''
dedent|''
dedent|''
name|'def'
name|'_setWidgets'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'GladeKeeper'
op|'.'
name|'_setWidgets'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_statusContext'
op|'='
name|'self'
op|'.'
name|'_statusBar'
op|'.'
name|'get_context_id'
op|'('
string|'"Login dialog."'
op|')'
newline|'\n'
name|'get_widget'
op|'='
name|'self'
op|'.'
name|'glade'
op|'.'
name|'get_widget'
newline|'\n'
name|'get_widget'
op|'('
string|'"versionLabel"'
op|')'
op|'.'
name|'set_text'
op|'('
name|'copyright'
op|'.'
name|'longversion'
op|')'
newline|'\n'
name|'get_widget'
op|'('
string|'"protocolLabel"'
op|')'
op|'.'
name|'set_text'
op|'('
string|'"Protocol PB-%s"'
op|'%'
nl|'\n'
op|'('
name|'pb'
op|'.'
name|'Broker'
op|'.'
name|'version'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_loginDialog_response
dedent|''
name|'def'
name|'_on_loginDialog_response'
op|'('
name|'self'
op|','
name|'widget'
op|','
name|'response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'handlers'
op|'='
op|'{'
name|'gtk'
op|'.'
name|'RESPONSE_NONE'
op|':'
name|'self'
op|'.'
name|'_windowClosed'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'RESPONSE_DELETE_EVENT'
op|':'
name|'self'
op|'.'
name|'_windowClosed'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'RESPONSE_OK'
op|':'
name|'self'
op|'.'
name|'_doLogin'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'RESPONSE_CANCEL'
op|':'
name|'self'
op|'.'
name|'_cancelled'
op|'}'
newline|'\n'
name|'handler'
op|'='
name|'handlers'
op|'.'
name|'get'
op|'('
name|'response'
op|')'
newline|'\n'
name|'if'
name|'handler'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'handler'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'log'
op|'.'
name|'msg'
op|'('
string|'"Unexpected dialog response %r from %s"'
op|'%'
op|'('
name|'response'
op|','
nl|'\n'
name|'widget'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_loginDialog_close
dedent|''
dedent|''
name|'def'
name|'_on_loginDialog_close'
op|'('
name|'self'
op|','
name|'widget'
op|','
name|'userdata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_windowClosed'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_on_loginDialog_destroy_event
dedent|''
name|'def'
name|'_on_loginDialog_destroy_event'
op|'('
name|'self'
op|','
name|'widget'
op|','
name|'userdata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_windowClosed'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_cancelled
dedent|''
name|'def'
name|'_cancelled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'deferredResult'
op|'.'
name|'called'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deferredResult'
op|'.'
name|'errback'
op|'('
name|'netError'
op|'.'
name|'UserError'
op|'('
string|'"User hit Cancel."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_loginDialog'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_windowClosed
dedent|''
name|'def'
name|'_windowClosed'
op|'('
name|'self'
op|','
name|'reason'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'deferredResult'
op|'.'
name|'called'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'deferredResult'
op|'.'
name|'errback'
op|'('
name|'netError'
op|'.'
name|'UserError'
op|'('
string|'"Window closed."'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_doLogin
dedent|''
dedent|''
name|'def'
name|'_doLogin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'idParams'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'idParams'
op|'['
string|"'host'"
op|']'
op|'='
name|'self'
op|'.'
name|'_hostEntry'
op|'.'
name|'get_text'
op|'('
op|')'
newline|'\n'
name|'idParams'
op|'['
string|"'port'"
op|']'
op|'='
name|'self'
op|'.'
name|'_portEntry'
op|'.'
name|'get_text'
op|'('
op|')'
newline|'\n'
name|'idParams'
op|'['
string|"'identityName'"
op|']'
op|'='
name|'self'
op|'.'
name|'_identityNameEntry'
op|'.'
name|'get_text'
op|'('
op|')'
newline|'\n'
name|'idParams'
op|'['
string|"'password'"
op|']'
op|'='
name|'self'
op|'.'
name|'_passwordEntry'
op|'.'
name|'get_text'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'idParams'
op|'['
string|"'port'"
op|']'
op|'='
name|'int'
op|'('
name|'idParams'
op|'['
string|"'port'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'='
name|'pb'
op|'.'
name|'PBClientFactory'
op|'('
op|')'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'connectTCP'
op|'('
name|'idParams'
op|'['
string|"'host'"
op|']'
op|','
name|'idParams'
op|'['
string|"'port'"
op|']'
op|','
name|'f'
op|')'
newline|'\n'
name|'creds'
op|'='
name|'UsernamePassword'
op|'('
name|'idParams'
op|'['
string|"'identityName'"
op|']'
op|','
name|'idParams'
op|'['
string|"'password'"
op|']'
op|')'
newline|'\n'
name|'f'
op|'.'
name|'login'
op|'('
name|'creds'
op|','
name|'self'
op|'.'
name|'client'
nl|'\n'
op|')'
op|'.'
name|'addCallbacks'
op|'('
name|'self'
op|'.'
name|'_cbGotPerspective'
op|','
name|'self'
op|'.'
name|'_ebFailedLogin'
nl|'\n'
op|')'
op|'.'
name|'setTimeout'
op|'('
number|'30'
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'statusMsg'
op|'('
string|'"Contacting server..."'
op|')'
newline|'\n'
nl|'\n'
comment|'# serviceName = self._serviceNameEntry.get_text()'
nl|'\n'
comment|'# perspectiveName = self._perspectiveNameEntry.get_text()'
nl|'\n'
comment|'# if not perspectiveName:'
nl|'\n'
comment|"#     perspectiveName = idParams['identityName']"
nl|'\n'
nl|'\n'
comment|'# d = _identityConnector.requestService(serviceName, perspectiveName,'
nl|'\n'
comment|'#                                       self.client)'
nl|'\n'
comment|'# d.addCallbacks(self._cbGotPerspective, self._ebFailedLogin)'
nl|'\n'
comment|'# setCursor to waiting'
nl|'\n'
nl|'\n'
DECL|member|_cbGotPerspective
dedent|''
name|'def'
name|'_cbGotPerspective'
op|'('
name|'self'
op|','
name|'perspective'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'statusMsg'
op|'('
string|'"Connected to server."'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deferredResult'
op|'.'
name|'callback'
op|'('
name|'perspective'
op|')'
newline|'\n'
comment|'# clear waiting cursor'
nl|'\n'
name|'self'
op|'.'
name|'_loginDialog'
op|'.'
name|'destroy'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ebFailedLogin
dedent|''
name|'def'
name|'_ebFailedLogin'
op|'('
name|'self'
op|','
name|'reason'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'reason'
op|','
name|'failure'
op|'.'
name|'Failure'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
name|'reason'
op|'.'
name|'value'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'statusMsg'
op|'('
name|'reason'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'reason'
op|','
op|'('
name|'unicode'
op|','
name|'str'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'reason'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'unicode'
op|'('
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'msg'
op|'='
name|'gtk'
op|'.'
name|'MessageDialog'
op|'('
name|'self'
op|'.'
name|'_loginDialog'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'DIALOG_DESTROY_WITH_PARENT'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'MESSAGE_ERROR'
op|','
nl|'\n'
name|'gtk'
op|'.'
name|'BUTTONS_CLOSE'
op|','
nl|'\n'
name|'text'
op|')'
newline|'\n'
name|'msg'
op|'.'
name|'show_all'
op|'('
op|')'
newline|'\n'
name|'msg'
op|'.'
name|'connect'
op|'('
string|'"response"'
op|','
name|'lambda'
op|'*'
name|'a'
op|':'
name|'msg'
op|'.'
name|'destroy'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# hostname not found'
nl|'\n'
comment|'# host unreachable'
nl|'\n'
comment|'# connection refused'
nl|'\n'
comment|'# authentication failed'
nl|'\n'
comment|'# no such service'
nl|'\n'
comment|'# no such perspective'
nl|'\n'
comment|'# internal server error'
nl|'\n'
nl|'\n'
DECL|member|_on_advancedButton_toggled
dedent|''
name|'def'
name|'_on_advancedButton_toggled'
op|'('
name|'self'
op|','
name|'widget'
op|','
name|'userdata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'active'
op|'='
name|'widget'
op|'.'
name|'get_active'
op|'('
op|')'
newline|'\n'
name|'if'
name|'active'
op|':'
newline|'\n'
indent|'            '
name|'op'
op|'='
string|'"show"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'op'
op|'='
string|'"hide"'
newline|'\n'
dedent|''
name|'for'
name|'widgetName'
name|'in'
name|'self'
op|'.'
name|'_advancedControls'
op|':'
newline|'\n'
indent|'            '
name|'widget'
op|'='
name|'self'
op|'.'
name|'glade'
op|'.'
name|'get_widget'
op|'('
name|'widgetName'
op|')'
newline|'\n'
name|'getattr'
op|'('
name|'widget'
op|','
name|'op'
op|')'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|statusMsg
dedent|''
dedent|''
name|'def'
name|'statusMsg'
op|'('
name|'self'
op|','
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'text'
op|','
op|'('
name|'unicode'
op|','
name|'str'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'text'
op|'='
name|'unicode'
op|'('
name|'text'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_statusBar'
op|'.'
name|'push'
op|'('
name|'self'
op|'.'
name|'_statusContext'
op|','
name|'text'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
