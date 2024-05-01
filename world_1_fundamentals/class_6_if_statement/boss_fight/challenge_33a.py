'''
Develop a program that reads three numbers and shows which is the largest and which is the smallest

'''

firstNumber = int(input("\nWelcome to the CiV Labs!\n\nThis is the Largest Number & Smallest Number Checker\n\nEnter the first number: "))
secondNumber = int(input("\nEnter the second number: "))
thirdNumber = int(input("\nEnter the third number: "))

largestNumber = firstNumber

if secondNumber > firstNumber and secondNumber > thirdNumber:
    largestNumber = firstNumber
if thirdNumber > firstNumber and thirdNumber > secondNumber:
    largestNumber = thirdNumber

smallestNumber = firstNumber
if secondNumber < firstNumber and secondNumber < thirdNumber:
    smallestNumber = secondNumber
if thirdNumber < firstNumber and thirdNumber < secondNumber:
    smallestNumber = thirdNumber

print(f"The largest number is {largestNumber} and the smallest number is {smallestNumber}.")
