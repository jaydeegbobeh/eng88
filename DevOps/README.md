# Devops
## IT before DevOps
- Software Develpoment Team
- Wall Team - space inbetween representing confussion misalignment and stress
- Quality Assurance Team
- System Engineering Team

## Application Design Patterns
- Monolith 
Traditional unified model for the design of a software program, software is composed all in one piece.
- Front and back end
Separates the concerns between the visual elements of the app that the user will interact with (front end) and the building of the structure of the app (back end).
- Microservice
Consists of a collection of small, autonomous service, each service is self-contained.
- Advantages	
	- Microservices are deploy independently => easy to manage bus fixes and feature releases
	- Compared to monolithic application, code dependencies can become tangled adding a new feature requires editing code in many places, in a microservice you dont share code or data stores minimising dependencies making it much easier to add new features.
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