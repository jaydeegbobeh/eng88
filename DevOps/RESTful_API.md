# REST (Representation State Transfer) API/ RESTful Services
- An architectural style for apps
- Primarily used to build web services that are lightweight, maintainable and scalable
- REST is not dependent on any protocol
- But most RESTful services use HTTP as its underlying protocol

A RESTful service should be: easy to implement, maintainable, extensible and scalable.

## Properties

- **Representation and data flow**
	- First step is to define data sources
	- e.g JSON, XML
- **HTTP Messages and verbs**
	- HTTP is the protocol of internet communication
	- HTTP works on the simple methodology of a request/ response sytem.
		- There is a Request and Response structure

|HTTP - request sturcture|
|------------------------|
|Vendor                  |
|02 42 90                


HTTP verbs
- GET: read
- POST: create
- PUT: update/ replace
- PATCH: update/ modify
- DELETE: delete

- **URI's & Naming Resources**
	- Naming resources is key in regards to the R - representational part of REST
	- Expose customer databases to partners and third parties
		- http://ourservice/customer/1
		- OR http://ourservice/customer?id=1
{
"ID" : "1",
"firstname" : "Joe"
"surname" : "Bloggs"
"email" : "joe.b@gmail.com"

- **Statelessness**
	- Statelessness means that the RESTful service doesn't maintan the state of a previous request, it treats every call as a new request
	- http://ourservice/customer/1 
	- http://ourservice/customer/2
	- These calls are totally separate and will return customer 2 details without considering customer 1
	- Authentication is a token in stateless API - this token can be used to access multiple servers but in stateful API it saves your authentication to one server and you can't access other servers.
	- In a **stateful** service: 
		- http://ourservice/customer/1
		- http://ourservice/nextcustomer
- ****

## Converting Calculator app to a Web app

Shell commands
- python -m venv env
- source env/bin/activate

[calc_functions.py]()
```python
from flask import Flask, request, abort
import calculator.calc_functions as calc_functions

def read_number(number_id):
    number = input("Please enter an int number {}:".format(number_id))
    return int(number)

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the calculator app."

@app.route('/add/<int:number1>/<int:number2>')
def perform_add(number1, number2):
    return calc_functions.add(number1, number2)
    return str(number3)

# e.g URL http://127.0.0.1:5000/add?num1=1&num2=2
# e.g URL http://127.0.0.1:5000/add?num1=J&num2=I - 404 not found
# in shell command: curl "URL"

@app.route('/add')
def perform_add_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(404)

    number3 = calc_functions.add(number1, number2)
    return str(number3)

@app.route('/subtract')
def perform_subtract_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(404)

    number3 = calc_functions.subtract(number1, number2)
    return str(number3)

@app.route('/multiply')
def perform_multiply_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(404)

    number3 = calc_functions.multiply(number1, number2)
    return str(number3)

@app.route('/divide')
def perform_divide_query():
    number1 = request.args.get('num1', type=int)
    number2 = request.args.get('num2', type=int)

    if number1 is None or number2 is None:
        abort(404)

    number3 = calc_functions.divide(number1, number2)
    return str(number3)
```


Bridged network? -adapter

changed network settings
sudo ip link set dev eth0 down
sudo ip link set dev eth0 up

docker run -p 5000:5000 jaydeegb23/web-calculator
docker run -p 5000:5000 jaydeegb23/web-calculator