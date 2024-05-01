'''
Develop a program that reads an integer and shows on the screen whether it is EVEN or ODD.

'''

numberInput = int(input("\nWelcome to the CiV Labs!\n\nThis is the Even or Odd Checker\n\nEnter a number: "))
checkOperation = int(numberInput % 2)

if checkOperation == 0:
    print(f"The number {numberInput} is even!")
else:
    print(f"The number {numberInput} is odd")
