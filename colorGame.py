#This is my main code.

import random

randomNumber = random.randint(1,10)

print ("Color games is now beginning! Try your wit and lets see how many times it takes you to guess...")

guess = int(input("enter a number between 1 and 10: "))

while randomNumber != guess:

    if guess < randomNumber:
        print ("Too low")
        guess = int(input("Guess again: "))

    elif guess > randomNumber:
        print ("too high")
        guess = int(input("Guess again?: "))

print ("You guessed it. You win!")