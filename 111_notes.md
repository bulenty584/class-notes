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


