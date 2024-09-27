# Notes Friday 27, 2024

## Protocols

- OSI-7 is the overall flow
- Understand TCP and UDP and what the transport layer is for
- IP is big for network Layer


## Flight analogy OSI-7

- Physical layer is the base, every other layer isn't physical

- Purpose of trip is application layer

- Transportation layer guarantees that you will arrive to your destination safely and in an orderly manner

- *Network layer* is focused on starting dest. and final dest.

- *Data link layer* is focused on immediate flights (routing from two adjacent nodes) *Localized*

- *Transport layer* answers 'how' (how will data get from source to dest and what headers/permissions do you have)
  - Without transport layer, we have no idea how to get from source to dest. (what path to take, etc.)


## TCP vs UDP

- TCP is focused on reliability and connection

- UDP is focused on speed (we care more about speed, how fast can we transfer data from source to dest.)

- TCP begins with a 3-way handshake, then we can send data, attach sequence number, receiver could acknowledge the data received and also send some data, etc.

- TCP retransmits packages immediately after it gets an acknowledgement from the receiver that a packet is lost or corrupted

- UDP has no handshake and no acknowledgement from receiver


## Rules

- Router works at network layer (it can only see and modify data as specified by the IP header)
