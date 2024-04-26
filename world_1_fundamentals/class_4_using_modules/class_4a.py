'''
Using Modules

How to import modules

import `module`
from `module` import `method`
'''

import math

userInput = int(input("Input a number: "))
squareRoot = math.sqrt(userInput)
print(f"The square root of {userInput} is {squareRoot}")
print(f"The square root of {userInput} rounded up is {math.ceil(squareRoot)}")
print(f"The square root of {userInput} rounded down is {math.floor(squareRoot)}")
