'''
Develop a program that reads the year of birth of a young person and reports it according to their age:

- Whether they are yet to enlist in military service;
- If it's time to enlist;
- If the time for enlistment has passed.

Your program should also show how much time is left or when the deadline has passed.

'''

birth_year = int(input("\nWelcome to the CiV Labs\n\nThis the Military Enlistment Software!\nPlease insert your year of birth: "))
current_year = int(input("\nNow, please insert the current year: "))

user_age = current_year - birth_year
time_left = birth_year - current_year
has_passed = user_age - 18
time_to_enlist = birth_year + 18
early_enlistment = user_age - 18


if user_age > 18:
    print(f"\nUnfortunately it's too late for you to enlist! Your deadline has already passed {has_passed} year ago.")
elif early_enlistment < 18:
    print(f"\nIt's not time for your enlistment yet, there are {time_left} years left to go.")
else:
    print(f"It's your year! We are in {current_year}! Time to enlist!")
