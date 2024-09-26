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
