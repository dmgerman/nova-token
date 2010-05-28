begin_unit
comment|'# -*- test-case-name: twisted.test.test_htb -*-'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright (c) 2001-2004 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
nl|'\n'
string|'"""Hierarchical Token Bucket traffic shaping.\n\nPatterned after U{Martin Devera\'s Hierarchical Token Bucket traffic\nshaper for the Linux kernel<http://luxik.cdi.cz/~devik/qos/htb/>}.\n\n@seealso: U{HTB Linux queuing discipline manual - user guide\n  <http://luxik.cdi.cz/~devik/qos/htb/manual/userg.htm>}\n@seealso: U{Token Bucket Filter in Linux Advanced Routing & Traffic Control\n    HOWTO<http://lartc.org/howto/lartc.qdisc.classless.html#AEN682>}\n@author: Kevin Turner\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'__future__'
name|'import'
name|'nested_scopes'
newline|'\n'
nl|'\n'
DECL|variable|__version__
name|'__version__'
op|'='
string|"'$Revision: 1.5 $'"
op|'['
number|'11'
op|':'
op|'-'
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# TODO: Investigate whether we should be using os.times()[-1] instead of'
nl|'\n'
comment|'# time.time.  time.time, it has been pointed out, can go backwards.  Is'
nl|'\n'
comment|'# the same true of os.times?'
nl|'\n'
name|'from'
name|'time'
name|'import'
name|'time'
newline|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'implements'
op|','
name|'Interface'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'pcp'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Bucket
name|'class'
name|'Bucket'
op|':'
newline|'\n'
indent|'    '
string|'"""Token bucket, or something like it.\n\n    I can hold up to a certain number of tokens, and I drain over time.\n\n    @cvar maxburst: Size of the bucket, in bytes.  If None, the bucket is\n        never full.\n    @type maxburst: int\n    @cvar rate: Rate the bucket drains, in bytes per second.  If None,\n        the bucket drains instantaneously.\n    @type rate: int\n    """'
newline|'\n'
nl|'\n'
DECL|variable|maxburst
name|'maxburst'
op|'='
name|'None'
newline|'\n'
DECL|variable|rate
name|'rate'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|variable|_refcount
name|'_refcount'
op|'='
number|'0'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'parentBucket'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'content'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'parentBucket'
op|'='
name|'parentBucket'
newline|'\n'
name|'self'
op|'.'
name|'lastDrip'
op|'='
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|add
dedent|''
name|'def'
name|'add'
op|'('
name|'self'
op|','
name|'amount'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add tokens to me.\n\n        @param amount: A quanity of tokens to add.\n        @type amount: int\n\n        @returns: The number of tokens that fit.\n        @returntype: int\n        """'
newline|'\n'
name|'self'
op|'.'
name|'drip'
op|'('
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'maxburst'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'allowable'
op|'='
name|'amount'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'allowable'
op|'='
name|'min'
op|'('
name|'amount'
op|','
name|'self'
op|'.'
name|'maxburst'
op|'-'
name|'self'
op|'.'
name|'content'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'parentBucket'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'allowable'
op|'='
name|'self'
op|'.'
name|'parentBucket'
op|'.'
name|'add'
op|'('
name|'allowable'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'content'
op|'+='
name|'allowable'
newline|'\n'
name|'return'
name|'allowable'
newline|'\n'
nl|'\n'
DECL|member|drip
dedent|''
name|'def'
name|'drip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Let some of the bucket drain.\n\n        How much of the bucket drains depends on how long it has been\n        since I was last called.\n\n        @returns: True if I am now empty.\n        @returntype: bool\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'parentBucket'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'parentBucket'
op|'.'
name|'drip'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'rate'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'content'
op|'='
number|'0'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'now'
op|'='
name|'time'
op|'('
op|')'
newline|'\n'
name|'deltaT'
op|'='
name|'now'
op|'-'
name|'self'
op|'.'
name|'lastDrip'
newline|'\n'
name|'self'
op|'.'
name|'content'
op|'='
name|'long'
op|'('
name|'max'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'content'
op|'-'
name|'deltaT'
op|'*'
name|'self'
op|'.'
name|'rate'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lastDrip'
op|'='
name|'now'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IBucketFilter
dedent|''
dedent|''
dedent|''
name|'class'
name|'IBucketFilter'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
DECL|member|getBucketFor
indent|'    '
name|'def'
name|'getBucketFor'
op|'('
op|'*'
name|'somethings'
op|','
op|'**'
name|'some_kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""I\'ll give you a bucket for something.\n\n        @returntype: L{Bucket}\n        """'
newline|'\n'
nl|'\n'
DECL|class|HierarchicalBucketFilter
dedent|''
dedent|''
name|'class'
name|'HierarchicalBucketFilter'
op|':'
newline|'\n'
indent|'    '
string|'"""I filter things into buckets, and I am nestable.\n\n    @cvar bucketFactory: Class of buckets to make.\n    @type bucketFactory: L{Bucket} class\n    @cvar sweepInterval: Seconds between sweeping out the bucket cache.\n    @type sweepInterval: int\n    """'
newline|'\n'
nl|'\n'
name|'implements'
op|'('
name|'IBucketFilter'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|bucketFactory
name|'bucketFactory'
op|'='
name|'Bucket'
newline|'\n'
DECL|variable|sweepInterval
name|'sweepInterval'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'parentFilter'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'buckets'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'parentFilter'
op|'='
name|'parentFilter'
newline|'\n'
name|'self'
op|'.'
name|'lastSweep'
op|'='
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|getBucketFor
dedent|''
name|'def'
name|'getBucketFor'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""You want a bucket for that?  I\'ll give you a bucket.\n\n        Any parameters are passed on to L{getBucketKey}, from them it\n        decides which bucket you get.\n\n        @returntype: L{Bucket}\n        """'
newline|'\n'
name|'if'
op|'('
op|'('
name|'self'
op|'.'
name|'sweepInterval'
name|'is'
name|'not'
name|'None'
op|')'
nl|'\n'
name|'and'
op|'('
op|'('
name|'time'
op|'('
op|')'
op|'-'
name|'self'
op|'.'
name|'lastSweep'
op|')'
op|'>'
name|'self'
op|'.'
name|'sweepInterval'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'sweep'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'parentFilter'
op|':'
newline|'\n'
indent|'            '
name|'parentBucket'
op|'='
name|'self'
op|'.'
name|'parentFilter'
op|'.'
name|'getBucketFor'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'parentBucket'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'key'
op|'='
name|'self'
op|'.'
name|'getBucketKey'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'bucket'
op|'='
name|'self'
op|'.'
name|'buckets'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'bucket'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'bucket'
op|'='
name|'self'
op|'.'
name|'bucketFactory'
op|'('
name|'parentBucket'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'buckets'
op|'['
name|'key'
op|']'
op|'='
name|'bucket'
newline|'\n'
dedent|''
name|'return'
name|'bucket'
newline|'\n'
nl|'\n'
DECL|member|getBucketKey
dedent|''
name|'def'
name|'getBucketKey'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""I determine who gets which bucket.\n\n        Unless I\'m overridden, everything gets the same bucket.\n\n        @returns: something to be used as a key in the bucket cache.\n        """'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|sweep
dedent|''
name|'def'
name|'sweep'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""I throw away references to empty buckets."""'
newline|'\n'
name|'for'
name|'key'
op|','
name|'bucket'
name|'in'
name|'self'
op|'.'
name|'buckets'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
name|'bucket'
op|'.'
name|'_refcount'
op|'=='
number|'0'
op|')'
name|'and'
name|'bucket'
op|'.'
name|'drip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'del'
name|'self'
op|'.'
name|'buckets'
op|'['
name|'key'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'lastSweep'
op|'='
name|'time'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FilterByHost
dedent|''
dedent|''
name|'class'
name|'FilterByHost'
op|'('
name|'HierarchicalBucketFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A bucket filter with a bucket for each host.\n    """'
newline|'\n'
DECL|variable|sweepInterval
name|'sweepInterval'
op|'='
number|'60'
op|'*'
number|'20'
newline|'\n'
nl|'\n'
DECL|member|getBucketKey
name|'def'
name|'getBucketKey'
op|'('
name|'self'
op|','
name|'transport'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'transport'
op|'.'
name|'getPeer'
op|'('
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FilterByServer
dedent|''
dedent|''
name|'class'
name|'FilterByServer'
op|'('
name|'HierarchicalBucketFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A bucket filter with a bucket for each service.\n    """'
newline|'\n'
DECL|variable|sweepInterval
name|'sweepInterval'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|getBucketKey
name|'def'
name|'getBucketKey'
op|'('
name|'self'
op|','
name|'transport'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'transport'
op|'.'
name|'getHost'
op|'('
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShapedConsumer
dedent|''
dedent|''
name|'class'
name|'ShapedConsumer'
op|'('
name|'pcp'
op|'.'
name|'ProducerConsumerProxy'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""I wrap a Consumer and shape the rate at which it receives data.\n    """'
newline|'\n'
comment|"# Providing a Pull interface means I don't have to try to schedule"
nl|'\n'
comment|'# traffic with callLaters.'
nl|'\n'
DECL|variable|iAmStreaming
name|'iAmStreaming'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'consumer'
op|','
name|'bucket'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pcp'
op|'.'
name|'ProducerConsumerProxy'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'consumer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'='
name|'bucket'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'_refcount'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
DECL|member|_writeSomeData
dedent|''
name|'def'
name|'_writeSomeData'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
comment|'# In practice, this actually results in obscene amounts of'
nl|'\n'
comment|'# overhead, as a result of generating lots and lots of packets'
nl|'\n'
comment|'# with twelve-byte payloads.  We may need to do a version of'
nl|'\n'
comment|'# this with scheduled writes after all.'
nl|'\n'
indent|'        '
name|'amount'
op|'='
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'add'
op|'('
name|'len'
op|'('
name|'data'
op|')'
op|')'
newline|'\n'
name|'return'
name|'pcp'
op|'.'
name|'ProducerConsumerProxy'
op|'.'
name|'_writeSomeData'
op|'('
name|'self'
op|','
name|'data'
op|'['
op|':'
name|'amount'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stopProducing
dedent|''
name|'def'
name|'stopProducing'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pcp'
op|'.'
name|'ProducerConsumerProxy'
op|'.'
name|'stopProducing'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'bucket'
op|'.'
name|'_refcount'
op|'-='
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShapedTransport
dedent|''
dedent|''
name|'class'
name|'ShapedTransport'
op|'('
name|'ShapedConsumer'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""I wrap a Transport and shape the rate at which it receives data.\n\n    I am a L{ShapedConsumer} with a little bit of magic to provide for\n    the case where the consumer I wrap is also a Transport and people\n    will be attempting to access attributes I do not proxy as a\n    Consumer (e.g. loseConnection).\n    """'
newline|'\n'
comment|'# Ugh.  We only wanted to filter IConsumer, not ITransport.'
nl|'\n'
nl|'\n'
DECL|variable|iAmStreaming
name|'iAmStreaming'
op|'='
name|'False'
newline|'\n'
DECL|member|__getattr__
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
comment|'# Because people will be doing things like .getPeer and'
nl|'\n'
comment|'# .loseConnection on me.'
nl|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'consumer'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ShapedProtocolFactory
dedent|''
dedent|''
name|'class'
name|'ShapedProtocolFactory'
op|':'
newline|'\n'
indent|'    '
string|'"""I dispense Protocols with traffic shaping on their transports.\n\n    Usage::\n\n        myserver = SomeFactory()\n        myserver.protocol = ShapedProtocolFactory(myserver.protocol,\n                                                  bucketFilter)\n\n    Where SomeServerFactory is a L{twisted.internet.protocol.Factory}, and\n    bucketFilter is an instance of L{HierarchicalBucketFilter}.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'protoClass'
op|','
name|'bucketFilter'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tell me what to wrap and where to get buckets.\n\n        @param protoClass: The class of Protocol I will generate\n          wrapped instances of.\n        @type protoClass: L{Protocol<twisted.internet.interfaces.IProtocol>}\n          class\n        @param bucketFilter: The filter which will determine how\n          traffic is shaped.\n        @type bucketFilter: L{HierarchicalBucketFilter}.\n        """'
newline|'\n'
comment|'# More precisely, protoClass can be any callable that will return'
nl|'\n'
comment|'# instances of something that implements IProtocol.'
nl|'\n'
name|'self'
op|'.'
name|'protocol'
op|'='
name|'protoClass'
newline|'\n'
name|'self'
op|'.'
name|'bucketFilter'
op|'='
name|'bucketFilter'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make a Protocol instance with a shaped transport.\n\n        Any parameters will be passed on to the protocol\'s initializer.\n\n        @returns: a Protocol instance with a L{ShapedTransport}.\n        """'
newline|'\n'
name|'proto'
op|'='
name|'self'
op|'.'
name|'protocol'
op|'('
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'origMakeConnection'
op|'='
name|'proto'
op|'.'
name|'makeConnection'
newline|'\n'
DECL|function|makeConnection
name|'def'
name|'makeConnection'
op|'('
name|'transport'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bucket'
op|'='
name|'self'
op|'.'
name|'bucketFilter'
op|'.'
name|'getBucketFor'
op|'('
name|'transport'
op|')'
newline|'\n'
name|'shapedTransport'
op|'='
name|'ShapedTransport'
op|'('
name|'transport'
op|','
name|'bucket'
op|')'
newline|'\n'
name|'return'
name|'origMakeConnection'
op|'('
name|'shapedTransport'
op|')'
newline|'\n'
dedent|''
name|'proto'
op|'.'
name|'makeConnection'
op|'='
name|'makeConnection'
newline|'\n'
name|'return'
name|'proto'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
