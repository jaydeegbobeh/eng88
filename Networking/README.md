# Networking
Collection of devices exchanging data.

## Network components
**Host** : Computer connected to a network, helps communicate with other hosts in the network. Hosts include clients and servers.
**Server** : Host whose software allows them to provide services to other hosts (client)
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
- The data link layer handles such tasks as gathering up sets of bits for transmission as packets and making sure the packets get from one end to the other. In addition, recognizing that physical layer transmission sometimes introduces errors, the data link layer handles error detection (and sometimes correction).
- The MAC layer routes packets from a sender to a receiver along a common path. It makes sure the message arrives at the intended recipient. The MAC layer adds a physical address, defining the intended recipient machine, and controls shared access to a resource.
- It handles problems that occur as a result of bit transmission errors.
- It ensures data flows at a pace that doesn't overwhelm sending and receiving devices.
- It permits the transmission of data to Layer 3, the network layer, where it is addressed and routed.
- Logical Link Control (LLC) provides flow and error control over the physical medium.
**Network Layer**
Responsible for receiving frames from the data link layer and delivering them to their intended destinations based on the addresses contained inside the frame (the protocol data unit at the data link layer)
- Network layer finds the destination by using logical addresses such as IP (internet protocol).
- Routers are crucial component used to quite literally route information where it needs to go between networks
**Transport Layer**
Transport layer manages the delivery and error checking of data packets 
- It's the layer at which TCP/IP ports listen e.g the standard port which HTTP listens on is TCP Port 80
- TCP: Transmission Control Protocol, TCP is a transport level protocol of the Internet that provides reliable, end-to-end communication between two processes. The requesting process, often known as the client, requests services from the server process.
- UDP: User Datagram Protocol, a communications protocol that facilitates the exchange of messages between computing devices in a network
**Session Layer**
- Controls conversation between different computers.
- It establishes, manages, and terminates the connections between end-user application processes
**Presentation Layer**
Formats or translates data for the application layer based on the syntax that the application accepts.
- Audio,
**Application Layer**
The end user and the application layer interact directly with the software application (top layer).


In TCP/IP session, presentation, application are considered as application.
Application layer - presentation, application are considered as application
Transport layer - transport layer
Internet layer - network layer
Network access layer - physical, data link

Node: modems, switches, hubs, bridges, servers, and printers are also nodes, as are other devices that connect over Wi-Fi or Ethernet.

- Whenever we send the data from one node to another in a computer network.
- The data is encapsulated at the sender's side, while it is de-encapsulated at the receiver's end. 
- Actually, the encapsulation of data at various layers of the implementing model(OSI or TCP/IP) adds various functionalities and features to the data transmission
    
Data Encapsulation is the process in which some extra information is added to the data item to add some features to it. We use either the OSI or the TCP/IP model in our network, and the data transmission takes place through various layers in these models. Data encapsulation adds the protocol information to the data so that data transmission can take place in a proper way. This information can either be added in the header or the footer of the data.
The data is encapsulated on the sender’s side, starting from the application layer to the physical layer. Each layer takes the encapsulated data from the previous layer and adds some more information to encapsulate it and some more functionalities with the data. These functionalities may include proper data sequencing, error detection and control, flow control, congestion control, routing information, etc.

Data De-encapsulation is the reverse process of data encapsulation. The encapsulated information is removed from the received data to obtain the original data. This process takes place at the receiver’s end. The data is de-encapsulated at the same layer at the receiver’s end to the encapsulated layer at the sender’s end. The added header and trailer information are removed from the data in this process.


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
- The sender does not need to indicate recipient addresses – this is how the broadcast process differs from unicast, where only a single known recipient is addressed.
- Broadcast ip replaces the recipient addresses in question. 

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
All hosts on a network are located by their IP address, but NICs (layer 2) do not have IP addresses, they have MAC addresses. ARP associates the IP address to a MAC address.

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
- HTTPS makes a secure connection by establishing an encrypted link between the browser and the server or any two systems

**FTP**
File Transfer Protocol - application layer protocol used for the transfer of computer files from a server to a client on a computer network.
TCP port 21 - used to establish the connection between 2 hosts
TCP port 20 - used to transfer data 

**DNS**
Domain Name System - converts host names/ domain names into IP addresses, browsers uses these IPs to load internet pages.
DNS is an application layer protocol that uses the transport layer protocol . Uses TCP for zone transfer and UDP for name.
- DNS amplification is a Distributed Denial of Service (DDoS) attack in which the attacker exploits vulnerabilities in domain name system (DNS) servers to turn initially small queries into much larger payloads, which are used to bring down the victim's servers.

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
- A common DMZ meaning is a subnetwork that sits between the public internet and private networks. It exposes external-facing services to untrusted networks and adds an extra layer of security to protect the sensitive data stored on internal networks, using firewalls to filter traffic.
- Using the DMZ subnet instead. Since it's an independent subnet, the DMZ host and other LAN subnet are isolated. Therefore, if an attacker breaks into a host on the DMZ subnet, he or she cannot access the other LAN subnets.

## Virtual Private Networks (VPN)

VPN aims to secure network traffic between sites and users.
- Users and organisations use VPNs to create end-to-end private network connections
- A VPN is virtual in that it carries info within a private network but that info is actually transported over a public network
- VPN is private in that the traffic is encrypted to keep the data confidential while it is transported to keep the data confidential while it is transported across the public network

### VPN Protocols

**Point-to-Point Tunneling Protocol (PPTP)**
- A set of communication rules that govern the secure implementation of VPNs which allow organisations a method of extending their own private networks over the public Internet via "tunnels"

**Generic Route Encapsulation (GRE)**
- A tunneling protocol that can encapsulate a wide variety of network layer protocols inside virtual point-to-point links over an IP network

**Layer 2 Tunneling Protocol (L2PT)**
- A tunneling protocol used to support VPNs. L2PT uses encryption only for its own control messages and does not provide any encryption or confidentiality of content by itself.
 
**IP Security (IPSec)**
- A secure network protocol suite, authenticates and encrypts the packets of data to provide secure encrypted communication between two computes over an IP network.

**Secure Socket Layer (SSL)**
- An ecryption-based internet security protocol.
- 

**Transport Layer Security (TLS)**
- Transport Layer Security, or TLS, is a widely adopted security protocol designed to facilitate privacy and data security for communications over the Internet. A primary use case of TLS is encrypting the communication between web applications and servers, such as web browsers loading a website.

**OpenVPN**
An open source tool that can be used to create VPN connection

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

- NAT protects private IP
- Flexibility, whenever there's a problem with one IP address, the router can switch 
### Types of NAT

Static NAT: uses a one-to one mapping of local and global addresses. 
- Useful when a network device inside a private network needs to be accessible from internet
- If you don't give access to NAT to everbody, you can hide internal network
- Inside local addresss always takes a specific inside global address (addresses reachable via NAT Router)
- For example, you may have a web server with the inside IP address 192.168.0.10 and you want it to be accessible when a remote host makes a request to 209.165.200.10. For  this to work, you must do a static NAT mapping between those to IPs.
- Static NAT is useful for Servers inside your network
- e.g give private ip to server on router/firewall do NAT to give server a public address (when you need it to be fixed)

Dynamic NAT: mapping of a private IP address to a public IP address from a group of public addresses called a NAT pool.
- Establishes a one-to-one mapping between a private IP address to a public IP address - takes first available public address
- Here public IP address is taken from the pool of IP addresses configured on the end NAT router.
- Cannot translate 2 ip addresses to 1 public address.
(still map 1-to-1, e.g there's 8 IPs available but 10 employees, 8 employees at same time can browse internet => limited
- less used because it doesn't really solve a problem like static and PAT

Port Address Translation NAT: can map multiple private IP addresses to a single public IP address by using a technology known as PAT
- When a client from inside the network communicates to a host in the internet, the router changes the source port (TCP/ UDP) number with another port number.
- The port mappings are also kept in a table which keep the port mapping and forward the data packet to the originial sender.
- Adv: multiple internal hosts can share a single IP address for communication => conserving IP addresses
- Adv: Hosts on private network dont have to expose their private IP address to the public network making attacks from the public network less likely
- Disadv: if too many hosts on the private network try to make many connections to the public network PAT device may not have sufficient room in its internal table to keep track of the connections or it may run out of unused ports
e.g router at home


