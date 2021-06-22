# Object Oriented Python

## The four pillars of OOP are:
- **Encapsulation**
    - using OOP in python, you can restrict access to methods and variables, preventing data from direct modification
    - __dob = 18/02/1997  underscore restricts this data

- **Polymorphism**
    - Variables, functions and objects can exist in multiple forms
        - a method or subclass can define its behaviours and attributes whilst retaining some of the functionality of its parent class 
- **Inheritance**
    - Inheritance allows us to define a class that inherits all the methods and properties from another class
        - Parent class: the class being inherited from
        - Child class is the class that inherits from another class
- **Abstraction**
    - abstraction focuses on hiding the internal implementations of a process or method from the user
        - The user knows what they are doing but not how it's done



## Modules

We have built in Modules that we can find on Python's Library
https://docs.python.org/3/py-modindex.html

There is a keyword called **import** : calls modules

**random** module
```
print(random.random()) # generates a random number

from random import random # from module random import class: random
print(random())

import math
num1 = 23.66
print(num1)
print(math.ceil(num1)) # rounds up to 24
print(math.floor(num1)) # rounds down to 23
```
```
from random import random
import math


random_num = (random())
print("This is randomly generated", str(random_num))
if random_num >= 0.5:
    print("This is the value with math.ceil", str(math.ceil(random_num)))
else:
    print("This is the value with math.floor", str(math.floor(random_num)))
 ```
```
# what is the use case
# os, sys are used to get information about your localhost/you machine such as name, path

import os, sys

working_directory = os.getcwd()
print("This is your current working directory", working_directory)

system_path = sys.path
print("This is your path", str(system_path))
```
```
import os, sys, datetime, math
print(os.cpu_count())
print(datetime.datetime.today())  # prints date a time according to OS
```
```
# % remainder value
print(math.remainder(25, 7)) # returns the remainder of dividing the left hand operand by the right hand operand
```
```
def add(num1, num2):
    return num1 + num2
```
### Lambda
Syntax **arguments : expression**
#### A lambda function is a small anonymous function, it can take any number of arguments but can only have one expression
```
addition = lambda num1, num2: num1 + num2 # calculating the expression

print("value returned by add() function")
print(add(2, 2))
print(addition(101, 25))
```

**A method is a function in a class**


### Create Animal class
Use pass when you have to create a class but don't know yet what functions, variables you would like to place inside
```
class Animal:

    def __init__(self): # self refers to this class
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "nom nom nom"

    def move(self):
        return "moving all around the world"

# create an object of our Animal class
cat = Animal() # create an object of our Animal class called cat
print(cat.breathe()) # breathe for cat is abstracted
```
**Inheritance**
```
# creating a reptile class to Inherit everything from Animal class

from animal import Animal

class Reptile(Animal):

    def __init__(self):
    #we have a key word called super which inherits everthing from parent class at the time of initialisation of this class
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None
        self.heart_chambers = [3, 4]

    def seek_heat(self):
        return "it's rainy and windy, where is the sun?"

    def hunt(self):
        return "keep hunting for food until you get it"

    def use_venom(self):
        return "if I've got it I'm using it"


# create an object of Reptile 
classreptile_object = Reptile()
print(reptile_object.hunt()) # this function is from Reptile class
print(reptile_object.eat()) # this function is inherited from Animal parent class
```

**Encapsulation and Polymorphism**
```
class Python(Snake):
    def __init__(self):

        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        return "yum yum yum"

    def climb(self):
        return "up we go"

    def shed_skin(self):
        return "Time to refresh"

python_object = Python()
dog_object = Python()
print(dog_object.eat())

print(python_object.climb()) # method from Python class
print(python_object.use_tongue_to_smell()) # method from Snake class
```