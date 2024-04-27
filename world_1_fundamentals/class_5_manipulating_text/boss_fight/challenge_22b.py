'''
Develop a program that reads a person's full name and displays it:

- The name with all uppercase letters

- The name with all lowercase letters

- How many letters in total (excluding spaces).

- How many letters are in the first name.

'''

print("\nWelcome to the CiV Labs!\nThis is the \"Know Your Name\" Tool\nThis Software is going to display the user Full Name in lowercase, uppercase, the amount of letters in total and how many letters are on the first name.")
userFullName = str(input("Please insert your full name: "))
print(f"This is your full name in uppercase: {userFullName.strip().upper()}\nThis is your full name in lowercase: {userFullName.strip().lower()}\nThis is the amount of letters in your name: {len(userFullName) - userFullName.count(" ")}")
stringSplitter = userFullName.split()
print(f"Your first name is {stringSplitter[0]} and the amount of letters in your name is {len(stringSplitter[0])} ")
