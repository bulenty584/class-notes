# Appendix B: Virtual Machine Monitors (Week 9 Lecture 14 Readings)

## **B.1 Introduction**

* To solve the problem of running different OSs on the machine at the same time
  * The monitor sits between one or more OSs and the hardware
  * Gives illusion to each running OS that it controls the machine
    * Actually the monitor is in control of the hardware
	* VMM => OS for OSs!
	* **Transparency** is key!

## **B.2 Motivation: Why VMMs?**

* Server consolidation
  * people can run services on diff. machines (which run on diff. OSs)
  * Owner can **consolidate** multiple OSs onto fewer hardware platforms

* Virtualization
  * users want to run one OS but also want to run another (for native apps)

* Testing and Debugging

  * Devs can debug and test code they write on one platform on many diff ones
  
## **B.3 Virtualizing the CPU**

* To run **virtual machine**, we need **limited direct execution**
  * When we boot a new OS on top of VMM, just jump to address of first instruction and let OS run!
  * Not that Simple!
    * VMM must perform **machine switch** when running multiple OSs
	  * VMM must save entire machine state of one OS(registers, PC, privileged hardware state), restore machine state of the to-be-run VM, and then jump to PC of the to-be-run VM
	  * **Problem**: When running app or OS tries to perform **privileged operation**
	    * E.g. OS normally updates TLB, but in Virtualized environment not possible bc then OS controls machine instead of VMM
		* VMM must intercept attempts to do privileged ops
	      * When app performs system call, it executes trap instruction, but VMM controls machine, which has installed a trap handler
	* The VMM doesn't know **how** to deal with the system call (doesn't know details of each OS!)
	* It does know **where** the OSs trap handler is!
	  * When OS booted up, it tried to install its own trap handlers
	    * This is a privileged op. so it trapped into the VMM, and VMM recorded necessary info
		* **When OS performs privileged op. it traps into VMM**
		  * User-mode app does sys call, trap into OS(VMM knows where OS trap handler is), OS performs trap, does return from trap (VMM trap handler is called, does real return-from-trap) 
		* due to all the jumping around, performance is hurt
		* OS runs in supervised mode
		  * No access to privileged instructions, but one can access a little more memory than when in user mode
		  
## **B.4 Virtualizing Memory**

* How does an OS normally think of physical memory?
  * linear array of pages, assigns each page to itself or user processes
* Extra layer of virtualization for VMM
  * "physical memory" ==> virtualization on top of **machine memory**(real physical memory of the system!)
* How does Address Translation work normally?
  * User generates address, process generates **virtual address** (address space virtualized by the OS)
    * Job of the OS is to translate VPN (20 bits) into valid PFN and produce fully-formed physical address
	  * We expect TLB to handle translation (when TLB miss, OS gets involved to service miss: trap into OS, which looks up VPN in page table and updating TLB)
* Address Translation with VMM
  * Process makes virtual memory reference (if misses, trap into VMM TLB miss handler since VMM is the true privileged owner of machine)
  * VMM TLB handler jumps to OS TLB miss handler which runs, does page table lookup for VPN, installs VPN-to-PFN mapping in TLB
    * This is a privileged instruction! So we trap again into VMM and it installs VPN-to-MFN mapping instead!
	* System gets back to user level code, retries instruction which is a TLB hit
	* How does a VMM get involved with hardware-managed TLB?
	  * hardware walks the page table on each TLB miss and updates TLB
	    * VMM doesn't have a chance to run on each TLB miss to sneak its translation into the system
		* VMM must closely monitor changes the OS makes to each page table(in hardware-managed systems, is pointed to by page-table base register)
		* Must keep **shadow page table** that maps the virtual addresses of each process to the VMMs desired machine pages
	* TLB misses on a virtualized system become more expensive
	  * to reduce cost, "software TLB"
	    * VMM records every virtual-to-physical mapping that it sees the OS tried to install
		* On a TLB miss, VMM consults software TLB
		  * if it finds the translation, simply installs the virtual-to-machine mapping directly into the hardware TLB
	*ASIDE: Para-Virtualization
	  * Running a modified OS to run on a VM (**para-virtualization**)
## **B.5 The Information Gap**

* **Information gap** exists btwn OS and VMM (VMM has no idea what OS is doing)
  * Can lead to inefficencies
    * If OS has nothing else to run, OS will go into **idle loop**
	  * just spins and waits for the next interrupt to occur
	* Demand zeroing of pages
	  * Most OSs zero a physical frame before mapping it to process's address space(done for security)
	    * If OS gave one process a page that another had been using *without* zeroing it, information leak!
	  * VMM must also zero pages that it gives to each OS, and so many times page will be zeroed twice, once by VMM and once by OS
	    * No real solution, just made OS aware to not zero pages it knew had been zeroed by VMM
	* Solutions
	  * inference (**implicit info**)
	    * VMM can detect idle loop by noticing OS switched to low-power mode
	  * OS can be changed

# CHAPTER 39: FILES AND DIRECTORIES

## Introduction

* Two key OS abstractions are:
  * the process ==> virtualization of the CPU
  * the address space ==> Allows a program to run as if it's in its own private, isolated world
* Another SUPER IMPORTANT PIECE: **persistent storage**. 
  * **Hard disk drive** or modern **solid-state storage device**
    * Stores info permanently
    
* FOLLOWING IS ALL TO DO WITH A <i><b> UNIX FILESYSTEM </b></i> 

## 39.1: Files and Directories

* **File** abstraction
  * linear array of bytes, each of which you can read and write
  * Each file has some kind of low-level name
    * **INODE NUMBER**
  * OS doesn't really know much about the structure of the file
    * Job is to just store it!
* **Directory** abstraction
  * Like a file, it has a low-level name but its contents are specific
    * contains list of user-readable and low-level name pairs
    
## 39.3 Creating Files

* **open()** system call used to create a file with O_CREAT flag
  * O_TRUNC flag truncates the existing file to a size of zero bytes as to remove any existing content if it exists
  * returns a **File descriptor**
    * Just an integer and is used in UNIX to access files (you use file descriptor to read or write to a file once it's opened)
    * File descriptor is a **capability**
      * handle that gives you power to perform certain ops
      * pointer to an object of type file
        * once you have such an object, you can call other methods to access the file
    
    * File descriptors are managed by the OS on a per-process basis
      * Some kind of simple structure (e.g. an array) is kept in the proc structure on unix
      * Each entry of the array is just a pointer to a <i>struct file</i>. 

## 39.4: Reading and Writing Files
  * **strace** is used to track the system calls made by a program
    * traces every system call made by a program while it runs
    * = num, this num is the file descriptor!
      * Why does first call to open return 3?
        * Each running process already has three files open!
          * STDIN, STDOUT, STDERR (0,1,2)
      * read() system call reads bytes from a file
        * First arg is file descriptor
        * Second arg points to a buffer where the result of the read() will be placed
        * Third arg is the size of the buffer
        * return arg is the number of bytes it read
      * write() system call writes bytes to a file
        * first file is opened for writing, then write() system call is called, then close()
  * **Open file table**
    * Each process maintains an array of file descriptors
      * each of which refers to an entry in the system-wide **open file table**. 
      * Each entry in this table tracks which underlying file the descriptor refers to, the current offset and other details like if the file is readable or writable

## 39.5: Reading and Writing

* lseek system call is used to read ot write to a specific offset in a file

