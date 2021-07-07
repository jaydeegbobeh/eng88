# Introduction to Cybersecurity 

Definitions:
NIST - The ability to protect or defend the use of cyberspace from cyber attacks
CNSS
- Prevention of damage
- Protection of and the restoration of computers, electronic communication systems, electronic communications services, wire communication and electronic communication
- Including information contained in these ^
- To ensure it availability, integrity, authentication, confidentiality and non-repudiation

## Cybersecurity Cube (McCumber)

A model framework for establishing and evaluating information security programs

1. Desired goals 
	- Confidentiality: what is?
	- Integrity
	- Availability
2. Data states
	- Transmission
	- Storage
	- Processing
3. Safeguards
	- Human Factors: people should be aware of their roles - person in charge of setting up this firewall
	- Policies and Practices - configuration of the firewall, access control list
	- Technology - firewall


### 1st dimension: desired goals (CIA Triad)
- Confidentiality: unautharized access is prevented (cryptography, access lists)
- Integrity: data should not be modified by unautharized users
- Available: access should be accessible to authorized users when needed (9am-5pm, during working hours)

### 2nd dimension: data states
- Storage: Data At Rest (DAR) in an information system e.g stored in  memory, a disk
- Transmission: transferring data between information systems - also known as Data In Transit (DIT)
- Processing: performing operations on data in order to achieve a desired objective

Data vs Information?
- Data is a collection of facts, information provides the context for those facts
- Data is unorganised, information is structured
e.g for a class test each student's test score is a piece of data, the average score of the class is a piece of information

### 3rd dimension: safeguards
- 

## Key terms
- Asset: an asset is something that needs to be protected e.g data, device
- Vulnerability: a weakness or gap in protection efforts - use pentesting to find bugs and determine their severity
- Exploit: a program, piece of code, tool designed to take advantage of the vulnerabilities 
- Threat: (hypothetical event) malicious act that seeks to damage data, steal data or cause any disruption
- Risk: intersection of asssets, threats and vulnerabilities - evaluate to existence of a vulnerability of an asset and determine the severity/chance of a potential threat.

## Causes of Vulnerabilities
1. Development/ design errors
2. Poor system configuration - not configuring
3. Human errors - someone leaves a document unattended/ not disposing of it properly, sharing passwords
4. Connectivity - accesible via a public wifi
5. Complexity 
6. Passwords - should be strong, don't share it, changed frequently, different passwords for different systems (don't use the same)
7. User input - hackers can feed malicious input into a web app that is processed without any blocks
8. Management
9. Lack of training staff
10. Communication

## Cyber attacks
1. Un-targeted cyber attacks
2. Targeted cyber attacks
	- In 2020 hackers inserted malicious code into the SolarWinds system, there was a backdoor that the hackers could access and impoersonate users and accounts of organizations, this malware could access system files and blend in with legitimate activity without detection (even by antivirus software!)

## Cyber threat actors
1. Nation-states: geopolital motivation
2. Cybercriminals: profit
3. Hacktivists: ideological
4. Terrorist groups: ideological violence
5. Thrill-seekers: satisfaction 
6. Insider threats: discontent

# Cyber threats
- Malware: software that carries out malicious tasks on a device or network e,g corrupting data
- Spyware: a form of malware that hides on a device providing real-time info e.g gives them access to steal bank account details
- Phishing attacks: when a cybercriminal attempts to lure individuals into providing sensitive data
- DoS attack/Distributed denial of service (DDoS) attakcs: aims to disrupt a computer network by flooding the network with fake traffic to overwhelm it - in DDoS multiple systems target a single system
- 
- Ransomeware: a type of malware, denies access to a computer system or data until a ransom is paid e.g REvil a file encryption virus encrypts all files and demands money from the victim
- Zero-day exploits: a flaw in software, hardware, firmware that is unknown to the parties responsible for patching the flaw (take advantage of vulnerabilites)
- Advanced persistent threat: when an unauthorized user gains access to system/network and remains there undetected for a long period of time (until they are discovered they have access)
- Trojan: backdoor in your system
- Wiper attack: form of malware with the intention to wipe a hard drive
- Intellectual property theft: stealing or using someone else's intellectual property without permission
- Theft of money: gaining access to back accounts/ credit card numbers
- Data manipulation: change data in a system
- Data destruction: delete data
- Man-in-the-middle attack: alters communication between two parties who beliebe they are communicating with each other
- Rogue software: malware disguised as real software
- Unpatched software: software that has known security weaknesses that are fixed in a later release but not yet updated
- Data centre disrupted by disaster: data centre could be disrupted by flooding
- Spear-phishing: sending emails to targeted individuals that could contain an attachment with malicious software, or a link that downloads malicious software

## Cyber threat surface
- The available endpoints that threat actors may attempt to exploit in internet-connected devices within the cyber threat environment
- Services, devices and data can all be targeted
- Systems that connect with the internet

## Cyber kill chain

graph TD;
	Reconnaissance(choose target, identifiy vulnerabilities)-->Weaponization(create malware weapon like a virus to exploit the vulnerabilities fo the target)
	Weaponization(create malware weapon like a virus to exploit the vulnerabilities for the target)-->Delivery(transmitting the weapon to the target e.g USB drive, email attachment)	
	Delivery(transmitting the weapon to the target e.g USB drive, email attachment)-->Exploitation(program code of malware is triggered, exploiting the target's vulnerability)
	Exploitation(program code of malware is triggered, exploiting the target's vulnerability)-->Installation(malware installs an access point for intruder- a backdoor)
	Installation(malware installs an access point for intruder- a backdoor)-->Command and control(malware gives intruder access in the network/system)
	Command and control(malware gives intruder access in the network/system)-->Actions on objective(once attacker gains persistent access, they fufill their purpose e.g encryption for ransom)


# Cryptology

## Cryptography
- The study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents.
- Encryption: the process which transforms the orginal information into an unrecognizable form
	- Add a key to plain text, use algorith to convert plain text into cipher(unrecognisable) text

- Decryption: the process of converting encoded/encrypted data in a form that is readable and understood by a human or a computer
	- Use key algorith to translate cipher text to plain text (readable)

## Classic ciphers
Cipher- an algorithm for performing encryption/decryption that consists of a series of well-defined steps that can be followed as a procedure.

- Substitution cipher
- Transposition cipher
	- No letters are replaced; simply rearranged
	- Key for transposition cipher (e.g rail fnece cypher key=3 encrypt by text in 3 diagonal rows)
- Caesar cipher

## Encryption classes

Two classes of encryption used to provide data confidentiality- differ in how they use keys
1. Symmetric encryption algoriths: encryption algorithms that use the same key to encrypt and decrypt data
	- Used in: payment applications, validations to confirm that the send of a message is who they claim to be
	- **Block cipher**: encryption is completed in 64 bit blocks, 
	- **Stream cipher**: encryption is one bit at a time
	- example: Advanced Encryption Standard, key size: 128, 192, 256
	- Symmetric encryption is commonly used as it uses less resources (less bits), it also has the advantage of speed (useful for online banking)
	- Initialisation vector

2. Assymetric encryption algoriths: use different keys to encrypt and decrypt data
	- Use public key (encryption) and private key (decryption)
	- Less than 1024 bits is not recommended
	- Alogrithms e.g Diffie-Hellman 512,1024, 2048, 3072, 4096 key length, Digital Signature Standard 512-1024 key length
- Assymetric Encryption for confidentiality
	- public key (encrypt) + private key(decrypt) = confidentiality
- Assymetric Encryption for authentication
	- private key (encrypt) + public key(decrypt) = authentication - ensure message is coming from someone with the correct private key


### Diffie-Hellman
- An asymmetric mathematical algorithm
- Allows two computers to generate an identical shared secret w/out having communicated before
- New shared key is never actually exchanged between the sender and receiver
- Uses
	- Data exchanged using an IPsec VPN
	- Data is encrypted on the internet using SSL/TLS
	- SSH data is exchanged

## RSA algorithm

### Protocols-based on asymmetric key algorithms
- Internet key exchange (IKE): fundamental compontent 

## Symmetric vs Assymetric 
*add table


## Cryptographic Hash Operation

