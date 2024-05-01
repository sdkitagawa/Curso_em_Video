'''
Develop a program that reads three numbers and shows which is the largest and which is the smallest

'''

firstNumber = int(input("\nWelcome to the CiV Labs!\n\nThis is the Largest Number & Smallest Number Checker\n\nEnter the first number: "))
secondNumber = int(input("\nEnter the second number: "))
thirdNumber = int(input("\nEnter the third number: "))
largestNumber = int(0)
smallestNumber = int(0)

if firstNumber > secondNumber:
    if firstNumber > thirdNumber:
        largestNumber = firstNumber
    else:
        largestNumber = thirdNumber
else:
    if secondNumber > thirdNumber:
        largestNumber = secondNumber
    else:
        largestNumber = thirdNumber

if firstNumber < secondNumber:
    if firstNumber < thirdNumber:
        smallestNumber = firstNumber
    else:
        smallestNumber = thirdNumber
else:
    if secondNumber < thirdNumber:
        smallestNumber = secondNumber
    else:
        smallestNumber = thirdNumber

print(f"The largest number is {largestNumber} and the smallest number is {smallestNumber}.")
