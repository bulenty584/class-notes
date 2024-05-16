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

+ Gievn block can only be written once
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
