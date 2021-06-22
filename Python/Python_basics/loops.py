import random

game_random_number = random.randint(1, 100)
game_active = True

while game_active:
    game_start_message = "guess a number between 1-100"
    user_guess = input()
    if user_guess == game_random_number:
        print("you guessed correctly")
    elif user_guess < game_random_number:
        print("too low, guess again")
    else:
        print("too high, guess again")
