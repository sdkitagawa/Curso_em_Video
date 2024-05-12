'''
Develop a program that reads two integers and compares them, displaying a message on the screen:

- The first number (`number_here`) is greater!
- The second number (`number_here`) is greater!
- There's no greater one, both are equal.

'''

first_number = int(input("\nWelcome to the CiV Labs\n\nThis is the Integer Comparator\nPlease enter the first number: "))
second_number = int(input("\nAlright! Now, enter the second number: "))

if first_number == second_number:
    print(f"There's no greater one, both are equal.")
elif first_number > second_number:
    print(f"\nThe first number ({first_number}) is greater!")
else:
    print(f"\nThe second number ({second_number}) is greater!")
