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

An algorithm that takes an arbitray amount of data input (credential) and produces a fixed-sized output (bit array) on enciphered text called a hash value.

Hashes are used to verify and ensure data intergrity
Based on one-way maths funct - easy to compute but v. hard to reverse this calc
Can be used to verify authentication

Aritrary length text --> Hash function --> Hash value

### Well known Hash functions
1. Message Digest 5 (MD5)
2. Secure Hash Algorithm 1 (SHA-1)
3. Secure Hash Algorithm 2 (SHA-2) - SHA-384

### Hash Message Authentication Code (HMAC)
- To add authentication, HMAC uses an additional secret key as input to the hash function
- Output HMAC - an authenticated fingerprint

### Password salting

- The addition of a unique, random string of characters (known only to the site) to the end of each password to create a different hash value
- e.g g Password 546789gfvgrTY
- Salt = SALT
- Salted_Password = 546789gfvgrTYSALT
- Hash(Password) = <>Hash(Salted_Password)

## Public Key Infrastructure
Digital signatures
- A mathematical technique used to provide authenticity, integrity and non-repudiation
- Properties of digital signatures
	- Authentic: cannot be forfed and provides proof that the signer and no one else signed the doc
	- Unalterable: after signed, a document cannot be altered
	- Non-reusable: document signature cannot be transferred to another doc
	- Non-repudiated: signed document is considered to be the same as a physical document

### Digital Signature standards 
- Digital Signature Algorithm
- Rivest-Shamir Adelman Algorithm
- Elliptic Curve Digital Signature Algorithm

### Code signing
Digital signatures are commonly used to provide assurance of the authenticity and integrity of software code - users can verify that code is legitimate.
Digitally signing code provides several assurances about the code.

- Code is authentic and sourced by the publisher
- The code has not been modified since itleft the software publisher
- The publisher undeniably published the code, this provides non-repudiation of publishing


### Digital certificates
Equivalent to an electronic passport. Allows users, hosts and organisations to securely exchange info over the internet.
- Verifies identities between users in a transaction
- Provide assurance that published content has not been modified by any authorized actors
- Used to exchange public keys for encrypting and decrypting web content - public key certificate proves ownership of the public key
- Requires a 3rd party to validate the certificate

### Public key Infrastructure

Certificate database
PKI certificate authority - there's a hierachy: Root ca (give to users and subordinate ca), Subordinate ca (give to users)
Certificate store (on your pc)
PKI certificate 


**Certificate enrolment, authentication and revocation**

- Enrolment
	- The certificate authority permits a user's request to provide them with a certificate
	-  Requester generates a key pair (public and private), sends the public key to the CA with the request, once accepted they receive a CA signed public key and a certificate which they can install
- Authentication
	- Identify users, machines or devices using digital certificates
	- An electronic document based on the idea of a passport
	- Contains the digital identity of a user including a public key and the digital signiture of a certification authority
 	- Digital certificates prove the ownership of a public key issued by the certification authority
- Revocation
	- Sometimes the certificate must be revoked e.g a digital certificate can be revoked if a key is compromised/ no longer needed
	- Two common methods for revocation: Certification Revocation List, Online Certificate Status Protocol

## Cryptanalysis
The study of ciphertext, ciphers and cryptosystems with the aim of understanding how they work and finding and improving techniques for defeating/ weakening them 

Methods uses in cyptanalysis:
- Brute-force method
	- Defeating a scheme by entering a large number of possibilites to break a cipher
- Ciphertext method
	- Attacker only has access to a set of ciphertexts, attacker attempts to extract the corresponding plaintexts or the key from the ciphertext
- Known-plaintext method
	- Attacker has access to both plaintext and its encrypted version (the ciphertext), these can be used to reveal secret keys
- Chosen-plaintext method
	- Attacker can choose random plaintexts to be encrypted and obtain the corresponding ciphertexts, the information gained reduces the security of the encryption scheme, the attacker could even calculate the secret key
- Chosen-ciphertext method
	- Attacker gains info by choosing a ciphertext and obtaining decryption unde
- Meet-in-the-middle method
	-


# Access control


## Access Control Models

- DAC: Discretionary access control
- MAC: Mandatory access control
	- Restricts the ability individual resource owners have to grant or deny access to resource objects in a file system
- RBAC: Role-based access control
	- Organizations use RBAC to provide their employees w/ varying levels of access based on their roles and responsibilities (Accounting manager will have different privilege than a junior accountant)
- ABAC: Attribute-based- access contol
	-
- RBAC: Rule-based access control
- TAC: Time-based access control
- The principle of least privilege
	- Privilege escalation
## AAA Framework

- Authentication: users and admins must prove who they are (username and password, id card w/ magnet, certificate, ssh key)
- Authorization: authorization services determine which resources the user can access and what operations they are permitted to perform (controlled by the server what can/ can't a user do)
- Accounting: accounting records hold info about- what the user does, what's being accessed, amount of time the resource is accessed, changes that are made 

## AAA Architecture
- Local AAA Authentication: sometimes known as self-contained authentication- it authenticates users against locally stored usernames/ passwords
- Server-Based AAA Authentication - authenticates against a central AAA server that contains the usernames/ passwords for all users
- LDAB

## AAA Protocols
- Remote Authentication Dial-in User Service (RADIUS): supports centralized authentication authorization and accounting management for clients that establish connection with a networj and intend to use any of the provided services
- Terminal Access Controller Access Control System (TACAS)
- TACAS+ 


# SSH key
- Generate authentication key (public/private RSA key pair) on the client computer
- Setup SSH on server to use this authentication key
- When you want to access server, you can now access it without entering username/password
	- It recognises the shh key when you copy the public key to the authorised keys files

# Authentication

The process of recognising a user's identity to allow/deny resources.

## Fundamentals

- Something you know e.g password or PIN 
- Something you carry/have such as flash drive or proximity card
- Something you are e.g fingerprints

## Passwords

- Passwords are the most common methods of authentication
	- Can contain letters, numbers, special characters
- The average person has about 25 different online accounts but only 54% of users use different passwords accoss these accounts
- At one time 86% of > 2 mil breached passwords were identical to passwords already breached
- Top most common passwords (123456, qwerty, password etc) are still used regulary
- [NCSC top 100K commonly used passwords](https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt)

** Good Passwords **
- The longer the password the more difficult it is to crack
- Always use a combination of character, numbers and special characters
- Use a variety of passwords
- Don't keep a pattern between passwords

** Bad Passwords **
- Dictionary word
- Using personal information
- Using patterns
- Using character substitutions
- Using numbers and special characters only at the end
- Using common passwords
- Using anything but a random password


** Password Attacks and Defence **
- Attacks
	- Brute-force attack: submit many passwords in hope of eventually guessing the correct combination, systematically check all possible passwords
	- Rainbow Table attack: using a rainbow hash table to crack the passwords stored in a database system
- Defence
	- Salt technique prevents rainbow table attack
	- Key stretching, converting a password to a longer and more random key for encryption

## Token Authentication
A material device that is used to access secure systems
- Common forms include a dongle, card or RFID chip
- Tokens make it more difficult for hackers to access an account since they must have long credentials and tangible device itself which is much harder for the attacker to obtain

## Biometric Authentication

Advantages:
- Can be easily compared to authorized features saved in a databse
- Can control physical access when installed on entrances and doors
- Can be added into multi-factior authentication process password + voice or token + face recognation

Types
- Facial recognition - e.g measuring distance between eyes, chin shape disadvantages: people who look alike, face at different angles, algorithm is not complex enough
- Fingerprint scanners - can even vein match (vascular biometrics)
- Voice identification - say a sentence or a word to authenticate
- Eye scanners - iris recognition, retina scanner - glasses can cause issues

## Certificate-based Authentication
- Identify users, machines or devices using digital certificates
- An electronic document based on the idea of a passport
- Contains the digital identity of a user including a public key and the digital signiture of a certification authority
- Digital certificates prove the ownership of a public key issued by the certification authority

## Multifactor Authentication

- Requires two or more independent ways to identify a user
- e.g codes generated from user's smartphone, fingerprints, facial recognition
- Increase the confidence of users as there are multiple layers of security
- Good defence against account hacks, but disadvantage: people may lose their phones or SIMs => can't generate an authentication code


## Authentication Protocols
- NTLM - suite of Microsoft security protocols intended to provide authentication, integrity and confidentiality to users
- KERBEROS - uses tickets to authenticate, uses symmetric key
- PAP - password authentication protocol (weak, vulnerable protocol)
- CHAP - challenge handshake authentication protocol
- Secure Sockets Layer (SSL)/Transport Layer Security (TLS) - client uses the servers public key to encrypt the data that is used to compute the secret key, server can only generate the secret key if it can decrypt the data with the correct private key
