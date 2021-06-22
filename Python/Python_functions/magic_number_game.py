import random
# random library allows you to pick a random number in a given range, pick a random element from a list, flip a coin
play = True
while play != "exit":
    print("Welcome to the Magic Number Game")
    (max_num) = (input("Please enter the highest number that can be used to generate a random number:\n"))
    random_num = random.randint(1,max_num)
    guess_1 = int(input("Please enter your first guess:\n"))
    if guess_1 == random.randint(1, max_num):
        print("Wow! You guessed the Magic Number on your first try!")
    elif guess_1 < random.randint(1, max_num):
        print("Too low :( please try again")
    elif guess_1 > random.randint(1, max_num):
        print("Too high :( try again")
    guess_2 = int(input("Please enter your second guess:\n"))
    if guess_2 == random.randint(1, max_num):
        print("Yay! You guessed the magic number")
    else:
        print("Please try again, you have one guess remaining.")
    guess_3 = int(input("Please enter your final guess:\n"))
    if guess_3 == random.randint(1, max_num):
        print("Third time's a charm! You guessed the Magic Number!")
    else:
        play = input("If you would like to play again, enter any key.\n Otherwise enter 'exit'\n")
        if play == "exit":
            print("Thank you for playing")


#here's how many times you guessed correctly:\nGoodbye")
# if str(max_num) or str(guess_1) or str(guess_2) or str(guess_3) == "exit":
# #print

# print(random.randint(1, max_num))
