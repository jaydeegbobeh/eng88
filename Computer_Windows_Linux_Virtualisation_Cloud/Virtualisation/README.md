# Virtualisation

## What is virtualisation?
- Virtualisation creates a simulated computing environment.
- Virtualisation does not exist in a physical form, allows you to create OS's/ storage devices that are traditionally bound to hardware.

## Hypervisors
- A hypervisor is software that creates and runs virtual machines (VMs)
- They isolate the hypervisor OS and resources from VMs.
- Hypervisors are VM monitors, they manage the OS's of the VMs as they run alongside each other.

**Type 1 and Type 2 Hypervisors**

 Type 1 Hypervisors are also known as Metal Hypervisors
- They run directly on the host hardware.
	- The software is installed directly on top of a physical server and it's underlying hardware.

Type 2 Hypervisors are also known Host OS Hypervison
- They execute on an operating system similar to other computer programs.
	- They provide an emulator environment to run another operating system - it's a guest OS running as a process on the host.
- Examples: VirtualBox, VMware

**Type 1 or Type 2?**

- Type 1 is independent from the host OS
	- Better for cloud computing
	- Any malfunction does not harm the rest of the system
	- More secure as it does not depend upon the underlying OS
- Type 2 has the advantage of ease of use, you can easily import/ use multiple OS's

## Benefits of Virtualisation
- Reduced cost - less hardware required, reduced power usage
- Minimise downtime - when a VM is corrupted/ unavailable a new server can be started
- Scalability - the system allocates resources dynamically

