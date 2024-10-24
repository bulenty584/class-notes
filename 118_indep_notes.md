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

# Physical Layer Notes

## What is the physical layer?

The physical layer is a bit pipe that transfers bits from sender to multiple receivers.

The key issues associated with using Morse Code to send bits:

- **Fundamental Limits to transmission**

  - ISI! The receiver gets confused if the sender sends bits at a super fast rate (noise from other reflections can affect the decoding)

- **Technical Aspects of the Medium**
  
  - Sender could use flashlight to send a bit (turning on and off)
  - Technical aspects of medium do matter! (flashlight battery time, ability to see semaphores at night)

- **Encoding and Decoding Information**

  - Encoding in Morse Code is not that problematic
  - Decoding is trickier: what if the receiver thinks the sender is going too fast? The receiver must learn at what rate the sender is sending to *clock recover*
  - Clock recovery scheme can be simple if receiver and sender have agreed on rate and they both have accurate stopwatches

## 2.0 Physical Layer Sublayers

The physical layer is divided into three sublayers:

- **Transmission Sublayer**: Bottom sublayer describes the essential properties of the media(e.g. frequency response and bit error rate) that influence and limit transmission rates

- **Media Dependent Sublayer**: middle sublayer describes properties of particular media (satellites, coaxial cable, fiber)

- **Coding and Decoding Layer**: Top sublayer

  - How info from higher layers is encoded and decoded
  - To help the receiver, the sender adds some extra bits to its input stream to help the receiver get into and stay in sync
  - *Layers can be studied and combined independently*

## 3.0 Transmission Sublayer

The goal of physical layer is to send symbols from sender to receiver

The most common way to do the above is by sending energy (light, electricity) over a channel (fiber, cable)

We will focus on On-off coding: send a 0 by sending no energy and we code a 1 by sending energy down the channel

The problem with real-life mediums is that real channels **distort energy signals**

Immediate question is how does distortion affect maximum bit rate??:

- inherent inertia of the channel affects maximum signaling rate (Nyquist limit) and inertia plus noise affects max. bit rate(Shannon limit)

### 3.1 What we mean Bandwidth at the Physical Layer

Signal is something that carries energy that varies with time

Channel is the physical medium that conveys energy from sender to a receiver

The *bandwidth* of a channel is the width of its pass band

Most real channels have less clearly defined band region and one has to define the band in an arbitrary way

Most real channels will not pass through frequencies past a cutoff point (if they do, the output will be super distorted)

Most channels are sluggish because they turn a deaf ear to higher frequencies in the input signal

Therefore lower bandwith channels are more sluggish since any high frequency signal will get distorted

What about Noise??

Simple, common model is white or thermal noise (we assume noise is uniformly distr. at all frequencies and that its amplitude is normally dist. within a frequency

### 3.2 Nyquist Limit: How fast can we send symbols because of bandwidth limits

**Key Idea**: if we send a signal that has higher frequencies than the channel can pass, output is distorted

Also, if we transmit bits at a rate that goes over the channel bandwidth, then the output will also be distorted and receiver won't be able to recover bits

Receivers sample at periodic points and decide what the bit is based on a threshold (close to middle of bit period)

**Nyquist Limit**: We cannot send symbols faster than a rate of 2B per second (if channel bandwidth is B) without causing ISI

### 3.3 Shannon Limit: How fast can we send bits due to bandwidth *and* noise

If we allow L levels, we can have logL bits per pulse

*symbol*: refers to an individual pulse of energy

*signalling rate/baud rate*: rate of sending pulses

- Bit rate is the baud rate * # bits / symbol

levels refers to amplitudes (we can send 2 bits per pulse if we divide levels, log2(L) where L is levels)

Can't we send as high a bit rate as we want by dividing each pulse into as many levels??

- No! All real channels have noise that prevent a signal from being divided into too many levels (noise could cause one level to be confused w/ another)

If we have a max. signal ampliture of S and a max. noise amplitude of N, we cannot be safe unless levels are separated by at least 2N.

We can transmit as most log(S/2N) bits per symbol

Combining with Nyquist limit, we cannot send faster than 2B*log(S/2N) bits per second

## 4.0 Clock Recovery Sublayer

*clock recovery problem* is concerned with having the receiver dynamically adjust its receiver clock in order to track - as closely as it can - the middle bit instants of the sender

Consists of two tasks: 

- Getting in phase (figuring out when to sample first bit)

- Staying in phase (keep sucessive sampling instants synchronized)

We must assume that the receiver roughly knows the clock period of the sender by some arrangement

**To solve the first task**:

- sender generally sends a well-defined sequence of trailing bits before it sends its data bit stream

- trailing bits get the receiver in phase

**To solve the second task**:

- either we rely on accuracy of receiver clock (and limit # bits sent to small value) or ensure data always has *transitions*

*Transitions* are changes in signal amplitudes (0 to 1) that provide cues that help the receiver stay in sync after getting in phase, even over a long stream of consec. bits

Think of receiver clock as a stopwatch that can be started or restarted based on transitions

**KEY DIFFERENCE**:

- real data bits do not provide training bits(preamble or start bits)or even guarantee transitions

- Top sublayer at physical sublayer is a coding sublayer that encodes raw data bits fed to it by Data Link layer and codes it to add training bits and transitions

- *Frame*: result of Physical layer will be handed some sequence of bits to transmit, these bits are encoded with some preamble or possibly some code to force transitions 

- *Frame* is the raw data with some preamble or forced transitions encoded into it

### 4.1: Asynchronous Coding

Sender's physical layer is given a character of data to transmit

Data character can be 5-8 bits and may also include parity bit

Parity bit is used to detect if data has been corrupted during transmission

The coding has the following rules:

- low amplitudes are used to encode a 1 and high amplitudes encode a 0
- we add a parity bit to each character and then "frame" the character with an extra start bit and 1-2 stop bits
- start bit is a 0 and stop bit is 1
- **regardless of value of data character, first bit sent is a 0 and last bit is 1**

The times between sending of characters can be arbitrary and therefore this is called *asynchronous*

**Key Concept**: Time between bits is NOT arbitrary but is controlled by the sender clock. The time between characters IS arbitrary

Summary:

- Receiver and sender don't share continuous clock, but they need to operate at simply the same **baud rate**
- Receiver uses start bit of a character to align itself with incoming data stream and begins to sample until the stop bit(s) at expected intervals

- asynchronous communication means characters don't have to be sent back to back but there can be gaps btwn them

- if there is a gap btwn characters, the line amplitude is low (encoded as 1)

The second problem (staying in phase) is solved by brute force:

- we assume sender and receiver clocks are pretty close
- since we only have 10-11 bits in a frame, even if receiver clock drifts, the receiver sampling points cannot drift too much by end of a frame
- **pseudocode analysis**:
  - we start our time for every 1/2 bit
  - for each possible bit (0-10) 10:
  - we wait for the timer to expire and then sample signal
  - we start the timer for one bit to get the next 1/2 bit
  - once we do this, we make sure our start and stop bits are encoded properly and we extract the middle data


### 4.2 Synchronous Coding

FRAME INCLUDES MULTIPLE CHARACTERS OR BITS

In asynchronous coding, receiver gets locked in phase when the voltage goes from low to high (start bit)

For this to be reliable, we need to have a large idle time btwn characters for the receiver to get locked in phase which slows down transmission and limits it to low rates (9600 bits per second)
 
Two overheads:
- adding start bit and stop bit for every 8 bits of data
- extra time needed for reliable detection and starting up receiver clock for each character

*Synchronous coding* attacks the above problems by using a frame size that is normally MUCH larger than a character!

- overhead of preamble and postamble is gradually decreased over a huge amount of bits
- phase info learnt from preamble is used to clock remaining bits in frame as well
- inter-frame time needed for reliable phase detection is paid ONCE over a huge group of bits

One problem is if we make the frame size larger, we cannot use the brute force approach of relying on the bounded inaccuracy btwn the sender and the receiver to *stay in phase*

**Types of Synchronous Coding**:

Like asynch. coding, we can represent a 1 with one voltage and 0 with another (NRZ (non-return to zero) coding)

We can always also prefix a frame of data by an alternating string of 1s and 0s to get into phse, but the main problem is if we have a long string of 1s or 0s will have no transitions

More Popular scheme is Manchester Encoding:

0 is encoded as -1.5V for half a bit follows by 1.5V for the remaining half bit

1 is encoded as 1.5V for half a bit then -1.5V (FLIPPED)

We are essentially sending two coded bits for every real bit transmitted (transmission efficiency is poor)

**HUGE ADVANTAGE** is that Manchester is *self-clocking* --> Every bit regardless of its value provides a transition that can be used to sample the bit value

If we knew where approx. where the half bit period was, our decoding algo could be: *wait for a transition at roughly the mid bit. Then start a timer for a quarter bit after that. If the value is above some threshold, its a 0, otherwise its a 1*


We can compare different types of codes based on:

*Ability to guarantee transitions*: Most important
*Transmission Efficiency*: Ratio of real to transmitted bits
*Signal to noise ratio*: Given same max. and min. transmission levels, the amount of noise required to render a received signal ambiguous
*Implementation Complexity*: Qualitative

### 4.3 Broadband Coding

*baseband* coding: coding using energy levels (voltage or light)

*broadband* coding: information is *modulated* on a carrier wave of a certain frequency

In *frequency shift keying (FSK)*, we let a high frequency encode a 0 and a low one encode a 1

In *amplitude shift keying*, we change the amplitude of the sine wave to encode either a 1 or a 0

## 5.0: Media Dependent Sublayer: Types of Media

### 5.1: Media Affects Protocols

Examples of how media affects protocol design:

**Bandwidth and Message Formats**: Earliest networks used existing phone lines and were limited to low bandwidth voice links so they would send fewer messages

With fiber, this is less of an issue

**Broadcast LANs and Broadcast**: Use of coaxial cable in Ethernet made broadcasting free essentially.


# Data Link

## 1 Abstracting services of the Physical Layer

The 3 sublayer model of the physical layer (coding(encoding, decoding), transmission, media)

We can abstract the internal details of the physical layer and consider the physical layer to be a bit pipe

Physical layer acts as a sort of pipe that connects sender and one or more (multiple receivers are common in a LAN like an Ethernet) receivers

Sender interface allows sender to send a sequence of bits:

- physical layer "bit pipe" delivers these bits to the receiver interfaces after an arbitrary delay

- Bits that are sent can be lost or corrupt, so physical layer abstractio is sort of like a lossy bit pipe that can lose or corrupt bits with some probability

- Two main kinds of errors: **random bit** errors (thermal noise) and **burst errors** that corrupt a group of bits (impulse noise)

## 2 Functions of the Data Link Layer

Data Link can be studied separately based on whether we are dealing with point-to-point(1 sender 1 receiver) or broadcast (multiple senders and multiple receivers)

For both point to point and broadcast, the first two sublayers ARE THE SAME

First major function of all links is to convert a stream of bits into units called *frames* using *framing*

**EACH FRAME IS A GROUP OF BITS WITH EXTRA BITS THAT ARE USED TO DELIMIT FRAMES AND EXTRA BITS USED FOR ERROR DETECTION**

Layers: 

**Point-Point(2 nodes sender receiver)**: Framing -> Error Detection -> Error Recovery(if we have errors)

**Broadcast Links(>= 2 nodes)**: Framing -> Error Detection -> Media Access -> Multiplexing

*Error detection* sublayer adds check bits to frames in order to detect corrupted frames with high probability. These frames are rejected at this level

For broadcast control layers, they have a traffic control problem (think of multiple intersections) --> We need a traffic control (Media access control) (MAC sublayer)

**ETHERNET AND TOKEN RING PROTOCOLS NEED A MAC LAYER**

  - Point-Point link with one sender and one receiver doesn't need media access because there is only one sender that can send whenever it wants to
  

**ERROR RECOVERY SUBLAYER**

Error detection detects errors in corrupted frames but error recovery actually takes action when errors are detected

A typical approach to error recovery is to have the receiver send acknowledgement (think of return receipt for certified mail sent through a post office) to the sender when it gets a frame successfully

If sendr doesn't receive an acknowledgement within a specified timeout, teh sender retransmits the frame

Multiple routing protocols may use data link: broadcast LANs typically allow this using a multiplexing sublayer (LLC sublayer)

**DATA LINK OFFERS 5 FUNCTIONS**

REQUIRED:
1. Framing
2. Error Detection
3. Media Access(only for broadcast links)

OPTIONAL:
4. multiplexing
5. error recovery

## 3 Data Link Operation

Framing and error detection main goal is to convert a semi-reliable bit pipe into quasi-reliable frame pipe

**HOW THE DATA LINK OPERATES**

It accepts packets from its upper layer (network layer) then adds data link header info to a packet to form a frame

The frame are sent to the receiving data link bit by bit through the physical layer

The receiving data link will assemble the received stream into frames (by framing)

Receiving Data Link will also use information in the frame (checksums ex.) to decide whether to accept or reject a frame

Accepted frames are passed up by its receiving data link to its client layer (routing normally)

**ALL DATA LINKS DO ERROR DETECTION**

The sending data link adds extra bits to a frame called a *checksum*(ex. parity bit)

The receiving Data Link examines the received checksum to decide whether the bits in a frame were received in error (if it was, frame is dropped)

If a receiver only does error detection, there is a finite probability that some frames will be lost

## 4 Why Error Recovery is Sometimes a Good Idea

**End-to-end Argument**: typical exchange of packets must be sent by the network across multiple hops therefore a packet will traverse several Data Links and several nodes.

**The only worthwhile reliability guarantees are end-to-end guarantees**
  - e.g. btwn transport protocols at the two endpoints that are communicating
  
It might be worthwhile to do hop-by-hop error recovery and detection at each Data Link on the path, but this is only a performance optimization

For correctness, we must rely on end-to-end recovery

Why do we need this??

**End-to-end Recovery is needed for several reasons!**:

1. Each data link may successfully deliver the packet to intermediate routers but the intermediate routers may drop the packet

2. The intermediate Data Links may crash in the middle of a packet transfer and the packet can be lost.

3. Transport layer must work over both unreliable and reliable data links

The transport layer must send end-to-end acknowledgements anyway for reliability

Without data link recovery, for every frame lost on a single link, a frame must be retransmitted by all the links by the sending transport

It takes longer to recover from a lost frame because the sending transport must wait for a longer period for an ack from the destination because the delay over n hops is larger than the delay over a single hop

**With data link recovery at every hop, a lost frame causes only a *single* retransmission at every hop and the retransmission is normally quicker**

### KEY POINTS ABOUT PERFORMANCE

IF the physical links have very low bit error rates, then the Data Link overhead can actually decrease performance

Part of the physical layer bandwidth would be wasted due to acknowledgements.

Sending Data Links also have to buffer frames for possible retransmission, which adds complexity and slows down the Data Link processing.

**On telephone links with very poor Bit error rates, it's probably a good idea to run a reliabble Data Link protocol like HDLC, but on Fibre links or local area networks that have good bit error rates, you should probably use unreliable Data Links (no error recovery) like ATM, Frame Relay, and Ethernet**

With extremely high error rates it pays to use hop-by-hop while with extremely low error rates it pays to not do hop-by-hop

## 5 Quasi-Reliable Frame Pipes

Definition of a Quasi-Reliable frame pipe:

- Probability of receiving Data Link passing up an incorrect frame to the client layer should be very very small. This is the *unknown error probability*; a possible goal for a system is one undetected error every 20 years. We need good checksums that can detect almost all corrupted frames

- Probability of a receiving Data Link dropping frames sent by the sender should be reasonably small to allow good performance. This is the *frame loss probability*: a typical goal for fibre optic link would be one frame loss everyday

End-to-end checksums are often not performed for performance reasons, so it is good engineering practice to require that the probability of undetected errors on Data Link be low.

## 6 Why Framing

Two great reasons for Framing:

- If the data link layer offers a bit pipe service, then it is impossible for the data link to "time-share" or multiplex its services among multiple clients
  - Many workstations run two routing protocols, OSI and IP. Yet two files sent using these two different routing protocols can be simultaneously in transit on the same ethernet
  
- Frames offer a small, manageable unit for error recovery and detection. 
  - E.g. it would be bad to retransmit a large file because of a single bit error; with frames, we need only retransmit the frame
  
## 7 How Framing

Any framing algo must allow variable length frames, idle time btwn frames (sender shouldn't send continuously) and must not depend on assumptions about client behavior. Framing overhead should also be low

Three techniques for Framing:

- **Flags and Bit Stuffing**: Use special bit patterns or flags at start and end of frames

    - To prevent the possibility of confusion due to user data that contains the flag patterns we use *bit stuffing*. 
    - We add bits to user data whenever to prevent the flags from occuring in data
      - HDLC uses a flag of 01111110
      - **HDLC bit stuffing rule**:
        - after any sequence of 5 1's in the user data, add a 0
        
      - At the receiving end the user data must be destuffed: after any 5 1's in the data, the next 0 is removed
      

Explaining the algo using sublayering:
  - **stuffing layer** first converts user data into data bits that do not contain flags
  - **framing layer** then adds flags at eitehr end and gives the resulting frame to the physical layer for tranmission bit by bit
  - At the receiver, the *physical layer* passes the bits to the *deframing layer* that assembles frames based on flags and removes the flags
  - Finally frame is passed to the destuffing layer that 'decodes' by removing any stuffed 0's

### Inventing variants of the stuffing rule
  
  We can invent many variants of the stuffing rule!
  - We want to ensure that the flag does not occur in the encoded data
  
  - We must first argue that a flag cannot occur btwn stuffed bits. This is pretty easy since if it did, there would have been an extra stuffed bit added. 
  
  - More tricky part of the argument is to show that the stuffed bit cannot be a part of a flag (i.e. arguing that a flag cannot occur across a stuffed bit boundary)
  
  - besides proving that a flag doesn't occur in the data bits we also need to show that a fake flag cannot be formed by the last few data bits and the first few bits of the real final flag
  
  - to finish the proof we need to show that if any suffix of a flag is also a prefix of the flag, then we cannot add data bits to the suffix to form a false flag
  

### Start Flags and Character Count

Use flags to indicate the start of a frame and then a length field at the start of frame to indicate how many bits to the end of the frame. We do not need bit stuffing

### Start and End Flags supplied to Physical Layer:

Suppose the physical layer also has the ability to send a third symbol "F"

## 8 Principles

- **Each layer or sublayer exacts its penalty**: Layering paradigm has overhead concerns. There is often a cost to layering

- **The end-to-end argument**: The idea of having control checks (reliability guarantees) at the two endpoints of our system. We could add hop-to-hop guarantees, but it is only a performance optimization

- **Lower Layers should not depend for correctness on assumptions about how Higher Layers work**:
Framing algorithms should never assume that user data will ever contain some sequence of bits

- **All layers have some common problems to solve**:
Most layers have to address problems of synchronization (bit recovery, frame recovery) and multiplexing (how can multiple clients share the service, e.g., Time Division Multiplexing at the physical layer, Protocol Fields at the Data Link Layer), and addressing.

- **Best principles should be violated for pragmatic reasons**:
When transferring a file, end-to-end argument implies that we should add end-to-end checksums to guarantee the end-to-end integrity of the data and not rely on the hop-by-hop data integrity provided by data links

Since TCP checkums increase processing time significantly, this option is often not used(Transport level checksum)

This increases the responsibility of Data Links to provide good per hop integrity (probability of undetected errors should be extremely low). Result, though, is a violation of the end-to-end agreement

- **Layering and Sublayering are a Good way to Solve Protocol Problems**:
Layering is a tool for protocol design. It is a generalization of divide and conquer used in algorithm design

- **Good systems thinking can sometimes lead to simple solutions to hard problems**:
  - Most real systems consist of a bunch of interacting pieces that are hard
  - avoiding spurious flags is easy if we don't use 0 and 1
  
  
# Error Detection in the Data Link Layer

Error detection can only occur after framing has occured since checksums are attached to frames - error detection is layered *above* framing in the sublayer model

## 1 Why Error Detection

Main goal is to make probability of a receiving Data Link passing up an incorrect frame to the client super small (*undetected error probability*)
  - Why? Because most systems ignore the end-to-end principle since calculating checksums inhibit performance (therefore we must make sure probability of undetected errors in Data Link is low)
  
Another reason is intermediary routers may make decisions based on bogus data and misdirected packets

## 2 Kinds of Errors

Two main types of errors: **Intersymbol Interference**(energy from previous bit interferes with how the next bit is interpreted) and **noise**(changes a 0 level to 1 level)

Burst errors are errors that are highly correlated: if one bit has an error, it's likely that the adjacent bits could also be corrupted. Burst error of size *k* means that the distance in bits from the first to the last error in the frame is at most *k-1*. The intermediate bits may or may not be corrupted

**Example of Burst error**:
  - Suppose we have a burst error of size 5 that starts in bit pos. 50. Then we know for sure that bits 50 and 54 are corrupted but 51-53 may or may not be corrupted
  
  - Burst errors tend to be more localized but allow for a larger number of actual bit errors
  - Bit Errors tend to be more localized but allow for a larger number of actual bit errors (bit errors can be spread out arbitrarily but can be smaller)
  
  **An ideal error detection code should be able to detect large localized burst errors and also be able to detect as many random bit errors as possible**
  
## 3 Parity Bits

MAIN IDEA IS TO USE REDUNDANCY TO DETECT ERRORS IN A LARGE SEQUENCE OF DATA

A cheap solution is to add a single checksum bit that represents the parity ("even"-arity) of the data: 
  - **The extra parity bit is set to 1 if the number of 1's in the data bits is odd, and 0 otherwise**
  - **Rule for calculating parity is to take the exclusive XOR of all the data bits (1 iff the two bits are not the same)**
  
## 4 CRCs

Most networks do not use error correcting codes because they are expensive. They can only correct a few bits of errors and aren't much help with burst errors

Instead of increase the number of bits transmitted with each packet, network applications prefer to detect errors at the receiver and have the sender retransmit the correct bits

Error detection for us is done using checksums

Checksums are pretty similar to hash functions(a function f that takes two random strings a and b and generates two different outputs with high probability)

Consider checksums to be a hash function for the data. We start with some valid codeword C and we use f(C) as the checksum for C. If errors corupt C to a random other string C, we want (with very high probability) that f(C) != f(C) so we can detect an error!

CRCs are a method for developing these hashes!

### 4.1 Ordinary Division Checksum

An hashing algorithm that uses ordinary division to generate a checksum:

- Consider message M and checksum generator G to be binary Ints

- Let r be the number of bits in G. We find the remainder of t of Y = 2^r*M when divided by G. If we do M divided by G, we can easily separate checksum from message at receiver by looking at the last r bits

- 2^r*M = k.G + t. Thus, 2^rM + G - t = (k+1)G. We add checksum c = G - t to the shifted message and the result should divide by G. 

CRCs are essentially the remainder when doing Modulo 2 arithmetic

### 4.2 Mod 2 Arithmetic and division

Mod-2 Arithmetic has following properties:

1. No carries because both addition and subtraction are EXCLUSIVE-OR. Repeated addition does not result in mult. 

2. Mult. is normal except for no carries: 1001 * 11 = 10010+1001 = 11011. Multiplication by a power of two corresponds to a shift (as usual) but addition is EX-OR. Therefore we use shift and Ex-or instead of shift and add

3. Division uses similar algo. 

Division in Mod 2 is very iterative. We store the current remainder of the bits looked at so far, shifting in the next bit, and then subtracting G from the result to leave a number less than G. We then iterate this process till all bits have been shifted in.

Division in Mod2 arithmetic is similar except for 2 differences. First, there is no subtraction anymore, only EX-OR. Second, to find a remainder, we want to reduce the current remainder after shifting in the new bit. The only way to reduce the value of a sequence of bits in this arithmetic is to remove the most significant bit (if it's a 1). Assuming the CRC divisor always has a 1 in its MSB, this is done by EX-ORing the CRC divisor with the current contents in case the MSB of the current contents is 1

### 4.3 CRCs - The Idea

Algo: 

- Let r be the number of bits in G. We find the remainder c of 2^r-1M when divided by G. We only shift r-1 bits this time since we are sure that the remainder will be only r-1 bits in this case
  
Ex. M = 110 and G = 111(deg 3) so 2^(r-1)* M = 11000

11000 XOR 111 (since MSB is 1, we XOR 110 w 111 to get 010. We can shift again to get 100 XOR 111 to finally get 011

- 2^r-1M - k.G + t, thus 2^r-1M + t = k.G

Ex. M = 11 and G = 101 --> 2^r-1M = 1100

### 4.4 CRC Properties and the Polynomial View

We can think of CRC computation as dividing a message polynomial (shifted by multiplying by x^(r-1) by a CRC divisor polynomial (the generator) and adding in the remainder. While this view is equivalent to our older view, this view is easier to analyze. 

A common CRC is CRC-16: x^16+x^15+x^2 + 1 which corresponds to a CRC generator string of 110000000000000101

CRCs like CRC-32 can detect 1,2,3 and all odd bit random errors

CRC-32 can detect all burst errors of size 32 or smaller and can detect any error with high probability. 

### Implementing CRCs

Software impl.done one bit at a time. 

Our remainder algo. consists of the following two steps that are iterated until all message bits are consumed: 

- Current remainder is held in a register (can hold r bits, where r is the number of bits in the divisor) which is initialized w/ the first r bits of the message.
  - If the MSB of the current remainder is 1, then EXOR the current remainder with the divisor bits; if the MSB is 0, do nothing. 
  - Shift the current remainder register 1 bit to the left and shift in the next message bit
  
A naive hardware implementation would mimic the above appraoch and use a shift register that shifts rbits one at a time. Each iteration requires 3 steps: checking the MSB, computing the Ex-or, and then shifting

**Ex-OR** only needs to be done ONLY if the MSB is 1; thus in the process of shifting left the MSB, we can feed back the MSB to the appropriate bits of the remainder register. The remaining bits are EXORed during their shift to the left. 

to gain speed, CRC implementations have to shift W bits at a time, for W > 1.

# Error Recovery in Data Link

Last two sublayers: Framing and error detection. 

Framing used to transform stream of bits into units called Frames

Error detection added checksums to these frames to detect whether any bits in a frame are corrupted

## 1 Why Error Recovery

Error recovery is an optimal sublayer of point-to-point links. 

## 2 What Must Error Recovery Guarantee??

Must guarantee that the packets for transmission to the sending data link must be delivered to the receiver without duplicates, loss, or misordering

Avoiding reordering and duplication can avoid extra work for the end-to-end transport protocol to reject dups and reorder the stream of packets

## 3 Assumptions

We can assume that Error recovery is done betwen a single sender and receiver that are connected by two point-point physical links in each direction. The error recovery sublayer is above the error detection sublayer

Assumptions:

- Undetected error rate (probability of a corrupted frame being passed by error detection) is small enough to be ignored

- Whole frames can be lost in a way that may not be detected by error detection (e.g. if all bits in a frame are lost)

- Physical layer is FIFO. If bit is sent before b', then if both bits are received, bit b is received before b'

- Delay on the physical links is arbitrary and can vary from packet-to-packet

If there is multiplexing going on, the delay may vary

Timers on most OSs are fairly inaccurate and the result is that one can't measure time precisely. 

## 4 Protocol Play

Sending Data Link sends the sequence of received packets as frames

Then, we have the receiver send back a special ACK frame for every data message it receives. If the sender doesn't get an ACT within a timeout period, the sender retransmits, which can cause duplication. If a is sent and received but the ACK is lost, then the sender will resend a and the receiver will output aa. 

We can try and detect duplicates by rejecting any frames whose data is the same as the previous frame. Could cause deadlock if data sent has same value in successive frames

We add a sequence number to each frame (sender starts with 0 and receiver starts w 0)
  - Each frame sent(or resent) by sender carries the current sender sequence number
  - The receiver only accepts frames that have the same sequence number as the receiver number
  - On a successful receipt, the receiver acepts the frame, increments its number and sends an ACK (on receipt of the ACK, the sender updates its number and sends the next packet)
  - We could get **deadlock** if the first ACK is lost; the sender will keep retransmitting but the receiver will not accept a new packet and send an ACK
  

The Sender should only accept ACKs with number greater than its own sequence number

We need sequence numbers to detect duplicates and misordering, retransmission for loss, and we need to send ACKS back even on duplicate data receipts, and ACKS must be numbered

## 6 Stop and Wait Example

Sender keeps sending until its received, so it will eventually get an ACK and go onto number n + 1

Since the physical channels are FIFO, when the receiver receives frame n, it can be sure that the sender has received a *n* numbered ack which must have flushed out the reverse link of all lower numbered acks. 

Also, the data frame numbered *n* must have flushed the forward link of all lower numbered frames

At the instant the receiver receives a data frame with number *n*, the entire system only contains number *n* (all lower numbers must have disappeared)

There are only 2 possible consecutive sequence numbers in any state.

In the sender and receiver protocols we only check if the two numbers are equal or unequal. 


**IF TWO NUMBERS BEING COMPARED ARE ALWAYS CONSECUTIVE NUMBERS, IT SUFFICES TO CHECK THEIR LEAST SIGNIFICANT BIT. SO, WE CAN REPLACE LARGE SEQUENCE NUMBER BY A SINGLE BIT THAT IS INCREMENTED MOD 2.** : Alternating bit protocol

To prove correctness of stop-and-wait, we can say that when the sender first reaches number *n*, there are no data frames numbered *n* in the forward link and no ACKS numbered n+1 in the reverse link. Our receiver is also at n. 

## 7 Invariants

The state of a node at any instant is simply the values of all node variables that are relevant to theh protocol

The state of Node S is the value of i, and the state of R is the value of j. 

The state of a link is the sequence of frames (assuming its FIFO) that have been sent on the link but not yet received

Think of tasks as a queue, where Sender inserts at rear of the queue, and receiver pops off at the head of the queue

**SOME GLOBAL STATES AER POSSIBLE WHILE SOME ARE NOT**

Invariants of a protocol describe the possible states of a protocol when it is working correctly.

You can prove invariants by induction!

Assume invariant is initially true (protocol initialization must guarantee this), then assume it is true in a state s and show it is true in any possible state that can follow *s*. 

Any such state transition must be the result of a protocol action, so we need only consider protocol actions

## 8 Band Invariant for Stop-and-Wait

When drawing global states, consider only the numbers in transit frames and acks

The more interesting case is when s = R N . In that case, if the
invariant is true in the previous state, the entire band must b e equal to s. Thus when the receiver
increments to r + 1 and sends an ack, we now create 2 bands. A smaller one starting at the receiver
with values equal to s + 1, and the rest of the circle, equal to s. We can argue similarly ab out all
other cases. Try to do so yourself for practice! (You can easily disp ose of many of the simple cases
by observing that removing a numb er or duplicating a numb er do es not a ect the invariant: thus
frame loss and frame sending do es not a ect the invariant.)

### 8.1 Getting the strongest invariant needed

In doing a proof you can only use the fact that all your listed invariants hold in the previous state

If you find that there is some case in which your proof fails, you may need to add another invariant to rule out the case that fails

## 9 Point of Invariant

If the invariant is true initially and every action preserves the invariant, assuming it was true before, it's true in all states

When the sender goes to number n+1, on receiving an ack with number n + 1, the invariant implies that the receiver is at n + 1, any acks in transit have number n + 1, and any data frames in transit have number n. 

## 10 Alternating Bit Protocol

Sender code: 


ender has a bit SN (for sender number) initially 0.
Sender repeats the following loop:
1) Accept a new packet from the higher layer if available and store it
in Buffer B.
2) Transmit a frame (SN, B)
3) If an error-free (ACK,R) frame is received and R is not equal to SN then
SN = R
Go to Step 1.
Otherwise if the previous condition does not occur with an arbitrary
timeout period, go to Step 2 after the timeout period.


Receiver Code: 

Receiver has a bit RN (for receiver number) initially 0.
Receiver does the following code:
When an error-free data frame (S, D) is received:
    If S = RN then
        Pass D to higher layer
        RN = RN + 1 mod 2
    Send (Ack, RN)
    
**USE OF A SINGLE BIT WORKS ONLY ON FIFO LINKS! TRANSPORT PROTOCOLS HAVE TO WORK OVER NON-FIFO NETWORKS AND CAN'T GET AWAY WITH ONLY A SINGLE BIT**

## 11 Retransmission Timers

retransmission timer values don't affect CORRECTNESS of stop-and-wait procedures, but they do affect PERFORMANCE (we could have unnecessary delays)

# Sliding Window Error Protocol (Error Recovery in Data Link)

These protocols offer much larger throughput than alternating bit or stop-and-wait protocols. 
## 1 Latency and Throughput

**Throughput**: Number of jobs completed per second
**Latency**: Measures time (worst-case) to complete a job

**Throughput is more important for busy systems and latency is more important for idle systems**

For networks, jobs are messages and the system is a network. The service stations respond in a series of hops

*Transmission rate*: Rate at which the physical layer sends bits
*Propogation delay*: The time it takes for a single bit that is sent to arrive at the receiver. It is limited by the speed of light to at least 3 usec/per km.

Throughput of a link can be made independent of its latency by pipelining, but it can never exceed the transmission rate. Propogation delay is always an unavoidable part of latency on a link

**Bandwidth is the range of frequencies that are passed through at physical layer**

**At Data link layer it is used to mean the link transmission rate**

**Round-trip delay**: This is the delay to send a frame from a sender to a receiver and to receive a reply frame from the receiver. It includes the time to transmit both frames and two propogation delays

## 2 Why Pipeline??

Stop and wait limits us to sending one frame every round-trip delay

This stop-and-wait problem is not just limited to the satellite link. It applies to all links **WHERE LINK TRANSMISSION RATE MULTIPLIED BY PROPOGATION DELAY IS LARGE COMPARED TO THE FRAME SIZE** (bandwidth-delay product)

## 3 Sliding Window Protocols

The sender can send a window of outstanding frames before getting any acknowledgements

The window size depends on the degree of pipelining

Consider a sliding window prot. with a window size of w. The sender maintains a single variable (lower window edge L) which represents the lowest sequence number that the sender has not received an ack for. The upper window edge is L + w - 1 (maximum sequence number it is allowed to send)

The receiver maintains a receive sequence number R that is the next number it expects to see

In sliding window, the sender keeps retransmitting **all frames** in its current window until it gets an ack (receipt of an ack numbered R acks all sequence numbers that are less than R)

Two variants of sliding window: 

**Go-back-N**: The receiver only accepts frames in order. If any frames get lost and they were supposed to come before, then a go-back-N receiver will discard any subsequent frame even if they arrived. 

It is only when frames arrive in order that the receiver will accept each frame

For high-speed transport protocols where most frames are lost due to congestion and the window sizes are large, selective reject is very desirable

**Selective reject can recover faster from errors as sender has only to retransmit frames**

Selective reject buffers packets until the other packets (sequence number < packets received) are received before sending all of out at once

## 5 Sliding Window Code

**Code for Go-back-n sliding window** (receiver can send acks whenever it wants), also assume that sender has a long sequence of data packets given to it by its client that it wants to send. The data packets are stored at the sender. Numb er the data packets from 0 onwards. We
will send the s-th data packet with sequence numb er s attached.

Sender code for Go-back N:
Assume all counters are large integers that never wrap.
The sender keeps a lower window L, initially 0.
Send (s,m) (sender sends or resends s-th data packet )
    The sender can send this frame if and only if:
        m corresponds to data packet number s given to sender by client AND
        L <= s <= L + w - 1 ( only transmit within current window )
Receive(r, Ack) ( sender absorbs acknowledgement )
    On receipt, sender changes state as follows:
        L := R
The receiver keeps an integer R which represents the next sequence number
it expects, initially 0.
Receive(s,m) (receiver gets a data frame )
    On receipt, receiver changes state as follows:
        If s = R then (next frame in sequence )
        R := s + 1
        deliver data m to receiver client.
        
Send(r, Ack) (* we an allow receiver to send an ack any time *)
r must be equal to receiver number R at point ack is sent
most implementations send an ack only when a data frame is received

We assume that any unacknowledged frame in current window is periodically
resent. In particular, the lowest frame in the current window must be
periodically sent to avoid deadlock.

**Code for Selective reject** (Assume sender keeps a table that records which numbers greater than L have been acked (suffices to keep a bitmap representing numbers from L to L + w - 1)

We also assume that the receiver has a similar table that stores both a bit(indicating receipt) and a pointer to the data if the frames been received

**In order to prevent the sender from doing useless retransmissions, the receiver needs to send an ack containing its current number R as well as a list of numbers greater than R that have ben received out of sequence at the receiver**

Sender code for selective-reject:
Assume all counters are large integers that never wrap.
The sender keeps a lower window L, initially 0 and a table that
indicates which numbers have been acked (this can be optimized to store
only a windows worth of such state).

Send (s,m) (* sender sends or resends s-th data packet
    The sender can send this frame if and only if:
        m corresponds to data packet number s given to sender by client AND
        L <= s <= L + w - 1 ( only transmit within current window ) AND
        s has not been acked.

Receive(R, List, Ack) ( sender absorbs acknowledgement )
    On receipt, sender changes state as follows:
        L = R
        Mark every number in List as being acked in table.

The receiver keeps an integer R which represents the next sequence number
it expects, initially 0. The receiver also keeps a table that, for
each sequence number, stores a bit indicating whether it has been received
and a pointer to the data, if any, being buffered. Once again, this table
can be optimized to reduce the amount of storage to be proportional to
a window size.

Receive(s,m) (receiver gets a data frame )
    On receipt, receiver changes state as follows:
        If s >= R then
            Store m in table at position s and set bit in position s
            While the bit at position R is not set do
                Deliver data at position R
                R = R + 1

Send(R, List, Ack) (we an allow receiver to send an ack any time )
    R must be equal to receiver number R at point ack is sent
    List consists of numbers greater than L that have been received.
    most implementations send an ack only when a data frame is received

We assume that any unacknowledged frame in current window is periodically
resent. In particular, the lowest frame in the current window must be periodically sent to avoid deadlock

## 6 Implementation Details

In go-back-N it is enough to have one outstanding timer. Timer is set to some multiple of the average rount-trip delay (calculated by seeing how long it takes for acks to arrive)

**Protocol will work properly if timer values are set wrong, it'll only cost performance**

**In Selective reject, we have to set a timer for every outstanding frame in order to retransmit any outstanding frame in the window**

## 7 Sequence Number Space for Sliding Window Protocols

### 7.1 Go-back-n Modulus

This is a strict generalization of stop-and-wait if we set the window size to 1

If we can get away with a sequence number space of 2 (1+1) in stop-and-wait, maybe we can get away with space of w+1.

**w+1** sufficient for go-back-n. 

This is because for a window size of w, we don't want looping around

### 7.2 Selective Reject Modulus

R-w <= s <= R + w - 1. The space we need is **2w numbers**

## 8 Flow Control

A problem we could potentially run into is the receiver running out of buffer space. 

In Sliding window protocols, the receiver has at least *w* buffers. If the receiver wants to dynamically adjust the window, it can add a field to its acks, indicating that it is willing to receive frames beyond R

## 9 Initializing Sliding Window Protocols

We need a way for the sender to reset the protocol after teh sender crashes and vice-versa

Preliminary Procedure:

The sender sends a Reset message and waits for an ack (RA); when
the receiver gets a Reset message it resets its sequence numb er. When the sender gets the RA, the
sender resets its sequence numb er and starts sending data items.

The problem is that an alternating series of crashes at the sender and receiver force each node to respond to messages sent by previous incarnations. The sender could send a data frame that is lost, but an ack from an earlier incarnation and fools the sender into thinking that it has arrived

### 9.2 Reliable Restarts: Fixing the problem

The problem can be fixed by changing any of the assumptions:

1. *Non-volatile memory*: If we have non-volatile memory after a crash, the sender can keep a crash-count on disk that is incremented after every crash. RESTART messages are labeled with this counter, and RESTART-ACKs are accepted only if they match the current crash counter

2. *Probabilistic Protocol*: Instead of using a crash counter, use a random number to label RESTART messages. This should succeed with high probability if the number of possible random numbers is much larger than the number of frames that can be stored in the links

3. *Assume a time bound*: Most real protocols can assume that all frames on the link will either be lost or delivered in some maximum time delay, say 2 minutes. This delay can be set conservatively. Then after a crash the sender must wait for this time before sending RESTART messages

## 10 What makes Protocols So Hard

Since links can lose messages, it is impossible for two nodes in a protocol to change state at the same time. One node must change state before the other. 

If a router changes over to a diff. route, there will be a period in which the other routers may be using the old route. One has to be prepared for periods of inconsistency and prevent damage during such periods. 

# LANs

**Multiaccess/broadcast links**: Every transmission can be heard by all other stations, and there are multiple nodes that can access the link

Two new important features: medium access and *multicast*

- multicast is a mroe refined form of broadcast where a frame is sent to a set of receivers instead of all receivers

Typically all receivers receive all transmissions, though. 

## 1 Why LANs

Cost! LAN attachements are significantly cheaper than installing routers

LANs connect up all computers in a specific place with 200-1000 users

Wide-Area Networks(WANs) vs LANs

- LANs typically offer higher bandwidth and lower error rates for the same degree of connectivity and cost (since area covered is smaller)

## 2 Statistical Multiplexing and LANs

*strict* multiplexing is any scheme like TDM or FDM where a user is given a fixed allocation *regardless* of whether the user has data to send or not

Strict multiplexing is not a good idea because user traffic is usually very *bursty*

Bursty means that traffic has a high peak/average ratio. For many hours a workstation may only transmit some piddling control trafic; then in a single second send a Mbit of data as part of a file transfer

For bursty traffic, strict division of available bandwidth into smaller peices for each user means each user is limited to very small piece of bandwidth. 

**IT PAYS IF BUSY USERS CAN GET ACCESS TO BANDWIDTH OF IDLE USERS**

This is *statistical multiplexing*: multiplexing scheme attempts to take advantage of traffic statistics according to which most users are rarely busy at the same time

Every source gets a bandwidth B/N, where N is the number of possible sources; statistical multiplexing attempts to give each user B/x, where x is the number of users that currently wish to use the syste, 

Statistical multiplexing improves both latency and throughput

The statistical multiplexing must be fair!:

- *centralized solution*: every user who wants to transmit sends a request to a resource manager. The resource manager keeps each user's requests in a separate queue, and gives the round-robin service to each busy user (it won't give another service opportunity to a user until it has given a service opportunity to all other busy users)

- For LANs, this provides a bottleneck, so LANs use *decentralized solutions* but they attempt to provide statistical multiplexing

## 3 Ethernet 

Three main mechanisms in Ethernet: 

1. Carrier sense
2. Collision detection
3. backoff / CSMA/CD

It takes time for both data signals and collisions to propogate along the Ethernet wire

### 3.1 Historical Precursors of Ethernet 

Slotted Aloha requires fixed size slots (making them too small would be inefficient when you have large amounts of data: making them too big means lots of idle time for frames

### 3.2 Why Collision Detection and Semi-Reliability

Why does Ethernet do collision detection during transmission? 

- It's possible to do collision detection on a wire in a way that is hard to do on a radio medium
- Collision detection during transmission is much more efficient than collision detection after transmission **ESPECIALLY FOR LARGE FRAMES**

The Ethernet method of immediate collision detection allows the use of large frame sizes without a corresponding increase in wasted bandwidth. The immediate collision detection also allows a quick response to collisions unlike the Aloha metho d (which is based on timers and retransmissions as in Stop-and-Wait).

Another goal of Ethernet was semi-reliabiliy:

A relaible Data Link must guarantee that all lost or corrupted frames are resent. Ethernets have good random bit error rates

*The Ethernet does its best to retransmit (in hardware) all frames lost due to
col lisions.*

### 3.3 Ethernet Design Details

#### 3.3.1 Collision Detection

Collision detection was done by using a Manchester Encoding with a net DC bias that is non-zero

Carrier Sense can be done either by sensing a DC voltage or sensing the receipt of a Manchester Signal (alternating voltage pushes)

#### 3.3.2 Semi-reliability Mechanisms: Min Frame Size and Jamming

*Slot*: 2T, where T is the maximum propogation delay between two stations on the Ethernet. A slot is the maximum time it takes for a sender to detect a collision involving its own transmission. 

The Ethernet requires a min. frame size of at least 64 bytes. If users have smaller amounts of data to be sent, they must add a special pad character to pad out the frame to 64 bytes (Ethernet header has length field)

*jamming*: If B detects a collision and stops its transmission after only sending a few bits, A may not reliably be able to detect a collision, so B sends a fixed number of bits to enforce this collision. 

#### 3.3.3 Adaptive Backoff Times

The slot time is the vulnerable time for Ethernet

Once a frame has been transmitted for 51.2 usec without a collision, there should be no collisions for that frame (enough time has elapsed fro all other stations to sense the transmission of the frame and to send back collided bits)

What should we do after a collision??

The ideal behavior is that one station transmits immediately, and the other waits a slot time to sense the medium

For two stations, it is essentially flipping a coin. Think about this game as two people tossing coins before one wins (not wait vs. wait one slot)

For multiple stations we can use a *dynamic scheme*

The Ethernet scheme starts with N small (equal to 20 = 1) and roughly doubles after each unsuccessful collision. This is what is called binary exponential backoff , because the backo time grows exponentially (by a factor of two) for every unsuccessful collision. You reset the backo time after your frame (not others frames) is transmitted successfully.

### 3.4 Ethernet Code

On receipt there is a check for min frame size before checking the checksum (FCS)

### 3.5 Ethernet Frame Format

Format: 

1. Preamble -> sequence of alternating 0's and 1's which help the clock recovery circuits get into synch followed by a 11 to help sender know when frame starts

2. first 6 bytes represent intended destination

### 3.7 Ethernet Pros and Cons

*Supposed challenges*

1. It is supposed to be unpredictable because of random delays
2. Min frame size requirement is supposed to be wasteful

*Three Real Disadvantages*

1. Ethernet has limited distance (2.5 km) -> Bridges help a lot
2. Performance gets worse on high loads
3. Doesn't work well on fiber but needs coax or twisted pair

### 3.8 Cost of Statistical Multiplexing in Ethernets

Suppose we increase the distance of an Ethernet or increase the transmission rate. It is easy to see that the scheme gets more inecient. If we increase the transmission sp eed or max distance by a factor of 10, the min frame size to detect collisions would go up to 640 bytes, which means that most small frames (of say 40 bytes) which have only about 50 percent padding overhead currently, will now have 500 percent overhead. Since 80 percent of the trac sent is little frames, this is inecient.
(As an aside, the 80-20 rule for frame sizes is a useful rule of thumb: 80 percent of the traffic consists of little frames of size 40 bytes and 20 percent consists of larger frames of 576 bytes or more. Frames of size 570 bytes or so are common because of some disk block sizes (512 byes) plus higher layer headers.

cost of Statistical multiplex. in Ethernet is prop. to product of propogation delay and transmission speed (pipe size)

## 5 Token Rings

Ethernet provides good latency at low loads, and token rings provide good throughput at high loads. 

### 5.1 Requirements: One-bit delays and Frame Stripping

Token Rings need for *small token passing delays* and *frame stripping*

Stations that do not want to transmit can essentially repeat all bits with a one-bit delay

If each station wants to transmit, and each of them delay each frame by 3 byte delays, delay will add up

All rings use approximately the same idea for avoiding store-and-forward delays. They use what we call cut-though forwarding: a node in the ring begins forwarding a frame before it has completely received it.

Second Requirement: Frame stripping:

However, while F will not consume ring throughput, its going to cost lots of unnecessary
pro cessing at the intended receivers and even cost wasted bandwidth at other links.

Receiver of a frame to strip a frame that's sent to it

After it reaches Dest. address, the receiver can strip the rest of the frame
  - this prohibits multicast, though
  
## 6 IBM Rings

IBM Token Ring solves two problems:

1. **1 bit token passing delays**: Free token and start of a frame differ by at most 1 bit
2. **Frame Stripping**: After sending its frames, teh sender doesn't pass the token until the first bit of its last frame sent arrives back. Station then keeps stripping the received bits unti it sees the end of its last frame

### 6.1 Implementing One-bit delays

