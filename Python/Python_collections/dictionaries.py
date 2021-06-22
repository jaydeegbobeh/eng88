# What are dictionaries?
# Dictionaries are structures as KEY = VALUE
# VALUE = str, int, list
## Syntax {}

student_1 = {
    "name": "Jaydee",
    "key": "value",
    "stream" : "Cyber Security", #str
    "completed_lessons": "3",  #int
    "completed_lessons_names": ["variables", "operators", "data collections"] #list

}

print(student_1)
print(student_1["name"])  #fetch value with key
print(student_1["stream"])
print(student_1["completed_lessons_names"])

#display only OPERATORS from the list inside dictionary
print(student_1["completed_lessons_names"][1]) #name of dict followed by the key then the index of the value you want

print(student_1.keys()) #return keys
print(student_1.values()) #return values