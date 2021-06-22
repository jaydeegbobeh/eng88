# Control flow with if, elif and else - loops

# weather = "raining"
#
# if weather == "sunny":  #if this condition is true, execute the next line of code
#     print("Enjoy the weather") #if true this line will execute
# elif weather == "raining":
#     print("Remember to bring an umberella!")
# elif weather == snowing:
#     print("Wrap up warm!")
# else:
#     print("Oops sorry something went wrong ...please try again") # if false it will execute the next line
#
#
# # Loops are used to ITERATE through data
# #
# list_data = [1, 2, 3, 4, 5]
# print(list_data)
# for list in list_data:       # for value in list_data, iterate through list and print each value
#     print(list)
#
# for list in list_data:
#     if list == 3:
#         print("I found 3")
#     if list == 2:
#         print("now I found 2")
#     if list == 5:
#         print("this is 5 and I have found it as well")
#     else:
#         print("try again")
#
#
# # looping through dictionaries
#
# student_1 = {
#     "name": "Jaydee",
#     "key": "value",
#     "stream" : "Cyber Security", #str
#     "completed_lessons": "3",  #int
#     "completed_lessons_names": ["variables", "operators", "data collections"]
# }
#
# for data in student_1:
#     print(data)
#
# for data in student_1.values():
#     print(data)    #prints all values
#
# for data in student_1.keys():
#     print(data)  #prints keys
#
# for data in student_1.values():
#     if data == "value":
#         break
#     print(data)    #stops before key:value, prints "Jaydee"


#While loops

user_prompt = True
while user_prompt:
    age = input("Please enter you age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits")
print(f"Your age is {age}")
