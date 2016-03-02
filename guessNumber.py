'''
We're creating a guess a number game.
'''
import random


name = raw_input("Hello and welcome! In this game, you are going to attempt to guess the number I am thinking of. To begin, please tell me your name: ") #player imports their name as a string
secretNumber = random.randint(1,20) # a random number is created
print "Well " + name + ", I'm thinking of a number between 1 and 20. Can you guess this number within 6 tries?"

#begin guessing

for guessTaken in range(1,7):
    guess = int(raw_input( "Take a guess. "))
    if guess > secretNumber:
        print "Sorry, " + str(guess) + " is too HIGH. You have " + str(6-guessTaken) + " guesses remaining."
    elif guess < secretNumber:
        print "Sorry, " + str(guess) + " is too LOW. You have " + str(6-guessTaken) + " guesses remaining."
    elif guess == secretNumber:
        break #this is the correct guess, we continue to the end of the game.

if guess == secretNumber:
    print "Good job " + name +"!!!! " + str(guess) + " is the correct number!"
else:
    print "Sorry " + name + ", the number I was thinking of was " + str(secretNumber) +". I hope you try again!"
