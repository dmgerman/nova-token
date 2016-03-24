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
string|'"""\nDEPRECATED: Manager for cells\n\nThe nova-cells manager class. This class defines RPC methods that\nthe local cell may call. This class is NOT used for messages coming\nfrom other cells. That communication is driver-specific.\n\nCommunication to other cells happens via the nova.cells.messaging module.\nThe MessageRunner from that module will handle routing the message to\nthe correct cell via the communication driver. Most methods below\ncreate \'targeted\' (where we want to route a message to a specific cell)\nor \'broadcast\' (where we want a message to go to multiple cells)\nmessages.\n\nScheduling requests get passed to the scheduler class.\n\nPossible values:\n\n* \'nova.cells.manager.CellsManager\' is the only possible value for\n  this option as of the Mitaka release\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|','
nl|'\n'
DECL|variable|deprecated_for_removal
name|'deprecated_for_removal'
op|'='
name|'True'
nl|'\n'
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
name|'help'
op|'='
string|'"""\nReserve percentage\n\nPercentage of cell capacity to hold in reserve, so the minimum\namount of free resource is considered to be;\n  min_free = total * (reserve_percent / 100.0)\nThis option affects both memory and disk utilization.\nThe primary purpose of this reserve is to ensure some space is\navailable for users who want to resize their instance to be larger.\nNote that currently once the capacity expands into this reserve\nspace this option is ignored.\n\nPossible values:\n\n* Float percentage value\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nType of cell\n\nWhen cells feature is enabled the hosts in the OpenStack Compute\ncloud are partitioned into groups. Cells are configured as a tree.\nThe top-level cell\'s cell_type must be set to ``api``. All other\ncells are defined as a ``compute cell`` by default.\n\nPossible values:\n\n* api: Cell type of top-level cell.\n* compute: Cell type of all child cells. (Default)\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* compute_api_class: This option must be set to cells api driver\n  for the top-level cell (nova.compute.cells_api.ComputeCellsAPI)\n* quota_driver: Disable quota checking for the child cells.\n  (nova.quota.NoopQuotaDriver)\n"""'
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
name|'help'
op|'='
string|'"""\nMute child interval\n\nNumber of seconds after which a lack of capability and capacity\nupdate the child cell is to be treated as a mute cell. Then the\nchild cell will be weighed as recommend highly that it be skipped.\n\nPossible values:\n\n* Time in seconds.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nBandwidth update interval\n\nSeconds between bandwidth usage cache updates for cells.\n\nPossible values:\n\n* Time in seconds.\n\nServices which consume this:\n\n* nova-compute\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nInstance update sync database limit\n\nNumber of instances to pull from the database at one time for\na sync. If there are more instances to update the results will\nbe paged through.\n\nPossible values:\n\n* Number of instances.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nMute weight multiplier\n\nMultiplier used to weigh mute children. Mute children cells are\nrecommended to be skipped so their weight is multiplied by this\nnegative value.\n\nPossible values:\n\n* Negative numeric number\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nRam weight multiplier\n\nMultiplier used for weighing ram. Negative numbers indicate that\nCompute should stack VMs on one host instead of spreading out new\nVMs to more hosts in the cell.\n\nPossible values:\n\n* Numeric multiplier\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nOffset weight multiplier\n\nMultiplier used to weigh offset weigher. Cells with higher\nweight_offsets in the DB will be preferred. The weight_offset\nis a property of a cell stored in the database. It can be used\nby a deployer to have scheduling decisions favor or disfavor\ncells based on the setting.\n\nPossible values:\n\n* Numeric multiplier\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nCells communication driver\n\nDriver for cell<->cell communication via RPC. This is used to\nsetup the RPC consumers as well as to send a message to another cell.\n\'nova.cells.rpc_driver.CellsRPCDriver\' starts up 2 separate servers\nfor handling inter-cell communication via RPC.\n\nPossible values:\n\n* \'nova.cells.rpc_driver.CellsRPCDriver\' is the default driver\n* Otherwise it should be the full Python path to the class to be used\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nInstance updated at threshold\n\nNumber of seconds after an instance was updated or deleted to\ncontinue to update cells. This option lets cells manager to only\nattempt to sync instances that have been updated recently.\ni.e., a threshold of 3600 means to only update instances that\nhave modified in the last hour.\n\nPossible values:\n\n* Threshold in seconds\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* This value is used with the ``instance_update_num_instances``\n  value in a periodic task run.\n"""'
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
name|'help'
op|'='
string|'"""\nInstance update num instances\n\nOn every run of the periodic task, nova cells manager will attempt to\nsync instance_updated_at_threshold number of instances. When the\nmanager gets the list of instances, it shuffles them so that multiple\nnova-cells services do not attempt to sync the same instances in\nlockstep.\n\nPossible values:\n\n* Positive integer number\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* This value is used with the ``instance_updated_at_threshold``\n  value in a periodic task run.\n"""'
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
name|'help'
op|'='
string|'"""\nMaximum hop count\n\nWhen processing a targeted message, if the local cell is not the\ntarget, a route is defined between neighbouring cells. And the\nmessage is processed across the whole routing path. This option\ndefines the maximum hop counts until reaching the target.\n\nPossible values:\n\n* Positive integer value\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nCells scheduler\n\nThe class of the driver used by the cells scheduler. This should be\nthe full Python path to the class to be used. If nothing is specified\nin this option, the CellsScheduler is used.\n\n\nPossible values:\n\n* \'nova.cells.scheduler.CellsScheduler\' is the default option\n* Otherwise it should be the full Python path to the class to be used\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nRPC driver queue base\n\nWhen sending a message to another cell by JSON-ifying the message\nand making an RPC cast to \'process_message\', a base queue is used.\nThis option defines the base queue name to be used when communicating\nbetween cells. Various topics by message type will be appended to this.\n\nPossible values:\n\n* The base queue name to be used when communicating between cells.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nScheduler filter classes\n\nFilter classes the cells scheduler should use. An entry of\n"nova.cells.filters.all_filters" maps to all cells filters\nincluded with nova. As of the Mitaka release the following\nfilter classes are available:\n\nDifferent cell filter: A scheduler hint of \'different_cell\'\nwith a value of a full cell name may be specified to route\na build away from a particular cell.\n\nImage properties filter: Image metadata named\n\'hypervisor_version_requires\' with a version specification\nmay be specified to ensure the build goes to a cell which\nhas hypervisors of the required version. If either the version\nrequirement on the image or the hypervisor capability of the\ncell is not present, this filter returns without filtering out\nthe cells.\n\nTarget cell filter: A scheduler hint of \'target_cell\' with a\nvalue of a full cell name may be specified to route a build to\na particular cell. No error handling is done as there\'s no way\nto know whether the full path is a valid.\n\nAs an admin user, you can also add a filter that directs builds\nto a particular cell.\n\n\nPossible values:\n\n* \'nova.cells.filters.all_filters\' is the default option\n* Otherwise it should be the full Python path to the class to be used\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nScheduler weight classes\n\nWeigher classes the cells scheduler should use. An entry of\n"nova.cells.weights.all_weighers" maps to all cell weighers\nincluded with nova. As of the Mitaka release the following\nweight classes are available:\n\nmute_child: Downgrades the likelihood of child cells being\nchosen for scheduling requests, which haven\'t sent capacity\nor capability updates in a while. Options include\nmute_weight_multiplier (multiplier for mute children; value\nshould be negative).\n\nram_by_instance_type: Select cells with the most RAM capacity\nfor the instance type being requested. Because higher weights\nwin, Compute returns the number of available units for the\ninstance type requested. The ram_weight_multiplier option defaults\nto 10.0 that adds to the weight by a factor of 10. Use a negative\nnumber to stack VMs on one host instead of spreading out new VMs\nto more hosts in the cell.\n\nweight_offset: Allows modifying the database to weight a particular\ncell. The highest weight will be the first cell to be scheduled for\nlaunching an instance. When the weight_offset of a cell is set to 0,\nit is unlikely to be picked but it could be picked if other cells\nhave a lower weight, like if they\'re full. And when the weight_offset\nis set to a very high value (for example, \'999999999999999\'), it is\nlikely to be picked if another cell do not have a higher weight.\n\nPossible values:\n\n* \'nova.cells.weights.all_weighers\' is the default option\n* Otherwise it should be the full Python path to the class to be used\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nScheduler retries\n\nHow many retries when no cells are available. Specifies how many\ntimes the scheduler tries to launch a new instance when no cells\nare available.\n\nPossible values:\n\n* Positive integer value\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* This value is used with the ``scheduler_retry_delay`` value\n  while retrying to find a suitable cell.\n"""'
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
name|'help'
op|'='
string|'"""\nScheduler retry delay\n\nSpecifies the delay (in seconds) between scheduling retries when no\ncell can be found to place the new instance on. When the instance\ncould not be scheduled to a cell after ``scheduler_retries`` in\ncombination with ``scheduler_retry_delay``, then the scheduling\nof the instance failed.\n\nPossible values:\n\n* Time in seconds.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* This value is used with the ``scheduler_retries`` value\n  while retrying to find a suitable cell.\n"""'
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
name|'help'
op|'='
string|'"""\nDB check interval\n\nCell state manager updates cell status for all cells from the DB\nonly after this particular interval time is passed. Otherwise cached\nstatus are used. If this value is 0 or negative all cell status are\nupdated from the DB whenever a state is needed.\n\nPossible values:\n\n* Interval time, in seconds.\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
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
name|'help'
op|'='
string|'"""\nOptional cells configuration\n\nConfiguration file from which to read cells configuration. If given,\noverrides reading cells from the database.\n\nCells store all inter-cell communication data, including user names\nand passwords, in the database. Because the cells data is not updated\nvery frequently, use this option to specify a JSON file to store\ncells data. With this configuration, the database is no longer\nconsulted when reloading the cells data. The file must have columns\npresent in the Cell model (excluding common database fields and the\nid column). You must specify the queue connection information through\na transport_url field, instead of username, password, and so on.\n\nThe transport_url has the following form:\nrabbit://USERNAME:PASSWORD@HOSTNAME:PORT/VIRTUAL_HOST\n\nPossible values:\n\nThe scheme can be either qpid or rabbit, the following sample shows\nthis optional configuration:\n\n    {\n        "parent": {\n            "name": "parent",\n            "api_url": "http://api.example.com:8774",\n            "transport_url": "rabbit://rabbit.example.com",\n            "weight_offset": 0.0,\n            "weight_scale": 1.0,\n            "is_parent": true\n        },\n        "cell1": {\n            "name": "cell1",\n            "api_url": "http://api.example.com:8774",\n            "transport_url": "rabbit://rabbit1.example.com",\n            "weight_offset": 0.0,\n            "weight_scale": 1.0,\n            "is_parent": false\n        },\n        "cell2": {\n            "name": "cell2",\n            "api_url": "http://api.example.com:8774",\n            "transport_url": "rabbit://rabbit2.example.com",\n            "weight_offset": 0.0,\n            "weight_scale": 1.0,\n            "is_parent": false\n        }\n    }\n\nServices which consume this:\n\n* nova-cells\n\nRelated options:\n\n* None\n"""'
op|')'
nl|'\n'
op|']'
newline|'\n'
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
string|"'cells'"
op|':'
name|'ALL_CELLS_OPTS'
op|'}'
newline|'\n'
dedent|''
endmarker|''
end_unit
