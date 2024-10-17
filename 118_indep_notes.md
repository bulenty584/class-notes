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

