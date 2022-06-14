# PySNMP SMI module. Autogenerated from smidump -f python TCP-MIB
# by libsmi2pysnmp-0.1.3 at Mon Apr  2 20:39:44 2012,
# Python version sys.version_info(major=2, minor=7, micro=2, releaselevel='final', serial=0)

# Imports

( Integer, ObjectIdentifier, OctetString, ) = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
( NamedValues, ) = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
( ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ) = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
( InetAddress, InetAddressType, InetPortNumber, ) = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetPortNumber")
( ModuleCompliance, ObjectGroup, ) = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup")
( Bits, Counter32, Counter64, Gauge32, Integer32, Integer32, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, mib_2, ) = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "Integer32", "Integer32", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "mib-2")

# Objects

tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
tcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 6, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(2,5,1,3,4,)).subtype(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4), ("rfc2988", 5), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoAlgorithm.setDescription("The algorithm used to determine the timeout value used for\nretransmitting unacknowledged octets.")
tcpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: tcpRtoMin.setDescription("The minimum value permitted by a TCP implementation for\nthe retransmission timeout, measured in milliseconds.\nMore refined semantics for objects of this type depend\non the algorithm used to determine the retransmission\ntimeout; in particular, the IETF standard algorithm\nrfc2988(5) provides a minimum value.")
tcpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly").setUnits("milliseconds")
if mibBuilder.loadTexts: tcpRtoMax.setDescription("The maximum value permitted by a TCP implementation for\nthe retransmission timeout, measured in milliseconds.\nMore refined semantics for objects of this type depend\non the algorithm used to determine the retransmission\ntimeout; in particular, the IETF standard algorithm\nrfc2988(5) provides an upper bound (as part of an\nadaptive backoff algorithm).")
tcpMaxConn = MibScalar((1, 3, 6, 1, 2, 1, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpMaxConn.setDescription("The limit on the total number of TCP connections the entity\ncan support.  In entities where the maximum number of\nconnections is dynamic, this object should contain the\nvalue -1.")
tcpActiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpActiveOpens.setDescription("The number of times that TCP connections have made a direct\ntransition to the SYN-SENT state from the CLOSED state.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpPassiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpPassiveOpens.setDescription("The number of times TCP connections have made a direct\ntransition to the SYN-RCVD state from the LISTEN state.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpAttemptFails = MibScalar((1, 3, 6, 1, 2, 1, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpAttemptFails.setDescription("The number of times that TCP connections have made a direct\ntransition to the CLOSED state from either the SYN-SENT\nstate or the SYN-RCVD state, plus the number of times that\nTCP connections have made a direct transition to the\nLISTEN state from the SYN-RCVD state.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpEstabResets = MibScalar((1, 3, 6, 1, 2, 1, 6, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpEstabResets.setDescription("The number of times that TCP connections have made a direct\ntransition to the CLOSED state from either the ESTABLISHED\nstate or the CLOSE-WAIT state.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 6, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpCurrEstab.setDescription("The number of TCP connections for which the current state\nis either ESTABLISHED or CLOSE-WAIT.")
tcpInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInSegs.setDescription("The total number of segments received, including those\nreceived in error.  This count includes segments received\non currently established connections.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutSegs.setDescription("The total number of segments sent, including those on\ncurrent connections but excluding those containing only\nretransmitted octets.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpRetransSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRetransSegs.setDescription("The total number of segments retransmitted; that is, the\nnumber of TCP segments transmitted containing one or more\npreviously transmitted octets.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 13))
if mibBuilder.loadTexts: tcpConnTable.setDescription("A table containing information about existing IPv4-specific\nTCP connections or listeners.  This table has been\ndeprecated in favor of the version neutral\ntcpConnectionTable.")
tcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 13, 1)).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: tcpConnEntry.setDescription("A conceptual row of the tcpConnTable containing information\nabout a particular current IPv4 TCP connection.  Each row\nof this table is transient in that it ceases to exist when\n(or soon after) the connection makes the transition to the\nCLOSED state.")
tcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 1), Integer().subtype(subtypeSpec=SingleValueConstraint(4,6,7,8,5,11,9,12,1,10,2,3,)).subtype(namedValues=NamedValues(("closed", 1), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnState.setDescription("The state of this TCP connection.\n\nThe only value that may be set by a management station is\ndeleteTCB(12).  Accordingly, it is appropriate for an agent\nto return a `badValue' response if a management station\nattempts to set this object to any other value.\n\nIf a management station sets this object to the value\ndeleteTCB(12), then the TCB (as defined in [RFC793]) of\nthe corresponding connection on the managed node is\ndeleted, resulting in immediate termination of the\nconnection.\n\nAs an implementation-specific option, a RST segment may be\nsent from the managed node to the other TCP endpoint (note,\nhowever, that RST segments are not sent reliably).")
tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalAddress.setDescription("The local IP address for this TCP connection.  In the case\nof a connection in the listen state willing to\naccept connections for any IP interface associated with the\nnode, the value 0.0.0.0 is used.")
tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalPort.setDescription("The local port number for this TCP connection.")
tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemAddress.setDescription("The remote IP address for this TCP connection.")
tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemPort.setDescription("The remote port number for this TCP connection.")
tcpInErrs = MibScalar((1, 3, 6, 1, 2, 1, 6, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInErrs.setDescription("The total number of segments received in error (e.g., bad\nTCP checksums).\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpOutRsts = MibScalar((1, 3, 6, 1, 2, 1, 6, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutRsts.setDescription("The number of TCP segments sent containing the RST flag.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpHCInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCInSegs.setDescription("The total number of segments received, including those\nreceived in error.  This count includes segments received\n\n\n\non currently established connections.  This object is\nthe 64-bit equivalent of tcpInSegs.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpHCOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCOutSegs.setDescription("The total number of segments sent, including those on\ncurrent connections but excluding those containing only\nretransmitted octets.  This object is the 64-bit\nequivalent of tcpOutSegs.\n\nDiscontinuities in the value of this counter are\nindicated via discontinuities in the value of sysUpTime.")
tcpConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 6, 19))
if mibBuilder.loadTexts: tcpConnectionTable.setDescription("A table containing information about existing TCP\nconnections.  Note that unlike earlier TCP MIBs, there\nis a separate table for connections in the LISTEN state.")
tcpConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 19, 1)).setIndexNames((0, "TCP-MIB", "tcpConnectionLocalAddressType"), (0, "TCP-MIB", "tcpConnectionLocalAddress"), (0, "TCP-MIB", "tcpConnectionLocalPort"), (0, "TCP-MIB", "tcpConnectionRemAddressType"), (0, "TCP-MIB", "tcpConnectionRemAddress"), (0, "TCP-MIB", "tcpConnectionRemPort"))
if mibBuilder.loadTexts: tcpConnectionEntry.setDescription("A conceptual row of the tcpConnectionTable containing\ninformation about a particular current TCP connection.\nEach row of this table is transient in that it ceases to\nexist when (or soon after) the connection makes the\ntransition to the CLOSED state.")
tcpConnectionLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionLocalAddressType.setDescription("The address type of tcpConnectionLocalAddress.")
tcpConnectionLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionLocalAddress.setDescription("The local IP address for this TCP connection.  The type\nof this address is determined by the value of\ntcpConnectionLocalAddressType.\n\nAs this object is used in the index for the\ntcpConnectionTable, implementors should be\ncareful not to create entries that would result in OIDs\nwith more than 128 subidentifiers; otherwise the information\ncannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.")
tcpConnectionLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 3), InetPortNumber()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionLocalPort.setDescription("The local port number for this TCP connection.")
tcpConnectionRemAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 4), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionRemAddressType.setDescription("The address type of tcpConnectionRemAddress.")
tcpConnectionRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 5), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionRemAddress.setDescription("The remote IP address for this TCP connection.  The type\nof this address is determined by the value of\ntcpConnectionRemAddressType.\n\nAs this object is used in the index for the\ntcpConnectionTable, implementors should be\ncareful not to create entries that would result in OIDs\nwith more than 128 subidentifiers; otherwise the information\ncannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.")
tcpConnectionRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 6), InetPortNumber()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpConnectionRemPort.setDescription("The remote port number for this TCP connection.")
tcpConnectionState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 7), Integer().subtype(subtypeSpec=SingleValueConstraint(4,6,7,8,5,11,9,12,1,10,2,3,)).subtype(namedValues=NamedValues(("closed", 1), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnectionState.setDescription("The state of this TCP connection.\n\nThe value listen(2) is included only for parallelism to the\nold tcpConnTable and should not be used.  A connection in\nLISTEN state should be present in the tcpListenerTable.\n\nThe only value that may be set by a management station is\ndeleteTCB(12).  Accordingly, it is appropriate for an agent\nto return a `badValue' response if a management station\nattempts to set this object to any other value.\n\nIf a management station sets this object to the value\ndeleteTCB(12), then the TCB (as defined in [RFC793]) of\nthe corresponding connection on the managed node is\ndeleted, resulting in immediate termination of the\nconnection.\n\nAs an implementation-specific option, a RST segment may be\nsent from the managed node to the other TCP endpoint (note,\nhowever, that RST segments are not sent reliably).")
tcpConnectionProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnectionProcess.setDescription("The system's process ID for the process associated with\nthis connection, or zero if there is no such process.  This\nvalue is expected to be the same as HOST-RESOURCES-MIB::\nhrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some\nrow in the appropriate tables.")
tcpListenerTable = MibTable((1, 3, 6, 1, 2, 1, 6, 20))
if mibBuilder.loadTexts: tcpListenerTable.setDescription("A table containing information about TCP listeners.  A\nlistening application can be represented in three\npossible ways:\n\n1. An application that is willing to accept both IPv4 and\n   IPv6 datagrams is represented by\n\n\n\n   a tcpListenerLocalAddressType of unknown (0) and\n   a tcpListenerLocalAddress of ''h (a zero-length\n   octet-string).\n\n2. An application that is willing to accept only IPv4 or\n   IPv6 datagrams is represented by a\n   tcpListenerLocalAddressType of the appropriate address\n   type and a tcpListenerLocalAddress of '0.0.0.0' or '::'\n   respectively.\n\n3. An application that is listening for data destined\n   only to a specific IP address, but from any remote\n   system, is represented by a tcpListenerLocalAddressType\n   of an appropriate address type, with\n   tcpListenerLocalAddress as the specific local address.\n\nNOTE: The address type in this table represents the\naddress type used for the communication, irrespective\nof the higher-layer abstraction.  For example, an\napplication using IPv6 'sockets' to communicate via\nIPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would\nuse InetAddressType ipv4(1)).")
tcpListenerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 20, 1)).setIndexNames((0, "TCP-MIB", "tcpListenerLocalAddressType"), (0, "TCP-MIB", "tcpListenerLocalAddress"), (0, "TCP-MIB", "tcpListenerLocalPort"))
if mibBuilder.loadTexts: tcpListenerEntry.setDescription("A conceptual row of the tcpListenerTable containing\ninformation about a particular TCP listener.")
tcpListenerLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 1), InetAddressType()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpListenerLocalAddressType.setDescription("The address type of tcpListenerLocalAddress.  The value\nshould be unknown (0) if connection initiations to all\nlocal IP addresses are accepted.")
tcpListenerLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 2), InetAddress()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpListenerLocalAddress.setDescription("The local IP address for this TCP connection.\n\nThe value of this object can be represented in three\npossible ways, depending on the characteristics of the\nlistening application:\n\n1. For an application willing to accept both IPv4 and\n   IPv6 datagrams, the value of this object must be\n   ''h (a zero-length octet-string), with the value\n   of the corresponding tcpListenerLocalAddressType\n   object being unknown (0).\n\n2. For an application willing to accept only IPv4 or\n   IPv6 datagrams, the value of this object must be\n   '0.0.0.0' or '::' respectively, with\n   tcpListenerLocalAddressType representing the\n   appropriate address type.\n\n3. For an application which is listening for data\n   destined only to a specific IP address, the value\n   of this object is the specific local address, with\n   tcpListenerLocalAddressType representing the\n   appropriate address type.\n\nAs this object is used in the index for the\ntcpListenerTable, implementors should be\ncareful not to create entries that would result in OIDs\nwith more than 128 subidentifiers; otherwise the information\ncannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3.")
tcpListenerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 3), InetPortNumber()).setMaxAccess("noaccess")
if mibBuilder.loadTexts: tcpListenerLocalPort.setDescription("The local port number for this TCP connection.")
tcpListenerProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpListenerProcess.setDescription("The system's process ID for the process associated with\nthis listener, or zero if there is no such process.  This\nvalue is expected to be the same as HOST-RESOURCES-MIB::\nhrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some\nrow in the appropriate tables.")
tcpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 49)).setRevisions(("2005-02-18 00:00","1994-11-01 00:00","1991-03-31 00:00",))
if mibBuilder.loadTexts: tcpMIB.setOrganization("IETF IPv6 MIB Revision Team\nhttp://www.ietf.org/html.charters/ipv6-charter.html")
if mibBuilder.loadTexts: tcpMIB.setContactInfo("Rajiv Raghunarayan (editor)\n\nCisco Systems Inc.\n170 West Tasman Drive\nSan Jose, CA 95134\n\nPhone: +1 408 853 9612\nEmail: <raraghun@cisco.com>\n\nSend comments to <ipv6@ietf.org>")
if mibBuilder.loadTexts: tcpMIB.setDescription("The MIB module for managing TCP implementations.\n\nCopyright (C) The Internet Society (2005). This version\nof this MIB module is a part of RFC 4022; see the RFC\nitself for full legal notices.")
tcpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2))
tcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 1))
tcpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 2))

# Augmentions

# Groups

tcpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 1)).setObjects(*(("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpConnRemAddress"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpConnLocalPort"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpConnLocalAddress"), ("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpCurrEstab"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpConnState"), ("TCP-MIB", "tcpOutRsts"), ("TCP-MIB", "tcpConnRemPort"), ) )
if mibBuilder.loadTexts: tcpGroup.setDescription("The tcp group of objects providing for management of TCP\nentities.")
tcpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 2)).setObjects(*(("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpOutRsts"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpCurrEstab"), ) )
if mibBuilder.loadTexts: tcpBaseGroup.setDescription("The group of counters common to TCP entities.")
tcpConnectionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 3)).setObjects(*(("TCP-MIB", "tcpConnectionProcess"), ("TCP-MIB", "tcpConnectionState"), ) )
if mibBuilder.loadTexts: tcpConnectionGroup.setDescription("The group provides general information about TCP\nconnections.")
tcpListenerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 4)).setObjects(*(("TCP-MIB", "tcpListenerProcess"), ) )
if mibBuilder.loadTexts: tcpListenerGroup.setDescription("This group has objects providing general information about\nTCP listeners.")
tcpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 5)).setObjects(*(("TCP-MIB", "tcpHCOutSegs"), ("TCP-MIB", "tcpHCInSegs"), ) )
if mibBuilder.loadTexts: tcpHCGroup.setDescription("The group of objects providing for counters of high speed\nTCP implementations.")

# Compliances

tcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 1)).setObjects(*(("TCP-MIB", "tcpGroup"), ) )
if mibBuilder.loadTexts: tcpMIBCompliance.setDescription("The compliance statement for IPv4-only systems that\nimplement TCP.  In order to be IP version independent, this\ncompliance statement is deprecated in favor of\ntcpMIBCompliance2.  However, agents are still encouraged\nto implement these objects in order to interoperate with\nthe deployed base of managers.")
tcpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 2)).setObjects(*(("TCP-MIB", "tcpConnectionGroup"), ("TCP-MIB", "tcpListenerGroup"), ("TCP-MIB", "tcpBaseGroup"), ("TCP-MIB", "tcpHCGroup"), ) )
if mibBuilder.loadTexts: tcpMIBCompliance2.setDescription("The compliance statement for systems that implement TCP.\n\nA number of INDEX objects cannot be\nrepresented in the form of OBJECT clauses in SMIv2 but\nhave the following compliance requirements,\nexpressed in OBJECT clause form in this description\nclause:\n\n-- OBJECT      tcpConnectionLocalAddressType\n-- SYNTAX      InetAddressType { ipv4(1), ipv6(2) }\n-- DESCRIPTION\n--     This MIB requires support for only global IPv4\n\n\n\n--     and IPv6 address types.\n--\n-- OBJECT      tcpConnectionRemAddressType\n-- SYNTAX      InetAddressType { ipv4(1), ipv6(2) }\n-- DESCRIPTION\n--     This MIB requires support for only global IPv4\n--     and IPv6 address types.\n--\n-- OBJECT      tcpListenerLocalAddressType\n-- SYNTAX      InetAddressType { unknown(0), ipv4(1),\n--                               ipv6(2) }\n-- DESCRIPTION\n--     This MIB requires support for only global IPv4\n--     and IPv6 address types.  The type unknown also\n--     needs to be supported to identify a special\n--     case in the listener table: a listen using\n--     both IPv4 and IPv6 addresses on the device.\n--")

# Exports

# Module identity
mibBuilder.exportSymbols("TCP-MIB", PYSNMP_MODULE_ID=tcpMIB)

# Objects
mibBuilder.exportSymbols("TCP-MIB", tcp=tcp, tcpRtoAlgorithm=tcpRtoAlgorithm, tcpRtoMin=tcpRtoMin, tcpRtoMax=tcpRtoMax, tcpMaxConn=tcpMaxConn, tcpActiveOpens=tcpActiveOpens, tcpPassiveOpens=tcpPassiveOpens, tcpAttemptFails=tcpAttemptFails, tcpEstabResets=tcpEstabResets, tcpCurrEstab=tcpCurrEstab, tcpInSegs=tcpInSegs, tcpOutSegs=tcpOutSegs, tcpRetransSegs=tcpRetransSegs, tcpConnTable=tcpConnTable, tcpConnEntry=tcpConnEntry, tcpConnState=tcpConnState, tcpConnLocalAddress=tcpConnLocalAddress, tcpConnLocalPort=tcpConnLocalPort, tcpConnRemAddress=tcpConnRemAddress, tcpConnRemPort=tcpConnRemPort, tcpInErrs=tcpInErrs, tcpOutRsts=tcpOutRsts, tcpHCInSegs=tcpHCInSegs, tcpHCOutSegs=tcpHCOutSegs, tcpConnectionTable=tcpConnectionTable, tcpConnectionEntry=tcpConnectionEntry, tcpConnectionLocalAddressType=tcpConnectionLocalAddressType, tcpConnectionLocalAddress=tcpConnectionLocalAddress, tcpConnectionLocalPort=tcpConnectionLocalPort, tcpConnectionRemAddressType=tcpConnectionRemAddressType, tcpConnectionRemAddress=tcpConnectionRemAddress, tcpConnectionRemPort=tcpConnectionRemPort, tcpConnectionState=tcpConnectionState, tcpConnectionProcess=tcpConnectionProcess, tcpListenerTable=tcpListenerTable, tcpListenerEntry=tcpListenerEntry, tcpListenerLocalAddressType=tcpListenerLocalAddressType, tcpListenerLocalAddress=tcpListenerLocalAddress, tcpListenerLocalPort=tcpListenerLocalPort, tcpListenerProcess=tcpListenerProcess, tcpMIB=tcpMIB, tcpMIBConformance=tcpMIBConformance, tcpMIBCompliances=tcpMIBCompliances, tcpMIBGroups=tcpMIBGroups)

# Groups
mibBuilder.exportSymbols("TCP-MIB", tcpGroup=tcpGroup, tcpBaseGroup=tcpBaseGroup, tcpConnectionGroup=tcpConnectionGroup, tcpListenerGroup=tcpListenerGroup, tcpHCGroup=tcpHCGroup)

# Compliances
mibBuilder.exportSymbols("TCP-MIB", tcpMIBCompliance=tcpMIBCompliance, tcpMIBCompliance2=tcpMIBCompliance2)