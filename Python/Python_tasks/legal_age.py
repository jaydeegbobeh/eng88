leave = True
while leave != "exit":
    age = int(input("Please enter your age:\n"))
    driver_license = input("Do you have a driving license?\nEnter Y/N: ")
    if age < 16:
        print("You're too young, go back to school!")
    elif age < 17:
        if driver_license.upper == "Y":
            print("You can't be under 17 with a license, please try again")
    elif age >= 18:
        if driver_license.upper == "Y":
            print("You can vote and drive!")
        else:
            print("You can vote!")
    elif age >= 17 and driver_license.upper == "Y":
        print("You can drive!")
    elif 16 <= age <= 17:
        print("You can't legally drink yet, but if your mates/uncles might have your back!")
    leave = input("If you would like to exit, type 'exit'. To continue, press any key\n")
    if leave == 'exit':
        print('Thank you, goodbye.')


