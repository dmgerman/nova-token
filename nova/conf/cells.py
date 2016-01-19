begin_unit
comment|'# Copyright 2015 OpenStack Foundation'
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
nl|'\n'
name|'import'
name|'itertools'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|cells_opts
name|'cells_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'enable'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nEnable cell functionality\n\nWhen this functionality is enabled, it lets you to scale an OpenStack\nCompute cloud in a more distributed fashion without having to use\ncomplicated technologies like database and message queue clustering.\nCells are configured as a tree. The top-level cell should have a host\nthat runs a nova-api service, but no nova-compute services. Each\nchild cell should run all of the typical nova-* services in a regular\nCompute cloud except for nova-api. You can think of cells as a normal\nCompute deployment in that each cell has its own database server and\nmessage queue broker.\n\nPossible values:\n\n* True: Enables the feature\n* False: Disables the feature\n\nServices which consume this:\n\n* nova-api\n* nova-cells\n* nova-compute\n\nRelated options:\n\n* name: A unique cell name must be given when this functionality\n  is enabled.\n* cell_type: Cell type should be defined for all cells.\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'topic'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cells'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nTopic\n\nThis is the message queue topic that cells nodes listen on. It is\nused when the cells service is started up to configure the queue,\nand whenever an RPC call to the scheduler is made.\n\nPossible values:\n\n* cells: This is the recommended and the default value.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'manager'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cells.manager.CellsManager'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nManager for cells\n\nThe nova-cells manager class. This class defines RPC methods that\nthe local cell may call. This class is NOT used for messages coming\nfrom other cells. That communication is driver-specific.\n\nCommunication to other cells happens via the nova.cells.messaging module.\nThe MessageRunner from that module will handle routing the message to\nthe correct cell via the communication driver. Most methods below\ncreate \'targeted\' (where we want to route a message to a specific cell)\nor \'broadcast\' (where we want a message to go to multiple cells)\nmessages.\n\nScheduling requests get passed to the scheduler class.\n\nPossible values:\n\n* \'nova.cells.manager.CellsManager\' is the only possible value for\n  this option as of the Mitaka release\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nName of the current cell\n\nThis value must be unique for each cell. Name of a cell is used as\nits id, leaving this option unset or setting the same name for\ntwo or more cells may cause unexpected behaviour.\n\nPossible values:\n\n* Unique name string\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* enabled: This option is meaningful only when cells service\n  is enabled\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'capabilities'"
op|','
nl|'\n'
name|'default'
op|'='
op|'['
string|"'hypervisor=xenserver;kvm'"
op|','
string|"'os=linux;windows'"
op|']'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nCell capabilities\n\nList of arbitrary key=value pairs defining capabilities of the\ncurrent cell to be sent to the parent cells. These capabilities\nare intended to be used in cells scheduler filters/weighers.\n\nPossible values:\n\n* key=value pairs list for example;\n  ``hypervisor=xenserver;kvm,os=linux;windows``\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'call_timeout'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
name|'help'
op|'='
string|'"""\nCall timeout\n\nCell messaging module waits for response(s) to be put into the\neventlet queue. This option defines the seconds waited for\nresponse from a call to a cell.\n\nPossible values:\n\n* Time in seconds.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'reserve_percent'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Percentage of cell capacity to hold in reserve. '"
nl|'\n'
string|"'Affects both memory and disk utilization'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cell_type'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'compute'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'api'"
op|','
string|"'compute'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Type of cell'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"mute_child_interval"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'300'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of seconds after which a lack of capability and '"
nl|'\n'
string|"'capacity updates signals the child cell is to be '"
nl|'\n'
string|"'treated as a mute.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'bandwidth_update_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Seconds between bandwidth updates for cells.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'instance_update_sync_database_limit'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'100'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Number of instances to pull from the database at one '"
nl|'\n'
string|"'time for a sync.  If there are more instances to update '"
nl|'\n'
string|"'the results will be paged through'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|mute_weigher_opts
name|'mute_weigher_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'mute_weight_multiplier'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'-'
number|'10000.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Multiplier used to weigh mute children. (The value '"
nl|'\n'
string|"'should be negative.)'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|ram_weigher_opts
name|'ram_weigher_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'ram_weight_multiplier'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Multiplier used for weighing ram.  Negative '"
nl|'\n'
string|"'numbers mean to stack vs spread.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|weigher_opts
name|'weigher_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|"'offset_weight_multiplier'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Multiplier used to weigh offset weigher.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cell_manager_opts
name|'cell_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'driver'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cells.rpc_driver.CellsRPCDriver'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cells communication driver to use'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"instance_updated_at_threshold"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3600'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of seconds after an instance was updated "'
nl|'\n'
string|'"or deleted to continue to update cells"'
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|'"instance_update_num_instances"'
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Number of instances to update per periodic task run"'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cell_messaging_opts
name|'cell_messaging_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'max_hop_count'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Maximum number of hops for cells routing.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'scheduler'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova.cells.scheduler.CellsScheduler'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Cells scheduler to use'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cell_rpc_driver_opts
name|'cell_rpc_driver_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'rpc_driver_queue_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'cells.intercell'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"Base queue name to use when communicating between "'
nl|'\n'
string|'"cells.  Various topics by message type will be "'
nl|'\n'
string|'"appended to this."'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cell_scheduler_opts
name|'cell_scheduler_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_filter_classes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.cells.filters.all_filters'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Filter classes the cells scheduler should use.  '"
nl|'\n'
string|'\'An entry of "nova.cells.filters.all_filters" \''
nl|'\n'
string|"'maps to all cells filters included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'scheduler_weight_classes'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'nova.cells.weights.all_weighers'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Weigher classes the cells scheduler should use.  '"
nl|'\n'
string|'\'An entry of "nova.cells.weights.all_weighers" \''
nl|'\n'
string|"'maps to all cell weighers included with nova.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_retries'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'10'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How many retries when no cells are available.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'scheduler_retry_delay'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'How often to retry in seconds when no cells are '"
nl|'\n'
string|"'available.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|cell_state_manager_opts
name|'cell_state_manager_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'db_check_interval'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'60'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Interval, in seconds, for getting fresh cell '"
nl|'\n'
string|"'information from the database.'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cells_config'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Configuration file from which to read cells '"
nl|'\n'
string|"'configuration.  If given, overrides reading cells '"
nl|'\n'
string|"'from the database.'"
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_intercell_opt
name|'rpcapi_cap_intercell_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'intercell'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent between cells services'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|rpcapi_cap_cells_opt
name|'rpcapi_cap_cells_opt'
op|'='
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'cells'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Set a version cap for messages sent to local cells services'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|ALL_CELLS_OPTS
name|'ALL_CELLS_OPTS'
op|'='
name|'list'
op|'('
name|'itertools'
op|'.'
name|'chain'
op|'('
nl|'\n'
name|'cells_opts'
op|','
nl|'\n'
name|'mute_weigher_opts'
op|','
nl|'\n'
name|'ram_weigher_opts'
op|','
nl|'\n'
name|'weigher_opts'
op|','
nl|'\n'
name|'cell_manager_opts'
op|','
nl|'\n'
name|'cell_messaging_opts'
op|','
nl|'\n'
name|'cell_rpc_driver_opts'
op|','
nl|'\n'
name|'cell_scheduler_opts'
op|','
nl|'\n'
name|'cell_state_manager_opts'
nl|'\n'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ALL_RPCAPI_CAP_OPTS
name|'ALL_RPCAPI_CAP_OPTS'
op|'='
op|'['
name|'rpcapi_cap_intercell_opt'
op|','
nl|'\n'
name|'rpcapi_cap_cells_opt'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|register_opts
name|'def'
name|'register_opts'
op|'('
name|'conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_CELLS_OPTS'
op|','
name|'group'
op|'='
string|'"cells"'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'register_opts'
op|'('
name|'ALL_RPCAPI_CAP_OPTS'
op|','
name|'group'
op|'='
string|'"upgrade_levels"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|list_opts
dedent|''
name|'def'
name|'list_opts'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
nl|'\n'
string|"'cells'"
op|':'
name|'ALL_CELLS_OPTS'
op|','
nl|'\n'
string|"'upgrade_levels'"
op|':'
name|'ALL_RPCAPI_CAP_OPTS'
op|','
nl|'\n'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit