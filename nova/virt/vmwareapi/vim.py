begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\r\n'
nl|'\r\n'
comment|'# Copyright (c) 2011 Citrix Systems, Inc.'
nl|'\r\n'
comment|'# Copyright 2011 OpenStack LLC.'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\r\n'
comment|'#    not use this file except in compliance with the License. You may obtain'
nl|'\r\n'
comment|'#    a copy of the License at'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#         http://www.apache.org/licenses/LICENSE-2.0'
nl|'\r\n'
comment|'#'
nl|'\r\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\r\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\r\n'
comment|'#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\r\n'
comment|'#    License for the specific language governing permissions and limitations'
nl|'\r\n'
comment|'#    under the License.'
nl|'\r\n'
nl|'\r\n'
string|'"""\r\nClasses that facilitate SOAP calls for VMware VI API.\r\n"""'
newline|'\r\n'
nl|'\r\n'
name|'import'
name|'httplib'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'suds'
name|'import'
name|'WebFault'
newline|'\r\n'
name|'from'
name|'suds'
op|'.'
name|'client'
name|'import'
name|'Client'
newline|'\r\n'
name|'from'
name|'suds'
op|'.'
name|'plugin'
name|'import'
name|'MessagePlugin'
newline|'\r\n'
name|'from'
name|'suds'
op|'.'
name|'sudsobject'
name|'import'
name|'Property'
newline|'\r\n'
nl|'\r\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\r\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'error_util'
newline|'\r\n'
nl|'\r\n'
DECL|variable|RESP_NOT_XML_ERROR
name|'RESP_NOT_XML_ERROR'
op|'='
string|'\'Response is "text/html", not "text/xml"\''
newline|'\r\n'
DECL|variable|CONN_ABORT_ERROR
name|'CONN_ABORT_ERROR'
op|'='
string|"'Software caused connection abort'"
newline|'\r\n'
DECL|variable|ADDRESS_IN_USE_ERROR
name|'ADDRESS_IN_USE_ERROR'
op|'='
string|"'Address already in use'"
newline|'\r\n'
nl|'\r\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\r\n'
name|'flags'
op|'.'
name|'DEFINE_string'
op|'('
string|"'vmwareapi_wsdl_loc'"
op|','
nl|'\r\n'
name|'None'
op|','
nl|'\r\n'
string|"'VIM Service WSDL Location'"
nl|'\r\n'
string|"'e.g http://<server>/vimService.wsdl'"
nl|'\r\n'
string|"'Due to a bug in vSphere ESX 4.1 default wsdl'"
nl|'\r\n'
string|"'Refer readme-vmware to setup'"
op|')'
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|VIMMessagePlugin
name|'class'
name|'VIMMessagePlugin'
op|'('
name|'MessagePlugin'
op|')'
op|':'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
comment|'# suds does not handle AnyType properly.'
nl|'\r\n'
comment|'# VI SDK requires type attribute to be set when AnyType is used'
nl|'\r\n'
indent|'        '
name|'if'
name|'node'
op|'.'
name|'name'
op|'=='
string|"'value'"
op|':'
newline|'\r\n'
indent|'            '
name|'node'
op|'.'
name|'set'
op|'('
string|"'xsi:type'"
op|','
string|"'xsd:string'"
op|')'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
indent|'        '
string|'"""suds will send the specified soap envelope.\r\n        Provides the plugin with the opportunity to prune empty\r\n        nodes and fixup nodes before sending it to the server.\r\n        """'
newline|'\r\n'
comment|'# suds builds the entire request object based on the wsdl schema.'
nl|'\r\n'
comment|'# VI SDK throws server errors if optional SOAP nodes are sent without'
nl|'\r\n'
comment|'# values, e.g. <test/> as opposed to <test>test</test>'
nl|'\r\n'
name|'context'
op|'.'
name|'envelope'
op|'.'
name|'prune'
op|'('
op|')'
newline|'\r\n'
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
newline|'\r\n'
nl|'\r\n'
nl|'\r\n'
DECL|class|Vim
dedent|''
dedent|''
name|'class'
name|'Vim'
op|':'
newline|'\r\n'
indent|'    '
string|'"""The VIM Object."""'
newline|'\r\n'
nl|'\r\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
nl|'\r\n'
name|'protocol'
op|'='
string|'"https"'
op|','
nl|'\r\n'
name|'host'
op|'='
string|'"localhost"'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""\r\n        Creates the necessary Communication interfaces and gets the\r\n        ServiceContent for initiating SOAP transactions.\r\n\r\n        protocol: http or https\r\n        host    : ESX IPAddress[:port] or ESX Hostname[:port]\r\n        """'
newline|'\r\n'
name|'self'
op|'.'
name|'_protocol'
op|'='
name|'protocol'
newline|'\r\n'
name|'self'
op|'.'
name|'_host_name'
op|'='
name|'host'
newline|'\r\n'
name|'wsdl_url'
op|'='
name|'FLAGS'
op|'.'
name|'vmwareapi_wsdl_loc'
newline|'\r\n'
name|'if'
name|'wsdl_url'
name|'is'
name|'None'
op|':'
newline|'\r\n'
indent|'            '
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|'"Must specify vmwareapi_wsdl_loc"'
op|')'
op|')'
newline|'\r\n'
comment|'# Use this when VMware fixes their faulty wsdl'
nl|'\r\n'
comment|"#wsdl_url = '%s://%s/sdk/vimService.wsdl' % (self._protocol,"
nl|'\r\n'
comment|'#        self._host_name)'
nl|'\r\n'
dedent|''
name|'url'
op|'='
string|"'%s://%s/sdk'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_protocol'
op|','
name|'self'
op|'.'
name|'_host_name'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'Client'
op|'('
name|'wsdl_url'
op|','
name|'location'
op|'='
name|'url'
op|','
nl|'\r\n'
name|'plugins'
op|'='
op|'['
name|'VIMMessagePlugin'
op|'('
op|')'
op|']'
op|')'
newline|'\r\n'
name|'self'
op|'.'
name|'_service_content'
op|'='
name|'self'
op|'.'
name|'RetrieveServiceContent'
op|'('
string|'"ServiceInstance"'
op|')'
newline|'\r\n'
nl|'\r\n'
DECL|member|get_service_content
dedent|''
name|'def'
name|'get_service_content'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Gets the service content object."""'
newline|'\r\n'
name|'return'
name|'self'
op|'.'
name|'_service_content'
newline|'\r\n'
nl|'\r\n'
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
newline|'\r\n'
indent|'        '
string|'"""Makes the API calls and gets the result."""'
newline|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'            '
name|'return'
name|'object'
op|'.'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attr_name'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\r\n'
nl|'\r\n'
DECL|function|vim_request_handler
indent|'            '
name|'def'
name|'vim_request_handler'
op|'('
name|'managed_object'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\r\n'
indent|'                '
string|'"""\r\n                Builds the SOAP message and parses the response for fault\r\n                checking and other errors.\r\n\r\n                managed_object    : Managed Object Reference or Managed\r\n                                    Object Name\r\n                **kwargs          : Keyword arguments of the call\r\n                """'
newline|'\r\n'
comment|'# Dynamic handler for VI SDK Calls'
nl|'\r\n'
name|'try'
op|':'
newline|'\r\n'
indent|'                    '
name|'request_mo'
op|'='
name|'self'
op|'.'
name|'_request_managed_object_builder'
op|'('
name|'managed_object'
op|')'
newline|'\r\n'
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
newline|'\r\n'
name|'response'
op|'='
name|'request'
op|'('
name|'request_mo'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\r\n'
comment|'# To check for the faults that are part of the message body'
nl|'\r\n'
comment|'# and not returned as Fault object response from the ESX'
nl|'\r\n'
comment|'# SOAP server'
nl|'\r\n'
name|'if'
name|'hasattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\r\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
op|':'
newline|'\r\n'
indent|'                        '
name|'fault_checker'
op|'='
name|'getattr'
op|'('
name|'error_util'
op|'.'
name|'FaultCheckers'
op|','
nl|'\r\n'
name|'attr_name'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
string|'"_fault_checker"'
op|')'
newline|'\r\n'
name|'fault_checker'
op|'('
name|'response'
op|')'
newline|'\r\n'
dedent|''
name|'return'
name|'response'
newline|'\r\n'
comment|'# Catch the VimFaultException that is raised by the fault'
nl|'\r\n'
comment|'# check of the SOAP response'
nl|'\r\n'
dedent|''
name|'except'
name|'error_util'
op|'.'
name|'VimFaultException'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
newline|'\r\n'
dedent|''
name|'except'
name|'WebFault'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'doc'
op|'='
name|'excep'
op|'.'
name|'document'
newline|'\r\n'
name|'detail'
op|'='
name|'doc'
op|'.'
name|'childAtPath'
op|'('
string|'"/Envelope/Body/Fault/detail"'
op|')'
newline|'\r\n'
name|'fault_list'
op|'='
op|'['
op|']'
newline|'\r\n'
name|'for'
name|'child'
name|'in'
name|'detail'
op|'.'
name|'getChildren'
op|'('
op|')'
op|':'
newline|'\r\n'
indent|'                        '
name|'fault_list'
op|'.'
name|'append'
op|'('
name|'child'
op|'.'
name|'get'
op|'('
string|'"type"'
op|')'
op|')'
newline|'\r\n'
dedent|''
name|'raise'
name|'error_util'
op|'.'
name|'VimFaultException'
op|'('
name|'fault_list'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'AttributeError'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'VimAttributeError'
op|'('
name|'_'
op|'('
string|'"No such SOAP method "'
nl|'\r\n'
string|'"\'%s\' provided by VI SDK"'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
op|'('
name|'httplib'
op|'.'
name|'CannotSendRequest'
op|','
nl|'\r\n'
name|'httplib'
op|'.'
name|'ResponseNotReady'
op|','
nl|'\r\n'
name|'httplib'
op|'.'
name|'CannotSendHeader'
op|')'
op|','
name|'excep'
op|':'
newline|'\r\n'
indent|'                    '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"httplib "'
nl|'\r\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'except'
name|'Exception'
op|','
name|'excep'
op|':'
newline|'\r\n'
comment|'# Socket errors which need special handling for they'
nl|'\r\n'
comment|'# might be caused by ESX API call overload'
nl|'\r\n'
indent|'                    '
name|'if'
op|'('
name|'str'
op|'('
name|'excep'
op|')'
op|'.'
name|'find'
op|'('
name|'ADDRESS_IN_USE_ERROR'
op|')'
op|'!='
op|'-'
number|'1'
name|'or'
nl|'\r\n'
name|'str'
op|'('
name|'excep'
op|')'
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
newline|'\r\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Socket "'
nl|'\r\n'
string|'"error in %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
comment|'# Type error that needs special handling for it might be'
nl|'\r\n'
comment|'# caused by ESX host API call overload'
nl|'\r\n'
dedent|''
name|'elif'
name|'str'
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
newline|'\r\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'SessionOverLoadException'
op|'('
name|'_'
op|'('
string|'"Type "'
nl|'\r\n'
string|'"error in  %s: "'
op|')'
op|'%'
op|'('
name|'attr_name'
op|')'
op|','
name|'excep'
op|')'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'                        '
name|'raise'
name|'error_util'
op|'.'
name|'VimException'
op|'('
nl|'\r\n'
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
newline|'\r\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'vim_request_handler'
newline|'\r\n'
nl|'\r\n'
DECL|member|_request_managed_object_builder
dedent|''
dedent|''
name|'def'
name|'_request_managed_object_builder'
op|'('
name|'self'
op|','
name|'managed_object'
op|')'
op|':'
newline|'\r\n'
indent|'        '
string|'"""Builds the request managed object."""'
newline|'\r\n'
comment|'# Request Managed Object Builder'
nl|'\r\n'
name|'if'
name|'type'
op|'('
name|'managed_object'
op|')'
op|'=='
name|'type'
op|'('
string|'""'
op|')'
op|':'
newline|'\r\n'
indent|'            '
name|'mo'
op|'='
name|'Property'
op|'('
name|'managed_object'
op|')'
newline|'\r\n'
name|'mo'
op|'.'
name|'_type'
op|'='
name|'managed_object'
newline|'\r\n'
dedent|''
name|'else'
op|':'
newline|'\r\n'
indent|'            '
name|'mo'
op|'='
name|'managed_object'
newline|'\r\n'
dedent|''
name|'return'
name|'mo'
newline|'\r\n'
nl|'\r\n'
DECL|member|__repr__
dedent|''
name|'def'
name|'__repr__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\r\n'
nl|'\r\n'
DECL|member|__str__
dedent|''
name|'def'
name|'__str__'
op|'('
name|'self'
op|')'
op|':'
newline|'\r\n'
indent|'        '
name|'return'
string|'"VIM Object"'
newline|'\r\n'
dedent|''
dedent|''
endmarker|''
end_unit
