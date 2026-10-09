"""
Dice Roulette: guess the total of two dice, or guess that they'll be doubles.
"""

import random

die_1 = random.randint(1, 6)
die_2 = random.randint(1, 6)
total = die_1 + die_2

guess = input("Guess a total from 2 to 12, or type 'doubles': ").lower()

if guess == 'doubles':
    print(f"You rolled {die_1} and {die_2}.")
    if die_1 == die_2:
        print("You win!")
    else:
        print("You lose.")
else:
    number = int(guess)
    if number < 2 or number > 12:
        print("Invalid guess! Pick a total from 2 to 12.")
    else:
        print(f"You rolled {die_1} and {die_2}.")
        if number == total and die_1 == die_2:
            print("JACKPOT!")
        elif number == total:
            print("You win!")
        else:
            print("You lose.")
