# Final notes

### Question 3 Bridges vs Routers

Bridges need to pick up everything! While Routers only pick up what you give it. Therefore, we need Bridges to transmit at LAN rates.

### Question 4 Route Computation

Link state is robust to link failure. No count-up in link state. Distance vector is NOT robust to failures.

### Question 5 Peering

You carry my customers, I carry your customers, and if traffic is similar lower latency and less cost

### Question 7 Link State Routing

Link state flooding is used to build the forwarding database. To avoid a circularity.

### Why is DNS a good idea??

Allows machine translation to IP addresses. It is kind of like a UI. Makes it easier to translate domain names to IPs

### Why is BGP a path vector protocol vs Distance vector

Avoids the count to infinity problem?? Paths give you instrument for policy that depend on all people in your path.

Problem is when nodes recirculate their routes and it adds up.

### Fragmentation

Packet ID field was used for fragmentation, but today we try sizes and we get to the max smallest size we can fit. The router sends back a message if it can fit or not

### TCP congestion control and RED

It is an early congestion warning. RED doesn't do this until it is around 80% full (makes sure we detect congestion early)

Sender will slow down

### Transport

Data link is FIFO but the network is Non-FIFO. You need the largest space to accomodate delayed packets.

TOPICS TO GO OVER:

Routing, DNS, ARP, IP Forwarding, LANs and across networks



## IP Addressing

### 1 Connectionless Routing

Each packet is on its own and finds a path through the network

**Routing is done to addresses! Domain names are mapped to 32-bit IP using DNS and all packets are sent to hat address.**

Hierarchy is crucial for scalability, since we can store hundreds of thousands of prefixes!

### 2 Structure of Addresses

The routing protocol can be hierarchical if addresses are hierarchical

We need *flexible hierarchies* since we do not know whether to divide into lots of subnets or a few large subnets.

#### 2.1 IP Addresses: From Classful to Classless addresses

Internet began with a simple hierarchy where 32 bit addresses were divided into a network address and a host number; routers only stored entries for networks

Initially network number was 1 byte and host address was 3 bytes (4bytes total)

However, it evolved because of three things:

1. Ethernets: The old model assumed a few large networks, each of which had a lot of hosts. When ethernets were introduced, rethought;

They separated it into classes (if first few buts of address started with a 0, then Class A, if first 2 bits started with 10, then Class B (w/ network number of 16 bits), if first 3 started with 110, then Class C (with network number of 24 bits))

Class C were introduced for orgs with small networks (allowed large # of networks with 256 hosts each)

Class B allowed medium size networks.

Class A was reserved for very large networks

Router forwarding tables were still easy to impl., a core router had to have 3 sets of hash tables, one for Class A, Class B, and Class C.

When a packet arrived, destination IP was parsed to see if it was Class A, B, or C

Depending on which it was, network # was extractded and looked up in the appropriate table to see what the next hop or next router was. If final hop, the packet was sent (for Ethernet, this is ARP)

2. Class B Address Depletion

Many orgs. wanted class B addresses and so they ran out.

Naive solution was to assign a bunch of class C to every or. but then the core router forwarding table size and router control traffic go up

CIDR assigns new orgs. multiple contiguous Class C addresses that can be aggregated by a common prefix

3. Depletion of the Entire Address Space

Internet registries are very conservative in the assignment of IPs. Small Org will be given on small portion of Class C addresses, /30 (only allows 4 IP addresses within organization)

Most companies cope w/ use by using NAT (Network Address translation)

NAT works by using TCP port numbers (dest is 16 bits, source is 16 bits) in every packet to extend the IP address space to 64 bits

First idea is that org. uses private IP addresses locally (not globally unique but each org. can reuse locally)

Sharing locally is fine! (if A uses address P1-P8 and B uses addresses P1-P8) but if you want to talk to other parties on Internet like a web server, doesn't work

NAT box for Org. A is given a single global address G which is globally unique. When packet from Host 1 in the org. wants to connect to the outside world, the NAT box sends it on its way after translating the soure IIP from P1 to G.

This works until the reply comes back (if packet from Host 2 (address P2) to the same server has also been sent out), when the reply comes back (it will be to dest. G, since remote server doesn't know abt. NAT). How does the NAT box tell its for Host 1 or 2??

IT USES PORT NUMBERS!!!!

NAT box can remember each Host's port number when the packet is sent. When the reply comes back, the NAT box can distinguish from the port numbers in the reply whether it is for Host 1 or Host 2.

If two hosts use the same port, it translates the destination IP address but it also translates the source port to pick any currently unused port! It ensures that any set of concurrent conversations via the NAT box can be told apart when the reply comes back!

CIDR and NAT help the Internet handle exponential growth with a finite 32-bit address space.

#### 2.2 Prefix Notation

CIDR (supernetting) and subnetting allow more careful allocation of the address space

Supernetting means to combine smaller networks into a larger one. It does this by decreasing the subnet mask /24 - /22. It is used to simplify routing in ISPs and large networks. It also aggregates routing info.

Subnetting divides a network into smaller subnets. We do this by increasing our subnet mask bits (/24 - /26). It is used to optimize address usage within organizations and reduces broadcast domains

Internet prefixes are defined using bits and not alphanumerical characters (up to 32 bits in length). IP prefixes though are written in dot-decimal notation.

Each of the decimal digits between dots represents a byte.

Prefixes can be variable length, so another way to denote a prefix is A/L. A is the 32 bit IP address in dot-decimal notation and L denotes the length of the prefix.

Thus the UCSD prefix can also be denoted as 132.239.0.0/16 (16 indicates only first 16 bits are relevant *132.239). Each number btwn dots is a byte

We can also use a mask in place of an explicit prefix length. Thus the UCSD prefix
can also be described as 128.239.0.0 with a mask of 255.255.0.0.

### 3. Neighbor Routing

*Endnodes* are hosts, user workstations (large numbers dedicated to computing)

*Routers (IMPs, Gateways)* (smaller numbers dedicated to communication)

On a point-point link, neighbor routing is p. easy. If an endnode is attached to a router, the endnode simply sends all its data packets to the router. It can be configured or learned from hellos the routers Data Link and IP address. The hello protocol can be used btwn the two nodes (router-router or router-endnode) on a point-point link to see if the link is up and to exchange Data Link and IP addresses.

HOWEVER, neighbor routing on a LAN is a little more complicated. in an LAN there are choices as to who to send the packet to, and a simple hello protocol btwn every endnode and every router wouldn't be scalable

#### 3.1 Neighbor Routing on a LAN

6 Problems:

1. Routers need network addresses of endnodes. When a router gets a packet for an endnode (E1 on its LAN), it needs to know that the endnode is on the LAN so that the routing process can terminate and the final packet be launched on the LAN

2. Routers need Data Link addresses of endnodes. Even when a router gets a packet and it knows that E1 is on its LAN, it needs to know E1's MAC address. Every node on a LAN has a 48-bit LAN address and this is not related to its IP address. We cannot send a packet to a station on a LAN and have that station pick up the packet without sending to the station's MAC address.

3. Endnodes need the Data Link address of at least one router. Endnodes need to be simple and so it suffices for them to know the IP and Data Link address of at least one router so that they can send all packets to be routed to that router!

4. E1 and E2 traffic shouldn't have to go through a router (Endnodes on the same LAN). It is wasteful! Every packet btwn them is sent twice on the LAN doubling traffic on the LAN. If most traffic is local, this is a waste of LAN bandwidth. Ideally traffic should eventually or always go directly.

5. E1 and E3 traffic (endnodes on different LANs) should go through R2 eventually (router that connects both LANs).

6. If R1, R2 are down, E1 and E2 should be able to communicate!

**THE IP SOLUTION! OSI ROUTING MODEL**

1. Routers need network addresses of endnodes. All endnodes on the same LAN use the same prefix, so the router is configured with the prefix of every interface! Checking by whether the prefix of an endnode matches the prefix associated with an interface means the Router nodes if an endnode is up on that interface!

2. Routers need Data Link addresses of endnodes. IP takes the position that a hello protocol btwn 1000s of endnodes and several routers is unscalable. Therefore, when an IP node wants the MAC address of another node (whether router or endnode), it simply broadcasts an ARP request to the ENTIRE LAN!!

ARP request is a broadcast packet sent to all the 1's MAC address which makes sure that every station on the LAN picks it up.

Ex. Suppose R1 wants E1's MAC address:

 - R1 sends an ARP request with its own MAC address as the data link header source with all 1's address in the Data Link layer destination address. Inside the packet is a field that says this is an ARP packet and the 32-bit IP address of E1. Essentially saying "if you are E1, please reply with your MAC address". All stations pick up the broadcast on the LAN and all stations besides E1 discard the packet.

 - E1 replies with a so-called ARP response. E1 puts in the MAC source address sent in the ARP request as the destination address and places its own MAC address in the MAC source address. The ARP response contains E1's IP address in the routing header and thus when R1 gets the ARP it can realize that the MAC address corresponding to the IP address E1 is in the source MAC address of the ARP response. Since ARP is such a high overhead process, R1 will **CACHE** the mapping btwn E1's routing and MAC address. All subsequent packets btwn R1 to E1 won't need to do an ARP anymore!

3. Endnodes need Data link address of at least one router. IP endnodes are either statically configured or are provided with a router address by an auto-configuring protocol DHCP! DHCP works by using DHCP servers on the LAN; DHCP servers can be found using a common multicast address. With DHCP, a new endnode can get both its prefix and its router!

4. E1 to E2 traffic shouldn't have to go through a router! In IP, E1 doesn't send traffic to E2 via any of the routers. Instead, E1 checks whether E2 matches the same prefix which it has been configured with (i.e. if it uses a mask it simply uses the mask to AND both addresses E1 and E2, and notices that the unmasked value is the same) before sending to a router. If they have the same prefix, E1 assumes E2 is on the same LAN and tries to send directly. If it doesn't have a cached MAC address for E2, E2 does an ARP just like routers.

5. E1 to E3 traffic should go through R2 eventually. Whenever a router sends a packet back on the same interface it arrived on, the router sends a second packet called a **Redirect packet.** The redirect packet is sent directly to the source of the packet and says "Send to R2 in the future!". On receiving a redirect, E1 maintains a small cache that maps from E3 to R2. Endnodes always consult this preferred router cache before sending a packet to a destination IP address.

6. If R1 and R2 are down, sol. to problem 4 should fix this.

## Route Comparison

Problem lies in deciding which path should be chosen to route btwn subnets that are connectd by routers.

When a failure occurs, which NEW path should be chosen??

Route comparison is different within an enterprise and btwn enterprises!

If in a local network, we have a core section of routers that connect endnodes and subnets within local network. Called Enterprise networks and are typically managed by a single entity and don't provide transit service for other enterprises (DOMAIN and given an AS number)

Enterprise is also connected to an ISP called CENIC which is connectd to other ISPs

To get from Point A to point B the packet may have to traverse a couple ISPs like MCI, UUNET, and Sprint. These ISPs provide transit service, and the collection of these ISPs form the Wide Area Network (WAN).

The WAN is comprised of individual ISPs, each of which has their own AS number and are managed separately.

We separate route computation into two components:

1. Routing within a domain (intra-domain routing): finding shortest routes btwn co-operating entities within an enterprise. Distance Vector and link state routing. Distance vector is used within small enterprises and Link state is used within most ISPs

Inter-domain routing is left to policy routing which doesn't even compute shortest paths and settles for routes that comply with each individual ISPs local policy. The only protocol in use is BGP-4 (Border Gateway Protocol). Every leaf domain will have some routers that speak BGP (BGP speakers) and communicate with a BGP router(s) at their upstream ISP in order to relay packets outside the enterprise

### 1 Intra-domain routing

Distance vector resembles protocol that bridges use to compute a spanning tree.

Main problem is the count-to-infinity problem! (Slow convergence after failures)

#### 1.1 Distance Vector Routing

In spanning trees, bridges find distances to min ID node (root node) by "gossiping" with their neighbors. Distance vector uses the same idea for updating distance to all nodes

Bridges keep a single triple (Root, distance, parent) that each bridge reports to its enighbors. In distance vector, each router in an enterprise keeps a vector (ID, distance) where ID is the ID of a subnetwork in an Enterprise (i.e. ECE) where a subnetwork is identified by a prefix. Each enterprise router maintains a *vector* of distances to each subnetwork in the enterprise

A real distance vector has n components, one for each n subnetwork

The way the protocol works is that a router gets updates from its neighbors about total cost to a specific subnet and then relays this information to other routers with endnodes

**Distance Vector Databases:** Router needs to have a port database for each neighbor (contains vector reported by that neighbor) and a central database(containing vector that is this router's current best estimate to all subnets in the enterprise)

The distance vector databases have a port database for each neighbor (port 1, port 2) with cost calculations for each neighbor, and then a central database with the minimum cost for each neighbor regardless of port.

The central table has two pieces of info for each subnet: the cost and port number to reach to get to that subnet (i.e. the least cost to get to C is 2 and the best way is through P2)

Algorithm:

1. When a new distance vector is received by a neighbor on an interface, the distance vector is sored in the corresponding port database. The distance vector algorithm is then run to check if the central database needs to be updated (subnet by subnet). If there are changes, the central database is updated and the resulting changed database is sent as a new distance vector (only first and third columns) on all interfaces of the router (to each neighbor). This process continues until all the central databases settle down. The process resumes again after a failure occurs

The router's *forwarding table* is the first two columns of the central table. We only need to know the interface if we wanna know where to forward, cost is only useful to compute routes and to send to neighbors

**Distance Vector Dynamics:** Routers are preconfigured with the prefix of a specific endnode being reachable on some interface

A router sends a distance vector update of its central database info

Until the update to a router arrives, a router cannot update a subsequent router to reflect a better route.

After an update is received, it is broadcast to all of its neighbors!

**Link Failures:** Neighbor discovery will detect a link failure since hellos aren't being received! The router will delete the stored distance vector on that interface and recomputes its central database, and the algorithm continues until stabile.

However, the router has a stored port database entry for another neighbor and it recalculates its best cost to be what was stored in the other neighbor plus the cost to that neighbor! (10 in the case of the example!)

**Count-to-Infinity Problem:** When a subnet is completely cut off from the source (no valid path), it will take a while for the routers to figure this out. (this case happens when routers crash or links fail very closely, our routers won't update quick enough and we get bizarre values)

The new distance corresponds to no path in the network! This is basd because we send bizarre updates to our neighbors. We keep sending updates back and forth and the ECE values increase to infinity.

When the distance goes over a certain threshold, RIP (distance vector protocol), that destination is defined as unreachable and the routers finally realize the distance is unreachable.

Another Problem is *data packet looping*!

If someone tries to connect to a website at the destination that is unreachable, both routers in the disconnected subnet will send the packet to each other over and over, since both routers believe the other is the best route to the destination. Links can be filled with several such packets looping btwn routers

This problem is inevitable in data networks because one router can shift to a route before its neighbors. Till the neighbor also picks up the new routes, the two routers have inconsistent route info and so data packets can loop. Data packet looping in distance vector is a lot MORE SERIOUS

*Naive solution is to have R6 never send an update to R5 if its central database was computed based on an update from R5, but this can't work for the other routers in the subnet for their route to the destination

**ACTUAL FIX**

We can have each distance vector update list the path of routers as well as the distance.

###  2 Link State Routing

Link state routing has quicker response to failures and no count-up problem

**Link State Basic Idea**

1. LSP Generation: Each node knows by default (manager settable) cost of its outgoing links. Neighbor discovery is used to compile a list of neighbors that are up. This info, along with link costs is placed in a Link State Packet (LSP)

2. LSP Prop.: Each source broadcasts its LSP to all other nodes using intelligent flooding

3. Dijkstra Shortest Path Computation

After LSP prop. process stabilizes, each node has a complete and identical picture of the network graph. Then each node S uses any shortest path algo. to compute the next node on the shortest path from S to every other node D

**Steps in detail**

1. LSP Generation

Each router computes a list of adjacent neighbors routers (or prefixes) that are currently up (verified by hellos) and places this info in a link state packet. The LSP describes the local neighborhood of a router.

LSP is a local snapshot of costs to neighbors!

On a failure:

New link state packet sent from a neighbor involved in the crash will NOT contain the link from that router to the one that crashed! As usual the hellos are timed out and R4 will delete the link from its LSP and then attempt to propogate the new LSP from itself to the entire network. Propogation of all post-failure LSPs will produce the correct map of the network after failures!

In the example, only R4 and R6 will notice the failure and regenerate and broadcast their LSPs, other routers do not have to generate new LSPs and so don't have to boradcast their current LSPs again!

2. Intelligent Flooding

Naive solution is that when a router receives an LSP, it should forward the packet to all other neighbors.

This only works for bridges because the bridge topology is a *spanning tree*

When there is a loop, flooding can cause LSPs to go around forever in loops. We also want a notion of "recentness": after a failure, we want the newest LSP sent by a router to go to every other router

The problem is called when R3 receives a copy of L back from R4 which it already has! R3 should not flood the packet again.

R3 should not flood a duplicate of a LSP it has already received. To suppress duplicates, we can compare an incoming LSP with the contents of a stored LSP. With reliable data links, this is more efficiently done by attaching a *sequence number* to each LSP. A sequence number also gives you a notion of recentness:

When R1 wants to send a new LSP, it increments its sequence number to persuade the other routers to accept its most recent offering and discard older LSPs stored for R1.

**Intelligent Flooding vs. Ordinary Flooding:**

When a router R receives a LSP L with LSP source S and sequence number x, router R first looks to see if it has stored LSP L' for source S. If R doesn't have a stored L' from S, R does ordinary flooding on L. If R does have a stored copy L', it compares the sequence number of L', (i.e. y) with sequence number x of the incoming LSP L. If x <= y, R assumes this is a duplicate or an older LSP and discards the LSP (most link state applications also send an ACK back to the previous neighbor to stop retransmissions). If x > y, then R assumes it has 'more recent' information from S and does ordinary flooding on L (Sends it on all interfaces except the one it has received it on, and sends an ACK back on the interface on which it received L)

After the process terminates, every router has a copy of LSP sent from a router.

Each router has an LSP database which contains the latest stored LSP received from every other router in the network.

**LSP ROUTING IS DONE WITHIN AN ENTERPRISE, THEY ARE NOT FLOODED OUTSIDE AN ENTERPRISE**

Very large enterprises or ISPs are broken into smaller areas and LSP flooding only occurs within the area, with another inter-area protocol btwn areas. So, expect LSP databases to have no more than a few thousand entries.

Other subtleties with intelligent flooding:

1. Jumping

Imagine a router sends 50000 LSPs and then crashes. every other router has LSPs w/ sequence number 50000. When the router comes back to life it sends an LSP with sequence number 1. Since 1 < 50000, every router discards the new LSP!

Solution: Modify the rules of LSP prop.: when a router R receives an older LSP, instead of discarding the LSP, the router sends back its stored LSP to the neighbor who sent it to the router. Also, when a source like R1 receives a copy of its own LSP with a larger sequence number z than its current LSP, R1 jumps to z + 1 and sends its current stored LSP with sequence number z + 1 to all neighbors. If router sends SEQ number 1 and receives 50000 back from a neighbor, the router will jump to 50001 and send it back to all neighbors.

2. Aging

What happens when a router reaches the maximum of its sequence number space??

If we make it wrap around like sliding window, we can have L1, L2, L3, where L1 < L2 < L3 but L3 < L1.

The three updates kept looping through the network. Current LSPs use linear sequence number space, and they use a large space (64 bits) which makes reaching the top of the space super unlikely.

If at all a bug causes this to happen we use two safeguards: all LSPs are also aged out. Every LSP carries an age field and is aged out after half an hour (this forces routers to send a new LSP every half hour even if no data has changed)

In the worst case, a source router would be disbelieved for half an hour.

After all routers time out its older LSPs, it can start again at sequence number 1. Even th delay can be avoided if each router has multiple IP addresses (which they all do since they need an IP address for each interface). If the previous LSP used source address X, the router can come up and send new LSPs with an alternate IP address Y.

It's as if a router with source address X crashed and an identical looking router called Y came in place of X.

3. Computing Routes

In most routers, the routing table together with the LSP database are stored in a route processor (PC like processor with lots of slow memyr to store the (large) LSP database

The forwarding table is stored in fast memory, which is sometimes shared by all router interfaces but is sometimes replicated on every interface

Once LSP propogation stabilizes and every router has the LSP of every other router in the enterprise, a decision process can run at every router to compute the shortest path routes from that router to all prefixes in the network

In practice, real routers never know when the set of LSPs have stabilized. When a new LSP arrives, a router recomputes its shortest paths. If new LSPs arrive during the route comp., the old route computation is not abandoned. Instead the new LSPs are held for the next computation that starts when the previous computation has finished.

## BGP

The current wide-area routing protocol which exchanges reachability info. about routeable IP-address prefixes btwn routers at the boundary btwn ISPs

The wide-area rounding architecture is divided into *autonomous systems* (ASes) that exchange reachability info.

An AS is owned and administered by a single commercial entity and implements a set of policies in deciding how to route its packets to the rest of the internet. Each AS implements some set of policies in deciding how to route its packets to the rest of the internet and how to export its routes to other ASes

Each AS is identified by a unique 16-bit number

A different routing protocol operates within each AS (called IGPs) and includes (Routing Information Protocol (RIP))

BGP (interdomain protocol) is also called an EGP (Exterior Gateway Protocol)

Key difference btwn BGP and IGPs is that the former is concerned with providing *reachability info* and facilitating *routing policy* impl. in a *scalable* manner. The latter is concerned with optimizing a path metric.

### 4.2 Inter-AS Relationships: Transit and Peering

Internet has many ASes (universities to corps. to regional ISPs to nationwide ISPs)

First form of AS-AS interconnection is **provider-customer transit:**

One ISP provides access to all (or most) destinations in its routing tables!

Provider charges customer

Second form is called **peering**

Two ASes provide mutual access to a subset of each others' routing tables. Peering is a business deal. The subset is to share their transit customers

#### 4.2.1 Peering v. Transit

Peering relationships are btwn business competitors:

each party knows that a non-trivial fraction of the packets emanating from each one is destined for other's direct transit customers (best thing to do would be to get the other's customes, but they wouldn't be able to. So, this is the next best thing, instead of paying transit costs to their respective providers, they would set up a transit-free link btwn each other to forward packets for their direct customers)

Better since this is a more direct path! (better end-end performance in terms of latency, packet loss rate, and throughput) for their customers

#### 4.2.2 Exporting Routes: Route Filtering

Each AS (ISP) needs to make decisions on which routes to export to its neighboring ISPs using BGP

An AS should advertise routes to neighbors with care

**Transit customer routes**

To an ISP, its customer routes are the most important, because the view it provides to its customers is the sense that *all* potential senders in the Internet can reach them!

It is in the ISPs best interest to advertise routes to its transit customers to as many other connected ASes as possible.

The more traffic an ISP carries on behalf of a customer, higher revenue for ISP.

**Transit Provider routes**

ISP doesn't want to provide *transit* to the routes exported by its provider to it.

**Peer routes**

Makes sense for an ISP to export only selected routes from its routing tables to other peering ISPs

ISPs end up providing *selective transit:* Typically, full transit capabilities for their own transit customers in both directions, some transit(btwn mutual customers) in a peering relationship, and transit only for one's transit customers (and ISP-internal addresses) to one's providers

#### 4.2.3 Importing Routes

When a router hears many possible routes to a destination network, it needs to decide which route to install in its forwarding tables

When a router hears advertisements to its transit customers from other Ases, it needs to ensure that packets to the customer do not traverse additional ASes unnecessarily.

So, customer routes are prioritized over routes to same network advertised by providers or peers.

**customer > peer > provider**

This rule can be impl. in BGP using a special attribute that's locally maintained by routers in an AS (LOCAL PREF) attribute. First rule of BGP is to select a route based on this attribute.

Only when the attribute is not set are other attributes of a route even considered.

### 4.3 BGP

#### 4.3.1 Design Goals

1. **Scalability.** BGP needs to ensure that the Internet routing infrastructure remained scalable as the number of connected networks increased.

2. **Policy.** The ability for each AS to implement and enforce various forms of routing policy.

3. **Cooperation under competitive circumstances.** BGP was designed in large part to handle the transition from the NSFNet to a situation where the "backbone" Internet infrastructure would no longer be run by a single administrative entity. This structure implies that the routing protocol should allow ASes to make purely local decisions on how to route packets

#### 4.3.2 The Protocol

BGP runs over TCP, on port 179.

To start participating in a BGP session with another router, a router sends an OPEN message after establising a TCP connection to it on the BGP port.

After the OPEN is completed, both routers exchange their tables of all active routes

After the initialization there are two main types of messages on the BGP session:

1. BGP Routers send route UPDATE messages sent on the session. These updates only send any routing entries that have changed since the last update (or transmission of all active routes). There are two kinds of updates:

  - *announcements* - changes to existing routes or new routes
  - *withdrawals* - messages that inform the receiver that the named routes no longer exist

A withdrawal only happens when some previously route can't be used

Because BGP uses TCP, which provides reliable and in-order delivery, routes do not need
to be periodically announced, unless they change.

But, in the absence of periodic routing updates, how does a router know whether the
neighbor at the other end of a session is still functioning properly?

Answer: BGP could have "keepalive" messages, or "is the peer alive" message protocol. BGP implements its own since TCP doesn't.

Each BGP session has a configurable keepalive timer, and the router generates that it will attempt to send at least one BGP message during that time. If there are no UPDATE messages, then the router sends the second type of message on the session: KEEPALIVE messages. The absence of a certain number of BGP KEEPALIVE messages on a session causes the router to terminate that session.

The number of missing messages depends on a configurable times called the *hold timer*

Unlike many IGP’s, BGP does not simply optimize any metrics like shortest-paths or
delays. Because its goals are to provide reachability information and enable routing poli-
cies, its announcements do not simply announce some metric like hop-count. Rather, they
have the following format:
     IP prefix : Attributes
where for each announced IP prefix, one or more attributes are also announced.

Recall that one BGP attribute has already been introduced, the LOCAL PREF attribute.
This attribute isn’t disseminated with route announcements, but is an important attribute
used locally while selecting a route for a destination. When a route is advertised from a
neighboring AS, the receiving BGP router consults its configuration and may set a LOCAL
PREF for this route.

#### 4.3.3 Disseminating Routes within an AS: eBGP and iBGP

Two types of BGP sessions: eBGP sessions are btwn BGP-speaking routers in different ASes while iBGP sessions are btwn BGP routers in the same AS. They use the same protocol but for different purposes

eBGP is the "standard" mode in which BGP is used. BGP routers in eBGP implement route filtering rules and exchange a subset of their routes with routers in other ASes

Each AS will have more than one router that participates in eBGP sessions with neighboring ASes. During this process, each router will obtain info about some subset of all the prefixes that the entire AS knows about. Each such eBGP router must disseminate routes to the external prefix to all the other routers in the AS.

This dissemination is done to meet two goals:

1. *Loop-free forwarding* - The resulting routes (and the subsequent forwarding paths of packets sent along these routes) picked by all routers should be free of deflections and forward loops.

2. *Complete visibility* - The several eBGP-speaking routes in the AS must exchange external route info. so that they have a complete view of all external routes. **One of the goals of BGP is to allow each AS to be treated as a single
monolithic entity.**

How should iBGP sessions be run (purpose is to update external routing info of all routers)

One solution:

Use an arbitrary connected graph and "flood" updates of external routes to all BGP routers in an AS.

We set up a *full mesh* of iBGP sessions (every eBGP router maintains an iBGP session with every other BGP router in the AS). Flooding updates is simple now:

an eBGP router sends UPDATE messages to its iBGP neighbors. An iBGP router does not have to send any UPDATE messages because it does not have any eBGP sessions with a router in another AS.

It is important to note that iBGP is not an IGP like RIP or OSPF, and it cannot be used to
set up routing state that allows packets to be forwarded correctly between internal nodes
in an AS. Rather, iBGP sessions, running over TCP, provide a way by which routers inside
an AS can use BGP to exchange information about external routes. In fact, iBGP sessions
and messages are themselves routed between the BGP routers in the AS via whatever IGP
is being used in the AS!

Why do we use iBGP instead of IGP?

1. Most IGPs don't scale as well as BGP does, and often rely on periodic routing announcements rather than incremental updates

2. IGPs usually don't implement the attributes in BGP

What is a route reflector??

A route reflector is a BGP router that can be configured to have *client* BGP routers.

A route reflector selects a single best route to each destination prefix and announces that route to all of its clients

An AS with a route reflector configuration follows the following rules in route updates:

1. If a route reflector learns a route via eBGP or via iBGP from one of its clients, it re-advertises that route over all of its sessions to its clients

2. If a route reflector learns a route via iBGP from a router that is not one of its clients, then it re-advertises the route to its client routers, *but not over any other iBGP sessions!*

The route reflector is used to reduce the number of iBGP connections in an AS. It is used to address the scalability issue of the full-mesh requirement in iBGP!

Many networks deploy multiple route deflectors, organizing them hierarchically

**BGP route updates propagate differently depending on whether the update is propagat-
ing over an eBGP session or an iBGP session. An eBGP session is typically a point-to-point (IP addresses of each router on either end of the session are directly connected with one another and are typically on the same LAN)

When an eBGP session is point-to-point, the next-hop attribute for the BGP route is guaranteed to be reachable, as is the other end!

A router will advertise a route over an eBGP session regardless of whether that route was originally learned via eBGP or iBGP

Also, an iBGP session may exist btwn two routers that are NOT directly connected, and in iBGP, the routers rely on the AS's internal routing protocol (IGP) to both (1) establish connectivity btwn two endpoints of the BGP session and (2) establish the route to the next-hop IP address named in the route attribute

#### 4.3.4 BGP Policy Expression: Filters and Rankings

BGP allows network operators to configure routers to manipulate route attributes when disseminating routes.

Network operators can configure routers to perform the following:

1. Control how router ranks candidate routes and selects paths to destinations

2. Control the "next hop" IP address for the advertised route to balance load

3. "Tag" a route to control how the ranking and filtering functions on other routers treat the route.

#### 4.3.5 NEXT HOP Attribute

BGP route announcement has set of attributes associated with each prefix

NEXT HOP attribute: gives the IP address of the router to send the packet to. As the announcement propogates across an AS boundary, the NEXT HOP field is changed.

For iBGP speakers, the first router that introduces the route into iBGP sets the NEXT HOP attribute to its loopback address (address that all other routers within the AS can use to reach the first router).

All other iBGP routers within the AS preserve this setting and use the Ases IGP to route any packets destined for the route toward the NEXT HOP IP address.

In general, packets destined for a prefix flow in the opposite direction to the route announcements for the prefix

ASPATH attribute: vector that lists all the ASes in reverse order that this route announcement has been through

Upon crossing an AS boundary, the first router prepends the unique identifier of its own AS and propogates the announcement on.

This use of a "path vector" (list of ASes per route) is the reason BGP is classified as a path vector protocol

A path vector serves two purposes:

1. Loop avoidance: When we cross an AS boundary, the router checks to see if its own AS identifier is already in the vector. If it is, it discards the route announcement since importing this route would simply cause a routing loop when packets are forwarded

2. Help pick a suitable path from among multiple choices!

If no LOCAL PREF is present fro a route, then the ASPATH length is used to decide on a route

Shorter ASPATH lengths are preferred than longer ones

**The LOCAL PREF attribute is always given priority over ASPATH**

**MED ATTRIBUTE**

There are many situations when two ASes are linked at multiple locations, and one of them
may prefer a particular transit point over another. This situation can’t be distinguished us-
ing LOCAL PREF (which decides which AS’ announcement to import) or shortest ASPATH
(since they would be equal). A BGP attribute called MED, for multi-exit discriminator is used
for this.

MED attribute allows an AS to tell another how to choose btwn multiple NEXT HOPs for a prefix. Each router will pick the smallest MED from among multiple choices coming from the same neighbor AS.

MEDs are usually ignored in AS-AS relationships that don't have some form of financial settlement.

Most peering arrangements ignore MED. This leads to a lot of asymmetric routes in the Wide-area internet.

### 4.4.2 Convergence Problem

BGP doesn't always converge quickly after a fault is detected and routes withdrawn. Depending on the eBGP session topology btwn ASes, this could involve the investigation of many routes before we get route convergence



