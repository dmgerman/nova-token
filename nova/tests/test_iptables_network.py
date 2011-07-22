begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'# All Rights Reserved.'
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
string|'"""Unit Tests for network code."""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'linux_net'
newline|'\n'
nl|'\n'
DECL|class|IpSetTestCase
name|'class'
name|'IpSetTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_add
indent|'    '
name|'def'
name|'test_add'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding an address"""'
newline|'\n'
name|'ipset'
op|'='
name|'linux_net'
op|'.'
name|'IpSet'
op|'('
string|"'somename'"
op|')'
newline|'\n'
nl|'\n'
name|'ipset'
op|'.'
name|'add_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'1.2.3.4'"
name|'in'
name|'ipset'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_add_remove
dedent|''
name|'def'
name|'test_add_remove'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding and then removing an address"""'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'verify_cmd_call_count'
op|'='
number|'0'
newline|'\n'
DECL|function|verify_cmd
name|'def'
name|'verify_cmd'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'args'
op|','
name|'self'
op|'.'
name|'expected_cmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'verify_cmd_call_count'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'expected_cmd'
op|'='
op|'('
string|"'ipset'"
op|','
string|"'-A'"
op|','
string|"'run_tests.py-somename'"
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'ipset'
op|'='
name|'linux_net'
op|'.'
name|'IpSet'
op|'('
string|"'somename'"
op|','
name|'execute'
op|'='
name|'verify_cmd'
op|')'
newline|'\n'
name|'ipset'
op|'.'
name|'add_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'1.2.3.4'"
name|'in'
name|'ipset'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'expected_cmd'
op|'='
op|'('
string|"'ipset'"
op|','
string|"'-D'"
op|','
string|"'run_tests.py-somename'"
op|','
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'ipset'
op|'.'
name|'remove_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'1.2.3.4'"
name|'not'
name|'in'
name|'ipset'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'self'
op|'.'
name|'verify_cmd_call_count'
op|','
number|'2'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|test_two_adds_one_remove
dedent|''
name|'def'
name|'test_two_adds_one_remove'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Adding the same address twice works. Removing it once removes it entirely."""'
newline|'\n'
name|'ipset'
op|'='
name|'linux_net'
op|'.'
name|'IpSet'
op|'('
string|"'somename'"
op|')'
newline|'\n'
nl|'\n'
name|'ipset'
op|'.'
name|'add_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'ipset'
op|'.'
name|'add_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'ipset'
op|'.'
name|'remove_ip'
op|'('
string|"'1.2.3.4'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'1.2.3.4'"
name|'not'
name|'in'
name|'ipset'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IptablesManagerTestCase
dedent|''
dedent|''
name|'class'
name|'IptablesManagerTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|sample_filter
indent|'    '
name|'sample_filter'
op|'='
op|'['
string|"'#Generated by iptables-save on Fri Feb 18 15:17:05 2011'"
op|','
nl|'\n'
string|"'*filter'"
op|','
nl|'\n'
string|"':INPUT ACCEPT [2223527:305688874]'"
op|','
nl|'\n'
string|"':FORWARD ACCEPT [0:0]'"
op|','
nl|'\n'
string|"':OUTPUT ACCEPT [2172501:140856656]'"
op|','
nl|'\n'
string|"':nova-compute-FORWARD - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-INPUT - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-local - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-OUTPUT - [0:0]'"
op|','
nl|'\n'
string|"':nova-filter-top - [0:0]'"
op|','
nl|'\n'
string|"'-A FORWARD -j nova-filter-top '"
op|','
nl|'\n'
string|"'-A OUTPUT -j nova-filter-top '"
op|','
nl|'\n'
string|"'-A nova-filter-top -j nova-compute-local '"
op|','
nl|'\n'
string|"'-A INPUT -j nova-compute-INPUT '"
op|','
nl|'\n'
string|"'-A OUTPUT -j nova-compute-OUTPUT '"
op|','
nl|'\n'
string|"'-A FORWARD -j nova-compute-FORWARD '"
op|','
nl|'\n'
string|"'-A INPUT -i virbr0 -p udp -m udp --dport 53 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A INPUT -i virbr0 -p tcp -m tcp --dport 53 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A INPUT -i virbr0 -p udp -m udp --dport 67 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A INPUT -i virbr0 -p tcp -m tcp --dport 67 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A FORWARD -s 192.168.122.0/24 -i virbr0 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A FORWARD -i virbr0 -o virbr0 -j ACCEPT '"
op|','
nl|'\n'
string|"'-A FORWARD -o virbr0 -j REJECT --reject-with '"
nl|'\n'
string|"'icmp-port-unreachable '"
op|','
nl|'\n'
string|"'-A FORWARD -i virbr0 -j REJECT --reject-with '"
nl|'\n'
string|"'icmp-port-unreachable '"
op|','
nl|'\n'
string|"'COMMIT'"
op|','
nl|'\n'
string|"'# Completed on Fri Feb 18 15:17:05 2011'"
op|']'
newline|'\n'
nl|'\n'
DECL|variable|sample_nat
name|'sample_nat'
op|'='
op|'['
string|"'# Generated by iptables-save on Fri Feb 18 15:17:05 2011'"
op|','
nl|'\n'
string|"'*nat'"
op|','
nl|'\n'
string|"':PREROUTING ACCEPT [3936:762355]'"
op|','
nl|'\n'
string|"':INPUT ACCEPT [2447:225266]'"
op|','
nl|'\n'
string|"':OUTPUT ACCEPT [63491:4191863]'"
op|','
nl|'\n'
string|"':POSTROUTING ACCEPT [63112:4108641]'"
op|','
nl|'\n'
string|"':nova-compute-OUTPUT - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-floating-ip-snat - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-SNATTING - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-PREROUTING - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-POSTROUTING - [0:0]'"
op|','
nl|'\n'
string|"':nova-postrouting-bottom - [0:0]'"
op|','
nl|'\n'
string|"'-A PREROUTING -j nova-compute-PREROUTING '"
op|','
nl|'\n'
string|"'-A OUTPUT -j nova-compute-OUTPUT '"
op|','
nl|'\n'
string|"'-A POSTROUTING -j nova-compute-POSTROUTING '"
op|','
nl|'\n'
string|"'-A POSTROUTING -j nova-postrouting-bottom '"
op|','
nl|'\n'
string|"'-A nova-postrouting-bottom -j nova-compute-SNATTING '"
op|','
nl|'\n'
string|"'-A nova-compute-SNATTING -j nova-compute-floating-ip-snat '"
op|','
nl|'\n'
string|"'COMMIT'"
op|','
nl|'\n'
string|"'# Completed on Fri Feb 18 15:17:05 2011'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'IptablesManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'manager'
op|'='
name|'linux_net'
op|'.'
name|'IptablesManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_rules_are_wrapped
dedent|''
name|'def'
name|'test_filter_rules_are_wrapped'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_filter'
newline|'\n'
nl|'\n'
name|'table'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
newline|'\n'
name|'table'
op|'.'
name|'add_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-A run_tests.py-FORWARD '"
nl|'\n'
string|"'-s 1.2.3.4/5 -j DROP'"
name|'in'
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
name|'table'
op|'.'
name|'remove_rule'
op|'('
string|"'FORWARD'"
op|','
string|"'-s 1.2.3.4/5 -j DROP'"
op|')'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
name|'table'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-A run_tests.py-FORWARD '"
nl|'\n'
string|"'-s 1.2.3.4/5 -j DROP'"
name|'not'
name|'in'
name|'new_lines'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nat_rules
dedent|''
name|'def'
name|'test_nat_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_nat'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'nat'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
op|'['
string|"':nova-compute-OUTPUT - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-floating-ip-snat - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-SNATTING - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-PREROUTING - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-POSTROUTING - [0:0]'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'in'
name|'new_lines'
op|','
string|'"One of nova-compute\'s chains "'
nl|'\n'
string|'"went missing."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'seen_lines'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'not'
name|'in'
name|'seen_lines'
op|','
nl|'\n'
string|'"Duplicate line: %s"'
op|'%'
name|'line'
op|')'
newline|'\n'
name|'seen_lines'
op|'.'
name|'add'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'last_postrouting_line'
op|'='
string|"''"
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'-A POSTROUTING'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'last_postrouting_line'
op|'='
name|'line'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-j nova-postrouting-bottom'"
name|'in'
name|'last_postrouting_line'
op|','
nl|'\n'
string|'"Last POSTROUTING rule does not jump to "'
nl|'\n'
string|'"nova-postouting-bottom: %s"'
op|'%'
name|'last_postrouting_line'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'chain'
name|'in'
op|'['
string|"'POSTROUTING'"
op|','
string|"'PREROUTING'"
op|','
string|"'OUTPUT'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-A %s -j run_tests.py-%s'"
op|'%'
op|'('
name|'chain'
op|','
name|'chain'
op|')'
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"Built-in chain %s not wrapped"'
op|'%'
op|'('
name|'chain'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_filter_rules
dedent|''
dedent|''
name|'def'
name|'test_filter_rules'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'current_lines'
op|'='
name|'self'
op|'.'
name|'sample_filter'
newline|'\n'
name|'new_lines'
op|'='
name|'self'
op|'.'
name|'manager'
op|'.'
name|'_modify_rules'
op|'('
name|'current_lines'
op|','
nl|'\n'
name|'self'
op|'.'
name|'manager'
op|'.'
name|'ipv4'
op|'['
string|"'filter'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'line'
name|'in'
op|'['
string|"':nova-compute-FORWARD - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-INPUT - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-local - [0:0]'"
op|','
nl|'\n'
string|"':nova-compute-OUTPUT - [0:0]'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'in'
name|'new_lines'
op|','
string|'"One of nova-compute\'s chains"'
nl|'\n'
string|'" went missing."'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'seen_lines'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'line'
name|'not'
name|'in'
name|'seen_lines'
op|','
nl|'\n'
string|'"Duplicate line: %s"'
op|'%'
name|'line'
op|')'
newline|'\n'
name|'seen_lines'
op|'.'
name|'add'
op|'('
name|'line'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'chain'
name|'in'
op|'['
string|"'FORWARD'"
op|','
string|"'OUTPUT'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'line'
name|'in'
name|'new_lines'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
string|"'-A %s'"
op|'%'
name|'chain'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-j nova-filter-top'"
name|'in'
name|'line'
op|','
nl|'\n'
string|'"First %s rule does not "'
nl|'\n'
string|'"jump to nova-filter-top"'
op|'%'
name|'chain'
op|')'
newline|'\n'
name|'break'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-A nova-filter-top '"
nl|'\n'
string|"'-j run_tests.py-local'"
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"nova-filter-top does not jump to wrapped local chain"'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'chain'
name|'in'
op|'['
string|"'INPUT'"
op|','
string|"'OUTPUT'"
op|','
string|"'FORWARD'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'-A %s -j run_tests.py-%s'"
op|'%'
op|'('
name|'chain'
op|','
name|'chain'
op|')'
name|'in'
name|'new_lines'
op|','
nl|'\n'
string|'"Built-in chain %s not wrapped"'
op|'%'
op|'('
name|'chain'
op|','
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
