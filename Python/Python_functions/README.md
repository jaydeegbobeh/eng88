# Functions
## DRY - DON'T REPEAT YOURSELF

A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

**Syntax**
def function_name():

```
# first iteration

def greetings():
    return "Welcome to Cyber Security!"
print(greetings)

# second iteration
def hello(name):
    return f"Hello how are you {name}"
print(hello(input("What is your name?:  ")))

def add(value1, value2):
    return value1 + value2    # once values are given, function add, adds values
print(add(2, 3))  # returns 5

def subtract(value1, value2):
    return value1 - value2    # once values are given, function subtract, subtracts values
print(subtract(9, 5))

def multiply(value1, value2):
    return value1 * value2    # once values are given, function multiply, multiplies values
print(multiply(101, 46))

def divide(value1, value2):
    return value1 / value2    # once values are given, function divide, divides value1 by value2
print(divide(4000, 20))
```
