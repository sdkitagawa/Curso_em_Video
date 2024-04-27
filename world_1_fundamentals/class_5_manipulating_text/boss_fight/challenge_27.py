'''
Develop a program that reads a person's full name and then displays their first and last name separately.

Ex: Ana Maria de Souza
First name: Ana
Last name: Souza

'''

print("\nWelcome to the CiV Labs!\n\nThis is the \"I am Lord Voldemort\" Checker!\nThis software is going print out only your First and Last names separately\n\ni.e, Tom Marvolo Riddle\nFirst name: Tom\nLast name: Riddle\n")
fullName = str(input("Please enter a full name: ")).strip()

print(f"The name that you entered: {fullName}")

fullName = fullName.split()

print(f"First Name: {fullName[0]}\nLast name: {fullName[len(fullName) - 1]}")
