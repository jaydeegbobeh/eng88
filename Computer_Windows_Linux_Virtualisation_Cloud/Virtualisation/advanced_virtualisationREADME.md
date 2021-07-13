# Virtulisation for Software Development

Virtualisation allows you to create an environment similar to the environment of production.

## Vagrant 

Vagrant is an open source software for building and maintaining portable virtual software development environments - an automation tool.
	- Allow you to manage virtual machines
	- If you're developing several project, Windows, MacOS, Linux. You have to install different types of VM software and switch between environments, vagrant helps you to access all of them by openinng them in a terminal.

Synced folders enable Vagrant to sync to a folder on the host machine to the guest machine.
	- Allows you to continue working on your project files on your host machine, whilst using the resources in the guest machine to compile the project.

###Vagrant set-up

**create a vm**

**initialize a vm**
vagrant init your_folder - the folder that contains vagrant file

**start a vm**
vagrant up

**stop a vm**
vagrant stop

**reload vm**
vagrant reload

### Connect to vm

**using ssh to connect to vm**
vagrant ssh

### Vagrantfile

The function of the Vagrantfile: describes the machine required for a project, and how to configure the machines. Vagrant runs with one Vagranfile per project.

## Docker

Docker enables developers to easily create, deploy and run applications as a lightweight, portable, self sufficient container which can run virtually anywhere.

### Containerisation

- A **container** is a standardised unit of software - containers are based on an image.
- Containers allow a developer to package up an app with all the parts it needs (libraries/ code/ dependencies) and deploy as a package.
- This ensures the application runs quickly and reliably from one computing environment to another.


Docker images become contaiers when they run on Docker engine.
- Docker containers that run on Docker Engine are:
	- Standard: portable anywhere
	- Lightweight: share the the machines OS system kernel, so they don't require an OS per application. This makes Docker efficient and reduces server/ licensing costs.
	- Secure: applications are safer in containers.


### VM vs Docker
- Container shares OS with host but with VM the host can be anything. Containers must run on the same OS.

### Advantages of containerisation
- Consistent and isolated environment
- Cost effective and fast development
- Containers allow you to cap resources when running multiple servers
- Able to run anywhere, provided its is targeted at the OS 

### Disadvantages of containerisation
- Security: as the container shares resources, malware can escape from the container to the host.

### Docker commands
e.g in Linux terminal

**docker run it ubuntu bash**
**uname -a** : gives system version
**docker ps -a** : lists all containers
**docker images** : shows all top level images, their repository and size.
**docker start xxx** : start containter with first 3 characters of their id
**docker exec -it xxx*: execute a command on a running terminal
**docker stop** : app stops gracefully
**docker kill** : terminates immediately
