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



