'''
Develop a program that reads any integer and asks the user to choose the conversion base:

- Binary;
- Octal;
- Hexadecimal.

'''

user_choice = int(input("\nWelcome to the CiV Labs! This is the Number Base Converter\n\nPlease choose an operation to convert your number based on the options listed down below:\n1 - Binary\n2 - Octal\n3 - Hexadecimal\n\nYour choice is: "))

if user_choice > 3:
    print("There's no such option. You must choose between \"1\" to \"3\"!")
else:
    converting_number = int(input("\nNow, enter the number you want to convert: "))

    if user_choice == 1:
        print(f"The number {converting_number} converted to a Binary number is {bin(converting_number)[2:]}")
    elif user_choice == 2:
        print(f"The number {converting_number} converted to an Octal number is {oct(converting_number)[2:]}")
    else:
        print(f"The number {converting_number} converted to a Hexadecimal number is {hex(converting_number)}")
