begin_unit
comment|'# Copyright (c) 2006,2007 Mitch Garnaat http://garnaat.org/'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Permission is hereby granted, free of charge, to any person obtaining a'
nl|'\n'
comment|'# copy of this software and associated documentation files (the'
nl|'\n'
comment|'# "Software"), to deal in the Software without restriction, including'
nl|'\n'
comment|'# without limitation the rights to use, copy, modify, merge, publish, dis-'
nl|'\n'
comment|'# tribute, sublicense, and/or sell copies of the Software, and to permit'
nl|'\n'
comment|'# persons to whom the Software is furnished to do so, subject to the fol-'
nl|'\n'
comment|'# lowing conditions:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# The above copyright notice and this permission notice shall be included'
nl|'\n'
comment|'# in all copies or substantial portions of the Software.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS'
nl|'\n'
comment|'# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-'
nl|'\n'
comment|'# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT'
nl|'\n'
comment|'# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, '
nl|'\n'
comment|'# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,'
nl|'\n'
comment|'# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS'
nl|'\n'
comment|'# IN THE SOFTWARE.'
nl|'\n'
nl|'\n'
string|'"""\nRepresents an EC2 Elastic Block Storage Volume\n"""'
newline|'\n'
name|'from'
name|'boto'
op|'.'
name|'ec2'
op|'.'
name|'ec2object'
name|'import'
name|'EC2Object'
newline|'\n'
nl|'\n'
DECL|class|Volume
name|'class'
name|'Volume'
op|'('
name|'EC2Object'
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
name|'connection'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'EC2Object'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'create_time'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'status'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'size'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'snapshot_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'attach_data'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'zone'
op|'='
name|'None'
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
string|"'Volume:%s'"
op|'%'
name|'self'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'attachmentSet'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_data'
op|'='
name|'AttachmentSet'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'attach_data'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'volumeId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'createTime'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'create_time'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'status'"
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'value'
op|'!='
string|"''"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'status'
op|'='
name|'value'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'size'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'size'
op|'='
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'snapshotId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'snapshot_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'availabilityZone'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'zone'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_update
dedent|''
dedent|''
name|'def'
name|'_update'
op|'('
name|'self'
op|','
name|'updated'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__dict__'
op|'.'
name|'update'
op|'('
name|'updated'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rs'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_all_volumes'
op|'('
op|'['
name|'self'
op|'.'
name|'id'
op|']'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'rs'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_update'
op|'('
name|'rs'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Delete this EBS volume.\n\n        :rtype: bool\n        :return: True if successful\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach
dedent|''
name|'def'
name|'attach'
op|'('
name|'self'
op|','
name|'instance_id'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Attach this EBS volume to an EC2 instance.\n\n        :type instance_id: str\n        :param instance_id: The ID of the EC2 instance to which it will\n                            be attached.\n\n        :type device: str\n        :param device: The device on the instance through which the\n                       volume will be exposted (e.g. /dev/sdh)\n\n        :rtype: bool\n        :return: True if successful\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'attach_volume'
op|'('
name|'self'
op|'.'
name|'id'
op|','
name|'instance_id'
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach
dedent|''
name|'def'
name|'detach'
op|'('
name|'self'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Detach this EBS volume from an EC2 instance.\n\n        :type force: bool\n        :param force: Forces detachment if the previous detachment attempt did\n                      not occur cleanly.  This option can lead to data loss or\n                      a corrupted file system. Use this option only as a last\n                      resort to detach a volume from a failed instance. The\n                      instance will not have an opportunity to flush file system\n                      caches nor file system meta data. If you use this option,\n                      you must perform file system check and repair procedures.\n\n        :rtype: bool\n        :return: True if successful\n        """'
newline|'\n'
name|'instance_id'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'attach_data'
op|':'
newline|'\n'
indent|'            '
name|'instance_id'
op|'='
name|'self'
op|'.'
name|'attach_data'
op|'.'
name|'instance_id'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'attach_data'
op|':'
newline|'\n'
indent|'            '
name|'device'
op|'='
name|'self'
op|'.'
name|'attach_data'
op|'.'
name|'device'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'detach_volume'
op|'('
name|'self'
op|'.'
name|'id'
op|','
name|'instance_id'
op|','
name|'device'
op|','
name|'force'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'description'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Create a snapshot of this EBS Volume.\n\n        :type description: str\n        :param description: A description of the snapshot.  Limited to 256 characters.\n        \n        :rtype: bool\n        :return: True if successful\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'create_snapshot'
op|'('
name|'self'
op|'.'
name|'id'
op|','
name|'description'
op|')'
newline|'\n'
nl|'\n'
DECL|member|volume_state
dedent|''
name|'def'
name|'volume_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Returns the state of the volume.  Same value as the status attribute.\n        """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|attachment_state
dedent|''
name|'def'
name|'attachment_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get the attachment state.\n        """'
newline|'\n'
name|'state'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'attach_data'
op|':'
newline|'\n'
indent|'            '
name|'state'
op|'='
name|'self'
op|'.'
name|'attach_data'
op|'.'
name|'status'
newline|'\n'
dedent|''
name|'return'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|snapshots
dedent|''
name|'def'
name|'snapshots'
op|'('
name|'self'
op|','
name|'owner'
op|'='
name|'None'
op|','
name|'restorable_by'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get all snapshots related to this volume.  Note that this requires\n        that all available snapshots for the account be retrieved from EC2\n        first and then the list is filtered client-side to contain only\n        those for this volume.\n\n        :type owner: str\n        :param owner: If present, only the snapshots owned by the specified user\n                      will be returned.  Valid values are:\n                      self | amazon | AWS Account ID\n\n        :type restorable_by: str\n        :param restorable_by: If present, only the snapshots that are restorable\n                              by the specified account id will be returned.\n\n        :rtype: list of L{boto.ec2.snapshot.Snapshot}\n        :return: The requested Snapshot objects\n        \n        """'
newline|'\n'
name|'rs'
op|'='
name|'self'
op|'.'
name|'connection'
op|'.'
name|'get_all_snapshots'
op|'('
name|'owner'
op|'='
name|'owner'
op|','
nl|'\n'
name|'restorable_by'
op|'='
name|'restorable_by'
op|')'
newline|'\n'
name|'mine'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'snap'
name|'in'
name|'rs'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'snap'
op|'.'
name|'volume_id'
op|'=='
name|'self'
op|'.'
name|'id'
op|':'
newline|'\n'
indent|'                '
name|'mine'
op|'.'
name|'append'
op|'('
name|'snap'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'mine'
newline|'\n'
nl|'\n'
DECL|class|AttachmentSet
dedent|''
dedent|''
name|'class'
name|'AttachmentSet'
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
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'status'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'attach_time'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'None'
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
string|"'AttachmentSet:%s'"
op|'%'
name|'self'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
DECL|member|startElement
dedent|''
name|'def'
name|'startElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'attrs'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|endElement
dedent|''
name|'def'
name|'endElement'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'name'
op|'=='
string|"'volumeId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'instanceId'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'instance_id'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'status'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'status'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'attachTime'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'attach_time'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
string|"'device'"
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'device'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
