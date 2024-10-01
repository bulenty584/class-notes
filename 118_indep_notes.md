# Layering Notes

Layering in software is the combination of a hierarchy of software and hardware layers

It abstracts the middle btwn raw hardware and the user

*Each layer improves upon the services of the next layer below* to offer a better server to the next layer up

## From hats to networking

- Post office resembles TCP protocol

- Physical carrier use actual phyiscal technology to actually carry packages (packets) based on characteristics of technology

- Layers in analogy: Hats, Import-Export, Post Office, Carrier Logistics, Carrier Technology

- Layers are *distributed* --> people at each layer are distributed at diff. locations and must communicate with each other

- Bigwig locations resemble source and dest.


### Transferring Email Using Internet

- *TCP* ships data reliably btwn computers on the Internet on behalf of some application protocols
  - Breaks down data into smaller packets to be shipped faster to the destination
  - Also keeps track of segments that have been delivered, retransmitting missing segments if it needs to
  
- *TCP* relies on packet-switching abilities of the IP.

- *IP* interface is simple: Any segment that needs to be sent from TCP source is labeled with the destination IP address
  - Biggest IP value-add is to compute a route from source to dest. and to update that route in case of failures
  - Once route is chosen, packet is forwarded from router to router en route
  
- *Router* is just a computer with attachments to multiple links that acts like an automated post office

- *Data link*: The physical channel that can bridge the distance between two adjacent routers on the chosen path

- Layers in Internet Structure are Application Program, Transport(TCP), Routing(IP), Data Link(Ethernet) and Physical(thin wire ethernet or RF satellite channels)

- Layers are distributed, which means the software (or hardware) implementing each layer must communicate with each other to synchronize transfers

- For security, most services provide some encryption of packets in a security layer btwn application and TCP
