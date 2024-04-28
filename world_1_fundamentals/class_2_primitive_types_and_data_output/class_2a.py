'''
Primitive Types are basically the several variable types, e.g: int, float, bool and str

Int ➝ Integer: 7, -4, 0, 9875
Float ➝ Floating Point: 4.5, 0.076, -15.223, 7.0
Bool ➝ Boolean: True, False
Str ➝ String: "Hello", "7.5", ""

To check a primitive you can use the function "type()"
'''

firstNumber = int(input("Insert the first number: "))
secondNumber = int(input("Insert the second number: "))
operationAddition = firstNumber + secondNumber
print(f"The result of your addition between {firstNumber} and {secondNumber} is {operationAddition}")
#print("The result of your addition between {} and {} is {}".format(firstNumber, secondNumber, operationAddition))
#print("The result of your addition between {0} and {1} is {2}".format(firstNumber, secondNumber, operationAddition))
#print("The result of your addition between", firstNumber,"and", secondNumber,"is", operationAddition)
#print("The result of your addition is ", operationAddition)
#print("The result of your addition is {}.".format(operationAddition))

print(f"The primitive type of the variables used to build this software are: {type(firstNumber)}, {type(secondNumber)}, {type(operationAddition)}!")
#print("The primitive type of the variables used to build this software are: {}!".format(type(firstNumber), type(secondNumber), type(operationAddition)))
#print("The primitive type of the data used to build this software is: {}!".format(type(firstNumber)))
#print ("The primitive type of the data used to build this software is: ", operationAddition)
#print("The primitive type of the data used to build this software is: {}!".format(type(firstNumber)))
