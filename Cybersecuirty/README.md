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
	- Confidentiality: 
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
- Human factors
- Policies and practices
- Technology

## Key terms
- Asset: an asset is something that needs to be protected e.g data, device
- Vulnerability: a weakness or gap in protection efforts - use pentesting to find bugs and determine their severity
- Exploit: a program, piece of code, tool designed to take advantage of the vulnerabilities 
- Threat: (hypothetical event) malicious act that seeks to damage data, steal data or cause any disruption
- Risk: intersection of asssets, threats and vulnerabilities - evaluate the existence of a vulnerability of an asset and determine the severity/chance of a potential threat.

## Causes of Vulnerabilities
1. Development - mistake in development process/ design errors- flaw in hard/software that can't be fixed
2. Poor system configuration - not configuring encryption/cryptography/ password in the system.
3. Human errors - someone leaves a document unattended/ not disposing of it properly, sharing passwords
4. Connectivity - connecting to an insecure network e.g a public wifi
5. Complexity - more features in a system = more attacj syrfaces to cover, greater chance of attack
6. Passwords - should be strong, don't share it, changed frequently, different passwords for different systems (don't use the same)
7. User input - hackers can feed malicious input into a web app that is processed without any blocks
8. Management - lack of management, policies not enforces
9. Lack of training staff - keep employees up to date
10. Communication

## Cyber attacks
1. Un-targeted cyber attacks
2. Targeted cyber attacks
	- In 2020 hackers inserted malicious code into the SolarWinds system, there was a backdoor that the hackers could access and impersonate users and accounts of organizations, this malware could access system files and blend in with legitimate activity without detection (even by antivirus software!)

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
- Ransomeware: a type of malware, denies access to a computer system or data until a ransom is paid e.g REvil a file encryption virus encrypts all files and demands money from the victim
- Zero-day exploits: a flaw in software, hardware, firmware that is unknown to the parties responsible for patching the flaw (take advantage of vulnerabilites)
- Advanced persistent threat: when an unauthorized user gains access to system/network and remains there undetected for a long period of time (until they are discovered they have access)
- Trojan: backdoor in your system
- Wiper attack: form of malware with the intention to wipe a hard drive
- Intellectual property theft: stealing or using someone else's intellectual property without permission
- Theft of money: gaining access to back accounts/ credit card numbers
- Data manipulation: change data in a system
- Data destruction: delete data
- Man-in-the-middle attack: alters communication between two parties who believe they are communicating with each other - alice & bob
- Rogue software: malware disguised as real software
- Unpatched software: software that has known security weaknesses that are fixed in a later release but not yet updated
- Data centre disrupted by disaster: data centre could be disrupted by flooding
- Spear-phishing: sending emails to targeted individuals that could contain an attachment with malicious software, or a link that downloads malicious software

## Cyber threat surface
- The available endpoints that threat actors may attempt to exploit in internet-connected devices within the cyber threat environment
- Services, devices and data can all be targeted
- Systems that connect with the internet

## Cyber kill chain

- Reconnaissance(choose target, identifiy vulnerabilities)
- Weaponization(create malware weapon like a virus to exploit the vulnerabilities for the target)
- Delivery(transmitting the weapon to the target e.g USB drive, email attachment)
- Exploitation(program code of malware is triggered, exploiting the target's vulnerability)
- Installation(malware installs an access point for intruder- a backdoor)
- Command and control(malware gives intruder access in the network/system)
- Actions on objective(once attacker gains persistent access, they fufill their purpose e.g encryption for ransom);
- Once complete cover your tracks and retrieve

# Cryptology

## Cryptography
- The study of secure communications techniques that allow only the sender and intended recipient of a message to view its contents.
- Encryption: the process which transforms the orginal information into an unrecognizable form
	- Add a key to plain text, use algorithm to convert plain text into cipher(unrecognisable) text

- Decryption: the process of converting encoded/encrypted data in a form that is readable and understood by a human or a computer
	- Use key algorith to translate cipher text to plain text (readable)

## Classic ciphers
Cipher- an algorithm for performing encryption/decryption that consists of a series of well-defined steps that can be followed as a procedure.

- Substitution cipher
	- units of plaintext are replaced with the ciphertext
- Transposition cipher
	- No letters are replaced; simply rearranged
	- Key for transposition cipher (e.g rail fence cypher key=3 encrypt by text in 3 diagonal rows)
- Caesar cipher
	- replace each plaintext letter with a different one a fixed number of places down the alphabet

## Encryption classes

Two classes of encryption used to provide data confidentiality- differ in how they use keys
1. Symmetric encryption algoriths: encryption algorithms that use the same key to encrypt and decrypt data
	- Used in: payment applications, validations to confirm that the send of a message is who they claim to be
	- **Block cipher**: encryption is completed in 64 bit blocks, bit is the most basic unit of info 
	- **Stream cipher**: encryption is one bit at a time
	- example: Advanced Encryption Standard, key size: 128, 192, 256
	- Symmetric encryption is commonly used as it uses less resources (less bits), it also has the advantage of speed
	- Initialisation vector: arbitrary number that can be used along with a secret key for data encryption
		- Prevents repition in data encryption, making it more difficult for a hacker usig a dictionary attack to find patterns and break a cipher

2. Asymmetric encryption algoriths: use different keys to encrypt and decrypt data
	- Use public key and private key
	- Less than 1024 bits is not recommended
	- Alogrithms e.g Diffie-Hellman 512,1024, 2048, 3072, 4096 key length, Digital Signature Standard 512-1024 key length
- Asymmetric Encryption for confidentiality
	- public key (encrypt) + private key(decrypt) = confidentiality
- Asymmetric Encryption for authentication
	- private key (encrypt) + public key(decrypt) = authentication - ensure message is coming from someone with the correct private key, integrity of message - it has not been changed
- When connecting to a website on the public internet it becomes more complicated and symmetric encryption, by itself, won’t work because you don’t control the other end of the connection. So asymmetric prevents man in the middle attacks so reducing the risk of someone on the internet incercepting in the middle.

### Diffie-Hellman - used for key exchange not for encryption/decryption
- An asymmetric mathematical algorithm
- Allows two computers to generate an identical shared secret w/out having communicated before
- New shared key is never actually exchanged between the sender and receiver
- Uses
	- Data exchanged using an IPsec VPN
	- Data is encrypted on the internet using SSL/TLS
	- SSH data is exchanged
- Securely exchanging keys over a public channel.
## RSA algorithm

Algorithm for public-key cryptography, works on basic of a public and private key. Public key used to encrypt data before it's sent to the server on which the certificate is located.
### Protocols-based on asymmetric key algorithms
- Internet key exchange (IKE): fundamental compontent 

## Symmetric vs Asymmetric 
| Radix             | Symmetrical Encryption                      | Asymmetrical Encryption                                                | 
|-------------------|---------------------------------------------|------------------------------------------------------------------------|
| Number of keys    |Use same key to encrypt/decrypt data         |Use different keys to encrypt/decrypt                                   | 
| Key length        |Short key length (40 to 256 bits)            |Key lengths are long (512-4096 bits)                                    |
| Speed/ performance|Faster than asymmetric                       |Computationally tasking => slower                                       |
| Usage             |Used for encrypting bulk data e.g VPN traffic|Used for quick data transactions e.g HTTPs when accessing your bank data| 
 


## Cryptographic Hash Operation

An algorithm that takes an arbitray amount of data input (credential) and produces a fixed-sized output (bit array) on enciphered text called a hash value.

Hashes are used to verify and ensure data intergrity: no changes have been made to a set of data, 
Based on one-way maths funct - easy to compute but v. hard to reverse this calc
- Modulo operation is not reversible. If the result of the modulo operation is 4 – that’s great, you know the result, but there are infinite possible number combinations that you could use to get that 4.
Can be used to verify authentication, the source of data can be verified

Aritrary length text --> Hash function --> Hash value
- The set size is determined by the hash function used.  If a change is made to the input data, even something as small as capitalizing a single letter, adding a space or removing a punctuation mark, the output data string will be different.
- Hash functions are deterministic, meaning that no matter how many times the same data is input to the function, the output will be the same.

### Well known Hash functions
1. Message Digest 5 (MD5) - produces 128 bit hash value, MD5 is not suitable for SSL certificates or digital certificates
2. Secure Hash Algorithm 1 (SHA-1) - It takes an input and produces a 160 bits hash value
3. Secure Hash Algorithm 2 (SHA-2) - It produces 224, 256, 384 or 512 bits hash value. Uses improved algorithms and larger hashes

### Hash Message Authentication Code (HMAC)
- To add authentication, HMAC uses an additional secret key as input to the hash function
- Output HMAC - an authenticated fingerprint
- Prevents man-in-the-middle attack
-  provides the server and the client each with a private key that is known only to that specific server and that specific client
- The client creates a unique HMAC, or hash, per request to the server by hashing the request data  with the private keys and sending it as part of a request
- Key and the message are hashed in separate steps.
- Secure file transfer protocols like FTPS, SFTP, and HTTPS use HMACs instead of just hash functions.
- Encryption vs Hashing - encryption is data scambling that is two ways, hashing only one way

### Password salting

- The addition of a unique, random string of characters (known only to the site) to the end of each password to create a different hash value
- Salt is generated randomly for each user and each time they change their password
- e.g g Password 546789gfvgrTY
- Salt = SALT
- Salted_Password = 546789gfvgrTYSALT
- Hash(Password) = <>Hash(Salted_Password)

## Public Key Infrastructure
Digital signatures
- A mathematical technique used to provide authenticity, integrity and non-repudiation
- Properties of digital signatures
	- Authentic: cannot be forced and provides proof that the signer and no one else signed the doc
	- Unalterable: after signed, a document cannot be altered
	- Non-reusable: document signature cannot be transferred to another doc
	- Non-repudiated: signed document is considered to be the same as a physical document, cannot deny its validity

### Digital Signature standards 
- Digital Signature Algorithm
- Rivest-Shamir Adelman Algorithm
- Elliptic Curve Digital Signature Algorithm

### Code signing
Digital signatures are commonly used to provide assurance of the authenticity and integrity of software code - users can verify that code is legitimate.
Digitally signing code provides several assurances about the code.

- Code is authentic and sourced by the publisher
- The code has not been modified since it left the software publisher
- The publisher undeniably published the code, this provides non-repudiation of publishing


### Digital certificates
Equivalent to an electronic passport. Allows users, hosts and organisations to securely exchange info over the internet.
- Verifies identities between users in a transaction
- Provide assurance that published content has not been modified by any unauthorized actors
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

- PKI is most commonly used by website operators to assure visitors to their website that the website is trustworthy
- Provide key material to the SSL layer which permits traffic to/from the website and the end user to be exchanged in private (through encryption) and authenticated (through data authentication).

**TLS and PKI**
- TLS defines framework for the server and client to identify themselves and agree on an encryption standard and key. This identification process makes PKI possible through TLS
**X5O9**

- Standard defining the format of public key certificates.
- X.509 certificates are used in many Internet protocols, including TLS/SSL, which is the basis for HTTPS, the secure protocol for browsing the web.
- Authenticating and verifying the identity of a host or site
- When you click on the padlock displayed or check the trust mark the certificate chain details prove where the certificate is generated from.
- Enables the encryption of information exchanged via a website. When you encrypt data in transit, it that the sensitive information exchanged via the website cannot be intercepted and read by anyone other than the intended recipient. 

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
	- Attacker can analyse any chosen cipher texts together with their corresponding plaintexts, with the goal of acquiring the secret key
- Meet-in-the-middle method
	- A plaintext attack that reduces the number of brute-force permutations required to decrypt text that has been encrypted by more than one key, attacker encrypts plaintext using various keys to achieve an intermediate ciphertext


# Access control

## Access Control Models

- DAC: Discretionary access control
	- In DAC, each system object (file or data object) has an owner, and each initial object owner is the subject that causes its creation. Thus, an object's access policy is determined by its owner.
- MAC: Mandatory access control
	- Restricts the ability that individual resource owners have to grant or deny access to resource objects in a file system, method of limiting access to resources based on the sensitivity of the information that the resource contains and the authorization of the user to access information with that level of sensitivity.
- RBAC: Role-based access control
	- Organizations use RBAC to provide their employees w/ varying levels of access based on their roles and responsibilities (Accounting manager will have different privilege than a junior accountant)
- ABAC: Attribute-based- access contol
	- access decisions are made based on attributes (characteristics) about the subject or user making the access request, the resource being requested, what the user will do with the resource, and the environment (geolocation, network, etc.) or context of the of the request.
- RBAC: Rule-based access control
	- you’re focusing on the rules associated with the data’s access or restrictions. These rules may be parameters, such as allowing access only from certain IP addresses, denying access from certain IP addresses, or something more specific
- TAC: Time-based access control
	- Allow access based on a time period, during work hours 9am-5pm
- The principle of least privilege
	- user is given the minimum levels of access – or permissions – needed to perform his/her job functions.
- Privilege escalation: act of exploiting a bug, design flaw or configuration oversight in an operating system, or software application to gain elevated access to resources that are normally protected from an application or user

## AAA Framework

- Authentication: users and admins must prove who they are (username and password, id card w/ magnet, certificate, ssh key)
- Authorization: authorization services determine which resources the user can access and what operations they are permitted to perform (controlled by the server what can/ can't a user do)
- Accounting: accounting records hold info about- what the user does, what's being accessed, amount of time the resource is accessed, changes that are made 

## AAA Architecture
- Local AAA Authentication: sometimes known as self-contained authentication- it authenticates users against locally stored usernames/ passwords
- Server-Based AAA Authentication - authenticates against a central AAA server that contains the usernames/ passwords for all users
- LDAP: (Lightweight Directory Access Protocol) is a software protocol for enabling anyone to locate data about organizations, individuals and other resources such as files and devices in a over an internet protocol network -- whether on the public Internet or on a corporate Intranet

## AAA Protocols
- Remote Authentication Dial-in User Service (RADIUS): supports centralized authentication authorization and accounting management for clients that establish connection with a network and intend to use any of the provided services
- Terminal Access Controller Access Control System (TACAS)
- TACAS+: handles authentication, authorization, and accounting (AAA)

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

**Good Passwords**
- The longer the password the more difficult it is to crack
- Always use a combination of character, numbers and special characters
- Use a variety of passwords
- Don't keep a pattern between passwords

**Bad Passwords**
- Dictionary word
- Using personal information
- Using patterns
- Using character substitutions
- Using numbers and special characters only at the end
- Using common passwords
- Using anything but a random password


**Password Attacks and Defence**
- Attacks
	- Brute-force attack: submit many passwords in hope of eventually guessing the correct combination, systematically check all possible passwords
	- Rainbow Table attack: using a rainbow hash table to crack the passwords stored in a database system
- Defence
	- Salt technique prevents rainbow table attack
	- Key stretching, converting a password to a longer and more random key for encryption: hash password, then hash the hash of the password, hash the hash of the hashed password

## Token Authentication
A material device that is used to access secure systems
- Common forms include a dongle, card or RFID chip
- Tokens make it more difficult for hackers to access an account since they must have long credentials and tangible device itself which is much harder for the attacker to obtain

## Biometric Authentication

Advantages:
- Can be easily compared to authorized features saved in a database
- Can control physical access when installed on entrances and doors
- Can be added into multi-factior authentication process password + voice or token + face recognation

Types
- Facial recognition - e.g measuring distance between eyes, chin shape disadvantages: people who look alike, face at different angles, algorithm is not complex enough
- Fingerprint scanners - can even vein match (vascular biometrics)
- Voice identification - say a sentence or a word to authenticate
- Eye scanners - iris recognition, retina scanner - glasses can cause issues
- Keystroke dynamics- track typing

## Certificate-based Authentication
- Identify users, machines or devices using digital certificates
- An electronic document based on the idea of a passport
- Contains the digital identity of a user including a public key and the digital signiture of a certification authority
- Digital certificates prove the ownership of a public key issued by the certification authority
- To prove  ownership of pub key users provide dc when they sign into a server, server verifies credibility of the digital signature and CA and the server uses cryptography to confirm that the user has the correct private key associated with the  certificate.

## Multifactor Authentication

- Requires two or more independent ways to identify a user
- e.g codes generated from user's smartphone, fingerprints, facial recognition
- Increase the confidence of users as there are multiple layers of security
- Good defence against account hacks, but disadvantage: people may lose their phones or SIMs => can't generate an authentication code
- In vulnerability checker app we had username password and also captcha

## Authentication Protocols
- NTLM - suite of Microsoft security protocols intended to provide authentication, integrity and confidentiality to users
- KERBEROS - uses tickets to authenticate, uses symmetric key
- PAP - password authentication protocol (weak, vulnerable protocol)
- CHAP - challenge handshake authentication protocol
- Secure Sockets Layer (SSL)/Transport Layer Security (TLS) - client uses the servers public key to encrypt the data that is used to compute the secret key, server can only generate the secret key if it can decrypt the data with the correct private key.

# Web App Authentication

To associate an incoming request e.g HTTP

## Cookie-based authentication
- A small piece of data created by a server and sent to your browser when visiting a website
- Browsers often store and send the cookie back to the server to tell that the request is comming from the same browser to keep the user authenticated
	- Read browser cookies as key-value pairs

1. Client sends login request w/ credentials to backend server
2. Server validates credentials, if login successful web server creates a session in the database and include a set-cookie header on the response containing a unique ID in the cookie object
3. Browser saves cookie locally, as long as the user stays logged in, client must send the cookie in all the requests to the server
	- server then compares session ID stored in the cookie against the one in the database to verify validity
4. During logout, server makes the cookie expire by deleting it from the server

### Advantages of cookie-based authentication
- Using cookies in authentication makes the app stateful
	- Efficient in tracking/personalizing the state of a user
- Cookies are small in size => efficient to store them on the client side
- They can be HTTP-only => impossible to read on the client-side, improves protection against **Cross-site scripting** attakcs
- Cookies are added to the request automatically => developer does not have to implement them manually (less code)
- Client is given option to reject **non-essential cookies**, essential web authentication cookies cannot be rejected if you want access to site

### Disadvantages of cookie-based authentication
- Vulnerable to Cross-site request forgery attack
- Need to store session data in database, less scalable when site has many users at one time
- Client must send cookie on every request, even w/ URLs that don't need authentication for access

## Token-based authentication
- Tokens offer a second layer of security, and administrators have detailed control over each action and transaction.
- Used to store the user's state on the client machine
- The JSON Web Token (JWT) is an open standard that defines a way of securely transmitting info between a client and a server as a JSON object
- Anatomy of JWT token: 3 parts searated by dots
- Stateless, self contained object

header.payload.signature - do hashing for these values (SHA-256)

- User submits login credentials to backend server
- Upon request, server verifies credentials before generating an encrypted JWT w/ secret key and sends back to the client
- On client side browser stores the token locally using local storage, session storage or cookie storage
- On future requests, JWT is added to authorization header, and server will validate its signature by decoding the token before sending the response
- On logout operation, token on client-side is destroyed without server interation

### Advantages of token-based authentication
- Stateless, webserver does not need to keep a record of tokens as they are **self-contained** - server just need to sign tokens on successful login and verify incoming tokens in requests are valid.
- Can be generated from anywhere 

## Revoking cookies/json token
If you’re using a revocation list on your server to invalidate tokens, revoking a token can instantly boot the attacker out of your system until they get hold of a new token. While it is a temporary solution, it will make the attacker’s life slightly more difficult.
- Tokens are slightly less stateless now

# Penetration Testing (PenTesting)
An authorised, simulated attack on a system to evaluate the security of the system and its vulnerabilities.

- Is a method for gaining assurance in the security of an IT system
- By attempting to breach some or all of a system's security
- Using the same tools and techniques
- As an adversary might

## Cybersecurity colours
1. Blue team (the defenders): they are responsible for implementing defensive security damage control and incident response
2. Red red team (breakers/attackers): commissioned to perform "ethical hacking" on an organization, 
3. White team (admins): group responsible for refereeing an engagement between a red team of mock attackers and a blue team of actual defenders
4. Yellow team (builders): team responsible for developing the security system of an organization

## Hackers
1. Black hat hackers - attackers
2. White hat hackers - ethical hacker
3. Grey hat hackers - a hacker who may sometimes violate ethical standards but don't have malicious intent

## Testing colours
1. Whitebox testing: white hat hacker has full knowledge of the system being attacked
2. Blackbox testing: black-box testing refers to a method where an ethical hacker has no knowledge of the system being attacked. The goal of a black-box penetration test is to simulate an external hacking.
3. Greybox testing: internal structure of system is partially known.

## PenTesters

- They can be internal employees or a 3rd party penetration tester
- Should be performed by qualified and experienced staff only (can trust that they won't leak any info about your system)
- Pentests cannot be entirely procedural: exhaustive set of test cases cannot be drawn up => quality of a pen test is closely linked to the abilities of the pentesters 

## PenTesting objectives

- Vulnerability identification
- Scenario driven testing aimed at identifying vulnerabilities
- Scenario driven testing of detection and response capability


## PenTesting Scope

- Well-scoped penetration test can give confidence:
	- Products and security controls tested have been configured in accordance with good practice
	- No common/ publicly known vulnerabilities in the tested components at the time of the test

## PenTesting results
- Typically, pen tests are used to identify level of technical risk from software/hardware vulnerabilities
- Setting limits will affect the results: what techniques are used, what targets are allowed, how much knowledge of the system is given to the testers beforehand and how much knowledge of the test is given to system admins can vary within the same test regime

## PenTesting expiry
- A year or more to elapse between penetration tests, but vulnerabilities can pop up anytime in that period
- Not really a guaranteed expiry date (in reality it could be just a week)

## PenTesting startup point
- External network penetration test: an external network penetration test is typically what most people think of when talking about pentesting
- Internal network penetration test: simulates either the actions a hacker might take once access has been gained to a network, or those of an employess with access that they escalate

## PenTesting methods/target
- Physical penetration testing - tests show how a malicious actor might gain physical access to your facilities, perimeter security, intrusion alarms, motion detectors, locks, sensors, cameras, mantraps and other physical barriers to gain unauthorized physical access to sensitive areas.
- Social engineering penetration testing - identify weakness in a person, group of people: phishing, impersonation, leave a USB device containing malicious code, find passwords by looking at emplooyees' desks
- Web Application penetration testing - evaluate the development, design and coding of your website/web app to find any area that exposes sensitive customer info/ company data - e.g entering old password before being able to change password for an account
- Client side penetration testing - pentesting from client side usually for email clients, web apps 
	- Target specific employees/groups. Email carrying malicious payload or by pointing the victim to a malicious Web site. Exploit Required. Use Social Engineering. Convince a user to install your malware without using an exploit. Set up a phishing site targeting organization’s users. Large-scale client-side infection campaigns. Rely on victims to visit compromised Web sites that deliver client-side exploits
- Cloud security - a lot of services are on the cloud and you want to be able to protect those services, but you would need to notify cloud provider before doing pentests e.g AWS allows you to pentest the company's Application Programming Interface (HTTP/HTTPS), web applications hosted by the company, application server and stack (e.g programming languages python...), virtual machines/OS but AWS does not allow you to test Services/apps that belong to AWS e.g Infrastructure-as-a-Service, the physical hardware/underlying infrastructure or facility that belongs to AWS, EC2 environments belonging to other organisations.

## Blindness level
- Targeted(blindless) penetration testing - IT specialist that work within the org work with a specialist pentesting team - often called "lights-on" as all those involved know that the test is being carried out and also know when it starts and ends.
- Blind penetration testing - simulates a real cyber attackers, tester gets v. limited data before test takes place e.g company name/ website URL
- Double blind penetration testing - the IT/security team within the org are not warned about the test taking place, tests the security monitoring methods, the incident identification and response of the IT/cybersec specialists.

## PenTesting phases
- Pre-engagement interactions: prepare and plan, outline logistics of the test, objectives/goals of custerms they would like you to achieve and if there are any legal implications
- Reconnaissance: gather as much inteligence on the organization and the potential targets for exploit
- Scanning: attackers begin to start singling out possible areas of attack against their target 
- Threat modeling: mapping out potential threats: Where am I most vulnerable to attack? What are the most relevant threats? What do I need to do to safeguard against these threats?
- Exploitation: with a map of all possible vulnerabilities and entry points, pentester begins to test the exploits found within the network, applications and data
- Foothold installation: tester maintains continued control over the compromised system, establish a foothold by installing a persistent backdoor/ downloading additional utilities/malware to the system.
- Analysis and reporting: pentesters will give review of their findings and recommendations.
- Clean up and remediation


## Advantages/Disadvantages of pentesting

- **Adv**
	- Identify/resolve system vulnerabilites
		- Identify high-risk weaknesses that result from a combo or small vulnerabilities
	- Gain insights into your systems - reports provide specific advice on how to protect the system
- **Disadv**
	- If done incorrectly, servers can crash, sensitive data can be exposed, cruicial data can be corrupted
	- Must trust that the pentester won't abuse their role
	- Test conditions must be realistic - employees might prepare for the test whereas a genuine attack could happen at any point in ways that might be creative/ hard to plan for

## Reconnaissance
Discovering and collection info about a system

### Footprinting
The process of collecting as much info as possible about the target system, finding ways to penetrate the system

- Get an overview of the secuirty posture, the overall status of cybersecurity readiness (e.g firewalls)
	- Controls and processes you have in place to protect against cyber attacks
	- Ability to detect attacks
	- Ability to react and recover from security events
	- Level of automation in your security program
- Reduce attack area
- Identify vulnerabilities
- Draw network map

### OSINT Sources
Open source intelligence (OSINT) is the practice of collecting information from published or otherwise publicly available sources.
- Surface web
- Deep web, accessible through authentication
- Dark web

### OSINT Use cases

- Public civilian for basic knowledge, business and public opinions
- Governements for any national threat analysis/services
- Cybersecurity professionals
	- Cyber defence
	- Pentesters
	- Security analysis
	- Cybercrime groups

### OSINT Tools

- Domain and IP search
- Exposed data on the enterprise website
- Exposed data already on the internet
- Hidden data in files
- Connected devices search e.g webcams

#### WHOIS - domain info, identifies who owns a domain and how to get in contact with them
1. Who Is https://www.who.is
2. Domain Tools https://whois.domaintools.com/
3. ICANN lookup https://lookup.icann.org/
4. Central ops https//centralops.net/cokal
5. WHOIS Search https://main.whoisxmlapi.com/

DNSRecon (python script)
- Find DNS info with python
```bash
dnsrecon -D subdomains-top1mil-5000.txt -d spartaglobal.com -t brt > dns_recon_sparta.txt
```
- DNS information helps in mapping the network infrastructure of the target host.
- DNSRecon can perform enumerations:  the process of locating all the DNS servers and their corresponding records for an organization. DNS enumeration will yield usernames, computer names, and IP addresses of potential target systems. 

#### Google hacking and dorking 
- operator_name:keyword
- e.g
	- intitle:
	- inurl:
	- intext:
	- define:
	- site:
	- phonebook:
- Used to find security holes in the configuration and computer code tha websires are using
- Devices connected to the Internet can be found. A search string such as inurl:"ViewerFrame?Mode=" will find public web cameras.
- intitle:index.of followed by a search keyword. This can give a list of files on the servers. For example, intitle:index.of mp3 will give all the MP3 files available on various types of servers.

#### Harvester
- gather emails, subdomains, hosts, employee names, open ports and banners from different public sources like search engines and the SHODAN data base
- Intended to help pentesters in the early stages of pentests in order to understand the customer footprint on the internet
#### DShield

#### Virus total

#### FOCA

#### Metagoofil

#### Shodan

#### Wappalyzer - firefox add-on

#### crt.sh

#### Sublist3r

#### [OSINT Framework](osintframework.com)

# Scanning

Scanning is part of the reconnaissance phase in the Cyber Kill Chain
- But many PenTesting categorisations put it in a separate phase
- Scanning could be considered as footprinting

- Consider it separate:
	1. Consists of technical steps that require actions to be taken toward the target enterprise
	2. Needs legal prep to make sure action plan is legal

Scanning: set of procedures for identifying live hosts, ports, discovering OS and architecture of target system - identifying vulnerabilities and threats in the network.


## Network Scanning

Gathering information about a network to determine all active devices on it 
- Passive scanning
	- Silently analyse network traffic (packet sniffing) - identify endpoints and traffic patterns
	- No risk of disturbing the network (no intercepting)
	- e.g TCPDump, Wireshark
	- Limitations: 
		- Can't detect devices/applications that never communicate, they may still have vulnerabilities they will go unnoticed
		- Infected systems intentionally distribute misinformation
		
	
- Active scanning
	- Sending test traffic into the network and querying individual endpoints
	- Levels of active scanning
		- Host scanning
		- Port scanning
	- OS fingerprinting

## Host scanning

- Detect all active hosts on a network and mapping them to their IP addresses

- Address Resolution Protocol (ARP) scans:
	- ARP requests can be sent out to many IP addresses on a Local Area Network (LAN) to determine which hosts are up based on the ones that respond with ARP reply
- Internet Control Message Protocol (ICMP) scans:
	- Echo (ping) requests are used to detect if another host can be reached
	- Timestamp messages determine the latency between two hosts - the time it takes for data packets to be captured, transmitted, processed
	- Address mask requests discover the subnet mask in use on the network

## Port scanning 

- Sending packets to specific ports on a host and analysing the responses to learn details about its running services or potential vulnerabilities.
- Ports are classified as follows:
	- Open: the destination responds
	- Closed: destination received the request packet but responds with a reply that there is no service listening at the port
	- Filtered: request packet is sent but the host does not reply

- Port scanning methodology
	- Vanilla: scan all 65535 ports
	- Strobe: scan only known services/ports
	- Sweep: scan same ports on several machines

- Intrusion Detection System can detect these scans
	- Keep dely between port scans to prevent it looking suspicious and being flagged to admin, you can also send decoy traffic

### TCP Handshake
- Three-Way HandShake or a TCP 3-way handshake is a process which is used in a TCP/IP network to make a connection between the server and client. It is a three-step process that requires both the client and server to exchange synchronization and acknowledgment packets before the real data communication process starts.
- 3-way handshake to establish a reliable connection between a client and server: both sides synchronize (SYN) and acknowledge eachother (ACK)
1. SYN: client wants to establish connection with server => sends a segment with SYN (synchronise sequence number), informs server that client is likely to start communication 
2. SYNACK: server responds to client request with SYN-ACK signal bits. ACK signifies the response of segment it received and SYN signifies with what sequence number it is likely to start the segments with
3. ACK: client acknowledges the response of server and they both establish a reliable connection which they use to transfer data

- SYN Scan
	- Determine the state of a port without establishing a full connection
- ACK Scan
	- Determines whether a port is filtered or unfiltered
- TCP Connect Scan
	- Needs a full connection (SYN ACK) => more likely to log full TCP connection, trigger IDS
- NULL (no flag in header), FIN (fin flag set to 1), Xmas Scan 
	- Each results in a closed port, open or filtered port
- IDLE Scan

### UDP Scanning

TCP has a connection between sender/reciever
UDP does not have a connection

- Sends a UDP packet to various ports on target system and determine the availability of the host from the response
- Receiving a UDP response = port is open, ICMP port unreachable = closed port, no response could indicate that the port is either open or filtered by a firewall/packet filter

### OS Fingerprinting

- Determining the operating system used by a host on a network
	- IP TTL values: time to live in the IP header, the amount of time that a packet is set to exist inside a network before being discarded by a router
	- IP DF option: don't fragment, 
	- IP Type of Service (TOS)  
	- IP ID values (IPID sampling)
	- TCP Window size: The TCP receive window size is the amount of receive data (in bytes) that can be buffered during a connection. The sending host can send only that amount of data before it must wait for an acknowledgment and window update from the receiving host. 
	- TCP Options (TCP SYN and SYN+ACK packets - can have assigned values between OS)
	- Initial sequence number (ISN) sampling
	- DHCP requests: most OS’ DHCP clients will ask for DHCP options in a specific sequence.
	- ICMP requests: from layout of reply, if the ICMP reply contains a TTL value of 128 then it is a Windows machine, and if the ICMP reply contains a TTL value of 64 then it is a Linux-based machine.
	- HTTP packets
	- Running services
	- Open port paterns: Microsoft Windows machines often have TCP ports 135 and 139 open. Windows 2000 and newer also listen on port 445. Meanwhile, a machine running services on port 22 (ssh) and 631 (Internet Printing Protocol) is likely running Unix.

| Operating System                  | Time To Live | TCP Window Size |
|-----------------------------------|--------------|-----------------|
| Linux (Kernel 2.4 and 2.6)        | 64           | 5840            |
| Google Linux                      | 64           | 5720            |
| FreeBSD                           | 64           | 65535           |
| Windows XP                        | 128          | 65535           |
| Windows Vista and 7 (Server 2008) | 128          | 8192            |
| iOS 12.4 (Cisco Routers)          | 255          | 4128            |


## Hybrid scanning
- Use both active and passwive scanning helps you to gain an overview of the processes in the networks
- Active scanning should be used in small amounts, in extreme cases to avoid generating a large amount of traffic on the network
- Make sure you can discover more machines rather than just relying on one.
## Nmap
- Open source utility for network discovery, uses active scanning methods

### e.g nmap commands

- nmap -PR 172.25.0.0/16 ; ARP scan
- nmap -p2000-3000 172.25.1.101 ; scan range of ports

## Vulnerability scanning
Identifying potential vulnerabilities in network devices e.g firewalls, routers, switches, servers and applications - once vulnerabilities are found, they can be exploited by the pentester.
- Scan specifies set of ports on a remote host
- Tries to test the service offered at each port for its know vulnerabilities
- Automated
- Doesn't exploit the vulnerabilities
- Scope is business wide

### Vulnerability data-source
- Common Vulnerabilities and Exposures (CVE)
- Many public CVE sources
	- (https://cve.mitre.org/)
	- (https://nvd.nist.gov/vuln/search)
	- (https://www.cvedetails.com/)
	- (https://vuldb.com/)
	- (https://vulners.com/)
	- (https://owasp.org/www-pdf-archive/OWASP_Top_10-2017_%28en%29.pdf.pdf)

### Vulnerability categories
- Outdated software
- Misconfigured software
- Poorly developed apps
	- website attacks
	- mobile app attacks
- Cloud applications
- Data breach
- Vulnerabilities in shares of \\server\share over the SMB protocol
	- 	- SMB – protocol that’s used in sharing in windows system – e.g share folder on the internet – some ppL don’t put authentication when they share – hacker can access database on the server

### Vulnerability scanner types
- Network vulnerability scanner
	- Network-based vulnerability scanner, in simplistic terms, is the process of identifying loopholes on a computer’s network, or IT assets, which can be exploited by hackers and threat actors.
Read more at: https://www.appknox.com/blog/agent-based-and-network-based-vulnerability-scanning
- Wireless scanner
- Agent based scanners
	- Agent-based scanners make use of software scanners on each and every device; the results of the scans are reported back to the central server. Such scanners are well equipped to find and report out on a range of vulnerabilities.
- Web application scanner
- Database scanners

### Vulnerability scanning scheduling strategy

- Change based
	- based of software, hardware updates
- Hygeine based
	- best practices that an organisation undertakes, when there's something new in system e.g apps, OS updates look for new vulnerabilities
- Compliance based
	- comply with standard of organisation

### Running your scans
- Are you systems accessible to the scanner?
	- Firewalls
- Are any of your systems protected by an IPS/IDS or WAF?
	- Intrusion prevention system, intrusion detection system, web application firewall
- Do you need authentication?

### Nessus


### OpenVAS/GVM

### Burp Suite

### SQLMap
- sqlmap an open source penetration testing tool
- automates the process of detecting and exploiting SQL injection flaws and taking over of database servers

## Exploitation

### Exploitation catergories
- Known exploit: known to system/software developers
- Unknown exploits: no documentation 

### Exploit naming
Named by:
- Type of vulnerability they exploit (BOF - buffer overflow)
- Where they are local/remote exploits
- The result of running the exploit e.g DoS/ spoofing

### Exploit types
- Null or default passwords
	- Networking hardware can have default credentials
	- Admins sometimes create privileged user accounts in a rush and leave the password null
	- Wireless access points and preconfigured secure server appliances
- Network exploits
	- IP Spoofing - the creation of Internet Protocol (IP) packets which have a modified source address in order to either hide the identity of the sender, to impersonate another computer system, or both. Used predominately to launch DDoS and Man-In-The-Middle attacks aiming either to disrupt the delivery of network services or to steal sensitive data.
		- GitHub hit by a DDOS attack that was executed by spoofing GitHub's IP address and sending data to several servers.
	- Man-in-the-middle - attacker secretly relays and possibly alters the communications between two parties who believe that they are directly communicating with each other
		- e.g DNS spoofing spoofing is a technique that forces a user to a fake website rather than the real one the user intends to visit. If you are a victim of DNS spoofing, you may think you’re visiting a safe, trusted website when you’re actually interacting with a fraudster. The perpetrator’s goal is to divert traffic from the real site or capture user login credentials.
	- Firewall Traversal - strategy of bypassing firewalls which are commonly used to block access to certain sites and communication protocols.
	- ARP Poisoning - threat actor sends falsified ARP (Address Resolution Protocol) messages over a local area network. Results in linking of an attacker’s MAC address with the IP address of a legitimate computer or server on the network. Once the attacker’s MAC address is connected to an authentic IP address, the attacker will begin receiving any data that is intended for that IP address. ARP spoofing can enable malicious parties to intercept, modify or even stop data in-transit
		- The technique is often used to initiate further attacks, such as session hijacking or denial-of-service
	- WLAN 
		- Evil twin is a fraudulent Wi-Fi access point that appears to be legitimate but is set up to eavesdrop on wireless communications. The evil twin is the wireless LAN equivalent of the phishing scam. The US Department of Justice charged hackers within the Russian military agency with implementing evil twin attacks to steal credentials and malware targeting organizations such as anti-doping agencies, nuclear power operations, and chemical testing laboratories.
- Eavesdropping
	- Works mostly with plain text transmission protocols - HTTP
	- Remote attacker needs access to a compromised system
	- Prevent using cryptography
	- This process typically sees attackers exploit unsecured or open network communications and unencrypted data, which enables them to access data in transit between devices. Hackers can also eavesdrop by placing bugs on telephones, which allow them to intercept and record communication.

- Service vulnerabilities
	- HTTP-based services are vulnerable to remote command attack
		- Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application. Command injection attacks are possible when an application passes unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell
	- Services might have vulnerabilities e.g buffer overflow: 
		- Buffers are memory storage regions that temporarily hold data while it is being transferred from one location to another. A buffer overflow (or buffer overrun) occurs when the volume of data exceeds the storage capacity of the memory buffer. As a result, the program attempting to write the data to the buffer overwrites adjacent memory locations.
		-Attackers exploit buffer overflow issues by overwriting the memory of an application. This changes the execution path of the program, triggering a response that damages files or exposes private information. For example, an attacker may introduce extra code, sending new instructions to the application to gain access to IT systems.
		Buffer overflows can be used by attackers to crash a web-server or execute malicious code.	
	- Web server exploits
		- Session hijacking: compromises the session token by stealing or predicting a valid session token to gain unauthorized access to the web server.
			- Can be done through session sniffing, client-side attacks e.g malicious JavaScript attacks, man in the middle attack - alters communication between two parties who believe they are communicating with each other
		- SQL injection: malicious SQL statements inserted into a user input field this can destroy a data base or reveal information in tables such as usernames and passwords. 
			- SQL injection based on 1=1 is always true, entering 1234 OR 1=1 into a userid input equivalent to an SQL statement such as SELECT * FROM Users WHERE userid = 1234 or 1=1 revealing all rows in the table.
			- Use DROP TABLE in input could delete a particular table
			- Prevent by adding parameters to SQL queries, input validation,- pre-compiling an SQL statement so that you can then supply the parameters in order for the statement to be executed.
			- Use character-escaping functions for user-supplied input provided by each database management system (DBMS). This is done to make sure the DBMS never confuses it with the SQL statement provided by the developer.
		- Directory traversal: allows attacker to read arbitrary files on the server that is running an app - e.g app code/data, credentials for back-end systems, sensitive OS files. Can possibly write to these files, modifying app data/behaviour and possibly take control of the server.
		- Code injection: injecting code that is interpreted/executed by the app, lack of proper input/output data validation
		- Cross site scripting: malicious scripts are injected into trusted websites, the attacker can inject trojans into the website, capture users login credentials.
	- Prevent: admins should not runs services as the root user ()

- Host based vulnerabilites
	- Workstations and desktops are more prone to exploitation
	- Safeguards can be implemented e.g email client software does not automatically open or execute attachments
	- Automatic update of OS, software
- Denial of Service (DoS) attacks
	- Ping flood attacks:
	- Source packets usually forged
	- IDS intrusion detection sytem, IPS instusion prevention system, IDPs intrusion detection prevention

### Exploit kits
Tools embedded in compromised web pages
- Automatically scan a visitor's machine for vulnerabilities and attempt to exploit them 
- If exploit is successful, kit injects malware to the user's system

e.g
- Magnitude: attackers inject malicous code into adverts that redirects users to malicious websites, infects users with ransomeware (can encrypt files and delete file backups) with a focus on users in south korea also Taiwan and Hong Kong attackers behind it utilised CVE common vulnerabilities and exposures database as an exploit - modified and obscured it, also used elevation of privelege exploit
- exploit as a service

### Exploit databases
- [Exploit DB](https:www.exploit-db.com)
- [Rapid7](https://rapid7.con/db)
- (https://cxsecurity.com/exploit/)
- (https://www.vulnerability-lab.com/)

e.g Microsoft CVE-2021-31183
- Windows TCP/IP driver denial of service vulnerability - kernel driver

- The vulnerability allows a remote attacker to perform a denial of service (DoS) attack.
- The vulnerability exists due to insufficient validation of user-supplied input in the Windows TCP/IP Driver. A remote attacker can pass specially crafted input to the application and perform a denial of service (DoS) attack.

# Threat modelling
- Identifying what threats an organization, a target network or an in-scope application should be worried about.
- For pentesting
	- Modelling (mapping out)
	- The threats (things that can attack/harm)
	- To inform the types of activities conducted 
	- And to inform the risk of the vulnerabilites discovered

- After pentesting (organizations and blue teams)
	- apply countermeasures and mitigating controls to addess the dangers
- 3 questions to answers:
	- Where am I most vulnerable to attack?
	- What are the most relvant threats?
	- What do I need to do to safeguard against these threats?

## STRIDE, microsoft
Used to help reason and find threats.
Spoofing - Authentication| Impersonationg something or someone known and trusted
Tampering - Integrity| Modifying data on disk, memory, network 
Repudiation - Non-repudiation| Claim to not be responsible for an action
Information Disclosure - Confidentiality| Providing information to someone who is not authorised
Denial of Service - Availability| Denying or obstructing access to resources required to provide a service
Elevation of Privilege - Authorization| Allowing access to someone without proper authorization

## PASTA: Process for Attack Simulation and Threat Analysis
v 
PASTA gives an attacker-centric view of the system.
Phases:
1. Define objectives
2. Define Technical scope
3. Decomposition and analysis of application
4. Threat analysis
5. Vulnerabilities and weakness analysis
6. Analyze modelling and simulation
7. Risk and impact analysis 

## DREAD, microsoft
Focusses of determining the severity of a threat:
- Damage: impact of an attack
- Reproducibility: how easily can the attack be reproduced
- Exploitability: how easy it is to launch the attack
- Affected users: how many users will be impacted
- Discoverability: how easily can the vulnerability be found

# Digital Forensics Incident Response (DFIR)

- IR: structure methodology for handling security incidents, breaches and cyber threats
- Well-defined incident response plan (IRP) allows you to effectively identify, minimize the damage, and reduce the cost of a cyber attack, while finding and fixing the cause to prevent future attacks.

## Incident categorisation
- Malicious code: malware infection on the network, including ransomware
- Denial of Service: typically a flood of traffic taking down a website, can apply to phone lines, web-facing systems
- Phishing: emails attempting to convince someone to click on a link/atttachment
- Unauthorised access: access to systems, accounts, data by an aunauthorised person - e.g access to someone's emails/ account
- Insider: malicious/ accidental action by an employee causing a security incident
- Data breach: lost/stolen devices or hard copy documents, unauthorised access or extraction of data from the network
- Target attack: attack specificaly targeted at the business- usually by a sophisticated attacker (often encompasses the above categories)

## Severity matrix

- Critical:
	- Over 80% of staff/several critical staff/teams unable to work
	- Critical systems offline without a known resolution
	- High risk to/ definite breach of sensitive client or personal data
	- High financial impact
	- Severe reputational damage - likely to impact business long term
- High:
	- 50% of staff unable to work
	- Risk of breach of personal/sensitive data
	- Non-critical systems affected, or critical systems affected with known (quick) resolution
	- Financial impact
	- Potential serious reputational damage
- Medium
	- 20% of staff unable to work
	- Possible breach of small amounts of non-sensitive data
- Low
	- Minimal impact
	- One or two sensitive non-crital machines affected, <10% of non critical staff affected temporarily

### IR steps
1. Preparation
	- Has everyone been trained on secuity policies?
	- Have your security policies and indiced response plan been approved by management?
	- Does the IR team know their roles and the required notifications to make?
	- Have all incident response team members participate in mock drills?
2. Identification
	- When did the event happen?
	- How was it discovered?
	- Who discovered it?
	- Have any other area been impacted?
	- What is the scope of the compromise?
	- Does it affect operations?
	- Has the source (point of entry) of the event been discovered?
3. Containment
	- What has been done to contain the breach short term
	- What's been done to contain the breach long term
	- Has any discovered malware been quarantined from the rest of the enviroment? - Unplug devices, isolate infected section of network
	- What backups are in place?
	- Does remote access require true multifactor authentication
	- Have all access credentials been reviewed for legitimacy?
	
4. Eradication
	- Have artifacts/malware from the attacker been securely removed?
	- Has the system been harderened, patched and updates applied?
	- Can the system be re-imaged? - before infected version

5. Recovery
	- When can systems be returned to production?
	- Have systems been patched, hardened and tested?
	- Can the system be restored from a trusted back-up
	- How long will the affected systems be monitored and what will you look for when monitoring
	- What tools will ensure similar attacks will not reoccur? (File integrity monitoring)
6. Post-incident activity
	- What changes need to be made to the security?
	- How should employee be trained differently?
	- What weakness did the breach exploit?
	- How will your 
- Emergency contact/commincations list
- At least one conference number
- Escalation criteria
- System backup and recovery process list
- Forensic analysis list
- Jumpbag list
- Security policy review list

### Playbook

## Digital Forensics
### Computer Forensics
Analysing and collecting info for:
- Computer systems
- Embedded systems
- Static memory e.g USB pen drives
- Includes reporting the results

### Mobile Device Forensics
- Mobile device forensics collect data from mobile devices
- Mobile devices are diffrent from computers as they have inbuild communication systems such as GSM
- Data retrieved from movile devices includes

### Network Forensics
- Involves capturing and analysisng network traffic and network packets over local and wide area networks (or internet)
- The analysis also covers intrusion detection
- Network data are often considered as a proactive investigation element, uses 2 systems to collect data:
	- Catch it as you can
	- Stop look and listen

### Database Forensics
- Study of databases and its metadata
- Analyses:
	- database content
	- log files
	- in-RAM data to recover pieces of digital evidence or to buld a timeline

### Forensic Data Analysis
- Covers the investigation of financial crimes associated with structured data - data from application systems or their databases
- Primary motive of 

### Email Forensics
- Email header analysis
- Email server analysis
- Investigation of network devices
- Sender mailer fingerprints
- Software embedded indentifiers
- Bait tactics

### Cloud forensisc
- The application of digital forensics in cloud computing as a subset of network forensics to gather and preserve evidence in a way that is suitable for presnetation in a court of law
- Cloud forensic is the amalgamation of all different forensics
- Involves interactions amongst various cloud actors
	- Cloud providers
	- Cloud

### Digital Forensic Phases
1. Phase I - first response: what is done after security incident takes place, dependent on nature of attack
2. Phase II- search and seizure
3. Phase III - collect the evidence
4. Phase IV - secure the evidence
5. Phase V - data acquisition
6. Phase VI - data analysis

## OWASP Top 10 security risks

xml external entities - markup language for encoding documents in a readable format

Attackers can exploit XML proceesors if they can upload XML or include hostile content in an XML document
to exploit vulnerable code, dependencies and integrations - these vulnerabilities can be used to extract data, 
execute remote requests from the server, scan internal systems, perform a DOS attack

Apps and XML-based web servies can be vulnerable to attack if:
The app accepts XML directly or XML uploads from untrusted sources or inserts untrusted data into XML - similar to json docs
which will be passed to the XML processor
To prevent this from happening: 
use less complex data formats e.g JSON and avoid serialization of sensitive data
Upgrade all XML processors and libraries in use by the application or on the OS
Disable XML external entity and document type definitions processing

exploitability 2, prevealence 2, detectibility 3, technical 3
average, common, average, easy, severe

Example Attack Scenarios
Numerous public XXE issues have been discovered, including attacking embedded devices. XXE occurs in a lot of unexpected places, including deeply nested dependencies. The easiest way is to upload a malicious XML file, if accepted:
Scenario #1: The attacker attempts to extract data from the server:
  <?xml version="1.0" encoding="ISO-8859-1"?>
    <!DOCTYPE foo [
    <!ELEMENT foo ANY >
    <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
    <foo>&xxe;</foo>
Scenario #2: An attacker probes the server's private network by changing the above ENTITY line to:
   <!ENTITY xxe SYSTEM "https://192.168.1.1/private" >]>
Scenario #3: An attacker attempts a denial-of-service attack by including a potentially endless file:
   <!ENTITY xxe SYSTEM "file:///dev/random" >]>

<!DOCTYPE test [<!ENTITY list SYSTEM "file:/">]>
cross site scripting
allows attakers to inject client-side scripts into web pages viewed by other users
- automated tools can detect this vulnerability and exploit XSS
- this can be used to perform remote code execution on the victim's browser e.g stealing credentials, or delivering malware to them
- 3 forms of XSS that target user's browers
reflected xss - the app includes unvalidated and unescaped user input as part of HTML output
- if successful the attacker can execture arbitrary HTML and JavaScrips in the victims browser - the user 
usually must click on a malicious link that is an attacker-controlled page e.g malvertisment
- Stored xss: app/api stores unsanitised user input that is viewed later by another user/admin - attacker might
enter malicious script into a user input field, when the infected page is opened by the victim - the XSS attack
payload is served as part of their HTML code and results in the victim executing the malicious script
once the page is viewed
- DOM xss Javascript frameworks and APIs that dynamically include attacker-controllable data to a page are
vulnerable to DOM xxs
if the web app's client side scripts write data provided by the user to the Document object model(dom)
data is read from the DOM by the web app and outputted to the browser
when data is incorrectly handled, and inject a payload
to prevent use frameworks that automatically escape XSS by design e.g the latest React JS
, escape untrusted HTTP request data based on the context in the HTML output (body, JavaScript, the URL

exploitability: 3, prevalence 3, detectability 3, technical 2
easy, widespread, easy, moderate

e.g in input forms:
- <script>alert(123)</script>
- ><script>alert(document.cookie)</script>


OWASP Juice shop insecure web application that contains hacking challenges where the user exploits the vulnerabilities.

# Cyber Threat Intelligence & MITRE ATT&CK

## MITRE ATT&CK: global.y-accessible knowledge base of advesary tactics and techniques based on real-world observations of cybersecurity threats
- Adversarial Tactics, Techniques & Common Knowledge (ATT&CK)
- Knowledge base of adversary behaviour
- Free, open and globally accessible
- Based on real-world observation
- Focus on: Tactics, Techniques & Procedures
- Use Knowledge of adversary to help defenders
- Shift from indicators to behaviours
- Use a common knowledge
pyramid of pain img

### Mapping ATT&CK to CTI
1. Understand ATT&CK
2. Map data to ATT&CK
3. Store and analyse
4. Defence recommendation

### Mapping to ATT&CK
1. Find behaviour
	- Check what adversary/software does
	- Analyse initial compromise and post-compromise
	- e.g running a command (ifconfig), creating a foothold/task, establishing a connection, sending data
2. Research behaviour
	- Consult other teams (red team, blue tea)
	- Search on the internet
	- Academic and secuirty-focus journal and reports
	- Time-consuming task but builds the knowledge
	- e.g protocol used, port used, command used
3. Map behaviour to a tactic on MITRE ATT&CK
	- What is adhersary trying to accomplish?
	
4. Find technique
	- Technique is a special behaviour to achieve a goal and often a single step
	- Toughest part
	- Behaviour might not be a technique
	- Search MITRE ATT&CK (keywords, commands, etc)
5. Compare results
	- Different interpretation for analysing same situation/ case - normal as analysts have bias (based on their knowledge and expertise)
	- Discuss results

- Work from finished report or raw data

### Mapping to ATT&CK from raw data
- More data available at procedure level
- Working on case from scratch (without someone else's bias)
- Needs great technical knowledge

1. Find behaviour
- Similar to find behaviour step in mapping
- Behaviour found by analysing data

2. Research the Behaviour
- May require expertise in specific domain e.g:
	- Digital forensics - analyse without corrupting evidence
	- Specific OS
	- Specific network devices
	- Specific data types: jpeg, mp3

- May require multiple data sources or context
- May require consulting/interviewing other team members
- Researching similar cases

3. Translate behaviour into a tactic


4. Find the technique
- Think about concurrent techniques (pairs):
	- Data compression (exfiltration) + data encryption (exfiltration)
	- Spearphishing attachment (initial access) + user execution(execution)
	- Data from local system (collection) + email collection (collection)
	- Process delivery (discovery) + command line

5. Compare the results
- Need several analyst with different sets of expertise
- Different interpretation for analysing same situation/case
- Discuss results

### Mapping from report vs raw data
TABLE
Step Report/Finished Raw
Find the behaviour
Research the behaviour
Behaviour -> Tactic
Find technique
Compare the results
## Recommendations
1. Determine Priority techniques
2. Research how techniques are being used 
3. Research defensive options related to techniques
4. Research organisational capability/constraints
5. Determine what tradeoff are for the organisation on specific points
6. Make recommendations

https://mitre-attack.github.io/attack-navigator/
