# What is terraform?

An open source infrastructure as code IaC software tool that allows DevOps engineers to programmatically provision the physical resources an application requires to run
IaC manages an applications underlying IT infrastructure through programming
A popular automation tool

Allows developers to logically manage monitor and provision resources rather than manually configuring each required resource
Terraform parses the code ansd translates it into an app program

It has four major commands
terraform init : initialize a working directory containing Terraform configuration files
terraform plan : creates an execution plan
terraform apply : executes actions in plan
terraform destroy : destroy all remote objects 


A tool for building, changing and versioning infrastructure safely and efficiently
Can manage existing service providers

It works with AWS - Terraform can automate launching an EC2 instance, creating S3 bucket, creating an IAM (Identity and Access Management) group and policy - permissions set for users.


## Creating an EC2 instance with Terraform

terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "eu-west-1"
}
resource "aws_default_vpc" "yourname_web_server_vpc_tf"{

}

data "aws_subnet_ids" "yourname_web_server_subnet_tf"{
  vpc_id = aws_default_vpc.yourname_web_server_vpc_tf.id
}
resource "aws_security_group" "yourname_web_server_security_group_tf" {
   name = "yourname_web_server_security_group"


   ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   }

   ingress {
    from_port = 22
    to_port = 22
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
   }

   egress {
    from_port = 0
    to_port = 0
    protocol = -1
    cidr_blocks = ["0.0.0.0/0"]
   }
}
resource "aws_instance" "web-server-instance" {
  ami = "ami-0f89681a05a3a9de7"
  instance_type = "t2.micro"
  subnet_id = tolist(data.aws_subnet_ids.yourname_web_server_subnet_tf.ids)[0]
  associate_public_ip_address = true
  key_name = ""
  vpc_security_group_ids = [aws_security_group.yourname_web_server_security_group_tf.id]
}

In shell:
terraform validate
terraform plan
terraform apply
terraform show
ssh ec2-user@dnsname




ami - ami-id
instance type - t2 micro
key-name ssh-key
subnet-id - vpc_id takes first subnet - vpc is the virtual private cloud created for your server - id is not static => can't define it, it's given to you when you create it (dynamic)
security-group - vpc id
subnet and security group are given from the vpc_id

## Configuration as a code