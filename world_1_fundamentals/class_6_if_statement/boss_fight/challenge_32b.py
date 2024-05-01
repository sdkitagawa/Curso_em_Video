'''
Develop a program that reads any year and shows whether it is a leap year.

'''

yearInput = int(input("\nWelcome to the CiV Labs!\n\nThis is the Leap Year Checker\n\nInsert the year number: "))

if yearInput % 4 == 0 and yearInput % 100 != 0 or yearInput % 400 == 0:
    print(f"\nThe year of {yearInput} it is a leap year.")
else:
    print(f"\nThe year of {yearInput} it isn't a leap year.")
