'''
Using Modules

How to import modules

import `module`
from `module` import `method`
'''

from math import sqrt, floor, ceil

userInput = int(input("Input a number: "))
squareRoot = sqrt(userInput)
print(f"The square root of {userInput} is {squareRoot}")
print(f"The square root of {userInput} rounded up is {ceil(squareRoot)}")
print(f"The square root of {userInput} rounded down is {floor(squareRoot)}")
