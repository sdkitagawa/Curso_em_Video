'''
Create a program that makes the computer play Jankenpo with you.

'''

from random import randint
from time import sleep

user_choice = str(input("\nWelcome to the CiV Labs!\n\nThis is the Jankenpo Game!\nChoose between:\n\n1 - Rock\n2 - Paper\n3 - Scissors\n\nYour choice: "))



if user_choice == 1:
    print("Joooooo! ")
    sleep(1)
    print("keeeeeen")
    sleep(1)
    print("pan!")
elif user_choice == 2:
    print(f"Jooooookeeeeeenpan! ")
else:
    print(f"Jooooookeeeeeenpan! ")
