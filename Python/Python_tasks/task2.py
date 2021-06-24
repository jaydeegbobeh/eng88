# age = 24
# name = "Jaydee"
# year = 2021 - age
# print("OMG", name, "you are", age, "years old so you were born in", year)


name = input("What is your name? : ")
age = input("How old are you? - Please enter integer! : ")
year = 2021 - int(age)
print("OMG", name, "you are", age, "years old so you were born in", year)

wrong_year = input("Is this the correct year? enter Y/N : ")
if wrong_year == "N":
    year +=1
    print("OMG", name, "you are", age, "years old so you were born in", year)
elif wrong_year != "Y" and "N":
    raise Exception("Please enter Y or N")
else:
    print("Great, thanks!")



