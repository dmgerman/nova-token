begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# Copyright (c) 2010 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Licensed under the Apache License, Version 2.0 (the "License");'
nl|'\n'
comment|'#    you may not use this file except in compliance with the License.'
nl|'\n'
comment|'#    You may obtain a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#        http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#    distributed under the License is distributed on an "AS IS" BASIS,'
nl|'\n'
comment|'#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.'
nl|'\n'
comment|'#    See the License for the specific language governing permissions and'
nl|'\n'
comment|'#    limitations under the License.'
nl|'\n'
nl|'\n'
string|'"""Module for VNC Proxying."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|vnc_opts
name|'vnc_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'novncproxy_base_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http://127.0.0.1:6080/vnc_auto.html'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location of VNC console proxy, in the form '"
nl|'\n'
string|'\'"http://127.0.0.1:6080/vnc_auto.html"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'xvpvncproxy_base_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'http://127.0.0.1:6081/console'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Location of nova xvp VNC console proxy, in the form '"
nl|'\n'
string|'\'"http://127.0.0.1:6081/console"\''
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vncserver_listen'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address on which instance vncservers should listen'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vncserver_proxyclient_address'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'127.0.0.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'The address to which proxy clients '"
nl|'\n'
string|"'(like nova-xvpvncproxy) should connect'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'vnc_enabled'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Enable VNC related features'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vnc_keymap'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'en-us'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Keymap for VNC'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'vnc_opts'
op|')'
newline|'\n'
endmarker|''
end_unit
