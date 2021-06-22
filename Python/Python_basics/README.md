# Python

## Python installation: 3.7 and later

### Pycharm set up

#### Documentation with README.md to store on Git-hub
-Testing the python env 'print("hello world")'

Why is Python used in DevOps?
  - Its flexibility and accessibility make python a great fit
  - You can build web applications, data visualizations...
  - Python is one of the best scripting languages, the vast variety of python libraries allows us to write scripts for the improved development life cycle
  - Understanding Python means you can apply security measures
  - Python OOP's can be translated to other languages, understanding concept is important

## Variables

- What are variables?
  - Variables work as a place holder to store data.

- str, bool, int, floats
  - "is considered as a String"
  - boolean is True/False
  - numbers are ints
  - decimals are floats
 

```python
first_name = "Jaydee" #string

last_name = "Gbobeh" #string

print(first_name)
print(last_name)

salary = 1000000 #int
DOB = "18/02/1997"


```

- input
```python
print("Please enter your name  ")
name = input("")
print("Hello", name)
```

## Operators

### Arithmetic Operators `# + - * / %`
| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| + | add two operands (variables) together| X + y + 2 |
| - | subtract two operands (variables) | X - y - 2 |
| * | multiply two operands (variables) | X - y - 2 |
| / | divide two operands (variables) | X - y - 2 |
| % | Modulus - remainder of the division of left operand by the right | X - y - 2 |
| + | add two operands (variables) together| X + y + 2 |

### Comparison Operators `> < == != >= <=`

| Operand | Description | Example |
|:---------: |:----------------------------: |:--------: |
| > | True if left operand is greater than the right| x > y |
| < | True if left operand is less than the right| x < y |
| == | True if both operands are equal | x == y |
| != | True if both operands are equal | x != y |
| >= | True if left operand is greater than or equal to the right| x >= y |
| <= | True if left operand is less than or equal to the right| x <= y |
```
value1 = 6
value2 = 7

print(value2 > value1) # is value2 greater than value1? Returns boolean - true
print(value1 > value2) # false
print(value1 + value2) # adding the values = 13
print(value1 - value2) # subtracting values = -1
print(value1 >= value2) # false
print(value1 != value2) # true
```
#### There built in methods available in python that give us boolean outcomes as well
```
Name = "Jaydee"
```
#### .isalpha() # checks if the value is alphabetical
```
print(Name.isalpha()) # returns the boolean outcome -true
```
#### Casting - turn age value into string
```
Age = 2
print(str(Age).isalpha()) # false

print(Name.isdigit()) # false

print(Name.startswith("J")) # true
```
