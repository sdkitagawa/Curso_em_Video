'''
Arithmetic Operators

+  ➝ Addition
-  ➝ Subtraction
*  ➝ Multiplication
/  ➝ Division
** ➝ Exponentiation
// ➝ Floor division: Integer rest of a division
%  ➝ Modulus: Rest of a division

Order of Precedence (Order of Priority)

1 ➝ ()
2 ➝ **
3 ➝ * ➝ / ➝ // ➝ %
4 ➝ + ➝ -
'''

userName = input("What's your name: ")

# Printing your name but having 20 characters (filling the not used characters by the letters with spaces) on the left side
print(f"Nice to meet you {userName:>20}")

# Printing your name but having 20 characters (filling the not used characters by the letters with spaces) on the right side
print(f"Nice to meet you {userName:<20}")

# Printing your name but having 20 characters (filling the not used characters by the letters with spaces) on center
print(f"Nice to meet you {userName:^20}")

# Printing your name but having 20 characters (filling the not used characters by the A letters instead of spaces)
print(f"Nice to meet you {userName:A^20}")

numberOne = int(input("Type a number: "))
numberTwo = int(input("Type the second number: "))
operationAddition = numberOne + numberTwo
operationSubtraction = numberOne - numberTwo
operationMultiplication = numberOne * numberTwo
operationDivision = numberOne / numberTwo
operationExponentiation = numberOne ** numberTwo
operationFloor = numberOne // numberTwo
operationModulus = numberOne % numberTwo

print(f"Addition result is {operationAddition}, Subtraction result is {operationSubtraction}, Multiplication result is {operationMultiplication}, Division result is {operationDivision:.2f}, Exponentiation result is {operationExponentiation}, Floor result is {operationFloor}, Modulus result is {operationModulus}")
