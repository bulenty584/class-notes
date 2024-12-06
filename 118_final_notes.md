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



