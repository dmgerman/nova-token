begin_unit
comment|'# -*- Python -*-'
nl|'\n'
nl|'\n'
string|'"""Example of rate-limiting your web server.\n\nCaveat emptor: While the transfer rates imposed by this mechanism will\nlook accurate with wget\'s rate-meter, don\'t forget to examine your network\ninterface\'s traffic statistics as well.  The current implementation tends\nto create lots of small packets in some conditions, and each packet carries\nwith it some bytes of overhead.  Check to make sure this overhead is not\ncosting you more bandwidth than you are saving by limiting the rate!\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'htb'
newline|'\n'
comment|'# for picklability'
nl|'\n'
name|'import'
name|'shaper'
newline|'\n'
nl|'\n'
DECL|variable|serverFilter
name|'serverFilter'
op|'='
name|'htb'
op|'.'
name|'HierarchicalBucketFilter'
op|'('
op|')'
newline|'\n'
DECL|variable|serverBucket
name|'serverBucket'
op|'='
name|'htb'
op|'.'
name|'Bucket'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Cap total server traffic at 20 kB/s'
nl|'\n'
name|'serverBucket'
op|'.'
name|'maxburst'
op|'='
number|'20000'
newline|'\n'
name|'serverBucket'
op|'.'
name|'rate'
op|'='
number|'20000'
newline|'\n'
nl|'\n'
name|'serverFilter'
op|'.'
name|'buckets'
op|'['
name|'None'
op|']'
op|'='
name|'serverBucket'
newline|'\n'
nl|'\n'
comment|'# Web service is also limited per-host:'
nl|'\n'
DECL|class|WebClientBucket
name|'class'
name|'WebClientBucket'
op|'('
name|'htb'
op|'.'
name|'Bucket'
op|')'
op|':'
newline|'\n'
comment|'# Your first 10k is free'
nl|'\n'
DECL|variable|maxburst
indent|'    '
name|'maxburst'
op|'='
number|'10000'
newline|'\n'
comment|'# One kB/s thereafter.'
nl|'\n'
DECL|variable|rate
name|'rate'
op|'='
number|'1000'
newline|'\n'
nl|'\n'
DECL|variable|webFilter
dedent|''
name|'webFilter'
op|'='
name|'htb'
op|'.'
name|'FilterByHost'
op|'('
name|'serverFilter'
op|')'
newline|'\n'
name|'webFilter'
op|'.'
name|'bucketFactory'
op|'='
name|'shaper'
op|'.'
name|'WebClientBucket'
newline|'\n'
nl|'\n'
DECL|variable|servertype
name|'servertype'
op|'='
string|'"web"'
comment|'# "chargen"'
newline|'\n'
nl|'\n'
name|'if'
name|'servertype'
op|'=='
string|'"web"'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'web'
name|'import'
name|'server'
op|','
name|'static'
newline|'\n'
DECL|variable|site
name|'site'
op|'='
name|'server'
op|'.'
name|'Site'
op|'('
name|'static'
op|'.'
name|'File'
op|'('
string|'"/var/www"'
op|')'
op|')'
newline|'\n'
name|'site'
op|'.'
name|'protocol'
op|'='
name|'htb'
op|'.'
name|'ShapedProtocolFactory'
op|'('
name|'site'
op|'.'
name|'protocol'
op|','
name|'webFilter'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'servertype'
op|'=='
string|'"chargen"'
op|':'
newline|'\n'
indent|'    '
name|'from'
name|'twisted'
op|'.'
name|'protocols'
name|'import'
name|'wire'
newline|'\n'
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'protocol'
newline|'\n'
nl|'\n'
DECL|variable|site
name|'site'
op|'='
name|'protocol'
op|'.'
name|'ServerFactory'
op|'('
op|')'
newline|'\n'
name|'site'
op|'.'
name|'protocol'
op|'='
name|'htb'
op|'.'
name|'ShapedProtocolFactory'
op|'('
name|'wire'
op|'.'
name|'Chargen'
op|','
name|'webFilter'
op|')'
newline|'\n'
comment|'#site.protocol = wire.Chargen'
nl|'\n'
nl|'\n'
dedent|''
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'reactor'
newline|'\n'
name|'reactor'
op|'.'
name|'listenTCP'
op|'('
number|'8000'
op|','
name|'site'
op|')'
newline|'\n'
name|'reactor'
op|'.'
name|'run'
op|'('
op|')'
newline|'\n'
endmarker|''
end_unit
