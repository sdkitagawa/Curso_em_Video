'''
The National Swimming Confederation needs a program that reads an athlete's year of birth and shows their category according to age:

- Up to 9 years old: Beginner;
- Up to 14 years old: Infant;
- Up to 19 years old: Junior;
- Up to 20 years old: Senior;
- Above: Master.

'''

birth_year = int(input("\nWelcome to the CiV Labs\n\nThis an Official Software for the Fake National Swimming Confederation!\nPlease, insert the athlete's year of birth: "))
current_year = int(input("\nNow, please enter the current year: "))

user_age = current_year - birth_year
beginner_level = "Beginner"
infant_level = "Infant"
junior_level = "Junior"
senior_level = "Senior"
master_level = "Master"

if user_age <= 9:
    print(f"\nThis athlete is {user_age} years old. So they're in the {beginner_level} category.")
elif user_age > 9 and user_age <= 14:
    print(f"\nThis athlete is {user_age} years old. So they're in the {infant_level} category.")
elif user_age > 14 and user_age <= 19:
    print(f"\nThis athlete is {user_age} years old. They're therefore in the {junior_level} category.")
elif user_age > 19 and user_age <= 20:
    print(f"\nThis athlete is {user_age} years old. They're thus in the {senior_level} category.")
else:
    print(f"\nThis athlete is {user_age} years old. Hence they're in the {master_level} category.")
