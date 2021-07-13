# Linux

Linux is a family of open source Unix-like OS - source code is publically accessible so that anyone can read, modify and distribute the code.

## Architecture 

**Hardware layer** - Linux OS contains a hardware layer that consists of peripheral devices e.g CPU, HDD, RAM

**Kernel** - a core section of the OS, it's a software code that serves as a layer between the hardware and main programs that run on the computer.
- Memory management: track how much memory is used to store what and where.
- Process management: determine which processes can use the CPU, when and how long.
- Device drivers: interpreter between hardware and processes.
- System calls and security.

**Shell** -  provides the user with an interface to the system.
- A layer between the user and the kernel, where the user can enter commands.

**Applications**

**Utilities**
![alt text](https://raw.githubusercontent.com/jaydeegbobeh/eng88-cybercourse/main/Computer_Windows_Linux_Virtualisation_Cloud/Linux/linux_architecture.png)

## Distribution

Linux distributions are OS's based on the Linux kernel.
There are many distros of Linux e.g:
- Kali Linux: mainly used for advanced Penetration Testing(Ethical Hacking) and Security Auditing (Debian-based).
- Fedora: mainly used for servers and cloud computing.
- Ubuntu

## Filesystems

- The Linux filesytem unifies all physical hard drives and partitions into a single directory structure.
- The entire Linux directory structure starts at the top /root directory.
- Data storage formats include: EXT3, EXT4, BTRFS, XFS.

**"Everything is a File"**

- Everything in the system from processes, files, directories is represented by a file descriptor.
	- There is one way of reading/writing everything.
	- The same set of tools can be used on all input/output resources - documents, directories, hard-drives, keyboards etc.

 