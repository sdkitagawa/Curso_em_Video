'''
Develop a program that reads a person's name and tells you if they have "SILVA" in their name.

'''

print("\nWelcome to the CiV Labs!\n\nThis is the Silva Checker Software!\nYou might be thinking, what the heck is the SILVA Checker?\nThe answer is very simple, it is a program to check if the name entered has the word \"SILVA\"\n\n")
fullName = str(input("Enter the full name of a person: ")).upper().strip()

print(f"Is there any occurrence of \"Silva\"'s name being found on the name entered by the user: {"SILVA" in fullName}")
