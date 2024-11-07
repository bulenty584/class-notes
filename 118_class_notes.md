# Lecture 1 - Thursday (9/22/24)

## Big Idea: Packet Switching

  - Reasons for packet switching
    - If one page is lost, we can still keep overall package
    - more resilient and reliable
    
## Hat Transfer Analogy

  - Think of layers horizontally (e.g. 2 TCPS form TCP layer)
  
## Anatomy of a Web Transfer

  - *Forwarding*: routers forward packets based on looking up dest. addresses in a forwarding table. 
  - *Routing*: Routers work together to build a forwarding table(OSPF), BGP
  
### What Happens in a Web Transfer

  - Sender --> Internet --> Receiver
  - browser initiates a TCP connection to CNN.com (Since it's a name, we translate it to IP address)
  - TCP initializes all numbers 
  
## Layering More Formally

  - We call it layering because each layer uses the layer below it to provide functionality
  - Layering in a network resembles regular layering except each layer is there in both server and client 
    - Communicate through Headers passing through router
    - When it moves through layers it will also strip layers away
    - *in-band*: Everything is in the packet!
    - IP ~ Post Office
    - TCP ~ transferring hats
    
  - Physical layer sends bits at a time (1 bit)
    - Convert bits into energy
  - Physical -> data link -> IP -> TCP
  - Bits -> frames -> packets
  - *SDU* is the actual data you pass (data depends on the layer)
  - *PDU* are the messages that are exchanged between peer entities.

### Headers

  - We have two headers, with one changing with data link layer
  - Before routing link, we removed the data link layer
  - Data link header keeps changing as you traverse the internet
    - Not so much about privacy
    
## Layers is Modular Design

  - Strict layering (I can only worry about the layer below me, my own API, and my own header)
  - Layers can change without disturbing other layers
  - *Protocol*: Interface among peers in a layer
  
## Key Design Decision in IP

  - Don't redo things in lower layers when you can do them correctly in higher layers

  - *TCP's abstraction is just two shared queues (shared memory, one writes from queue one reads from queue)*


# Lecture 2: Intro to the Physical Layer

- Worksheet solutions
  - You start with a bit at the IP layer, it goes all the way to the destination to TCP, and you take a second bit in the TCP header that gets reflected back in the acknowledgement
  

## The Foundation Sending Bits
  - Three step process
    - Take an input stream of bits(Digital) --> Modulate(Send louder frequency signal to reflect 1 and softer to reflect 0) it to travel over physical media (Analog) and demodulate it at the other end (Digital)
  
## What Does the Physical Layer do?

The physical layer is a possibly faulty, single-hop, bit pipe that connects a sender to multiple receivers

## Physical Layer: Sublayers

- We take an input stream, code it, take that coded stream and pass it through *media transmission* to generate an input signal(often square, not curved since perfect)
- Then the above passes through *signal transmission* to generate our output signal which passes through *media reception* which generates a coded stream that is decoded into the bits again

## Understanding the sublayers

- *Top sublayer*: how senders and receivers synchronize to sample analog signals to bits

- *Middle sublayer*: Converting above to media

- *Bottom sublayer*: Defines essential properties of the media (limits, etc.)

## Sending Bits to a receiver questions

- How do we predict output of energu on channel? Fourier analysis

- How does distortion affect maximum bit rate? Nyquist(sluggishness) and Shannon(noise) limits

## Fourier Analysis

- Big picture: we rewrite a signal <i>S</i> as a sum of sine waves with different frequencies
- Use the amplitude and phase response to see the effect of each sine wave and add the scaled sine waves to find the output signal

- *Bandwidth*: How *fast* is my cable modem in bits/s?

## Sluggishness and Noise

Most channels are sluggish (take time to respond) since they turn a *deaf ear to higher frequencies* in the input signal. Thus, *lower bandwidth* channels are more sluggish.

## Sampling Bits

Receivers recover bits in the input signal by sampling the output signal close to the middle of bit periods
  - two limits to bit rate:
    - Channel bandwidth (Nyquist)
    - Noise (Shannon)
    
## Nyquist Limit

- Why how fast you can send (CS bandwidth) depends on the range of frequencies (EE bandwidth)

## Intersymbol Interference

- bits around others can influence how the other bits are read leading to false values (energy of the second bit interferes with the first bit, causing the first bit to look like something else

## How fast could we send without InterSymbol Interfence

- Nyquist noticed that sending every *T/2* also works because the peaks line up with the past zeros
- We can get the Max bit rate to be 2B! (2*1/T = 2B) 1/T = B (Bandwidth)

## Shannon Limit

- Nyquist rate is the max rate of sending symbols not bits (baud rate)
- ISI(Inter-symbol interference) when energy spills over to other bits

- log(1 + S/2N) * B is a bit different from naive bound log(S/2N) * 2B since our sample model was only for a simple coding and for fixed deterministic frequencies

## Top Sublayer

- How do we know when to sample bits?

### Who needs a clock?

- We need to wake up the receiver (send *initial training bits*)

- We need to code to make sure we add transitions in between bits in our signals

### Asynchronous coding

- Codes a character (5-7) bits at a time (ASCII with Parity bit)
- Characters are framed using a start bit and two stop bits
  - 1 is encoded as low voltage
  - 0 is encoded as high voltage
- first bit is always a rise and the last bit is always a fall
- Start bit (5-8 data bits + parity) and then 1-2 stop bits




# Lecture Notes Oct 15, 2024

## Initializing link protocols

HTLC sends a restart message (the receiver sets its number to 0), back and forth

## How naive restarts fail

We can prove that there is no reliable init. protocol if we assume no non-volatile memory that survives crashes, the protocol is deterministic, and message can stay on wire indef.

How can we fix this? **Change assumptions**

**END OF DATALINK RECOVERY**

## Local Area Networks, Ethernet and 802.11

### Why Lans?

Cost: Connect up all computers in a building, saves writing costs to share one wire

Bandwidth: Provides high bandwidth and low error rates for local group of users. Worth is because most high bandwidth distr. locally has acess locality

Statistical Multiplexing: Time division multiplexing not a good idea when user traffic is bursty (high peak / average ratio)

Xerox machine analogy: Just show up to use Xerox machine! and sort out collisions
  - better latency and throuput in common case: what ethernet does
  
TDM vs SM:
    We have more users sharing the bandwidth (B/N) where N is number of users but for SM we have (B/X) where X is the number of busy users!
    

## Aloha

White frames conflict with black frames

Every island had a clock and every island had to start transmitting at a multip[<35;8;21Mle of T (differnet multiple)

CSMA: Listen before you transmit

CD: While you are transmitting you look for a collision
  - detect collision while you are transmitting
  - stop and start again

# Lecture Notes Oct. 17, 2024

MAC Address -> anytime you have an ethernet connection, you have a MAC address (two for each router, one at each endpoint)

Multicast address -> an address that you can send to mult. people

## LAN

Local area network (LAN) is like a shared wire with multiple senders and multiple receivers

**Bridges**: All we need are a destination and source address


# Lecture Notes 10/22/24

Bridging Review ==> Addresses A, B, C in datalink header are MAC addresses

Basic Ideas are so simple

All routers are just MAC addresses to Bridges (each Bridge sees ethernet). 

From router pov: bridges are invisible

Why have routers? Data link headers were dev. before bridges! People built headers in order to support routers


Why are bridges bad: 

- 802 addresses are flat. Routing addresses hierarchical. Bridges have to learn all addresses in an extended LAN

MAC addresses are flat and unique, IP addresses are hierarchical


Routers connect extended LANs to form a routing network

Bridges can be used to construct a small number of compatible LANs to form an extended LAN.

Most routers today are multiport


**IP ADDRESSING AND FORWARDING**

When you send to a domain name like cs.Berkeley.edu, a resolver is your host translates the name to a 32bit IP address. ALl messages carry IP destinations addresses. 

They used to have ONLY Class A addresses, then moved to class B, class C


OLD IP FORWARDING

Algo:

- Find destination: Extract Nextwork number of dest. by parsing and checking for class A, class B

-Final Hop reached? If (network number of dest = network number of one of the routers local interfaces) deliver packet. Map to local address using ARP or some such network specific protocol

- Lookup Router Table: Lookup Network Number in the corresponding routing table, if it exists, deliver packet

NEW IP FORWARDING

Prefix table has entries that define prefix number

In real time as packets are incoming, we have to determine where each prefix goes. 

What the last hop has to do?

Four problems the Endnodes MUST solve

P1: Routers need Data Link addresses of endnodes
P2: Endnodes need DL address of 1 router
P3: E1 and E2 should be able to communicate without a router
P4: E1 to E3 traffic should go through R2


IP Addresses to End-Node problems:

P1: ARP for MAC address of destination
P2: a service called DHCP that gives you the IP address of one router
P3: Need to understand how to implement ACLs using simple linear search


# Lecture Notes 10/29/2024: Route Comparison

MAC address comes built into laptop, which is used to talk to DHCP server to get routing number, and assigns you an IP address.

DNS server: provides the source IP address
  - browser has a resolver that has a local DNS agent (locally) (name -> address)

ARP protocol: changes route address to MAC address on every hop!

Router also ARPs

**Question Route Comparison Answers: Who builds the forwarding table in the router??**

## Part 1: Routing Within Organizations

Four Parts in Routing: 
  - **Set up addresses and topology**: assign IP addresses, connect routers
  - **Neighbor determination**: Endnodes talk to routers (ARP), Roter to router neighbors
  - **Compute Routes**: most complex 
  - **Forward packets**: Ships off forwarding table (packets)
  
Two ways of constructing Routes:

**Link State**: Global view of Link state to everyone!
**Distance Vector**: We know if someone keeps neighbors and who they are, we can determine how far away a specific node is
- Routers gossip with neighbors but does badly with node failures

### Distance Vectors

Everybody locally is getting gossip from their neighbors (periodically sending gossip vectors)

As in spanning tree we have port and central databases

Central is computed based on best port database

You store all of your neighbors even if they aren't the most cost-effective! (Good for when a link fails)

In distance vector, everybody sends predictions to every router


In Link State: every router sends its cost to all neighbors


# Lecture 118 Computing Routes

What if we want to move to different place (CMU -> UCLA)?

**Answer:** Autonomous Systems (AS)

**BGP: routing btwn ASs**:

- Does not hold a distance, holds a list of ASs

# Lecture Notes Tuesday November 5, 2024

What does BGP do?

Choose btwn routes based on attributes and local network policy

## BGP is suboptimal

- we rely on local knowledge only:
  - neighbors best routes may not be your best
  
## Three Topics in Naming

- How to get an IP address to get started (DHCP)
- How to map from user-friendly names like ccle.ucla.edu to an IP address to send (DNS)
- How to build a large private network with only 1 assigned to public IP address: magic. No (NAT)

## Mapping btwn Identifiers

DNS: Given hostname, provide IP address; given IP address, provide hostname
ARP: Given IP address, provide MAC address; To enable communication within LAN
DHCP: Automates host boot-up process; Given MAC address, assign unique IP address; also tells host other stuff about the Local Area Network


