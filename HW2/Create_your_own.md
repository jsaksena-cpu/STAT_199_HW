# Part 5: Dice Roulette
## The homework question

Write a program called dice_roulette.py that plays a simple dice game.

Roll two six-sided dice using random.randint().
Ask the player to guess a total from 2 to 12, or to type doubles. Any capitalization of doubles should work.
Print the two dice, then print the result:
If the player guessed doubles, they win if both dice match. Otherwise they lose.
If the player guessed a total, they win if the dice add up to that number. Otherwise they lose.
Jackpot: if the player guessed the right total and the dice match, print JACKPOT! instead of a normal win. For example, guessing 8 and rolling 4 and 4 is a jackpot, but guessing 8 and rolling 5 and 3 is a normal win.
If the player guesses a number below 2 or above 12, print an error message instead of showing the dice.

Use if, elif, and else to decide the result. You can assume the player types either a whole number or the word doubles.

What this question assesses

This question tests whether a student understands that an if/elif/else chain only runs the first branch that is true. The jackpot is the tricky part: rolling 4 and 4 on a guess of 8 is both "the right total" and "the right total with doubles." If the student checks for the right total first, the program prints You win! and never reaches the jackpot. There's no error message, so the student has to notice the wrong output on their own. To get it right, they have to put the more specific condition first. The question also tests reading input as a string and only converting it to a number with int() when the player didn't type doubles.