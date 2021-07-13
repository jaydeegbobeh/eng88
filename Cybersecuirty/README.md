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
- Human factors
- Policies and practices
- Technology

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

- Reconnaissance(choose target, identifiy vulnerabilities)
- Weaponization(create malware weapon like a virus to exploit the vulnerabilities for the target)
- Delivery(transmitting the weapon to the target e.g USB drive, email attachment)
- Exploitation(program code of malware is triggered, exploiting the target's vulnerability)
- Installation(malware installs an access point for intruder- a backdoor)
- Command and control(malware gives intruder access in the network/system)
- Actions on objective(once attacker gains persistent access, they fufill their purpose e.g encryption for ransom);


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
	- ADD STUFF HERE   units of plaintext are replaced with the ciphertext
- Transposition cipher
	- No letters are replaced; simply rearranged
	- Key for transposition cipher (e.g rail fence cypher key=3 encrypt by text in 3 diagonal rows)
- Caesar cipher
	- replace each plaintext letter with a different one a fixed number of places down the alphabet

## Encryption classes

Two classes of encryption used to provide data confidentiality- differ in how they use keys
1. Symmetric encryption algoriths: encryption algorithms that use the same key to encrypt and decrypt data
	- Used in: payment applications, validations to confirm that the send of a message is who they claim to be
	- **Block cipher**: encryption is completed in 64 bit blocks, 
	- **Stream cipher**: encryption is one bit at a time
	- example: Advanced Encryption Standard, key size: 128, 192, 256
	- Symmetric encryption is commonly used as it uses less resources (less bits), it also has the advantage of speed (useful for online banking)
	- Initialisation vector

2. Asymmetric encryption algoriths: use different keys to encrypt and decrypt data
	- Use public key (encryption) and private key (decryption)
	- Less than 1024 bits is not recommended
	- Alogrithms e.g Diffie-Hellman 512,1024, 2048, 3072, 4096 key length, Digital Signature Standard 512-1024 key length
- Asymmetric Encryption for confidentiality
	- public key (encrypt) + private key(decrypt) = confidentiality
- Asymmetric Encryption for authentication
	- private key (encrypt) + public key(decrypt) = authentication - ensure message is coming from someone with the correct private key, integrity of message - it has not been changed


### Diffie-Hellman
- An asymmetric mathematical algorithm
- Allows two computers to generate an identical shared secret w/out having communicated before
- New shared key is never actually exchanged between the sender and receiver
- Uses
	- Data exchanged using an IPsec VPN
	- Data is encrypted on the internet using SSL/TLS
	- SSH data is exchanged

## RSA algorithm
ADD STUFF 
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

Hashes are used to verify and ensure data intergrity
Based on one-way maths funct - easy to compute but v. hard to reverse this calc
Can be used to verify authentication

Aritrary length text --> Hash function --> Hash value

### Well known Hash functions
1. Message Digest 5 (MD5)
2. Secure Hash Algorithm 1 (SHA-1) - SHA-256
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
	- Non-repudiated: signed document is considered to be the same as a physical document, cannot deny its validity

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

XFO9

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
	- A plaintext attack that reduces the number of brute-force permutsations required to decrypt text that has been encrypted by more than one key, attacker encrypts plaintext using various keys to achieve an intermediate ciphertext


# Access control


## Access Control Models

- DAC: Discretionary access control
	-
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
- Secure Sockets Layer (SSL)/Transport Layer Security (TLS) - client uses the servers public key to encrypt the data that is used to compute the secret key, server can only generate the secret key if it can decrypt the data with the correct private key.


# Web App Authentication

To associate and incoming request e.g HTTP

## Cookie-based authentication
- A small piece of data created by a server and sent to your browser when visiting a website
- Browsers often store and send the cookie back to the server to tell that the request is comming from the same browser to keep the user authenticated
	- Read browser cookies as key-value pairs

1. Client sends login request w/ credentials to backend server
2. Server validates credentials, if login successful web server creates a session in the database and include a set-cookie header on the response containing a unique ID in the cookie object
3. Browser saves cookie locally, as long as the user stays logged in, cliend must send the cookie in all the requests to the server
	- server then compares session ID stored in the cookie against the one one in the database to verify validity
4. During logout, server makes the cookie xpire by deleting it from the server

### Advantages of cookie-based authentication
- Using cookies in authentication makes the app stateful
	- Efficient in tracking/personalizing the state of a user
- Cookies are small in size => efficient to store them on the client side
- They can be HTTP-only => impossible to read on the client-side, improves protection against **Cross-site scripting** attakcs
- Cookies are added to the request automatically => developer does not have to implement them manually (less code)
- Client is given option to reject **non-essential cookies**, web authentication cookies cannot be rejected if you want access to site

### Disadvantages of cookie-based authentication
- Vulnerable to Cross-site request forgery attack
- Need to store session data in database, less scalable when site has many users at one time
- Client must send cookie on every request, even w/ URLs that don't need authentication for access

## Token-based authentication
- Used to store the user's state on the client machine
- The JSON Web Token (JWT) is an open standard that defines a way of securly transmitting info between a cliend and a server as a JSON object
- Anatomy of JWT token: 3 parts searated by dots
- Stateless, self contained object

header.payload.signature - do hashing for these values (SHA-256)

- User submits login credentials to backend server
- Upon request, server verifies credentials before generating an encrypted JWT w/ secret key and sends back to the client
- On client side browser stores the token locally using local storage, session storage or cookie storage
- On future requests, JWT is added to authorization header, and server will validate its signature by decoding the token before sending the response
- On logout operation, token on client-side is destroyed without server interation?

### Advantages of token-based authentication
- Stateless, webserver does not need to keep a record of tokens as they are **self-contained** - server just need to sign tokens on successful login and verify incoming tokens in requests are valid.
- 
-

## Revoking cookies/json


# Penetration Testing (PenTesting)
An authorised, simulated attack on a system to evaluate the security of the system and its vulnerabilities

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
3. Grey hat hackers - a hacker who may sometimes violate ethical standards but don't hve malicious intent

## Testing colours
1. Whitebox testing: white hat hacker has full knowledge of the system being attacked
2. Blackbox testing
3. Greybox testing


## PenTesters

- They can be internal employees or a 3rd party penetration tester
- Should be performed by qualified and experienced staff only (can trust that they won't leak any info about you system)
- Pentests cannot be entirely procedural: exhaustive set of test cases cannot be drawn up => quality of a pen test is cosely linked to the abilities of the pentesters 


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
-

## PenTesting expiry
- Not common for a year or more to elapse between penetration tests
-

## PenTesting startup point
- External network penetration test: an external network penetration test is typically what most people think of when talking about pentesting
- Internal network penetration test: simulates either the actions a hacker might take once access has been gained to a network, or those of an employess with access that they escalate


## PenTesting methods/target
- Physical penetration testing
- Social engineering penetration testing - identify weakness in a person, group of people: phishing, impersonation, leave a USB device containing malicious code, find passwords by looking at emplooyees' desks
- Web Application penetration testing - evealuate the development, design and coding of your website/web app to find any area what exposed sensitive customer info/ company data
- Client side penetration testing -
- Cloud security

## Blindness level
- Targeted(blindless) penetration testing - 
- Blind penetration testing -
- Double blind penetration testing

##
PenTesting phases
- Pre-engagement interactions
- Reconnaissance: gather as much inteligence on the organization and the potential targets for exploit
- Scanning:
- Threat modeling: mapping out potential threats: Where am I most vulnerable to attack? What are the most relevant threats? what do I need to do to safeguard against these threats?
- Exploitation: with a map of all possible vulnerabilities and entry points, pentester begins to test the exploits found within the network, applications and data
- Foothold installation
- Analysis and reporting
- Clean up and remediation


## Advantages of pentesting

## Disadvantages of pentesting


## Reconnaissance
Discovering and collection info about a system

### Foorprinting
The process of collecting as much info as possible about the target system, finding ways to penetrate the system

- Get an overview of the secuirty posture, the overall status of cybersecurity readiness (e.g firewalls)
	- Controls and processes you have in place to protect against cyber attacks
	- Ability to detect attacks
	- Ability to react and reocver from security events
	- Level of automation in your security program
- Reduce attack area
- Identify vulnerabilities
- Draw network map

### OSINT Sources
- Surface web
- Deep web
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
- Connected devices search

#### WHOIS - domain info
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

#### Google hacking and dorking 
- operator_name:keyword
- e.g
	- intitle:
	- inurl:
	- intext:
	- define:
	- site:
	- phonebook:

#### Harvester

#### DShield

#### Virus total

#### FOCA

#### Metagoofil

#### Shodan

#### Wappalyzer - firebox add-on

#### crt.sh

#### Sublist3r

#### [OSINT Framework](osintframework.com)




