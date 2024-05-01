'''
Develop a software that makes the computer "think" between 0 and 5 and asks the user to try to find out which number the computer has chosen.

The program should write on the screen whether the user has won or lost.

'''

from random import randint

randomNumber = randint(0, 5)
userGuess = int(input("\nWelcome to the CiV Labs!\n\nThis is a Guess game!\n\nTry to guess what was the number that your computer has chosen: "))

if userGuess > 5:
    print("The number can't be higher than 5!")
else:
    if randomNumber == userGuess:
        print("\nYou guessed the correct number! You won!")
    else:
        print(f"\nYou guessed the incorrect number! My number was {randomNumber}! You lost ~")
