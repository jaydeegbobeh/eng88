# Working with files
## Error and Exception handling
`try`, `except` and `finally` block of codes
- They as if and else block

# create a function called greetings
```
def greeting():
    pass

name = "devops"
year = 2021
print(name + year)  #type error you cannot add str and int
```

```
file = open("order.txt") #filenotfound error no such file or directory

try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
# creating aliases
    # raise
    print("order.txt not found", errmsg )

finally:
    print("Thank you for visiting hope to see you again!")

# The finally block will always be executed, no matter if the try block raises an error
```
### Handling files - Reading files
- We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening

`open(file, mode)`

| Mode |Description|
| :----: |:---- |
|'r' |This is the default mode. It Opens file for reading. |
|'w' |This Mode Opens file for writing. If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x' |Creates a new file. If file already exists, the operation fails.|
|'a' |Open file in append mode. If file does not exist, it creates a new file.|
|'t' |This is the default mode. It opens in text mode.|
|'b' |This opens in binary mode.
|'+' |This will open a file for reading and writing (updating)|

```
# task add items to menu
def open_with_to_write_to_file(file):
    try:
        with open("order.txt", 'a') as file:
            file.write("\nPizza\nCake\nAvocado\nBiriyani\nPasta")
    except FileNotFoundError as errmsg:
        print("Sorry file not found")

    finally:
        print("Thank you for visiting hope to see you again!")

open_with_to_write_to_file('order.txt')
```