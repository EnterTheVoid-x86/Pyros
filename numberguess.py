# Number guessing game
print ("I'm thinking of a number between 1 and 10.")
print ("You have 5 tries to guess it.")
import random
number = random.randint(1, 10)
tries = 5
while tries > 0:
    guess = int(input("Guess: "))
    if guess == number:
        print ("You win!")
        break
    elif guess > number:
        print ("Your guess is too high.")
    elif guess < number:
        print ("Your guess is too low.")
    tries -= 1
    if tries == 0:
        print ("You lose!")
        print ("The number was {}.".format(number))
        break

