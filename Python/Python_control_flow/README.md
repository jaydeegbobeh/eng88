# Control flow
## control flow is very important in all programming languages:
### controls the flow of your conditions and decisions


#### Control flow with if, elif and else 
Every if-elif statement is followed by a condition.
If the condition evaluates as True, then the code in that block gets executed.
Once the code in any of the block is executed, the control flow moves out of the if-elif-else block.
If none of the conditions are True, then the else block code is executed
```
num = 10
if num < 20:
    print("This number is less than 20")
else:
    print("This number is not less than 20")
```
```
weather = "sunny"

if weather == "sunny":  # if this condition is true, execute the next line of code
    print("Enjoy the weather")
elif weather == "rainy":
    print("Bring an umbrella!")


```

####  For Loops
A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
```
list_data = [1, 2, 3, 4, 5]
 print(list_data)
 for list in list_data:       # for value in list_data, iterate through list and print each value
     print(list)
 student_1 = {
     "name": "Jaydee",
     "key": "value",
     "stream" : "Cyber Security", #str
     "completed_lessons": "3",  #int
     "completed_lessons_names": ["variables", "operators", "data collections"]
 }
 
for data in student_1:
    print(data)

for data in student_1.values():
    print(data)    #prints all values

for data in student_1.keys():
    print(data)  #prints keys

for data in student_1.values():
    if data == "value":
        break
    print(data)    #stops before key:value, prints "Jaydee"
```
#### While loops
With the while loop we can execute a set of statements as long as a condition is true.
```
user_prompt = True
while user_prompt:
    age = input("Please enter you age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits")
print(f"Your age is {age}")
```
