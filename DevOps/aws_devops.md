# DevOps with AWS

## AWS Virtual Private Cloud (VPC)
VPC is the networkig layer for Amazon EC2 and enables launching AWS resources into a virtual network

## AWS Security Group
Security group acts as a virtual firewall for EC2 instances, controls incoming/ outgoing traffic from your instance

## Manual deployment
- Create an ec2 instance
- ssh into ec2 instance in shell
- Install docker on ec2 instance
- Run docker image in instance, access from port 80
	- docker run -p 80:5000 jaydeegb23/web-calculator:3


