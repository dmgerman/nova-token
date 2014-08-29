begin_unit
comment|'# Copyright (c) 2012 VMware, Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\n'
comment|'# Copyright 2011 OpenStack Foundation'
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
string|'"""\nClasses for making VMware VI SOAP calls.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'httplib'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
name|'import'
name|'urllib2'
newline|'\n'
nl|'\n'
name|'import'
name|'decorator'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
name|'import'
name|'suds'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\n'
nl|'\n'
DECL|variable|RESP_NOT_XML_ERROR
name|'RESP_NOT_XML_ERROR'
op|'='
string|'\'Response is "text/html", not "text/xml"\''
newline|'\n'
DECL|variable|CONN_ABORT_ERROR
name|'CONN_ABORT_ERROR'
op|'='
string|"'Software caused connection abort'"
newline|'\n'
DECL|variable|ADDRESS_IN_USE_ERROR
name|'ADDRESS_IN_USE_ERROR'
op|'='
string|"'Address already in use'"
newline|'\n'
nl|'\n'
DECL|variable|vmwareapi_wsdl_loc_opt
name|'vmwareapi_wsdl_loc_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'wsdl_location'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Optional VIM Service WSDL Location '"
nl|'\n'
string|"'e.g http://<server>/vimService.wsdl. '"
nl|'\n'
string|"'Optional over-ride to default location for bug work-arounds'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'vmwareapi_wsdl_loc_opt'
op|','
string|"'vmware'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'decorator'
op|'.'
name|'decorator'
newline|'\n'
DECL|function|retry_if_task_in_progress
name|'def'
name|'retry_if_task_in_progress'
op|'('
name|'f'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'retries'
op|'='
name|'max'
op|'('
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'api_retry_count'
op|','
number|'1'
op|')'
newline|'\n'
name|'delay'
op|'='
number|'1'
newline|'\n'
name|'for'
name|'attempt'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'retries'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'attempt'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
name|'delay'
op|')'
newline|'\n'
name|'delay'
op|'='
name|'min'
op|'('
number|'2'
op|'*'
name|'delay'
op|','
number|'60'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'TaskInProgress'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_moref
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_moref'
op|'('
name|'value'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get managed object reference."""'
newline|'\n'
name|'moref'
op|'='
name|'suds'
op|'.'
name|'sudsobject'
op|'.'
name|'Property'
op|'('
name|'value'
op|')'
newline|'\n'
name|'moref'
op|'.'
name|'_type'
op|'='
name|'type'
newline|'\n'
name|'return'
name|'moref'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|object_to_dict
dedent|''
name|'def'
name|'object_to_dict'
op|'('
name|'obj'
op|','
name|'list_depth'
op|'='
number|'1'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert Suds object into serializable format.\n\n    The calling function can limit the amount of list entries that\n    are converted.\n    """'
newline|'\n'
name|'d'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'suds'
op|'.'
name|'sudsobject'
op|'.'
name|'asdict'
op|'('
name|'obj'
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'hasattr'
op|'('
name|'v'
op|','
string|"'__keylist__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
name|'object_to_dict'
op|'('
name|'v'
op|','
name|'list_depth'
op|'='
name|'list_depth'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'v'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'used'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'v'
op|':'
newline|'\n'
indent|'                '
name|'used'
op|'='
name|'used'
op|'+'
number|'1'
newline|'\n'
name|'if'
name|'used'
op|'>'
name|'list_depth'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'item'
op|','
string|"'__keylist__'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'d'
op|'['
name|'k'
op|']'
op|'.'
name|'append'
op|'('
name|'object_to_dict'
op|'('
name|'item'
op|','
name|'list_depth'
op|'='
name|'list_depth'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'d'
op|'['
name|'k'
op|']'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'d'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'d'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VIMMessagePlugin
dedent|''
name|'class'
name|'VIMMessagePlugin'
op|'('
name|'suds'
op|'.'
name|'plugin'
op|'.'
name|'MessagePlugin'
op|')'
op|':'
newline|'\n'
DECL|member|addAttributeForValue
indent|'    '
name|'def'
name|'addAttributeForValue'
op|'('
name|'self'
op|','
name|'node'
op|')'
op|':'
newline|'\n'
comment|'# suds does not handle AnyType properly.'
nl|'\n'
comment|'# VI SDK requires type attribute to be set when AnyType is used'
nl|'\n'
indent|'        '
name|'if'
name|'node'
op|'.'
name|'name'
op|'=='
string|"'value'"
op|':'
newline|'\n'
indent|'            '
name|'node'
op|'.'
name|'set'
op|'('
string|"'xsi:type'"
op|','
string|"'xsd:string'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|marshalled
dedent|''
dedent|''
name|'def'
name|'marshalled'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""suds will send the specified soap envelope.\n        Provides the plugin with the opportunity to prune empty\n        nodes and fixup nodes before sending it to the server.\n        """'
newline|'\n'
comment|'# suds builds the entire request object based on the wsdl schema.'
nl|'\n'
comment|'# VI SDK throws server errors if optional SOAP nodes are sent'
nl|'\n'
comment|'# without values, e.g. <test/> as opposed to <test>test</test>'
nl|'\n'
name|'context'
op|'.'
name|'envelope'
op|'.'
name|'prune'
op|'('
op|')'
newline|'\n'
name|'context'
op|'.'
name|'envelope'
op|'.'
name|'walk'
op|'('
name|'self'
op|'.'
name|'addAttributeForValue'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Vim
dedent|''
dedent|''
name|'class'
name|'Vim'
op|':'
newline|'\n'
indent|'    '
string|'"""The VIM Object."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
nl|'\n'
name|'protocol'
op|'='
string|'"https"'
op|','
nl|'\n'
name|'host'
op|'='
string|'"localhost"'
op|','
nl|'\n'
name|'port'
op|'='
number|'443'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates the necessary Communication interfaces and gets the\n        ServiceContent for initiating SOAP transactions.\n\n        protocol: http or https\n        host    : ESX IPAddress or Hostname\n        port    : port for connection\n        """'
newline|'\n'
name|'if'
name|'not'
name|'suds'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Unable to import suds."'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_protocol'
op|'='
name|'protocol'
newline|'\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host'
newline|'\n'
name|'self'
op|'.'
name|'wsdl_url'
op|'='
name|'Vim'
op|'.'
name|'get_wsdl_url'
op|'('
name|'protocol'
op|','
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'url'
op|'='
name|'Vim'
op|'.'
name|'get_soap_url'
op|'('
name|'protocol'
op|','
name|'host'
op|','
name|'port'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'suds'
op|'.'
name|'client'
op|'.'
name|'Client'
op|'('
name|'self'
op|'.'
name|'wsdl_url'
op|','
name|'location'
op|'='
name|'self'
op|'.'
name|'url'
op|','
nl|'\n'
name|'plugins'
op|'='
op|'['
name|'VIMMessagePlugin'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_service_content'
op|'='
name|'self'
op|'.'
name|'retrieve_service_content'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|retrieve_service_content
dedent|''
name|'def'
name|'retrieve_service_content'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'RetrieveServiceContent'
op|'('
string|'"ServiceInstance"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_wsdl_url
name|'def'
name|'get_wsdl_url'
op|'('
name|'protocol'
op|','
name|'host_name'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Allows override of the wsdl location, making this static\n        means we can test the logic outside of the constructor\n        without forcing the test environment to have multiple valid\n        wsdl locations to test against.\n\n        :param protocol: https or http\n        :param host_name: localhost or other server name\n        :param port: port for connection\n        :return: string to WSDL location for vSphere WS Management API\n        """'
newline|'\n'
comment|'# optional WSDL location over-ride for work-arounds'
nl|'\n'
name|'if'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'wsdl_location'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'CONF'
op|'.'
name|'vmware'
op|'.'
name|'wsdl_location'
newline|'\n'
nl|'\n'
comment|'# calculate default WSDL location if no override supplied'
nl|'\n'
dedent|''
name|'return'
name|'Vim'
op|'.'
name|'get_soap_url'
op|'('
name|'protocol'
op|','
name|'host_name'
op|','
name|'port'
op|')'
op|'+'
string|'"/vimService.wsdl"'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_soap_url
name|'def'
name|'get_soap_url'
op|'('
name|'protocol'
op|','
name|'host_name'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Calculates the location of the SOAP services\n        for a particular server. Created as a static\n        method for testing.\n\n        :param protocol: https or http\n        :param host_name: localhost or other vSphere server name\n        :param port: port for connection\n        :return: the url to the active vSphere WS Management API\n        """'
newline|'\n'
name|'if'
name|'utils'
op|'.'
name|'is_valid_ipv6'
op|'('
name|'host_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'%s://[%s]:%d/sdk'"
op|'%'
op|'('
name|'protocol'
op|','
name|'host_name'
op|','
name|'port'
op|')'
newline|'\n'
dedent|''
name|'return'
string|"'%s://%s:%d/sdk'"
op|'%'
op|'('
name|'protocol'
op|','
name|'host_name'
op|','
name|'port'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_service_content
dedent|''
name|'def'
name|'get_service_content'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Gets the service content object."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_service_content'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes the API calls and gets the result."""'
newline|'\n'
DECL|function|vim_request_handler
name|'def'
name|'vim_request_handler'
op|'('
name|'managed_object'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Builds the SOAP message and parses the response for fault\n            checking and other errors.\n\n            managed_object    : Managed Object Reference or Managed\n                                Object Name\n            **kwargs          : Keyword arguments of the call\n            """'
newline|'\n'
comment|'# Dynamic handler for VI SDK Calls'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'request_mo'
op|'='
name|'self'
op|'.'
name|'_request_managed_object_builder'
op|'('
nl|'\n'
name|'managed_object'
op|')'
newline|'\n'
name|'request'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'client'
op|'.'
name|'service'
op|','
name|'attr_name'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'('
name|'request_mo'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
comment|'# To check for the faults that are part of the message body'
nl|'\n'
comment|'# and not returned as Fault object response from the ESX'
nl|'\n'
comment|'# SOAP server'
nl|'\n'
name|'if'
name|'hasattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'fault_checker'
op|'='
name|'getattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
newline|'\n'
name|'fault_checker'
op|'('
name|'response'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'response'
newline|'\n'
comment|'# Catch the VimFaultException that is raised by the fault'
nl|'\n'
comment|'# check of the SOAP response'
nl|'\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'except'
name|'suds'
op|'.'
name|'MethodNotFound'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'except'
name|'suds'
op|'.'
name|'WebFault'
name|'as'
name|'excep'
op|':'
newline|'\n'
indent|'                '
name|'doc'
op|'='
name|'excep'
op|'.'
name|'document'
newline|'\n'
name|'fault_string'
op|'='
name|'doc'
op|'.'
name|'childAtPath'
op|'('
string|'"/Envelope/Body/Fault/"'
nl|'\n'
string|'"faultstring"'
op|')'
op|'.'
name|'getText'
op|'('
op|')'
newline|'\n'
name|'detail'
op|'='
name|'doc'
op|'.'
name|'childAtPath'
op|'('
string|'"/Envelope/Body/Fault/detail"'
op|')'
newline|'\n'
name|'fault_list'
op|'='
op|'['
op|']'
newline|'\n'
name|'details'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'detail'
op|':'
newline|'\n'
indent|'                    '
name|'for'
name|'fault'
name|'in'
name|'detail'
op|'.'
name|'getChildren'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'fault_list'
op|'.'
name|'append'
op|'('
name|'fault'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'fault'
op|'.'
name|'getChildren'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                            '
name|'details'
op|'['
name|'child'
op|'.'
name|'name'
op|']'
op|'='
name|'child'
op|'.'
name|'getText'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'raise'
name|'error_util'
op|'.'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
name|'fault_string'
op|','
nl|'\n'
name|'details'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
name|'as'
name|'excep'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'VimAttributeError'
op|'('
name|'_'
op|'('
string|'"No such SOAP method "'
nl|'\n'
string|'"\'%s\' provided by VI SDK"'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'httplib'
op|'.'
name|'CannotSendRequest'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'ResponseNotReady'
op|','
nl|'\n'
name|'httplib'
op|'.'
name|'CannotSendHeader'
op|')'
name|'as'
name|'excep'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"httplib "'
nl|'\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'urllib2'
op|'.'
name|'URLError'
op|','
nl|'\n'
name|'urllib2'
op|'.'
name|'HTTPError'
op|')'
name|'as'
name|'excep'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'error_util'
op|'.'
name|'SessionConnectionException'
op|'('
name|'_'
op|'('
string|'"urllib2 "'
nl|'\n'
string|'"error in  %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'excep'
op|':'
newline|'\n'
comment|'# Socket errors which need special handling for they'
nl|'\n'
comment|'# might be caused by ESX API call overload'
nl|'\n'
indent|'                '
name|'msg_excep'
op|'='
name|'six'
op|'.'
name|'text_type'
op|'('
name|'excep'
op|')'
newline|'\n'
name|'if'
op|'('
name|'msg_excep'
op|'.'
name|'find'
op|'('
name|'ADDRESS_IN_USE_ERROR'
op|')'
op|'!='
op|'-'
number|'1'
name|'or'
nl|'\n'
name|'msg_excep'
op|'.'
name|'find'
op|'('
name|'CONN_ABORT_ERROR'
op|')'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Socket "'
nl|'\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
comment|'# Type error that needs special handling for it might be'
nl|'\n'
comment|'# caused by ESX host API call overload'
nl|'\n'
dedent|''
name|'elif'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'excep'
op|')'
op|'.'
name|'find'
op|'('
name|'RESP_NOT_XML_ERROR'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Type "'
nl|'\n'
string|'"error in  %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'VimException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Exception in %s "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'vim_request_handler'
newline|'\n'
nl|'\n'
DECL|member|_request_managed_object_builder
dedent|''
name|'def'
name|'_request_managed_object_builder'
op|'('
name|'self'
op|','
name|'managed_object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Builds the request managed object."""'
newline|'\n'
comment|'# Request Managed Object Builder'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'managed_object'
op|','
name|'str'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'mo'
op|'='
name|'suds'
op|'.'
name|'sudsobject'
op|'.'
name|'Property'
op|'('
name|'managed_object'
op|')'
newline|'\n'
name|'mo'
op|'.'
name|'_type'
op|'='
name|'managed_object'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mo'
op|'='
name|'managed_object'
newline|'\n'
dedent|''
name|'return'
name|'mo'
newline|'\n'
nl|'\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\n'
nl|'\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
