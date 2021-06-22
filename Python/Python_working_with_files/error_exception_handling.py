### `try`, `except` and `finally` block of codes
# They as if and else block

# create a function called greetings
# def greeting():
#     pass
#
# name = "devops"
# year = 2021
# print(name + year)  #type error you cannot add str and int
#
# file = open("order.txt") #filenotfound error no such file or directory

# try:
#     file = open("order.txt")
# except FileNotFoundError as errmsg:
# # creating aliases
#     # raise
#     print("order.txt not found", errmsg )
#
# finally:
#     print("Thank you for visiting hope to see you again!")

# The finally block will always be executed, no matter if the try block raises an error

# # second iteraction
# def open_using_with_and_print(file):
#
#     try:
#         with open("order.txt") as file:
#             for line in file.readline():
#                 print(line.rstrip('\n'))
#     #try code block ends
#     except FileNotFoundError as errmsg:
#         print("Sorry file not found")
#
#     finally:
#         print("Thank you for visiting hope to see you again!")
#
# print(open_using_with_and_print("order.txt"))

# task
def open_with_to_write_to_file(file):
    try:
        with open("order.txt", 'a') as file:
            file.write("\nPizza\nCake\nAvocado\nBiriyani\nPasta")
    except FileNotFoundError as errmsg:
        print("Sorry file not found")

    finally:
        print("Thank you for visiting hope to see you again!")

open_with_to_write_to_file('order.txt')
