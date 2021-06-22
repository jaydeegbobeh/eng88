# Networking
Collection of devices exchanging data.

## Network components
**Host** : Computer connected to a network, helps communicate with other hosts in the network. Hosts include clients and servers.
**Server** : Host whose software allow them to provide services to other hosts (client)
**Client** : Host that requests the service

## Server-client architechture
Structure that partitions tasks/ workloads between the providers (server) of a resource/server and service requesters (client).

## Peer-to-peer architecture 
Here the workload is partitioned between peers. Peers are equally privileged and equipotent. Both peers can request from each other.
- e.g Network print sharing: a printer is connected to one device via USB, this device is then configured to a shared printer. Other devices in the network can then access the shared printer as a resource on te network.

## Intermediary device 
Networking device positioned between a remote access service (RAS) and a RAS client.
- Switches and wireless access points (network access)
- Routers
- Firewalls

## Network media
- Metal wired (usually Cu) cable
- Fiber optic (drawing glass/ plastic, diameter is slightly thicker than a human hair)
- Wireless

## End device
A source or destination device in a networked system e.g a user's PC.

## Network type is based on
- Size of area covered
- Number of users connected
- Type of serices
- Area of responsibility

	- LAN: Local Area Network (house/office)
	- WAN : Wide Area Network (extends over a large geographic area for the primary purpose of computer networking)


## Internet
### Internet interconnected network
WAN/ LAN - can be wired, fiber optic, wireless (public).
### Intranet
LAN/WAN - Network internal to an organisation (private)
### Extranet
Controlled, private network that allows third party partners to gain information about a company, without granting access to an organisations entire network.

Private networks are not routable like public networks.

## Communication fundamentals
A source (sender) and destination (reader) communicate over a channel. The purpose is to transmit a message over the channel from source to destination.

## Message delivery options
- Unicast: delivered to one destination
- Multicast: delivered to a set of destinations
- Broadcast: delivered to all destinations in a network

## Protocol standards
Group of interelated protocols

### Open System Interconnection (OSI) model, a conceptual framework used to describe the functions of a network system.
**Physical Layer**
Lowest layer of the OSI model, electrically transmits raw unstructured data bits across the network from the physical layer of the sending device to the physical layer of the receiving device e.g voltages, pin layout, cabling.
**Data Link Layer**
Directly connected nodes are used to perform node-to-node data transfer where data is packaged into frames. Data link layer also corrects errors that may have occurred at the physical layer.
- Data link layer encompasses two sub-layers, Media Access Control (MAC), provides flow control and multiplexing for device transmissions over a network.
- Logical Link Control (LLC) provides flow and error control over the physical medium.
**Network Layer**
Responsile for receiving frames from the data link layer and delivering them to their intended destinations based on the addresses contained inside the frame.
- Network layer finds the destination by using logical addresses such as IP (internet protocol).
- Routers are crucial component used to quite literally route information where it needs to go between networks
**Transport Layer**
Transport layer manages the delivery and error checking of data packets.
- TCP: Transmission Control Protocol
- UDP: User Datagram Protocol
**Session Layer**
Controls conversation between different computers.
**Presentation Layer**
Formats or translates data for the application layer based on the syntax that the application accepts.
**Application Layer**
The end user and the application layer interact directly with the software application (top layer).


In TCP/IP session, presentation, application are considered as application.
Application layer
Transport layer
Internet layer
Network access layer

Layers work together by encapsulation - when data moves from upper layer to lower layer of TCP/IP protocol stack, during an outgoing transmission, each layer includes a bundle of relevant information called "header" along with the actual data.
Decapsulation - each layer takes out info from previous layer.

## Port number
Communication end point.
- Identifies a specific process/ type of network service.
- Port numbers are always associated with an IP address of a host and the type of transport used for communication.
- Source ports and destination ports form a channel/

###Port numbers
0-65535 (2^16) 16 bits

0-1023: well known ports: reserved for popular services, e.g email
1024-49151: registered ports e.g applications
49152-65535: private/dynamic ports

Some examples of TCP port numbers:
**TCP 20** : FTP file transfer protocol - data transfer
**TCP 21** : FTP control
**TCP 22** : SSH (secure shell) access port host
**TCP 23** : telnet 
**TCP 25** : SMTP - simple mail tranfer protocol
**TCP 80** : HTTP (web) hyper text transfer protocol

Bandwidth: maximum rate of data transfer accross a given path e.g bits per second

## Positional Number System
### Binary Numeral System (0,1)
**2^n** - radix=2, position in number=n

| Radix              | 2   | 2   | 2   | 2   | 2   | 2   | 2   | 2   |
|--------------------|-----|-----|-----|-----|-----|-----|-----|-----|
| Position in number | 7   | 6   | 5   | 4   | 3   | 2   | 1   | 0   |
| Calculate          | 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
| Position value     | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| 1=                 | 0   | 0   | 0   | 0   | 0   | 0   | 0   | 1   |
| 2=                 | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 0   |
| 3=                 | 0   | 0   | 0   | 0   | 0   | 0   | 1   | 1   |
| 8=                 | 0   | 0   | 0   | 0   | 1   | 0   | 0   | 0   |
| 17=                | 0   | 0   | 0   | 1   | 0   | 0   | 1   | 0   |
| 172=               | 1   | 0   | 1   | 0   | 0   | 0   | 1   | 1   |
| 255=               | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |

### Decimal Numeral System

| Radix              | 10   | 10   | 10   | 10   |
|--------------------|------|------|------|------|
| Position in number | 4    | 2    | 1    | 0    |
| Calculate          | 10^3 | 10^2 | 10^1 | 10^0 |
| Position value     | 1000 | 100  | 10   | 1    |
| 1=                 | 0    | 0    | 0    | 1    |
| 2=                 | 0    | 0    | 0    | 2    |
| 34=                | 0    | 0    | 30   | 4    |
| 3458=              | 3    | 4    | 5    | 8    |

### Hexadecimal Numeral System
**16^n** 

| Hexidecimal | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | A    | B    | C    | D    | E    | F    |
|-------------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|------|
| Decimal     | 0    | 1    | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   | 14   | 15   |
| Binary      | 0000 | 0001 | 0010 | 0011 | 0100 | 0101 | 0110 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

e.g converting from hexidecimal to decimal and binary
hex- A9, dec- (10 x 16^1) + (9 x 16^0) = 169, binary- 1010, 1001
hex- CAB, dec- (12 x 16^2) + (10 x 16^1) + (10 x 16^0) = 3243, binary - 1100, 1010, 1011 

## MAC address: Media Acess Link
MAC address controls device interaction
48 bit 12 hexidecimal (6 octets)


|OUI     |NIC     |
|--------|--------|
|Vendor  |Device  |
|02 42 90|c1 b4 8c|

OUI:organisationally unique identifier
NIC:network interfacing controller

- To view the MAC address of your PC : ipconfig /all (Windows PowerShell), ifconfig -a (MAC terminal, Linux shell)
The MAC address is not routable, you can't find where it exists outside the local address.

## Network Layer (3) Addressing
**IP address** : A numerical lable assigned to each device connected to a network that uses the Internet Protocol for communication.
**IP** : the internet protocol is a set of rules governing the format of data sent via the internet.

IPV4 - series of 1s and 0s (binary numeral system)
32 bit (4 octet)

**IP classes**
Classful addressing
|       |Octet 1|Octet 2|Octet 3|Octet 4|
|-------|-------|-------|-------|-------|
|Class A|1-127  |0-255  |0-255  |0=255  |
|Class B|128-191|0-255  |0-255  |0=255  |
|Class C|192-223|0-255  |0-255  |0=255  |
|Class D|224-239|0-255  |0-255  |0=255  |
|Class E|240-255|0-255  |0-255  |0=255  |

Class A first octet starts with 0
Class B first octet starts with 10
Class C first octet starts with 110

Class A - 2^24 available host IP addresses
Class B - 2^16 available host IP addresses
Class B - 2^8 avaiable host IP addresses

Class A subnet mask - 255.0.0.0 /8, bpcast IP - 0nnn nnnn.255.255.255 (first octet is between 1-127)
Reserved Private 10.0.0.0-10.255.255.255
Loopback 127.0.0.0-127.255.255.255 - local host, don't assign this to anything

Class B subnet mask - 255.255.0.0 /16, bpcast IP 10nn nnnn.nnnn nnnn.255.255 (first octet between 128-191 and second 0-255)
Reserved private: 172.16.0.0-172.31.255.255

Class C
Net ID 192-223.0-255.0-255.0
1st IP: 192-223.0-255.0-255.1
Last IP: 192-223.0-255.0-255.254
bcast IP: 192-223.0-225/0-255/255
Subnet mask 255.255.255.0 /24

**Subnet Mask**
- 32 bit address
- Used to mask a portion of the IP address to distinguish the network ID from the host ID
	- Calculate the Network ID: convert the IP to binary, calculate the logical AND for the IP address and the Subnet Mask
- Every host on a TCP/IP network requires a subnet mask
- In the subnet mask:
	-Bits that correspond to the network ID are set to 1
	-Bits that correspond to the host ID are set to 0
	- 1s on left, 0s on right

e.g
255.0.0.0 = 1111 1111.0000 0000.0000 0000.0000 0000 = /8
255.255.0.0 = 1111 1111.1111 1111.0000 0000.0000 0000 = /16
255.255.255.0 = 1111 1111.1111 1111.1111 1111.0000 0000 = /24
255.255.255.128 = 1111 1111.1111 1111.1111 1111.1000 0000 = /25
255.255.255.192 = 1111 1111.1111 1111.1111 1111.1100 0000 = /26
255.255.255.224 = 1111 1111.1111 1111.1111 1111.1110 0000 = /27
255.255.255.252 = 1111 1111.1111 1111.1111 1111.1111 1100 = /32

**Logical AND**
0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1
e.g calculate Network ID
Host ID: 192.128.2.1
logical AND
Subnet Mask: 255.255.255.0
Network ID: 192.128.2.1

**Broadcast ID (bcast IP)**
- The last IP in the network
- all hosts bits of the IP address are 1's
- All host in a network should have the same Broadcast IP
- Use the broadcast IP to send specific data to all the machines on the same network

**Localhost- 127.0.0.1**
The standard IP address used for a loopback network connection - looped back to your own machine (this computer)

**Ping**
- Ping is Internet Control Message Protocol (ICMP) packet. -at layer 3 (Network)
- Ping allows a user to ping another device IP address, this helps determine whether a device is reachable via the network.

command prompt:
ping 192.128.2.1

Returns:
Reply from... : host has received the ping message back from the destination device within the designated time period
Request timed out: host did not receive the ping message back from the destination device within designated time period
Destination host unreachable: route to destination computer system cannot be found

**Broadcast Domain**
A broadcast domain is the region that broadcasts are received, broadcasts are restricted by routers(layer 3 devices)

**ARP & RARP**
Layer 2
Address resolution protocol - maps an IP address to a permanent physical machine address in a local area network MAC
Reverse address resolution protocol
ARP and RARP translate between IP addresses and MAC layer addresses
- They are broadcast protocols
All hosts on a network are located by their IP address, but NICs (layer 2) do not have IP addresses, they have MAC addresses. ARP associated the IP address to a MAC address.

**Default Gateway**

The device that handles the traffic between different IP networks, usually the router interface.
Hosts can only send traffic to the gateway if:
- it's connected to its network physically
- it's on the same subnet (usually)

## Servers

**DHCP**
Dynamic Host Configuration Protocol - works on bc mode (mac address FFFF.FFFF.FFFF) - this uses UDP ports => application layer protocol
Server/ client protocol
- Automatically assigns IP hosts with IP addresses and other IP addresses of devices connected to the network (e.g default gateway)
- Port numbers:
	- 67/udp for DHCP server
	- 68/udp for DHCP client 
-  Eliminates need for individually configuring network devices manually.

**HTTP**
Hypertext Transfer Protocol - an application layer protocol for transmitting hypermedia documents (graphics, audio, plain text video)
HTML - markup languge for documents designed to be displayed in a web browser
HTTP runs over TCP
TCP port 80
HTTPS (secure)
TCP port 443

**FTP**
File Transfer Protocol - application layer protocol used for the transfer of computer files from a server to a client on a computer network.
TCP port 21 - used to establish the connection between 2 hosts
TCP port 20 - used to transfer data 

**DNS**
Domain Name System - converts host names/ domain names into IP addresses, browsers uses these IPs to load internet pages.
DNS is an application layer protocol that uses the transport layer protocol . Uses TCP for zone transfer and UDP for name.

## Firewalls
A network security system that monitors/ controls incoming and outgoing network traffic (between networks) - firewalls can be a device or a software.
Access Control List (ACL) - set of rules or policy that grants/denies access to a resource, it filter access to a network.
ACLs usually reside in a firewall router in a router that connects networks.

**Properties of Firewalls**
- Resistent to network attacks.
- Have ACLs
- Can be software installed on a host/ hardware, a computes that enforces ACLs.

**Advantages**
- Prevents hackers and remote access
- Protects data
- Protects privacy details
- Can protect against Trojans - malware often disguised as legitimate software.

**Disadvantages**
- It can't always protect network from attacks from the inside.


**Packet Filtering Firewall**
Based on network, transport layers. Monitors outgoing and incoming packets and allowing them to pass or halt based on the source and destination IP address, protocols and ports (TCP/UDP ports)

**Application Gateway Firewall**
More capable than packet filtering firewall.
Operates at the application layer (also checks presentation, session, transport, network layers). This means firewall can check software.

**Firewall zones**
Private(inside)
Public(untrusted)
DMZ - a perimeter network that protects the internal local-area network from untrusted traffic.
- Allows you to access untrusted networks like the internet, whilst ensuring its private network remains secure.

## Virtual Private Networks (VPN)

VPN aims to secure network traffic between sites and users.
- Users and organisations use VPNs to create end-toend private network connections
- A vpn is virtual in that it carries info within a private network but that info is actually transported over a public network
- The traffic is encrypted to keep the data confidential while it is transported

### VPN Protocols


**Point-to-Point Tunneling Protocol (PPTP)**
- A set of communication rules that govern the secure implementation of VPNs which allow organisations a method of extending their own private networks over the public Internet via "tunnels"

**Generic Route Encapsulation (GRE)**
- A tunneling protocol that can enca[sulate a wide variety of network layer protocols inside virtual point-to-point links over an IP network

**Layer 2 Tunneling Protocol (L2PT)**
- A tunneling protocol used to support VPNs. L2PT uses encryption only for its own control messages and does not provide any encryption or confidentiality of content by itself.
 
**IP Security (IPSec)**
- A secure network protocol suite, authenticates and encrypts the packets of data to provide secure encrypted communication between two computes over an IP network.


**Secure Socket Layer (SSL)**
- An ecryption-based internet security protocol.

### Host-to-Host VPN
Connects one desktop to another host. This connection uses the network to which each host is connected to create a secure tunnel between the two.
Connects hosts not networks
Intercepter - router can only see scrambled data with VPN tunnel

### Host-to-Site VPN
VPN client software is on host itself

vpn server: vpn gateway(vpn concentrator)router/ firewall
Connection is from host to entire network => host can access all of network resources e.g webserver

### Site-to-Site VPN
A connection between two or more networks, e.g a coporate network and a branch office network
- Creates an encrypted link between vpn gateways located at each of these sites
- A site-to-site vpn tunnel encrypts traffic at one end and sends it to the other site over the public internet where it is decrypted and routed on to its destination

## Network Address Translation (NAT)

### IP address shortage
- There are not enough public IPv4 addresses to assign a unique address to each device connected to the internet (whole world)
- Private addresses are used within an organization or site to allow devices to communicate locally 
- Private IPv4 addresses cannot be routed over the internet

To allow a device with a private IPv4 address to access devices and resources outside of the local network, the private address must first be translated to a public address.
NAT provides the translation of private addresses to public addresses - NAT router
A single public IPv4 address can be shared by hundred, even thousands of devices (i.e private IP addresses)
Assigned by network provider then depends on region (country, even sometimes what city).
- My phone and laptop connected to my home router have the same public IP.

NAT keeps a table containing details of the connections
Inside Local IP, Inside Global IP, Outside Global IP

### Types of NAT

Static NAT: uses a one-to one mapping of local and global addresses. 
- Useful when a network device inside a private network needs to be accessible from internet
- If you don't give access to NAT to everbody, you can hide internal network
- Inside local addresss always takes a specific inside global address (addresses reachable via NAT Router)

Dynamic NAT: mapping of a private IP address to a public IP address from a group of public addresses called a NAT pool.
- Establishes a one-to-one mapping between a private IP address to a public IP address - takes first available public address
- Here public IP address is taken from the pool of IP addresses configured on the end NAT router.
- Cannot translate 2 ip addresses to a public address.

Port Address Translation NAT: can map multiple private IP addresse to a single public IP address by using a technology known as PAT
- When a client from inside the network communicates to a host in the internet, the router changes the source port (TCP/ UDP) number with another port number.
- The port mappings are also kept in a table which keep the port mapping and forward the data packet to the originial sender.
- Adv: multiple internal hosts can share a single IP address for communication => conserving IP addresses
- Adv: Hosts on private network dont have to expose their private IP address to the public network making attacks from the public network less likely
- Disadv: if too many hosts on the private network try to make many connections to the public network PAT device may not have sufficient room in its internal table to keep track of the connections or it may run out of unused ports
e.g router at home


