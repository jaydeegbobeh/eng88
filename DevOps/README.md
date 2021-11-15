# Devops
## IT before DevOps
- Software Develpoment Team
- Wall Team - space inbetween representing confusion misalignment and stress
- Quality Assurance Team
- System Engineering Team

## Application Design Patterns
- Monolith 
Traditional unified model for the design of a software program, software is composed all in one piece.
- N-tier (Front and back end)
Separates the concerns between the visual elements of the app that the user will interact with (front end) and the building of the structure of the app (back end).
	- Front end - in which the user will see and deal with.
	- Back end – you have the software that will serve on the server and the database. This is where the DevOps team are.
- Microservice
Consists of a collection of small, autonomous services, each service is self-contained.
- Advantages	
	- Microservices are deployed independently => easy to manage bug fixes and feature releases
	- Compared to monolithic application, code dependencies can become tangled adding a new feature requires editing code in many places, in a microservice you don't share code or data stores, minimising dependencies making it much easier to add new features.
	- You can use different technologies that fit your microservice
	- If a microservice becomes unavailable this does not distrupt the entire app
	- Microservices can be scaled independently from each other
- Disadvantages
	- There are lots of moving parts compared to monolithic applications, the system is more complex
	- Teams may use many different languages/frameworks meaning the app as a whole is difficult to maintain

## Challanges in new Software Development Life Cycle
- Ease of use
- Flexibility 
- Robustness
- Cost

## What is DevOps?
A term related to enterprise software development
Developers & Testers + IT Operations = DevOps

- Collaboration of Development and Operations
- A culture which promotes collaboration between Development and Operations teams to deploy code to production faster in an automated & repeatable way.
- An approach through which superior quality software can be developed quickly and with more reliability

## CAMS Model

- Culture: intersction of people and groups is driven by behavior, change the business culture by sharing responsibilty and getting teams on the same page is a major goal (e.g using agile)
- Automation: save time, effort and money - speed up the flow of information
- Measurement: continuous improvement process is at the heart of DevOps, but in order to know how something has improved you **measure** the response time of the system for example
- Sharing: visibility, transparency, transfer of knowledge


## DevOps Principles
1. Customer-Centric Action - focus on the customers needs
2. End-To-End Responsibility - provide performance support from the beginning to the end of the life cycle
3. Continuous Improvement
4. Automate everything - everything as code: testing, application environment, version control
5. Work as one team
6. Monitor and test everything

## Stages in DevOps Lifecycle
- Continuous Development
- Continuous Testing
- Continuous Integration
- Continuous Deployment
- Continuous Monitoring

## Risk Register
- Description of risk (developer environment broken, testing server broken, automated testing broken)
- Chance of its occurence
- Potential damage (developers cannot work, new code cannot be tested, testing cannot be automated)
- Risk rating (low, medium, high)

## Skills required
- Be an excellent Sysadmin
- Deploy virtualization
- Hands-on experience in network and storage
- Knowledge of coding goes a long way
- Soft skills
- Understand automation tools
- Knowledge of testing
- Knowledge of security aspects
For DevSecOps you must understand the application of cybersecurity to these.

## CI/CD

**Continuous intergration and continuous delivery**
Continuous intergration - implementing small changes and check in code to version control repositories frequently
	- run automatic code quality scans on it and generate a report of how well latest changes adhere to good coding practices
	- build code and run any automated tests that you might have written to make sure changes don't break functionality
	- generating test coverage reports to observe how thorough automated tests are

Continuous delivery - automate software release but final step of approving and initiating a deploy to production is done manually
Continuous deployment - automating the deployment of applications to selected infrastructure environments
- doing so in short cycles
- Code done -> unit tests -> integrate -> acceptance test -> deploy to production (each step is automated)

- Jenkins is a CI/CD server, facilitates CI/CD by can buiding, testing and deploying software.
- You can set up Jenkins to watch for any code changes in places e.g GitHub and automatically do a build.
- You can utilize container technology such as Docker, initiate tests and then take actions like rolling back/forward in production.
	
- Terraform CI,  a tool for building, changing, and versioning infrastructure safely and efficiently. Terraform can manage existing and popular service providers as well as custom in-house solutions

- Docker
- Run unit tests as part of your docker build command by adding a target for them in your Dockerfile. This way, as you are making changes and rebuilding locally, you can run the same unit tests you would run in the CI on your local machine using a simple command.
- Once you build docker image, you deploy it e.g Amazon EC2 container supports Docker images  

CI/CD Pipeline
CI
- Build 
- Unit tests
- Inegration Tests
CD
- Review
- Staging 
- Production

### Benefits of CI/CD
- Reduce cost
- Faster release rate
- Smaller code changes
- Fault isolations
- More test reliability
- Increase team transparency and accountability
- Easy maintenance and updates