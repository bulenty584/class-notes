# Lecture 13 Notes #

## Introduction

* Most systems need to store data persistently

## Our Persistent Data Options

+ Use raw storage blocks to store data
  + on a hard disk, flash drive, etc.
  + not easy for OS developers to work with

+ Use database to store the data
  + more structure (and more overhead) than we need!

+ Use a file system!
  + some organized way of structuring persistent data
  + makes sense to users and programmers
  + hide all the details about what goes on in storage devices!

## Basic File System Concept

+ Organize data into natural coherent units
  + like paper, spreadsheet, message, program, etc.
  
+ store each unit as its own self-contained entity
  + a file
  + store each file in a way allowing efficient access

+ Provide some simple, powerful organizing principle for the collection of files
  + easy to find and organize them

## File Systems and Hardware

+ file systems are typically stored on hardware(persistent memory)
  + flash drives, etc

+ expectation that file put in one place will be there when we look again

+ performance considerations (match implementation to hardware)

## Flash Drives

+ Solid state persistent storage devices
  + I.e. no moving parts
  
+ Reads and writes are fast

+ Given block can only be written once
  + writing again requires erasing
  + much slower and erases large sectors of the drive
  
## Data and Metadata

+ File systems deal with two kinds of info

+ *data* - the information that the file is actually storing

+ *Metadata* - Information about the information the file stores
  + E.g. how many bytes are there and when was it created
  + also called *attributes*

+ Data and Metadata must be stored persistently
  + usually on the same piece of hardware
  
## A Further Wrinkle

+ Want file system to be agnostic to storage device

+ Same program should access the file system the same way, regardless of device

+ Should work for flash drives of different types


## Desirable File System Properties

+ Persistence

+ Easy to use model
  + for accessing a file
  + for organizing collections of files
  
+ Flexibility
  + no limit on number of files
  + no limit on file size, type, contents

+ Portability across hardware device types

+ Performance

+ Reliability

+ Suitable security

## The Performance Issue

+ How fast should our File System be?
  + as fast as everything else! (CPU, memory, and bus, etc.)
  + so we don't get a bottleneck
  
+ Devices operate today at nanosecond speeds

+ Flash drives are so much slower!

## The Reliability Issue

+ Persistence implies reliability

+ file systems must be free of errors (hardware or software)

## Basics of File System Design

  + File control data structures
    + interacts with OS
	
## File Container Operations

+ Standard file management System Calls

## Directory Operations

+ Organize files into directories

+ Directories translate name to a lower-level file pointer

+ Directory operations tend to be related to that
  + file by name
  + create new name/file mapping
  + list a set of known names
  
## File I/O Operations

+ Open - use name to set up an open instance

+ Read and write data from/to a file
  + Implemented using logical block fetches
  + Copy data btwn user space and file buffer
  + Request file system to write back block when we're done

+ Seek
  + Change logical offset associated with open instance
  
+ Map file to address space
  + File block buffers are just pages of physical memory
  + Map into address space, page it to and from the file system
  
## The Virtual File System Layer

+ Federation layer to generalize file systems
  + Permits rest of the OS to treat all file systems as the same
  + Support dynamic addition of new file systems

+ Plug-in interface for file system implementations


# Lecture 15 Notes #

## Creating a New File

* Allocate a free file control block
  * For unix
    * search super-block free 1-node list
	* take the first free 1-node
  * For DOS
    * Search the [parent directory for an unused directory entry
* Initialize a new file Control block
  * With file type, protection, ownership
  
## Extending a File

* Application requests new data assigned to a file
  * may be explicit allocation/extension request
  * may be implicit(e.g. write to a currently non-existing block)
  
## Deleting a file

* Release all space that is allocated to the file
  * For unix, return each block to free block list
  * DOS does not free space!
    * uses garbage collection
	* searches all deallocated blocks and add them to free list at some future time

* Deallocate the file control lock
  * For UNIX, zero inode and return it to free list
  * For DOS, zero the first byte of the name in the parent directory
    * indicating that the directory entry is no longer in use

## Free Space Maintenance

* File system manager manages the free space

* Getting and releasing blocks should be fast
  * They are extremely frequent
  * We'd like to not do I/O as much as possible

## Allocation/Transfer size

* Per operation overheads are high

* larger transfer units are more efficient
  * Amortize fixed per-op costs over more bytes/op
  * multi-megabyte transfers are very good

* What unit do we use to allocate storage space
  * small chunks reduce efficiency
  * large fixed size chunks -> internal fragmentation
  * variable sized chunks -> external fragmentation

## Flash Drive Issues

* Dominant technology

* Special flash characteristics:
  * faster than hard disks, slower than RAM
  * Any location equally fast to access
  * But write-once/read-many access
    * until you erase
  * Only erase large chunks of memory

## Read Ahead

* Request Blocks from the device before any process asked for them

* reduces process wait time

* When does it make sense?
  * When client requests sequential access
  * When client seems to be reading sequentially

* What are the risks
  * May waste device access time reading unwanted blocks
  
  * may waste buffer space on unneeded blocks
  
## Write Caching

* Most device writes go to a write-back cache
  * They will be flushed out to the device later

* Aggregates small writes into large writes
  * If application does less than full block writes
  
* Eliminates moot writes
  * If application rewrites to the same data
  * If application deletes the file

* Accumulates large batches of writes
  * A deeper queue to enable better disk scheduling
  
## Common Types of Disk Caching

* General block caching
  * Popular files that are read frequently
  * Files that are written and then re-read
  * Provides buffers for read-ahead and deferred write

* Special purpose caches
  * Directory caches speed up searches of same dirs
  * Inode caches speed up re-uses of same file

* Special purpose caches are more complex
  * often work much better by matching cache granularities to actual needs

## Pinning File Data in Caches

* Caching usually controlled by LRU-ish strategy

* Some file data is *pinned* in memory
  * Not subject to cache replacement, temporarily

* Inodes of files processes are one example
  * Ensures quick access to a structure that will probably be used again

* Contents of current working directories may be pinned

## Naming in File Systems

* Each file needs some kind of handle for us to refer to it!

* OS likes simple numbers as names
  * not usable by people of programs tho

## File Names and Binding

* File systems know files by descriptor structures

* We must provide more useful names for users

* The file system must handle name-to-file mapping
  * Associating names with new files
  * Finding the underlying rep. for a given name
  * Changing names associated with existing files
  * allowing users to organize files using names
  
* *Name Space* - the total collection of all names known by some naming mechanism
  * All names that *could* be created by mechanism

## Some Issues in Name Space Architecture

* How many files can have the same name?
  * one per file system ... flat name spaces
  * one per directory ... hierarchical name spaces

* How many different names can one file have?

  * Single "true name"
  * Only one "true name", aliases are allowed

* Do different names have different characteristics?

* Directories are like files (have their own inodes, NO SYMBOLIC LINKS THO)

## Directories are Files

* Stored in file system, have inodes, file descriptors

* Directory contains multiple directory entries
  * Each directory entry describes one file and its name

* User applications are allowed to read directories
  * get info on each file
  * find out what files exist

## File Names vs. File Paths

* In some name space systems, files had "true names"
  * only one possible name for a file
  * kept in a record somewhere

## Multiple File Names In Unix

* How do links relate to files?
  * They're the names only

* All other metadata is stored in the file inode
  * File owner sets file protection
  
* All links provide access to the same file

## Links and De-allocation

* Files exist under multiple names

* What do we do if one name is removed?

* Unix: File exists as long as at least one name exists!

* We must keep and maintain a reference count of links (in file inode, not directory)

## Symbolic Linls

* Different way of giving files multiple names

* implemented as a special type of file
  * No guarantee the file is actually there!

* NOT A REFERENCE TO THE INODE

* File system automatically recognizes symbolic links (automatically opens associated file instead)

## Core Reliability Problem

* File system writes typically involve multiple operations
  * not just writing data block to disk/flash
  * also writing one or more metadata blocks
  * inode, free list, maybe directory blocks

* All must be committed to disk for write to succeed

# Lecture 15

## Introduction

* OS provides the lowest layer of software visible to users
* OS is also close to the hardware!
  * has complete access to hardware
* if OS isn't protected, the machine isn't protected
* flaws in the OS compromise all security at higher levels (rotten core)

## Why is the OS security so Important??

* OS controls access to application memory
* OS schedules processes!
* OS ensures that users receive the resources they ask for
* if OS isn't doing these things securely, a lot can go wrong

## Important Definitions

* *Security* is a policy
  * describes what you want to have happen (what should happen vs. what shouldn't)
* *Protection* is a mechanism
  * E.g. permissions for different users
*Protection mechanisms implement security policies

## Vulnerabilities and Exploits

* *vulnerability* is a weakness that can cause an attacker to cause problems
* *exploit* is an actual incident of taking advantage of a vulnerability
  * allowing attacker to do something bad on some particular machine
  * term also refers to code or methodology that is used to take advantage of a vulnerability
  
## Trust

* Extremely important
* Do certain stuff for people you trust
* Don't do certain stuff for people you don't trust
* Seems simple, but how do you express it, why do you trust, how can you be sure...?

## Trust and the Operating System

* You **have** to trust your OS
  * Controls hardware, including memory
  * Controls how your processes are handled
  * Controls all I/O devices
* If your OS is corrupt, you're cooked

## Authentication and Authorization

* We need to know who wants to do something
  * Allow trusted parties to do it
  * Don't allow others to do it
* We need to know who's asking
  * *authentication!!*
* We then need to check if that party should be allowed to do it
  * Determining that is authorization
  * authorization usually requires authentication
  
## Authentication

* Security policies tend to allow some parties to do something, but not others
* We need to know who's doing the asking
* For OS, the computer decides this!

## Real World Authentication

* Identification by recognition
* Identification by credentials
* Identification by knowledge
* Identification by location
* All of the above have similar cyber analogs

## Authentication With a Computer

* Can't do certain things well
  * e.g. facial recognition
* Bottom line is they are not as smart as people!
* They can do computations super fast, though
  * Mathematical methods are acceptable
* Often must authenticate non-human entities
  * Like processes or machines
  
  
## Identities in OS

* We usually rely on User ID
  * Uniquely identifies some user on a particular computer
  * Processes run on his behalf, so they inherit his ID
* Implies a model where any process belonging to a user has all his privileges
  * drawbacks are there

## Boostrapping OS Authentication

* Processes inherit their User IDs from their parent process
* Somewhere along the line we have to create a process belonging to a new user
  * Typically on login to a system
* We can't just inherit that identity, so how can we tell who this newly arrived user is?

## Passwords

* Authenticate the user by what he *knows*
  * Secret word he supplies to the system on login
* System must be able to chekc that the password was correct
  * either by storing it, or a hash of it
* If correct, tie user ID to a new command shell or window management process

## Problems With Passwords

* They have to be unguessable
* If networks connect remote devices to computers , susceptibleto password sniffers
  * Programs which read data from the network, extracting passwords when they see them
* Unless quite long, brute force attacks often work on them
* Widely regarded as an outdated technology
* But widely used

## Proper Use of Passwords

* Passwords should be sufficiently long
* Passwords should be unguessable
* Passwords should never be written down
* Passwords should never be shared
* Hard to achieve all this simultaneously

## Challenge/Response Systems

* Authentication by what questions you can answer correctly
  * Again, by what you know!
* The system asks the user to provide some information
* If it's provided correctly, the user is authenticated
* Safest if it's a different question every time
  * Not practical for humans

## Hardware-Based Challenge/Response

* The challenge is sent to a hardwaer device belonging to the appropriate user
  * Authentication based on what you have
* Sometimes possession of device is enough 
  * text challenges sent to a smart phone to be typed into web request
* Sometimes device performs a secret function on the challenge
  * smart cards
  
## Problems With Challenge/Response
  * If based on what you know, usually too few unique and secret challenge/response pairs
    * Often the response can be found by attackers
  * If based on what you have, fails if you don't have it
    * Whoever does have it might pose as you
  * Some forms susceptible to network sniffing
  
## Biometric Authentication

* Authentication based on what you are
* Measure some physical attribute of the user
  * Fingerprints, voice patterns, retinal patterns, etc.
* Convert it into a binary representation
* Check the representation against a stored value for that attribute
* if it's a close match, authenticate the user

## Problems With Biometric Authentication

* Requires very special hardware
* Many physical characteristics vary too much for practical use
* Generally not helpful for authenticating programs or roles
* Requires special care when done across network!


## Errors in Biometric Authentication

* False Positives
  * You identified Bill Smith as Peter Reiher
*False negatives
  * Didn't identify Peter Reiher as Peter Reiher
  
## Multi-factor Authentication

* Rely on two separate authentication methods
  * E.g. password and text message to your cell phone
* If well done, each method compensates for some of the other's drawbacks
  * If poorly done, not so much
* The current preferred approach in authentication

## Access Control in OS

* OS can control which processes access which resources
* Giving it the chance to enforce security policies
* Mechanisms used to enforce policies

## Access Control Lists

* ACLs

## An Example Use of ACLs: The Unix File System

* Still in wide use today
* Per-file ACLs (files are the objects)
* Three subjects on list for each file
  * Owner, group, other
* Three modes
  * Read, write, execute
  * Sometimes have special meanings
  
## Pros and Cons of ACLs

* Easy to figure out who can access a resource
* Easy to revoke or change access permissions
* Hard to figure out what a subject can access
* Changing access rights requires getting to the object

## Capabilities

* Each entity keeps a set of data items that specify his allowable accesses
* Essentially, a set of tickets
* To access an object, present the proper capability
* Possession of the capability for an object implies that access is allowed

## Properties of Capabilities

* Capabilities are essentially a data structure
  * just collection of bits
* Having the capability grants access
  * can't be forgeable
* How to ensure unforgeability for collection of bits?
  * don't let user/process have them
  * store them in the OS
  
## Pros and Cons of Capabilities 

* Easy to determine what objects a subject can access
* Potentially faster than ACLs 
* Easy model for transfer of privileges
* Hard to determine who can access an object
* Requires an extra mechanism to allow revocation
* In network environment, need cryptographic methods to prevent forgery
  * Someone can listen to what's being transferred, and can make copy of capability bits
  
## OS Use of Access Control

* OS use both ACLs and capabilities
  * sometimes for same resource
* E.g. Unix/Linux uses ACLs for file opens
* That creates a file descriptor with a particular set of access rights
  * E.g., read-only
* The descriptor is essentially a capability

## Enforcing Accesses in an OS

* Protected resources must be inaccessible
  * Hardware protection must be used to ensure this
  * only the OS can make them accessible to a process
* To get access, issue a request (system call) to OS
  * OS consults access control policy data
* Access may be granted directly
  * Resource manager maps resource into process
* Access may be granted indirectly
  * Resource manager returns a *capability* to process
  
## Cryptography

* Convert secret from a readable form to a different one that's not readily readable

## Cryptography Terminology

* Sender is S
* Receiver is R
* *Encryption* is the process of making the message unreadable by anyone but R
* *Decryption* is the process of making the encrypted message readable by R
* A system performing these transformations is a cryptosystem
  * Rules for transformation sometimes called a *cipher*

## Plaintext and Ciphertext

* *Plaintext* is the original form of the message (often referred to as P)
* *Ciphertext* is the encrypted form

## Cryptographic Keys

* Most cryptographic algorithms use a *key* to perform encryption and decryption
  * Referred to as K
* The key is a secret
* Without the key, decryption is hard
* Reduces secrecy problem from your (long) message to the (short) key
  * Still a secret

# Lecture 17 Continued

## Asymmetric Cryptosystems

* *public key cryptography*
* Encryption and decryption use different keys
  * Encrypt with one and decrypt with the other

## Using Public Key Crytography

* Keys are created in pairs
* One key is kept secret by the owner and the other is made public to the world
* If you want to send an encrypted message to someone, encrypt with his public key
  * Only this person has private key to be able to decrypt encrypted message
  
## Authentication with Public Keys

* If I want to "sign" a message, encrypt it with my private key
* Only I know my private key, so no one else could create that same message
* Everyone knows my public key, so everyone can check my claim directly
* This is much better than with symmetric cryptography
  * receiver could not have created the message!
  * Only sender could have created it
  
## Issues with PK Key Distribution

* Security of public key cryptography depends on using the right public key
* If I'm fooled into using wrong one, that key's owner reads my message
  * or authenticate incorrectly
* Need high assurance that a given key belongs to a specific person
  * either key distribution infrastructure
  * certificates
* Both are problematic

## Nature of PK Algos

* Usually based on some problem in math
  * like factoring really large numbers
* Security less dependent on brute force
* More on the complexity of the underlying problem
* Implies choosing key pairs is complex and expensive
* We need big keys!
  * We regard 4096 bit key as being good enough!

## Example Public Key Ciphers

* RSA
  * Most popular public key algo
  * Used on everyone's computer nowadays
* Elliptic Curve Cryptography
  * An alternative to RSA
  * Usually has better performance
  * Not as widely used or studied
  * Still generally available

## Security of PK Systems

* Based on solving the underlying problem
  * E.g. for RSA, factoring large numbers!
* The longer the key, the more expensive the encryption and decryption

## Combined Use of Symmetric and Asymmetric Cryptography
  * Common to use both in single session
  * Asymmetric Cryptography essentially used to securely share a key btwn sender and receiver
  

# Lecture 18: Distributed Systems

## Intro

* Modern computing is an application of distributed systems
  * We need help from more than one computer in most cases
* OS is going to help in local applications
  * controls filesystem, etc.

## Why Distributed Systems

* Scalability
  * We can make use of more than just one computer!
    * Throwing computing power at a single problem
  * Better performance!
* Better Reliability and availability
  * Can access any resource at any time
  * 24/7 service despite disk/computer/software failure
* Ease of use, with reduced operating expenses
  * Centralized management of all services and systems
  * Buy better services rather than computer equipment
  
## Few Problems

* Different machines don't share memory
  * Or any peripheral devices
  * So one machine can't easily know the state of another!
    * synchronization problems!
* Only way to interact remotely is to use a network
  * Usually asynchronous, slow, and error prone
  * Usually not controlled by any single machine
* Failures of one machine aren't visible to other machines
  * pieces of a machine could fail at any moment!
  
## Deutsch's "Seven Fallacies of Network Computing"

1. Network is reliable
2. There is no latency
3. Available bandwidth is infinite
4. Network is secure
5. Topology of the network does not change
6. One administrator for the whole network
7. Cost of transporting additional data is zero 

**Bottom Line: true transparency is not achievable!**

## Distributed System Paradigms

* Parallel Processing
  * Relying on tightly coupled special hardware
* Single System Images
  * Make all nodes look like one big computer
  * Somewhere btwn hard and impossible
* Loosely Coupled systems
  * Work with difficulties as best you can!
  * Typical modern approach to distributed systems
* Cloud Computing
  * recent variant

## Loosely Coupled Systems

* Characterization
  * Parallel group of independent computers
  * Connected by high speed LAN
  * Serving similar but independent requests
  * Minimal coordination and cooperation required
* Motivation
  * Scalability and price performance
  * Availability: if protocol permits stateless servers
  * Ease of management, reconfigurable capacity
* Examples
  * Web servers, app servers

## Horizontal Scalability

* Each node is largely independent
* You can add capacity just by adding a node "on the side"
* Scalability can be limited by hardware, etc.

## Elements of Loosely Coupled Architecture

* Farm of independent servers
  - servers run same software, serve different requests
  - may share a common back-end database
* Front-end switch
  - Distributes incoming requests among available servers
  - Can do both load balancing and fail-over
* Service protocol
  - Stateless server and independent operations
  - Successive requests may be sent to different servers

## Horizontally Scaled Performance

* Individual servers are very inexpensive
  - Blade servers may be only 100-200$ each
* Scalability is great
  - 100 servers deliver ~100x performance
* Service availability is great
  - front-end automatically bypasses failed servers
  - stateless servers adn client retries fail-over easily
* True challenge is managing thousands of servers
  - Automated installation, global config. services
  - Self-monitoring, self-healing systems
  - Scaling limited by management, not Hardware or algos

## Cloud Computing

* Most recent twist on distributed computing
* What runs in a cloud?
  - anything
  - General distributed computing is hard
* So much of the work is run using special tools
* Tools support particular kinds of parallel/distributed processing
  - Using a method like map-reduce or horizontal scaling
* User need not be a distributed systems expert

## MapReduce

* The most common cloud computing software tool
* Method of dividing large problems into little pieces
* Each of which can be performed on a separate node
* With an eventual combined set of results

## The Idea behind MapReduce

* Single function you want to perform on a lot of data
  - Searchig for a particular string
* Divide data into disjoint pieces
* Perform the function on each piece on a separate node (map phase)
* Combine results to obtain output (reduce)

## An Example

* We have 64 mb of text data, divide into 4 pieces of 16 mb
* Send each piece to a different processor to run a function on each piece
* At the end the pieces are sent to reduced nodes to combine again

## Synchronization in MapReduce

* Each map node produces an output file for each resource node
* Produced automatically
* Reduced node can't work on this data until the whole file is written
* Forcing a synchronization point btwn the map and reduce phases

## What's hard about Distributed Synchronization?

* Spatial separation
  - Different processes run on different systems
  - No shared memory for locks
  - They are controlled by different OSes
* Temporal Separation
  - Can't "totally order" spatially separated events
  - Before/simultaneous/after lose their meaning
* Independent modes of failure
  - One partner can die while others continue
  
