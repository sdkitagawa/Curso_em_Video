'''
Develop a program that reads the year of birth of a young person and reports it according to their age:

- Whether they are yet to enlist in military service;
- If it's time to enlist;
- If the time for enlistment has passed.

Your program should also show how much time is left or when the deadline has passed.

'''

from datetime import date

birth_year = int(input("\nWelcome to the CiV Labs\n\nThis the Military Enlistment Software!\nPlease insert your year of birth: "))
user_age = date.today().year - birth_year

if user_age > 18:
    print(f"\nUnfortunately it's too late for you to enlist! Your deadline has already passed {user_age -18} year ago.")
elif user_age < 18:
    print(f"\nIt's not time for your enlistment yet, there are {18 - user_age} years left to go")
else:
    print(f"It's your year! We are in {date.today().year}! Time to enlist!")
