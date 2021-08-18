# DevOps with AWS

## EC2 (Elastic Compute Cloud) instance: a virtual server in EC2 cloud
- A web service that provides; secure, resizable computer capacity in the cloud, designed to make web-scale cloud computing services easier: with choice of processor, storage, networking, operating system.


## AMI
- Provides the information required to launch an instance
- Contains an operating system (Linux, Unix, Windows) , application server (containers: mysql server, phpmyadmin server) and applications - software configuration, contains launch permissions that control which AWS accounts can use the AMI to launch instances

## Key pairs
- Security credentials: key pair (public key and private key) that use you to prove your identity when connecting to EC2 instance. Amazon EC2 stores the public key on your instance, you store the private key. 
- For Linux instances private key allows you to securely SSH into your instance, SSH establish secure remote access to server, remote computer

## S3 (Simple storage service)
- Storage sevice, built to store and retrieve any amount of data, anytime, anywhere on the web
- Bucket: container for objects stored in S3
- Object: entities that is stored in S3 bucket, consits of object data/ metadata
- Key: unique identifier for object within bucket
- Attach a S3 sevrer to an EC2 instance so that if we ever destroy the instance all the data will be saved.

## Regions
- AWS has several regions (physical location around the world where amazon clusters data centres) where you can create resources: each region has several availability zones (consists of one or more data centres at a location within an AWS region - each AZ has independent cooling, power and physical security
- If app is partitioned accross AZs, companies are better isolated/ protected from power outages, natural disasters (AZs within a region are separated within 100km from each other)
- Pick region (and AZ) thats geographically close to company/ customers:  lowest network latency and quickest response

## AWS Virtual Private Cloud (VPC)
VPC is the networking layer for Amazon EC2 and enables launching AWS resources into a virtual network that you've defined.
- Subnet: the range of IP addresses in your VPC/ virtual network
- Route table: set of rules (routes)determines where network traffic is directed - routes to particular network destinations
- Internet gateway = gateway you attach to your VPC to enable communication between resources (VPC and internet)
- VPC endpoints enables private connections between your VPC and AWS services e.g a S3 bucket (gateway)
- CIDR block: how you define subnet mask, specify the range of IP addresses for the VPC


## AWS Security Group
Security group acts as a virtual firewall for EC2 instances, controls incoming/ outgoing traffic from your instance
- Inbound rules control incoming traffic to your instance and outbound rules control outgoing traffic to instance - ACL (Access Control List)
- Add rules to security group: for example, an instance that's configured as a web server needs security group rules that allow inbound HTTP and HTTPS access. 
- Likewise, a database instance needs rules that allow access for the type of database, such as access over port 3306 for MySQL, inbound rules that allow SSH access over port 22

## Manual deployment
- Create an ec2 instance
- ssh into ec2 instance in shell
- Install docker on ec2 instance
- Run docker image in instance, access from port 80
	- docker run -p 80:5000 /web-calculator:3


