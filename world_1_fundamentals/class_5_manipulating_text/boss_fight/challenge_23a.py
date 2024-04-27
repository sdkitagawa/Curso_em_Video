'''
Develop a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.

Ex:

Type a number: 1834

Unit: 4
Tens: 3
Hundred: 8
Thousand: 1

Method: Variables, String Slicing

'''

print("\nWelcome to the CiV Labs\n\nThis is a program to check if the user input is between 0 and 9999 and then print out the result using a well organized formatting\nThis is how it is going to look like:\n\nUnit: Z\nTens: Y\nHundred: X\nThousand W\n")
numberInput = str(input("Enter a number starting from the minimum value of 0 and the maximum value of 9999: "))

print(f"Unit: {numberInput[3]}\nTens: {numberInput[2]}\nHundred: {numberInput[1]}\nThousand: {numberInput[0]}")
