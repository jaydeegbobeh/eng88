# We have built in Modules that we can find on Python's Library
## https://docs.python.org/3/py-modindex.html

## e.g Math modules: if the value is 1.49 floor(1.49) = 1, ceil(1.51) = 2

# There is a keyword called *import* : calls modules

# import random
# print(random.random()) # generates a random number
#
# from random import random # from module random import class: random
# print(random())

# import math
# num1 = 23.66
# print(num1)
# print(math.ceil(num1)) # rounds up to 24
# print(math.floor(num1)) # rounds down to 23

# task generate random number, if >= .50 use ceil if <= .49 use floor

from random import random
import math


random_num = (random())
print("This is randomly generated", str(random_num))
if random_num >= 0.5:
    print("This is the value with math.ceil", str(math.ceil(random_num)))
else:
    print("This is the value with math.floor", str(math.floor(random_num)))

# is instance for numbers greater than 1 e.g 13.567


# what is the use case
# os, sys are used to get information about your localhost/you machine such as name, path

import os, sys

working_directory = os.getcwd()
print("This is your current working directory", working_directory)

system_path = sys.path
print("This is your path", str(system_path))

# def current_system_path():
#     print("This is your current path")
#     return sys.path
# print(current_system_path())
#
# def current_working_dir():
#     print("This is your current working directory")
#     return os.getcwd()
# print(current_system_path())

import os, sys, datetime, math
print(os.cpu_count())
print(datetime.datetime.today())  # prints date a time according to OS

# % remainder value
print(math.remainder(25, 7)) # returns the remainder of dividing the left hand operand by the right hand operand
#
# print(math.pi)  # prints pi to 16 significant figures


def add(num1, num2):
    return num1 + num2

# Syntax lambda arguments : expression

addition = lambda num1, num2: num1 + num2 # calculating the expression

print("value returned by add() function")
print(add(2, 2))
print(addition(101, 25))