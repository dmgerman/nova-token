begin_unit
comment|'# -*- Python -*-'
nl|'\n'
comment|'# Copyright (c) 2008 Twisted Matrix Laboratories.'
nl|'\n'
comment|'# See LICENSE for details.'
nl|'\n'
nl|'\n'
string|'"""\nPan-protocol chat client.\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'zope'
op|'.'
name|'interface'
name|'import'
name|'Interface'
op|','
name|'Attribute'
newline|'\n'
nl|'\n'
name|'from'
name|'twisted'
op|'.'
name|'words'
op|'.'
name|'im'
name|'import'
name|'locals'
newline|'\n'
nl|'\n'
comment|'# (Random musings, may not reflect on current state of code:)'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Accounts have Protocol components (clients)'
nl|'\n'
comment|'# Persons have Conversation components'
nl|'\n'
comment|'# Groups have GroupConversation components'
nl|'\n'
comment|'# Persons and Groups are associated with specific Accounts'
nl|'\n'
comment|'# At run-time, Clients/Accounts are slaved to a User Interface'
nl|'\n'
comment|"#   (Note: User may be a bot, so don't assume all UIs are built on gui toolkits)"
nl|'\n'
nl|'\n'
nl|'\n'
DECL|class|IAccount
name|'class'
name|'IAccount'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    I represent a user\'s account with a chat service.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|client
name|'client'
op|'='
name|'Attribute'
op|'('
string|"'The L{IClient} currently connecting to this account, if any.'"
op|')'
newline|'\n'
DECL|variable|gatewayType
name|'gatewayType'
op|'='
name|'Attribute'
op|'('
string|"'A C{str} that identifies the protocol used by this account.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'accountName'
op|','
name|'autoLogin'
op|','
name|'username'
op|','
name|'password'
op|','
name|'host'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @type accountName: string\n        @param accountName: A name to refer to the account by locally.\n        @type autoLogin: boolean\n        @type username: string\n        @type password: string\n        @type host: string\n        @type port: integer\n        """'
newline|'\n'
nl|'\n'
DECL|member|isOnline
dedent|''
name|'def'
name|'isOnline'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Am I online?\n\n        @rtype: boolean\n        """'
newline|'\n'
nl|'\n'
DECL|member|logOn
dedent|''
name|'def'
name|'logOn'
op|'('
name|'chatui'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Go on-line.\n\n        @type chatui: Implementor of C{IChatUI}\n\n        @rtype: L{Deferred} L{Client}\n        """'
newline|'\n'
nl|'\n'
DECL|member|logOff
dedent|''
name|'def'
name|'logOff'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sign off.\n        """'
newline|'\n'
nl|'\n'
DECL|member|getGroup
dedent|''
name|'def'
name|'getGroup'
op|'('
name|'groupName'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @rtype: L{Group<IGroup>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getPerson
dedent|''
name|'def'
name|'getPerson'
op|'('
name|'personName'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @rtype: L{Person<IPerson>}\n        """'
newline|'\n'
nl|'\n'
DECL|class|IClient
dedent|''
dedent|''
name|'class'
name|'IClient'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|account
indent|'    '
name|'account'
op|'='
name|'Attribute'
op|'('
string|"'The L{IAccount} I am a Client for'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'account'
op|','
name|'chatui'
op|','
name|'logonDeferred'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @type account: L{IAccount}\n        @type chatui: L{IChatUI}\n        @param logonDeferred: Will be called back once I am logged on.\n        @type logonDeferred: L{Deferred<twisted.internet.defer.Deferred>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|joinGroup
dedent|''
name|'def'
name|'joinGroup'
op|'('
name|'groupName'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @param groupName: The name of the group to join.\n        @type groupName: string\n        """'
newline|'\n'
nl|'\n'
DECL|member|leaveGroup
dedent|''
name|'def'
name|'leaveGroup'
op|'('
name|'groupName'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @param groupName: The name of the group to leave.\n        @type groupName: string\n        """'
newline|'\n'
nl|'\n'
DECL|member|getGroupConversation
dedent|''
name|'def'
name|'getGroupConversation'
op|'('
name|'name'
op|','
name|'hide'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|getPerson
dedent|''
name|'def'
name|'getPerson'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPerson
dedent|''
dedent|''
name|'class'
name|'IPerson'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'name'
op|','
name|'account'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize me.\n\n        @param name: My name, as the server knows me.\n        @type name: string\n        @param account: The account I am accessed through.\n        @type account: I{Account}\n        """'
newline|'\n'
nl|'\n'
DECL|member|isOnline
dedent|''
name|'def'
name|'isOnline'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Am I online right now?\n\n        @rtype: boolean\n        """'
newline|'\n'
nl|'\n'
DECL|member|getStatus
dedent|''
name|'def'
name|'getStatus'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        What is my on-line status?\n\n        @return: L{locals.StatusEnum}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getIdleTime
dedent|''
name|'def'
name|'getIdleTime'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @rtype: string (XXX: How about a scalar?)\n        """'
newline|'\n'
nl|'\n'
DECL|member|sendMessage
dedent|''
name|'def'
name|'sendMessage'
op|'('
name|'text'
op|','
name|'metadata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send a message to this person.\n\n        @type text: string\n        @type metadata: dict\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IGroup
dedent|''
dedent|''
name|'class'
name|'IGroup'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A group which you may have a conversation with.\n\n    Groups generally have a loosely-defined set of members, who may\n    leave and join at any time.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
name|'Attribute'
op|'('
string|"'My C{str} name, as the server knows me.'"
op|')'
newline|'\n'
DECL|variable|account
name|'account'
op|'='
name|'Attribute'
op|'('
string|"'The L{Account<IAccount>} I am accessed through.'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'name'
op|','
name|'account'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Initialize me.\n\n        @param name: My name, as the server knows me.\n        @type name: str\n        @param account: The account I am accessed through.\n        @type account: L{Account<IAccount>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|setTopic
dedent|''
name|'def'
name|'setTopic'
op|'('
name|'text'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Set this Groups topic on the server.\n\n        @type text: string\n        """'
newline|'\n'
nl|'\n'
DECL|member|sendGroupMessage
dedent|''
name|'def'
name|'sendGroupMessage'
op|'('
name|'text'
op|','
name|'metadata'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Send a message to this group.\n\n        @type text: str\n\n        @type metadata: dict\n        @param metadata: Valid keys for this dictionary include:\n\n            - C{\'style\'}: associated with one of:\n                - C{\'emote\'}: indicates this is an action\n        """'
newline|'\n'
nl|'\n'
DECL|member|join
dedent|''
name|'def'
name|'join'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Join this group.\n        """'
newline|'\n'
nl|'\n'
DECL|member|leave
dedent|''
name|'def'
name|'leave'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Depart this group.\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IConversation
dedent|''
dedent|''
name|'class'
name|'IConversation'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    A conversation with a specific person.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'person'
op|','
name|'chatui'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @type person: L{IPerson}\n        """'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        doesn\'t seem like it belongs in this interface.\n        """'
newline|'\n'
nl|'\n'
DECL|member|hide
dedent|''
name|'def'
name|'hide'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        nor this neither.\n        """'
newline|'\n'
nl|'\n'
DECL|member|sendText
dedent|''
name|'def'
name|'sendText'
op|'('
name|'text'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|showMessage
dedent|''
name|'def'
name|'showMessage'
op|'('
name|'text'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|changedNick
dedent|''
name|'def'
name|'changedNick'
op|'('
name|'person'
op|','
name|'newnick'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @param person: XXX Shouldn\'t this always be Conversation.person?\n        """'
newline|'\n'
nl|'\n'
DECL|class|IGroupConversation
dedent|''
dedent|''
name|'class'
name|'IGroupConversation'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|show
indent|'    '
name|'def'
name|'show'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        doesn\'t seem like it belongs in this interface.\n        """'
newline|'\n'
nl|'\n'
DECL|member|hide
dedent|''
name|'def'
name|'hide'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        nor this neither.\n        """'
newline|'\n'
nl|'\n'
DECL|member|sendText
dedent|''
name|'def'
name|'sendText'
op|'('
name|'text'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|showGroupMessage
dedent|''
name|'def'
name|'showGroupMessage'
op|'('
name|'sender'
op|','
name|'text'
op|','
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|setGroupMembers
dedent|''
name|'def'
name|'setGroupMembers'
op|'('
name|'members'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Sets the list of members in the group and displays it to the user.\n        """'
newline|'\n'
nl|'\n'
DECL|member|setTopic
dedent|''
name|'def'
name|'setTopic'
op|'('
name|'topic'
op|','
name|'author'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Displays the topic (from the server) for the group conversation window.\n\n        @type topic: string\n        @type author: string (XXX: Not Person?)\n        """'
newline|'\n'
nl|'\n'
DECL|member|memberJoined
dedent|''
name|'def'
name|'memberJoined'
op|'('
name|'member'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Adds the given member to the list of members in the group conversation\n        and displays this to the user,\n\n        @type member: string (XXX: Not Person?)\n        """'
newline|'\n'
nl|'\n'
DECL|member|memberChangedNick
dedent|''
name|'def'
name|'memberChangedNick'
op|'('
name|'oldnick'
op|','
name|'newnick'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Changes the oldnick in the list of members to C{newnick} and displays this\n        change to the user,\n\n        @type oldnick: string (XXX: Not Person?)\n        @type newnick: string\n        """'
newline|'\n'
nl|'\n'
DECL|member|memberLeft
dedent|''
name|'def'
name|'memberLeft'
op|'('
name|'member'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Deletes the given member from the list of members in the group\n        conversation and displays the change to the user.\n\n        @type member: string (XXX: Not Person?)\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IChatUI
dedent|''
dedent|''
name|'class'
name|'IChatUI'
op|'('
name|'Interface'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|registerAccountClient
indent|'    '
name|'def'
name|'registerAccountClient'
op|'('
name|'client'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Notifies user that an account has been signed on to.\n\n        @type client: L{Client<IClient>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|unregisterAccountClient
dedent|''
name|'def'
name|'unregisterAccountClient'
op|'('
name|'client'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Notifies user that an account has been signed off or disconnected.\n\n        @type client: L{Client<IClient>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getContactsList
dedent|''
name|'def'
name|'getContactsList'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @rtype: L{ContactsList}\n        """'
newline|'\n'
nl|'\n'
comment|"# WARNING: You'll want to be polymorphed into something with"
nl|'\n'
comment|'# intrinsic stoning resistance before continuing.'
nl|'\n'
nl|'\n'
DECL|member|getConversation
dedent|''
name|'def'
name|'getConversation'
op|'('
name|'person'
op|','
name|'Class'
op|','
name|'stayHidden'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        For the given person object, returns the conversation window\n        or creates and returns a new conversation window if one does not exist.\n\n        @type person: L{Person<IPerson>}\n        @type Class: L{Conversation<IConversation>} class\n        @type stayHidden: boolean\n\n        @rtype: L{Conversation<IConversation>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getGroupConversation
dedent|''
name|'def'
name|'getGroupConversation'
op|'('
name|'group'
op|','
name|'Class'
op|','
name|'stayHidden'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        For the given group object, returns the group conversation window or\n        creates and returns a new group conversation window if it doesn\'t exist.\n\n        @type group: L{Group<interfaces.IGroup>}\n        @type Class: L{Conversation<interfaces.IConversation>} class\n        @type stayHidden: boolean\n\n        @rtype: L{GroupConversation<interfaces.IGroupConversation>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getPerson
dedent|''
name|'def'
name|'getPerson'
op|'('
name|'name'
op|','
name|'client'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get a Person for a client.\n\n        Duplicates L{IAccount.getPerson}.\n\n        @type name: string\n        @type client: L{Client<IClient>}\n\n        @rtype: L{Person<IPerson>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|getGroup
dedent|''
name|'def'
name|'getGroup'
op|'('
name|'name'
op|','
name|'client'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Get a Group for a client.\n\n        Duplicates L{IAccount.getGroup}.\n\n        @type name: string\n        @type client: L{Client<IClient>}\n\n        @rtype: L{Group<IGroup>}\n        """'
newline|'\n'
nl|'\n'
DECL|member|contactChangedNick
dedent|''
name|'def'
name|'contactChangedNick'
op|'('
name|'oldnick'
op|','
name|'newnick'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        For the given person, changes the person\'s name to newnick, and\n        tells the contact list and any conversation windows with that person\n        to change as well.\n\n        @type oldnick: string\n        @type newnick: string\n        """'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
