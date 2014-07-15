begin_unit
comment|'# Copyright 2014 Red Hat, Inc'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'collections'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
DECL|variable|virt_cpu_opts
name|'virt_cpu_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vcpu_pin_set'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Defines which pcpus that instance vcpus can use. '"
nl|'\n'
string|'\'For example, "4-12,^8,15"\''
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
name|'virt_cpu_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_vcpu_pin_set
name|'def'
name|'get_vcpu_pin_set'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parsing vcpu_pin_set config.\n\n    Returns a list of pcpu ids can be used by instances.\n    """'
newline|'\n'
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'vcpu_pin_set'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'cpuset_ids'
op|'='
name|'parse_cpu_spec'
op|'('
name|'CONF'
op|'.'
name|'vcpu_pin_set'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cpuset_ids'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"No CPUs available after parsing %r"'
op|')'
op|'%'
nl|'\n'
name|'CONF'
op|'.'
name|'vcpu_pin_set'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'sorted'
op|'('
name|'cpuset_ids'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_cpu_spec
dedent|''
name|'def'
name|'parse_cpu_spec'
op|'('
name|'spec'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse a CPU set specification.\n\n    :param spec: cpu set string eg "1-4,^3,6"\n\n    Each element in the list is either a single\n    CPU number, a range of CPU numbers, or a\n    caret followed by a CPU number to be excluded\n    from a previous range.\n\n    :returns: a set of CPU indexes\n    """'
newline|'\n'
nl|'\n'
name|'cpuset_ids'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'cpuset_reject_ids'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'for'
name|'rule'
name|'in'
name|'spec'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rule'
op|'='
name|'rule'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
comment|"# Handle multi ','"
nl|'\n'
name|'if'
name|'len'
op|'('
name|'rule'
op|')'
op|'<'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
comment|'# Note the count limit in the .split() call'
nl|'\n'
dedent|''
name|'range_parts'
op|'='
name|'rule'
op|'.'
name|'split'
op|'('
string|"'-'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'range_parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
comment|'# So, this was a range; start by converting the parts to ints'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'start'
op|','
name|'end'
op|'='
op|'['
name|'int'
op|'('
name|'p'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
name|'for'
name|'p'
name|'in'
name|'range_parts'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"Invalid range expression %r"'
op|')'
nl|'\n'
op|'%'
name|'rule'
op|')'
newline|'\n'
comment|"# Make sure it's a valid range"
nl|'\n'
dedent|''
name|'if'
name|'start'
op|'>'
name|'end'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"Invalid range expression %r"'
op|')'
nl|'\n'
op|'%'
name|'rule'
op|')'
newline|'\n'
comment|'# Add available CPU ids to set'
nl|'\n'
dedent|''
name|'cpuset_ids'
op|'|='
name|'set'
op|'('
name|'range'
op|'('
name|'start'
op|','
name|'end'
op|'+'
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'rule'
op|'['
number|'0'
op|']'
op|'=='
string|"'^'"
op|':'
newline|'\n'
comment|'# Not a range, the rule is an exclusion rule; convert to int'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cpuset_reject_ids'
op|'.'
name|'add'
op|'('
name|'int'
op|'('
name|'rule'
op|'['
number|'1'
op|':'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"Invalid exclusion "'
nl|'\n'
string|'"expression %r"'
op|')'
op|'%'
name|'rule'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# OK, a single CPU to include; convert to int'
nl|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'cpuset_ids'
op|'.'
name|'add'
op|'('
name|'int'
op|'('
name|'rule'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'_'
op|'('
string|'"Invalid inclusion "'
nl|'\n'
string|'"expression %r"'
op|')'
op|'%'
name|'rule'
op|')'
newline|'\n'
nl|'\n'
comment|'# Use sets to handle the exclusion rules for us'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'cpuset_ids'
op|'-='
name|'cpuset_reject_ids'
newline|'\n'
nl|'\n'
name|'return'
name|'cpuset_ids'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|format_cpu_spec
dedent|''
name|'def'
name|'format_cpu_spec'
op|'('
name|'cpuset'
op|','
name|'allow_ranges'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Format a libvirt CPU range specification.\n\n    :param cpuset: set (or list) of CPU indexes\n\n    Format a set/list of CPU indexes as a libvirt CPU\n    range specification. It allow_ranges is true, it\n    will try to detect continuous ranges of CPUs,\n    otherwise it will just list each CPU index explicitly.\n\n    :returns: a formatted CPU range string\n    """'
newline|'\n'
nl|'\n'
comment|"# We attempt to detect ranges, but don't bother with"
nl|'\n'
comment|'# trying to do range negations to minimize the overall'
nl|'\n'
comment|'# spec string length'
nl|'\n'
name|'if'
name|'allow_ranges'
op|':'
newline|'\n'
indent|'        '
name|'ranges'
op|'='
op|'['
op|']'
newline|'\n'
name|'previndex'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'cpuindex'
name|'in'
name|'sorted'
op|'('
name|'cpuset'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'previndex'
name|'is'
name|'None'
name|'or'
name|'previndex'
op|'!='
op|'('
name|'cpuindex'
op|'-'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ranges'
op|'.'
name|'append'
op|'('
op|'['
op|']'
op|')'
newline|'\n'
dedent|''
name|'ranges'
op|'['
op|'-'
number|'1'
op|']'
op|'.'
name|'append'
op|'('
name|'cpuindex'
op|')'
newline|'\n'
name|'previndex'
op|'='
name|'cpuindex'
newline|'\n'
nl|'\n'
dedent|''
name|'parts'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'ranges'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'entry'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'parts'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'entry'
op|'['
number|'0'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'parts'
op|'.'
name|'append'
op|'('
string|'"%d-%d"'
op|'%'
op|'('
name|'entry'
op|'['
number|'0'
op|']'
op|','
name|'entry'
op|'['
name|'len'
op|'('
name|'entry'
op|')'
op|'-'
number|'1'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|'","'
op|'.'
name|'join'
op|'('
name|'parts'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'","'
op|'.'
name|'join'
op|'('
name|'str'
op|'('
name|'id'
op|')'
name|'for'
name|'id'
name|'in'
name|'sorted'
op|'('
name|'cpuset'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VirtCPUTopology
dedent|''
dedent|''
name|'class'
name|'VirtCPUTopology'
op|'('
name|'object'
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
name|'sockets'
op|','
name|'cores'
op|','
name|'threads'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new CPU topology object\n\n        :param sockets: number of sockets, at least 1\n        :param cores: number of cores, at least 1\n        :param threads: number of threads, at least 1\n\n        Create a new CPU topology object representing the\n        number of sockets, cores and threads to use for\n        the virtual instance.\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'sockets'
op|'='
name|'sockets'
newline|'\n'
name|'self'
op|'.'
name|'cores'
op|'='
name|'cores'
newline|'\n'
name|'self'
op|'.'
name|'threads'
op|'='
name|'threads'
newline|'\n'
nl|'\n'
DECL|member|score
dedent|''
name|'def'
name|'score'
op|'('
name|'self'
op|','
name|'wanttopology'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Calculate score for the topology against a desired configuration\n\n        :param wanttopology: VirtCPUTopology instance for preferred topology\n\n        Calculate a score indicating how well this topology\n        matches against a preferred topology. A score of 3\n        indicates an exact match for sockets, cores and threads.\n        A score of 2 indicates a match of sockets & cores or\n        sockets & threads or cores and threads. A score of 1\n        indicates a match of sockets or cores or threads. A\n        score of 0 indicates no match\n\n        :returns: score in range 0 (worst) to 3 (best)\n        """'
newline|'\n'
nl|'\n'
name|'score'
op|'='
number|'0'
newline|'\n'
name|'if'
op|'('
name|'wanttopology'
op|'.'
name|'sockets'
op|'!='
op|'-'
number|'1'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'sockets'
op|'=='
name|'wanttopology'
op|'.'
name|'sockets'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'score'
op|'='
name|'score'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'wanttopology'
op|'.'
name|'cores'
op|'!='
op|'-'
number|'1'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'cores'
op|'=='
name|'wanttopology'
op|'.'
name|'cores'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'score'
op|'='
name|'score'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'wanttopology'
op|'.'
name|'threads'
op|'!='
op|'-'
number|'1'
name|'and'
nl|'\n'
name|'self'
op|'.'
name|'threads'
op|'=='
name|'wanttopology'
op|'.'
name|'threads'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'score'
op|'='
name|'score'
op|'+'
number|'1'
newline|'\n'
dedent|''
name|'return'
name|'score'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_topology_constraints
name|'def'
name|'get_topology_constraints'
op|'('
name|'flavor'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the topology constraints declared in flavor or image\n\n        :param flavor: Flavor object to read extra specs from\n        :param image_meta: Image object to read image metadata from\n\n        Gets the topology constraints from the configuration defined\n        in the flavor extra specs or the image metadata. In the flavor\n        this will look for\n\n         hw:cpu_sockets - preferred socket count\n         hw:cpu_cores - preferred core count\n         hw:cpu_threads - preferred thread count\n         hw:cpu_maxsockets - maximum socket count\n         hw:cpu_maxcores - maximum core count\n         hw:cpu_maxthreads - maximum thread count\n\n        In the image metadata this will look at\n\n         hw_cpu_sockets - preferred socket count\n         hw_cpu_cores - preferred core count\n         hw_cpu_threads - preferred thread count\n         hw_cpu_maxsockets - maximum socket count\n         hw_cpu_maxcores - maximum core count\n         hw_cpu_maxthreads - maximum thread count\n\n        The image metadata must be strictly lower than any values\n        set in the flavor. All values are, however, optional.\n\n        This will return a pair of VirtCPUTopology instances,\n        the first giving the preferred socket/core/thread counts,\n        and the second giving the upper limits on socket/core/\n        thread counts.\n\n        exception.ImageVCPULimitsRangeExceeded will be raised\n        if the maximum counts set against the image exceed\n        the maximum counts set against the flavor\n\n        exception.ImageVCPUTopologyRangeExceeded will be raised\n        if the preferred counts set against the image exceed\n        the maximum counts set against the image or flavor\n\n        :returns: (preferred topology, maximum topology)\n        """'
newline|'\n'
nl|'\n'
comment|'# Obtain the absolute limits from the flavor'
nl|'\n'
name|'flvmaxsockets'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
nl|'\n'
string|'"hw:cpu_max_sockets"'
op|','
number|'65536'
op|')'
op|')'
newline|'\n'
name|'flvmaxcores'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
nl|'\n'
string|'"hw:cpu_max_cores"'
op|','
number|'65536'
op|')'
op|')'
newline|'\n'
name|'flvmaxthreads'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
nl|'\n'
string|'"hw:cpu_max_threads"'
op|','
number|'65536'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Flavor limits %(sockets)d:%(cores)d:%(threads)d"'
op|','
nl|'\n'
op|'{'
string|'"sockets"'
op|':'
name|'flvmaxsockets'
op|','
nl|'\n'
string|'"cores"'
op|':'
name|'flvmaxcores'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'flvmaxthreads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get any customized limits from the image'
nl|'\n'
name|'maxsockets'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_max_sockets"'
op|','
name|'flvmaxsockets'
op|')'
op|')'
newline|'\n'
name|'maxcores'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_max_cores"'
op|','
name|'flvmaxcores'
op|')'
op|')'
newline|'\n'
name|'maxthreads'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_max_threads"'
op|','
name|'flvmaxthreads'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Image limits %(sockets)d:%(cores)d:%(threads)d"'
op|','
nl|'\n'
op|'{'
string|'"sockets"'
op|':'
name|'maxsockets'
op|','
nl|'\n'
string|'"cores"'
op|':'
name|'maxcores'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'maxthreads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Image limits are not permitted to exceed the flavor'
nl|'\n'
comment|'# limits. ie they can only lower what the flavor defines'
nl|'\n'
name|'if'
op|'('
op|'('
name|'maxsockets'
op|'>'
name|'flvmaxsockets'
op|')'
name|'or'
nl|'\n'
op|'('
name|'maxcores'
op|'>'
name|'flvmaxcores'
op|')'
name|'or'
nl|'\n'
op|'('
name|'maxthreads'
op|'>'
name|'flvmaxthreads'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageVCPULimitsRangeExceeded'
op|'('
nl|'\n'
name|'sockets'
op|'='
name|'maxsockets'
op|','
nl|'\n'
name|'cores'
op|'='
name|'maxcores'
op|','
nl|'\n'
name|'threads'
op|'='
name|'maxthreads'
op|','
nl|'\n'
name|'maxsockets'
op|'='
name|'flvmaxsockets'
op|','
nl|'\n'
name|'maxcores'
op|'='
name|'flvmaxcores'
op|','
nl|'\n'
name|'maxthreads'
op|'='
name|'flvmaxthreads'
op|')'
newline|'\n'
nl|'\n'
comment|'# Get any default preferred topology from the flavor'
nl|'\n'
dedent|''
name|'flvsockets'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
string|'"hw:cpu_sockets"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
name|'flvcores'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
string|'"hw:cpu_cores"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
name|'flvthreads'
op|'='
name|'int'
op|'('
name|'flavor'
op|'.'
name|'extra_specs'
op|'.'
name|'get'
op|'('
string|'"hw:cpu_threads"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Flavor pref %(sockets)d:%(cores)d:%(threads)d"'
op|','
nl|'\n'
op|'{'
string|'"sockets"'
op|':'
name|'flvsockets'
op|','
nl|'\n'
string|'"cores"'
op|':'
name|'flvcores'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'flvthreads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# If the image limits have reduced the flavor limits'
nl|'\n'
comment|'# we might need to discard the preferred topology'
nl|'\n'
comment|'# from the flavor'
nl|'\n'
name|'if'
op|'('
op|'('
name|'flvsockets'
op|'>'
name|'maxsockets'
op|')'
name|'or'
nl|'\n'
op|'('
name|'flvcores'
op|'>'
name|'maxcores'
op|')'
name|'or'
nl|'\n'
op|'('
name|'flvthreads'
op|'>'
name|'maxthreads'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'flvsockets'
op|'='
name|'flvcores'
op|'='
name|'flvthreads'
op|'='
op|'-'
number|'1'
newline|'\n'
nl|'\n'
comment|'# Finally see if the image has provided a preferred'
nl|'\n'
comment|'# topology to use'
nl|'\n'
dedent|''
name|'sockets'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_sockets"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
name|'cores'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_cores"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
name|'threads'
op|'='
name|'int'
op|'('
name|'image_meta'
op|'.'
name|'get'
op|'('
string|'"properties"'
op|','
op|'{'
op|'}'
op|')'
nl|'\n'
op|'.'
name|'get'
op|'('
string|'"hw_cpu_threads"'
op|','
op|'-'
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Image pref %(sockets)d:%(cores)d:%(threads)d"'
op|','
nl|'\n'
op|'{'
string|'"sockets"'
op|':'
name|'sockets'
op|','
nl|'\n'
string|'"cores"'
op|':'
name|'cores'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'threads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Image topology is not permitted to exceed image/flavor'
nl|'\n'
comment|'# limits'
nl|'\n'
name|'if'
op|'('
op|'('
name|'sockets'
op|'>'
name|'maxsockets'
op|')'
name|'or'
nl|'\n'
op|'('
name|'cores'
op|'>'
name|'maxcores'
op|')'
name|'or'
nl|'\n'
op|'('
name|'threads'
op|'>'
name|'maxthreads'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageVCPUTopologyRangeExceeded'
op|'('
nl|'\n'
name|'sockets'
op|'='
name|'sockets'
op|','
nl|'\n'
name|'cores'
op|'='
name|'cores'
op|','
nl|'\n'
name|'threads'
op|'='
name|'threads'
op|','
nl|'\n'
name|'maxsockets'
op|'='
name|'maxsockets'
op|','
nl|'\n'
name|'maxcores'
op|'='
name|'maxcores'
op|','
nl|'\n'
name|'maxthreads'
op|'='
name|'maxthreads'
op|')'
newline|'\n'
nl|'\n'
comment|'# If no preferred topology was set against the image'
nl|'\n'
comment|'# then use the preferred topology from the flavor'
nl|'\n'
comment|"# We use 'and' not 'or', since if any value is set"
nl|'\n'
comment|'# against the image this invalidates the entire set'
nl|'\n'
comment|'# of values from the flavor'
nl|'\n'
dedent|''
name|'if'
name|'sockets'
op|'=='
op|'-'
number|'1'
name|'and'
name|'cores'
op|'=='
op|'-'
number|'1'
name|'and'
name|'threads'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'sockets'
op|'='
name|'flvsockets'
newline|'\n'
name|'cores'
op|'='
name|'flvcores'
newline|'\n'
name|'threads'
op|'='
name|'flvthreads'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Chosen %(sockets)d:%(cores)d:%(threads)d limits "'
nl|'\n'
string|'"%(maxsockets)d:%(maxcores)d:%(maxthreads)d"'
op|','
nl|'\n'
op|'{'
string|'"sockets"'
op|':'
name|'sockets'
op|','
string|'"cores"'
op|':'
name|'cores'
op|','
nl|'\n'
string|'"threads"'
op|':'
name|'threads'
op|','
string|'"maxsockets"'
op|':'
name|'maxsockets'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
name|'maxcores'
op|','
string|'"maxthreads"'
op|':'
name|'maxthreads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'return'
op|'('
name|'VirtCPUTopology'
op|'('
name|'sockets'
op|','
name|'cores'
op|','
name|'threads'
op|')'
op|','
nl|'\n'
name|'VirtCPUTopology'
op|'('
name|'maxsockets'
op|','
name|'maxcores'
op|','
name|'maxthreads'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_possible_topologies
name|'def'
name|'get_possible_topologies'
op|'('
name|'vcpus'
op|','
name|'maxtopology'
op|','
name|'allow_threads'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get a list of possible topologies for a vCPU count\n        :param vcpus: total number of CPUs for guest instance\n        :param maxtopology: VirtCPUTopology for upper limits\n        :param allow_threads: if the hypervisor supports CPU threads\n\n        Given a total desired vCPU count and constraints on the\n        maximum number of sockets, cores and threads, return a\n        list of VirtCPUTopology instances that represent every\n        possible topology that satisfies the constraints.\n\n        exception.ImageVCPULimitsRangeImpossible is raised if\n        it is impossible to achieve the total vcpu count given\n        the maximum limits on sockets, cores & threads.\n\n        :returns: list of VirtCPUTopology instances\n        """'
newline|'\n'
nl|'\n'
comment|'# Clamp limits to number of vcpus to prevent'
nl|'\n'
comment|'# iterating over insanely large list'
nl|'\n'
name|'maxsockets'
op|'='
name|'min'
op|'('
name|'vcpus'
op|','
name|'maxtopology'
op|'.'
name|'sockets'
op|')'
newline|'\n'
name|'maxcores'
op|'='
name|'min'
op|'('
name|'vcpus'
op|','
name|'maxtopology'
op|'.'
name|'cores'
op|')'
newline|'\n'
name|'maxthreads'
op|'='
name|'min'
op|'('
name|'vcpus'
op|','
name|'maxtopology'
op|'.'
name|'threads'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'allow_threads'
op|':'
newline|'\n'
indent|'            '
name|'maxthreads'
op|'='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Build topologies for %(vcpus)d vcpu(s) "'
nl|'\n'
string|'"%(maxsockets)d:%(maxcores)d:%(maxthreads)d"'
op|','
nl|'\n'
op|'{'
string|'"vcpus"'
op|':'
name|'vcpus'
op|','
string|'"maxsockets"'
op|':'
name|'maxsockets'
op|','
nl|'\n'
string|'"maxcores"'
op|':'
name|'maxcores'
op|','
string|'"maxthreads"'
op|':'
name|'maxthreads'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# Figure out all possible topologies that match'
nl|'\n'
comment|'# the required vcpus count and satisfy the declared'
nl|'\n'
comment|'# limits. If the total vCPU count were very high'
nl|'\n'
comment|'# it might be more efficient to factorize the vcpu'
nl|'\n'
comment|'# count and then only iterate over its factors, but'
nl|'\n'
comment|"# that's overkill right now"
nl|'\n'
name|'possible'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'s'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'maxsockets'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'c'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'maxcores'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'t'
name|'in'
name|'range'
op|'('
number|'1'
op|','
name|'maxthreads'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'t'
op|'*'
name|'c'
op|'*'
name|'s'
op|'=='
name|'vcpus'
op|':'
newline|'\n'
indent|'                        '
name|'possible'
op|'.'
name|'append'
op|'('
name|'VirtCPUTopology'
op|'('
name|'s'
op|','
name|'c'
op|','
name|'t'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# We want to'
nl|'\n'
comment|'#  - Minimize threads (ie larger sockets * cores is best)'
nl|'\n'
comment|'#  - Prefer sockets over cores'
nl|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
name|'possible'
op|'='
name|'sorted'
op|'('
name|'possible'
op|','
name|'reverse'
op|'='
name|'True'
op|','
nl|'\n'
name|'key'
op|'='
name|'lambda'
name|'x'
op|':'
op|'('
name|'x'
op|'.'
name|'sockets'
op|'*'
name|'x'
op|'.'
name|'cores'
op|','
nl|'\n'
name|'x'
op|'.'
name|'sockets'
op|','
nl|'\n'
name|'x'
op|'.'
name|'threads'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Got %d possible topologies"'
op|','
name|'len'
op|'('
name|'possible'
op|')'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'possible'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'ImageVCPULimitsRangeImpossible'
op|'('
name|'vcpus'
op|'='
name|'vcpus'
op|','
nl|'\n'
name|'sockets'
op|'='
name|'maxsockets'
op|','
nl|'\n'
name|'cores'
op|'='
name|'maxcores'
op|','
nl|'\n'
name|'threads'
op|'='
name|'maxthreads'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'possible'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|sort_possible_topologies
name|'def'
name|'sort_possible_topologies'
op|'('
name|'possible'
op|','
name|'wanttopology'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sort the topologies in order of preference\n        :param possible: list of VirtCPUTopology instances\n        :param wanttopology: VirtCPUTopology for preferred topology\n\n        This takes the list of possible topologies and resorts\n        it such that those configurations which most closely\n        match the preferred topology are first.\n\n        :returns: sorted list of VirtCPUTopology instances\n        """'
newline|'\n'
nl|'\n'
comment|'# Look at possible topologies and score them according'
nl|'\n'
comment|'# to how well they match the preferred topologies'
nl|'\n'
comment|"# We don't use python's sort(), since we want to"
nl|'\n'
comment|'# preserve the sorting done when populating the'
nl|'\n'
comment|"# 'possible' list originally"
nl|'\n'
name|'scores'
op|'='
name|'collections'
op|'.'
name|'defaultdict'
op|'('
name|'list'
op|')'
newline|'\n'
name|'for'
name|'topology'
name|'in'
name|'possible'
op|':'
newline|'\n'
indent|'            '
name|'score'
op|'='
name|'topology'
op|'.'
name|'score'
op|'('
name|'wanttopology'
op|')'
newline|'\n'
name|'scores'
op|'['
name|'score'
op|']'
op|'.'
name|'append'
op|'('
name|'topology'
op|')'
newline|'\n'
nl|'\n'
comment|'# Build list of all possible topologies sorted'
nl|'\n'
comment|'# by the match score, best match first'
nl|'\n'
dedent|''
name|'desired'
op|'='
op|'['
op|']'
newline|'\n'
name|'desired'
op|'.'
name|'extend'
op|'('
name|'scores'
op|'['
number|'3'
op|']'
op|')'
newline|'\n'
name|'desired'
op|'.'
name|'extend'
op|'('
name|'scores'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
name|'desired'
op|'.'
name|'extend'
op|'('
name|'scores'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'desired'
op|'.'
name|'extend'
op|'('
name|'scores'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'desired'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_desirable_configs
name|'def'
name|'get_desirable_configs'
op|'('
name|'flavor'
op|','
name|'image_meta'
op|','
name|'allow_threads'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get desired CPU topologies according to settings\n\n        :param flavor: Flavor object to query extra specs from\n        :param image_meta: ImageMeta object to query properties from\n        :param allow_threads: if the hypervisor supports CPU threads\n\n        Look at the properties set in the flavor extra specs and\n        the image metadata and build up a list of all possible\n        valid CPU topologies that can be used in the guest. Then\n        return this list sorted in order of preference.\n\n        :returns: sorted list of VirtCPUTopology instances\n        """'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Getting desirable topologies for flavor %(flavor)s "'
nl|'\n'
string|'"and image_meta %(image_meta)s"'
op|','
nl|'\n'
op|'{'
string|'"flavor"'
op|':'
name|'flavor'
op|','
string|'"image_meta"'
op|':'
name|'image_meta'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'preferred'
op|','
name|'maximum'
op|'='
op|'('
nl|'\n'
name|'VirtCPUTopology'
op|'.'
name|'get_topology_constraints'
op|'('
name|'flavor'
op|','
nl|'\n'
name|'image_meta'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'possible'
op|'='
name|'VirtCPUTopology'
op|'.'
name|'get_possible_topologies'
op|'('
nl|'\n'
name|'flavor'
op|'.'
name|'vcpus'
op|','
name|'maximum'
op|','
name|'allow_threads'
op|')'
newline|'\n'
name|'desired'
op|'='
name|'VirtCPUTopology'
op|'.'
name|'sort_possible_topologies'
op|'('
nl|'\n'
name|'possible'
op|','
name|'preferred'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'desired'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_best_config
name|'def'
name|'get_best_config'
op|'('
name|'flavor'
op|','
name|'image_meta'
op|','
name|'allow_threads'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get bst CPU topology according to settings\n\n        :param flavor: Flavor object to query extra specs from\n        :param image_meta: ImageMeta object to query properties from\n        :param allow_threads: if the hypervisor supports CPU threads\n\n        Look at the properties set in the flavor extra specs and\n        the image metadata and build up a list of all possible\n        valid CPU topologies that can be used in the guest. Then\n        return the best topology to use\n\n        :returns: a VirtCPUTopology instance for best topology\n        """'
newline|'\n'
nl|'\n'
name|'return'
name|'VirtCPUTopology'
op|'.'
name|'get_desirable_configs'
op|'('
name|'flavor'
op|','
nl|'\n'
name|'image_meta'
op|','
nl|'\n'
name|'allow_threads'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
